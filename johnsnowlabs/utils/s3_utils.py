from typing import Tuple

from johnsnowlabs.utils.boto_utils import BotoException


def parse_s3_url(s3_url: str) -> Tuple[str, str]:
    """Parse s3 url and return bucket and key"""
    return s3_url.split("/")[2], "/".join(s3_url.split("/")[3:]).rstrip("/")


def create_bucket(boto_session: "boto3.Session", bucket: str):
    """Create a bucket for EMR cluster logs
    :param boto_session: Botocore session
    :param bucket: Bucket name
    """
    import botocore

    try:
        s3_client = boto_session.client("s3")
        region = boto_session.region_name
        if region == "us-east-1":
            s3_client.create_bucket(
                Bucket=bucket,
            )
        else:
            s3_client.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={"LocationConstraint": region},
            )
        return bucket
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            return bucket
        raise BotoException(
            code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
        )


def check_if_file_exists_in_s3(boto_session: "boto3.Session", s3_url: str):
    """Check if file exists in s3 using s3 client
    :param boto_session : Botocore session
    :param s3_url: S3 url to check
    """
    import botocore

    try:
        s3_client = boto_session.client("s3")
        bucket, key = parse_s3_url(s3_url)
        s3_client.head_object(Bucket=bucket, Key=key)

        return True
    except botocore.exceptions.ClientError as e:
        return False
    except Exception:
        return False


def upload_file_to_s3(
    boto_session: "boto3.Session", file_path: str, bucket: str, file_name: str
) -> str:
    """Upload a file to s3 bucket
    :botocore_session: Botocore session
    :param file_path: Path to file to upload
    :param bucket: Bucket to upload to
    :param file_name: File name to create
    :return s3_url: S3 url of uploaded file
    """
    import botocore

    try:
        s3_client = boto_session.client("s3")
        s3_client.upload_file(file_path, bucket, file_name)
        return f"s3://{bucket}/{file_name}"
    except botocore.exceptions.ClientError as e:
        raise BotoException(
            code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
        )


def upload_content(
    boto_session: "boto3.Session", content: str, bucket: str, file_name: str
) -> str:
    import botocore

    """Upload content to s3 bucket
    :param boto_session: Botocore session
    :param content: Content to upload
    :param bucket: Bucket to upload to
    :param file_name: File name to create
    :return: s3_url: S3 url of uploaded file
    """

    try:
        s3_client = boto_session.client("s3")
        s3_client.put_object(Body=content, Bucket=bucket, Key=file_name)
        return f"s3://{bucket}/{file_name}"
    except botocore.exceptions.ClientError as e:
        raise BotoException(
            code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
        )
