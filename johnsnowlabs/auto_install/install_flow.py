import os.path
import shutil
import sys
from typing import Optional, List


from johnsnowlabs import settings
from johnsnowlabs.auto_install.databricks.dbfs import dbfs_rm
from johnsnowlabs.auto_install.databricks.install_utils import (
    create_cluster,
    get_db_client_for_token,
    install_jsl_suite_to_cluster,
    install_list_of_pypi_ref_to_cluster,
)
from johnsnowlabs.auto_install.emr.install_utils import create_emr_cluster
from johnsnowlabs.auto_install.glue.install_utils import (
    create_glue_bucket,
    upload_pylibs_jars_to_glue_bucket,
)
from johnsnowlabs.auto_install.glue.utils import get_printable_glue_notebook_commands
from johnsnowlabs.auto_install.install_software import check_and_install_dependencies
from johnsnowlabs.auto_install.jsl_home import (
    get_install_suite_from_jsl_home,
    setup_jsl_home,
)
from johnsnowlabs.auto_install.offline_install import get_printable_dependency_urls
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.enums import JvmHardwareTarget, ProductName, PyInstallTypes


def install(
        # -- JSL-Auth Flows --
        # Browser Auth
        browser_login: bool = True,
        force_browser: bool = False,
        # JWT Token Auth
        access_token: Optional[str] = None,
        # JSON file Auth
        json_license_path: Optional[str] = None,
        # Manual License specification Auth
        med_license: Optional[str] = None,
        enterprise_nlp_secret: Optional[str] = None,
        ocr_secret: Optional[str] = None,
        ocr_license: Optional[str] = None,
        fin_license: Optional[str] = None,
        leg_license: Optional[str] = None,
        aws_access_key: Optional[str] = None,
        aws_key_id: Optional[str] = None,
        # -- Databricks auth flows & Install Target --
        databricks_cluster_id: Optional[str] = None,
        databricks_token: Optional[str] = None,
        databricks_host: Optional[str] = None,
        # -- Install Params --
        # Install Target
        python_exec_path: str = sys.executable,
        venv_creation_path: Optional[str] = None,
        offline_zip_dir: Optional[str] = None,
        # Download Params
        offline: bool = False,
        install_optional: bool = True,
        install_licensed: bool = True,
        slim_install: bool = False,  # Only Downloads jars
        product: Optional[str] = ProductName.jsl_full.value,
        include_dependencies: bool = True,
        nlp: bool = True,
        spark_nlp: bool = True,
        visual: bool = False,
        # License usage & Caching
        local_license_number: int = 0,
        remote_license_number: int = 0,
        store_in_jsl_home: bool = True,
        # Install File Types
        hardware_platform: str = JvmHardwareTarget.cpu.value,
        py_install_type: str = PyInstallTypes.wheel.value,
        only_refresh_credentials: bool = False,
        refresh_install: bool = False,
        # -- Databricks Cluster Creation Params --
        block_till_cluster_ready=True,
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
        clean_cluster=True,
        write_db_credentials=True,
        extra_pip_installs: Optional[List[str]] = None,
):
    if refresh_install and os.path.exists(settings.root_dir):
        print("🧹 Cleaning up old JSL Home in ", settings.root_dir)
        shutil.rmtree(settings.root_dir)
    if clean_cluster and databricks_host:
        dbfs_rm(
            get_db_client_for_token(databricks_host, databricks_token),
            settings.dbfs_home_dir,
            recursive=True,
        )

    # Input Validation
    py_install_type = PyInstallTypes.from_str(py_install_type)
    hardware_platform = JvmHardwareTarget.from_str(hardware_platform)
    product = Software.for_name(product)

    # Get Credentials from Auth Flow
    secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(
        browser_login=browser_login,
        force_browser=force_browser,
        access_token=access_token,
        local_license_number=local_license_number,
        remote_license_number=remote_license_number,
        secrets_file=json_license_path,
        hc_license=med_license,
        hc_secret=enterprise_nlp_secret,
        ocr_secret=ocr_secret,
        ocr_license=ocr_license,
        aws_access_key=aws_access_key,
        aws_key_id=aws_key_id,
        return_empty_secrets_if_none_found=True,
        fin_license=fin_license,
        leg_license=leg_license,
        store_in_jsl_home=store_in_jsl_home,
    )
    if only_refresh_credentials:
        return

    if offline:
        # Offline Install
        get_printable_dependency_urls(
            secrets=secrets,
            jvm_install_type=hardware_platform,
            py_install_type=py_install_type,
        )
        if not offline_zip_dir:
            return

    if store_in_jsl_home and not offline:
        # Cache credentials, Wheels and Jars in ~/.johnsnowlabs
        setup_jsl_home(
            secrets=secrets,
            jvm_install_type=hardware_platform,
            py_install_type=py_install_type,
            refresh_install=refresh_install,
            visual=visual,
            nlp=nlp,
            spark_nlp=spark_nlp,
        )

    # Databricks Install
    if databricks_host and databricks_token and not offline:
        print(
            "nlp.install() for databricks will be deprecated next release, instead use nlp.install_to_databricks()"
        )
        suite = get_install_suite_from_jsl_home(
            jvm_hardware_target=hardware_platform,
            visual=visual,
            nlp=nlp,
            spark_nlp=spark_nlp,
        )
        if databricks_cluster_id:
            install_jsl_suite_to_cluster(
                db=get_db_client_for_token(databricks_host, databricks_token),
                install_suite=suite,
                cluster_id=databricks_cluster_id,
                medical_nlp=nlp,
                spark_nlp=spark_nlp,
                visual=visual,
            )
            if extra_pip_installs:
                install_list_of_pypi_ref_to_cluster(
                    db=get_db_client_for_token(databricks_host, databricks_token),
                    cluster_id=databricks_cluster_id,
                    pip_installs=extra_pip_installs,
                )

        else:
            return create_cluster(
                medical_nlp=nlp,
                spark_nlp=spark_nlp,
                visual=visual,
                databricks_host=databricks_host,
                databricks_token=databricks_token,
                install_suite=suite,
                block_till_cluster_ready=block_till_cluster_ready,
                num_workers=num_workers,
                cluster_name=cluster_name,
                node_type_id=node_type_id,
                driver_node_type_id=driver_node_type_id,
                spark_env_vars=spark_env_vars,
                autotermination_minutes=autotermination_minutes,
                spark_version=spark_version,
                spark_conf=spark_conf,
                auto_scale=auto_scale,
                aws_attributes=aws_attributes,
                ssh_public_keys=ssh_public_keys,
                custom_tags=custom_tags,
                cluster_log_conf=cluster_log_conf,
                enable_elastic_disk=enable_elastic_disk,
                cluster_source=cluster_source,
                instance_pool_id=instance_pool_id,
                headers=headers,
                write_db_credentials=write_db_credentials,
                extra_pip_installs=extra_pip_installs,
            )

    # Local Py-Install
    elif not slim_install:
        check_and_install_dependencies(
            product=product,
            secrets=secrets,
            install_optional=install_optional,
            install_licensed=install_licensed,
            python_exec_path=python_exec_path,
            py_setup_dir=venv_creation_path,
            offline_zip_dir=offline_zip_dir,
            include_dependencies=include_dependencies,
            visual=visual,
            spark_nlp=spark_nlp,
            enterpise_nlp=nlp,
        )


