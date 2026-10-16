import importlib
import re
import site
import subprocess
from importlib import reload

from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.utils.venv_utils import VenvWrapper

reload(site)
import os
from typing import Optional

from johnsnowlabs.utils.enums import (
    LatestCompatibleProductVersion,
    ProductLogo,
    PyInstallTypes,
)
from johnsnowlabs.py_models.primitive import LibVersionIdentifier
from johnsnowlabs.py_models.jsl_secrets import JslSecrets

import json
import sys
from urllib import request
from packaging.version import parse


def get_all_lib_version_on_pypi(pkg_name):
    url = f"https://pypi.python.org/pypi/{pkg_name}/json"
    releases = json.loads(request.urlopen(url).read())["releases"]
    return sorted(releases, key=parse, reverse=True)


def get_latest_lib_version_on_pypi(pkg_name):
    return get_all_lib_version_on_pypi(pkg_name)[0]


def get_pip_lib_version(lib: str, py_exec: str = sys.executable):
    # Get lib version of a library according to pip
    r = subprocess.run([py_exec, "-m", "pip", "list"], capture_output=True, text=True)
    matches = list(filter(lambda x: x.split(" ")[0] == lib, r.stdout.split("\n")))
    if not matches:
        return False  # raise ValueError(f'Could not find lib {lib}')
    else:
        return LibVersion(matches[0].split(" ")[-1])


def uninstall_lib(pip_package_name, py_path=sys.executable):
    cmd = f"{py_path} -m pip uninstall {pip_package_name} -y "
    os.system(cmd)
    reload(site)


