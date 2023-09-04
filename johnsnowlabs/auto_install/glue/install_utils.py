from typing import List, Optional, Tuple

import boto3
import botocore

from johnsnowlabs.py_models.install_info import InstallSuite, LocalPy4JLib
from johnsnowlabs.utils.boto_utils import BotoException
from johnsnowlabs.utils.s3_utils import create_bucket, upload_file_to_s3


def create_glue_bucket(bucket=None):
    """Create a bucket for EMR cluster logs
    :param bucket_name: Bucket name
    """
    try:
        sts_client = boto3.client("sts")
        account_id = sts_client.get_caller_identity()["Account"]
        region = sts_client.meta.region_name
        if not bucket:
            bucket = f"aws-glue-assets-{account_id}-{region}"

        return create_bucket(region=region, bucket_name=bucket)

    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            return bucket
        raise BotoException(
            code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
        )


def upload_pylibs_jars_to_glue_bucket(
    install_suite: InstallSuite, bucket: Optional[str]
) -> Tuple[List[str], List[str]]:
    libs: List[LocalPy4JLib] = [install_suite.nlp, install_suite.ocr, install_suite.hc]
    uploaded_python_packages = []
    uploaded_jars = []
    for lib in libs:
        if lib:
            if lib.java_lib:
                s3_jar_file_name = upload_file_to_s3(
                    file_path=lib.get_java_path(),
                    bucket=bucket,
                    file_name=f"assets/jars/{lib.java_lib.file_name}",
                )
                uploaded_jars.append(s3_jar_file_name)
                print(f"✅ Successfully uploaded to {s3_jar_file_name}")
            if lib.py_lib:
                print(f"Uploading {lib.py_lib.file_name} ...")
                pypi_jar_file_name = upload_file_to_s3(
                    file_path=lib.get_py_path(),
                    bucket=bucket,
                    file_name=f"assets/packages/{lib.py_lib.file_name}",
                )
                uploaded_python_packages.append(pypi_jar_file_name)
                print(f"✅ Successfully uploaded to {pypi_jar_file_name}")
    return [uploaded_jars, uploaded_python_packages]
