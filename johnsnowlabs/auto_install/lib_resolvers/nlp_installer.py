from typing import Optional
from abc import ABCMeta

from johnsnowlabs.abstract_base.lib_resolver import (
    Py4JJslLibDependencyResolverABC,
    PyInstallTypes,
)
from johnsnowlabs.py_models.url_dependency import (
    UrlDependency,
    local_file_name_from_url,
)
from johnsnowlabs.utils.enums import (
    LatestCompatibleProductVersion,
    ProductName,
    SparkVersion,
    JvmHardwareTarget,
)


def _pypi_artifact_url(pypi_name: str, version: str, install_type) -> Optional[str]:
    # PyPI file paths carry a per-file hash, so they cannot be templated from the version
    import json
    import urllib.request

    want = "sdist" if getattr(install_type, "name", "") == "tar" else "bdist_wheel"
    try:
        with urllib.request.urlopen(
            f"https://pypi.org/pypi/{pypi_name}/{version}/json", timeout=60
        ) as r:
            for f in json.load(r).get("urls", []):
                if f.get("packagetype") == want:
                    return f.get("url")
    except Exception as e:
        print(f"Warning: could not look up {pypi_name}=={version} on PyPI: {e}")
    return None


class NlpLibResolver(Py4JJslLibDependencyResolverABC, metaclass=ABCMeta):
    has_m1_jar = True
    has_aarch_jar = True
    has_cpu_jars = True
    has_py_install = True
    has_gpu_jars = True
    product_name = ProductName.nlp
    lib_version = LatestCompatibleProductVersion.spark_nlp.value
    compatible_spark_versions = [SparkVersion.spark3xx.value]

    compatible_spark_to_jar_map = {
        SparkVersion.spark3xx: {
            JvmHardwareTarget.aarch: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-aarch64-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.aarch,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.gpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-gpu-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.gpu,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.m1: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-silicon-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.m1,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.cpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.cpu,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
        SparkVersion.spark400: {
            JvmHardwareTarget.aarch: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-aarch64-spark400-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.aarch,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.gpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-gpu-spark400-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.gpu,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.m1: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-silicon-spark400-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.m1,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.cpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-spark400-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.cpu,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
        SparkVersion.spark4xx: {
            JvmHardwareTarget.aarch: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-aarch64-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.aarch,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.gpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-gpu-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.gpu,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.m1: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-silicon-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.m1,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            JvmHardwareTarget.cpu: UrlDependency(
                url="https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/scala-2.13/spark-nlp-assembly-{lib_version}.jar",
                dependency_type=JvmHardwareTarget.cpu,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
    }

    compatible_spark_to_py_map = {
        SparkVersion.spark3xx: {
            # TODO HARDCODE HASH!!! OR grap from enum or somwhere comfy. Maybe configs/settings file?
            PyInstallTypes.wheel: UrlDependency(
                url="https://files.pythonhosted.org/packages/65/19/c439d42f7afd75d6c9c20207db8ee0c95d7c82177b759303c7601120e91a/spark_nlp-{lib_version}-py2.py3-none-any.whl",
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            PyInstallTypes.tar: UrlDependency(
                url="https://files.pythonhosted.org/packages/62/86/6b6c79f923db6ece28dd1c96d088fd2cc01ef7c748021ecb5fe73355635a/spark-nlp-{lib_version}.tar.gz",
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark3xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
        # Same wheel every lane, but the resolver still needs a key per lane.
        SparkVersion.spark400: {
            PyInstallTypes.wheel: UrlDependency(
                url="https://files.pythonhosted.org/packages/65/19/c439d42f7afd75d6c9c20207db8ee0c95d7c82177b759303c7601120e91a/spark_nlp-{lib_version}-py2.py3-none-any.whl",
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            PyInstallTypes.tar: UrlDependency(
                url="https://files.pythonhosted.org/packages/62/86/6b6c79f923db6ece28dd1c96d088fd2cc01ef7c748021ecb5fe73355635a/spark-nlp-{lib_version}.tar.gz",
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark400,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
        SparkVersion.spark4xx: {
            PyInstallTypes.wheel: UrlDependency(
                url="https://files.pythonhosted.org/packages/65/19/c439d42f7afd75d6c9c20207db8ee0c95d7c82177b759303c7601120e91a/spark_nlp-{lib_version}-py2.py3-none-any.whl",
                dependency_type=PyInstallTypes.wheel,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
            PyInstallTypes.tar: UrlDependency(
                url="https://files.pythonhosted.org/packages/62/86/6b6c79f923db6ece28dd1c96d088fd2cc01ef7c748021ecb5fe73355635a/spark-nlp-{lib_version}.tar.gz",
                dependency_type=PyInstallTypes.tar,
                spark_version=SparkVersion.spark4xx,
                product_name=product_name,
                file_name=product_name.name,
                dependency_version=lib_version,
            ),
        },
    }

    @classmethod
    def get_py_urls(
        cls,
        secret=None,
        spark_version_to_match=None,
        install_type=PyInstallTypes.wheel,
    ) -> UrlDependency:
        dep = super().get_py_urls(
            secret=secret,
            spark_version_to_match=spark_version_to_match,
            install_type=install_type,
        )
        real = _pypi_artifact_url("spark-nlp", cls.lib_version.as_str(), install_type)
        if real:
            dep.update_url(real)
            dep.file_name = local_file_name_from_url(real)
        return dep
