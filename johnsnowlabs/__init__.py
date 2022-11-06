
from .abstract_base.lib_resolver import try_import_lib

# get helpers into global space
from johnsnowlabs import nlp, settings, display, lab


# These we may only import, if the corresponding package is installed
# Otherwise we will run modules __init__ to early and will not attach new classes/methods to it
if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
    from johnsnowlabs import medical, finance, legal
    from sparknlp_jsl.alab import AnnotationLab
    lab = AnnotationLab()

if try_import_lib('sparkocr') and try_import_lib('sparknlp'):
    from johnsnowlabs import visual


def refresh_imports():
    import inspect
    inspect.__globals__


def new_version_online():
    from .utils.pip_utils import get_latest_lib_version_on_pypi
    # we are outdated, if current version does not match the latest on PypPi
    from .auto_install.softwares import Software
    return settings.raw_version_jsl_lib != get_latest_lib_version_on_pypi(Software.jsl_lib.pypi_name)
