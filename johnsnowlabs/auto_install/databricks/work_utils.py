import inspect
import os.path
import time
from pathlib import Path
from types import ModuleType
from typing import Callable, Optional, List, Any

from johnsnowlabs.auto_install.databricks.dbfs import *
from johnsnowlabs.auto_install.databricks.install_utils import create_cluster
from johnsnowlabs.utils.file_utils import path_tail, str_to_file


class LifeCycleState:
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    SKIPPED = "SKIPPED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    BLOCKED = "BLOCKED"
    WAITING_FOR_RETRY = "WAITING_FOR_RETRY"

    end_states = [
        TERMINATING,
        TERMINATED,
        SKIPPED,
        INTERNAL_ERROR,
        BLOCKED,
    ]

    wait_states = [
        PENDING,
        RUNNING,
    ]


class ResultState:
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMEDOUT = "TIMEDOUT"
    CANCELED = "CANCELED"
    MAXIMUM_CONCURRENT_RUNS_REACHED = "MAXIMUM_CONCURRENT_RUNS_REACHED"
    EXCLUDED = "EXCLUDED"
    SUCCESS_WITH_FAILURES = "SUCCESS_WITH_FAILURES"
    UPSTREAM_FAILED = "UPSTREAM_FAILED"
    UPSTREAM_CANCELED = "UPSTREAM_CANCELED"

    wait_states = []

    end_states = [
        SUCCESS,
        FAILED,
        FAILED,
        TIMEDOUT,
        CANCELED,
        MAXIMUM_CONCURRENT_RUNS_REACHED,
        EXCLUDED,
        SUCCESS_WITH_FAILURES,
        UPSTREAM_FAILED,
        UPSTREAM_CANCELED,
    ]


def create_job_in_databricks(
    db: DatabricksAPI,
    local_python_script: str = None,
    cluster_id=None,
    name=None,
    new_cluster=None,
    libraries=None,
    email_notifications=None,
    timeout_seconds=None,
    max_retries=None,
    min_retry_interval_millis=None,
    retry_on_timeout=None,
    schedule=None,
    notebook_task=None,
    spark_jar_task=None,
    # spark_python_task=None,
    spark_submit_task=None,
    max_concurrent_runs=None,
    tasks=None,
    headers=None,
    version=None,
):
    #     https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsCreate
    dbfs_target_path = copy_from_local_to_hdfs(
        db=db,
        local_path=local_python_script,
        dbfs_path=get_db_path(local_python_script),
    )
    if not name:
        name = settings.db_job_name.format(
            job=get_db_path(local_python_script).split("/")[-1]
        )

    if not cluster_id:
        raise NotImplementedError("Not Cluster ID based install not yet implemented")

    db.jobs.create_job(
        name=name,
        spark_python_task=dbfs_target_path,
        notebook_task=notebook_task,
        spark_jar_task=spark_jar_task,
        spark_submit_task=spark_submit_task,
        libraries=libraries,
        existing_cluster_id=cluster_id,
        new_cluster=new_cluster,
        email_notifications=email_notifications,
        timeout_seconds=timeout_seconds,
        max_retries=max_retries,
        min_retry_interval_millis=min_retry_interval_millis,
        retry_on_timeout=retry_on_timeout,
        schedule=schedule,
        max_concurrent_runs=max_concurrent_runs,
        tasks=tasks,
        headers=headers,
        version=version,
    )


