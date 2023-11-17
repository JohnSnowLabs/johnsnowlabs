class BotoException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.code}: {self.message}"


def get_aws_used_creds(session):
    return session.get_credentials().get_frozen_credentials()


# def get_boto_session() -> boto3.session.Session:
# payload = {}
# if environ.get("EMR_AWS_ACCESS_KEY_ID"):
# payload["aws_access_key_id"] = environ.get("EMR_AWS_ACCESS_KEY_ID")
# if environ.get("EMR_AWS_SECRET_ACCESS_KEY"):
# payload["aws_secret_access_key"] = environ.get("EMR_AWS_SECRET_ACCESS_KEY")
# if environ.get("EMR_AWS_SESSION_TOKEN"):
# payload["aws_session_token"] = environ.get("EMR_AWS_SESSION_TOKEN")
# payload["region_name"] = environ.get("EMR_AWS_REGION", "us-east-1")
# payload["profile_name"] = environ.get("AWS_PROFILE", "default")
# return boto3.Session(**payload)


# def get_boto_client(service) -> boto3.client:
# session = get_boto_session()
# return session.client(service)
