import importlib
import site
import os
import subprocess


def try_import(lib):
    try:
        importlib.reload(site)
        globals()[lib] = importlib.import_module(lib)
        importlib.import_module(lib)
    except Exception as _:
        # print(f'Failed to import {lib}')
        return False
    return True


def try_import_in_venv(lib, py_path):
    c = f'{py_path} -c "import {lib}"'
    try:
        result = subprocess.check_output(c, shell=True, stderr=subprocess.STDOUT)
        if result == b'':
            return True
            print('all good!')
        else:
            print(f'Looks like {lib} is missing \n{result}')
            return False
    except:
        print(f'Looks like {lib} is missing')
        return False


def is_running_in_databricks():
    """ Check if the currently running Python Process is running in Databricks or not
     If any Environment Variable name contains 'DATABRICKS' this will return True, otherwise False"""
    for k in os.environ.keys():
        if 'DATABRICKS' in k:
            return True
    return False


def env_required_license():
    if 'JSL_AWS_PLATFORM' in os.environ.keys() and str(os.environ['JSL_AWS_PLATFORM']) == '1':
        return False
    if 'JSL_AZURE_PLATFORM' in os.environ.keys() and str(os.environ['JSL_AZURE_PLATFORM']) == '1':
        return False
    return True


def set_py4j_logger_to_error_on_databricks():
    # Only call this when in Databricks
    import logging
    logger = spark._jvm.org.apache.log4j
    logging.getLogger("py4j.java_gateway").setLevel(logging.ERROR)
