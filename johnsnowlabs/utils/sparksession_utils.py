import time
import os
from typing import Optional, List, Dict

from johnsnowlabs import settings
from johnsnowlabs.auto_install.jsl_home import get_install_suite_from_jsl_home
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.utils.enums import JvmHardwareTarget
from johnsnowlabs.py_models.install_info import InstallSuite


def authenticate_enviroment_HC(suite: InstallSuite):
    """Set Secret environ variables for Spark Context"""
    if suite.secrets.HC_LICENSE:
        os.environ['SPARK_NLP_LICENSE'] = suite.secrets.HC_LICENSE
    os.environ['AWS_ACCESS_KEY_ID'] = suite.secrets.AWS_ACCESS_KEY_ID
    os.environ['AWS_SECRET_ACCESS_KEY'] = suite.secrets.AWS_SECRET_ACCESS_KEY


def authenticate_enviroment_OCR(suite: InstallSuite):
    """Set Secret environ variables for Spark Context"""
    if suite.secrets.OCR_LICENSE:
        os.environ['SPARK_NLP_LICENSE'] = suite.secrets.OCR_LICENSE
    os.environ['AWS_ACCESS_KEY_ID'] = suite.secrets.AWS_ACCESS_KEY_ID
    os.environ['AWS_SECRET_ACCESS_KEY'] = suite.secrets.AWS_SECRET_ACCESS_KEY


def authenticate_enviroment_HC_and_OCR(suite: InstallSuite):
    """Set Secret environ variables for Spark Context"""
    authenticate_enviroment_HC(suite)
    authenticate_enviroment_OCR(suite)


def retry(fun, max_tries=10):
    for i in range(max_tries):
        try:
            time.sleep(0.3)
            fun()
            break
        except Exception:
            continue


