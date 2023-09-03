# DB-API Helper funcs

import base64
import json
import os
import time
from pprint import pprint
from typing import Union, List

import requests

from johnsnowlabs import nlp

ENDPOINT_MAP = {
    # secret endpoints
    "list_scopes": "api/2.0/secrets/scopes/list",
    "create_scope": "api/2.0/secrets/scopes/create",
    "create_scret": "api/2.0/secrets/put",
    "list_secrets": "api/2.0/secrets/list",
    # serve endpoints
    "update_endpoint": "api/2.0/serving-endpoints/{endpoint_name}/config",
    "endpoint_exists": "api/2.0/serving-endpoints/{endpoint_name}",
    "wait_for_endpoint": "api/2.0/serving-endpoints/{endpoint_name}",
    "create_endpoint": "api/2.0/serving-endpoints",
    "update_endpoint_conf": "api/2.0/serving-endpoints/{endpoint_name}/config",
    "delete_endpoint": "api/2.0/serving-endpoints/{endpoint_name}",
    "list_endpoints": "api/2.0/serving-endpoints",
    "get_endpoint": "api/2.0/serving-endpoints/{endpoint_name}",
}


def get_endpoint(name, host, token):
    """Check if an endpoint with the serving_endpoint_name exists"""
    response = requests.get(
        get_endpoint_url(
            ENDPOINT_MAP["list_endpoints"].format(endpoint_name=name), host
        ),
        headers=get_headers(token),
    )
    return response.json()


def delete_endpoint(endpoint_name, host, token):
    """Check if an endpoint with the serving_endpoint_name exists"""
    response = requests.delete(
        get_endpoint_url(
            ENDPOINT_MAP["delete_endpoint"].format(endpoint_name=endpoint_name), host
        ),
        headers=get_headers(token),
    )
    return response.status_code == 200


def list_endpoints(host, token):
    """Check if an endpoint with the serving_endpoint_name exists"""
    response = requests.get(
        get_endpoint_url(ENDPOINT_MAP["list_endpoints"], host),
        headers=get_headers(token),
    )
    return response.json()


def delete_all_endpoints(host, token):
    for end in list_endpoints(host, token)["endpoints"]:
        print("deleting endpoint ", end["name"])
        delete_endpoint(end["name"], host, token)


def dump(data):
    return json.dumps(data).encode("utf-8")


def get_headers(db_token):
    return {"Authorization": f"Bearer {db_token}"}


def get_endpoint_url(req, db_host):
    return f"{db_host}/{req}"


# def update_endpoint(endpoint_name):
#     """Update serving endpoint and wait for it to be ready"""
#     print(f"Updating existing serving endpoint: {endpoint_name}")
#     pay = {"served_models": served_models, "traffic_config": traffic_config}
#     response = requests.post(
#         get_endpoint_url(
#             ENDPOINT_MAP["update_endpoint"].format(endpoint_name=endpoint_name)
#         ),
#         data=dump(pay),
#         headers=get_headers(),
#     )
#
#     response.raise_for_status()
#     wait_for_endpoint()
#     displayHTML(
#         f"""Updated the <a href="/#mlflow/endpoints/{ENDPOINT_NAME}" target="_blank">{ENDPOINT_NAME}</a> serving endpoint"""
#     )


def endpoint_exists(endpoint_name, host, token):
    """Check if an endpoint with the serving_endpoint_name exists"""
    response = requests.get(
        get_endpoint_url(
            ENDPOINT_MAP["endpoint_exists"].format(endpoint_name=endpoint_name), host
        ),
        headers=get_headers(token),
    )
    return response.status_code == 200


def wait_for_endpoint(endpoint_name, host, token):
    """Wait until deployment is ready, then return endpoint config"""
    endpoint_url = get_endpoint_url(
        ENDPOINT_MAP["wait_for_endpoint"].format(endpoint_name=endpoint_name), host
    )
    response = requests.request(
        method="GET", headers=get_headers(token), url=endpoint_url
    )

    print("Deployment starting, this may take 10 to 20 minutes...")
    while (
        response.json()["state"]["ready"] == "NOT_READY"
        or response.json()["state"]["config_update"] == "IN_PROGRESS"
    ):
        if response.json()["state"]["config_update"] == "UPDATE_FAILED":
            print("Something went wrong! Check Serving UI and Status:")
            pprint(response.json())
            raise Exception("Endpoint failed!")
        time.sleep(30)
        response = requests.request(
            method="GET", headers=get_headers(token), url=endpoint_url
        )
        response.raise_for_status()
    return response.json()


