import re
import time
from pprint import pprint
from typing import List, Optional

from johnsnowlabs.auto_install import jsl_home
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.py_models.install_info import (
    InstallSuite,
    LocalPy4JLib,
    LocalPyLib,
    RootInfo,
)
from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.utils.env_utils import is_running_in_databricks_runtime
from .dbfs import *

# https://pypi.org/project/databricks-api/
from ...utils.enums import DatabricksClusterStates


def get_db_client_for_token(host, token) -> DatabricksAPI:
    # Get client via host or token
    return DatabricksAPI(host=host, token=token)


def get_db_client_for_password(host, email, password) -> DatabricksAPI:
    # Get client via user and password
    return DatabricksAPI(host=host, user=email, password=password)


def clean_cluster(
    databricks_host: str,
    databricks_token: str,
):
    dbfs_rm(
        get_db_client_for_token(databricks_host, databricks_token),
        settings.dbfs_home_dir,
        recursive=True,
    )


def install_license_to_cluster(install_suite: InstallSuite, db: DatabricksAPI, ):
    lic = {
        "SECRET": install_suite.secrets.HC_SECRET,
        "SPARK_OCR_SECRET": install_suite.secrets.OCR_SECRET,
        "SPARK_NLP_LICENSE": install_suite.secrets.HC_LICENSE,
        "SPARK_OCR_LICENSE": install_suite.secrets.OCR_LICENSE,
    }
    lic = {k: v for k, v in lic.items() if v is not None}
    # TODO license info-files and shit should be created! also folder!!
    put_file_on_dbfs(db, f'{settings.dbfs_license_path}/license.json', lic, overwrite=True)
    return settings.dbfs_license_path


def install_info_to_cluster(db: DatabricksAPI, ):
    info = RootInfo.get_from_jsl_home().dict()
    info["version"] = info["version"].as_str()
    put_file_on_dbfs(
        db,
        settings.dbfs_info_path,
        info,
        overwrite=True,
    )
    return settings.dbfs_info_path


def get_spark_conf(user_spark_conf):
    # Return merged user and default spark conf
    default_spark_conf = {
        "spark.kryoserializer.buffer.max": "2000M",
        "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
        "spark.sql.optimizer.expression.nestedPruning.enabled": "false",
        "spark.sql.optimizer.nestedSchemaPruning.enabled": "false",
        "spark.sql.legacy.allowUntypedScalaUDF": "true",
        "spark.sql.repl.eagerEval.enabled": "true",
    }

    if not user_spark_conf:
        spark_conf = default_spark_conf
    else:
        user_spark_conf.update(default_spark_conf)
        spark_conf = user_spark_conf
    return spark_conf


def get_spark_env_vars(user_spark_env_vars, install_suite: InstallSuite, databricks_host,
                       databricks_token,
                       visual, medical_nlp, write_db_credentials,
                       ):
    # Return merged user and default spark env vars
    default_spark_env_vars = dict(
        SPARK_NLP_LICENSE_FILE=f"/dbfs/johnsnowlabs/license.json",
        AWS_ACCESS_KEY_ID=install_suite.secrets.AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY=install_suite.secrets.AWS_SECRET_ACCESS_KEY,
    )

    if install_suite.secrets.OCR_SECRET and visual:
        default_spark_env_vars["VISUAL_SECRET"] = install_suite.secrets.OCR_SECRET
    if install_suite.secrets.HC_SECRET and medical_nlp:
        default_spark_env_vars["HEALTHCARE_SECRET"] = install_suite.secrets.HC_SECRET

    if write_db_credentials:
        default_spark_env_vars["DATABRICKS_HOST"] = databricks_host
        default_spark_env_vars["DATABRICKS_TOKEN"] = databricks_token
    # Env vars may not be None, so we drop any that are None
    default_spark_env_vars = {
        k: v for k, v in default_spark_env_vars.items() if v is not None
    }

    if not user_spark_env_vars:
        spark_env_vars = default_spark_env_vars
    else:
        user_spark_env_vars.update(default_spark_env_vars)
        spark_env_vars = user_spark_env_vars
    return spark_env_vars


