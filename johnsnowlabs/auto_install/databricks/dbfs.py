# https://pypi.org/project/databricks-api/
import base64
import json
from os.path import dirname
from typing import Union

from databricks_api import DatabricksAPI

from johnsnowlabs import settings
from johnsnowlabs.py_models.install_info import JvmInstallInfo, PyInstallInfo
from johnsnowlabs.utils.file_utils import path_tail


def dbfs_file_exists(db: DatabricksAPI, path: str):
    try:
        dbfs_ls(db, path)
        return True
    except:
        return False


def dbfs_ls(db: DatabricksAPI, dbfs_path: str):
    return db.dbfs.list(dbfs_path)


def dbfs_rm(
    db: DatabricksAPI,
    dbfs_path: str,
    recursive: bool = False,
):
    print("🧹 Cleaning up old JSL home in ", dbfs_path)
    return db.dbfs.delete(dbfs_path, recursive=recursive)


def copy_from_local_to_hdfs(
    db: DatabricksAPI, local_path: str, dbfs_path: str, overwrite: bool = True
):
    print(f"Copying {local_path} to remote cluster path {dbfs_path}")
    db.dbfs.put(
        path=dbfs_path,
        overwrite=overwrite,
        # contents=None,
        src_path=local_path,
    )


def put_file_on_dbfs(
    db: DatabricksAPI, path: str, content: any, overwrite: bool = True
):
    try:
        directory = dirname(path)
        db.dbfs.mkdirs(directory)
    except:
        pass
    if type(content) != "string":
        content = json.dumps(content)
    content = base64.b64encode(content.encode()).decode()
    db.dbfs.put(path=path, overwrite=overwrite, contents=content)


def get_db_path(local_info: Union[JvmInstallInfo, PyInstallInfo, str]):
    """Get a deterministic path for a JvmInstallInfo or PyInstallInfo or local files on dbfs.
    Always use this method to generate output file path for dbfs.
    """
    if isinstance(local_info, JvmInstallInfo):
        return f"{settings.dbfs_java_dir}/{local_info.file_name}"
    elif isinstance(local_info, PyInstallInfo):
        # Gotta add the suffix or databricks will not pickup the correct version
        return f'{settings.dbfs_py_dir}/{local_info.file_name.split(".")[0]}-py2.py3-none-any.whl'
    elif isinstance(local_info, str):
        if ".py" in local_info:
            return f"{settings.db_py_jobs_dir}/{path_tail(local_info)}"
        elif ".jar" in local_info:
            return f"{settings.db_jar_jobs_dir}/{path_tail(local_info)}"
        elif ".ipynb" in local_info:
            return f"{settings.db_py_notebook_dir}/{path_tail(local_info)}"
        else:
            raise Exception(
                f"Invalid Job file, file name must contain either .py .jar or .ipynb"
                f"But got {local_info}"
            )
    else:
        raise Exception(f"Invalid install type = {type(local_info)}")