def start(
        # -- JSL-Auth Flows --
        # Browser Auth
        browser_login: bool = False,
        # JWT Token Auth
        access_token: Optional[str] = None,
        # JSON file Auth
        json_license_path: Optional[str] = None,
        # AWS Auth
        aws_access_key: Optional[str] = None,
        aws_key_id: Optional[str] = None,
        # Manual License specification Auth
        enterprise_nlp_secret: Optional[str] = None,
        ocr_secret: Optional[str] = None,
        hc_license: Optional[str] = None,
        ocr_license: Optional[str] = None,
        fin_license: Optional[str] = None,
        leg_license: Optional[str] = None,
        # License usage & Caching
        remote_license_number: int = 0,
        local_license_number: int = 0,
        store_in_jsl_home: bool = True,

        # -- Spark Session Configs --
        spark_conf: Optional[Dict[str, str]] = None,
        master_url: str = 'local[*]',
        jar_paths: List[str] = None,
        exclude_nlp: bool = False,
        exclude_healthcare: bool = False,
        exclude_ocr: bool = False,
        hardware_target: str = JvmHardwareTarget.cpu.value,
        model_cache_folder: str = None,

) -> 'pyspark.sql.SparkSession':
    from pyspark.sql import SparkSession

    already_launched = False
    if '_instantiatedSession' in dir(SparkSession) and SparkSession._instantiatedSession is not None:
        print('Spark Session already created, some configs may not take.')
        already_launched = True
        if settings.on_databricks:
            print("Looks like you are on databricks. A Sparksession is launched by Databricks, jsl.start() will not ")

    from johnsnowlabs.auto_install.lib_resolvers import OcrLibResolver, HcLibResolver, NlpLibResolver
    launched_products: List[str] = []
    hardware_target = JvmHardwareTarget.from_str(hardware_target)

    # Get all Local Jar Paths, downloads them if missing
    suite = get_install_suite_from_jsl_home(only_jars=True, jvm_hardware_target=hardware_target,
                                            force_browser=browser_login,
                                            browser_login=browser_login,
                                            access_token=access_token,
                                            local_license_number=local_license_number,
                                            remote_license_number=remote_license_number,
                                            secrets_file=json_license_path,
                                            hc_license=hc_license,
                                            hc_secret=enterprise_nlp_secret,
                                            ocr_secret=ocr_secret,
                                            ocr_license=ocr_license,
                                            aws_access_key=aws_access_key,
                                            aws_key_id=aws_key_id,
                                            fin_license=fin_license,
                                            leg_license=leg_license,
                                            store_in_jsl_home=store_in_jsl_home)

    # Collect all local Jar Paths we have access to for the SparkSession
    jars = []
    if not exclude_nlp and Software.spark_nlp.check_installed(None) \
            and suite.nlp.get_java_path():
        jars.append(suite.nlp.get_java_path())
        import sparknlp
        launched_products.append(f'{Software.spark_nlp.logo}{Software.spark_nlp.name}=={sparknlp.version()}')

    if suite.secrets:
        if suite.hc and not exclude_healthcare and Software.spark_hc.check_installed(None) and suite.hc.get_java_path():
            jars.append(suite.hc.get_java_path())
            authenticate_enviroment_HC(suite)
            import sparknlp_jsl
            launched_products.append(f'{Software.spark_hc.logo}{Software.spark_hc.name}=={sparknlp_jsl.version()}')

        if suite.ocr and not exclude_ocr and Software.spark_ocr.check_installed(None) and suite.ocr.get_java_path():
            jars.append(suite.ocr.get_java_path())
            authenticate_enviroment_OCR(suite)
            import sparkocr
            launched_products.append(f'{Software.spark_ocr.logo}{Software.spark_ocr.name}=={sparkocr.version()}')
    import pyspark
    launched_products.append(f'running on {Software.spark.logo}{Software.pyspark.name}=={pyspark.version.__version__}')

    builder = SparkSession.builder \
        .appName(f'{settings.spark_session_name} with Jars for: {", ".join(launched_products)}') \
        .master(master_url)

    if jar_paths:
        # Add user specified Jars
        jars += jar_paths
    default_conf = {"spark.driver.memory": "16G",
                    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
                    "spark.kryoserializer.buffer.max": "2000M",
                    'spark.driver.maxResultSize': '2000M',
                    'spark.jars': ','.join(jars), }

    if suite.ocr and suite.ocr.get_java_path():
        # is_spark_version_env('32')
        default_conf["spark.sql.optimizer.expression.nestedPruning.enabled"] = "false"
        default_conf["spark.sql.optimizer.nestedSchemaPruning.enabled"] = "false"
        default_conf["spark.sql.legacy.allowUntypedScalaUDF"] = "true"
        default_conf["spark.sql.repl.eagerEval.enabled"] = "true"

    for k, v in default_conf.items():
        builder.config(str(k), str(v))

    if model_cache_folder:
        if not spark_conf:
            spark_conf = {}
        spark_conf['spark.jsl.settings.pretrained.cache_folder'] = model_cache_folder

    if spark_conf:
        for k, v in spark_conf.items():
            builder.config(str(k), str(v))
    spark = builder.getOrCreate()

    if suite.hc and exist_in_jvm('com.johnsnowlabs.util.start.registerListenerAndStartRefresh'):
        spark._jvm.com.johnsnowlabs.util.start.registerListenerAndStartRefresh()
    if suite.ocr and exist_in_jvm('com.johnsnowlabs.util.OcrStart.registerListenerAndStartRefresh'):
        retry(spark._jvm.com.johnsnowlabs.util.OcrStart.registerListenerAndStartRefresh)

    from colorama import Fore
    if not already_launched:
        print(
            f'👌 Launched {Fore.LIGHTGREEN_EX + hardware_target.value}-Optimized JVM{Fore.RESET} SparkSession with Jars for: {", ".join(launched_products)}')

    return spark


def exist_in_jvm(java_class):
    from pyspark import SparkContext
    from pyspark.ml.util import _jvm
    from py4j.java_gateway import UserHelpAutoCompletion
    java_obj = _jvm()
    for name in java_class.split("."):
        # Bug in P4J. Even if ClassPath does not Exist, JVM response is proto.SUCCESS_PACKAGE
        # But it should give exception
        java_obj = getattr(java_obj, name)

    if UserHelpAutoCompletion.KEY in dir(java_obj):
        return False
    return True
