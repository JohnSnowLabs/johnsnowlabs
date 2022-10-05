from abc import ABCMeta
from johnsnowlabs.abstract_base.lib_resolver import Py4JJslLibDependencyResolverABC, PyInstallTypes
from johnsnowlabs.utils.enums import ProductName, SparkVersion, JvmHardwareTarget, \
    LatestCompatibleProductVersion
from johnsnowlabs.py_models.url_dependency import UrlDependency


class HcLibResolver(Py4JJslLibDependencyResolverABC, metaclass=ABCMeta):
    has_py_install = True
    has_cpu_jars = True
    has_secret = True
    compatible_spark_versions = [SparkVersion.spark3xx.value]
    lib_version = LatestCompatibleProductVersion.healthcare.value
    product_name = ProductName.hc

    compatible_spark_to_jar_map = {
        SparkVersion.spark3xx: {
            JvmHardwareTarget.cpu:
                UrlDependency(url='https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl-{lib_version}.jar',
                              dependency_type=JvmHardwareTarget.cpu,
                              spark_version=SparkVersion.spark3xx,
                              product_name=product_name,
                              file_name=product_name.name,
                              dependency_version=lib_version)

        }
    }

    compatible_spark_to_py_map = {
        SparkVersion.spark3xx: {
            PyInstallTypes.wheel:
                UrlDependency(
                    url='https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl/spark_nlp_jsl-{lib_version}-py3-none-any.whl',
                    dependency_type=PyInstallTypes.wheel,
                    spark_version=SparkVersion.spark3xx,
                    product_name=product_name,
                    file_name=product_name.name,
                    dependency_version=lib_version),

            PyInstallTypes.tar:
                UrlDependency(
                    url='https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl/spark-nlp-jsl-{lib_version}.tar.gz',
                    dependency_type=PyInstallTypes.tar,
                    spark_version=SparkVersion.spark3xx,
                    product_name=product_name,
                    file_name=product_name.name,
                    dependency_version=lib_version),
        }
    }
