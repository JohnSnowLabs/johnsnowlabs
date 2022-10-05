from .auto_install.health_checks.report import check_health, list_remote_licenses, list_local_licenses
from .utils.sparksession_utils import start
from .auto_install.install_flow import install
# get helpers into global space
from johnsnowlabs import medical, nlp, ocr, settings, viz, finance, legal
import johnsnowlabs as jsl


from johnsnowlabs.auto_install.databricks.databricks_utils import create_cluster, get_db_client_for_token, \
    install_jsl_suite_to_cluster, run_local_py_script_as_task
from .abstract_base.software_product import AbstractSoftwareProduct
from .py_models import jsl_secrets
from .py_models.install_info import InstallFolder
from .py_models.jsl_secrets import LicenseInfos, JslSecrets
from .utils.pip_utils import get_latest_lib_version_on_pypi

# Input validation enums for typing the functions
from johnsnowlabs.utils.enums import ProductName, PyInstallTypes, JvmHardwareTarget

from johnsnowlabs.nlp import *
# from johnsnowlabs.medical import *
# from johnsnowlabs.ocr import *
# from johnsnowlabs.finance import *
from typing import Dict, Optional, List, Tuple


def new_version_online():
    # we are outdated, if current version does not match the latest on PypPi
    return settings.raw_version_jsl_lib != get_latest_lib_version_on_pypi('jsl_tmp')

def databricks_submit(
        py_script_path: str,
        databricks_cluster_id: Optional[str] = None,
        databricks_token: Optional[str] = None,
        databricks_host: Optional[str] = None,
        databricks_password: Optional[str] = None,
        databricks_email: Optional[str] = None,
):
    db_client = get_db_client_for_token(databricks_host, databricks_token)
    return run_local_py_script_as_task(db_client, py_script_path, cluster_id=databricks_cluster_id)
