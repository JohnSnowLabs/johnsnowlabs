from typing import Union

from johnsnowlabs.auto_install.lib_resolvers import OcrLibResolver, HcLibResolver, NlpLibResolver
from johnsnowlabs.abstract_base.software_product import AbstractSoftwareProduct
from johnsnowlabs.utils.enums import ProductName, ProductLogo, LatestCompatibleProductVersion, \
    ProductSlogan
from johnsnowlabs.utils.env_utils import try_import
from johnsnowlabs.utils.venv_utils import VenvWrapper

"""
These are the nodes and edges that define the DAG graph for the check_and_install_dependencies() in install_software.py
"""


class PythonSoftware(AbstractSoftwareProduct):
    name = ProductName.python.value
    logo = ProductLogo.python.value
    latest_version = LatestCompatibleProductVersion.python.value


class JavaSoftware(AbstractSoftwareProduct):
    name = ProductName.java.value
    logo = ProductLogo.java.java
    latest_version = LatestCompatibleProductVersion.java.value


class SparkSoftware(AbstractSoftwareProduct):
    name = ProductName.spark.value
    logo = ProductLogo.spark.value
    hard_dependencies = {JavaSoftware}
    latest_version = LatestCompatibleProductVersion.spark.value


class PysparkSoftware(AbstractSoftwareProduct):
    # TODO needs custom install for windows! (?)
    name = ProductName.pyspark.value
    logo = ProductLogo.pyspark.value
    slogan = ProductSlogan.pyspark.value
    hard_dependencies = {PythonSoftware}
    latest_version = LatestCompatibleProductVersion.pyspark.value
    py_module_name = 'pyspark'
    pypi_name = 'pyspark'

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import pyspark
            return pyspark.__version__
        except:
            return False


class SparkNlpSoftware(AbstractSoftwareProduct):
    name = ProductName.nlp.value
    logo = ProductLogo.nlp.value
    slogan = ProductSlogan.spark_nlp.value
    hard_dependencies = {SparkSoftware, PysparkSoftware}
    latest_version = LatestCompatibleProductVersion.spark_nlp.value
    jsl_url_resolver = NlpLibResolver
    py_module_name = 'sparknlp'
    pypi_name = 'spark-nlp'
    is_py4j = True

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import sparknlp
            return sparknlp.version()
        except:
            return False


class SparkHcSoftware(AbstractSoftwareProduct):
    name = ProductName.hc.value
    logo = ProductLogo.hc.value
    slogan = ProductSlogan.healthcare.value
    hard_dependencies = {SparkNlpSoftware}
    latest_version = LatestCompatibleProductVersion.healthcare.value
    jsl_url_resolver = HcLibResolver
    py_module_name = 'sparknlp_jsl'
    pypi_name = 'spark-nlp-jsl'
    licensed = True
    is_py4j = True

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import sparknlp_jsl
            return sparknlp_jsl.version()
        except:
            return False


class SparkOcrSoftware(AbstractSoftwareProduct):
    name = ProductName.ocr.value
    logo = ProductLogo.ocr.value
    slogan = ProductSlogan.ocr.value
    hard_dependencies = {SparkSoftware, PysparkSoftware, SparkNlpSoftware, }
    optional_dependencies = {SparkHcSoftware}
    latest_version = LatestCompatibleProductVersion.ocr.value
    jsl_url_resolver = OcrLibResolver
    py_module_name = 'sparkocr'  #
    pypi_name = 'spark-ocr'
    licensed = True
    is_py4j = True

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import sparkocr
            return sparkocr.version()
        except:
            return False


class NlpDisplaySoftware(AbstractSoftwareProduct):
    name = ProductName.nlp_display.value
    logo = ProductLogo.nlp_display.value
    slogan = ProductSlogan.nlp_display.value
    hard_dependencies = {SparkSoftware}
    licensed_dependencies = {SparkHcSoftware}
    latest_version = LatestCompatibleProductVersion.nlp_display.value
    py_module_name = 'sparknlp_display'
    pypi_name = 'spark-nlp-display'

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import sparknlp_display
            return sparknlp_display.version()
        except:
            return False