def install_to_databricks(
    # -- JSL-Auth Flows --
    # Browser Auth
    browser_login: bool = True,
    force_browser: bool = False,
    # JWT Token Auth
    access_token: Optional[str] = None,
    # JSON file Auth
    json_license_path: Optional[str] = None,
    # Manual License specification Auth
    med_license: Optional[str] = None,
    enterprise_nlp_secret: Optional[str] = None,
    ocr_secret: Optional[str] = None,
    ocr_license: Optional[str] = None,
    fin_license: Optional[str] = None,
    leg_license: Optional[str] = None,
    aws_access_key: Optional[str] = None,
    aws_key_id: Optional[str] = None,
    # -- Databricks auth flows & Install Target --
    databricks_cluster_id: Optional[str] = None,
    databricks_token: Optional[str] = None,
    databricks_host: Optional[str] = None,
    databricks_password: Optional[str] = None,
    databricks_email: Optional[str] = None,
    # -- Install Params --
    product: Optional[str] = ProductName.jsl_full.value,
    nlp: bool = True,
    spark_nlp: bool = True,
    visual: bool = False,
    # License usage & Caching
    local_license_number: int = 0,
    remote_license_number: int = 0,
    store_in_jsl_home: bool = True,
    # Install File Types
    hardware_platform: str = JvmHardwareTarget.cpu.value,
    py_install_type: str = PyInstallTypes.wheel.value,
    refresh_install: bool = False,
    # -- Databricks Cluster Creation Params --
    block_till_cluster_ready=True,
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
    clean_cluster=True,
    write_db_credentials=True,
    extra_pip_installs: Optional[List[str]] = None,
):
    if refresh_install and os.path.exists(settings.root_dir):
        print("🧹 Cleaning up old JSL Home in ", settings.root_dir)
        shutil.rmtree(settings.root_dir)
    if clean_cluster and databricks_host:
        dbfs_rm(
            get_db_client_for_token(databricks_host, databricks_token),
            settings.dbfs_home_dir,
            recursive=True,
        )

    # Input Validation
    py_install_type = PyInstallTypes.from_str(py_install_type)
    hardware_platform = JvmHardwareTarget.from_str(hardware_platform)
    product = Software.for_name(product)

    # Get Credentials from Auth Flow
    secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(
        browser_login=browser_login,
        force_browser=force_browser,
        access_token=access_token,
        local_license_number=local_license_number,
        remote_license_number=remote_license_number,
        secrets_file=json_license_path,
        hc_license=med_license,
        hc_secret=enterprise_nlp_secret,
        ocr_secret=ocr_secret,
        ocr_license=ocr_license,
        aws_access_key=aws_access_key,
        aws_key_id=aws_key_id,
        return_empty_secrets_if_none_found=True,
        fin_license=fin_license,
        leg_license=leg_license,
        store_in_jsl_home=store_in_jsl_home,
    )

    if store_in_jsl_home:
        # Cache credentials, Wheels and Jars in ~/.johnsnowlabs
        setup_jsl_home(
            secrets=secrets,
            jvm_install_type=hardware_platform,
            py_install_type=py_install_type,
            refresh_install=refresh_install,
            visual=visual,
            nlp=nlp,
            spark_nlp=spark_nlp,
        )

    # Databricks Install
    if not databricks_host and databricks_token:
        raise Exception()
    suite = get_install_suite_from_jsl_home(
        jvm_hardware_target=hardware_platform,
        visual=visual,
        nlp=nlp,
        spark_nlp=spark_nlp,
    )
    if databricks_cluster_id:
        # Install to existing cluster
        install_jsl_suite_to_cluster(
            db=get_db_client_for_token(databricks_host, databricks_token),
            install_suite=suite,
            cluster_id=databricks_cluster_id,
            medical_nlp=nlp,
            spark_nlp=spark_nlp,
            visual=visual,
        )
        if extra_pip_installs:
            install_list_of_pypi_ref_to_cluster(
                db=get_db_client_for_token(databricks_host, databricks_token),
                cluster_id=databricks_cluster_id,
                pip_installs=extra_pip_installs,
            )

    else:
        # Create new cluster
        return create_cluster(
            medical_nlp=nlp,
            spark_nlp=spark_nlp,
            visual=visual,
            databricks_host=databricks_host,
            databricks_token=databricks_token,
            install_suite=suite,
            extra_pip_installs=extra_pip_installs,
            block_till_cluster_ready=block_till_cluster_ready,
            num_workers=num_workers,
            cluster_name=cluster_name,
            node_type_id=node_type_id,
            driver_node_type_id=driver_node_type_id,
            spark_env_vars=spark_env_vars,
            autotermination_minutes=autotermination_minutes,
            spark_version=spark_version,
            spark_conf=spark_conf,
            auto_scale=auto_scale,
            aws_attributes=aws_attributes,
            ssh_public_keys=ssh_public_keys,
            custom_tags=custom_tags,
            cluster_log_conf=cluster_log_conf,
            enable_elastic_disk=enable_elastic_disk,
            cluster_source=cluster_source,
            instance_pool_id=instance_pool_id,
            headers=headers,
            write_db_credentials=write_db_credentials,
        )