def create_endpoint(
    endpoint_name,
    model_name,
    model_version,
    secret_scope_name,
    secret_name,
    db_host,
    token,
    workload_size="Small",
    block_until_deployed=True,
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
            "scale_to_zero_enabled": "true",
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
            ],
        }
    ]

    request_data = {"name": endpoint_name, "config": {"served_models": served_models}}
    json_bytes = json.dumps(request_data).encode("utf-8")
    response = requests.post(endpoint_url, data=json_bytes, headers=get_headers(token))
    response.raise_for_status()
    if block_until_deployed:
        wait_for_endpoint(endpoint_name, db_host, token)
    try:
        displayHTML(
            f"""Created the <a href="/#mlflow/endpoints/{endpoint_name}" target="_blank">{endpoint_name}</a> serving endpoint"""
        )
    except:
        print(
            f"Created serving endpoint {endpoint_name} at {db_host}/#mlflow/endpoints/{endpoint_name}"
        )


######## Secret handling
def list_scopes(host, db_token):
    response = requests.get(
        get_endpoint_url(ENDPOINT_MAP["list_scopes"], host),
        headers=get_headers(db_token),
    )
    response.raise_for_status()
    return response.text


def create_scope(scope_name, host, db_token):
    pay = {
        "scope": scope_name,
    }
    response = requests.post(
        get_endpoint_url(ENDPOINT_MAP["create_scope"], host),
        data=dump(pay),
        headers=get_headers(db_token),
    )
    print(response.text)
    response.raise_for_status()
    return response.text


def create_secret_in_scope(key, value, scope_name, host, db_token):
    base64_encoded_value = base64.b64encode(value.encode("utf-8")).decode("utf-8")
    pay = {
        "scope": scope_name,
        "key": key,
        "value": value,
        "bytes_value": base64_encoded_value,
    }
    response = requests.post(
        get_endpoint_url(ENDPOINT_MAP["create_scret"], host),
        data=dump(pay),
        headers=get_headers(db_token),
    )
    response.raise_for_status()
    return response.text


def list_secrets_in_scope(scope_name, host, db_token):
    pay = {
        "scope": scope_name,
    }
    response = requests.get(
        get_endpoint_url(ENDPOINT_MAP["list_secrets"], host),
        data=dump(pay),
        headers=get_headers(db_token),
    )
    response.raise_for_status()
    return response.text


def scope_exists(scope_name, host, db_token):
    scopes = json.loads(list_scopes(host, db_token))
    if not scopes:
        return False
    if "scopes" not in scopes:
        return False
    scopes = scopes["scopes"]
    return len(list(filter(lambda x: x["name"] == scope_name, scopes))) == 1


def setup_secrets(scope_name, secret_name, secret_value, host, db_token):
    # 1) create scope
    if not scope_exists(scope_name=scope_name, host=host, db_token=db_token):
        print(f"Scope {scope_name} does not exist, creating it")
        create_scope(scope_name, host, db_token=db_token)
    # 2) Write license
    print(f"Writing license to scope {scope_name}")
    create_secret_in_scope(
        key=secret_name,
        value=secret_value,
        scope_name=scope_name,
        host=host,
        db_token=db_token,
    )
    # 3) Write DB API URL
    create_secret_in_scope(
        key="DB_API_URL",
        value=os.environ["DATABRICKS_HOST"],
        scope_name="JSL_SCOPE",
        host=os.environ["DATABRICKS_HOST"],
        db_token=os.environ["DATABRICKS_TOKEN"],
    )


####### Mlfow Client Utils


def delete_registerd_model(name):
    from mlflow import MlflowClient

    print(f"Deleting registered model {name}")
    return MlflowClient().delete_registered_model(name)


