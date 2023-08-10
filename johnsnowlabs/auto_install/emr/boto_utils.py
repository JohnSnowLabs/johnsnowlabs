from os import environ

import boto3


def get_boto_client(service) -> boto3.client:
    payload = {}
    if environ.get("EMR_AWS_ACCESS_KEY_ID"):
        payload["aws_access_key_id"] = environ.get("EMR_AWS_ACCESS_KEY_ID")
    if environ.get("EMR_AWS_SECRET_ACCESS_KEY"):
        payload["aws_secret_access_key"] = environ.get("EMR_AWS_SECRET_ACCESS_KEY")
    if environ.get("EMR_AWS_SESSION_TOKEN"):
        payload["aws_session_token"] = environ.get("EMR_AWS_SESSION_TOKEN")
    payload["region_name"] = environ.get("EMR_AWS_REGION", "us-east-1")
    payload["profile_name"] = environ.get("AWS_PROFILE", "default")

    session = boto3.Session(**payload)
    return session.client(service)
