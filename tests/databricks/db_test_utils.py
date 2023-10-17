import queue
import time

import pytest

from johnsnowlabs import nlp, settings
from johnsnowlabs.auto_install.databricks.install_utils import (
    cluster_exist_with_name_and_runtime,
    get_db_client_for_token,
    get_cluster_id,
    wait_till_cluster_running,
    _get_cluster_id,
)
from johnsnowlabs.auto_install.health_checks.generate_endpoint_test import (
    generate_endpoint_test,
)
from johnsnowlabs.utils.enums import DatabricksClusterStates
from tests.utilsz import secrets as sct


@pytest.fixture()
def azure_gpu_node_type():
    return "Standard_NC4as_T4_v3"


@pytest.fixture()
def azure_cpu_node():
    return "Standard_DS3_v2"


@pytest.fixture()
def aws_cpu_node():
    return "i3.xlarge"


@pytest.fixture()
def azure_creds():
    import tests.utilsz.secrets as sct

    lic = sct.db_lic_azure
    host = sct.ckl_host_azure
    token = sct.ckl_token_azure
    return lic, host, token


@pytest.fixture()
def azure_trial_creds():
    import tests.utilsz.secrets as sct

    lic = sct.azure_trail_lic2
    host = sct.azure_trail_host2
    token = sct.azure_trail_token2
    return lic, host, token


@pytest.fixture()
def aws_creds():
    import tests.utilsz.secrets as sct

    lic = sct.ckl_lic_aws
    host = sct.ckl_host_aws
    token = sct.ckl_token_aws
    return lic, host, token


@pytest.fixture
def creds(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def node_type(request):
    return request.getfixturevalue(request.param)


def host_creds(host):
    if host == "aws":
        return aws_creds()
    elif host == "azure":
        return azure_creds()
    else:
        raise Exception("Unknown host")


def assert_job_suc(state):
    assert state["state"]["result_state"] == "SUCCESS"


def run_endpoint_tests(test_cluster_id, host, token, model):
    # generate job.py script and submit it
    assert_job_suc(
        nlp.run_in_databricks(
            generate_endpoint_test(model, sct.container_lic_json),
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name=f"endpoint_creation_test_run_{model}",
        )
    )


def run_cluster_test_suite(test_cluster_id, host, token):
    # run test suite again a existing cluster

    # Test modules
    import johnsnowlabs.auto_install.health_checks.hc_test as hc_test
    import johnsnowlabs.auto_install.health_checks.ocr_test as ocr_test
    import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test

    assert_job_suc(
        nlp.run_in_databricks(
            nlp_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="nlp_test",
        )
    )

    assert_job_suc(
        nlp.run_in_databricks(
            hc_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="hc_test",
        )
    )

    assert_job_suc(
        nlp.run_in_databricks(
            ocr_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="ocr_test",
        )
    )


def get_one_model_per_class():
    # todo actually generate from spellbook
    return ["sentiment", "ner", "spell", "bert", "elmo", "albert", "roberta"]


def delete_all_test_clusters(db_client):
    for i in range(10):
        while _get_cluster_id(db_client, f"TEST_CLUSTER_{i}"):
            cluster_id = _get_cluster_id(db_client, f"TEST_CLUSTER_{i}")
            db_client.cluster.permanent_delete_cluster(cluster_id)
            print(f"Deleted cluster {cluster_id}")
            time.sleep(5)


def get_or_create_test_cluster(
    creds, node_type, n=0, runtime=None, clean_workspace=False
):
    """
    Creates a cluster with name TEST_CLUSTER_{n} and runtime runtime if it doesn't exist.
    If it exists, it checks if it's running and if not, it starts it.
    "exists" means another cluster with same name and runtime exists.
    """
    lic, host, token = creds
    # runtime = "9.1.x-scala2.12"
    if runtime is None:
        runtime = settings.db_spark_version
    cluster_name = f"TEST_CLUSTER_{n}"
    db_client = get_db_client_for_token(host, token)

    # 1) Check if cluster with name and correct runtime exists and it's running state If not, create it.
    if cluster_exist_with_name_and_runtime(db_client, cluster_name, runtime):
        cluster_id = get_cluster_id(db_client, cluster_name, runtime)

        status = DatabricksClusterStates(
            db_client.cluster.get_cluster(
                cluster_id,
            )["state"]
        )

        # if status is terminated, try restart it
        if status == DatabricksClusterStates.TERMINATED:
            db_client.cluster.start_cluster(cluster_id=cluster_id)
            wait_till_cluster_running(db_client, cluster_id)
            status = DatabricksClusterStates(
                db_client.cluster.get_cluster(
                    cluster_id,
                )["state"]
            )
        if status == DatabricksClusterStates.RUNNING:
            return cluster_id
        else:
            print(
                f"Could not find or start {cluster_name} with runtime {runtime} creating a new one"
            )

    else:
        #  no cluster exists, create new one
        cluster_id = nlp.install(
            spark_version=runtime,
            json_license_path=lic,
            databricks_host=host,
            databricks_token=token,
            driver_node_type_id=node_type,
            node_type_id=node_type,
            cluster_name=cluster_name,
            clean_cluster=clean_workspace,
            block_till_cluster_ready=True,
        )
        return cluster_id


def subtester_thread(cluster_id, job_que, host, token, results):
    while not job_que.empty():
        try:
            model = job_que.get_nowait()
        except queue.Empty:
            return
        try:
            run_endpoint_tests(cluster_id, host, token, model)
            print(f"{model} success!")
            results[model] = "SUCCESS"
        except Exception as e:
            print(f"{model} failed!")
            results[model] = f"FAILED: {str(e)}"


db_cloud_node_params = pytest.mark.parametrize(
    "creds, node_type",
    [
        ("aws_creds", "aws_cpu_node"),
        ("azure_creds", "azure_cpu_node"),
        # ("azure_creds", "azure_gpu_node_type"),
    ],
    indirect=["creds", "node_type"],
)
db_cloud_params = pytest.mark.parametrize(
    "creds",
    [
        "aws_creds",
        "azure_creds",
    ],
    indirect=["creds"],
)
