import glob
import os
import subprocess


def process_was_suc(result: subprocess.CompletedProcess) -> bool:
    if result.stderr:
        return False
    return True


def log_process(result: subprocess.CompletedProcess):
    print("______________STDOUT:")
    print(result.stdout.decode())
    print("______________STDERR:")
    print(result.stderr.decode())


#
# @dataclass
# class VenvState:
#     installed_libs: List[str]
#     py_version: str


class VenvWrapper:
    """
    Utils to install into a Python Executable, which is not the same as current the currently running one
    I.e. whenever you want to install to a local python executable which is != sys.executable use this
    """

    @staticmethod
    def create_venv(venv_target_dir, ensure_pip=True, log=False):
        # Create venv with given or current sys.executables
        import venv

        venv.create(venv_target_dir)
        if ensure_pip:
            VenvWrapper.install_pip_if_missing(venv_target_dir)
        return True

    @staticmethod
    def glob_py_exec_from_venv(venv_dir, raise_except=True):
        py_exec_path = glob.glob(f"{venv_dir}/bin/*python*")
        if py_exec_path:
            return py_exec_path[0]
        if raise_except:
            raise Exception(
                f"Could not find Python Executable in venv dir = {venv_dir} "
                f"Please Specify correct path manually"
            )
        else:
            return False

    @staticmethod
    def is_pip_in_venv(venv_py_exec_path, log=False):
        r = subprocess.run([venv_py_exec_path, "-m", "pip"], capture_output=True)
        if log:
            log_process(r)
        return process_was_suc(r)

    @staticmethod
    def install_pip_in_venv(venv_py_exec_path, log=False):
        if not os.path.exists("get-pip.py"):
            pip_url = "https://bootstrap.pypa.io/get-pip.py"
            os.system(f"! wget {pip_url}")

        r = subprocess.run([venv_py_exec_path, "get-pip.py"], capture_output=True)
        if log:
            log_process(r)
        return process_was_suc(r)

    @staticmethod
    def install_pip_if_missing(venv_target_dir: str):
        venv_py_exec_path = VenvWrapper.glob_py_exec_from_venv(
            venv_target_dir, raise_except=True
        )
        if not VenvWrapper.is_pip_in_venv(venv_py_exec_path):
            if not VenvWrapper.install_pip_in_venv(venv_py_exec_path):
                raise Exception(
                    f"Could not find or setup pip in venv at  {venv_target_dir} using python executable {venv_py_exec_path}"
                )

    @staticmethod
    def install_to_venv(venv_target_dir, pypi_name, log=False):
        venv_py_exec_path = VenvWrapper.glob_py_exec_from_venv(
            venv_target_dir, raise_except=True
        )
        r = subprocess.run(
            [venv_py_exec_path, "-m", "pip", "install", pypi_name], capture_output=True
        )
        if log:
            log_process(r)
        return process_was_suc(r)

    @staticmethod
    def uninstall_from_venv(venv_target_dir, pypi_name, log=False):
        venv_py_exec_path = VenvWrapper.glob_py_exec_from_venv(
            venv_target_dir, raise_except=True
        )
        r = subprocess.run(
            [venv_py_exec_path, "-m", "pip", "uninstall", pypi_name, "-y"],
            capture_output=True,
        )
        if log:
            log_process(r)
        return process_was_suc(r)

    @staticmethod
    def is_lib_in_venv(venv_target_dir, module_name, log=False):
        venv_py_exec_path = VenvWrapper.glob_py_exec_from_venv(
            venv_target_dir, raise_except=True
        )
        return VenvWrapper.is_lib_in_py_exec(venv_py_exec_path, module_name, log)

    @staticmethod
    def is_lib_in_py_exec(venv_py_exec_path, module_name, log=False):
        r = subprocess.run(
            [venv_py_exec_path, "-c", f"import {module_name}"], capture_output=True
        )
        if log:
            log_process(r)
        return process_was_suc(r)

    @staticmethod
    def run_in_venv(venv_dir, py_script, log=False):

        print(f"Running with  {venv_dir} Script:\n{py_script}")
        r = subprocess.run(
            [VenvWrapper.glob_py_exec_from_venv(venv_dir), "-c", f"{py_script}"],
            capture_output=True,
        )
        if log:
            log_process(r)
        return process_was_suc(r)
