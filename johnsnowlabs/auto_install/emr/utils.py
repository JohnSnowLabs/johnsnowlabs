import time
from os import path
from typing import Any, Dict, Optional

import boto3

from johnsnowlabs.utils.s3_utils import parse_s3_url, upload_file_to_s3

_TERMINAL_STATES = {"FINISHED", "FAILED", "STOPPED", "FAILING", "STOPPING"}
_SUCCESS_STATES = {"FINISHED"}


def upload_notebook_to_s3(
    boto_session: boto3.Session,
    workspace_storage_s3_url: str,
    editor_id: str,
    path_to_notebook: str,
) -> str:
    """Uploads a notebook to S3 and returns its s3 url
    :param workspace_storage_s3_url: S3 path to workspace storage
    :param editor_id: EMR editor id
    :param path_to_notebook: Local Path to notebook
    """
    if not boto_session:
        boto_session = boto3.Session()
    # Upload local notebook to S3
    if not path.exists(path_to_notebook):
        raise FileNotFoundError(f"Notebook {path_to_notebook} not found")
    notebook_name = path.basename(path_to_notebook)

    bucket, key = parse_s3_url(workspace_storage_s3_url)

    file_name_key = f"{key}/{editor_id}/{notebook_name}"

    return upload_file_to_s3(
        boto_session=boto_session,
        file_path=path_to_notebook,
        bucket=bucket,
        file_name=file_name_key,
    )


def run_local_notebook(
    boto_session: boto3.Session,
    workspace_storage_s3_url: str,
    cluster_id: str,
    editor_id: str,
    path_to_notebook: str,
) -> str:
    """Runs an EMR notebook using boto3"""
    if not boto_session:
        boto_session = boto3.Session()

    emr_client = boto_session.client("emr")
    upload_notebook_to_s3(
        boto_session=boto_session,
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


def get_notebook_execution_status(
    boto_session: boto3.Session,
    execution_id: str,
) -> Dict[str, Any]:
    """Returns the current status and metadata for an EMR notebook execution.

    :param boto_session: Boto3 session
    :param execution_id: EMR notebook execution ID returned by start_notebook_execution
    :return: NotebookExecution dict from the EMR describe_notebook_execution API
    """
    if not boto_session:
        boto_session = boto3.Session()
    emr_client = boto_session.client("emr")
    response = emr_client.describe_notebook_execution(
        NotebookExecutionId=execution_id
    )
    return response["NotebookExecution"]


def wait_for_notebook_execution(
    boto_session: boto3.Session,
    execution_id: str,
    poll_interval: int = 30,
    timeout: Optional[int] = None,
    verbose: bool = True,
) -> Dict[str, Any]:
    """Polls until the notebook execution reaches a terminal state.

    :param boto_session: Boto3 session
    :param execution_id: EMR notebook execution ID
    :param poll_interval: Seconds between status checks (default 30)
    :param timeout: Max seconds to wait, or None to wait indefinitely
    :param verbose: If True, print status on each poll
    :return: Final NotebookExecution dict from the EMR API
    :raises TimeoutError: If timeout is exceeded before a terminal state is reached
    :raises RuntimeError: If the execution ends in a non-success state
    """
    if not boto_session:
        boto_session = boto3.Session()

    elapsed = 0
    while True:
        details = get_notebook_execution_status(boto_session, execution_id)
        status = details.get("Status", "UNKNOWN")

        if verbose:
            print(f"[EMR] Notebook execution {execution_id}: {status}")

        if status in _TERMINAL_STATES:
            if status not in _SUCCESS_STATES:
                reason = details.get("LastStateChangeReason", "no reason provided")
                raise RuntimeError(
                    f"Notebook execution {execution_id} ended with status {status!r}: {reason}"
                )
            return details

        if timeout is not None and elapsed >= timeout:
            raise TimeoutError(
                f"Notebook execution {execution_id} did not finish within {timeout}s "
                f"(last status: {status!r})"
            )

        time.sleep(poll_interval)
        elapsed += poll_interval


def run_local_notebook_and_wait(
    boto_session: boto3.Session,
    workspace_storage_s3_url: str,
    cluster_id: str,
    editor_id: str,
    path_to_notebook: str,
    poll_interval: int = 30,
    timeout: Optional[int] = None,
    verbose: bool = True,
) -> Dict[str, Any]:
    """Uploads a local notebook to S3, starts execution, and blocks until it finishes.

    Convenience wrapper around run_local_notebook and wait_for_notebook_execution.
    Raises on failure so the caller does not need to manually check the returned status.

    :param boto_session: Boto3 session
    :param workspace_storage_s3_url: S3 path to workspace storage
    :param cluster_id: EMR cluster ID
    :param editor_id: EMR editor ID
    :param path_to_notebook: Local path to the .ipynb file
    :param poll_interval: Seconds between status checks (default 30)
    :param timeout: Max seconds to wait, or None to wait indefinitely
    :param verbose: If True, print the execution ID and status updates
    :return: Final NotebookExecution dict from the EMR API
    :raises FileNotFoundError: If the notebook file does not exist locally
    :raises TimeoutError: If timeout is exceeded before the execution completes
    :raises RuntimeError: If the execution ends in a non-success state
    """
    if not boto_session:
        boto_session = boto3.Session()

    execution_id = run_local_notebook(
        boto_session=boto_session,
        workspace_storage_s3_url=workspace_storage_s3_url,
        cluster_id=cluster_id,
        editor_id=editor_id,
        path_to_notebook=path_to_notebook,
    )

    if verbose:
        print(f"[EMR] Started notebook execution: {execution_id}")

    return wait_for_notebook_execution(
        boto_session=boto_session,
        execution_id=execution_id,
        poll_interval=poll_interval,
        timeout=timeout,
        verbose=verbose,
    )
