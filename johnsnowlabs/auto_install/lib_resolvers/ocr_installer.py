from abc import ABCMeta

from johnsnowlabs.abstract_base.lib_resolver import (
    Py4JJslLibDependencyResolverABC,
    PyInstallTypes,
)
from johnsnowlabs.py_models.url_dependency import UrlDependency
from johnsnowlabs.utils.enums import (
    LatestCompatibleProductVersion,
    ProductName,
    SparkVersion,
    JvmHardwareTarget,
)


class OcrLibResolver(Py4JJslLibDependencyResolverABC, metaclass=ABCMeta):
    has_cpu_jars = True
    has_py_install = True
    has_secret = True
    product_name = ProductName.ocr
    compatible_spark_versions = [
        SparkVersion.spark32x.value,
        SparkVersion.spark33x.value,
    ]
    lib_version = LatestCompatibleProductVersion.ocr.value

    compatible_spark_to_jar_map = {
        SparkVersion.spark3xx: {
            JvmHardwareTarget.cpu: UrlDependency(
                url="https://pypi.johnsnowlabs.com/{secret}/jars/spark-ocr-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.cpu,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
    }

    compatible_spark_to_py_map = {
        SparkVersion.spark3xx: {
            PyInstallTypes.wheel: UrlDependency(
                url="https://pypi.johnsnowlabs.com/{secret}/spark-ocr/spark_ocr-{lib_version}-py3-none-any.whl",
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark32x,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            PyInstallTypes.tar: UrlDependency(
                url="https://pypi.johnsnowlabs.com/{secret}/spark-ocr/spark-ocr-{lib_version}.tar.gz",
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark32x,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
    }
