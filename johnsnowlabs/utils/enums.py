from dataclasses import dataclass
from typing import Optional

from johnsnowlabs import settings

from johnsnowlabs.abstract_base.base_enum import BaseEnum
from johnsnowlabs.py_models.primitive import LibVersionIdentifier
from johnsnowlabs.py_models.lib_version import LibVersion


class DatabricksClusterStates(BaseEnum):
    # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    RESTARTING = 'RESTARTING'
    RESIZING = 'RESIZING'
    TERMINATING = 'TERMINATING'
    TERMINATED = 'TERMINATED'
    ERROR = 'ERROR'
    UNKNOWN = 'UNKNOWN'


class JvmHardwareTarget(BaseEnum):
    gpu = 'gpu'
    cpu = 'cpu'
    m1 = 'm1'
    aarch = 'aarch'

    @classmethod
    def bool_choice_to_hardware(cls, gpu: bool = False, cpu: bool = False, m1: bool = False) -> 'JvmHardwareTarget':
        if gpu:
            return cls.gpu
        elif cpu:
            return cls.cpu
        elif m1:
            return cls.m1
        else:
            return cls.cpu

    @staticmethod
    def from_str(s):
        if s not in JvmHardwareTarget:
            bck = "\n"
            raise Exception(f'Invalid value for jvm_install_type: {s}'
                            f' please specify on of:\n{bck.join([n.value for n in JvmHardwareTarget])}')
        else:
            return JvmHardwareTarget(s)


class PyInstallTypes(BaseEnum):
    tar = 'tar.gz'
    wheel = 'whl'

    @staticmethod
    def from_str(s):
        bck = "\n"
        if s not in PyInstallTypes:
            raise Exception(f'Invalid value for py_install_type: {s}'
                            f' please specify on of:\n{bck.join([n.value for n in PyInstallTypes])}')
        else:
            return PyInstallTypes(s)


class SparkVersion(BaseEnum):
    # Broad versions
    spark3xx = LibVersion('3.x.x')
    spark31x = LibVersion('3.1.x')
    spark32x = LibVersion('3.2.x')
    spark33x = LibVersion('3.3.x')
    spark330 = LibVersion('3.3.0')
    spark322 = LibVersion('3.2.2')
    spark321 = LibVersion('3.2.1')
    spark320 = LibVersion('3.2.0')
    spark313 = LibVersion('3.1.3')
    spark312 = LibVersion('3.1.2')
    spark311 = LibVersion('3.1.1')
    spark303 = LibVersion('3.0.3')
    spark302 = LibVersion('3.0.2')
    spark301 = LibVersion('3.0.1')
    spark300 = LibVersion('3.0.0')


# hc = LibVersion('4.0.2')
# nlp = LibVersion('4.0.2')
# ocr = LibVersion('4.0.0')
# nlp_display = LibVersion('4.0.0')
# nlu = LibVersion('4.0.0')




class LicenseType(BaseEnum):
    trial = 'Trial'
    research = 'Research'


class LicensePlattform(BaseEnum):
    none = None
    databricks = 'Databricks'
    floating = 'Floating'


class LicensePlattform(BaseEnum):
    none = None
    research = 'Research'


class ProductName(BaseEnum):
    hc = 'Spark-Healthcare'
    nlp = 'Spark-NLP'
    ocr = 'Spark-OCR'
    finance = 'Spark-Finance'
    nlp_display = 'NLP-Display'
    nlu = 'nlu'
    jsl_full = 'full'
    pyspark = 'PySpark'
    spark = 'spark'
    java = 'java'
    python = 'python'
    jsl_lib = 'John Snow Labs Python Library'

    @staticmethod
    def from_str(s):
        bck = "\n"
        if s not in ProductName:
            raise Exception(f'Invalid Product to install: {s}'
                            f' please specify on of:\n{bck.join([n.value for n in ProductName])}')
        else:
            return ProductName(s)

    @staticmethod
    def from_jsl_api(s: str):
        if s == 'Visual NLP':
            return ProductName.ocr
        if s == 'Healthcare NLP':
            return ProductName.hc
        if s == 'Spark NLP':
            return ProductName.hc
        if s == 'Finance NLP':
            return ProductName.hc
        if s == 'Legal NLP':
            return ProductName.hc


        raise ValueError(f'Unknown product name from jsl-api {s}')


