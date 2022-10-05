import shutil
from typing import Optional

from johnsnowlabs import settings
from johnsnowlabs.auto_install.databricks.databricks_utils import create_cluster, get_db_client_for_token, \
    install_jsl_suite_to_cluster
from johnsnowlabs.auto_install.jsl_home import setup_jsl_home, get_install_suite_from_jsl_home
from johnsnowlabs.auto_install.offline_install import get_printable_dependency_urls
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.utils.enums import ProductName, PyInstallTypes, JvmHardwareTarget
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.auto_install.install_software import check_and_install_dependencies
import sys


def install(
        # -- JSL-Auth Flows --
        # Browser Auth
        browser_login: bool = True,
        force_browser: bool = False,
        # JWT Token Auth
        access_token: Optional[str] = None,
        # JSON file Auth
        json_license_path: Optional[str] = None,
        # Manual License specification Auth
        med_license: Optional[str] = None,
        enterprise_nlp_secret: Optional[str] = None,
        ocr_secret: Optional[str] = None,
        ocr_license: Optional[str] = None,
        fin_license: Optional[str] = None,
        leg_license: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_key_id: Optional[str] = None,

        # -- Databricks auth flows & Install Target --
        databricks_cluster_id: Optional[str] = None,
        databricks_token: Optional[str] = None,
        databricks_host: Optional[str] = None,
        databricks_password: Optional[str] = None,
        databricks_email: Optional[str] = None,

        # -- Install Params --
        # Install Target
        python_exec_path: str = sys.executable,
        venv_creation_path: Optional[str] = None,
        offline_zip_dir: Optional[str] = None,

        # Download Params
        offline: bool = False,
        install_optional: bool = True,
        install_licensed: bool = True,
        only_download_jars: bool = False,
        product: Optional[str] = ProductName.jsl_full.value,
        include_dependencies: bool = True,
        # License usage & Caching
        license_number: int = 0,
        store_in_jsl_home: bool = True,
        # Install File Types
        jvm_install_type: str = JvmHardwareTarget.cpu.value,
        py_install_type: str = PyInstallTypes.wheel.value,
        block_till_cluster_ready:bool=True,
        only_refresh_credentials: bool = False,
        refresh_install: bool = False,
):
    if refresh_install:
        shutil.rmtree(settings.root_dir)
    # Input Validation
    py_install_type = PyInstallTypes.from_str(py_install_type)
    jvm_install_type = JvmHardwareTarget.from_str(jvm_install_type)
    product = Software.for_name(product)

    # Get Credentials from Auth Flow
    secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(browser_login=browser_login,
                                                               force_browser=force_browser,
                                                               access_token=access_token,
                                                               license_number=license_number,
                                                               secrets_file=json_license_path,
                                                               hc_license=med_license,
                                                               hc_secret=enterprise_nlp_secret,
                                                               ocr_secret=ocr_secret,
                                                               ocr_license=ocr_license,
                                                               aws_access_key=aws_access_key,
                                                               aws_key_id=aws_key_id,
                                                               return_empty_secrets_if_none_found=True,
                                                               fin_license=fin_license,
                                                               leg_license=leg_license,
                                                               store_in_jsl_home=store_in_jsl_home)
    if only_refresh_credentials:
        return

    if offline:
        # Offline Install
        get_printable_dependency_urls(secrets=secrets,
                                      jvm_install_type=jvm_install_type,
                                      py_install_type=py_install_type)
        if not offline_zip_dir:
            return

    if store_in_jsl_home and not offline:
        # Cache credentials, Wheels and Jars in ~/.johnsnowlabs
        setup_jsl_home(
            secrets=secrets,
            jvm_install_type=jvm_install_type,
            py_install_type=py_install_type,
            refresh_install=refresh_install)

    # Databricks Install
    if databricks_host and databricks_token and not offline:
        suite = get_install_suite_from_jsl_home(only_jars=True, jvm_hardware_target=jvm_install_type)
        if databricks_cluster_id:
            install_jsl_suite_to_cluster(
                db=get_db_client_for_token(databricks_host, databricks_token),
                install_suite=suite,
                cluster_id=databricks_cluster_id)

        else:
            return create_cluster(db=get_db_client_for_token(databricks_host, databricks_token),
                                  install_suite=suite,block_till_cluster_ready=block_till_cluster_ready,
                                  )

    # Local Py-Install
    elif not only_download_jars:
        check_and_install_dependencies(product=product, secrets=secrets, install_optional=install_optional,
                                       install_licensed=install_licensed,
                                       python_exec_path=python_exec_path,
                                       py_setup_dir=venv_creation_path,
                                       offline_zip_dir=offline_zip_dir,
                                       include_dependencies=include_dependencies
                                       )
