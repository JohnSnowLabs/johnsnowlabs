from johnsnowlabs.auto_install.databricks.install_utils import *
from johnsnowlabs.auto_install.databricks.install_utils import _get_cluster_id
from tests.databricks.db_test_utils import *
from tests.databricks.db_test_utils import get_or_create_test_cluster


@db_cloud_params
def test_list_workspace_infos(creds):
    # List infos about the workspace
    lic, host, token = creds
    db_client = get_db_client_for_token(host, token)
    list_db_runtime_versions(db_client)
    list_node_types(db_client)
    list_clusters(db_client)


# Parameterizing over both creds and node_type
@db_cloud_node_params
def test_get_db_cluster_infos(creds, node_type):
    # list infos specific to a cluster
    lic, host, token = creds
    db_client = get_db_client_for_token(host, token)

    cluster_id = get_or_create_test_cluster(creds, node_type, 0)
    list_cluster_lib_status(db_client, cluster_id)
    pprint(db_client.cluster.get_cluster(cluster_id))

    # Check cluster name+runtime detected
    assert (
        cluster_exist_with_name_and_runtime(
            db_client, "TEST_CLUSTER_0", settings.db_spark_version
        )
        == True
    )

    # check cluster id exists
    assert does_cluster_exist_with_id(db_client, cluster_id) == True
    # cluster_id = get_or_create_test_cluster(aws_creds, aws_cpu_node, 0)


@db_cloud_params
def test_delete_all_test_clusters(creds):
    lic, host, token = creds
    db_client = get_db_client_for_token(host, token)
    delete_all_test_clusters(db_client)
    for i in range(10):
        assert _get_cluster_id(db_client, f"TEST_CLUSTER_{i}") is None
