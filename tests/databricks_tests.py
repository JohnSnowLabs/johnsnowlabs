from multiprocessing import Queue
from threading import Thread

import pytest

import tests.utilsz.secrets as sct
from johnsnowlabs import *
from johnsnowlabs.auto_install.databricks.install_utils import *
from tests.db_testing_utils import (
    assert_job_suc,
    run_endpoint_tests,
    run_cluster_test_suite,
    get_one_model_per_class,
    get_test_cluster,
    tester_thread,
)


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
def aws_cpu_node():
    return "i3.xlarge"


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


def test_get_db_cluster_infos(aws_creds):
    # list infos specific to a cluster
    lic, host, token = aws_creds
    db_client = get_db_client_for_token(host, token)
    list_cluster_lib_status(db_client, cluster_id)
    pprint(db_client.cluster.get_cluster(cluster_id))


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


def test_endpoints_multi_cluster(aws_creds, aws_cpu_node):
    n_clusters = 1
    n_parallel_jobs_per_cluster = 4  # todo add
    # 1) Create clusters
    # TODO try db_spark_version = "9.1.x-scala2.12" and otyhers!?
    # TODO there is some bug with cluster created from localhost! Gives errors... but db originated cluster not!
    # cluster_ids = [
    #     get_test_cluster(aws_creds, aws_cpu_node, n) for n in range(n_clusters)
    # ]
    cluster_ids = ["0913-161805-nlmmtquc"]

    # 2) Define job-queue
    job_que = Queue()
    one_model_per_class = get_one_model_per_class()
    for model in one_model_per_class:
        job_que.put(model)

    # Create a semaphore to limit parallelism per cluster

    # 3) For each cluster, start a tester-thread.
    # Threads take jobs from the queue and run them on the cluster till completion.
    lic, host, token = aws_creds
    threads = []
    results = {}
    for cluster_id in cluster_ids:
        t = Thread(
            target=tester_thread, args=(cluster_id, job_que, host, token, results)
        )
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # 4) Print results
    for model, result in results.items():
        print(f"Model {model}: {result}")

    # 5) Delete all clusters
    # for cluster_id in cluster_ids:
    #     delete_cluster(cluster_id)


def test_endpoint(aws_creds, aws_cpu_node):
    cluster_id = "0913-161805-nlmmtquc"
    cluster_id = get_test_cluster(aws_creds, aws_cpu_node, 0)

    lic, host, token = aws_creds
    run_endpoint_tests(cluster_id, host, token, "tokenize")
