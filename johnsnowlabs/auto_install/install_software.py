import os
import sys
from pathlib import Path
from typing import Dict, Set
import shutil
from colorama import Fore, Back, Style

from johnsnowlabs import settings
from johnsnowlabs.utils.env_utils import is_running_in_databricks

from johnsnowlabs.abstract_base.software_product import AbstractSoftwareProduct
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.utils.enums import ProductName, LatestCompatibleProductVersion
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.pip_utils import get_pip_lib_version
from johnsnowlabs.utils.venv_utils import VenvWrapper


def check_and_install_dependencies(product: AbstractSoftwareProduct,
                                   secrets: JslSecrets,
                                   python_exec_path: str = sys.executable,
                                   install_optional: bool = False,
                                   install_licensed: bool = True,
                                   py_setup_dir: str = None,
                                   offline_zip_dir: str = None,
                                   include_dependencies: bool = True,
                                   visual: bool = False,
                                   spark_nlp: bool = True,
                                   enterpise_nlp: bool = True,

                                   ):
    """
    Iterates the dependency DAG in DFS order for input product and downloads installs all dependencies
    into python_exec_path with pip module.
    Usually we just iterate starting from jsl-full-suite Product, which depends on everything

    A product may have 3 types of dependencies which are defined as outgoing edges in the DAG:
        - hard_dependency: Must have this installed for core functionality like pyspark
        - licensed_dependency: Requires a license, install if accessible like OCR/NLP-Licensed
        - optional_dependency: Can be installed for extra features, like NLU, NLP-Display, etc..

    NOTE: There is currently no product that has licensed dependencies.
    INVARIANT :
        Either the product itself is licensed and then no dependencies requiring license
        Or product is free, but it has licensed optional dependencies

    Spark NLP must be re-installed last, because other libs may depend on it but might install a
    Spark NLP version which is not the one we have defined in johnsnowlabs.settings

    TODO (UX Improvement)
        To properly log what was installed, we must first iterate the DAG and get all missing notes
        Otherwise we might install multiple nodes because of sub-dependencies in one iteration
        And then we will not be able to properly track what was installed ( Everything works fine tho)
        This causes venv/cli based installs which will install jsl_lib not to print out all JSL-product logos
            Like Spark-NLP-Display, NLU, Pyspark or Spark-NLP

    # TODO generalize HOST class Databricks/Local/Venv etc.. with host.has_lib_installed() etc..

    :param offline_zip_dir:
    :param include_dependencies:
    :param py_dir:
    :param product:
    :param python_exec_path: A Python executable into which products should be installed.
        The pip module of this executable is used to install all libs
    :param py_setup_dir: If not None, a fresh Python Venv with target products will be setup in folder
        if using this parameter, the python_exec_path parameter will be ignored
        and the python_exec_path from the newly created venv is used to setup all libs
    :param secrets: to use for installing licensed libs
    :param install_optional: install optional dependencies if True, otherwise not
    :param install_licensed: install licensed products if license permits it if True, otherwise not
    sparknlp_to_latest: for some releases we might not want to go to the latest spark release
    """
    import site
    from importlib import reload
    reload(site)
    offline_py_dir = None
    license_dir = None
    java_dir = None
    if py_setup_dir:
        # Use VenvWrapper to setup new Env
        VenvWrapper.create_venv(venv_target_dir=py_setup_dir, log=False)
        python_exec_path = VenvWrapper.glob_py_exec_from_venv(py_setup_dir)
    if offline_zip_dir and not os.path.exists(offline_zip_dir):
        offline_py_dir = f'{offline_zip_dir}/py_installs'
        java_dir = f'{offline_zip_dir}/java_installs'
        license_dir = f'{offline_zip_dir}/licenses'
        Path(offline_py_dir).mkdir(parents=True, exist_ok=True)
        Path(java_dir).mkdir(parents=True, exist_ok=True)
        Path(license_dir).mkdir(parents=True, exist_ok=True)

    # Iteration Variables
    hard_nodes: Set[AbstractSoftwareProduct] = {product}
    licensed_nodes: Set[AbstractSoftwareProduct] = set([])
    optional_nodes: Set[AbstractSoftwareProduct] = set([])
    install_results: Dict[AbstractSoftwareProduct:bool] = {}

    # Boolean Checkers
    is_spark_nlp = lambda node: node.name == ProductName.nlp.value
    is_ocr = lambda node: node.name == ProductName.ocr.value
    is_healthcare = lambda node: node.name == ProductName.hc.value
    exist_install_result = lambda node: node in install_results
    licensed_nodes_left_to_install = lambda: licensed_nodes and install_licensed
    optional_nodes_left_to_install = lambda: optional_nodes and install_optional

    while hard_nodes or licensed_nodes_left_to_install() or optional_nodes_left_to_install():
        # Core loop, check if any more vertex left to explore
        # In addition to popping whatever is not empty, we remember what we popped by returning a tuple
        v = hard_nodes.pop() if hard_nodes \
            else licensed_nodes.pop() if licensed_nodes_left_to_install() \
            else optional_nodes.pop() if optional_nodes_left_to_install() \
            else None

        if not visual and is_ocr(v):
            continue
        if not enterpise_nlp and is_healthcare(v):
            continue
        if not spark_nlp and is_spark_nlp(v):
            continue

        v: AbstractSoftwareProduct
        # Collect all children of this vertex for next iteration
        hard_nodes = hard_nodes | v.hard_dependencies
        licensed_nodes = licensed_nodes | v.licensed_dependencies
        optional_nodes = optional_nodes | v.optional_dependencies

        # Check if we should install this vertex
        if not v.pypi_name:
            # Non Python Dependencies are not handled here yet
            continue
        if not v.licensed and not install_licensed:
            continue
        if v.check_installed(python_exec_path=python_exec_path, download_folder=offline_py_dir) \
                and v.check_installed_correct_version() and not offline_py_dir:
            # It's already installed and has correct version
            continue
        elif is_spark_nlp(v) and not offline_py_dir:
            # We don't install spark nlp during iterating the DAG
            continue
        elif exist_install_result(v):
            # We could have failed in a previous iteration installing this vertex
            # Only if we don't have an entry for it, we attempt installing
            continue

        # Attempt installing the node and store the result
        install_results[v] = v.install(
            secrets=secrets, py_path=python_exec_path, download_folder=offline_py_dir,
            include_dependencies=include_dependencies, re_install=v.check_installed_correct_version()
        )
    if offline_zip_dir:
        print('👷 Zipping installation files for offline install')
        finalize_zip_folder(offline_zip_dir, java_dir, offline_py_dir, license_dir)
        print("Done zipping")
        return
    else:
        # These checks are only for current env, not defined for offline
        if not get_pip_lib_version('spark-nlp', py_exec=python_exec_path).equals(
                LatestCompatibleProductVersion.spark_nlp.value):
            # Re-install NLP incase some other library up/downgraded it while we installed it
            install_results[Software.spark_nlp] = \
                Software.spark_nlp.install(re_install=True,
                                           version=LatestCompatibleProductVersion.spark_nlp.value,
                                           py_path=python_exec_path, download_folder=offline_py_dir,
                                           include_dependencies=include_dependencies, )
        if not get_pip_lib_version('pyspark', py_exec=python_exec_path).equals(
                LatestCompatibleProductVersion.pyspark.value):
            # Re-install NLP incase some other library up/downgraded it while we installed it
            install_results[Software.spark_nlp] = \
                Software.pyspark.install(re_install=True,
                                         version=LatestCompatibleProductVersion.pyspark.value,
                                         py_path=python_exec_path, download_folder=offline_py_dir,
                                         include_dependencies=include_dependencies,
                                         )

    # Log The results of installation
    if Software.jsl_full in install_results:
        del install_results[Software.jsl_full]
    if len(install_results) > 0:
        print(f'Installed {len(install_results)} products:')
        for installed_software, result in install_results.items():
            if installed_software.check_installed(python_exec_path=python_exec_path, download_folder=offline_py_dir):
                print(
                    f'{installed_software.logo} {installed_software.name}=={installed_software.get_installed_version(prefer_pip=True, fallback_import=False)}'
                    f' installed! ✅ {installed_software.slogan} ')
            else:
                print(f'{installed_software.logo} {installed_software.name} not installed! ❌')

        # Trigger Imports after install. so module is reloaded and no re-start is required
        from johnsnowlabs import medical, finance, legal, visual
        from importlib import reload
        for mod in [medical, finance, legal, visual]:
            reload(mod)
        # print(f'🔁{Fore.LIGHTRED_EX} If you are on Google Colab, please restart your Notebook for changes to take effect {Fore.RESET}🔁')

    else:
        print(f'👌 Everything is already installed, no changes made')