def create_cluster(
    databricks_host: str,
    databricks_token: str,
    medical_nlp,
    spark_nlp,
    visual,
    install_suite: InstallSuite = None,
    num_workers=1,
    cluster_name=settings.db_cluster_name,
    node_type_id=settings.db_node_type_id,
    driver_node_type_id=settings.db_driver_node_type,
    spark_env_vars=None,
    autotermination_minutes=60,
    spark_version=settings.db_spark_version,
    spark_conf=None,
    auto_scale=None,
    aws_attributes=None,
    ssh_public_keys=None,
    custom_tags=None,
    cluster_log_conf=None,
    enable_elastic_disk=None,
    cluster_source=None,
    instance_pool_id=None,
    headers=None,
    block_till_cluster_ready: bool = True,
    write_db_credentials: bool = True,
    extra_pip_installs: Optional[List[str]] = None,
) -> str:
    db = get_db_client_for_token(databricks_host, databricks_token)

    if not install_suite:
        install_suite = jsl_home.get_install_suite_from_jsl_home()

    install_license_to_cluster(install_suite, db)
    install_info_to_cluster(db)

    spark_env_vars = get_spark_env_vars(spark_env_vars, install_suite, databricks_host,
                                        databricks_token,
                                        visual, medical_nlp, write_db_credentials)
    spark_conf = get_spark_conf(spark_conf)

    cluster_id = db.cluster.create_cluster(
        num_workers=num_workers,
        autoscale=auto_scale,
        cluster_name=cluster_name,
        spark_version=spark_version,
        spark_conf=spark_conf,
        aws_attributes=aws_attributes,
        node_type_id=node_type_id,
        driver_node_type_id=driver_node_type_id,
        ssh_public_keys=ssh_public_keys,
        custom_tags=custom_tags,
        cluster_log_conf=cluster_log_conf,
        spark_env_vars=spark_env_vars,
        autotermination_minutes=autotermination_minutes,
        enable_elastic_disk=enable_elastic_disk,
        cluster_source=cluster_source,
        instance_pool_id=instance_pool_id,
        headers=headers,
    )["cluster_id"]
    print(f"👌 Created cluster with id={cluster_id} on host={db.client.url}")
    install_jsl_suite_to_cluster(
        db=db,
        cluster_id=cluster_id,
        install_suite=install_suite,
        medical_nlp=medical_nlp,
        spark_nlp=spark_nlp,
        visual=visual,
    )

    if extra_pip_installs:
        install_list_of_pypi_ref_to_cluster(db, cluster_id, extra_pip_installs)

    if block_till_cluster_ready:
        block_till_cluster_ready_state(db, cluster_id)

    return cluster_id


def list_db_runtime_versions(db: DatabricksAPI):
    versions = db.cluster.list_spark_versions()
    # pprint(versions)
    for version in versions["versions"]:
        print(version["key"])
        name = version["name"]
        # version_regex = r'[0-9].[0-9].[0-9]'

        spark_version = re.findall(r"Apache Spark [0-9].[0-9]", version["name"])
        if spark_version:
            spark_version = spark_version[0].lstrip("Apache Spark ")
        scala_version = re.findall(r"Scala [0-9].[0-9][0-9]", version["name"])[
            0
        ].lstrip("Scala ")
        has_gpu = len(re.findall("GPU", version["name"])) > 0
        if spark_version:
            spark_version = spark_version + ".x"
        version = LibVersion(spark_version).as_str()
        print(
            f"name={name}\n"
            f"version={version}\n"
            f"has_gpu={has_gpu}\n"
            f"scala_version={scala_version}\n"
            f"spark_version={spark_version}\n"
            f"{'=' * 25}"
        )


def list_cluster_lib_status(db: DatabricksAPI, cluster_id: str):
    lib_statuses = db.managed_library.cluster_status(cluster_id=cluster_id)
    # lib_statuses = db.managed_library.all_cluster_statuses()
    pprint(lib_statuses)
    return lib_statuses


def list_node_types(db: DatabricksAPI):
    node_types = db.cluster.list_node_types(headers=None)
    pprint(node_types)


