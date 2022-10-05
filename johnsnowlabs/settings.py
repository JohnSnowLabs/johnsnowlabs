from os.path import expanduser

# libs, these versions are used for auto-installs and version  checks
raw_version_jsl_lib = '1.0.0'
raw_version_nlp = '4.2.0'
raw_version_medical = '4.2.0'
raw_version_secret_medical = '4.2.0'
raw_version_secret_ocr = '4.1.0'

raw_version_ocr = '4.1.0'
raw_version_nlu = '4.0.1rc4'
raw_version_pyspark = '3.1.2'
raw_version_nlp_display = '4.1'
pypi_page = 'https://pypi.org/project/johnsnowlabs'



json_indent = 4
enforce_secret_on_version = False
enforce_versions = True

# Local paths for jsl home

## Directories
def databricks_env(): pass


if databricks_env():
    root_dir = f'/dbfs/johnsnowlabs'
else:
    root_dir = f'{expanduser("~")}/.johnsnowlabs'
license_dir = f'{root_dir}/licenses'
java_dir = f'{root_dir}/java_installs'
py_dir = f'{root_dir}/py_installs'

# Info Files
root_info_file = f'{root_dir}/info.json'
java_info_file = f'{java_dir}/info.json'
py_info_file = f'{py_dir}/info.json'
creds_info_file = f'{license_dir}/info.json'

# databricks paths
dbfs_home_dir = 'dbfs:/johnsnowlabs'
dbfs_java_dir = f'{dbfs_home_dir}/java_installs'
dbfs_py_dir = f'{dbfs_home_dir}/py_installs'
db_py_jobs_dir = f'{dbfs_home_dir}/py_jobs'
db_py_notebook_dir = f'{dbfs_home_dir}/py_notebook_jobs'
db_jar_jobs_dir = f'{dbfs_home_dir}/jar_jobs'

db_cluster_name = 'John-Snow-Labs-Databricks-Auto-Cluster🚀'
db_job_name = 'John-Snow-Labs-Job {job} 🚀'
db_run_name = 'John-Snow-Labs-Run 🚀'

# Local Spark mode
spark_session_name = 'John-Snow-Labs-Spark-Session 🚀'

#### Testing
success_worker_print = '$$JSL_TESTING_WORKER_SUC$$'
testing_dir = f'{root_dir}/tmp_tests'
tmp_notebook_dir = f'{testing_dir}/notebook_tests'
tmp_py_script_dir = f'{testing_dir}/notebook_tests'
tmp_markdown_dir = f'{testing_dir}/markdown_tests'

workshop_git = 'https://github.com/JohnSnowLabs/spark-nlp-workshop.git'
workshop_local_folder = f'{tmp_notebook_dir}/spark-nlp-workshop'
workshop_cert_nb_folder = f'{workshop_local_folder}/tutorials/Certification_Trainings'
workshop_fin_folder = f'{workshop_cert_nb_folder}/Finance'
workshop_leg_folder = f'{workshop_cert_nb_folder}/Healthcare'
workshop_med_folder = f'{workshop_cert_nb_folder}/Legal'
workshop_pub_folder = f'{workshop_cert_nb_folder}/Public'