def install_standard_pypi_lib(
    pypi_name: str,
    module_name: Optional[str] = None,
    python_path: str = sys.executable,
    upgrade: bool = True,
    re_install: bool = False,
    version: Optional[str] = None,
    download_folder: Optional[str] = None,
    include_dependencies: bool = True,
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
    if isinstance(version, LibVersion):
        version = version.as_str()

    if not pypi_name:
        raise Exception(
            f"Tried to install software which has no pypi file_name! Aborting."
        )
    print(f"Installing {pypi_name} to {python_path}")
    c = f"{python_path} -m pip install {pypi_name}"
    if version:
        c = c + f"=={version} "
    else:
        c = c + " "

    if upgrade:
        c = c + "--upgrade "
    if re_install:
        c = c + " --force-reinstall"

    if download_folder:
        if version:
            c = f"{python_path} -m pip download {pypi_name}=={version} -d {download_folder}"
        else:
            c = f"{python_path} -m pip download {pypi_name} -d {download_folder}"

    if not include_dependencies:
        c = c + " --no-deps"

    replay_deps, keep_present = [], False
    if include_dependencies and not download_folder:
        protect_pyspark, replay_deps, keep_present = _licensed_install_plan(
            pypi_name, python_path
        )
        if protect_pyspark:
            c = c + " --no-deps"

    os.system(c)
    _pip_install_each(python_path, replay_deps, keep_present)

    if module_name and not download_folder:
        try:
            # See if install worked
            # importlib.import_module(module_name)
            reload(site)
            globals()[module_name] = importlib.import_module(module_name)
        except ImportError as err:
            print(f"Failure Installing {pypi_name}")
            return False
    return True


def install_licensed_pypi_lib(
    secrets: JslSecrets,
    pypi_name,
    module_name,
    product: "AbstractSoftwareProduct",
    spark_version: LibVersionIdentifier = LatestCompatibleProductVersion.pyspark.value,
    upgrade=True,
    py_path: str = sys.executable,
    download_folder: Optional[str] = None,
    include_dependencies: bool = True,
):
    """Install Spark-NLP-Healthcare PyPI Package in target python executable
    This just requires the secret of the library.
    """
    get_deps = True
    missmatch = False
    if "spark-nlp-jsl" in pypi_name or "internal_with_finleg" in pypi_name:
        if not secrets.HC_SECRET:
            return False
        module_name = "sparknlp_jsl"
        secret = secrets.HC_SECRET
        # get_deps = True
    elif "ocr" in pypi_name:
        if not secrets.OCR_SECRET:
            return False
        secret = secrets.OCR_SECRET
        module_name = "sparkocr"
        # get_deps = True

    else:
        raise ValueError(f"Invalid install licensed install target ={pypi_name}")

    try:
        url = product.jsl_url_resolver.get_py_urls(
            secret=secret,
            spark_version_to_match=spark_version,
            install_type=PyInstallTypes.wheel,
        ).url
        cmd = f"{py_path} -m pip install {url}"

        # Install lib
        if upgrade:
            cmd = cmd + " --force-reinstall"
        # cmd = f'{sys.executable} -m pip install {pypi_name}=={lib_version} --extra-index-url https://pypi.johnsnowlabs.com/{secret}'

        if download_folder:
            cmd = f"{py_path} -m pip download {pypi_name} -d {download_folder}"

        if not include_dependencies:
            cmd = cmd + " --no-deps"

        replay_deps, keep_present = [], False
        if include_dependencies and not download_folder:
            protect_pyspark, replay_deps, keep_present = _licensed_install_plan(
                url, py_path
            )
            if protect_pyspark:
                cmd = cmd + " --no-deps"

        print(f'Running "{cmd.replace(secret, "[LIB_SECRET]")}"')
        os.system(cmd)
        _pip_install_each(py_path, replay_deps, keep_present)

        # Check if Install succeeded
        if py_path == sys.executable:
            # Check for python executable that is currently running
            reload(site)
            globals()[module_name] = importlib.import_module(module_name)
        else:
            # Check for python executable which is on this machine but not the same as the running one
            return VenvWrapper.is_lib_in_py_exec(py_path, module_name, False)

    except Exception as err:
        print("Failure to install", err)
        return False
    return True


def _is_spark4_env(py_path: str = sys.executable) -> bool:
    """True when the target interpreter has a Spark 4 pyspark installed."""
    try:
        if py_path == sys.executable:
            import pyspark

            return str(pyspark.__version__).split(".")[0] == "4"
        out = subprocess.run(
            [py_path, "-c", "import pyspark;print(pyspark.__version__)"],
            capture_output=True,
            text=True,
            timeout=60,
        ).stdout.strip()
        return out.split(".")[0] == "4"
    except Exception:
        return False


def _wheel_requirements_except_pyspark(wheel: str):
    # read from the wheel METADATA so the list cannot drift from what it declares
    try:
        import io
        import zipfile
        import urllib.request

        if os.path.exists(wheel):
            handle = open(wheel, "rb")
        else:
            handle = io.BytesIO(urllib.request.urlopen(wheel, timeout=600).read())
        reqs = []
        with zipfile.ZipFile(handle) as z:
            meta = next(n for n in z.namelist() if n.endswith("METADATA"))
            for line in z.read(meta).decode("utf-8", "ignore").splitlines():
                if not line.startswith("Requires-Dist:"):
                    continue
                spec = line.split(":", 1)[1].strip()
                if ";" in spec:
                    continue
                name = spec.split()[0].split("(")[0].split("[")[0]
                name = name.split("=")[0].split("<")[0].split(">")[0].split("!")[0]
                if name.strip().lower().replace("_", "-") == "pyspark":
                    continue
                reqs.append(spec.replace("(", "").replace(")", "").replace(" ", ""))
        return reqs
    except Exception as e:
        print(f"Warning: could not read dependencies from wheel, skipping. {e}")
        return []


def _target_python_version(py_path: str = sys.executable):
    if py_path == sys.executable:
        return sys.version_info[:2]
    out = subprocess.run(
        [py_path, "-c", "import sys;print('%d.%d' % sys.version_info[:2])"],
        capture_output=True, text=True, timeout=60,
    ).stdout.strip()
    return tuple(int(part) for part in out.split("."))


def _product_python_ceiling(target: str, py_path: str):
    # the product's highest supported python, but only when this interpreter is newer
    from johnsnowlabs import settings  # local, this module is imported during package init

    name = os.path.basename(str(target)).lower().replace("-", "_")
    if name.startswith("spark_ocr"):
        ceiling = settings.max_python_ocr
    elif name.startswith("spark_nlp_jsl"):
        ceiling = settings.max_python_hc
    else:
        return None
    try:
        current = _target_python_version(py_path)
    except Exception:
        return None
    if current > tuple(int(part) for part in ceiling.split(".")):
        return ceiling
    return None


def _licensed_install_plan(target: str, py_path: str):
    if not (str(target).endswith(".whl") and _is_licensed_wheel(target)):
        return False, [], False
    name = os.path.basename(str(target))
    ceiling = _product_python_ceiling(target, py_path)
    if ceiling:
        print(
            f"{ProductLogo.pyspark.value} Warning: {name} supports python up to "
            f"{ceiling}, this is python "
            f"{'.'.join(str(p) for p in _target_python_version(py_path))}. Its declared "
            f"dependency versions are not enforced here: missing ones get installed, "
            f"present ones are left alone."
        )
        return True, _wheel_requirements_except_pyspark(target), True
    # a licensed wheel's pyspark ceiling would otherwise downgrade an installed Spark 4
    if _is_spark4_env(py_path):
        print(
            f"{ProductLogo.pyspark.value} Spark 4 detected, installing {name} without "
            f"its declared dependencies to protect the installed pyspark"
        )
        return True, _wheel_requirements_except_pyspark(target), False
    return False, [], False


JSL_PRODUCT_DISTS = ("spark-nlp", "spark-nlp-jsl", "spark-ocr")


def _dist_is_installed(py_path: str, dist: str) -> bool:
    code = (
        "import importlib.metadata as m,sys;"
        "sys.exit(0 if m.version(%r) else 1)" % dist
    )
    try:
        return subprocess.run([py_path, "-c", code], capture_output=True, timeout=60).returncode == 0
    except Exception:
        return False


def _pip_install(py_path: str, spec: str) -> int:
    dep_cmd = f'{py_path} -m pip install "{spec}"'
    print(f'Running "{dep_cmd}"')
    return os.system(dep_cmd)


def _pip_install_each(py_path: str, deps, keep_present: bool = False) -> None:
    for dep in deps:
        bare = re.split(r"[<>=!~\[;]", dep, 1)[0].strip()
        is_jsl = bare.lower().replace("_", "-") in JSL_PRODUCT_DISTS
        # outside the declared ranges anyway, so any present version is left alone
        if keep_present and not is_jsl and bare and _dist_is_installed(py_path, bare):
            print(f"{bare} is already installed, leaving its version alone")
            continue
        if _pip_install(py_path, dep) == 0 or not keep_present or is_jsl or bare == dep:
            continue
        # the declared range has no release for this python, so take any version
        print(f'{dep} is not installable here, retrying as "{bare}"')
        _pip_install(py_path, bare)


def _is_licensed_wheel(path: str) -> bool:
    """True for the Healthcare and Visual NLP wheels, by file name."""
    name = os.path.basename(str(path)).lower().replace("-", "_")
    return name.startswith("spark_nlp_jsl") or name.startswith("spark_ocr")
