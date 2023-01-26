from johnsnowlabs.abstract_base.lib_resolver import try_import_lib

if try_import_lib("sparknlp_display", True):
    pass
else:
    pass
