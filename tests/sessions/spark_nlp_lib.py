import os
import sys
import unittest

from johnsnowlabs import nlp
from johnsnowlabs.auto_install.softwares import (SparkHcSoftware,
                                                 SparkNlpSoftware,
                                                 SparkOcrSoftware)
from tests.utils import clear_installed_jsl_installation

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable



def setUpModule():
    nlp.install(browser_login=False, spark_nlp=True, nlp=False, visual=False)


def tearDownModule():
    clear_installed_jsl_installation()


class InstallationTestCase(unittest.TestCase):
    def test_only_spark_nlp_should_be_installed_if_secrets_are_empty(self):
        
        installed_products = nlp.check_health()

        self.assertTrue(installed_products[SparkNlpSoftware])
        self.assertFalse(installed_products[SparkHcSoftware])
        self.assertFalse(installed_products[SparkOcrSoftware])

class SparkSessionTestCase(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        cls.spark = nlp.start()

    def test_sparknlp_session(self):
        print("Start test_spark_nlp_session")
        d = nlp.DocumentAssembler().setInputCol("text").setOutputCol("doc")
        t = nlp.Tokenizer().setInputCols("doc").setOutputCol("tok")
        c = (
                    nlp.DeBertaForTokenClassification()
                    .setInputCols(["tok", "doc"])
                    .setOutputCol("class")
                )
        p = nlp.Pipeline(stages=[d, t])
        p = nlp.to_nlu_pipe(p)
        print(p.predict("Hello World"))

    def test_sparknlp_gpu_session(self):
        print("Start test_spark_nlp_gpu_session")
        self.spark = nlp.start(hardware_target="gpu")
        d = nlp.DocumentAssembler().setInputCol("text").setOutputCol("doc")
        t = nlp.Tokenizer().setInputCols("doc").setOutputCol("tok")
        c = (
            nlp.DeBertaForTokenClassification()
            .setInputCols(["tok", "doc"])
            .setOutputCol("class")
        )
        p = nlp.Pipeline(stages=[d, t])
        p = nlp.to_nlu_pipe(p)
        print(p.predict("Hello form John SNow labs"))

