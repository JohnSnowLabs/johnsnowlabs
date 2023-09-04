from typing import List, Optional

import boto3

from johnsnowlabs import settings
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.boto_utils import get_aws_used_creds


def get_printable_glue_notebook_commands(
    glue_assets_bucket: str,
    sts_client: boto3.client,
    packages_s3_location: List[str],
    jars_s3_location: List[str],
    secrets: Optional[JslSecrets] = None,
):
    register_listener = (
        secrets.HC_LICENSE
        and "spark._jvm.com.johnsnowlabs.util.start.registerListenerAndStartRefresh()"
    ) or (
        secrets.OCR_LICENSE
        and "spark._jvm.com.johnsnowlabs.util.OcrStart.registerListenerAndStartRefresh()"
    )

    aws_creds = get_aws_used_creds()
    # Keys to be used for S3 access
    s3a_creds_conf = f"""--conf spark.hadoop.fs.s3a.access.key={aws_creds.access_key} 
--conf spark.hadoop.fs.s3a.secret.key={aws_creds.secret_key}"""
    if aws_creds.token:
        s3a_creds_conf += f""" 
--conf spark.hadoop.fs.s3a.session.token={aws_creds.token}"""

    if secrets and any([secrets.HC_LICENSE, secrets.OCR_LICENSE]):
        # Also append license and jsl keys
        jsl_secrets_conf = f""" 
--conf jsl.settings.license={secrets.HC_LICENSE or secrets.OCR_LICENSE} 
--conf spark.jsl.settings.pretrained.credentials.access_key_id={secrets.AWS_ACCESS_KEY_ID} 
--conf spark.jsl.settings.pretrained.credentials.secret_access_key={secrets.AWS_SECRET_ACCESS_KEY}"""

        s3a_creds_conf = s3a_creds_conf + jsl_secrets_conf

    return f"""

Add the following lines in the beginning of your Glue notebook job:

1. %additional_python_modules {Software.jsl_lib.pypi_name}=={settings.raw_version_jsl_lib},{
   ",".join([path for path in packages_s3_location])
}

2. %extra_jars {",".join([path for path in jars_s3_location])}

3. %%configure 
{{
    "--conf": \"\"\"spark.jsl.settings.pretrained.cache_folder=s3://{glue_assets_bucket}/cache_pretrained/  
--conf spark.jars.packages=org.apache.hadoop:hadoop-aws:3.2.1,com.amazonaws:aws-java-sdk:1.11.828 
{s3a_creds_conf} 
--conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem 
--conf spark.hadoop.fs.s3a.path.style.access=true 
--conf spark.jsl.settings.aws.region={sts_client.meta.region_name}\"\"\"
}}

4. 
%glue_version 4.0
%number_of_workers 2 

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
{register_listener}
job = Job(glueContext)
"""
