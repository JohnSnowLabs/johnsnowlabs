import inspect
import os.path
from pathlib import Path
from types import ModuleType

from typing import Callable, Union, Optional

from databricks_api import DatabricksAPI

from johnsnowlabs.auto_install.databricks.dbfs import *
from johnsnowlabs.auto_install.databricks.install_utils import create_cluster
from johnsnowlabs.utils.file_utils import path_tail, str_to_file


def create_job_in_databricks(db: DatabricksAPI,
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
    dbfs_target_path = copy_from_local_to_hdfs(db=db, local_path=local_python_script,
                                               dbfs_path=get_db_path(local_python_script))
    if not name:
        name = settings.db_job_name.format(job=get_db_path(local_python_script).split('/')[-1])

    if not cluster_id:
        raise NotImplementedError('Not Cluster ID based install not yet implemented')

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


def run_local_py_script_as_task(db: DatabricksAPI,
                                task_definition: Union[str, ModuleType, Callable],
                                cluster_id: str = None,
                                run_name: str = None,
                                parameters: List[Any] = None):
    """
    # https://docs.databricks.com/dev-tools/api/latest/examples.html#jobs-api-examples
    A job consists of 1 or more tasks
    :param db:
    :param task_definition:
    :param cluster_id:
    :param run_name:
    :return:
    """

    task_definition = executable_as_script(task_definition)
    if not run_name:
        run_name = settings.db_run_name
    if not cluster_id:
        cluster_id = create_cluster(db)
    copy_from_local_to_hdfs(db=db, local_path=task_definition, dbfs_path=get_db_path(task_definition), )
    py_task = dict(python_file=get_db_path(task_definition), )
    if parameters:
        py_task['parameters'] = parameters

    run_id = db.jobs.submit_run(
        existing_cluster_id=cluster_id,
        spark_python_task=py_task,
        run_name=run_name,
        # new_cluster=None,
        # libraries=None,
        # notebook_task=None,
        # spark_jar_task=None,
        # spark_submit_task=None,
        # timeout_seconds=None,
        # tasks=None,
        # headers=None,
        # version=None,
    )['run_id']
    print(f'Stated task with run_id={run_id}')
    return run_id


def executable_as_script(py_executable: Union[str, ModuleType, Callable]):
    if isinstance(py_executable, str) and os.path.exists(py_executable):
        print(f'Detected Python Script for Databricks Submission')
        # Py file, we can just run this
        return py_executable
    if isinstance(py_executable, (str, ModuleType, Callable)):
        # Convert Module/Callable into a script
        return executable_to_str(py_executable)
    raise TypeError(f'Invalid Executable Python  Task {py_executable}')


def executable_to_str(executable_to_convert: Union[str, ModuleType, Callable]):
    # write a python code-string/module/function into a temp file and return resulting python file
    Path(settings.tmp_notebook_dir).mkdir(parents=True, exist_ok=True)
    from random import randrange
    if isinstance(executable_to_convert, str) and not os.path.exists(executable_to_convert):
        # Executable script
        file_name = f'{randrange(1333777)}tmp.py'

    else:
        # Module/Callable
        try:
            file_name = path_tail(inspect.getfile(executable_to_convert))
        except:
            # Within a Python shell, we cannot getFile(), so we have this fallback name
            file_name = f'{randrange(1333777)}tmp.py'

    out_path = f'{settings.tmp_notebook_dir}/{file_name}'

    if isinstance(executable_to_convert, str):
        print(f'Detected Python Code String')
        return str_to_file(executable_to_convert, out_path)

    if isinstance(executable_to_convert, Callable):
        print(f'Detected Python Function for Databricks Submission')
        return str_to_file(inspect.getsource(executable_to_convert) + f'\n{executable_to_convert.__name__}()', out_path)

    if isinstance(executable_to_convert, ModuleType):
        print(f'Detected Python Module for Databricks Submission')
        return str_to_file(inspect.getsource(executable_to_convert), out_path)


def checkon_db_task(db: DatabricksAPI, run_id: str = None, ):
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
        databricks_password: Optional[str] = None,
        databricks_email: Optional[str] = None,
):
    from johnsnowlabs.auto_install.databricks.install_utils import create_cluster, get_db_client_for_token
    db_client = get_db_client_for_token(databricks_host, databricks_token)
    return run_local_py_script_as_task(db_client, py_script_path, cluster_id=databricks_cluster_id, run_name=run_name)
