import os
from abc import ABC
from typing import List, Set, Optional
import sys
import pkg_resources
from johnsnowlabs import settings
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.py_models.lib_version import LibVersion

from johnsnowlabs.abstract_base.lib_resolver import Py4JJslLibDependencyResolverABC
from johnsnowlabs.utils.enums import ProductName, ProductLogo, ProductSlogan, \
    SparkVersion
from johnsnowlabs.py_models.primitive import LibVersionIdentifier
from johnsnowlabs.utils.env_utils import try_import, try_import_in_venv
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.pip_utils import install_standard_pypi_lib, install_licensed_pypi_lib, get_pip_lib_version
from johnsnowlabs.utils.venv_utils import VenvWrapper


class AbstractSoftwareProduct(ABC):
    """Only first degree dependencies may be contained in the hard/licensed/optional/ dependency lists
     Higher degree dependencies will be resolved by iterating the dependency graph
     By default the ABC implements a check_installed based on import.

     """
    name: ProductName
    logo: ProductLogo
    slogan: Optional[ProductSlogan] = None
    hard_dependencies: Set['AbstractSoftwareProduct'] = set()
    licensed_dependencies: Set['AbstractSoftwareProduct'] = set()
    optional_dependencies: Set['AbstractSoftwareProduct'] = set()
    py_module_name: Optional[str] = None
    pypi_name: Optional[str] = None
    # Only defined for JSL libs below
    compatible_spark_versions: List[SparkVersion]
    latest_version: Optional[LibVersion] = None
    jsl_url_resolver: Optional[Py4JJslLibDependencyResolverABC] = None
    licensed: bool = False
    is_py4j = False
    pypi_name_databricks: Optional[str] = None

    @classmethod
    def get_installed_version_via_import(cls):
        return False

    @classmethod
    def check_installed(cls, python_exec_path: Optional[str] = sys.executable, download_folder: str = None) -> bool:
        if cls.pypi_name and download_folder:
            for whl in os.listdir(download_folder):
                # whl file names re-name '-' to '_'
                if cls.pypi_name.replace('-', '_') in whl:
                    return True

        if cls.py_module_name and not python_exec_path:
            return try_import(cls.py_module_name)
        elif python_exec_path:
            return VenvWrapper.is_lib_in_py_exec(python_exec_path, cls.py_module_name, False)

        # print(f'Assuming {cls.name} is installed, no checks defined.')
        return True

    @classmethod
    def check_installed_correct_version(cls, python_exec_path: str = sys.executable,
                                        download_folder: str = None) -> bool:
        # Only supported for current Py Exec Path, return True otherwise
        if python_exec_path != sys.executable:
            return True
        if download_folder:
            return True
        if not cls.pypi_name:
            return False
        if not cls.latest_version:
            return True
        if not cls.check_installed(python_exec_path=python_exec_path, download_folder=download_folder):
            return False
        try:
            if pkg_resources.get_distribution(cls.pypi_name).version == cls.latest_version.as_str():
                # print(f'👌 Installed version for {cls.logo + cls.name} is correct, no changes made.')
                return True
            else:
                # print(f'🤓 Installed version for {cls.logo + cls.name} is incorrect, '
                #       f'should be {cls.latest_version.as_str()} but is {pkg_resources.get_distribution(cls.pypi_name).version} '
                #       f'upgrading the package')

                return False
        except Exception as err:
            v = get_pip_lib_version(lib=cls.pypi_name, py_exec=python_exec_path)
            if v:
                return v.as_str() == cls.latest_version.as_str()
            return False

    @classmethod
    def get_installed_version(cls, python_exec_path: str = sys.executable,
                              download_folder: str = None,
                              prefer_pip=False,
                              fallback_import=False) -> bool:
        # Only supported for current Py Exec Path, return True otherwise
        if not prefer_pip:
            try:
                return pkg_resources.get_distribution(cls.pypi_name).version
            except:
                pass
        v = get_pip_lib_version(lib=cls.pypi_name, py_exec=python_exec_path)
        if v:
            return v.as_str()
        else:
            return cls.get_installed_version_via_import()

    @classmethod
    def check_dependencies(cls, python_exec_path=None) -> bool:
        # print(f'Assuming {cls.name} dependencies are fine, no checks defined.')
        return True

    @classmethod
    def health_check(cls) -> bool:
        # print(f'Assuming {cls.name} is ok, no checks defined.')
        return True

    @classmethod
    def install(cls,
                secrets: Optional[JslSecrets] = None,
                py_path=sys.executable,
                upgrade=True,
                re_install=False,
                version: Optional[str] = None,
                download_folder: Optional[str] = None,
                include_dependencies: bool = True,
                ) -> bool:
        """
        Install the product with default settings.
        Defaults to Pypi file_name install.

        -m pip download <module> -d path
        """
        if not version and cls.latest_version:
            version = cls.latest_version
        if cls.pypi_name:
            if cls.is_py4j and settings.enforce_versions:
                #  p4j lib should have jars/wheels for it in ~/.johnsnowlabs
                # Try using suite whl before attempting to install from remote location
                # Unless we toggle enforce_versions=False
                suite = get_install_suite_from_jsl_home()
                if cls.name == ProductName.hc.value and suite.hc and suite.hc.py_lib:
                    return install_standard_pypi_lib(f'{settings.py_dir}/{suite.hc.py_lib.file_name}',
                                                     cls.py_module_name,
                                                     python_path=py_path, upgrade=upgrade, re_install=re_install,
                                                     # version=version,
                                                     download_folder=download_folder,
                                                     include_dependencies=include_dependencies,
                                                     )
                elif cls.name == ProductName.ocr.value and suite.ocr and suite.ocr.py_lib:
                    return install_standard_pypi_lib(f'{settings.py_dir}/{suite.ocr.py_lib.file_name}',
                                                     cls.py_module_name,
                                                     python_path=py_path, upgrade=upgrade, re_install=re_install,
                                                     # version=version,
                                                     download_folder=download_folder,
                                                     include_dependencies=include_dependencies, )
                elif cls.name == ProductName.nlp.value and suite.nlp and suite.nlp.py_lib:
                    return install_standard_pypi_lib(f'{settings.py_dir}/{suite.nlp.py_lib.file_name}',
                                                     cls.py_module_name,
                                                     python_path=py_path, upgrade=upgrade, re_install=re_install,
                                                     # version=version,
                                                     download_folder=download_folder,
                                                     include_dependencies=include_dependencies, )
            if secrets and cls.licensed:
                # Licensed is versioned via the secrets
                # Fallback install if we could not find locally
                return install_licensed_pypi_lib(secrets=secrets,
                                                 pypi_name=cls.pypi_name,
                                                 module_name=cls.py_module_name,
                                                 product=cls,
                                                 py_path=py_path,
                                                 download_folder=download_folder,
                                                 include_dependencies=include_dependencies,
                                                 )
            else:
                return install_standard_pypi_lib(cls.pypi_name, cls.py_module_name,
                                                 python_path=py_path, upgrade=upgrade, re_install=re_install,
                                                 download_folder=download_folder,
                                                 version=version,
                                                 include_dependencies=include_dependencies, )
        # raise NotImplemented(f'No install defined for {cls.file_name}')
        return True

    @classmethod
    def install_cli(cls, ) -> bool:
        """
        Install the product configurable interactive from CLI
        """
        if cls.pypi_name:
            return install_standard_pypi_lib(cls.pypi_name)
        raise NotImplemented(f'No install defined for {cls.name}')
