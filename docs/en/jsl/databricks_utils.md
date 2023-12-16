---
layout: docs 
seotitle: NLP | John Snow Labs
title: Utilities for Databricks
permalink: /docs/en/jsl/databricks-utils
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
  nav: jsl
---

<div class="main-docs" markdown="1">



## Endpoint Creation

You can Query&Deploy John Snow Labs models with 1 line of code as [Databricks Model Serve Endpoints](https://docs.databricks.com/en/machine-learning/model-serving/index.html).     
Data is passed to the  [predict()](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) function and predictions are shaped accordingly.         
You must create endpoints from a Databricks cluster created by [nlp.install](https://nlp.johnsnowlabs.com/docs/en/jsl/install_advanced#automatic-databricks-installation).

See [Cluster Creation Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/tree/main/notebooks/create_databricks_cluster.ipynb) 
and [Databricks Endpoint Tutorial Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/tree/main/notebooks/databricks_endpoints_tutorial.ipynb)      


```python
# You need `mlflow_by_johnsnowlabs` installed until next mlflow is released
! pip install mlflow_by_johnsnowlabs
from johnsnowlabs import nlp
nlp.deploy_endpoint('bert')
nlp.query_endpoint('bert_ENDPOINT','My String to embed')
```

`nlp.deploy_endpoint` will register a ML-FLow model into your registry and deploy an Endpoint with a JSL license. 
It has the following parameters:

| Parameter              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| `model`                | Model to be deployed as endpoint which is [converted into NluPipelines](https://nlp.johnsnowlabs.com/docs/en/jsl/utils_for_spark_nlp#nlptonlupipepipe), supported classes are: `String` Reference to NLU Pipeline name like 'bert', `NLUPipeline`, `List[Annotator]`, `Pipeline`, `LightPipeline`, `PretrainedPipeline`, `PipelineModel`. In case of a NLU reference, the endpoint name is auto-generated aus `<nlu_ref>_ENDPOINT` i.e. `bert_ENDPOINT`. '.' is replaced with '_' in the nlu reference for the endpoint name |
| `endpoint_name`        | Name for the deployed endpoint. Optional if using NLU model reference but mandatory for custom pipelines.                                                                                                                                                                                                                                                                                                                                                 |
| `re_create_endpoint`   | if False, endpoint creation is skipped if one already exists. If True, it will delete existing endpoint if it exists                                                                                                                                                                                                                                                                                                                                      |
| `re_create_model`      | if False, model creation is skipped if one already exists. If True, model will be re-logged again, bumping the current version by 2                                                                                                                                                                                                                                                                                                                       |
| `workload_size`        | one of Small, Medium, Large.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `gpu`                  | `True`/`False` to load  GPU-optimized jars or CPU-optimized jars in the container. Must use a gpu based `workload_type` if `gpu=true`                                                                                                                                                                                                                                                                                                                     |
| `new_run`              | if True, mlflow will start a new run before logging the model                                                                                                                                                                                                                                                                                                                                                                                             |
| `block_until_deployed` | if True, this function will block until the endpoint is created                                                                                                                                                                                                                                                                                                                                                                                           |
| `workload_type`        | `CPU` by default, use `GPU_SMALL` to spawn a GPU based endpoint instead. Check Databricks docs for alternative values                                                                                                                                                                                                                                                                                                                                     |
| `db_host`              | the databricks host URL. If not specified, the DATABRICKS_HOST environment variable is used                                                                                                                                                                                                                                                                                                                                                               |
| `db_token`             | the databricks Access Token. If not specified, the DATABRICKS_TOKEN environment variable is used                                                                                                                                                                                                                                                                                                                                                          |

`nlp.query_endpoint` translates your query to JSON, sends it to the endpoint and returns the result as pandas DataFrame.
It has the following parameters which are forwarded to the [model.predict()](https://nlp.johnsnowlabs.com/docs/en/jsl/predict_api) call inside of the endpoint:

| Parameter                   | Description                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------| 
| `endpoint_name`        | Name of the endpoint to query           |
| `query`                | str or list of strings or raw json string. If raw json, is_json_query must be True                |
| `is_json_query`        | if True, query is treated as raw json string                                                      |
| `output_level`              | One of `token`, `chunk`, `sentence`, `relation`, `document` to shape outputs                      | 
| `positions`                 | Set `True`/`False` to include or exclude character index position of predictions                  | 
| `metadata`                  | Set `True`/`False` to include additional metadata                                                 | 
| `drop_irrelevant_cols`      | Set `True`/`False` to drop irrelevant columns                                                     | 
| `get_embeddings`            | Set `True`/`False` to include embedding or not                                                    | 
| `keep_stranger_features`    | Set `True`/`False` to return columns not named "text", 'image" or "file_type" from your input data | 
| `multithread`               | Set `True`/`False` to use multi-Threading for inference. Auto-inferred if not set                 | 
| `db_host`              | the databricks host URL. If not specified, the DATABRICKS_HOST environment variable is used       |
| `db_token`             | the databricks Access Token. If not specified, the DATABRICKS_TOKEN environment variable is used  |



`nlp.query_endpoint` and `nlp.deploy_endpoint` check the following **mandatory** env vars to resolve wheels for endpoints

| Env Var Name                | Description                                                                                                                                                 | 
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HEALTHCARE_SECRET`         | Automatically set on your cluster if you run nlp.install()                                                                                                  |
| `VISUAL_SECRET`             | Automatically set if you run. `nlp.install(..., visual=True)`. You can only spawn visual endpoint from a cluster created by `nlp.install(..., visual=True)` |
| `JOHNSNOWLABS_LICENSE_JSON` | JSON content of your john snow labs licensed to use for endpoints. Should be **airgap license**                                                             |


## Submit a Task with nlp.run_in_databricks
Easily run Python code in a Databricks cluster, using the John Snow Labs library. 
The fastest way to test this out, is to create a cluster with `nlp.install()` and then use `nlp.run_in_databricks` to start a task.
You can parameterize your jobs, according to the [Databricks docs](https://docs.databricks.com/en/workflows/jobs/create-run-jobs.html#pass-parameters-to-a-databricks-job-task) via the  
```python

# Execute a Raw Python string as script on Databricks
from johnsnowlabs import *
script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))"""

cluster_id = nlp.install(json_license_path=my_license, databricks_host=my_host,databricks_token=my_token)
nlp.run_in_databricks(script,
                      databricks_cluster_id=cluster_id,
                      databricks_host=my_host,
                      databricks_token=my_token,
                      run_name='Python Code String Example')

```
This will start a **Job Run** which you can view in the **Workflows tab**

![databricks_cluster_submit_raw.png](/assets/images/jsl_lib/databricks_utils/submit_raw_str.png)

And after a while you can see the results 

![databricks_cluster_submit_raw.png](/assets/images/jsl_lib/databricks_utils/submit_raw_str_result.png)


### Run a local Python Notebook in Databricks

Provide the path to a notebook on your localhost, it will be copied to HDFS and executed by the Databricks cluster.
You need to provide a destination path to your Workspace, where the notebook will be copied to and you have write access to.
A common pattern that should work is`/Users/<your_databricks_email@somewhere.com>/test.ipynb`

```python
local_nb_path = "path/to/my/notebook.ipynb"
remote_dst_path = "/Users/christian@johnsnowlabs.com/test.ipynb"

# notebook.ipynb will run on databricks, url will be printed
nlp.run_in_databricks(
  local_nb_path,
  databricks_host=host,
  databricks_token=token,
  run_name="Notebook Test",
  dst_path=remote_dst_path,
)
```

This could be your input notebook

![databricks_cluster_submit_notebook.png](/assets/images/jsl_lib/databricks_utils/submit_notebook.png)

A URL where you can monitor the run will be printed, which will look like this

![databricks_cluster_submit_notebook_result.png](/assets/images/jsl_lib/databricks_utils/submit_notebook_result.png)





### Run a Python Function in Databricks

Define a function, which will be written to a local file, copied to HDFS and executed by the Databricks cluster.

```python
def my_function():
    import nlu
    medical_text = """A 28-year-old female with a history of gestational 
    diabetes presented with a one-week history of polyuria ,
     polydipsia , poor appetite , and vomiting ."""
    df = nlu.load('en.med_ner.diseases').predict(medical_text)
    for c in df.columns: print(df[c])

# my_function will run on databricks
nlp.run_in_databricks(my_function,
                      databricks_cluster_id=cluster_id,
                      databricks_host=my_host,
                      databricks_token=my_token,
                      run_name='Function test')

```
This example will print all columns of the resulting dataframe which contains medical NER predictions.

![databricks_cluster_submit_raw.png](/assets/images/jsl_lib/databricks_utils/submit_func.png)


### Run a Raw Python Code String in Databricks
Provide a string which must be valid Python Syntax.    
It will be written to string, copied to HDFS and executed by the Databricks Cluster.

```python
script = """
import nlu
print(nlu.load('sentiment').predict('That was easy!'))"""

nlp.run_in_databricks(script,
                      databricks_cluster_id=cluster_id,
                      databricks_host=my_host,
                      databricks_token=my_token,
                      run_name='Python Code String Example')

```


### Run a Python Script in Databricks
Provide the path to a script on your machine. It will be copied to the Databricks HDFS and executed as task.
```python
nlp.run_in_databricks('path/to/my/script.py',
                      databricks_cluster_id=cluster_id,
                      databricks_host=my_host,
                      databricks_token=my_token,
                      run_name='Script test ')
```

### Run a Python Module in Databricks

Provide a module accessible to the john snow labs library.
It's content's will be written to a local file, copied to HDFS and executed by the databricks cluster.

```python
import johnsnowlabs.auto_install.health_checks.nlp_test as nlp_test
nlp.run_in_databricks(nlp_test,
                      databricks_cluster_id=cluster_id,
                      databricks_host=my_host,
                      databricks_token=my_token,
                      run_name='nlp_test')
```




## Parameterizing your Databricks Jobs

You can parameterize `run_in_databricks` with parameters formatted according to the [job task API](https://docs.databricks.com/en/workflows/jobs/create-run-jobs.html#pass-parameters-to-a-databricks-job-task)




### Parameterizing a Notebook run in Databricks
In your notebook you can use `dbutils.widgets.text("my_parameter", "my_default_value")` and other [ipywidets](https://ipywidgets.readthedocs.io/en/7.7.0/examples/Widget%20List.html) to parameterize your notebook.
You just pass a dictionary to `run_in_databricks` where `key=parameter_name` and `value=parameter_value`. 
See this [example parameterized DB-Notebook](https://github.com/JohnSnowLabs/johnsnowlabs/tree/main/notebooks/parameterized_nb_example.ipynb) for a full example which you can use as `nb_path` parameter.

```python
nb_path = "parameterized_nb_example.ipynb"
dst_path = "/Users/christian@johnsnowlabs.com/test.ipynb"
nlp.run_in_databricks(
    nb_path,
    databricks_cluster_id=cluster_id,
    databricks_host=host,
    databricks_token=token,
    run_name="Parameterized Notebook",
    dst_path=dst_path,
    parameters={"input_text": "I love peanut butter", "model_name": "sentiment"},
)



```



### Parameterizing a Python Script run in Databricks
Simply pass a list of parameters to the `run_in_databricks` function. They will be passed to the script as `sys.argv` arguments.
```python


script = """
import sys
print(f"First argument: {sys.argv[1]}, Second argument: {sys.argv[2]}")
"""
arg1 = "My first arg"
arg2 = "My second arg"
nlp.run_in_databricks(
    script,
    databricks_cluster_id=cluster_id,
    databricks_host=host,
    databricks_token=token,
    run_name="Parameterized Script",
    parameters=[arg1, arg2],
)


```



</div>