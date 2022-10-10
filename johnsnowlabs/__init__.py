from .auto_install.health_checks.report import check_health, list_remote_licenses, list_local_licenses
from .utils.sparksession_utils import start
from .auto_install.install_flow import install
# get helpers into global space
from johnsnowlabs import nlp, settings, viz
import johnsnowlabs as jsl

# databricks
from johnsnowlabs.auto_install.databricks.work_utils import run_in_databricks
from johnsnowlabs.nlp import *


# These we may only import, if the corresponding package is installed
# Otherwise we will run modules __init__ to early and will not attach new classes/methods to it
if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
    from johnsnowlabs import medical,finance,legal

if try_import_lib('sparkocr') and try_import_lib('sparknlp'):
    from johnsnowlabs import ocr





def refresh_imports():
    import inspect
    inspect.__globals__

def new_version_online():
    from .utils.pip_utils import get_latest_lib_version_on_pypi
    # we are outdated, if current version does not match the latest on PypPi
    from .auto_install.softwares import Software
    return settings.raw_version_jsl_lib != get_latest_lib_version_on_pypi(Software.jsl_lib.pypi_name)