class ProductLogo(BaseEnum):
    hc = '💊'  # 🏥 🩺 💊 ❤️ ‍🩹 ‍⚕️💉 🥼 🚑 🔬 🫀 🩻 🧪
    nlp = '🚀'
    ocr = '🕶'  # 👁️  🤖 🦾🦿 🥽 👀 🕶 🥽 ⚕
    finance = '🤑'  # 🤑🏦💲💳💰💸💵💴💶💷
    nlp_display = '🎨'
    nlu = '🤖'
    jsl_full = '💯🕴'  # 🕴
    java = '🫘'  # 🫘 # ☕ ♨ 🥃 🥃 🧋🍹♨️🥤🫖
    python = '🐍'  # 🐉
    pyspark = '🐍+⚡'
    spark = '⚡ '
    databricks = '🧱'
    jsl_lib = '🧪'


class ProductSlogan(BaseEnum):
    healthcare = 'Heal the planet with NLP!'
    spark_nlp = 'State of the art NLP at scale'
    ocr = 'Empower your NLP with a set of eyes'
    pyspark = 'The big data Engine'
    nlu = '1 line of code to conquer nlp!'
    jsl_full = 'The entire John Snow Labs arsenal!'
    finance = 'NLP for the Finance Industry'
    nlp_display = 'Visualize and Explain NLP!'
    jsl_lib = 'Easy access to all of John Snow Labs Enterprise Software!'
    spark = '⚡'
    java = '☕'
    python = '🐍'


@dataclass
class InstalledProductInfo:
    """Representation of a JSL product install. Version is None if not installed  """
    product: ProductName
    version: Optional[LibVersionIdentifier] = None


@dataclass
class JslSuiteStatus:
    """Representation and install status of all JSL products and its dependencies.
    Version attribute of InstalledProductInfo is None for uninstalled products
    """
    spark_nlp_info: Optional[InstalledProductInfo] = None
    spark_hc_info: Optional[InstalledProductInfo] = None
    spark_ocr_info: Optional[InstalledProductInfo] = None
    nlu_info: Optional[InstalledProductInfo] = None
    sparknlp_display_info: Optional[InstalledProductInfo] = None
    pyspark_info: Optional[InstalledProductInfo] = None


class LatestCompatibleProductVersion(BaseEnum):
    jsl_lib = LibVersion(settings.raw_version_jsl_lib)
    healthcare = LibVersion(settings.raw_version_medical)
    spark_nlp = LibVersion(settings.raw_version_nlp)
    ocr = LibVersion(settings.raw_version_ocr)
    nlu = LibVersion(settings.raw_version_nlu)
    nlp_display = LibVersion(settings.raw_version_nlp_display)
    pyspark = LibVersion(settings.raw_version_pyspark)
    finance = LibVersion('finance')
    spark = LibVersion(settings.raw_version_pyspark)
    java = LibVersion('java')
    python = LibVersion('python')

    @staticmethod
    def from_settings(p : ProductName):
        if p == ProductName.hc:
            return settings.raw_version_medical
        if p == ProductName.ocr:
            return settings.raw_version_ocr
        if p == ProductName.nlp:
            return settings.raw_version_nlp

    @staticmethod
    def sct_from_settings(p : ProductName):
        if p == ProductName.hc:
            return settings.raw_version_secret_medical
        if p == ProductName.ocr:
            return settings.raw_version_secret_ocr
        if p == ProductName.nlp:
            return settings.raw_version_nlp
