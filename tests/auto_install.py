import unittest
from pprint import pprint

import os
import sys

from zmq.backend.cython.message import ref

import johnsnowlabs as jsl
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.pip_utils import get_pip_lib_version
from johnsnowlabs.utils.print_messages import log_outdated_lib
from johnsnowlabs.utils.venv_utils import VenvWrapper
from johnsnowlabs import *


ckl_token = ''
ckl_host = ''
f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/latest_3_1_x_spark_nlp_for_healthcare_spark_ocr_V2.json'
class AutoInstallTestCase(unittest.TestCase):
    venv_creation_dir = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/venv/tmp_test_venv'
    zip_dir = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/offline'


    def test_quick_bad(self):
        l = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/bad/spark_nlp_1.0.0_with_ocr.json'
        jsl.install()
    def test_install_to_databricks(self):

        jsl.install(databricks_token='ckl_token')
        cluster_id = jsl.install(databricks_host=ckl_host, databricks_token=ckl_token)
        db_client = get_db_client_for_token(ckl_host, ckl_token)
    def test_install_to_current_env_browser_pop_up(self):
        jsl.install(force_browser=True, license_number=0)
        # jsl.install(browser_login=False)
        import sparknlp
        import sparknlp_jsl
        import sparkocr
        import nlu
        import sparknlp_display

    def test_install_to_current_env(self):
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/4_1_LATEST_OCR_HC_BCK.json'
        # f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/latest_3_1_x_spark_nlp_for_healthcare_NO_spark_ocr_5112.json'
        # f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/no_ocr/3_0_x_spark_nlp_for_healthcare_NO_spark_ocr_5112.json'
        # f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/no_ocr/latest_3_1_x_spark_nlp_for_healthcare_NO_spark_ocr_5112.json'
        jsl.install(json_license_path=f, refresh_install=True)
        # jsl.install(browser_login=False)
        # import sparknlp
        # import sparknlp_jsl
        # import sparkocr
        import nlu
        import sparknlp_display

    def test_install_to_different_python_env(self):
        # Install to env which is not the one we are currently running
        os.system(f'rm -r {self.venv_creation_dir} ')
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/ocr_40.json'
        VenvWrapper.create_venv(self.venv_creation_dir)
        py_path = VenvWrapper.glob_py_exec_from_venv(self.venv_creation_dir)
        jsl.install(json_license_path=f, python_exec_path=py_path)
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparknlp'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparkocr'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparknlp_display'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'nlu'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'internal_with_finleg'))  # ---> sparknlp_jsl
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'jsl_tmp'))  # --> johnsnowlabs
        os.system(f'rm -r {self.venv_creation_dir} ')

    def test_create_fresh_venv_and_install_to_it(self):
        # let jsl-lib create a fresh venv for us
        os.system(f'rm -r {self.venv_creation_dir} ')
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/ocr_40.json'
        jsl.install(json_license_path=f, venv_creation_path=self.venv_creation_dir)
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparknlp'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparkocr'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparknlp_display'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'nlu'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'sparknlp_jsl'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, 'johnsnowlabs'))
        os.system(f'rm -r {self.venv_creation_dir} ')

    def test_install_status(self):
        # jsl.check_health(check_licenses=True)
        jsl.list_remote_licenses()
        jsl.list_local_licenses()

    def test_oudated_message(self):
        from johnsnowlabs.auto_install.softwares import Software
        log_outdated_lib(Software.spark_ocr, '79')

    def test_offline_install_print(self):
        jsl.install(offline=True)

    def test_offline_install_zip(self):
        os.system(f'rm -r {self.zip_dir} ')
        jsl.install(offline=True, offline_zip_dir=self.zip_dir, install_optional=False, include_dependencies=False)

    def test_browser_install(self):
        jsl.install(force_browser=True)
        # jsl.install(license_number=1, force_browser=True)
        # jsl.install(license_number=2, force_browser=True)

    def test_upgrade_licensed_lib_via_secret_only(self):
        new_secret = ''
        jsl.install(ocr_secret=new_secret)


    def test_json_license_install(self):
        new_lic = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/4_2_LATEST_OCR_HC_BCK.json'
        jsl.install(json_license_path=new_lic)
        import sparknlp
        import sparknlp_jsl
        import sparknlp
        import sparknlp_jsl
        # import sparkocr
        import nlu
        import sparknlp_display
        # jsl.install(json_license_path=f)


    def test_json_license_install_outdated(self):
        # old_lic = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/no_ocr/ocr_40.json'
        latest_lic = ''
        old_lic2=f
        # new_lic = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/no_ocr/ocr_402.json'
        # jsl.install(json_license_path=f)
        jsl.install(json_license_path=old_lic2)
        import sparknlp
        import sparknlp_jsl
        import sparknlp
        import sparknlp_jsl
        # import sparkocr
        import nlu
        import sparknlp_display
        # jsl.install(json_license_path=f)

    def test_create_and_install_cluster(self):
        install_suite = get_install_suite_from_jsl_home()
        print(install_suite)

    def test_uninstall_all(self):
        # os.system(f'{sys.executable} -m pip uninstall spark-nlp -y')
        # os.system(f'{sys.executable} -m pip uninstall spark-nlp-display -y')
        # os.system(f'{sys.executable} -m pip uninstall nlu -y')

        os.system(f'{sys.executable} -m pip uninstall spark-nlp-jsl -y')
        os.system(f'{sys.executable} -m pip uninstall spark-nlp-jsl -y')
        os.system(f'{sys.executable} -m pip uninstall spark-ocr -y')
        # os.system(f'{sys.executable} -m pip uninstall jsl_tmp -y')
        os.system(f'{sys.executable} -m pip uninstall spark-nlp-internal -y')

    @classmethod
    def tearDownClass(cls):
        1
        # print("TEARING DOWN")
        # os.system(f'rm -r {cls.venv_creation_dir} ')
        # # os.system(f'rm -r {cls.zip_dir} ')
        #
        # os.system(f'{sys.executable} -m pip uninstall spark-nlp-jsl -y')
        # os.system(f'{sys.executable} -m pip uninstall spark-nlp-jsl -y')
        # os.system(f'{sys.executable} -m pip uninstall spark-ocr -y')
        # os.system(f'{sys.executable} -m pip uninstall jsl_tmp -y')
        # os.system(f'{sys.executable} -m pip uninstall internal_with_finleg -y')
        #
        # os.system(f'{sys.executable} -m pip uninstall spark-nlp -y')
        # os.system(f'{sys.executable} -m p ip uninstall spark-nlp-display -y')
        # os.system(f'{sys.executable} -m pip uninstall nlu -y')
        # os.system(f'{sys.executable} -m pip uninstall pyspark -y')

    def test_refresh_credentials(self):
        # Use this to upgrade all secrets on every license file, if greater
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/no_ocr/latest_3_1_x_spark_nlp_for_healthcare_NO_spark_ocr_5112.json'
        jsl.install(json_license_path=f, only_refresh_credentials=True)


if __name__ == '__main__':
    unittest.main()
