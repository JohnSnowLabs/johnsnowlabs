lic = """ENDPOINT LICENSE"""
model = """MODEL TO TEST"""


# def new_req():
#     from mlflow.utils.requirements_utils import _get_pinned_requirement
#     from johnsnowlabs import settings
#
#     _SPARK_NLP_JSL_WHEEL_URI = (
#         "https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl/spark_nlp_jsl-"
#         + f"{settings.raw_version_medical}-py3-none-any.whl"
#     )
#
#     return [
#         f"johnsnowlabs_for_databricks_by_ckl=={settings.raw_version_jsl_lib}",
#         _get_pinned_requirement("pyspark"),
#         _SPARK_NLP_JSL_WHEEL_URI.format(secret=os.environ["SECRET"]),
#         "pandas<=1.5.3",
#     ]
#
# mlflow.johnsnowlabs.get_default_pip_requirements = new_req


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


def run_test():
    import mlflow
    import os
    from johnsnowlabs.auto_install.databricks.endpoints import (
        query_and_deploy_if_missing,
        delete_endpoint,
        nlu_name_to_endpoint,
    )

    # mlflow.set_experiment(find_writable_directory())
    mlflow.set_experiment("/Users/christian@johnsnowlabs.com/my-experiment123")
    os.environ["JOHNSNOWLABS_LICENSE_JSON_FOR_CONTAINER"] = lic
    os.environ["JOHNSNOWLABS_LICENSE_JSON"] = lic
    # 1) one query to construct endpoint and run with default output level
    print(query_and_deploy_if_missing(model, "Hello World", True, True))

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


if __name__ == "__main__":
    dbutils.library.installPyPI("mlflow_by_johnsnowlabs")  # , version="2.10.0")
    dbutils.library.installPyPI("pandas", version="1.5.0")
    run_test()
