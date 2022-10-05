from pprint import pprint
import unittest
# import tests.found_secrets as sct
import johnsnowlabs
from johnsnowlabs import JvmHardwareTarget
from johnsnowlabs.auto_install.databricks.databricks_utils import *
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.utils.file_utils import str_to_file, path_tail

ckl_email = ''
ckl_token = ''
ckl_host = ''
sample_db_runtime = '10.5.x-scala2.12'
sample_node_type = 'i3.xlarge'
cluster_id = '0926-040523-d8k13d4f'
secret_path = '/tests/spark_nlp_ocr_hc.json'

from johnsnowlabs import *

# TODO DATABRICKS SELF INSTALL!!
class DatabricksTestCase(unittest.TestCase):
    def test_list_db_infos(self):
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        list_db_runtime_versions(db_client)
        list_node_types(db_client)
        list_clusters(db_client)

    def test_create_fresh_cluster(self):
        p = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/4_1_LATEST_OCR_HC.json'
        cluster_id = johnsnowlabs.install(json_license_path=p,
                                          databricks_host=ckl_host, databricks_token=ckl_token)
        db_client = get_db_client_for_token(ckl_host, ckl_token)

        from pprint import pprint
        while 1:
            status = db_client.cluster.get_cluster(cluster_id)
            pprint(status['state'])
            # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate

    def test_create_fresh_cluster_and_run_task(self):
        # TODO make example like OCR with PKR!
        py_script = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/johnsnowlabs/health_checks/hc.py'
        johnsnowlabs.databricks_submit(databricks_host=ckl_host, databricks_token=ckl_token, py_script_path=py_script)
        # TODO Submit Task/Job/???   and gifs

    def test_install_to_databricks(self):
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        p = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tests/utils/spark_nlp_ocr_hc.json'
        install_suite = get_install_suite_from_jsl_home(jvm_hardware_target=JvmHardwareTarget.cpu)
        print(install_suite)
        # db_utils.list_db_runtime_versions(db_client)
        # db_utils.list_node_types(db_client)
        cluster_id = create_cluster(db=db_client,
                                    install_suite=install_suite,
                                    cluster_name='Testing auto-install to databricks for JSL-Lib'
                                    )
        # list_cluster_lib_status(db_client, cluster_id)

    def test_lib_status(self):
        # WIP
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        list_cluster_lib_status(db_client, cluster_id)

    def test_hdfs_basic_methods(self):
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        src_p = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/setup.py'
        target_p = '/johnsnowlabs/testf'
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p)
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + '2')
        copy_from_local_to_hdfs(db_client, local_path=src_p, dbfs_path=target_p + '3')
        pprint(dbfs_ls(db_client, '/johnsnowlabs'))
        dbfs_rm(db_client, target_p)
        pprint(dbfs_ls(db_client, '/johnsnowlabs'))

    def test_submit_task_to_databricks(self):
        py_script = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/johnsnowlabs/utils/health_checks/hc.py'
        py_script = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/johnsnowlabs/utils/health_checks/nlp.py'
        py_script = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/johnsnowlabs/utils/health_checks/ocr.py'
        import inspect
        import johnsnowlabs.auto_install.health_checks.hc_test

        def get_runnable_test_script(test_module):
            out_path = f'{settings.tmp_notebook_dir}/{path_tail(inspect.getfile(test_module))}'
            str_to_file(inspect.getsource(test_module) + '\nrun_test()', out_path)
            return out_path

        import johnsnowlabs.auto_install.health_checks.hc_test as hc_test
        import johnsnowlabs.auto_install.health_checks.ocr_test as ocr_test
        import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test
        tests = [hc_test, ocr_test, nlp_test]
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        # ckl_cluster_id = None  # '0725-044129-2mwageql'
        # # TODO use self-destructing create cluster?
        for t in tests:
            run_id = run_local_py_script_as_task(db_client, get_runnable_test_script(t), cluster_id=cluster_id)
            print(run_id)

    def test_test_for_job_finishwait(self):
        db_client = get_db_client_for_token(ckl_host, ckl_token)
        r = checkon_db_task(db_client, run_id='32458')
        print(r)


if __name__ == '__main__':
    unittest.main()
