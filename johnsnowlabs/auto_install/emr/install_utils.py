import time
from os import path
from typing import Optional

from johnsnowlabs import settings
from johnsnowlabs.auto_install.emr.enums import EMRClusterStates
from johnsnowlabs.auto_install.emr.work_utils import create_emr_bucket
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.boto_utils import BotoException
from johnsnowlabs.utils.enums import JvmHardwareTarget
from johnsnowlabs.utils.s3_utils import upload_content

here = path.abspath(path.dirname(__file__))


def create_emr_cluster(
    boto_session: "boto3.Session",
    secrets: JslSecrets,
    bootstrap_bucket: Optional[str] = None,
    s3_logs_path: Optional[str] = None,
    service_role: Optional[str] = settings.emr_default_service_role,
    job_flow_role: Optional[str] = settings.emr_default_instance_profile,
    subnet_id: Optional[str] = None,
    ec2_key_name: Optional[str] = None,
    spark_nlp: bool = True,
    nlp: bool = True,
    visual: bool = False,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
    block_till_cluster_ready: bool = True,
    auto_terminate_hours: Optional[int] = None,
) -> str:
    """
    Creates an EMR cluster with the given settings.
    :param boto_session: Boto3 session
    :param secrets: JSL secrets

    :param bootstrap_bucket: S3 bucket where the bootstrap script will be uploaded
    :param s3_logs_path: S3 path where logs will be stored
    :param service_role: EMR service role
    :param job_flow_role: EMR job flow role
    :param subnet_id: EMR subnet id
    :param ec2_key_name: EMR EC2 key name
    :param spark_nlp: If True, Spark NLP will be installed
    :param nlp: If True, Spark NLP for Healthcare will be installed
    :param visual: If True, Visual NLP will be installed
    :param hardware_platform: Hardware platform
    :param block_till_cluster_ready: If True, the function will block until the cluster is ready
    :param auto_terminate_hours : Idle hours to wait before terminating the cluster
    :return: EMR cluster id
    # Refer: https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html
    # Refer Also: https://docs.aws.amazon.com/code-library/latest/ug/python_3_emr_code_examples.html
    """

    import botocore

    try:
        if not boto_session:
            raise Exception("Boto session is required")

        region = boto_session.region_name
        emr_client = boto_session.client("emr")

        # Make sure EMR bucket exists
        bucket = create_emr_bucket(boto_session=boto_session, bucket=bootstrap_bucket)

        bootstrap_script_path = create_bootstrap_script(
            boto_session=boto_session,
            bucket=bucket,
            secrets=secrets,
            spark_nlp=spark_nlp,
            nlp=nlp,
            visual=visual,
            hardware_platform=hardware_platform,
        )

        step_script = create_initialization_step_script(
            boto_session=boto_session,
            bucket=bucket,
        )

        payload = {
            "Name": settings.emr_cluster_name,
            "ReleaseLabel": settings.emr_release_label,
            "VisibleToAllUsers": True,
            "Steps": [
                {
                    "Name": "Initialization step",
                    "ActionOnFailure": "CONTINUE",
                    "HadoopJarStep": {
                        "Jar": f"s3://{region}.elasticmapreduce/libs/script-runner/script-runner.jar",
                        "Args": [step_script],
                    },
                }
            ],
            "Configurations": [
                {
                    "Classification": "spark-env",
                    "Configurations": [
                        {
                            "Classification": "export",
                            "Properties": {
                                "SPARK_NLP_LICENSE": secrets.HC_LICENSE or "",
                                "PYSPARK_PYTHON": "/usr/bin/python3",
                                "JSL_EMR": "1",
                            },
                        }
                    ],
                    "Properties": {},
                },
                {
                    "Classification": "yarn-env",
                    "Configurations": [
                        {
                            "Classification": "export",
                            "Properties": {
                                "SPARK_NLP_LICENSE": secrets.HC_LICENSE or "",
                                "JSL_EMR": "1",
                            },
                        }
                    ],
                    "Properties": {},
                },
                {
                    "Classification": "spark-defaults",
                    "Properties": {
                        "spark.driver.maxResultSize": "0",
                        "spark.driver.memory": "32G",
                        "spark.kryoserializer.buffer.max": "2000M",
                        "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
                        "spark.yarn.preserve.staging.files": "true",
                        "spark.yarn.stagingDir": "hdfs:///tmp",
                        "spark.jsl.settings.aws.region": region,
                        "spark.yarn.appMasterEnv.SPARK_NLP_LICENSE": secrets.HC_LICENSE
                        or "",
                        "spark.executorEnv.SPARK_NLP_LICENSE": secrets.HC_LICENSE or "",
                    },
                },
            ],
            "Instances": {
                "MasterInstanceType": settings.emr_instance_type,
                "SlaveInstanceType": settings.emr_instance_type,
                "InstanceCount": settings.emr_instance_count,
                "KeepJobFlowAliveWhenNoSteps": True,
            },
            "Applications": [{"Name": app} for app in settings.emr_applications],
            "Tags": [
                {"Key": "for-use-with-amazon-emr-managed-policies", "Value": "true"}
            ],
            "EbsRootVolumeSize": settings.emr_volume_size,
            "ServiceRole": service_role or settings.emr_default_service_role,
            "JobFlowRole": job_flow_role or settings.emr_default_instance_profile,
            "BootstrapActions": [
                {
                    "Name": "jsl_bootstrap",
                    "ScriptBootstrapAction": {
                        "Path": bootstrap_script_path,
                    },
                }
            ],
        }
        if s3_logs_path:
            payload["LogUri"] = s3_logs_path
        if subnet_id:
            payload["Instances"]["Ec2SubnetId"] = subnet_id
        if ec2_key_name:
            payload["Instances"]["Ec2KeyName"] = ec2_key_name
        if auto_terminate_hours:
            payload["AutoTerminationPolicy"] = {
                "IdleTimeout": auto_terminate_hours * 60 * 60
            }

        try:
            response = emr_client.run_job_flow(
                **payload,
            )
            cluster_id = response["JobFlowId"]

            print(f"✅ Created EMR cluster with id={cluster_id}")
            if block_till_cluster_ready:
                block_till_emr_cluster_ready(
                    emr_client=emr_client, cluster_id=cluster_id
                )
            return cluster_id
        except botocore.exceptions.ClientError as e:
            raise BotoException(
                code=e.response["Error"]["Code"], message=e.response["Error"]["Message"]
            )
    except Exception as e:
        print("❌ Failed creating EMR cluster. Error: ", e)


