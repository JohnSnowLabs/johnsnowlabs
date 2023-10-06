import os.path

from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import (
    assert_job_suc,
    run_cluster_test_suite,
    get_or_create_test_cluster,
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
