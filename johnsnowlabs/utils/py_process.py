import subprocess
import sys
from pathlib import Path
from typing import List, Callable, Union

import colorama
import pandas as pd

import johnsnowlabs.utils.testing.test_settings
from johnsnowlabs.utils.file_utils import str_to_file

def run_cmd_and_check_succ(
        args: Union[List[str],str],
        log=True,
        suc_print=johnsnowlabs.utils.testing.test_settings.success_worker_print,
        return_pipes=False,
        shell=False,
        raise_on_fail=False,
        use_code=False,
        text=False,
        log_outputs=True,
) -> bool:
    if log:
        if len(args) == 1:
            print(
                f"👷 Executing {colorama.Fore.LIGHTGREEN_EX}{args[0]}{colorama.Fore.RESET}"
            )
        else:
            print(
                f"👷 Executing {colorama.Fore.LIGHTGREEN_EX}{args}{colorama.Fore.RESET}"
            )

    r = subprocess.run(args, capture_output=True, shell=shell, text=text)
    was_suc = process_was_suc(r, suc_print=suc_print, use_code=use_code)
    if log:
        if was_suc:
            print(
                f"{colorama.Fore.LIGHTGREEN_EX}✅ Success running {args}{colorama.Fore.RESET}"
            )
        else:
            print(
                f"{colorama.Fore.LIGHTRED_EX}❌ Failure running {args}{colorama.Fore.LIGHTGREEN_EX}"
            )

    if log_outputs:
        log_process(r)
    if raise_on_fail and not was_suc:
        raise ValueError(f"Failed running {args}")
    if return_pipes:
        return was_suc, r
    return was_suc


def process_was_suc(
        result: subprocess.CompletedProcess,
        suc_print=johnsnowlabs.utils.testing.test_settings.success_worker_print,
        use_code=False,
) -> bool:
    if use_code and result.returncode != 0:
        return False
    elif use_code and result.returncode == 0:
        return True
    else:
        try:
            return suc_print in result.stdout.decode()
        except Exception as err:
            return suc_print in result.stdout


def log_process(result: subprocess.CompletedProcess):
    stdout = result.stdout.decode() if hasattr(result.stdout, "decode") else result.stdout
    stderr = result.stderr.decode() if hasattr(result.stderr, "decode") else result.stderr
    if stdout:
        print(f"STDOUT: {stdout}")
    if stderr:
        print(f"STDERR: {stderr}")




def execute_py_script_string_as_new_proc(
        py_script,
        suc_print=johnsnowlabs.utils.testing.test_settings.success_worker_print,
        py_exec_path=sys.executable,
        log=True,
        file_name=None,  # Optional metadata
        use_i_py=False,
        add_prefix=True,
):
    Path(johnsnowlabs.utils.testing.test_settings.tmp_markdown_dir).mkdir(
        exist_ok=True, parents=True
    )

    if file_name:
        out_path = f"{johnsnowlabs.utils.testing.test_settings.tmp_markdown_dir}/{file_name}_MD_TEST.py"
    else:
        out_path = "tmp.py"
    if add_prefix:
        prefix = """
from johnsnowlabs import *
spark = nlp.start()
"""
    else:
        prefix = ""

    suffix = f"""
print('{suc_print}')    
    
"""

    str_to_file(prefix + py_script + suffix, out_path)
    suc, proc = execute_py_script_as_new_proc(
        out_path, use_i_py=use_i_py, py_exec_path=py_exec_path
    )
    return make_modelhub_snippet_log(file_name, suc, proc)


def execute_py_script_as_new_proc(
        py_script_path: str,
        suc_print=johnsnowlabs.utils.testing.test_settings.success_worker_print,
        py_exec_path=sys.executable,
        log=True,
        use_i_py=True,
):
    # requires ipython installed
    if use_i_py:
        cmd_args = [py_exec_path, "-m", "IPython", py_script_path]
    else:
        cmd_args = [py_exec_path, py_script_path]  # '-m', 'IPython',
    return run_cmd_and_check_succ(
        cmd_args, log=log, suc_print=suc_print, return_pipes=True
    )


def log_multi_run_status(run_df):
    num_fails = len(run_df[run_df.success == False])
    print(f"#" * 10 + f"RUN RESULTS {num_fails} Failures!" + "#" * 10)
    i = 0
    for idx, row in run_df[run_df.success == False].iterrows():
        print(f'{"!" * 10} Failure No {i} : {"!" * 10}')
        i += 1
        for col in run_df.columns:
            print(f"{col} : {row[col]}")


def make_modelhub_snippet_log(md_file, suc, proc):
    return {
        "md_file": md_file,
        "success": suc,
        "stdout": proc.stdout.decode(),
        "stderr": proc.stderr.decode(),
    }


# def test_list_of_py_script_path(py_sc)
def test_list_of_py_script_strings(py_script_paths, use_i_py=False):
    total = len(py_script_paths)
    df = []
    for i, p in enumerate(py_script_paths):
        print(f"Testing {i}/{total}")
        df.append(
            execute_py_script_string_as_new_proc(p, file_name=f"{i}_TEST.py"),
            use_i_py=use_i_py,
        )
    return pd.DataFrame(df)
