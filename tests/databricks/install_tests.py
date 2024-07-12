from databricks_api import DatabricksAPI

from databricks_api import DatabricksAPI

from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    assert_job_suc,
)


@db_cloud_node_params
def test_create_cluster_with_custom_libs(creds, node_type):
    lic, host, token = creds
    extra_libs = ["farm-haystack==1.21.2", "langchain"]

    cluster_id = nlp.install_to_databricks(
        json_license_path=lic,
        databricks_host=host,
        databricks_token=token,
        driver_node_type_id=node_type,
        node_type_id=node_type,
        cluster_name="Test Custom Lib Cluster",
        clean_cluster=False,
        block_till_cluster_ready=True,
        extra_pip_installs=extra_libs,
    )
    script = """
import haystack
import langchain
print(haystack)
print(langchain)


    """
    # cluster_id = "1005-134624-a6p9ji9u"

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




@db_marketplace_cloud_node_params
def test_install_to_existing_cluster(creds, node_type):
    lic, host, token = creds
    print(lic, host, token)
    # Create a cluster with no installs
    db = DatabricksAPI(host=host, token=token)
    cluster_id = db.cluster.create_cluster(
        driver_node_type_id=node_type,
        node_type_id=node_type,
        spark_version=settings.db_spark_version,
        num_workers=1,
        cluster_name="Test Custom Lib Cluster6",
    )["cluster_id"]
    print(f"Created cluster {cluster_id}")
    wait_till_cluster_running(db, cluster_id)

    cluster_id = nlp.install_to_databricks(
        databricks_cluster_id=cluster_id,
        json_license_path=lic,
        databricks_host=host,
        databricks_token=token,
        driver_node_type_id=node_type,
        node_type_id=node_type,
        visual=True,
        clean_cluster=False,
        block_till_cluster_ready=True,
    )
    script = """
import nlu
nlu.load('en.embed_sentence.bert').predict('The quick brown fox jumps over the lazy dog')
    """
    # cluster_id = "1005-134624-a6p9ji9u"

    assert_job_suc(
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=host,
            databricks_token=token,
            run_name="Notebook Test",
        )
    )
