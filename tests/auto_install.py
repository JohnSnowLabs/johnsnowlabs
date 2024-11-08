import os
import sys
import unittest

import tests.utilsz.secrets as sct
from johnsnowlabs import *
from johnsnowlabs.auto_install.databricks.install_utils import *
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.utils.print_messages import log_outdated_lib
from johnsnowlabs.utils.venv_utils import VenvWrapper


class AutoInstallTestCase(unittest.TestCase):
    venv_creation_dir = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/venv/tmp_test_venv"
    zip_dir = "/home/ckl/Documents/freelance/jsl/johnsnowlabs/tmp/offline"


    def test_install_to_current_env_browser_pop_up(self):
        nlp.install(force_browser=False, visual=True, remote_license_number=2)


    def test_install_pr_secret(self):
        settings.enforce_versions = False
        nlp.install(enterprise_nlp_secret=secrets.pr_secret)

    def test_install_to_current_env(self):
        settings.enforce_versions = False
        nlp.install(json_license_path=sct.old_lic, refresh_install=True)
        # import sparknlp

    def test_install_to_different_python_env(self):
        # Install to env which is not the one we are currently running
        os.system(f"rm -r {self.venv_creation_dir} ")
        f = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/ocr_40.json"
        VenvWrapper.create_venv(self.venv_creation_dir)
        py_path = VenvWrapper.glob_py_exec_from_venv(self.venv_creation_dir)
        nlp.install(json_license_path=f, python_exec_path=py_path)
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparknlp"))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparkocr"))
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparknlp_display")
        )
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "nlu"))
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "internal_with_finleg")
        )  # ---> sparknlp_jsl
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "jsl_tmp")
        )  # --> johnsnowlabs
        os.system(f"rm -r {self.venv_creation_dir} ")

    def test_create_fresh_venv_and_install_to_it(self):
        # let jsl-lib create a fresh venv for us
        os.system(f"rm -r {self.venv_creation_dir} ")
        f = "/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/ocr_40.json"
        nlp.install(json_license_path=f, venv_creation_path=self.venv_creation_dir)
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparknlp"))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparkocr"))
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparknlp_display")
        )
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "nlu"))
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "sparknlp_jsl")
        )
        self.assertTrue(
            VenvWrapper.is_lib_in_venv(self.venv_creation_dir, "johnsnowlabs")
        )
        os.system(f"rm -r {self.venv_creation_dir} ")

    def test_list_license_status(self):
        nlp.check_health()
        nlp.check_health(check_install=True)
        nlp.list_remote_licenses()
        nlp.list_local_licenses()



    def test_offline_install_print(self):
        nlp.install(offline=True)

    def test_offline_install_zip(self):
        os.system(f"rm -r {self.zip_dir} ")
        nlp.install(
            offline=True,
            offline_zip_dir=self.zip_dir,
            install_optional=True,
            include_dependencies=True,
        )

    def test_browser_install(self):
        nlp.install(force_browser=True, visual=True, local_license_number=2)

    def test_upgrade_licensed_lib_via_secret_only(self):
        new_secret = secrets.random_secret
        from johnsnowlabs import settings

        settings.enforce_versions = False
        nlp.install(enterprise_nlp_secret=new_secret)

    def test_json_license_install(self):
        nlp.install(json_license_path=sct.latest_lic,visual=True)


    def test_json_license_install_outdated(self):
        nlp.settings.enforce_versions = False
        nlp.install(json_license_path=sct.old_lic)


    def test_create_and_install_cluster(self):
        install_suite = get_install_suite_from_jsl_home()
        print(install_suite)

    def test_uninstall_all(self):
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-nlp -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-nlp-display -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall nlu -y')

        # os.system(f"{sys.executable} -m pip uninstall spark-nlp-jsl -y")
        # os.system(f"{sys.executable} -m pip uninstall spark-ocr -y")
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall jsl_tmp -y')
        os.system(f"{sys.executable} -m pip uninstall spark-nlp-internal -y")

    def test_install_to_emr(self):
        # Make sure correct aws credentials are configured
        nlp.install_to_emr(
            "us-east-1",
            bootstrap_bucket="ksh-emr-bucket",
            subnet_id="subnet-28754965",
            s3_logs_path="s3://ksh-emr-bucket/logs",
        )

    @classmethod
    def tearDownClass(cls):
        1
        # print("TEARING DOWN")
        # os.system(old_lic'rm -r {cls.venv_creation_dir} ')
        # # os.system(old_lic'rm -r {cls.zip_dir} ')
        #
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-nlp-jsl -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-nlp-jsl -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-ocr -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall jsl_tmp -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall internal_with_finleg -y')
        #
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall spark-nlp -y')
        # os.system(old_lic'{sys.py_executable} -py_executable p ip uninstall spark-nlp-display -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall nlu -y')
        # os.system(old_lic'{sys.py_executable} -py_executable pip uninstall pyspark -y')

    def test_refresh_credentials(self):
        # Use this to upgrade all secrets on every license file, if greater
        nlp.install(json_license_path=sct.latest_lic, only_refresh_credentials=True)

    def test_refresh_install(self):
        # Use this to upgrade all secrets on every license file, if greater
        nlp.install(json_license_path=sct.latest_lic, refresh_install=True)


if __name__ == "__main__":
    unittest.main()
