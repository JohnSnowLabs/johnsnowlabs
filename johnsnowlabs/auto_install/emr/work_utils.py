import os
from random import randrange
from typing import Optional

import boto3
import botocore

from johnsnowlabs.auto_install.emr.boto_utils import get_boto_client
from johnsnowlabs.auto_install.emr.errors import BotoException
from johnsnowlabs.auto_install.emr.s3_utils import (
    check_if_file_exists_in_s3,
    create_emr_bucket,
    upload_content,
    upload_file_to_s3,
)
from johnsnowlabs.utils.file_utils import path_tail


def run_in_emr(
    py_script_path: str,
    cluster_id: str,
    script_bucket: Optional[str] = None,
    bucket_folder_path: Optional[str] = None,
    run_name: Optional[str] = None,
    execution_role_arn: Optional[str] = None,
) -> str:
    """Run a python script in EMR cluster
    :param py_script_path: Script content or path to script file in local file system or S3
    :param cluster_id: EMR cluster id
    :param script_bucket: S3 bucket where the script will be uploaded
    :param bucket_folder_path: S3 bucket folder where the script will be uploaded
    :param run_name: Name of the step
    :param execution_role_arn: IAM role to use for the step
    :return: Step id
    """
    s3_client = get_boto_client("s3")
    if check_if_file_exists_in_s3(s3_client, py_script_path):
        s3_path = py_script_path
    else:
        sts_client = get_boto_client("sts")
        # Making sure bucket exists

        script_bucket = create_emr_bucket(sts_client, s3_client, script_bucket)

        script_s3_path = temporary_script_name = f"{randrange(1333777)}tmp.py"
        if bucket_folder_path is not None:
            script_s3_path = os.path.join(bucket_folder_path, temporary_script_name)
        local_script = os.path.expanduser(py_script_path)
        if os.path.exists(local_script):
            s3_path = upload_file_to_s3(
                s3_client=s3_client,
                file_path=local_script,
                bucket=script_bucket,
                file_name=script_s3_path,
            )
        else:
            s3_path = upload_content(
                s3_client=s3_client,
                content=py_script_path,
                bucket=script_bucket,
                file_name=script_s3_path,
            )

    payload = {
        "JobFlowId": cluster_id,
        "Steps": [
            {
                "Name": run_name or path_tail(s3_path),
                "ActionOnFailure": "CONTINUE",
                "HadoopJarStep": {
                    "Jar": "command-runner.jar",
                    "Args": [
                        "spark-submit",
                        "--master",
                        "yarn",
                        s3_path,
                    ],
                },
            }
        ],
    }
    if execution_role_arn:
        payload["ExecutionRoleArn"] = execution_role_arn

    try:
        try:
            emr_client = get_boto_client("emr")
            response = emr_client.add_job_flow_steps(**payload)
            return response["StepIds"][0]
        except botocore.exceptions.ClientError as e:
            raise BotoException(
                code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
            )
    except Exception as e:
        print("❌ Failed running script in EMR cluster. Error: ", e)
