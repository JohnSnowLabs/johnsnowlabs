import ast
import importlib
import inspect
import os
import site
import subprocess
from typing import List

logged_imports = []


def inject_modules(imports: List[str], g):
    # Imports a list of modules in the global scope g
    for module_name in imports:
        try:
            if "." not in module_name:
                # plain module import
                g[module_name] = importlib.import_module(module_name)
                continue
            elif "*" in module_name:
                # Not handled but unlikely to break anytime soon
                continue
            elif " as " in module_name:
                # import with alias
                name = module_name.split(" ")[-1]
                module = module_name.split(" ")[0]
                attr = module.split(".")[-1]
                module = ".".join(module.split(".")[:-1])
            else:
                # import without alias
                attr = module_name.split(".")[-1]
                name = attr
                module = ".".join(module_name.split(".")[:-1])
            # import the module and attach to globals
            g[name] = getattr(importlib.import_module(module), attr)
        except Exception as e:  # ImportError
            if module_name not in logged_imports:
                logged_imports.append(module_name)
                print(f"Warning: Could not import module={module_name} error = {e}")


def collect_all_imports(source_code) -> List[str]:
    # collect all import statements from source code string
    tree = ast.parse(source_code)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname is None:
                    imports.append(alias.name)
                else:
                    imports.append(f"{alias.name} as {alias.asname}")
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.asname is None:
                    imports.append(f"{node.module}.{alias.name}")
                else:
                    imports.append(f"{node.module}.{alias.name} as {alias.asname}")
    return imports


def reverse_compatibility_import(script_path, g):
    """
    Fallback when import fails, this will read source code and import 1-by-1 and add to globals of the calling module
    :param script_path: tge script path, should be fetched with __file__ from calling module
    :param g: globals() from calling script into which we inject imports
    """
    inject_modules(
        collect_all_imports(ast.parse(open(script_path, encoding="utf8").read())), g
    )


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
        if result == b"":
            return True
            print("all good!")
        else:
            print(f"Looks like {lib} is missing \n{result}")
            return False
    except:
        print(f"Looks like {lib} is missing")
        return False


def is_running_in_emr():
    """We populate EMR with environment variable"""
    if "JSL_EMR" in os.environ.keys():
        return bool(os.environ["JSL_EMR"])
    return False


def is_running_in_databricks_runtime():
    """ Check if the currently running Python Process is running in Databricks runtime or not
    """
    return "DATABRICKS_RUNTIME_VERSION" in os.environ


def env_required_license():
    if (
        "JSL_AWS_PLATFORM" in os.environ.keys()
        and str(os.environ["JSL_AWS_PLATFORM"]) == "1"
    ):
        return False
    if (
        "JSL_AZURE_PLATFORM" in os.environ.keys()
        and str(os.environ["JSL_AZURE_PLATFORM"]) == "1"
    ):
        return False
    return True


def set_py4j_logger_to_error_on_databricks():
    # Only call this when in Databricks
    try:
        if "SKIP_py4j_DISABLE" in os.environ and os.environ["SKIP_py4j_DISABLE"] == "1":
            return
        import logging

        from pyspark.sql import SparkSession

        logger = SparkSession.builder.getOrCreate()._jvm.org.apache.log4j
        logging.getLogger("py4j.java_gateway").setLevel(logging.ERROR)
    except:
        pass


def get_folder_of_func(func):
    # Get the file path where the function is defined
    func_file = inspect.getfile(func)

    # Get the directory name from the file path
    func_dir = os.path.dirname(func_file)

    return func_dir
