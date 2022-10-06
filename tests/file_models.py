from johnsnowlabs import *
import unittest

from johnsnowlabs import settings

from johnsnowlabs.py_models.install_info import  InstallFolder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = '/home/ckl/.johnsnowlabs/java_installs/info2.json'
        p = '/home/ckl/.johnsnowlabs/java_installs/info3.json'
        info = FolderInfoV2.parse_file(p)
        print(info)
        print('_'*20)
        j = info.json(indent=4)
        print(j)

        p = '/home/ckl/.johnsnowlabs/java_installs/info9.json'
        info.write(p,indent=4)

    def test_parse_install_folder(self):
        f = '/home/ckl/old_home/ckl/Documents/freelance/johnsnowlabs_lib/tests/utils/spark_nlp_ocr_hc.json'
        # jsl.install()
        java_info = InstallFolder.parse_file(settings.java_info_file)
        print(java_info)
        py_info = InstallFolder.parse_file(settings.py_info_file)

if __name__ == '__main__':
    unittest.main()
