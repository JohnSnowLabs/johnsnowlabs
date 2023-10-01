import os
from johnsnowlabs.auto_install.databricks.install_utils import *
# fmt: off
from tests.databricks.db_test_utils import aws_creds
# fmt: on


def test_hdfs_basic_methods(aws_creds):
    lic, host, token = aws_creds
    db_client = get_db_client_for_token(host, token)
    src_p = os.path.abspath(__file__)
    target_p = "/johnsnowlabs/testf"
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p)
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "2")
    copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "3")
    pprint(dbfs_ls(db_client, "/johnsnowlabs"))
    dbfs_rm(db_client, target_p)
    pprint(dbfs_ls(db_client, "/johnsnowlabs"))
