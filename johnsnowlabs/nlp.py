from johnsnowlabs.abstract_base.lib_resolver import try_import_lib

if try_import_lib('sparknlp'):
    from sparknlp.base import *
    from sparknlp.annotator import *
    import sparknlp
    from sparknlp.pretrained import ResourceDownloader
    from sparknlp.training import *
    from sparknlp.functions import *
    from sparknlp.pretrained import PretrainedPipeline

if try_import_lib('pyspark'):
    from pyspark.sql import DataFrame
    import pyspark.sql.functions as F
    import pyspark.sql.types as T
    import pyspark.sql as SQL

    from pyspark import ml as ML
    import pyspark.ml.param.shared as _shared_pyspark_ml_param

    ML.param.shared = _shared_pyspark_ml_param

    from pyspark.sql import SparkSession
    from pyspark.ml import Pipeline, PipelineModel

if try_import_lib('warnings'):
    import warnings

    warnings.filterwarnings('ignore')

if try_import_lib('nlu'):
    from nlu import load, to_nlu_pipe, autocomplete_pipeline, to_pretty_df
    import nlu as nlu
