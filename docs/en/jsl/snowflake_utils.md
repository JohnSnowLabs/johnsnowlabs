---
layout: docs
seotitle: NLP | John Snow Labs
title: Utilities for Snowflake
permalink: /docs/en/jsl/snowflake-utils
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
    nav: jsl
---
<div class="main-docs" markdown="1">

You can easily deploy any John Snow Labs models within the Snowpark Container Services Ecosystem via `nlp.deploy_as_snowflake_udf()`


## Setup Snowflake Resources 

To create a Role, Database, Warehouse, Schema, Compute Pool and Image Repository for John Snow Labs models you can run
`nlp.snowflake_common_setup` which re-produces the [Common Setup for Snowpark Container Services Tutorials](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/tutorials/common-setup#introduction) automatically
with the same resource-names as in the tutorial. 

You must have the [snowflake-connector-python](https://pypi.org/project/snowflake-connector-python/) library installed beforehand installed


```python
from johnsnowlabs import nlp 
role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
    snowflake_user='my_snowflake_user',
    snowflake_account='my_snowflake_account',
    snowflake_password='my_snowflake_password',
)
```
This will create the following resources: 
- role_name=`test_role`
- schema_name=`data_schema`
- repo_name=`tutorial_repository`
- stage_name=`tutorial_stage`
- db_name=`tutorial_db`
- warehouse_name=`tutorial_warehouse`
- compute_pool_name=`tutorial_compute_pool`

You can specify a custom name for any resource by specifying it as a key-word argument. 

```python
role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
    snowflake_user='my_snowflake_user',
    snowflake_account='my_snowflake_account',
    snowflake_password='my_snowflake_password',
    role_name='my_test_role',
    schema_name='my_data_schema',
    repo_name='my_tutorial_repository',
    stage_name='my_tutorial_stage',
    db_name='my_tutorial_db',
    warehouse_name='my_tutorial_warehouse',
    compute_pool_name='tutorial_compute_pool'
)

```

## Deploy Model as Snowflake Container Services UDF

`nlp.deploy_model_as_snowflake_udf()` will build, tag & push a John Snow Labs model server to your 
Snowflake image repository and finally create a service & udf from the model and test it.
Role, Database, Warehouse, Schema, Compute Pool and Image Repository muss be created beforehand and passwed as arguments. 
```python
# Either run `nlp.snowflake_common_setup` or manually create&specify these resources
from johnsnowlabs import nlp
role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = ...
nlp.deploy_as_snowflake_udf(
    nlu_ref='en.de_identify.clinical_pipeline',
    snowflake_user='my_snowflake_user',
    snowflake_account='my_snowflake_account',
    snowflake_password='my_snowflake_password',
    license_path='path/to/my/jsl_license.json',
    repo_url=repo_url,
    role_name=role_name,
    database_name=db_name,
    warehouse_name=warehouse_name,
    schema_name=schema_name,
    compute_pool_name=compute_pool_name,
)

```

`nlp.deploy_model_as_snowflake_udf()` will build, tag & push a John Snow Labs model server to your
Snowflake image repository and finally create a service & udf from the model and test it.
Role, Database, Warehouse, Schema, Compute Pool and Image Repository muss be created beforehand and passwed as arguments.
```python
# Either run `nlp.snowflake_common_setup` or manually create&specify these resources
from johnsnowlabs import nlp
role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = ...
nlp.deploy_as_snowflake_udf(
    nlu_ref='en.de_identify.clinical_pipeline',
    snowflake_user='my_snowflake_user',
    snowflake_account='my_snowflake_account',
    snowflake_password='my_snowflake_password',
    license_path='path/to/my/jsl_license.json',
    repo_url=repo_url,
    role_name=role_name,
    database_name=db_name,
    warehouse_name=warehouse_name,
    schema_name=schema_name,
    compute_pool_name=compute_pool_name,
)

```

You can also optionally specify the name of the created service & UDF 

```python
# Either run `nlp.snowflake_common_setup` or manually create&specify these resources
from johnsnowlabs import nlp
role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = ...
nlp.deploy_as_snowflake_udf(
    nlu_ref='en.de_identify.clinical_pipeline',
    snowflake_user='my_snowflake_user',
    snowflake_account='my_snowflake_account',
    snowflake_password='my_snowflake_password',
    license_path='path/to/my/jsl_license.json',
    repo_url=repo_url,
    role_name=role_name,
    database_name=db_name,
    warehouse_name=warehouse_name,
    schema_name=schema_name,
    compute_pool_name=compute_pool_name,
    udf_name='my_udf',
    service_name='my_service'
)
```

You can now use the `en_de_identify_clinical_pipeline_udf()` function within your Snowflake SQL and Python Worksheets
when using the created role, database, warehouse, schema.


You can run the following commands in Snowflake to get he status of the service and query the UDF 
```sql
-- Set context 
USE ROLE test_role;
USE DATABASE tutorial_db;
USE WAREHOUSE tutorial_warehouse;
USE SCHEMA data_schema;

-- Describe UDF
DESCRIBE FUNCTION JSL_RESOLVE_MEDICATION(varchar);


-- Get service status of UDF backend
SELECT SYSTEM$GET_SERVICE_STATUS('en_de_identify_clinical_pipeline_service');

-- Describe service 
DESCRIBE SERVICE tokenize_servicedelthi123s;

-- Get Logs of container  service
CALL SYSTEM$GET_SERVICE_LOGS('en_de_identify_clinical_pipeline_service', '0', 'jsl-container', 1000);

-- Call UDF
SELECT en_de_identify_clinical_pipeline_udf('The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet.');



```

## Streamlit Example with Snowpark services

Once you created an UDF in Snowflake you can access it within Streamlit Apps. 
Make sure to select the same resources to host your Streamlit app as used for hosting the UDF

This is a small example of a simple streamlit app you can now build: 
1. Go to the Streamlit Section in `Projects` within you Snowflake account
3. In the bottom left click on your username and then on switch role and select the role we just created. The default value is `test_role`
3. In the side-bar, click on Streamlit and then on the `+ Streamlit App` button. Specify a Database, Schema and Warehouse. The defaults are `TUTORIAL_DB`, `DATA_SCHEMA`, `TUTORIAL_WAREHOUSE`.
Copy and paste the following script into your streamlit app and run it 
```python
import streamlit as st
from snowflake.snowpark.context import get_active_session
session = get_active_session()
data = st.text_area("Type Your Text", value='Sample text', height=200)
udf_response = session.sql(f"""SELECT JSL_DEIDENTIFY_CLINICAL('{data}')""",)
st.write(udf_response.collect()[0].as_dict())
```

For a more advanced streamlit example, see [here](https://github.com/JohnSnowLabs/johnsnowlabs/blob/main/streamlits/advanced_snowflake.py)



</div>