import json
from multiprocessing import Queue
from threading import Thread

from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.utils.enums import JvmHardwareTarget
from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    run_endpoint_tests,
    get_or_create_test_cluster,
    subtester_thread,
)


def log_and_get_failed_models(results):
    retry_models = []
    for model, result in results.items():
        print(f"Model {model}: {result}")
        if result["success"] is False:
            retry_models.append(model)
    return retry_models


def parallel_run(
    cluster_ids,
    n_parallel_jobs_per_cluster,
    models_to_test,
    host,
    token,
    results,
    test_type,
):
    # 3) For each cluster, start a tester-thread.
    # Start an extra thread for same cluster, for every parallel job run on cluster
    # Threads take jobs from the queue and run them on the cluster till completion.
    job_que = Queue()
    for model in models_to_test:
        job_que.put(model)
    threads = []
    for cluster_id in cluster_ids:
        for i in range(n_parallel_jobs_per_cluster):
            # Start 1 thread for every job that should run, for every cluster
            t = Thread(
                target=subtester_thread,
                args=(
                    cluster_id,
                    job_que,
                    host,
                    token,
                    results,
                    test_type,
                ),
            )
            threads.append(t)
            t.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()


# @pytest.mark.skip(reason="WIP")
@db_cloud_node_params
def test_endpoints_multi_cluster(creds, node_type):
    n_clusters = 1
    n_parallel_jobs_per_cluster = 2
    runtime = "9.1.x-scala2.12"
    lic, host, token = creds

    # 1) Create clusters
    cluster_ids = [
        get_or_create_test_cluster(creds, node_type, i, runtime=runtime)
        for i in range(n_clusters)
    ]

    # 2) Define models to test
    models_to_test = get_mm_models()  # [:3]
    models_to_test = ["tokenize"]
    # one_model_per_class = get_one_model_per_class()

    # 3) Start parallel-job-cluster test
    results = {}
    # test_type = "load_predict"  # 'endpoint'
    test_type = "endpoint"  # ''
    parallel_run(
        cluster_ids=cluster_ids,
        n_parallel_jobs_per_cluster=n_parallel_jobs_per_cluster,
        models_to_test=models_to_test,
        host=host,
        token=token,
        results=results,
        test_type=test_type,
    )

    retry_models = log_and_get_failed_models(results)
    print(f"Retrying {len(retry_models)} models")
    # Give clusters some time to recover from any failures
    time.sleep(60 * 5)

    # run failed models again, with job-parallelism 1 but same cluster-parallelism
    parallel_run(
        cluster_ids=cluster_ids,
        n_parallel_jobs_per_cluster=1,
        models_to_test=retry_models,
        host=host,
        token=token,
        results=results,
        test_type=test_type,
    )
    json.dump(results, open("results.json", "w"))

    # 5) Delete all clusters
    # for cluster_id in cluster_ids:
    #     delete_cluster(cluster_id)


@db_cloud_node_params
def test_endpoint(creds, node_type):
    lic, host, token = creds
    cluster_id = get_or_create_test_cluster(creds, node_type, 10, clean_workspace=False)
    job_url, success = run_endpoint_tests(cluster_id, host, token, "tokenize")
    assert success


@db_cloud_node_params
def test_endpoint_licensed(creds, node_type):
    lic, host, token = creds
    cluster_id = get_or_create_test_cluster(creds, node_type, 0, clean_workspace=True)
    # run_endpoint_tests(cluster_id, host, token, "med_ner.clinical")
    # run_endpoint_tests(cluster_id, host, token, "en.med_ner.clinical")
    job_url, success = run_endpoint_tests(cluster_id, host, token, "tokenize")
    assert success


"""
We want to be able to test on :  
- List of models
- List of runtimes
- auto-generate benchmarks --> time for load/predicting

# TODO
- handle spot instance reclamation https://dbc-3d4c44aa-a512.cloud.databricks.com/?o=4085846932608579#job/407841450144996/run/583312836892114 -162028-g0yy9b85
- handle endpoint stuck/ use timeout 60mins 


"""
# https://github.com/qdrant/qdrant-haystack/tree/master
