import os
from random import randrange
from typing import Optional

from johnsnowlabs.utils.boto_utils import BotoException
from johnsnowlabs.utils.file_utils import path_tail
from johnsnowlabs.utils.s3_utils import (
    check_if_file_exists_in_s3,
    create_bucket,
    upload_content,
    upload_file_to_s3,
)


def create_emr_bucket(boto_session: "boto3.Session", bucket=None):
    """Create a bucket for EMR cluster logs
    :param boto_session: Boto3 session
    :param bucket: Bucket name
    """
    import botocore

    try:
        sts_client = boto_session.client("sts")
        account_id = sts_client.get_caller_identity()["Account"]
        region = sts_client.meta.region_name
        if not bucket:
            bucket = f"johnsnowlabs-emr-{account_id}-{region}"

        return create_bucket(boto_session=boto_session, bucket=bucket)

    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            return bucket
        raise BotoException(
            code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
        )


def run_in_emr(
    py_script_path: str,
    cluster_id: str,
    boto_session: Optional["boto3.Session"] = None,
    script_bucket: Optional[str] = None,
    bucket_folder_path: Optional[str] = None,
    run_name: Optional[str] = None,
    execution_role_arn: Optional[str] = None,
) -> str:
    """Run a python script in EMR cluster
    :param boto_session: Boto3 session. Refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
    :param py_script_path: Script content or path to script file in local file system or S3
    :param cluster_id: EMR cluster id
    :param script_bucket: S3 bucket where the script will be uploaded
    :param bucket_folder_path: S3 bucket folder where the script will be uploaded
    :param run_name: Name of the step
    :param execution_role_arn: IAM role to use for the step
    :return: Step id
    """
    import boto3
    import botocore

    if not boto_session:
        boto_session = boto3.Session()
    if check_if_file_exists_in_s3(py_script_path):
        s3_path = py_script_path
    else:
        # Making sure bucket exists

        script_bucket = create_emr_bucket(
            boto_session=boto_session, bucket=script_bucket
        )

        script_s3_path = temporary_script_name = f"{randrange(1333777)}tmp.py"
        if bucket_folder_path is not None:
            script_s3_path = os.path.join(bucket_folder_path, temporary_script_name)
        local_script = os.path.expanduser(py_script_path)
        if os.path.exists(local_script):
            s3_path = upload_file_to_s3(
                boto_session=boto_session,
                file_path=local_script,
                bucket=script_bucket,
                file_name=script_s3_path,
            )
        else:
            s3_path = upload_content(
                boto_session=boto_session,
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
            emr_client = boto_session.client("emr")
            response = emr_client.add_job_flow_steps(**payload)
            return response["StepIds"][0]
        except botocore.exceptions.ClientError as e:
            raise BotoException(
                code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
            )
    except Exception as e:
        print("❌ Failed running script in EMR cluster. Error: ", e)
