import queue

from johnsnowlabs import nlp
from johnsnowlabs.auto_install.health_checks.generate_endpoint_test import (
    generate_endpoint_test,
)
from tests.utilsz import secrets as sct


def assert_job_suc(state):
    assert state["state"]["result_state"] == "SUCCESS"


def run_endpoint_tests(test_cluster_id, host, token, model):
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


def delete_all_test_clusters():
    # TODO
    pass


def get_test_cluster(creds, node_type, n):
    # TODO check existing cluster for clusters named "TESTING_XYZ" if yes take that instead of create!
    runtime = "9.1.x-scala2.12"
    lic, host, token = creds
    cluster_id = nlp.install(
        spark_version=runtime,
        json_license_path=lic,
        databricks_host=host,
        databricks_token=token,
        driver_node_type_id=node_type,
        node_type_id=node_type,
        cluster_name=f"TEST_CLUSTER_{n}",
    )
    return cluster_id


def tester_thread(cluster_id, job_que, host, token, results):
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