def install_list_of_pypi_ref_to_cluster(db: DatabricksAPI, cluster_id, pip_installs):
    # expects list of pypy references, either 'numpy' or 'numpy==1.2.3'
    for p in pip_installs:
        if "==" in p:
            package, version = p.split("==")
        else:
            package, version = p, None
        install_py_lib_via_pip(db, cluster_id, package, version)


def install_to_existing_cluster(
        databricks_host: str,
        databricks_token: str,
        databricks_cluster_id: str,
        install_suite: InstallSuite,
        medical_nlp,
        spark_nlp,
        visual,
        write_db_credentials: bool = True,
        extra_pip_installs: Optional[List[str]] = None,

):
    db = get_db_client_for_token(databricks_host, databricks_token)
    install_license_to_cluster(install_suite, db)
    install_info_to_cluster(db)

    cluster_info = db.cluster.get_cluster(databricks_cluster_id)
    if 'spark_conf' in cluster_info['spec']:
        spark_conf = cluster_info['spec']['spark_conf']
    else:
        spark_conf = None
    if 'spark_env_vars' in cluster_info['spec']:
        spark_env_vars = cluster_info['spec']['spark_env_vars']
    else:
        spark_env_vars = None


    spark_env_vars = get_spark_env_vars(spark_env_vars, install_suite, databricks_host,
                                        databricks_token,
                                        visual, medical_nlp, write_db_credentials)
    spark_conf = get_spark_conf(spark_conf)

    db.cluster.edit_cluster(cluster_id=databricks_cluster_id,
                            spark_conf=spark_conf,
                            spark_env_vars=spark_env_vars,
                            num_workers=cluster_info['spec']['num_workers'],
                            spark_version=cluster_info['spec']['spark_version'],
                            node_type_id=cluster_info['spec']['node_type_id'],
                            driver_node_type_id=cluster_info['spec']['driver_node_type_id'],
                            cluster_name=cluster_info['spec']['cluster_name'],
                            autotermination_minutes=cluster_info['autotermination_minutes'],
                            )

    install_jsl_suite_to_cluster(
        db=db,
        install_suite=install_suite,
        cluster_id=databricks_cluster_id,
        medical_nlp=medical_nlp,
        spark_nlp=spark_nlp,
        visual=visual,
    )

    if extra_pip_installs:
        install_list_of_pypi_ref_to_cluster(
            db=db,
            cluster_id=databricks_cluster_id,
            pip_installs=extra_pip_installs,
        )


def install_jsl_suite_to_cluster(
    db: DatabricksAPI,
    cluster_id: str,
    install_suite: InstallSuite,
    medical_nlp: bool,
    spark_nlp: bool,
    visual: bool,
):
    py_deps = [
        {"package": Software.nlu.pypi_name, "version": settings.raw_version_nlu},
        {
            "package": Software.sparknlp_display.pypi_name,
            "version": settings.raw_version_nlp_display,
        },
        {
            "package": Software.jsl_lib.pypi_name_databricks,
            "version": settings.raw_version_jsl_lib,
        },
    ]
    uninstall_old_libraries(db, cluster_id, py_deps)
    if (
        install_suite.hc.get_py_path()
        and install_suite.hc.get_java_path()
        and medical_nlp
    ):
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.hc)
        print(
            f"Installed {Software.spark_hc.logo + Software.spark_hc.name} Spark NLP for Healthcare ✅"
        )
    if install_suite.ocr.get_py_path() and install_suite.ocr.get_java_path() and visual:
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.ocr)
        print(
            f"Installed {Software.spark_ocr.logo + Software.spark_ocr.name} Spark OCR ✅"
        )

    for dep in py_deps:
        install_py_lib_via_pip(db, cluster_id, dep["package"], dep["version"])
    # TODO remove when NLU is compatible with pandas >=2
    install_py_lib_via_pip(db, cluster_id, "pandas", "1.5.3")

    # Install Sparkr-NLP as last library, so we have the correct version
    if (
        install_suite.nlp.get_py_path()
        and install_suite.nlp.get_java_path()
        and spark_nlp
    ):
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.nlp)
        print(
            f"{Software.spark_nlp.logo + Software.spark_nlp.name} Installed Spark NLP! ✅"
        )

    # On databricks environment should restart current cluster to apply uninstalls and installations
    if is_running_in_databricks_runtime():
        try:
            restart_cluster(db, cluster_id)
        except:
            pass


