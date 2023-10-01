from multiprocessing import Queue
from threading import Thread

from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    run_endpoint_tests,
    get_one_model_per_class,
    get_or_create_test_cluster,
    subtester_thread,
)


@pytest.mark.skip(reason="WIP")
@db_cloud_node_params
def test_endpoints_multi_cluster(creds, node_type):
    n_clusters = 1
    # n_parallel_jobs_per_cluster = 4  # todo add
    # 1) Create clusters
    cluster_ids = [
        get_or_create_test_cluster(creds, node_type, i) for i in range(n_clusters)
    ]

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
            target=subtester_thread, args=(cluster_id, job_que, host, token, results)
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


@db_cloud_node_params
def test_endpoint(creds, node_type):
    lic, host, token = creds
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    run_endpoint_tests(cluster_id, host, token, "tokenize")
