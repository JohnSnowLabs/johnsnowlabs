import importlib
from abc import ABC
from typing import Dict, Union

from johnsnowlabs.py_models.url_dependency import UrlDependency
from johnsnowlabs.utils.enums import *
from johnsnowlabs.py_models.lib_version import LibVersion


def is_spark_version_env(spark_version: str) -> bool:
    import pyspark
    env_spark_version = pyspark.__version__[0:-2].replace(".", "")
    return spark_version in env_spark_version


def try_import_lib(lib: str, print_failure=False):
    try:
        importlib.import_module(lib)
        return True
    except Exception as _:
        if print_failure:
            print(f'Failed to import {lib}. Seems not installed.')


class Py4JJslLibDependencyResolverABC(ABC):
    """
    We define a resolver for all JAR based dependencies
    Each JslLibDependencyResolver util must implement the following :
    - get_jar_urls(lib_version,spark_version_to_match,Optional[secret])->UrlDependency
    - get_mvn_coordinates(lib_version,spark_version_to_match,Optional[secret])->RepoDependency
    - get_python_urls(lib_version,spark_version_to_match,Optional[secret],install_type)->UrlDependency
    - get_pypi_identifier(lib_version,spark_version_to_match,Optional[secret],install_type)->RepoDependency
    - get_lib_version_i

    INVARIANTS :
    2. Jar/Py Dependencies are always Spark version UN-agnostic.
     This is why we have to map pyspark version to jar/py dependencies


    """
    has_gpu_jars: bool = False
    has_cpu_jars: bool = False
    has_m1_jar: bool = False
    has_py_install: bool = False
    has_secret: bool = False
    lib_version: LibVersion
    product_name: ProductName
    # key = Supported Spark Version, Value = Dict  with key=m1/cpu/gpu and value = URL/ URL formatable with secret
    compatible_spark_to_jar_map: Dict[SparkVersion,
                                      Dict[JvmHardwareTarget, UrlDependency]]

    # key = Supported Spark Version, Value = Py Locations
    compatible_spark_to_py_map: Dict[SparkVersion,
                                     Dict[PyInstallTypes, UrlDependency]]

    @classmethod
    def get_dependency_url(cls,
                           install_type: Union[JvmHardwareTarget, PyInstallTypes],
                           spark_version_to_match: Optional[Union[str, LibVersion]],
                           secret: Optional[str] = None,
                           ) -> UrlDependency:

        if install_type in PyInstallTypes:
            return cls.get_py_urls(
                secret=secret, spark_version_to_match=spark_version_to_match, install_type=install_type)
        elif install_type in JvmHardwareTarget:
            return cls.get_jar_urls(
                secret=secret, spark_version_to_match=spark_version_to_match, hardware_target=install_type)
        else:
            raise ValueError(f'Invalid Install type = {install_type} must be JvmHardwareTarget or PyInstallType')

    @classmethod
    def get_url_from_compat_map(cls,
                                compat_map:
                                Dict[SparkVersion,
                                     Dict[Union[JvmHardwareTarget, PyInstallTypes],
                                          UrlDependency]],
                                install_type: Union[JvmHardwareTarget, PyInstallTypes],
                                spark_version_to_match: Optional[Union[str, LibVersion]],
                                secret: Optional[str] = None,
                                suffix: str = '',
                                ) -> UrlDependency:

        spark_version_to_match = cls.resolve_to_spark_lib_version(spark_version_to_match)
        matching_jsl_spark_release = None
        for compatible_spark in compat_map.keys():
            compatible_spark: SparkVersion = compatible_spark
            if compatible_spark.value.equals(spark_version_to_match):
                matching_jsl_spark_release = compatible_spark

        if not matching_jsl_spark_release:
            # Todo make special type of exception and catch?
            # TODO nicer print
            raise Exception(
                f'{cls.product_name.value} does not have any install candidates for'
                f' pyspark=={spark_version_to_match.as_str()} \n'
                f'Please install one of the following Pyspark Versions : {1} TODO')

        if cls.has_secret:
            if settings.enforce_versions:
                url = compat_map[matching_jsl_spark_release][install_type].url.format(
                    secret=secret, lib_version=cls.lib_version.as_str())
            else:
                # Read Version from secret
                url = compat_map[matching_jsl_spark_release][install_type].url.format(
                    secret=secret, lib_version=secret.split('-')[0])

        else:
            if settings.enforce_versions:
                url = compat_map[matching_jsl_spark_release][install_type].url.format(
                    lib_version=cls.lib_version.as_str())
            else:
                # read from updated settings instead of already instantiated Objects, which will not reflect setting updates
                url = compat_map[matching_jsl_spark_release][install_type].url.format(
                    lib_version=LatestCompatibleProductVersion.from_settings(cls.product_name))
                url.replace(cls.lib_version.as_str(), LatestCompatibleProductVersion.from_settings(cls.product_name))

        # NAME-VERSION-INSTALL_TYPE-for-spark-SPARK_VERSION-.[jar/tar/wheel]
        name = f'{cls.product_name.value}-{cls.lib_version.as_str()}' \
               f'-{install_type.name}-for-spark-{matching_jsl_spark_release.value.as_str()}.{suffix}'
        return UrlDependency(url=url,
                             dependency_type=install_type,
                             spark_version=matching_jsl_spark_release,
                             dependency_version=cls.lib_version,
                             file_name=name,
                             product_name=cls.product_name.value)

    @classmethod
    def get_jar_urls(cls,
                     secret: Optional[str] = None,
                     spark_version_to_match: Optional[Union[str, LibVersion]] = None,
                     hardware_target: JvmHardwareTarget = JvmHardwareTarget.cpu,
                     ) -> UrlDependency:
        """
        Get jar URL location for hardware target.
        Jar loc formats with secret+jsl_lib_version for licensed and
         only with jsl-lib_version for open source
        """
        if hardware_target == JvmHardwareTarget.cpu and not cls.has_cpu_jars:
            raise Exception(f'{cls.product_name.value} has no CPU Jars!')

        if hardware_target == JvmHardwareTarget.gpu and not cls.has_gpu_jars:
            raise Exception(f'{cls.product_name.value} has no GPU Jars!')

        if hardware_target == JvmHardwareTarget.m1 and not cls.has_m1_jar:
            raise Exception(f'{cls.product_name.value} has no M1 Jars!')

        return cls.get_url_from_compat_map(compat_map=cls.compatible_spark_to_jar_map,
                                           install_type=hardware_target,
                                           spark_version_to_match=spark_version_to_match,
                                           secret=secret, suffix='jar')

    @classmethod
    def get_py_urls(cls,
                    secret: Optional[str] = None,
                    spark_version_to_match: Optional[Union[str, LibVersion]] = None,
                    install_type: PyInstallTypes = PyInstallTypes.wheel) -> UrlDependency:
        if not cls.has_py_install:
            raise Exception(f'{cls.product_name.value} has no Py Dependencies!')
        return cls.get_url_from_compat_map(compat_map=cls.compatible_spark_to_py_map,
                                           install_type=install_type,
                                           spark_version_to_match=spark_version_to_match,
                                           secret=secret, suffix=install_type.value)

    @classmethod
    def resolve_to_spark_lib_version(cls, spark_version_to_match) -> LibVersion:
        """Get Pyspark version from installed pyspark.
         If not compatible across all libraries, print warning.
         If no pyspark installed, use latest pyspark which is compatible across all libs.
        Uses LatestCompatibleProductVersion for this

        :return: LibVersionIdentifier for the specific Resolver
        """

        # 1. Check if is spark_version_to_match is a string, if yes cast to LibVersion
        if isinstance(spark_version_to_match, str):
            # TODO print warning if spark_version_to_match is not compatible across all libs
            #  in --> Helper func since we need it in get_installed_pyspark_version_or_latest_compatible as well
            return LibVersion(spark_version_to_match)
        # 2. Check if is spark_version_to_match is a LibVersion, if yes return
        elif isinstance(spark_version_to_match, LibVersion):
            return spark_version_to_match
        # 3. Check if is SparkVersion enum
        elif isinstance(spark_version_to_match, SparkVersion):
            return spark_version_to_match.value
        # 3. Check if is spark_version_to_match is some other type, if yes raise exception, should not happen
        elif spark_version_to_match:
            raise ValueError(
                f'Invalid Type for spark_version_to_match, '
                f'must be either str in format A.B.C, None or Libversion'
                f'But type is ={type(spark_version_to_match)}')

        # 4. Check if is pyspark is installed
        elif try_import_lib('pyspark'):
            import pyspark
            # TODO check product wide compatibility for pre-installed pyspark --> make helper method for that
            return LibVersion(pyspark.__version__)
        # 5. Return the latest compatible pyspark if no other method  resolves
        else:
            return LatestCompatibleProductVersion.pyspark.value
