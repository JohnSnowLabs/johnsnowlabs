from .auto_install.health_checks.report import check_health, list_remote_licenses, list_local_licenses
from .utils.sparksession_utils import start
from .auto_install.install_flow import install
# get helpers into global space
from johnsnowlabs import medical, nlp, ocr, settings, viz, finance, legal
import johnsnowlabs as jsl

# databricks
from johnsnowlabs.auto_install.databricks.work_utils import run_in_databricks
from johnsnowlabs.nlp import *


def new_version_online():
    from .utils.pip_utils import get_latest_lib_version_on_pypi
    # we are outdated, if current version does not match the latest on PypPi
    from .auto_install.softwares import Software
    return settings.raw_version_jsl_lib != get_latest_lib_version_on_pypi(Software.jsl_lib.pypi_name)
