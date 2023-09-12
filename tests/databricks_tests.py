import pytest

import tests.utilsz.secrets as sct
from johnsnowlabs import *
from johnsnowlabs.auto_install.databricks.install_utils import *


def assert_job_suc(state):
    assert state["state"]["result_state"] == "SUCCESS"


def run_endpoint_tests(test_cluster_id, host, token):
    import johnsnowlabs.auto_install.health_checks.endpoint_test as endp_test

    assert_job_suc(
        nlp.run_in_databricks(
            endp_test,
            databricks_cluster_id=test_cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="endpoint_creation_test_run",
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


@pytest.fixture()
def host_creds(host):
    if host == "aws":
        return aws_creds()
    elif host == "azure":
        return azure_creds()
    else:
        raise Exception("Unknown host")


@pytest.fixture()
def azure_gpu_node_type():
    return "Standard_NC4as_T4_v3"


@pytest.fixture()
def azure_cpu_node():
    return "Standard_DS3_v2"


@pytest.fixture()
def azure_creds():
    lic = sct.db_lic_azure
    host = sct.ckl_host_azure
    token = sct.ckl_token_azure
    return lic, host, token


@pytest.fixture()
def azure_trial_creds():
    lic = sct.azure_trail_lic2
    host = sct.azure_trail_host2
    token = sct.azure_trail_token2
    return lic, host, token


@pytest.fixture()
def aws_creds():
    lic = sct.ckl_lic_aws
    host = sct.ckl_host_aws
    token = sct.ckl_token_aws
    return lic, host, token


@pytest.fixture
def creds(request):
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize("creds", ["aws_creds", "azure_creds"], indirect=True)
def test_list_db_infos(creds):
    # List infos about the workspace
    lic, host, token = creds
    db_client = get_db_client_for_token(host, token)
    list_db_runtime_versions(db_client)
    list_node_types(db_client)
    list_clusters(db_client)


def test_endpoint(azure_trial_creds, azure_cpu_node):
    cluster_id = "0831-180255-dki33myd"
    lic, host, token = azure_trial_creds
    run_endpoint_tests(cluster_id, host, token)


def test_get_db_cluster_infos(aws_creds):
    # list infos specific to a cluster
    lic, host, token = aws_creds
    db_client = get_db_client_for_token(host, token)
    list_cluster_lib_status(db_client, cluster_id)
    pprint(db_client.cluster.get_cluster(cluster_id))


def test_create_fresh_cluster(azure_trial_creds, azure_cpu_node):
    # Create a fresh cluster
    lic, host, token = azure_trial_creds
    #
    # nlp.install(
    #     json_license_path=lic,
    #     databricks_host=host,
    #     databricks_token=token,
    #     hardware_platform="gpu",
    #     node_type_id="Standard_NC12s_v3",
    #     driver_node_type_id="Standard_NC6s_v3",
    #     spark_version="13.1.x-gpu-ml-scala2.12",
    #     visual=True,
    #     clean_cluster=False,
    # )
    #
    instance_type = azure_cpu_node
    # lic, host, token = aws_creds

    nlp.install(
        json_license_path=lic,
        databricks_host=host,
        databricks_token=token,
        driver_node_type_id=instance_type,
        node_type_id=instance_type,
    )


def test_create_fresh_cluster_and_run_checks(azure_trial_creds, azure_cpu_node):
    instance_type = azure_cpu_node

    lic, host, token = azure_trial_creds
    test_cluster_id = nlp.install(
        json_license_path=lic,
        databricks_host=host,
        databricks_token=token,
        visual=True,
        driver_node_type_id=instance_type,
        node_type_id=instance_type,
        hardware_platform="gpu",
        clean_cluster=False,
    )
    # test_cluster_id = "0829-125925-deug1ja1"
    run_cluster_test_suite(test_cluster_id, host, token)
    # TODO delete cluster


def test_create_fresh_cluster2(azure_creds, azure_cpu_node):
    instance_type = azure_cpu_node

    parameters = [{}, {}]

    for param in parameters:
        lic, host, token = azure_creds
        test_cluster_id = nlp.install(
            json_license_path=lic,
            databricks_host=host,
            databricks_token=token,
            visual=True,
            driver_node_type_id=instance_type,
            node_type_id=instance_type,
            spark_conf=param,
            # hardware_platform="gpu",
        )
        # test_cluster_id = "0829-125925-deug1ja1"
        start_time = time.time()

        run_cluster_test_suite(test_cluster_id, host, token)
        # TODO delete cluster

        end_time = time.time()
        print("Time taken: ", end_time - start_time)


def test_install_to_databricks():
    db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
    cluster_id = nlp.install(
        databricks_host=sct.ckl_host,
        databricks_token=sct.ckl_token,
    )


def test_submit_task_api_to_databricks():
    # Make cluster
    # cluster_id = nlp.install(json_license_path=sct.db_lic_by_jsl, databricks_host=sct.ckl_host,
    #                          databricks_token=sct.ckl_token)
    cluster_id = "1006-050402-4nsqdu8h"

    # Test script
    py_script = "/home/ckl/Documents/freelance/jsl/johnsnowlabs/johnsnowlabs/auto_install/health_checks/hc_test.py"
    assert_job_suc(
        nlp.run_in_databricks(
            py_script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Script test ",
        )
    )

    # Test String
    script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))
    """
    assert_job_suc(
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Python Code String Example",
        )
    )

    assert_job_suc(
        nlp.run_in_databricks(
            "print('noice')",
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Code String test 2",
        )
    )

    def nlu_func():
        import nlu

        medical_text = """A 28-year-old female with a history of gestational 
        diabetes presented with a one-week history of polyuria ,
         polydipsia , poor appetite , and vomiting ."""
        df = nlu.load("en.med_ner.diseases").predict(medical_text)
        for c in df.columns:
            print(df[c])

    assert_job_suc(
        nlp.run_in_databricks(
            nlu_func,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Function test",
        )
    )

    # Test String
    script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))
    """
    assert_job_suc(
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Python Code String Example",
        )
    )

    # Test Function
    def sample_submit_func():
        print("Test Function")

    assert_job_suc(
        nlp.run_in_databricks(
            sample_submit_func,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Function test",
        )
    )

    run_cluster_test_suite(cluster_id, sct.ckl_host, sct.ckl_token)


def test_hdfs_basic_methods():
    db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
    src_p = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/setup.py"
    target_p = "/johnsnowlabs/testf"
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p)
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "2")
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "3")
    pprint(dbfs_ls(db_client, "/johnsnowlabs"))
    dbfs_rm(db_client, target_p)
    pprint(dbfs_ls(db_client, "/johnsnowlabs"))


if __name__ == "__main__":
    unittest.main()
