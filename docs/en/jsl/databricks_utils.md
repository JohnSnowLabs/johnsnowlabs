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
nlp.query_and_deploy_if_missing('bert','My String to embed')
```

`nlp.query_and_deploy_if_missing` has the following parameters:

| Parameter              | Description                                                                                                                                                                                                                                                                                                                               |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| `model`                | Model to be deployed as endpoint which is [converted into NluPipelines](https://nlp.johnsnowlabs.com/docs/en/jsl/utils_for_spark_nlp#nlptonlupipepipe), supported classes are: `String` Reference to NLU Pipeline name like 'bert', `NLUPipeline`, `List[Annotator]`, `Pipeline`, `LightPipeline`, `PretrainedPipeline`, `PipelineModel`, |
| `query`                | str or list of strings or raw json string. If raw json, is_json_query must be True                                                                                                                                                                                                                                                        |
| `is_json_query`        | if True, query is treated as raw json string                                                                                                                                                                                                                                                                                              |
| `base_name`            | Name-Prefix for all resources created (Endpoints, Models, etc). If using non nlu referenced based models, you must specify this.                                                                                                                                                                                                          |
| `re_create_endpoint`   | if False, endpoint creation is skipped if one already exists. If True, it will delete existing endpoint if it exists                                                                                                                                                                                                                      |
| `re_create_model`      | if False, model creation is skipped if one already exists. If True, model will be re-logged again, bumping the current version by 2                                                                                                                                                                                                       |
| `workload_size`        | one of Small, Medium, Large.                                                                                                                                                                                                                                                                                                              |
| `new_run`              | if True, mlflow will start a new run before logging the model                                                                                                                                                                                                                                                                             |
| `db_host`              | the databricks host URL. If not specified, the DATABRICKS_HOST environment variable is used                                                                                                                                                                                                                                               |
| `db_token`             | the databricks Access Token. If not specified, the DATABRICKS_TOKEN environment variable is used                                                                                                                                                                                                                                          |
| `block_until_deployed` | if True, this function will block until the endpoint is created                                                                                                                                                                                                                                                                           |



## Submit a Task with nlp.run_in_databricks
Easily run Python code in a Databricks cluster, using the John Snow Labs library. 
The fastest way to test this out, is to create a cluster with `nlp.install()` and then use `nlp.run_in_databricks` to start a task.
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
This example will print all columns of the resulting dataframe which contains emdical NER predictions.

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


</div>