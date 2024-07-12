lic = """ENDPOINT LICENSE"""
model = """MODEL TO TEST"""


# def new_req():
#     """
#     :return: A list of default pip requirements for MLflow Models produced by this flavor.
#              Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
#              that, at minimum, contains these requirements.
#     """
#     import os
#     from johnsnowlabs import settings
#     from mlflow.utils.requirements_utils import _get_pinned_requirement
#
#     nlp.start()
#     _JOHNSNOWLABS_ENV_JSON_LICENSE_KEY = "JOHNSNOWLABS_LICENSE_JSON"
#     _JOHNSNOWLABS_ENV_HEALTHCARE_SECRET = "HEALTHCARE_SECRET"
#     _JOHNSNOWLABS_ENV_VISUAL_SECRET = "VISUAL_SECRET"
#     if (
#         _JOHNSNOWLABS_ENV_HEALTHCARE_SECRET not in os.environ
#         and _JOHNSNOWLABS_ENV_VISUAL_SECRET not in os.environ
#     ):
#         raise Exception(
#             f"You need to set the {_JOHNSNOWLABS_ENV_HEALTHCARE_SECRET} or {_JOHNSNOWLABS_ENV_VISUAL_SECRET} environment variable set."
#             f" Please contact John Snow Labs to get one"
#         )
#
#     _SPARK_NLP_JSL_WHEEL_URI = (
#         "https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl/spark_nlp_jsl-"
#         + f"{settings.raw_version_medical}-py3-none-any.whl"
#     )
#
#     _SPARK_NLP_VISUAL_WHEEL_URI = (
#         "https://pypi.johnsnowlabs.com/{secret}/spark-ocr/"
#         f"spark_ocr-{settings.raw_version_ocr}-py3-none-any.whl"
#     )
#
#     deps = [
#         f"johnsnowlabs_for_databricks=={settings.raw_version_jsl_lib}",  # TODO UNDO THIS!!
#         _get_pinned_requirement("pyspark"),
#         # TODO remove pandas constraint when NLU supports it
#         # https://github.com/JohnSnowLabs/nlu/issues/176
#         "pandas<=1.5.3",
#         "nlu_by_ckl==5.0.2rc1",
#     ]
#
#     if _JOHNSNOWLABS_ENV_HEALTHCARE_SECRET in os.environ:
#         _SPARK_NLP_JSL_WHEEL_URI = _SPARK_NLP_JSL_WHEEL_URI.format(
#             secret=os.environ[_JOHNSNOWLABS_ENV_HEALTHCARE_SECRET]
#         )
#         deps.append(_SPARK_NLP_JSL_WHEEL_URI)
#
#     if _JOHNSNOWLABS_ENV_VISUAL_SECRET in os.environ:
#         _SPARK_NLP_VISUAL_WHEEL_URI = _SPARK_NLP_VISUAL_WHEEL_URI.format(
#             secret=os.environ[_JOHNSNOWLABS_ENV_VISUAL_SECRET]
#         )
#         deps.append(_SPARK_NLP_VISUAL_WHEEL_URI)
#     print("RETRNING DPES!!!!!!!!!!")
#     print(deps)
#     return deps


def print_query_df(query_df):
    print(query_df)
    for c in query_df.columns:
        print(query_df[c])


def find_writable_directory():
    import os

    # TODO this does not work
    # List of directories to check
    candidate_dirs = [os.getcwd()]

    for dir_path in candidate_dirs:
        if os.access(dir_path, os.W_OK):
            print(f"Found writable directory: {dir_path}")
            return dir_path
    print("Could not find a writable directory")
    return None


# mlflow.set_experiment(find_writable_directory())

import json


def write_string_to_json(input_string, filename="output.json"):
    with open(filename, "w") as json_file:
        json.dump({"data": input_string}, json_file)


def read_json_from_file(filename="output.json"):
    with open(filename, "r") as json_file:
        data = json.load(json_file)

    return data


def run_test():
    import mlflow
    import os
    from johnsnowlabs.auto_install.databricks.endpoints import (
        query_and_deploy_if_missing,
        delete_endpoint,
        nlu_name_to_endpoint,
    )

    # mlflow.johnsnowlabs.get_default_pip_requirements = new_req

    # write_string_to_json(lic, "lic.json")
    os.environ["HEALTHCARE_SECRET"] = json.loads(lic)["SECRET"]

    # mlflow.set_experiment(find_writable_directory())
    mlflow.set_experiment("/Users/christian@johnsnowlabs.com/my-experiment123")
    os.environ["JOHNSNOWLABS_LICENSE_JSON_FOR_CONTAINER"] = lic
    os.environ["JOHNSNOWLABS_LICENSE_JSON"] = lic

    print("USING LIC : ", lic)
    from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home

    get_install_suite_from_jsl_home(only_jars=True)
    # get_install_suite_from_jsl_home(only_jars=True, hc_secret=json.loads(lic)["SECRET"])
    # 1) one query to construct endpoint and run with default output level
    print_query_df(query_and_deploy_if_missing(model, "Hello World", True, True))

    # # 2) One query for every output level
    # for o in ["token", "sentence", "document"]:
    #     print_query_df(
    #         query_and_deploy_if_missing(model, "Hello World", output_level=o)
    #     )

    # 3) cleanup
    print(f"Deleting: {nlu_name_to_endpoint(model)}")
    delete_endpoint(
        nlu_name_to_endpoint(model),
        host=os.environ["DATABRICKS_HOST"],
        token=os.environ["DATABRICKS_TOKEN"],
    )


def run_test_v2():
    import mlflow
    import os
    from johnsnowlabs.auto_install.databricks.endpoints import (
        delete_endpoint,
        nlu_name_to_endpoint,
    )
    from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
    from johnsnowlabs.utils.enums import JvmHardwareTarget
    from johnsnowlabs import nlp

    os.environ["HEALTHCARE_SECRET"] = json.loads(lic)["SECRET"]
    mlflow.set_experiment("/Users/christian@johnsnowlabs.com/my-experiment123")
    os.environ["JOHNSNOWLABS_LICENSE_JSON_FOR_CONTAINER"] = lic
    os.environ["JOHNSNOWLABS_LICENSE_JSON"] = lic

    # print("USING LIC : ", lic)

    nlp.deploy_endpoint(model, True, True)
    df = nlp.query_endpoint(model, "Hello World")

    # get_install_suite_from_jsl_home(only_jars=True, hc_secret=json.loads(lic)["SECRET"])
    # 1) one query to construct endpoint and run with default output level
    print_query_df(df)

    # 2) cleanup
    print(f"Deleting: {nlu_name_to_endpoint(model)}")
    delete_endpoint(
        nlu_name_to_endpoint(model),
        host=os.environ["DATABRICKS_HOST"],
        token=os.environ["DATABRICKS_TOKEN"],
    )


if __name__ == "__main__":
    dbutils.library.installPyPI("mlflow_by_johnsnowlabs")
    dbutils.library.installPyPI("johnsnowlabs_for_databricks", version="5.1.8rc4")
    run_test_v2()
    # run_test()
