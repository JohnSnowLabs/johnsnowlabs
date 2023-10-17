from johnsnowlabs import lab, settings, viz
from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
from johnsnowlabs.auto_install.databricks.endpoints import query_and_deploy_if_missing
from johnsnowlabs.auto_install.databricks.work_utils import run_in_databricks
from johnsnowlabs.auto_install.emr.work_utils import run_in_emr

from .auto_install.health_checks.report import (
    check_health,
    list_local_licenses,
    list_remote_licenses,
)
from .auto_install.install_flow import (
    install,
    install_to_emr,
    install_to_glue,
    install_to_databricks,
)
from .utils.sparksession_utils import start

if try_import_lib("sparknlp"):
    import sparknlp
    from sparknlp import annotation
    from sparknlp.annotator import *
    from sparknlp.base import *
    from sparknlp.functions import *
    from sparknlp.pretrained import PretrainedPipeline, ResourceDownloader
    from sparknlp.training import *


if try_import_lib("pyspark"):
    import pyspark.ml.param.shared as _shared_pyspark_ml_param
    import pyspark.sql as SQL
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    from pyspark import ml as ML
    from pyspark.sql import DataFrame

    ML.param.shared = _shared_pyspark_ml_param

    from pyspark.ml import Pipeline, PipelineModel
    from pyspark.sql import SparkSession

if try_import_lib("warnings"):
    import warnings

    warnings.filterwarnings("ignore")

if try_import_lib("nlu"):
    import nlu as nlu
    from nlu import autocomplete_pipeline, load, to_nlu_pipe, to_pretty_df
