import time
from pprint import pprint
import re
from johnsnowlabs.auto_install.softwares import Software

from johnsnowlabs.py_models.install_info import InstallSuite, LocalPy4JLib, LocalPyLib
from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.auto_install import jsl_home
from .dbfs import *

# https://pypi.org/project/databricks-api/
from ...utils.enums import DatabricksClusterStates


def get_db_client_for_token(host, token) -> DatabricksAPI:
    # Get client via host or token
    return DatabricksAPI(host=host, token=token)


def get_db_client_for_password(host, email, password) -> DatabricksAPI:
    # Get client via user and password
    return DatabricksAPI(host=host, user=email, password=password)


def create_cluster(
        db: DatabricksAPI,
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

) -> str:
    if not install_suite:
        install_suite = jsl_home.get_install_suite_from_jsl_home()

    default_spark_conf = {
        'spark.kryoserializer.buffer.max': '2000M',
        'spark.serializer': 'org.apache.spark.serializer.KryoSerializer',
    }
    default_spark_env_vars = dict(
        SPARK_NLP_LICENSE=install_suite.secrets.HC_LICENSE,
        SPARK_OCR_LICENSE=install_suite.secrets.OCR_LICENSE,
        AWS_ACCESS_KEY_ID=install_suite.secrets.AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY=install_suite.secrets.AWS_SECRET_ACCESS_KEY,
    )

    if not spark_conf:
        spark_conf = default_spark_conf
    else:
        spark_conf.update(default_spark_conf)

    if not spark_env_vars:
        spark_env_vars = default_spark_env_vars
    else:
        spark_env_vars.update(default_spark_env_vars)

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
    )['cluster_id']
    print(f'👌 Created cluster with id={cluster_id} on host={db.client.url}')
    install_jsl_suite_to_cluster(db=db, cluster_id=cluster_id, install_suite=install_suite)
    if block_till_cluster_ready:
        block_till_cluster_ready_state(db, cluster_id)

    return cluster_id


def list_db_runtime_versions(db: DatabricksAPI):
    versions = db.cluster.list_spark_versions()
    # pprint(versions)
    for version in versions['versions']:
        print(version['key'])
        print(version['name'])
        # version_regex = r'[0-9].[0-9].[0-9]'

        spark_version = re.findall(r'Apache Spark [0-9].[0-9]', version['name'])[0].lstrip('Apache Spark ')
        scala_version = re.findall(r'Scala [0-9].[0-9][0-9]', version['name'])[0].lstrip('Scala ')
        has_gpu = len(re.findall('GPU', version['name'])) > 0
        spark_version = spark_version + '.x'
        print(LibVersion(spark_version).as_str(), has_gpu, scala_version)


def list_clusters(db: DatabricksAPI):
    clusters = db.cluster.list_clusters(headers=None)
    pprint(clusters)
    print(clusters)
    return clusters


def list_cluster_lib_status(db: DatabricksAPI, cluster_id: str):
    lib_statuses = db.managed_library.cluster_status(cluster_id=cluster_id)
    # lib_statuses = db.managed_library.all_cluster_statuses()
    pprint(lib_statuses)
    return lib_statuses


def list_node_types(db: DatabricksAPI):
    node_types = db.cluster.list_node_types(headers=None)
    pprint(node_types)


def install_jsl_suite_to_cluster(
        db: DatabricksAPI,
        cluster_id: str,
        install_suite: InstallSuite,
        install_optional: bool = True,
):
    if install_suite.hc.get_py_path() and install_suite.hc.get_java_path():
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.hc)
        print(f'Installed {Software.spark_hc.logo + Software.spark_hc.name} Spark NLP for Healthcare ✅')
    if install_suite.ocr.get_py_path() and install_suite.ocr.get_java_path():
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.ocr)
        print(f'Installed {Software.spark_ocr.logo + Software.spark_ocr.name} Spark OCR ✅')
    py_deps = [Software.nlu.pypi_name, Software.sparknlp_display.pypi_name, Software.jsl_lib.pypi_name_databricks]
    for dep in py_deps:
        install_py_lib_via_pip(db, cluster_id, dep)

    # Install Sparkr-NLP as last library, so we have the correct version
    if install_suite.nlp.get_py_path() and install_suite.nlp.get_java_path():
        install_py4j_lib_via_hdfs(db, cluster_id, install_suite.nlp)
        print(f'{Software.spark_nlp.logo + Software.spark_nlp.name} Installed Spark NLP! ✅')


