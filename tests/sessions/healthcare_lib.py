import os
import sys
import unittest

from johnsnowlabs import medical, nlp
from johnsnowlabs.auto_install.softwares import (SparkHcSoftware,
                                                 SparkNlpSoftware,
                                                 SparkOcrSoftware)
from tests.utils import (clear_installed_jsl_installation,
                         get_finance_pipeline, get_legal_pipeline)

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

def setUpModule():
    nlp.install(browser_login=False, spark_nlp=True, nlp=True, visual=False,
                med_license=os.environ.get("VALID_LICENSE"),
                aws_access_key="",
                aws_key_id=""
                )


def tearDownModule():
    clear_installed_jsl_installation()


class InstallationTestCase(unittest.TestCase):
    def test_spark_nlp_jsl_is_installed(self):
        installed_products = nlp.check_health()
        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertTrue(installed_products[SparkHcSoftware])
        self.assertFalse(installed_products[SparkOcrSoftware])

class SparkSessionTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.spark = nlp.start()

    def test_healthcare_session(self):
        print("Test Healthcare session ...")
        d = nlp.DocumentAssembler().setInputCol("text").setOutputCol("doc")
        t = nlp.Tokenizer().setInputCols("doc").setOutputCol("tok")
        c = (
            medical.BertForTokenClassification()
            .pretrained()
            .setInputCols(["tok", "doc"])
            .setOutputCol("class")
        )
        p = nlp.Pipeline(stages=[d, t, c])
        p = nlp.to_nlu_pipe(p)
        print(p.predict("Hello form John SNow labs"))
    
    def test_finance_session(self):
        print("Testing Finance Session ...")
        nlp.Pipeline(get_finance_pipeline()).fullAnnotate("unit")
    

    def test_legal_session(self):
        print("Testing Legal Session ...")
        nlp.Pipeline(get_legal_pipeline()).fullAnnotate("Shwrm")