def finalize_zip_folder(offline_zip_dir, new_java_dir, py_dir, new_license_dir):
    # Copy files from local jsl home and create zip file
    copy_jars_from_jsl_home_to_offline_zip_dir(new_java_dir)
    copy_py_installs_from_jsl_home_to_offline_zip_dir(py_dir)
    copy_licenses_from_jsl_home_to_zip_dir(new_license_dir)
    zip_folder(offline_zip_dir)


def copy_py_installs_from_jsl_home_to_offline_zip_dir(new_py_dir):
    for f in os.listdir(settings.py_dir):
        if '.gz' in f or '.whl' in f:
            print(f'Adding {f} to zip')
            shutil.copy(f'{settings.py_dir}/{f}', new_py_dir)


def copy_jars_from_jsl_home_to_offline_zip_dir(new_java_dir):
    for f in os.listdir(settings.java_dir):
        if '.jar' in f:
            print(f'Adding {f} to zip')
            shutil.copy(f'{settings.java_dir}/{f}', new_java_dir)


def copy_licenses_from_jsl_home_to_zip_dir(new_license_dir):
    for f in os.listdir(settings.license_dir):
        if 'info' not in f:
            shutil.copy(f'{settings.license_dir}/{f}', new_license_dir)


def zip_folder(offline_zip_dir):
    shutil.make_archive('john_snow_labs_suite', 'zip', offline_zip_dir)
    shutil.move('john_snow_labs_suite.zip', offline_zip_dir)
