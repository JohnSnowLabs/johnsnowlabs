import os
import shutil
import sys
from pathlib import Path
from typing import Optional, List

from colorama import Fore

from johnsnowlabs import settings
from johnsnowlabs.auto_install.offline_install import get_py4j_dependency_urls
from johnsnowlabs.py_models import jsl_secrets
from johnsnowlabs.py_models.install_info import (
    JvmInstallInfo,
    PyInstallInfo,
    RootInfo,
    InstallSuite,
    LocalPy4JLib,
    InstallFolder,
)
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.py_models.url_dependency import UrlDependency
from johnsnowlabs.utils.enums import (
    JvmHardwareTarget,
    PyInstallTypes,
    ProductName,
    ProductLogo,
)


def jsl_home_exist():
    return os.path.exists(settings.root_info_file)


def is_jsl_home_outdated():
    if jsl_home_exist:
        return (
            not RootInfo.get_from_jsl_home().version.as_str()
            == settings.raw_version_jsl_lib
        )
    else:
        raise Exception(f"JSL-Home does not exist! Cannot check if outdated")


def download_deps_and_create_info(
    deps: List[UrlDependency],
    lib_dir,
    info_file_path,
    overwrite=False,
):
    """Download a list of deps to given lib_dir folder and creates info_file at info_file_path."""
    info, old_info = {}, None
    if os.path.exists(info_file_path):
        #  keep old infos, we assume they are up-to-date and compatible
        if os.path.join("java_installs","info.json") in info_file_path:
            old_info = InstallFolder.java_folder_from_home()
        elif os.path.join("py_installs","info.json") in info_file_path:
            old_info = InstallFolder.py_folder_from_home()

    for p in deps:
        # print_prefix = Software.for_name(p.product_name).logo
        print_prefix = ProductLogo.from_name(p.product_name.name).value
        if p.dependency_type in JvmHardwareTarget:
            print_prefix = f"{ProductLogo.java.value}+{print_prefix} Java Library"
            constructor = JvmInstallInfo
        elif p.dependency_type in PyInstallTypes:
            print_prefix = f"{ProductLogo.python.value}+{print_prefix} Python Library"
            constructor = PyInstallInfo
        else:
            raise ValueError(f"Unknown Install type {p.dependency_type}")
        if not os.path.exists(f"{lib_dir}/{p.file_name}") or overwrite:
            try:
                p.download_url(lib_dir, name_print_prefix=print_prefix)
            except ValueError as _:
                # sys.tracebacklimit = 0
                err_msg = f"""🚨 Cannot install {ProductLogo.from_name(p.product_name.name).value}{p.product_name.value} because provided license file secret is outdated or it is invalid.
How to Fix this: 
Option1: Run {Fore.LIGHTGREEN_EX}nlp.install(force_browser=True){Fore.RESET} to get a Browser Window pop-up where you can refresh your license data
Option2: Run {Fore.LIGHTGREEN_EX}nlp.install(json_license_path="path/to/fresh_credentials.json"){Fore.RESET} after downloading a fresh license from https://my.johnsnowlabs.com/subscriptions   
Option3: Run {Fore.LIGHTGREEN_EX}nlp.install(refresh_install=True,force_browser=True){Fore.RESET} to refresh everything 
Option4: Set {Fore.LIGHTGREEN_EX}nlp.settings.enforce_versions=False{Fore.RESET} and run{Fore.LIGHTGREEN_EX} nlp.install(refresh_install=True,force_browser=True){Fore.RESET} to disable this protection mechanism and try to install anyways. Not Recommended, can yield unforeseen consequences 
"""

                print(err_msg)
                raise Exception(err_msg)

        info[p.file_name] = constructor(
            file_name=p.file_name,
            product=p.product_name,
            compatible_spark_version=p.spark_version.value.as_str(),
            install_type=p.dependency_type.value,
            product_version=p.dependency_version.as_str(),
        )
        info[p.file_name].compatible_spark_version = p.spark_version.value.as_str()
        info[p.file_name].product_version = p.dependency_version.as_str()

    if info:
        info = InstallFolder(**{"infos": info})
        if old_info:
            info.infos.update(old_info.infos)
        with open(info_file_path, "w") as f:
            for k, v in info.infos.items():
                v.product_version = str(v.product_version)
                v.compatible_spark_version = str(v.compatible_spark_version)

            f.write(info.model_dump_json())

