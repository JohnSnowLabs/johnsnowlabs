import unittest
from johnsnowlabs.utils.enums import *
from johnsnowlabs.auto_install.lib_resolvers import *
import tests.utils.secrets as sct


class LibDependencyResolutionCase(unittest.TestCase):
    def test_list_ocr_lib_resolve(self):
        for spark_version in OcrLibResolver.compatible_spark_versions:
            for install_type in [PyInstallTypes.tar, PyInstallTypes.wheel, JvmHardwareTarget.cpu]:
                print(f'Testing Spark version ={spark_version.as_str()} and install type = {install_type}')
                dep = OcrLibResolver.get_dependency_url(secret=sct.OCR_SECRET,
                                                        spark_version_to_match=spark_version,
                                                        install_type=install_type)
                print(dep)
                self.assertTrue(dep.validate())

                dep = OcrLibResolver.get_dependency_url(secret=sct.OCR_SECRET,
                                                        spark_version_to_match=None,
                                                        install_type=install_type)
                print(dep)
                self.assertTrue(dep.validate())


    def test_list_hc_lib_resolve(self):
        for spark_version in HcLibResolver.compatible_spark_versions:
            for install_type in [PyInstallTypes.tar, PyInstallTypes.wheel, JvmHardwareTarget.cpu]:
                print(f'Testing Spark version ={spark_version.as_str()} and install type = {install_type}')
                dep = HcLibResolver.get_dependency_url(secret=sct.JSL_SECRET,
                                                       spark_version_to_match=spark_version,
                                                       install_type=install_type)
                dep = HcLibResolver.get_dependency_url(secret=sct.JSL_SECRET,
                                                       spark_version_to_match=None,
                                                       install_type=install_type)

                print(dep)
                self.assertTrue(dep.validate())
                dep = HcLibResolver.get_dependency_url(secret=sct.JSL_SECRET,
                                                       spark_version_to_match=None,
                                                       install_type=install_type)
                print(dep)
                self.assertTrue(dep.validate())


    def test_list_nlp_lib_resolve(self):
        for spark_version in NlpLibResolver.compatible_spark_versions:
            for install_type in [PyInstallTypes.tar, PyInstallTypes.wheel,
                                 JvmHardwareTarget.cpu, JvmHardwareTarget.gpu, JvmHardwareTarget.m1]:
                print(f'Testing Spark version ={spark_version.as_str()} and install type = {install_type}')
                dep = NlpLibResolver.get_dependency_url(
                                                       spark_version_to_match=spark_version,
                                                       install_type=install_type)
                print(dep)
                self.assertTrue(dep.validate())

                dep = NlpLibResolver.get_dependency_url(
                    spark_version_to_match=None,
                    install_type=install_type)
                print(dep)
                self.assertTrue(dep.validate())



if __name__ == '__main__':
    unittest.main()