def block_till_cluster_ready_state(db: DatabricksAPI, cluster_id: str):
    status = None
    while status != DatabricksClusterStates.RUNNING:
        # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate
        status = DatabricksClusterStates(db.cluster.get_cluster(cluster_id)["state"])
        print(f"Cluster-Id={cluster_id} not ready, status={status.value}")
        time.sleep(10)

    print(f"👌 Cluster-Id {cluster_id} is ready!")


def uninstall_old_libraries(
    db: DatabricksAPI,
    cluster_id: str,
    pypi_deps: List[dict],
):
    """
    Tell Cluster to uninstall old libraries
    # https://docs.databricks.com/dev-tools/api/latest/libraries.html
    https://docs.databricks.com/dev-tools/api/latest/libraries.html#install
    :param db:
    :param cluster_id:
    :param pypi_deps:
    :return:
    """
    uninstalls = []
    statuses = db.managed_library.cluster_status(cluster_id=cluster_id)
    file_names = [
        "spark_nlp",
        "spark_nlp_jsl",
        "spark_ocr",
    ]
    pypi_packages = [d["package"] for d in pypi_deps]
    for status in statuses.get("library_statuses", []):
        installation_types = ["jar", "whl", "pypi"]
        for typ in installation_types:
            path = status["library"].get(typ)
            if path:
                if typ == "pypi":
                    pkg = path.get("package")
                    if pkg in pypi_packages:
                        uninstalls.append({typ: {"package": pkg}})
                else:
                    for fil in file_names:
                        path = path.replace("/dbfs/", "dbfs:/")
                        if fil in path.replace("-", "_"):
                            uninstalls.append({typ: path})
    if uninstalls:
        db.managed_library.uninstall_libraries(
            cluster_id=cluster_id, libraries=uninstalls
        )


def install_py_lib_via_pip(
    db: DatabricksAPI, cluster_id: str, pypi_lib: str, version: Optional[str] = None
):
    """
    Tell Cluster to install via public pypi
    # https://docs.databricks.com/dev-tools/api/latest/libraries.html
    https://docs.databricks.com/dev-tools/api/latest/libraries.html#install
    :param db:
    :param cluster_id:
    :param pypi_lib:
    :param version:
    :return:
    """
    # By not defining repo, we will use default pip index
    pypi = dict(package=pypi_lib)
    if version:
        pypi["version"] = version
    payload = [dict(pypi=pypi)]
    db.managed_library.install_libraries(cluster_id=cluster_id, libraries=payload)
    if version:
        print(f"Installed {pypi_lib}=={version} ✅")
    else:
        print(f"Installed {pypi_lib} ✅")


def install_py4j_lib_via_hdfs(db: DatabricksAPI, cluster_id: str, lib: LocalPy4JLib):
    """
    1. Copy lib files to HDFS if not present
    2. Tell Cluster to install
    https://docs.databricks.com/dev-tools/api/latest/libraries.html#install
    :param db:
    :param cluster_id:
    :param lib:
    :return:
    """
    copy_p4j_lib_to_hdfs_if_not_present(db, lib)
    payload = [
        dict(jar=get_db_path(lib.java_lib)),
        dict(
            whl=get_db_path(lib.py_lib),
        ),
    ]
    db.managed_library.install_libraries(cluster_id=cluster_id, libraries=payload)


def copy_p4j_lib_to_hdfs_if_not_present(db: DatabricksAPI, lib: LocalPy4JLib):
    if not is_lib_on_dbfs_cluster(db, lib.java_lib):
        copy_lib_to_dbfs_cluster(db, lib.java_lib)
    if not is_lib_on_dbfs_cluster(db, lib.py_lib):
        copy_lib_to_dbfs_cluster(db, lib.py_lib)


def copy_py_lib_to_hdfs_if_not_present(db: DatabricksAPI, lib: LocalPyLib):
    if not is_lib_on_dbfs_cluster(db, lib.py_lib):
        copy_lib_to_dbfs_cluster(db, lib.py_lib)


def is_lib_on_dbfs_cluster(
    db: DatabricksAPI, local_info: Union[JvmInstallInfo, PyInstallInfo]
):
    dbfs_path = get_db_path(local_info)
    return dbfs_file_exists(db, dbfs_path)