def setup_jsl_home(
    secrets: Optional[JslSecrets] = None,
    jvm_install_type: JvmHardwareTarget = JvmHardwareTarget.cpu,
    py_install_type: PyInstallTypes = PyInstallTypes.wheel,
    only_jars: bool = False,
    spark_version=None,
    overwrite=False,
    log=True,
    refresh_install=False,
    visual=False,
    nlp=True,
    spark_nlp=True,
) -> None:
    """Folder structure :
    Creates Folder for JSL home and downloads all Py4J wheels/Jars
    for which we need to take PySpark Compatibility into account as well as JVM Hardware target
    ~.johnsnowlabs/
       ├─ licenses/
       │  ├─ info.json
       │  ├─ license1.json
       │  ├─ license2.json
       ├─ java_installs/
       │  ├─ info.json
       │  ├─ app1.jar
       │  ├─ app2.jar
       ├─ py_installs/
       │  ├─ info.json
       │  ├─ app1.tar.gz
       │  ├─ app2.tar.gz
       ├─ info.json
    """

    # Create all Paths
    Path(settings.license_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.java_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.py_dir).mkdir(parents=True, exist_ok=True)
    force_update = False
    suite = None

    if jsl_home_exist():
        if secrets:
            # Don't log because we will ignore the license from localhost, since one is provided
            jsl_secrets.already_logged = True
        suite = get_install_suite_from_jsl_home(
            create_jsl_home_if_missing=False,
            recursive_call=True,
            log=False,
            browser_login=False,
            jvm_hardware_target=jvm_install_type,
        )
        if secrets:
            # We overwrite secrets if user provided any
            suite.secrets = secrets

    if jsl_home_exist() and is_jsl_home_outdated() and log:
        print(f"🤓 Looks like {settings.root_dir} is outdated, updating it")
    if not jsl_home_exist() or is_jsl_home_outdated() or refresh_install:
        print(
            f"👷 Setting up  John Snow Labs home in {settings.root_dir}, this might take a few minutes."
        )
        # Delete everything except license data and re-create folder
        shutil.rmtree(settings.java_dir)
        shutil.rmtree(settings.py_dir)
        Path(settings.java_dir).mkdir(parents=True, exist_ok=True)
        Path(settings.py_dir).mkdir(parents=True, exist_ok=True)
        force_update = True

    # Get Urls for P4J based libs
    if force_update or suite and suite.get_missing_products(nlp, visual, spark_nlp):
        java_deps, py_deps = get_py4j_dependency_urls(
            secrets=secrets,
            spark_version=spark_version,
            visual=visual,
            nlp=nlp,
            spark_nlp=spark_nlp,
            jvm_install_type=jvm_install_type,
            py_install_type=py_install_type,
        )

        # store deps to jsl home with info.json files
        if not only_jars:
            download_deps_and_create_info(
                py_deps, settings.py_dir, settings.py_info_file, overwrite
            )
        download_deps_and_create_info(
            java_deps, settings.java_dir, settings.java_info_file, overwrite
        )

        root_info = RootInfo(version=settings.raw_version_jsl_lib, run_from=sys.executable)
        root_info.version = root_info.version.as_str()
        with open(settings.root_info_file, "w") as f:
            f.write(root_info.model_dump_json())
        print(f"🙆 JSL Home setup in {settings.root_dir}")

        return
    if log:
        print(f"👌 JSL-Home is up to date! ")