def block_till_emr_cluster_ready(emr_client, cluster_id: str):
    status = None
    while status not in [EMRClusterStates.WAITING, EMRClusterStates.RUNNING]:
        response = emr_client.describe_cluster(ClusterId=cluster_id)
        status = EMRClusterStates(response["Cluster"]["Status"]["State"])
        if status in [EMRClusterStates.TERMINATED, EMRClusterStates.TERMINATING]:
            raise Exception("EMR cluster terminating or terminated")

        print(f"Cluster-Id={cluster_id} not ready, status={status.value}")
        time.sleep(30)

    print(f"👌 Cluster-Id {cluster_id} is ready!")


def create_initialization_step_script(
    boto_session: "boto3.Session", bucket: str
) -> str:
    """Creates a EMR initialization step script and uploads it to s3 bucket. Returns the s3 path of the script
    :param boto_session: Boto3 session
    :param s3_client: S3 boto3 client
    :param sts_client: STS boto3 client
    :param bucket: S3 bucket to upload the script
    :return s3_path: S3 path of the script
    """
    script_name = "initialization_script.sh"
    script = f"""#!/bin/bash
sudo usermod -a -G hdfsadmingroup livy
sudo usermod -a -G hdfsadmingroup hadoop
# Issue with EMR. See https://stackoverflow.com/questions/68406738/aws-emr-pandas-conflict-with-numpy-in-pyspark-after-bootstrapping
sudo python3 -m pip uninstall -y numpy
sudo python3 -m pip install "numpy>1.17.3"
sudo python3 -m pip install scipy scikit-learn "tensorflow==2.11.0" tensorflow-addons
exit 0
"""

    return upload_content(
        boto_session=boto_session,
        bucket=bucket,
        content=script,
        file_name=script_name,
    )


def create_bootstrap_script(
    boto_session: "boto3.Session",
    bucket: str,
    secrets: JslSecrets,
    spark_nlp: bool = True,
    nlp: bool = True,
    visual: bool = False,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
) -> str:
    """Creates a EMR bootstrap script and uploads it to s3 bucket. Returns the s3 path of the script
    :param boto_session: Boto3 session
    :param bucket: S3 bucket to upload the script
    :param secrets: JSL secrets
    :param spark_nlp: Whether to install spark-nlp
    :param nlp: Whether to install nlp
    :param visual: Whether to install visual
    :return s3_path: S3 path of the script
    """

    script_name = "jsl_emr_bootstrap.sh"
    full_installation_script = f"""#!/bin/bash
set -x -e

echo -e 'export PYSPARK_PYTHON=/usr/bin/python3 
export JSL_EMR=1
export HADOOP_CONF_DIR=/etc/hadoop/conf 
export SPARK_JARS_DIR=/usr/lib/spark/jars 
export SPARK_HOME=/usr/lib/spark' >> $HOME/.bashrc && source $HOME/.bashrc

sudo python3 -m pip install 'urllib3<2.0'
sudo python3 -m pip install {Software.jsl_lib.pypi_name}=={settings.raw_version_jsl_lib}

__installation_script__
sudo bash -c "mkdir -p /usr/lib/spark/jars; cp /lib/.johnsnowlabs/johnsnowlabs/java_installs/*.jar /usr/lib/spark/jars/"
# Make sure pyspark is removed as EMR installs it by default
sudo python3 -m pip uninstall -y pyspark

set +x
exit 0

"""
    installation_script = ""
    if secrets.HC_LICENSE:
        installation_script += f"sudo -E python3 -c \"from johnsnowlabs import nlp;nlp.install(med_license='{secrets.HC_LICENSE or ''}',aws_key_id='{secrets.AWS_ACCESS_KEY_ID or ''}',aws_access_key='{secrets.AWS_SECRET_ACCESS_KEY or ''}', spark_nlp={spark_nlp}, nlp={nlp}, visual={visual}, hardware_platform='{hardware_platform}')\""
    else:
        installation_script += f"sudo -E python3 -c \"from johnsnowlabs import nlp;nlp.install(browser_login=False, nlp=False, hardware_platform='{hardware_platform}')\""

    full_installation_script = full_installation_script.replace(
        "__installation_script__", installation_script
    )

    return upload_content(
        boto_session=boto_session,
        bucket=bucket,
        content=full_installation_script,
        file_name=script_name,
    )