def install_to_emr(
    boto_session: Optional["boto3.Session"] = None,
    # EMR specific configs
    bootstrap_bucket: Optional[str] = None,
    s3_logs_path: Optional[str] = None,
    service_role: Optional[str] = settings.emr_default_service_role,
    job_flow_role: Optional[str] = settings.emr_default_instance_profile,
    subnet_id: Optional[str] = None,
    ec2_key_name: Optional[str] = None,
    # Browser Auth
    browser_login: bool = True,
    force_browser: bool = False,
    # JWT Token Auth
    access_token: Optional[str] = None,
    # JSON file Auth
    json_license_path: Optional[str] = None,
    # Manual License specification Auth
    license: Optional[str] = None,
    aws_access_key: Optional[str] = None,
    aws_key_id: Optional[str] = None,
    local_license_number: int = 0,
    remote_license_number: int = 0,
    nlp: bool = True,
    spark_nlp: bool = True,
    visual: bool = False,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
    auto_terminate_hours: Optional[int] = 1,
) -> str:
    """Install John Snow Labs NLP and selected products on an EMR cluster
    :param boto_session: Boto3 session. Refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
    :param bootstrap_bucket: S3 bucket to store bootstrap scripts
    :param s3_logs_path: S3 path to store logs
    :param service_role: EMR service role
    :param job_flow_role: EMR job flow role / instance profilie
    :param subnet_id: EMR subnet id
    :param ec2_key_name: EC2 key name
    :param browser_login: Use browser login
    :param force_browser: Force browser login
    :param access_token: JWT access token
    :param json_license_path: Path to JSON license file
    :param license: License string
    :param local_license_number: Local license number
    :param remote_license_number: Remote license number
    :param nlp: Install NLP
    :param spark_nlp: Install Spark NLP
    :param visual: Install Visual
    :param hardware_platform: Hardware platform
    :param auto_terminate_hours : Idle hour to wait before terminating the cluster
    :return: EMR cluster id
    """
    import boto3

    secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(
        browser_login=browser_login,
        force_browser=force_browser,
        access_token=access_token,
        local_license_number=local_license_number,
        remote_license_number=remote_license_number,
        secrets_file=json_license_path,
        hc_license=license,
        return_empty_secrets_if_none_found=True,
        fin_license=license,
        leg_license=license,
        aws_access_key=aws_access_key,
        aws_key_id=aws_key_id,
        only_return_secrets=True,
    )
    if not boto_session:
        boto_session = boto3.Session()

    cluster_id = create_emr_cluster(
        boto_session=boto_session,
        secrets=secrets,
        s3_logs_path=s3_logs_path,
        bootstrap_bucket=bootstrap_bucket,
        job_flow_role=job_flow_role,
        service_role=service_role,
        subnet_id=subnet_id,
        ec2_key_name=ec2_key_name,
        nlp=nlp,
        spark_nlp=spark_nlp,
        visual=visual,
        hardware_platform=hardware_platform,
        auto_terminate_hours=auto_terminate_hours,
    )
    return cluster_id