def run_local_py_script_as_task(
    db: DatabricksAPI,
    task_definition: Union[str, ModuleType, Callable],
    cluster_id: str = None,
    run_name: str = None,
    parameters: List[Any] = None,
    dst_path=None,
):
    """
    # https://docs.databricks.com/dev-tools/api/latest/examples.html#jobs-api-examples
    A job consists of 1 or more tasks
    :param db:
    :param task_definition:
    :param cluster_id:
    :param run_name:
    :return:
    """
    if not run_name:
        run_name = settings.db_run_name

    if not cluster_id:
        cluster_id = create_cluster(db)

    if (
        isinstance(task_definition, str)
        and os.path.exists(task_definition)
        and task_definition.endswith(".ipynb")
    ):
        # Notebook task, WIP
        # raise Exception("Notebook task not supported yet")
        if not dst_path:
            raise Exception("dst_path must be provided for notebook tasks")
        file_name = os.path.split(task_definition)[-1]
        run_id = submit_notebook_to_databricks(
            db, task_definition, cluster_id, dst_path, parameters, run_name=run_name
        )

    else:
        task_definition = executable_as_script(task_definition)

        copy_from_local_to_hdfs(
            db=db,
            local_path=task_definition,
            dbfs_path=get_db_path(task_definition) if not dst_path else dst_path,
        )
        py_task = dict(
            python_file=get_db_path(task_definition),
        )
        if parameters:
            py_task["parameters"] = parameters

        run_id = db.jobs.submit_run(
            existing_cluster_id=cluster_id,
            spark_python_task=py_task,
            run_name=run_name,
        )["run_id"]
    print(f"Stated task with run_id={run_id}")
    return run_id


def executable_as_script(py_executable: Union[str, ModuleType, Callable]):
    if (
        isinstance(py_executable, str)
        and os.path.exists(py_executable)
        and py_executable.endswith(".py")
    ):
        print(f"Detected Python Script for Databricks Submission")
        # Py file, we can just run this
        return py_executable
    if (
        isinstance(py_executable, str)
        and os.path.exists(py_executable)
        and py_executable.endswith(".ipynb")
    ):
        print(f"Detected Python Notebook for Databricks Submission")
        # Py file, we can just run this
        return py_executable
    if isinstance(py_executable, (str, ModuleType, Callable)):
        print(f"Module/Callable for Databricks Submission")
        # Convert Module/Callable into a script
        return executable_to_str(py_executable)
    raise TypeError(f"Invalid Executable Python  Task {py_executable}")


def executable_to_str(executable_to_convert: Union[str, ModuleType, Callable]):
    # write a python code-string/module/function into a temp file and return resulting python file

    Path(settings.tmp).mkdir(parents=True, exist_ok=True)
    from random import randrange

    if isinstance(executable_to_convert, str) and not os.path.exists(
        executable_to_convert
    ):
        # Executable script
        file_name = f"{randrange(1333777)}tmp.py"

    else:
        # Module/Callable
        try:
            file_name = path_tail(inspect.getfile(executable_to_convert))
        except:
            # Within a Python shell, we cannot getFile(), so we have this fallback name
            file_name = f"{randrange(1333777)}tmp.py"
    out_path = f"{settings.tmp}/{file_name}"

    if isinstance(executable_to_convert, str):
        print(f"Detected Python Code String")
        return str_to_file(executable_to_convert, out_path)

    if isinstance(executable_to_convert, Callable):
        print(f"Detected Python Function for Databricks Submission")
        return str_to_file(
            inspect.getsource(executable_to_convert)
            + f"\n{executable_to_convert.__name__}()",
            out_path,
        )

    if isinstance(executable_to_convert, ModuleType):
        print(f"Detected Python Module for Databricks Submission")
        return str_to_file(inspect.getsource(executable_to_convert), out_path)


def encode_nb(nb_path):
    import base64

    with open(nb_path, "rb") as f:
        encoded_nb = base64.b64encode(f.read()).decode("utf-8")
    return encoded_nb


def import_notebook_to_workspace(
    db: DatabricksAPI,
    dst_path: str,
    local_nb_path: str,
):
    db.workspace.import_workspace(
        path=dst_path,
        language="PYTHON",
        format="JUPYTER",
        content=encode_nb(local_nb_path),
        overwrite=True,
    )