def copy_lib_to_dbfs_cluster(
    db: DatabricksAPI, local_info: Union[JvmInstallInfo, PyInstallInfo]
):
    dbfs_path = get_db_path(local_info)
    if isinstance(local_info, JvmInstallInfo):
        local_path = f"{settings.java_dir}/{local_info.file_name}"
    elif isinstance(local_info, PyInstallInfo):
        local_path = f"{settings.py_dir}/{local_info.file_name}"
    else:
        raise Exception(f"Invalid lib install type to copy {type(local_info)}")
    return copy_from_local_to_hdfs(db, local_path=local_path, dbfs_path=dbfs_path)


def wait_till_cluster_running(db: DatabricksAPI, cluster_id: str, timeout=900):
    # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate
    import time

    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print(
                "Timeout reached while waiting for the cluster to be running. Check cluster UI."
            )
            return False

        time.sleep(5)
        status = DatabricksClusterStates(db.cluster.get_cluster(cluster_id)["state"])

        if status == DatabricksClusterStates.RUNNING:
            return True
        elif status in [
            DatabricksClusterStates.PENDING,
            DatabricksClusterStates.RESIZING,
            DatabricksClusterStates.RESIZING,
        ]:
            continue
        elif status in [
            DatabricksClusterStates.TERMINATED,
            DatabricksClusterStates.TERMINATING,
            DatabricksClusterStates.ERROR,
            DatabricksClusterStates.UNKNOWN,
        ]:
            return False


def restart_cluster(db: DatabricksAPI, cluster_id: str):
    db.cluster.restart_cluster(cluster_id=cluster_id)


####
def list_clusters(db: DatabricksAPI):
    """Lists all clusters."""
    clusters = db.cluster.list_clusters()
    return clusters


def cluster_exist_with_name_and_runtime(
    db: DatabricksAPI, name: str, runtime: str
) -> bool:
    """Checks if a cluster with a specific name and runtime exists."""
    clusters = list_clusters(db)
    for cluster in clusters.get("clusters", []):
        if cluster["cluster_name"] == name and runtime in cluster["spark_version"]:
            return True
    return False


def does_cluster_exist_with_id(db: DatabricksAPI, cluster_id: str) -> bool:
    """Checks if a cluster with a specific ID exists."""
    try:
        cluster_info = db.cluster.get_cluster(cluster_id=cluster_id)
        if cluster_info and "cluster_id" in cluster_info:
            return True
    except Exception as e:
        # Handle specific exceptions based on the Databricks API error responses
        pass
    return False


def get_cluster_id(db: DatabricksAPI, cluster_name: str, runtime: str) -> str:
    """
    Retrieves the cluster ID based on the cluster name and runtime.

    If there are multiple candidates:
    - Returns any that's in the 'RUNNING' state if there is one.
    - If none are in the 'RUNNING' state, returns any.
    """
    clusters = list_clusters(db)
    running_clusters = []
    other_clusters = []

    for cluster in clusters.get("clusters", []):
        if (
            cluster["cluster_name"] == cluster_name
            and runtime in cluster["spark_version"]
        ):
            if cluster["state"] == "RUNNING":
                running_clusters.append(cluster["cluster_id"])
            else:
                other_clusters.append(cluster["cluster_id"])

    if running_clusters:
        return running_clusters[0]
    elif other_clusters:
        return other_clusters[0]
    else:
        raise Exception(
            f"No cluster found with name {cluster_name} and runtime {runtime}"
        )


def _get_cluster_id(db: DatabricksAPI, cluster_name: str) -> str:
    """
    Retrieves the cluster ID based on the cluster name.
    """
    clusters = list_clusters(db)
    running_clusters = []
    other_clusters = []

    for cluster in clusters.get("clusters", []):
        if cluster["cluster_name"] == cluster_name:
            # if cluster["state"] != "TERMINATED":
            other_clusters.append(cluster["cluster_id"])

    if running_clusters:
        return running_clusters[0]
    elif other_clusters:
        return other_clusters[0]
    else:
        return None  # Return None if no cluster found with the given name


#############
