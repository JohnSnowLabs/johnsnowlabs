from johnsnowlabs.utils.print_messages import log_outdated_lib, log_broken_lib
from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.auto_install.softwares import Software

warning_logged = False
if try_import_lib("sparkocr") and try_import_lib("sparknlp"):
    try:
        from sparkocr.base import *

        from sparkocr.transformers import *
        from sparkocr.enums import *
        import sparkocr
        from sparkocr.utils import *
        from sparkocr.schemas import *
        from sparkocr.metrics import *
        from sparkocr.pretrained import *
        from sparkocr.databricks import isRunningInDatabricks

        if isRunningInDatabricks():
            # Overwrites functions imported from sparkocr.utils
            # but this is fine, since these are not compatible on databricks
            from sparkocr.databricks import *

        if (
            not Software.spark_ocr.check_installed_correct_version()
            and not warning_logged
        ):
            log_outdated_lib(Software.spark_ocr, sparkocr.version())
            warning_logged = True
    except Exception as err:
        import traceback

        log_broken_lib("Visual NLP")
        print(f"Error Message : {err}")
        print(f"Error Trace: {traceback.format_exc()}")
