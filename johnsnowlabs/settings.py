import os
from os.path import expanduser
from johnsnowlabs.utils.env_utils import (
    is_running_in_databricks,
    set_py4j_logger_to_error_on_databricks,
    env_required_license,
)

# These versions are used for auto-installs and version  checks
raw_version_jsl_lib = "5.0.7"
raw_version_nlp = "5.0.2"

raw_version_nlu = "5.0.0"

raw_version_pyspark = "3.1.2"
raw_version_nlp_display = "4.1"

raw_version_medical = "5.0.2"
raw_version_secret_medical = "5.0.2"

raw_version_secret_ocr = "5.0.0"
raw_version_ocr = "5.0.0"

raw_version_pydantic = "1.10.11"

pypi_page = "https://pypi.org/project/johnsnowlabs"
json_indent = 4
enforce_secret_on_version = False
enforce_versions = True

# Environment
on_databricks = is_running_in_databricks()
license_required = env_required_license()

# Set root path, from which all other paths will be relative

if on_databricks:
    root_dir = f"/dbfs/johnsnowlabs"
    set_py4j_logger_to_error_on_databricks()
else:
    home = expanduser("~")
    if home[-1] == "/":
        # on Docker and other setups, ~ may resolve to `/`, so we need special handling here
        root_dir = f'{expanduser("~")}.johnsnowlabs'
    else:
        root_dir = f'{expanduser("~")}/.johnsnowlabs'

## Directories
license_dir = os.path.join(root_dir, "licenses")
java_dir = os.path.join(root_dir, "java_installs")
py_dir = os.path.join(root_dir, "py_installs")

# Info Files
root_info_file = os.path.join(root_dir, "info.json")
java_info_file = os.path.join(java_dir, "info.json")
py_info_file = os.path.join(py_dir, "info.json")
creds_info_file = os.path.join(license_dir, "info.json")

# databricks paths
dbfs_home_dir = "dbfs:/johnsnowlabs"
dbfs_java_dir = f"{dbfs_home_dir}/java_installs"
dbfs_py_dir = f"{dbfs_home_dir}/py_installs"
db_py_jobs_dir = f"{dbfs_home_dir}/py_jobs"
db_py_notebook_dir = f"{dbfs_home_dir}/py_notebook_jobs"
db_jar_jobs_dir = f"{dbfs_home_dir}/jar_jobs"

db_cluster_name = "John-Snow-Labs-Databricks-Auto-Cluster🚀"
db_driver_node_type = "i3.xlarge"
db_node_type_id = "i3.xlarge"
db_spark_version = "10.5.x-scala2.12"

# db_spark_version = "13.2.x-scala2.12"

db_job_name = "John-Snow-Labs-Job {job} 🚀"
db_run_name = "John-Snow-Labs-Run 🚀"

# Local Spark mode


spark_session_name = "John-Snow-Labs-Spark-Session 🚀"
