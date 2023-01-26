from johnsnowlabs.abstract_base.lib_resolver import try_import_lib

if try_import_lib("sparknlp"):
    pass

if try_import_lib("pyspark"):
    from pyspark import ml as ML
    import pyspark.ml.param.shared as _shared_pyspark_ml_param

    ML.param.shared = _shared_pyspark_ml_param

if try_import_lib("warnings"):
    import warnings

    warnings.filterwarnings("ignore")

if try_import_lib("nlu"):
    pass
