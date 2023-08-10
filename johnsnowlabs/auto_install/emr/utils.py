from os import path

import boto3

from johnsnowlabs.auto_install.emr.boto_utils import get_boto_client
from johnsnowlabs.auto_install.emr.s3_utils import parse_s3_url, upload_file_to_s3


def upload_notebook_to_s3(
    workspace_storage_s3_url: str,
    editor_id: str,
    path_to_notebook: str,
) -> str:
    """Uploads a notebook to S3 and returns its s3 url
    :param workspace_storage_s3_url: S3 path to workspace storage
    :param editor_id: EMR editor id
    :param path_to_notebook: Local Path to notebook
    """
    # Upload local notebook to S3
    s3_client = get_boto_client("s3")
    if not path.exists(path_to_notebook):
        raise FileNotFoundError(f"Notebook {path_to_notebook} not found")
    notebook_name = path.basename(path_to_notebook)

    bucket, key = parse_s3_url(workspace_storage_s3_url)

    file_name_key = f"{key}/{editor_id}/{notebook_name}"

    return upload_file_to_s3(
        s3_client=s3_client,
        file_path=path_to_notebook,
        bucket=bucket,
        file_name=file_name_key,
    )


def run_local_notebook(
    workspace_storage_s3_url: str,
    cluster_id: str,
    editor_id: str,
    path_to_notebook: str,
):
    """Runs an EMR notebook using boto3"""

    emr_client = get_boto_client("emr")
    upload_notebook_to_s3(
        workspace_storage_s3_url=workspace_storage_s3_url,
        editor_id=editor_id,
        path_to_notebook=path_to_notebook,
    )

    notebook_name = path.basename(path_to_notebook)

    response = emr_client.start_notebook_execution(
        EditorId=editor_id,
        RelativePath=notebook_name,
        ExecutionEngine={"Id": cluster_id},
        ServiceRole="EMR_Studio_Service_Role",
    )
    return response["NotebookExecutionId"]