def delete_all_registerd_model(name):
    # TODO
    from mlflow import MlflowClient

    # MlflowClient().list_artifacts()
    return MlflowClient().delete_registered_model(name)


def get_latest_registerd_model_version(name):
    from mlflow import MlflowClient

    model = MlflowClient().get_registered_model(name)
    return model.latest_versions[-1].version


def model_exists(name):
    from mlflow import MlflowClient

    try:
        model = MlflowClient().get_registered_model(name)
    except:
        return False
    return True


############### High level Deployment & Query


def query_endpoint(data, nlu_model_name, db_host, db_token, base_name=None):
    # 5. Query the Endpoint
    # endpoint_name = f"{nlu_model_name.replace('.','_')}_ENDPOINT"
    endpoint_name = nlu_name_to_endpoint(base_name if base_name else nlu_model_name)
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


def query_to_json(in_data: Union[str, List[str]]):
    data = {}
    data["dataframe_split"] = {}
    data["dataframe_split"]["columns"] = ["text"]
    if isinstance(in_data, str):
        data["dataframe_split"]["data"] = [in_data]
    elif isinstance(in_data, list):
        data["dataframe_split"]["data"] = in_data
    else:
        raise Exception("Input must be str or list of str ")
    return json.dumps(data)


def log_nlu_model(nlu_model_name, registerd_model_name):
    import mlflow

    # 1. Load the model
    if isinstance(nlu_model_name, str):
        nlu_model = nlp.load(nlu_model_name)
    else:
        # pre-loaded pipe
        nlu_model = nlu_model_name

    # 2. Log the model
    mlflow.johnsnowlabs.log_model(
        nlu_model, "model", registered_model_name=registerd_model_name
    )

    # # 3. Download wheels to the model (current version +1)
    mlflow.models.utils.add_libraries_to_model(
        f"models:/{registerd_model_name}/latest",
        registered_model_name=registerd_model_name,
    )


def nlu_name_to_endpoint(nlu_model_name):
    return f"{nlu_model_name.replace('.', '_')}_ENDPOINT"


def nlu_name_to_registerd_model(nlu_model_name):
    return f"{nlu_model_name.replace('.', '_')}_REGISTERD_MODEL"


def is_nlu_pipe(pipe):
    from nlu.pipe.pipeline import NLUPipeline

    return isinstance(pipe, NLUPipeline)


def query_and_deploy_if_missing(
    model,
    query,
    re_create_endpoint=False,
    re_create_model=False,
    base_name=None,
    is_json_query=False,
    db_host=None,
    db_token=None,
    workload_size="Small",
    new_run=True,
    block_until_deployed=True,
):
    """
    nlu_model: reference to nlu_model you want to query or  NLU convertable pipe
    Supported types are
    - List[Annotator]
    - Pipeline
    - LightPipeline
    - PretrainedPipeline
    - PipelineModel
    - NLUPipeline
    - String Reference to NLU Pipeline name
        See https://nlp.johnsnowlabs.com/docs/en/jsl/utils_for_spark_nlp#nlptonlupipepipe for more details

    query: str or list of strings or raw json string. If raw json, is_json_query must be True
    is_json_query: if True, query is treated as raw json string
    base_name: Name-Prefix for all resources created (Endpoints, Models, etc). If using non nlu referenced based models, you must specify this.
    re_create_endpoint: if False, endpoint creation is skipped if one already exists. If True, it will delete existing endpoint if it exists
    re_create_model: if False, model creation is skipped if one already exists. If True, model will be re-logged again, bumping the current version by 2
    workload_size: one of Small, Medium, Large.
    new_run: if True, mlflow will start a new run before logging the model
    db_host: the databricks host URL. If not specified, the DATABRICKS_HOST environment variable is used
    db_token: the databricks Access Token. If not specified, the DATABRICKS_TOKEN environment variable is used
    block_until_deployed: if True, this function will block until the endpoint is deployed. If False, it will return immediately after the endpoint is created
    """

    if not db_host:
        db_host = os.environ.get("DATABRICKS_HOST")
    if not db_token:
        db_token = os.environ.get("DATABRICKS_TOKEN")
    if not db_host:
        raise Exception(
            "You must specify DATABRICKS_HOST and DATABRICKS_TOKEN en variables"
        )
    if workload_size not in ["Small", "Medium", "Large"]:
        raise Exception("workload_size must be one of Small, Medium, Large")
    if new_run:
        import mlflow

        mlflow.end_run()
        mlflow.start_run()

    if isinstance(model, str):
        deploy_nlu_model_as_endpoint(
            model,
            re_create_endpoint=re_create_endpoint,
            re_create_model=re_create_model,
            db_host=db_host,
            db_token=db_token,
            workload_size=workload_size,
            block_until_deployed=block_until_deployed,
        )
    else:
        if not base_name:
            raise Exception(
                "If you want to deploy custom pipes, you need to specify base_name"
            )
        try:
            model = nlp.to_nlu_pipe(model)
        except:
            raise Exception("Failure converting your model to NLU pipe")
        deploy_nlu_model_as_endpoint(
            model,
            re_create_endpoint=re_create_endpoint,
            re_create_model=re_create_model,
            base_name=base_name,
            db_host=db_host,
            db_token=db_token,
            workload_size=workload_size,
            block_until_deployed=block_until_deployed,
        )
    if not block_until_deployed:
        return
    return query_endpoint(
        query if is_json_query else query_to_json(query),
        model,
        db_host,
        db_token,
        base_name,
    )