def get_install_suite_from_jsl_home(
    create_jsl_home_if_missing: bool = True,
    jvm_hardware_target: JvmHardwareTarget = JvmHardwareTarget.cpu,
    nlp: bool = True,
    visual: bool = False,
    spark_nlp: bool = True,
    only_jars: bool = False,
    recursive_call=False,
    # Secret Flow Params
    browser_login: bool = True,
    force_browser: bool = False,
    access_token: Optional[str] = None,
    local_license_number: int = 0,
    remote_license_number: int = 0,
    secrets_file: Optional[str] = None,
    hc_license: Optional[str] = None,
    hc_secret: Optional[str] = None,
    ocr_secret: Optional[str] = None,
    ocr_license: Optional[str] = None,
    aws_access_key: Optional[str] = None,
    aws_key_id: Optional[str] = None,
    fin_license: Optional[str] = None,
    leg_license: Optional[str] = None,
    store_in_jsl_home: bool = True,
    log: bool = True,
) -> InstallSuite:
    """Read all info files from JSL home if exists. If not exists, sets up JSL home"""
    if not jsl_home_exist() and not create_jsl_home_if_missing:
        return InstallSuite.empty()
    license_data: JslSecrets = JslSecrets.build_or_try_find_secrets(
        browser_login=browser_login,
        force_browser=force_browser,
        access_token=access_token,
        local_license_number=local_license_number,
        remote_license_number=remote_license_number,
        secrets_file=secrets_file,
        hc_license=hc_license,
        hc_secret=hc_secret,
        ocr_secret=ocr_secret,
        ocr_license=ocr_license,
        aws_access_key=aws_access_key,
        aws_key_id=aws_key_id,
        return_empty_secrets_if_none_found=True,
        fin_license=fin_license,
        leg_license=leg_license,
        store_in_jsl_home=store_in_jsl_home,
    )

    if create_jsl_home_if_missing:
        if not jsl_home_exist():
            # Nothing setup yet, download at least spark nlp jars
            print(f"🤓 Looks like {settings.root_dir} is missing, creating it")
            setup_jsl_home(only_jars=only_jars, log=False)

        if jsl_home_exist() and is_jsl_home_outdated():
            # Nothing setup yet, download at least spark nlp jars
            setup_jsl_home(only_jars=only_jars, log=False)

    java_folder, py_folder = None, None

    if os.path.exists(settings.java_info_file):
        java_folder = InstallFolder.java_folder_from_home()
    if os.path.exists(settings.py_info_file):
        py_folder = InstallFolder.py_folder_from_home()

    info = RootInfo.get_from_jsl_home()
    # Read all dependencies from local ~/.johnsnowlabs folder
    suite = InstallSuite(
        nlp=LocalPy4JLib(
            java_lib=java_folder.get_product_entry(ProductName.nlp, jvm_hardware_target)
            if java_folder
            else None,
            py_lib=py_folder.get_product_entry(ProductName.nlp) if py_folder else None,
        ),
        hc=LocalPy4JLib(
            java_lib=java_folder.get_product_entry(ProductName.hc)
            if java_folder
            else None,
            py_lib=py_folder.get_product_entry(ProductName.hc) if py_folder else None,
        ),
        ocr=LocalPy4JLib(
            java_lib=java_folder.get_product_entry(ProductName.ocr)
            if java_folder
            else None,
            py_lib=py_folder.get_product_entry(ProductName.ocr) if py_folder else None,
        ),
        secrets=license_data,
        info=info,
    )

    missing = suite.get_missing_products(nlp, visual, spark_nlp)
    if missing and recursive_call and log:
        print(f"🚨 Looks like some of the missing jars could not be fetched...")
        suite.log_missing_jars(visual, nlp, spark_nlp)

    if missing and not recursive_call:
        print(f"🤓 Looks like you are missing some jars, trying fetching them ...")
        setup_jsl_home(
            license_data,
            jvm_install_type=jvm_hardware_target,
            only_jars=only_jars,
            log=False,
            nlp=nlp,
            visual=visual,
            spark_nlp=spark_nlp,
        )
        # After re-setting up jsl_home, call this method again
        return get_install_suite_from_jsl_home(
            jvm_hardware_target=jvm_hardware_target,
            nlp=nlp,
            visual=visual,
            spark_nlp=spark_nlp,
            only_jars=only_jars,
            recursive_call=True,
            browser_login=browser_login,
            access_token=access_token,
            local_license_number=local_license_number,
            remote_license_number=remote_license_number,
            secrets_file=secrets_file,
            hc_license=hc_license,
            hc_secret=hc_secret,
            ocr_secret=ocr_secret,
            ocr_license=ocr_license,
            aws_access_key=aws_access_key,
            aws_key_id=aws_key_id,
            fin_license=fin_license,
            leg_license=leg_license,
        )
    return suite
