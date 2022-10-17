import importlib
import site
import subprocess
from importlib import reload
from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.utils.venv_utils import VenvWrapper

reload(site)
import os
from typing import Optional

from johnsnowlabs.utils.enums import LatestCompatibleProductVersion, PyInstallTypes
from johnsnowlabs.py_models.primitive import LibVersionIdentifier
from johnsnowlabs.py_models.jsl_secrets import JslSecrets

import json
import sys
from urllib import request
from pkg_resources import parse_version


def get_all_lib_version_on_pypi(pkg_name):
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    return sorted(releases, key=parse_version, reverse=True)


def get_latest_lib_version_on_pypi(pkg_name):
    return get_all_lib_version_on_pypi(pkg_name)[0]


def get_pip_lib_version(lib: str, py_exec: str = sys.executable):
    # Get lib version of a library according to pip
    r = subprocess.run([py_exec, '-m', 'pip', 'list'], capture_output=True, text=True)
    matches = list(filter(lambda x: x.split(' ')[0] == lib, r.stdout.split('\n')))
    if not matches:
        return False  # raise ValueError(f'Could not find lib {lib}')
    else:
        return LibVersion(matches[0].split(' ')[-1])


def uninstall_lib(pip_package_name, py_path=sys.executable):
    cmd = f'{py_path} -m pip uninstall {pip_package_name} -y '
    os.system(cmd)
    reload(site)


def install_standard_pypi_lib(pypi_name: str,
                              module_name: Optional[str] = None,
                              python_path: str = sys.executable,
                              upgrade: bool = True,
                              re_install: bool = False,
                              version: Optional[str] = None,
                              download_folder: Optional[str] = None,
                              include_dependencies: bool = True
                              ):
    """
    Install module via pypi.
    runs the command : 
        `python -m pip install [module_name]`
        `python -m pip install [module_name] --upgrade`
    :param re_install:
    :param version:
    :param pypi_name: file_name of pypi package or path to local whl
    :param module_name: If defined will import module into globals, making it available to running process
    :param python_path: Which Python to use for installing. Defaults to the Python calling this method.
    :param upgrade: use --upgrade flag or not 
    :return:
    """
    if isinstance(version,LibVersion ):
        version = version.as_str()

    if not pypi_name:
        raise Exception(f'Tried to install software which has no pypi file_name! Aborting.')
    print(f'Installing {pypi_name} to {python_path}')
    c = f'{python_path} -m pip install {pypi_name}'
    print(f'Running: {c}')
    if version:
        c = c + f'=={version} '
    else:
        c = c + ' '

    if upgrade:
        c = c + '--upgrade '
    if re_install:
        c = c + ' --force-reinstall'

    if download_folder:
        if version:
            c = f'{python_path} -m pip download {pypi_name}=={version} -d {download_folder}'
        else:
            c = f'{python_path} -m pip download {pypi_name} -d {download_folder}'

    if not include_dependencies:
        c = c + ' --no-deps'

    os.system(c)
    if module_name and not download_folder:
        try:
            # See if install worked
            # importlib.import_module(module_name)
            reload(site)
            globals()[module_name] = importlib.import_module(module_name)
        except ImportError as err:
            print(f'Failure Installing {pypi_name}')
            return False
    return True


def install_licensed_pypi_lib(secrets: JslSecrets,
                              pypi_name,
                              module_name,
                              product: 'AbstractSoftwareProduct',
                              spark_version: LibVersionIdentifier = LatestCompatibleProductVersion.pyspark.value,
                              upgrade=True,
                              py_path: str = sys.executable,
                              download_folder: Optional[str] = None,
                              include_dependencies: bool = True

                              ):
    """ Install Spark-NLP-Healthcare PyPI Package in target python executable
    This just requires the secret of the library.
    """
    get_deps = True
    missmatch = False
    if 'spark-nlp-jsl' in pypi_name or 'internal_with_finleg' in pypi_name:
        if not secrets.HC_SECRET:
            return False
        module_name = 'sparknlp_jsl'
        secret = secrets.HC_SECRET
        # get_deps = True
    elif 'ocr' in pypi_name:
        if not secrets.OCR_SECRET:
            return False
        secret = secrets.OCR_SECRET
        module_name = 'sparkocr'
        # get_deps = True

    else:
        raise ValueError(f'Invalid install licensed install target ={pypi_name}')

    try:
        url = product.jsl_url_resolver.get_py_urls(secret=secret,
                                                   spark_version_to_match=spark_version,
                                                   install_type=PyInstallTypes.wheel).url
        cmd = f'{py_path} -m pip install {url}'

        # Install lib
        if upgrade:
            cmd = cmd + ' --force-reinstall'
        # cmd = f'{sys.executable} -m pip install {pypi_name}=={lib_version} --extra-index-url https://pypi.johnsnowlabs.com/{secret}'

        if download_folder:
            cmd = f'{py_path} -m pip download {pypi_name} -d {download_folder}'

        if not include_dependencies:
            cmd = cmd + ' --no-deps'

        print(f'Running "{cmd.replace(secret, "[LIB_SECRET]")}"')
        os.system(cmd)

        # Check if Install succeeded
        if py_path == sys.executable:
            # Check for python executable that is currently running
            reload(site)
            globals()[module_name] = importlib.import_module(module_name)
        else:
            # Check for python executable which is on this machine but not the same as the running one
            return VenvWrapper.is_lib_in_py_exec(py_path, module_name, False)

    except Exception as err:
        print('Failure to install', err)
        return False
    return True