def install_to_glue(
    boto_session: Optional["boto3.Session"] = None,
    glue_assets_bucket: Optional[str] = None,
    # Browser Auth
    browser_login: bool = True,
    force_browser: bool = False,
    # JWT Token Auth
    access_token: Optional[str] = None,
    # JSON file Auth
    json_license_path: Optional[str] = None,
    # Manual License specification Auth
    license: Optional[str] = None,
    aws_access_key: Optional[str] = None,
    aws_key_id: Optional[str] = None,
    local_license_number: int = 0,
    remote_license_number: int = 0,
    nlp: bool = True,
    spark_nlp: bool = True,
    visual: bool = False,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
):
    """Install John Snow Labs NLP and selected products on a Glue job
    :param boto_session: Boto3 session. Refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
    :param glue_assets_bucket: S3 bucket to store glue assets
    :param browser_login: Use browser login
    :param force_browser: Force browser login
    :param access_token: JWT access token
    :param json_license_path: Path to JSON license file
    :param license: License string
    :param local_license_number: Local license number
    :param remote_license_number: Remote license number
    :param nlp: Install NLP
    :param spark_nlp: Install Spark NLP
    :param visual: Install Visual
    :param hardware_platform: Hardware platform

    """
    import boto3

    if not boto_session:
        boto_session = boto3.Session()

    # Download jars and wheels so that we can upload them
    install_suite = get_install_suite_from_jsl_home(
        jvm_hardware_target=hardware_platform,
        visual=visual,
        nlp=nlp,
        spark_nlp=spark_nlp,
        browser_login=browser_login,
        force_browser=force_browser,
        access_token=access_token,
        local_license_number=local_license_number,
        remote_license_number=remote_license_number,
        secrets_file=json_license_path,
        hc_license=license,
        fin_license=license,
        leg_license=license,
        aws_access_key=aws_access_key,
        aws_key_id=aws_key_id,
    )
    # Make sure bucket exists
    bucket = create_glue_bucket(
        boto_session=boto_session,
        bucket=glue_assets_bucket,
    )
    # Upload jars and wheels to s3 bucket for glue
    jars_s3_location, packages_s3_location = upload_pylibs_jars_to_glue_bucket(
        boto_session=boto_session, install_suite=install_suite, bucket=bucket
    )

    # Show instructions on how to run a glue notebook
    print(
        get_printable_glue_notebook_commands(
            boto_session=boto_session,
            glue_assets_bucket=bucket,
            packages_s3_location=packages_s3_location,
            jars_s3_location=jars_s3_location,
            secrets=install_suite.secrets,
        )
    )
