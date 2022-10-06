from typing import List, Tuple
from johnsnowlabs.utils.enums import PyInstallTypes, ProductLogo, JvmHardwareTarget
from johnsnowlabs.py_models.url_dependency import UrlDependency
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.auto_install.lib_resolvers import OcrLibResolver, HcLibResolver, NlpLibResolver


def get_printable_dependency_urls(
        secrets: JslSecrets,
        jvm_install_type: JvmHardwareTarget = JvmHardwareTarget.cpu,
        py_install_type: PyInstallTypes = PyInstallTypes.wheel,
        spark_version=None,
) -> \
        Tuple[List[str], List[str]]:
    """
    Get URL for every dependency to which the found_secrets have access to with respect to CURRENT pyspark install.
    If no pyspark is installed, this fails because we need to know pyspark version to generate correct URL
    :param jvm_install_type:
    :param spark_version:
    :param secrets:
    :param py_install_type: PyInstallTypes.wheel or PyInstallTypes.tar
    :return: list of pre-formatted message arrays java_dependencies, py_dependencies
    """
    messages = []
    java_dependencies = []
    py_dependencies = []
    if jvm_install_type == JvmHardwareTarget.gpu:
        java_dependencies.append(
            f'{ProductLogo.nlp.value}{ProductLogo.java.value}  Spark NLP GPU Java Jar:'
            f'{NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version).url}')
    elif jvm_install_type == JvmHardwareTarget.cpu:
        java_dependencies.append(
            f'{ProductLogo.nlp.value}{ProductLogo.java.value}  Spark NLP CPU Java Jar:'
            f'{NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version).url}')
    elif jvm_install_type == JvmHardwareTarget.m1:
        java_dependencies.append(
            f'{ProductLogo.nlp.value}{ProductLogo.java.value}  Spark NLP M1 Java Jar:'
            f'{NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version).url}')

    if py_install_type == PyInstallTypes.wheel:
        py_dependencies.append(
            f'{ProductLogo.nlp.value}{ProductLogo.python.value} Spark NLP for Python Wheel: '
            f'{NlpLibResolver.get_py_urls(install_type=py_install_type, spark_version_to_match=spark_version).url}')
    else:
        py_dependencies.append(
            f'{ProductLogo.nlp.value}{ProductLogo.python.value} Spark NLP for Python Tar:'
            f'{NlpLibResolver.get_py_urls(install_type=py_install_type, spark_version_to_match=spark_version).url}')

    if secrets.HC_SECRET:
        java_dependencies.append(
            f'{ProductLogo.hc.value}{ProductLogo.java.value}  Spark NLP for Healthcare Java Jar:'
            f' {HcLibResolver.get_jar_urls(secret=secrets.HC_SECRET, hardware_target=jvm_install_type, spark_version_to_match=spark_version).url}')
        if py_install_type == PyInstallTypes.wheel:
            py_dependencies.append(
                f'{ProductLogo.hc.value}{ProductLogo.python.value} Spark NLP for Healthcare Python Wheel:'
                f' {HcLibResolver.get_py_urls(secret=secrets.HC_SECRET, install_type=py_install_type, spark_version_to_match=spark_version).url}')
        else:
            py_dependencies.append(
                f'{ProductLogo.hc.value}{ProductLogo.python.value} Spark NLP for Healthcare Python Tar:'
                f' {HcLibResolver.get_py_urls(secret=secrets.HC_SECRET, install_type=py_install_type, spark_version_to_match=spark_version).url}')

    if secrets.OCR_SECRET:
        java_dependencies.append(
            f'{ProductLogo.ocr.value}{ProductLogo.java.value}  Spark OCR Java Jar:'
            f' {OcrLibResolver.get_jar_urls(secret=secrets.OCR_SECRET, hardware_target=jvm_install_type, spark_version_to_match=spark_version).url}')
        if py_install_type == PyInstallTypes.wheel:
            py_dependencies.append(
                f'{ProductLogo.ocr.value}{ProductLogo.python.value} Spark OCR Python Wheel:'
                f' {OcrLibResolver.get_py_urls(secret=secrets.OCR_SECRET, install_type=py_install_type, spark_version_to_match=spark_version).url}')
        else:
            py_dependencies.append(
                f'{ProductLogo.ocr.value}{ProductLogo.python.value} Spark OCR Python Tar:'
                f' {OcrLibResolver.get_py_urls(secret=secrets.OCR_SECRET, install_type=py_install_type, spark_version_to_match=spark_version).url}')

    print('\n'.join(java_dependencies + py_dependencies))
    print(f'Make sure all these dependencies are installed on your Spark Driver and Worker nodes')
    return java_dependencies, py_dependencies