def block_till_cluster_ready_state(db: DatabricksAPI, cluster_id: str):
    status = None
    while status != DatabricksClusterStates.RUNNING:
        # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate
        status = DatabricksClusterStates(db.cluster.get_cluster(cluster_id)['state'])
        print(f'Cluster-Id={cluster_id} not ready, status={status.value}')
        time.sleep(10)

    print(f'👌 Cluster-Id {cluster_id} is ready!')


def install_py_lib_via_pip(db: DatabricksAPI, cluster_id: str, pypi_lib: str):
    """
    Tell Cluster to install via public pypi
    # https://docs.databricks.com/dev-tools/api/latest/libraries.html
    https://docs.databricks.com/dev-tools/api/latest/libraries.html#install
    :param db:
    :param cluster_id:
    :param lib:
    :return:
    """
    # By not defining repo, we will use default pip index
    payload = [dict(pypi=dict(package=pypi_lib))]
    db.managed_library.install_libraries(cluster_id=cluster_id, libraries=payload)
    print(f'Installed {pypi_lib} ✅')


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
    payload = [dict(jar=get_db_path(lib.java_lib)),
               dict(whl=get_db_path(lib.py_lib), )]
    db.managed_library.install_libraries(cluster_id=cluster_id, libraries=payload)


def copy_p4j_lib_to_hdfs_if_not_present(db: DatabricksAPI, lib: LocalPy4JLib):
    if not is_lib_on_dbfs_cluster(db, lib.java_lib):
        copy_lib_to_dbfs_cluster(db, lib.java_lib)
    if not is_lib_on_dbfs_cluster(db, lib.py_lib):
        copy_lib_to_dbfs_cluster(db, lib.py_lib)


def copy_py_lib_to_hdfs_if_not_present(db: DatabricksAPI, lib: LocalPyLib):
    if not is_lib_on_dbfs_cluster(db, lib.py_lib):
        copy_lib_to_dbfs_cluster(db, lib.py_lib)


def is_lib_on_dbfs_cluster(db: DatabricksAPI, local_info: Union[JvmInstallInfo, PyInstallInfo]):
    dbfs_path = get_db_path(local_info)
    return dbfs_file_exists(db, dbfs_path)


def copy_lib_to_dbfs_cluster(db: DatabricksAPI, local_info: Union[JvmInstallInfo, PyInstallInfo]):
    dbfs_path = get_db_path(local_info)
    if isinstance(local_info, JvmInstallInfo):
        local_path = f'{settings.java_dir}/{local_info.file_name}'
    elif isinstance(local_info, PyInstallInfo):
        local_path = f'{settings.py_dir}/{local_info.file_name}'
    else:
        raise Exception(f'Invalid lib install type to copy {type(local_info)}')
    return copy_from_local_to_hdfs(db, local_path=local_path, dbfs_path=dbfs_path)



def wait_till_cluster_running(db: DatabricksAPI, cluster_id: str):
    # https://docs.databricks.com/dev-tools/api/latest/clusters.html#clusterclusterstate
    import time
    while 1:
        time.sleep(5)
        status = DatabricksClusterStates(db.cluster.get_cluster(cluster_id)['state'])
        if status == DatabricksClusterStates.RUNNING:
            return True
        elif status in [DatabricksClusterStates.PENDING, DatabricksClusterStates.RESIZING,
                        DatabricksClusterStates.RESIZING]:
            continue
        elif status in [DatabricksClusterStates.TERMINATED, DatabricksClusterStates.TERMINATING,
                        DatabricksClusterStates.ERROR,
                        DatabricksClusterStates.UNKNOWN]:
            return False
