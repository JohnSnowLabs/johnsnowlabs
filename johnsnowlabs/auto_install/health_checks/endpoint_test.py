lic = """
ENDPOINT LICENSE
"""
import mlflow

from johnsnowlabs.auto_install.databricks.endpoints import *


def new_req():
    from mlflow.utils.requirements_utils import _get_pinned_requirement
    from johnsnowlabs import settings

    _SPARK_NLP_JSL_WHEEL_URI = (
        "https://pypi.johnsnowlabs.com/{secret}/spark-nlp-jsl/spark_nlp_jsl-"
        + f"{settings.raw_version_medical}-py3-none-any.whl"
    )

    return [
        f"johnsnowlabs_for_databricks_by_ckl=={settings.raw_version_jsl_lib}",
        _get_pinned_requirement("pyspark"),
        _SPARK_NLP_JSL_WHEEL_URI.format(secret=os.environ["SECRET"]),
        "pandas<=1.5.3",
    ]


mlflow.johnsnowlabs.get_default_pip_requirements = new_req


def run_test():
    mlflow.set_experiment("/Users/christian@johnsnowlabs.com/my-experiment")
    os.environ["JOHNSNOWLABS_LICENSE_JSON_FOR_CONTAINER"] = lic
    os.environ["JOHNSNOWLABS_LICENSE_JSON"] = lic
    res = query_and_deploy_if_missing("tokenize", "Hello World", True, True)
    print(res)


if __name__ == "__main__":
    run_test()