def get_py4j_dependency_urls(
        secrets: JslSecrets,
        jvm_install_type: JvmHardwareTarget = JvmHardwareTarget.cpu,
        py_install_type: PyInstallTypes = PyInstallTypes.wheel,
        spark_version=None,
        get_all_jvm_hardware_targets: bool = False,
) -> \
        Tuple[List[UrlDependency], List[UrlDependency]]:
    """
    Get URL for every dependency to which the found_secrets have access to with respect to CURRENT pyspark install.
    If no pyspark is installed, this fails because we need to know pyspark version to generate correct URL
    :param jvm_install_type:
    :param spark_version:
    :param get_all_jvm_hardware_targets:
    :param secrets:
    :param py_install_type: PyInstallTypes.wheel or PyInstallTypes.tar
    :return: list of pre-formatted message arrays java_dependencies, py_dependencies
    """
    messages = []
    java_dependencies = []
    py_dependencies = []
    if jvm_install_type == JvmHardwareTarget.gpu or get_all_jvm_hardware_targets:
        java_dependencies.append(
            NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version))
    elif jvm_install_type == JvmHardwareTarget.cpu or get_all_jvm_hardware_targets:
        java_dependencies.append(
            NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version))
    elif jvm_install_type == JvmHardwareTarget.m1 or get_all_jvm_hardware_targets:
        java_dependencies.append(
            NlpLibResolver.get_jar_urls(hardware_target=jvm_install_type, spark_version_to_match=spark_version))

    if py_install_type == PyInstallTypes.wheel:
        py_dependencies.append(
            NlpLibResolver.get_py_urls(install_type=py_install_type, spark_version_to_match=spark_version))
    else:
        py_dependencies.append(
            NlpLibResolver.get_py_urls(install_type=py_install_type, spark_version_to_match=spark_version))

    if secrets and secrets.HC_SECRET:
        java_dependencies.append(
            HcLibResolver.get_jar_urls(secret=secrets.HC_SECRET, spark_version_to_match=spark_version))
        if py_install_type == PyInstallTypes.wheel:
            py_dependencies.append(HcLibResolver.get_py_urls(secret=secrets.HC_SECRET, install_type=py_install_type,
                                                             spark_version_to_match=spark_version))
        else:
            py_dependencies.append(HcLibResolver.get_py_urls(secret=secrets.HC_SECRET, install_type=py_install_type,
                                                             spark_version_to_match=spark_version))

    if secrets and secrets.OCR_SECRET:
        java_dependencies.append(
            OcrLibResolver.get_jar_urls(secret=secrets.OCR_SECRET, spark_version_to_match=spark_version))
        if py_install_type == PyInstallTypes.wheel:
            py_dependencies.append(OcrLibResolver.get_py_urls(secret=secrets.OCR_SECRET, install_type=py_install_type,
                                                              spark_version_to_match=spark_version))
        else:
            py_dependencies.append(OcrLibResolver.get_py_urls(secret=secrets.OCR_SECRET, install_type=py_install_type,
                                                              spark_version_to_match=spark_version))

    return java_dependencies, py_dependencies
