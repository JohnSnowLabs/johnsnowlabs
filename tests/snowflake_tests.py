import os
from tests.utilsz import secrets

from johnsnowlabs import nlp



def test_create_service_udf_open_source():
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,
    )
    nlp.deploy_as_snowflake_udf('ner',
                                repo_url=repo_url,
                                role_name=role_name,
                                database_name=db_name,
                                warehouse_name=warehouse_name,
                                schema_name=schema_name,
                                compute_pool_name=compute_pool_name,
                                snowflake_user=secrets.snowflake_user,
                                snowflake_account=secrets.snowflake_account,
                                snowflake_password=secrets.snowflake_password,
                                )


def test_create_service_udf_healthcare():
    role_name, db_name, warehouse_name, schema_name, compute_pool_name, repo_url = nlp.snowflake_common_setup(
        secrets.snowflake_user, secrets.snowflake_account, secrets.snowflake_password,
        compute_pool_name='testpool6',
    )
    nlp.deploy_as_snowflake_udf('en.de_identify.clinical_pipeline',
                                                         repo_url=repo_url,
                                                         role_name=role_name,
                                                         database_name=db_name,
                                                         warehouse_name=warehouse_name,
                                                         schema_name=schema_name,
                                                         compute_pool_name=compute_pool_name,
                                                         snowflake_user=secrets.snowflake_user,
                                                         snowflake_account=secrets.snowflake_account,
                                                         snowflake_password=secrets.snowflake_password,
                                                         license_path=secrets.airgap_lic,
                                                         )


def test_create_service_udf_visual():
    nlp.deploy_as_snowflake_udf('todo', license_path=secrets.airgap_lic)
