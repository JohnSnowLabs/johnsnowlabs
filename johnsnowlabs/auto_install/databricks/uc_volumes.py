from typing import Optional, Union

import requests
from databricks_api import DatabricksAPI

from johnsnowlabs import settings
from johnsnowlabs.auto_install.databricks.dbfs import get_db_path
from johnsnowlabs.py_models.install_info import (
    JvmInstallInfo,
    LocalPy4JLib,
    PyInstallInfo,
)
from johnsnowlabs.utils.file_utils import path_tail

# DBFS library installs are rejected from this runtime on, Unity Catalog volumes replace them
FIRST_DBR_WITHOUT_DBFS_LIBRARIES = 15


def is_volume_path(path: Optional[str]) -> bool:
    return bool(path) and path.startswith("/Volumes/")


def dbr_major_of_cluster(db: DatabricksAPI, cluster_id: str) -> Optional[int]:
    try:
        runtime = db.cluster.get_cluster(cluster_id)["spark_version"]
        return int(runtime.split(".")[0])
    except Exception as err:
        print(f"Warning: could not read the runtime of cluster {cluster_id}: {err}")
        return None


def get_volume_lib_path(
    local_info: Union[JvmInstallInfo, PyInstallInfo], volume_dir: str
) -> str:
    sub_dir = "java_installs" if isinstance(local_info, JvmInstallInfo) else "py_installs"
    return f"{volume_dir.rstrip('/')}/{sub_dir}/{path_tail(get_db_path(local_info))}"


def _files_api_url(db: DatabricksAPI, volume_path: str) -> str:
    return db.client.get_url(f"/fs/files{volume_path}")


def _auth_headers(db: DatabricksAPI) -> dict:
    return {"Authorization": db.client.default_headers["Authorization"]}


def volume_file_exists(db: DatabricksAPI, volume_path: str) -> bool:
    try:
        response = requests.head(
            _files_api_url(db, volume_path), headers=_auth_headers(db), timeout=60
        )
        return response.status_code == 200
    except Exception:
        return False


def copy_local_to_volume(db: DatabricksAPI, local_path: str, volume_path: str) -> None:
    print(f"Copying {local_path} to remote cluster path {volume_path}")
    headers = {**_auth_headers(db), "Content-Type": "application/octet-stream"}
    with open(local_path, "rb") as file_handle:
        response = requests.put(
            _files_api_url(db, volume_path),
            headers=headers,
            params={"overwrite": "true"},
            data=file_handle,
            timeout=3600,
        )
    if response.status_code not in (200, 204):
        raise Exception(
            f"Could not upload {local_path} to {volume_path}, "
            f"status={response.status_code} {response.text[:300]}"
        )


def copy_lib_to_volume_if_not_present(
    db: DatabricksAPI,
    local_info: Union[JvmInstallInfo, PyInstallInfo],
    volume_dir: str,
) -> str:
    volume_path = get_volume_lib_path(local_info, volume_dir)
    if volume_file_exists(db, volume_path):
        return volume_path
    if isinstance(local_info, JvmInstallInfo):
        local_path = f"{settings.java_dir}/{local_info.file_name}"
    else:
        local_path = f"{settings.py_dir}/{local_info.file_name}"
    copy_local_to_volume(db, local_path, volume_path)
    return volume_path


def install_py4j_lib_via_volume(
    db: DatabricksAPI, cluster_id: str, lib: LocalPy4JLib, volume_dir: str
) -> None:
    jar_path = copy_lib_to_volume_if_not_present(db, lib.java_lib, volume_dir)
    py_path = copy_lib_to_volume_if_not_present(db, lib.py_lib, volume_dir)
    payload = [dict(jar=jar_path), dict(whl=py_path)]
    db.managed_library.install_libraries(cluster_id=cluster_id, libraries=payload)
