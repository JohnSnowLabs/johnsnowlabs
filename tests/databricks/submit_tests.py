import os.path

from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    assert_job_suc,
    run_cluster_test_suite,
    get_or_create_test_cluster,
)


def nlu_func():
    import nlu

    medical_text = """A 28-year-old female with a history of gestational
            diabetes presented with a one-week history of polyuria ,
             polydipsia , poor appetite , and vomiting ."""
    # TODO use licensed models
    # df = nlu.load("en.med_ner.diseases").predict(medical_text)
    df = nlu.load("tokenize").predict(medical_text)
    for c in df.columns:
        print(df[c])


@db_cloud_node_params
def test_run_integration_tests(creds, node_type):
    lic, host, token = creds
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    run_cluster_test_suite(cluster_id, host, token)


@db_cloud_node_params
def test_submit_string_task_to_databricks(creds, node_type):
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    lic, host, token = creds
    script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))
        """
    assert_job_suc(
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Python Code String Example",
        )
    )


@db_cloud_node_params
def test_submit_local_py_file_task_to_databricks(creds, node_type):
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    lic, host, token = creds
    # Test script
    import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test

    py_script_file_path = os.path.abspath(nlp_test.__file__)
    assert_job_suc(
        nlp.run_in_databricks(
            py_script_file_path,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Script test",
        )
    )


@db_cloud_node_params
def test_submit_function_task_to_databricks(creds, node_type):
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    lic, host, token = creds
    # basically reads the function code and submits it to databricks.
    # It also copies indentation and comments,watch out for that
    assert_job_suc(
        nlp.run_in_databricks(
            nlu_func,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Function test",
        )
    )


@db_cloud_node_params
def test_submit_notebook_task_to_databricks(creds, node_type):
    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    lic, host, token = creds

    nb_path = "sample.ipynb"
    dst_path = "/Users/christian@johnsnowlabs.com/test.ipynb"
    # nb_path = "/home/ckl/Documents/tmp/databricks_endpoints_tutorial_PUBLIC.ipynb"
    assert_job_suc(
        nlp.run_in_databricks(
            nb_path,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Notebook Test",
            dst_path=dst_path,
        )
    )


@db_cloud_node_params
def test_submit_notebook_parameterized_task_to_databricks(creds, node_type):
    # cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    lic, host, token = creds
    cluster_id = "1005-134624-a6p9ji9u"

    nb_path = "parameterized_nb_example.ipynb"
    dst_path = "/Users/christian@johnsnowlabs.com/test.ipynb"
    assert_job_suc(
        nlp.run_in_databricks(
            nb_path,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Notebook Test",
            dst_path=dst_path,
            parameters={"input_text": "How are you today", "model_name": "sentiment"},
        )
    )


@db_cloud_node_params
def test_submit_script_parameterized_task_to_databricks(creds, node_type):
    #    cluster_id = get_or_create_test_cluster(creds, node_type, 0)

    script = """
import sys
print(f"First argument: {sys.argv[1]}, Second argument: {sys.argv[2]}")
    """

    lic, host, token = creds
    cluster_id = "1005-134624-a6p9ji9u"

    arg1 = "My first arg"
    arg2 = "My second arg"
    assert_job_suc(
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Notebook Test",
            parameters=[arg1, arg2],
        )
    )
