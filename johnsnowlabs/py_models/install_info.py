from typing import Optional, Tuple, Dict, Union, List

from johnsnowlabs import settings
from johnsnowlabs.abstract_base.pydantic_model import WritableBaseModel
# from johnsnowlabs.abstract_base.software_product import AbstractSoftwareProduct
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.enums import ProductName, JvmHardwareTarget, PyInstallTypes
from johnsnowlabs.py_models.lib_version import LibVersion
import os


class InstallFileInfoBase(WritableBaseModel):
    file_name: str
    product: ProductName
    compatible_spark_version: Union[str, LibVersion]
    product_version: Union[str, LibVersion]

    # install_type: Optional[JvmHardwareTarget]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.compatible_spark_version = LibVersion(self.compatible_spark_version)
        self.product_version = LibVersion(self.product_version)


class PyInstallInfo(InstallFileInfoBase):
    install_type: PyInstallTypes


class JvmInstallInfo(InstallFileInfoBase):
    install_type: JvmHardwareTarget


class LocalPyLib(WritableBaseModel):
    py_lib: Optional[PyInstallInfo] = None

    def get_py_path(self):
        if not self.py_lib:
            return False
        if not os.path.exists(f'{settings.py_dir}/{self.py_lib.file_name}'):
            return False
        return f'{settings.py_dir}/{self.py_lib.file_name}'


class LocalPy4JLib(WritableBaseModel):
    java_lib: Optional[JvmInstallInfo] = None
    py_lib: Optional[PyInstallInfo] = None

    def get_java_path(self):
        if not self.java_lib:
            return False
        if not os.path.exists(f'{settings.java_dir}/{self.java_lib.file_name}'):
            return False
        return f'{settings.java_dir}/{self.java_lib.file_name}'

    def get_py_path(self):
        if not self.py_lib:
            return False
        if not os.path.exists(f'{settings.py_dir}/{self.py_lib.file_name}'):
            return False
        return f'{settings.py_dir}/{self.py_lib.file_name}'


class RootInfo(WritableBaseModel):
    version: Union[str, LibVersion]
    run_from: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = LibVersion(self.version)

    @staticmethod
    def get_from_jsl_home():
        return RootInfo.parse_file(settings.root_info_file)


class InstallFolder(WritableBaseModel):
    infos: Dict[str, Union[PyInstallInfo, JvmInstallInfo]]

    def get_product_entry(self, product: ProductName,
                          hardware_target: Optional[Union[PyInstallTypes, JvmHardwareTarget]] = None):
        for file_name, install_info in self.infos.items():
            if install_info.product == product:
                if hardware_target:
                    if install_info.install_type == hardware_target:
                        return install_info
                else:
                    return install_info

    @staticmethod
    def java_folder_from_home():
        if os.path.exists(settings.java_info_file):
            return InstallFolder.parse_file(settings.java_info_file)
        return False

    @staticmethod
    def py_folder_from_home():
        if os.path.exists(settings.py_info_file):
            return InstallFolder.parse_file(settings.py_info_file)
        return False


class InstallSuite(WritableBaseModel):
    info: RootInfo
    secrets: Optional[JslSecrets] = None
    # Py4J Libs
    nlp: LocalPy4JLib
    ocr: Optional[LocalPy4JLib] = None
    hc: Optional[LocalPy4JLib] = None
    # Pure Python Libs
    pure_py_jsl: Optional[LocalPyLib] = None

    def get_missing_products(self, ):
        missing = []
        from johnsnowlabs.auto_install.softwares import Software
        if self.secrets.OCR_LICENSE:
            if not self.ocr.java_lib or not self.ocr.get_java_path():
                missing.append(Software.spark_ocr)
        if self.secrets.HC_LICENSE:
            if not self.hc.java_lib or not self.hc.get_java_path():
                missing.append(Software.spark_hc)
        if not self.nlp.java_lib or not self.nlp.get_java_path():
            missing.append(Software.spark_nlp)
        return missing

    def log_missing_jars(self,
                         should_have_ocr,
                         should_have_hc,
                         should_have_nlp, ):
        print(f'🚨 Looks like some of the missing jars could not be fetched...')
        if not self.ocr.java_lib and self.secrets.OCR_LICENSE and should_have_ocr:
            print(f'🚨 Missing Jar for OCR')
        if not self.hc.java_lib and self.secrets.HC_LICENSE and should_have_hc:
            print(f'🚨 Missing Jar for Medical')
        if not self.nlp.java_lib and should_have_nlp:
            print(f'🚨 Missing Jar for NLP')
