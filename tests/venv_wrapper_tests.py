import unittest

from johnsnowlabs import JslSecrets
from johnsnowlabs.utils.venv_utils import *


class VenvTests(unittest.TestCase):
    test_dir = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/venv/tmp_test_venv'

    # venv_wrapper = VenvWrapper(self.venv_creation_dir, )
    def test_venv_wrapper(self):
        """
        Test all core features of the VenvWrapper, install, uninstall and check_if_contains_module
        """
        # Lib should not be found after having uninstalled it
        self.test_dir = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/venv/tmp_test_venv'
        VenvWrapper.create_venv(self.test_dir)
        VenvWrapper.uninstall_from_venv(self.test_dir, 'pyspark')
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.test_dir, 'pyspark') is False)

        # After installing lib should be found
        self.assertTrue(VenvWrapper.install_to_venv(self.test_dir, 'pyspark'))
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.test_dir, 'pyspark'))

        # Uninstall and check its missing
        VenvWrapper.uninstall_from_venv(self.test_dir, 'pyspark')
        self.assertTrue(VenvWrapper.is_lib_in_venv(self.test_dir, 'pyspark') is False)
        os.system(f'rm -r {self.test_dir} ')

    def test_install_jsl_suite_to_venv(self):
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/licenses/ocr_40.json'
        secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(secrets_file=f)


        print(secrets)
        # TODO
        pass

    # def test_jsl_suite_status(self):
    #     # TODO
    #     pass

    @classmethod
    def tearDownClass(cls):
        print("TEARING DOWN")
        os.system(f'rm -r {cls.test_dir} ')

    if __name__ == '__main__':
        unittest.main()
