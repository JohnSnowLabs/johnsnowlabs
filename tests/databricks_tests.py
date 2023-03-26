from pprint import pprint
import unittest

import tests.utils.secrets as sct
import johnsnowlabs
from johnsnowlabs.auto_install.databricks.install_utils import *
from johnsnowlabs import *
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.utils.enums import JvmHardwareTarget
from johnsnowlabs.utils.file_utils import str_to_file, path_tail

cluster_id = "0926-040523-d8k13d4f"

from johnsnowlabs import *


# Test Function
def test_submit_func():
    print("Test Function")


def nlu_func():
    import nlu

    medical_text = """A 28-year-old female with a history of gestational 
    diabetes presented with a one-week history of polyuria ,
     polydipsia , poor appetite , and vomiting ."""
    df = nlu.load("en.med_ner.diseases").predict(medical_text)
    for c in df.columns:
        print(df[c])


# TODO DATABRICKS SELF INSTALL!!
class DatabricksTestCase(unittest.TestCase):
    def test_list_db_infos(self):
        db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
        list_db_runtime_versions(db_client)
        list_node_types(db_client)
        list_clusters(db_client)

    def test_get_db_lib_infos(self):
        # WIP
        cluster_id = "1006-022913-lb94q2m0"
        db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
        list_cluster_lib_status(db_client, cluster_id)
        pprint(db_client.cluster.get_cluster(cluster_id))

    def test_create_fresh_cluster(self):
        nlp.install(
            json_license_path=sct.db_lic,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
        )

    def test_create_fresh_cluster_and_run_task(self):
        py_script = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/johnsnowlabs/health_checks/hc.py"
        johnsnowlabs.databricks_submit(
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            py_script_path=py_script,
        )

    def test_install_to_databricks(self):
        db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
        cluster_id = nlp.install(
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
        )

    def test_hdfs_basic_methods(self):
        db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
        src_p = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/setup.py"
        target_p = "/johnsnowlabs/testf"
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p)
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "2")
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + "3")
        pprint(dbfs_ls(db_client, "/johnsnowlabs"))
        dbfs_rm(db_client, target_p)
        pprint(dbfs_ls(db_client, "/johnsnowlabs"))

    def test_submit_task_to_databricks(self):
        import inspect
        import johnsnowlabs.auto_install.health_checks.hc_test

        # Make cluster
        # cluster_id = nlp.install(json_license_path=sct.db_lic, databricks_host=sct.ckl_host,
        #                          databricks_token=sct.ckl_token)
        cluster_id = "1006-050402-4nsqdu8h"
        # Test modules
        import johnsnowlabs.auto_install.health_checks.hc_test as hc_test
        import johnsnowlabs.auto_install.health_checks.ocr_test as ocr_test
        import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test

        nlp.run_in_databricks(
            nlp_test,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="nlp_test",
        )
        nlp.run_in_databricks(
            ocr_test,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="ocr_test",
        )
        nlp.run_in_databricks(
            hc_test,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="hc_test",
        )

        nlp.run_in_databricks(
            test_submit_func,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Function test",
        )

        # Test script
        py_script = "/home/ckl/Documents/freelance/jsl/johnsnowlabs/johnsnowlabs/auto_install/health_checks/hc_test.py"
        nlp.run_in_databricks(
            py_script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Script test ",
        )

        # Test String
        script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))
        """
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Python Code String Example",
        )

        nlp.run_in_databricks(
            "print('noice')",
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Code String test 2",
        )

        nlp.run_in_databricks(
            nlu_func,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Function test",
        )

        # Test String
        script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))
        """
        nlp.run_in_databricks(
            script,
            databricks_cluster_id=cluster_id,
            databricks_host=sct.ckl_host,
            databricks_token=sct.ckl_token,
            run_name="Python Code String Example",
        )

    def test_test_for_job_finishwait(self):
        # WIP
        db_client = get_db_client_for_token(sct.ckl_host, sct.ckl_token)
        r = checkon_db_task(db_client, run_id="32458")
        print(r)


if __name__ == "__main__":
    unittest.main()
