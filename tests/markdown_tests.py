import os
import unittest

from johnsnowlabs.utils.file_utils import file_to_str
from johnsnowlabs.utils.modelhub_markdown import test_markdown
from johnsnowlabs.utils.notebooks import test_ipynb
from johnsnowlabs import start
from johnsnowlabs import *
from johnsnowlabs import *


# lxml
class MarkdownTestTestCase(unittest.TestCase):
    def test_remote_markdown(self):
        nb_to_test = [
            'https://nlp.johnsnowlabs.com/2022/09/02/legner_roberta_zeroshot_en.html',
            'https://nlp.johnsnowlabs.com/2022/08/31/legpipe_deid_en.html',
            'https://nlp.johnsnowlabs.com/2022/10/02/legner_bert_large_courts_de.html',
        ]
        for n in nb_to_test:
            print(test_markdown(n))

    def test_local_markdown(self):
        url = 'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp/master/docs/_posts/josejuanmartinez/2022-08-30-legmulticlf_edgar_en.md'
        os.system(f'wget {url}')
        print(test_markdown('2022-08-30-legmulticlf_edgar_en.md'))

    def test_folder_of_markdown(self):
        urls = [
            'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp/master/docs/_posts/josejuanmartinez/2022-02-14-clinical_deidentification_es.md',
            'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp/master/docs/_posts/josejuanmartinez/2022-02-15-ner_deid_generic_augmented_es.md',
            'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp/master/docs/_posts/josejuanmartinez/2022-08-30-legmulticlf_edgar_en.md', ]
        for u in urls:
            os.system(f'wget {u}')
        test_markdown(os.getcwd())

if __name__ == '__main__':
    unittest.main()
