from johnsnowlabs.auto_install.databricks.endpoints import *
from databricks.sdk.runtime import *


def log_response_if_bad_status(response):
    try:
        response.raise_for_status()
    except Exception as err:
        print(response.text)
        raise err


from johnsnowlabs.auto_install.databricks.endpoints import *


def create_endpoint(
    endpoint_name,
    model_name,
    model_version,
    secret_scope_name="JSL_SCOPE",
    secret_name="JSL_SECRET_NAME",
    workload_size="Small",
    block_until_deployed=True,
    workload_type="CPU",
    db_token=None,
    db_host=None,
):
    """Create serving endpoint and wait for it to be ready
    maps name of your secret to an env variable with the same name in the container
    """

    print(f"Creating new serving endpoint: {endpoint_name}")
    endpoint_url = f"{db_host}/api/2.0/serving-endpoints"
    served_models = [
        {
            "name": "current",
            "model_name": model_name,
            "model_version": model_version,
            "workload_size": workload_size,
            "workload_type": workload_type,
            "scale_to_zero_enabled": "false"
            if "gpu" in workload_type.lower()
            else "true",
            "env_vars": [
                {
                    "env_var_name": "JOHNSNOWLABS_LICENSE_JSON",
                    "secret_scope": secret_scope_name,
                    "secret_key": secret_name,
                },
                {
                    "env_var_name": "spark.databricks.api.url",
                    "secret_scope": secret_scope_name,
                    "secret_key": "DB_API_URL",
                },
                {
                    "env_var_name": "DB_ENDPOINT_ENV",
                    "secret_scope": secret_scope_name,
                    "secret_key": "DB_ENDPOINT_ENV",
                },
            ],
        }
    ]

    request_data = {"name": endpoint_name, "config": {"served_models": served_models}}
    response = requests.post(
        endpoint_url,
        data=json.dumps(request_data).encode("utf-8"),
        headers=get_headers(db_token),
    )
    response_json = response.json()
    if (
        "error_code" in response_json
        and response_json["error_code"] == "RESOURCE_DOES_NOT_EXIST"
    ):
        print("Model not imported from marketplace")
        return "RESOURCE_DOES_NOT_EXIST"
    elif (
        "error_code" in response_json
        and response_json["error_code"] == "RESOURCE_ALREADY_EXISTS"
    ):
        return "RESOURCE_ALREADY_EXISTS"

    log_response_if_bad_status(response)
    if block_until_deployed:
        wait_for_endpoint(endpoint_name, db_host, db_token)

    try:
        displayHTML(
            f"""Created the <a href="/#mlflow/endpoints/{endpoint_name}" target="_blank">{endpoint_name}</a> serving endpoint"""
        )
    except:
        print(
            f"Created serving endpoint {endpoint_name} at {db_host}/#mlflow/endpoints/{endpoint_name}"
        )
    return True


import os

from johnsnowlabs.auto_install.databricks.endpoints import (
    setup_secrets,
)


def make_model_select_drop_down(models_df):
    def extract_number(s):
        import re

        # Use regular expression to extract the numeric part
        match = re.search(r"\d+", s)
        return int(match.group()) if match else 0

    models = sorted(models_df.DropDownId.values.tolist(), key=extract_number)
    first_model = models[0]
    dbutils.widgets.dropdown("The model", first_model, models)


def get_selected_widget_model_metadata(models_df):
    selected_model = dbutils.widgets.get("The model")
    model_data = models_df[models_df.DropDownId == selected_model]
    return model_data


def get_model_metadta(models_df, selected_model):
    model_data = models_df[models_df.DropDownId == selected_model]
    return model_data


def query_endpoint(data, endpoint_name, db_host, db_token, base_name=None):
    url = f"{db_host}/serving-endpoints/{endpoint_name}/invocations"
    headers = {
        "Authorization": f"Bearer {db_token}",
        "Content-Type": "application/json",
    }
    response = requests.request(method="POST", headers=headers, url=url, data=data)
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status {response.status_code}, {response.text}"
        )
    import pandas as pd

    return pd.DataFrame(json.loads(response.json()["predictions"]))


def render_ui():
    from johnsnowlabs.auto_install.databricks.marketplace_offering import models_df

    dbutils.widgets.removeAll()
    dbutils.widgets.text("JSL-License", "")
    dbutils.widgets.text("Databricks access token", "")
    dbutils.widgets.text("Databricks host", "")
    make_model_select_drop_down(models_df)
    dbutils.widgets.dropdown("hardware_target", "CPU", ["CPU", "GPU"])


def get_db_token():
    return dbutils.widgets.get("Databricks access token")


def get_db_host():
    return dbutils.widgets.get("Databricks host")


def get_hardware_target():
    return dbutils.widgets.get("hardware_target")


def get_jsl_license():
    return dbutils.widgets.get("JSL-License")


def deploy(deployed_endpoint_name=None, jsl_model_id=None):
    from johnsnowlabs.auto_install.databricks.marketplace_offering import models_df

    db_token = get_db_token()
    db_host = get_db_host()
    if db_host.endswith("/"):
        db_host = db_host[:-1]
    os.environ["DATABRICKS_HOST"] = db_host
    os.environ["DATABRICKS_TOKEN"] = db_token
    hardware_target = get_hardware_target()
    jsl_license = get_jsl_license()

    jsl_license = json.dumps({"SPARK_NLP_LICENSE": jsl_license})
    if not jsl_model_id:
        model_data = get_selected_widget_model_metadata(models_df)
    else:
        model_data = get_model_metadta(models_df, jsl_model_id)

    model_path = (
        model_data.CpuModelPath.values[0]
        if hardware_target == "CPU"
        else model_data.GpuModelPath.values[0]
    )
    endpoint_name = (
        (model_path + "_endpoint")[:50].replace(".", "") + "_" + hardware_target.lower()
        if not deployed_endpoint_name
        else deployed_endpoint_name
    )

    if len(endpoint_name) > 60:
        print("Endpoint name is too long, truncating to 60 characters")
        endpoint_name = endpoint_name[:60]

    setup_secrets(
        secret_name="JSL_SECRET_NAME",
        secret_value=jsl_license,
        scope_name="JSL_SCOPE",
        host=db_host,
        db_token=db_token,
    )

    print("creating model", model_path)
    print("creating endpoint", endpoint_name)

    endpoint_success = create_endpoint(
        endpoint_name,
        model_path,
        "2",
        db_token=db_token,
        db_host=db_host,
        workload_type=hardware_target,
    )

    if endpoint_success == "RESOURCE_DOES_NOT_EXIST":
        listing_id = model_data.ListingId.values[0]
        try:
            displayHTML(
                f"""Could not import the model. <a href="marketplace/consumer/listings/{listing_id}" target="_blank">Please click this link and click on "get instant access" in the top right</a> """
            )
        except:
            print(
                f"""Could not import the model. Please visit  {db_host}/marketplace/consumer/listings/{listing_id} and click on "get instant access" in the top righ"""
            )
        return False
    elif endpoint_success == "RESOURCE_ALREADY_EXISTS":
        print(
            f"Endpoint with name {endpoint_name} already exists. Provide a different name or deploy a different model. "
        )
        return False
    return endpoint_name
