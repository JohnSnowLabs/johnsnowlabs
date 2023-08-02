import os
import shutil
import unittest

from johnsnowlabs import nlp, settings
from johnsnowlabs.auto_install.softwares import (Software, SparkHcSoftware,
                                                 SparkNlpSoftware,
                                                 SparkOcrSoftware)
from johnsnowlabs.utils.enums import ProductName
from johnsnowlabs.utils.venv_utils import VenvWrapper


class AutoInstallationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        shutil.rmtree(settings.root_dir, ignore_errors=True)
        import pip
        for product in ProductName:
            software = Software.for_name(product)
            if software and software.pypi_name:
                pip.main(["uninstall", "-y", software.pypi_name])

    def test_only_spark_nlp_should_be_installed_if_secrets_are_empty(self):
        nlp.install(browser_login=False)
        installed_products = nlp.check_health()

        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertFalse(installed_products[SparkHcSoftware])
        self.assertFalse(installed_products[SparkOcrSoftware])
        
    def test_spark_hc_is_installed_if_licensed_provided(self):
        nlp.install(med_license=os.environ.get("VALID_LICENSE"))
        installed_products = nlp.check_health()

        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertTrue(installed_products[SparkHcSoftware])
        self.assertFalse(installed_products[SparkOcrSoftware])
    

    def test_spark_ocr_is_installed_if_visual_is_true(self):
        nlp.install(med_license=os.environ.get("VALID_LICENSE"), visual=True)
        installed_products = nlp.check_health()
        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertTrue(installed_products[SparkHcSoftware])
        self.assertTrue(installed_products[SparkOcrSoftware])
