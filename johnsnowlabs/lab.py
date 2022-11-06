from johnsnowlabs.abstract_base.lib_resolver import try_import_lib
try:
    if try_import_lib('sparknlp_jsl') and try_import_lib('sparknlp'):
        from sparknlp_jsl.alab import AnnotationLab
except:
    pass