def checkon_db_task(
    db: DatabricksAPI,
    run_id: str = None,
):
    """
    # https://docs.databricks.com/dev-tools/api/latest/examples.html#jobs-api-examples
    A job consists of 1 or more tasks
    :param db:
    :param task_definition:
    :param cluster_id:
    :param run_name:
    :return:
    """
    # https://docs.databricks.com/dev-tools/api/2.0/jobs.html#runstate
    return db.jobs.get_run(run_id=run_id)


def run_in_databricks(
    py_script_path: Union[str, ModuleType, Callable],
    databricks_cluster_id: Optional[str] = None,
    databricks_token: Optional[str] = None,
    databricks_host: Optional[str] = None,
    run_name: str = None,
    block_till_complete=True,
    dst_path: str = None,
    parameters: Any = None,
    return_job_url: bool = False,
):
    """

    :param py_script_path: Either
        - Path to local python script i.e "path/to/my_script.py"
        - Path to local python notebook i.e "path/to/my_notebook.ipynb"
        - string with python code i.e. "1+1"
        - python module i.e. import my_module
        - python function, i.e. def my_func(): return 1+1

    :param databricks_cluster_id: cluster ID to run your task on. If none provided, a cluster will be created first.
    :param databricks_token: databricks access token
    :param databricks_host: databricks host
    :param run_name: name of the run to generate, if None, a random name will be generated
    :param block_till_complete: if True, this function will block until the task is complete
    :param dst_path: path to store the python script/notebook. in databricks, mandatory for notebooks.
        I.e. /Users/<your@databricks.email.com>/test.ipynb
    :param parameters: parameters to pass to the python script/notebook formatted accordingly to https://docs.databricks.com/en/workflows/jobs/create-run-jobs.html#pass-parameters-to-a-databricks-job-task
    :param return_job_url: returns job_url instead of job_id
    :return: job_id if return_job_url=False else job_url
    """
    from johnsnowlabs.auto_install.databricks.install_utils import (
        get_db_client_for_token,
    )

    db_client = get_db_client_for_token(databricks_host, databricks_token)
    job_id = run_local_py_script_as_task(
        db_client,
        py_script_path,
        cluster_id=databricks_cluster_id,
        run_name=run_name,
        dst_path=dst_path,
        parameters=parameters,
    )

    if not block_till_complete:
        return job_id
    job_done = False
    link_logged = False
    while not job_done:
        job_status = checkon_db_task(db_client, job_id)
        if not link_logged and "run_page_url" in job_status:
            print(f"You can monitor the job at {job_status['run_page_url']}")
            link_logged = True

        if "result_state" in job_status["state"]:
            print(f"Job has a result! its {job_status['state']}")
            if return_job_url:
                return job_status, job_status["run_page_url"]
            else:
                return job_status
        elif "life_cycle_state" in job_status["state"]:
            print(
                f"Waiting 30 seconds, job {job_id}  is still running, its {job_status['state']}"
            )
        time.sleep(30)

    if return_job_url:
        return job_id, job_status["run_page_url"]
    else:
        return job_id


def submit_notebook_to_databricks(
    db: DatabricksAPI,
    local_nb_path,
    cluster_id,
    remote_path,
    parameters=None,
    run_name=None,
):
    # Instantiate the DatabricksAPI client
    # Read the local notebook content
    with open(local_nb_path, "rb") as file:
        content = file.read()

    # Base64 encode the content
    encoded_content = base64.b64encode(content).decode("utf-8")

    # Define the path on Databricks workspace where the notebook will be uploaded

    # Import the notebook to Databricks workspace
    db.workspace.import_workspace(
        path=remote_path,
        format="JUPYTER",
        language="PYTHON",
        content=encoded_content,
        overwrite=True,
    )

    # Define the notebook task
    notebook_task = {"notebook_path": remote_path}

    if parameters:
        notebook_task["base_parameters"] = parameters

    # Submit the job to run the notebook
    run_name = run_name or f"Notebook Run"
    response = db.jobs.submit_run(
        run_name=run_name,
        existing_cluster_id=cluster_id,
        notebook_task=notebook_task,
    )

    return response["run_id"]