def deploy_nlu_model_as_endpoint(
    model_name,
    re_create_endpoint=False,
    re_create_model=False,
    base_name=None,
    db_host=None,
    db_token=None,
    workload_size="Small",
    block_until_deployed=True,
):
    os.environ["MLFLOW_WHEELED_MODEL_PIP_DOWNLOAD_OPTIONS"] = "--prefer-binary"
    SCOPE_NAME = "JSL_SCOPE"
    SECRET_NAME = "JSL_SECRET_NAME"
    SECRET_VALUE = os.environ["JOHNSNOWLABS_LICENSE_JSON_FOR_CONTAINER"]
    REGISTERD_MODEL_NAME = nlu_name_to_registerd_model(
        base_name if base_name else model_name
    )
    ENDPOINT_NAME = nlu_name_to_endpoint(base_name if base_name else model_name)

    if not model_exists(REGISTERD_MODEL_NAME) or re_create_model:
        # 1. Log the model
        if model_exists(REGISTERD_MODEL_NAME):
            delete_registerd_model(REGISTERD_MODEL_NAME)
        log_nlu_model(model_name, REGISTERD_MODEL_NAME)
    else:
        print(
            "Model already has been logged, skipping logging and using latest. Set re_create_model=True if you want to cre-create it"
        )

    MODEL_VERSION = get_latest_registerd_model_version(REGISTERD_MODEL_NAME)

    if not endpoint_exists(ENDPOINT_NAME, db_host, db_token) or re_create_endpoint:
        if endpoint_exists(ENDPOINT_NAME, db_host, db_token):
            print(f"Deleting exisiting Endpoint {ENDPOINT_NAME}")
            delete_endpoint(ENDPOINT_NAME, db_host, db_token)

        # 2. Create endpboint & Secret Scope if missing. TOdo detect if missing?
        setup_secrets(
            secret_name=SECRET_NAME,
            secret_value=SECRET_VALUE,
            scope_name=SCOPE_NAME,
            host=db_host,
            db_token=db_token,
        )

        # 3. Deploy Endpoint
        create_endpoint(
            endpoint_name=ENDPOINT_NAME,
            model_name=REGISTERD_MODEL_NAME,
            model_version=MODEL_VERSION,
            secret_scope_name=SCOPE_NAME,
            secret_name=SECRET_NAME,
            db_host=db_host,
            token=db_token,
            workload_size=workload_size,
            block_until_deployed=block_until_deployed,
        )
    else:
        print(
            f"Endpoint {ENDPOINT_NAME} already exists!  Set re_create_endpoint=True if you want to re-create it "
        )
