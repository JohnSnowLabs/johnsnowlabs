import os
import sys
import unittest

from johnsnowlabs import nlp
from johnsnowlabs.auto_install.softwares import (SparkHcSoftware,
                                                 SparkNlpSoftware,
                                                 SparkOcrSoftware)
from tests.utils import clear_installed_jsl_installation, get_cross_lib_pipe

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def setUpModule():
    nlp.install(browser_login=False, spark_nlp=True, nlp=True, visual=True,
                med_license=os.environ.get("VALID_LICENSE"), ocr_license=os.environ.get("VALID_LICENSE"),
                aws_access_key="",
                aws_key_id=""
                )


def tearDownModule():
    clear_installed_jsl_installation()


class InstallationTestCase(unittest.TestCase):
    def test_all_libs_are_installedd(self):
        installed_products = nlp.check_health()
        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertTrue(installed_products[SparkHcSoftware])
        self.assertTrue(installed_products[SparkOcrSoftware])

class SparkSessionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = nlp.start( visual=True)
    
    def simple_cross_library_session(self):
        import pkg_resources
        doc_example = pkg_resources.resource_filename(
            "sparkocr", "resources/ocr/docs/doc2.docx"
        )
        df = self.spark.read.format("binaryFile").load(doc_example).cache()
        get_cross_lib_pipe().fit(df).transform(df).show()