class NluSoftware(AbstractSoftwareProduct):
    name = ProductName.nlu.value
    logo = ProductLogo.nlu.value
    slogan = ProductSlogan.nlu.value

    hard_dependencies = {SparkNlpSoftware}
    licensed_dependencies = {SparkHcSoftware, SparkOcrSoftware}
    optional_dependencies = {NlpDisplaySoftware}  # Todo streamlit,sklearn,plotly, nlp-display
    latest_version = LatestCompatibleProductVersion.nlu.value
    py_module_name = 'nlu'
    pypi_name = 'nlu'

    @classmethod
    def get_installed_version_via_import(cls):
        try:
            import nlu
            return nlu.version()
        except:
            return False

    @classmethod
    def health_check(cls) -> bool:
        import nlu
        try:
            pipe = nlu.load('sentiment')
            df = pipe.predict('I love peanut butter and jelly!')
            for c in df.columns:
                print(df[c])
        except Exception as err:
            print(f'Failure testing nlu. Err = {err}')
            return False
        return True


class JohnSnowLabsSoftware(AbstractSoftwareProduct):
    # Represents this Library itself
    name = ProductName.jsl_lib.value
    logo = ProductLogo.jsl_lib.value
    slogan = ProductSlogan.jsl_lib.value

    hard_dependencies = {SparkNlpSoftware}
    licensed_dependencies = {SparkHcSoftware, SparkOcrSoftware}
    optional_dependencies = {NlpDisplaySoftware, NluSoftware}
    latest_version = LatestCompatibleProductVersion.jsl_lib.value
    py_module_name = 'johnsnowlabs'
    pypi_name = 'johnsnowlabs'
    pypi_name_databricks = 'johnsnowlabs_for_databricks'

class JslFullSoftware(AbstractSoftwareProduct):
    name = ProductName.jsl_full.value
    logo = ProductLogo.jsl_full.value
    slogan = ProductSlogan.jsl_full.value

    optional_dependencies = {NlpDisplaySoftware, NluSoftware}  # Todo streamlit,sklearn,plotly?
    hard_dependencies = {JohnSnowLabsSoftware, SparkNlpSoftware, PysparkSoftware}
    licensed_dependencies = {SparkHcSoftware, SparkOcrSoftware}

    @classmethod
    def check_installed(cls, python_exec_path=None) -> bool:
        if python_exec_path:
            return VenvWrapper.is_lib_in_py_exec(python_exec_path, cls.py_module_name, False)
        # If python_exec_path=None, then check is for current Python py_executable
        return all(try_import(dep.py_module_name) for dep in cls.licensed_dependencies)


class Software:
    """Accessor to all classes that implement AbstractSoftwareProduct.
     This also gives access to all enums
     """
    spark_nlp: AbstractSoftwareProduct = SparkNlpSoftware
    spark_hc: AbstractSoftwareProduct = SparkHcSoftware
    spark_ocr: AbstractSoftwareProduct = SparkOcrSoftware
    nlu: AbstractSoftwareProduct = NluSoftware
    sparknlp_display: AbstractSoftwareProduct = NlpDisplaySoftware
    pyspark: AbstractSoftwareProduct = PysparkSoftware
    python: AbstractSoftwareProduct = PythonSoftware
    java: AbstractSoftwareProduct = JavaSoftware
    spark: AbstractSoftwareProduct = SparkSoftware
    jsl_lib: AbstractSoftwareProduct = JohnSnowLabsSoftware
    jsl_full: AbstractSoftwareProduct = JslFullSoftware

    @staticmethod
    def for_name(name: Union[str, ProductName]) -> AbstractSoftwareProduct:
        if isinstance(name, str):
            name = ProductName.from_str(name)

        if name == ProductName.nlp:
            return Software.spark_nlp
        elif name == ProductName.hc:
            return Software.spark_hc
        elif name == ProductName.ocr:
            return Software.spark_ocr
        elif name == ProductName.nlu:
            return Software.nlu
        elif name == ProductName.nlp_display:
            return Software.sparknlp_display
        elif name == ProductName.pyspark:
            return Software.pyspark
        elif name == ProductName.python:
            return Software.python
        elif name == ProductName.java:
            return Software.java
        elif name == ProductName.spark:
            return Software.spark
        elif name == ProductName.jsl_lib:
            return Software.jsl_lib
        elif name == ProductName.jsl_full:
            return Software.jsl_full
        return False  # raise ValueError(old_lic'Unknown Product {name}')
