import unittest

from johnsnowlabs.utils.file_utils import file_to_str
from johnsnowlabs.utils.notebooks import test_ipynb
from johnsnowlabs import start
from johnsnowlabs import *
from johnsnowlabs import *

# lxml
class WorkshopNotebookTestCase(unittest.TestCase):
    def test_remote_notebook(self):
        ocr_5 = 'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Certification_Trainings/Healthcare/5.Spark_OCR.ipynb'
        ocr_51 = 'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Certification_Trainings/Healthcare/5.1.Spark_OCR_Multi_Modals.ipynb'
        ocr_52 = 'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Certification_Trainings/Healthcare/5.2.Spark_OCR_Deidentification.ipynb'
        nb_to_test = [
            ocr_5,
            ocr_51,
            ocr_52,
        ]
        for n in nb_to_test:
            test_ipynb(n)

    def test_download_workshop_repo_and_run(self):
        res = test_ipynb('WORKSHOP-FIN')
        res.to_csv('WORKSHOP-FIN.csv',index=False)

    def test_folder_of_notebooks(self):
        folder = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tmp/nb_tests/latest_workshop/johnsnowlabs v1.0/Finance'
        res.to_csv('WORKSHOP-FIN.csv',index=False)

    def test_local_notebook(self):
        pass

    def test_parse(self):
        import ast
        f = '/home/ckl/.johnsnowlabs/tmp_tests/notebook_tests/5.2.Spark_OCR_Deidentification.ipynb.nb_converted.py'
        from ast import Expr
        a = ast.parse(file_to_str(f))

    bad_regex = [

    ]









    def test_nerModel(self):
        jsl.start()
        from sparknlp_jsl.finance import FinanceNerModel
        m = FinanceNerModel.pretrained("finner_deid", "en", 'finance/models')
        print("FOUND",m)







    def test_quick(self):
        s = """
        
spark = sparkocr.start(secret=SPARK_OCR_SECRET, 
                       nlp_version=PUBLIC_VERSION,
                       nlp_secret=SECRET,
                       nlp_internal=JSL_VERSION
                       )
        """

        r = r'sparkocr.start\(.*\)'
        import re
        print(re.findall(r, s, re.DOTALL))


if __name__ == '__main__':
    unittest.main()
