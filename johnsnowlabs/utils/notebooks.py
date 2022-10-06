import os
import shutil
import urllib
from pathlib import Path
from typing import Union, List

import nbformat
import pandas as pd
from nbconvert import PythonExporter

from johnsnowlabs import settings
from johnsnowlabs.utils.file_utils import str_to_file, path_tail
from johnsnowlabs.utils.py_process import str_to_file, execute_py_script_as_new_proc, log_multi_run_status

Path(settings.tmp_notebook_dir, ).mkdir(exist_ok=True, parents=True)


def clean_workshop_notebook(py_script_path, suc_print=settings.success_worker_print, work_dir=os.getcwd(),
                            model_cache_dir=None):
    out_path = f'{settings.tmp_notebook_dir}/{path_tail(py_script_path)}___CLEANED.py'
    prefix = f"""
import os 
os.chdir('{work_dir}')
from johnsnowlabs import *
"""
    if model_cache_dir:
        prefix = prefix + f"""
spark =  jsl.start(model_cache_folder='{model_cache_dir}')
        """
    else:
        prefix = prefix + f"""
spark = jsl.start()
        """

    suffix = f"""
print('{suc_print}')    
"""

    # Substring matches
    bad_sub_strings = [
        'files.upload()',
        # 'get_ipython',
        'pip install',
        'pip -q',
        'from google',
        'google.',
        'colab',
        'jsl.install',
        '#',
        'license_keys',
        'spark_ocr.json',
        'spark_jsl.json',
        'plt.',
        # 'sparkocr.start',
        # 'secret',
        # 'nlp_version',
        # 'nlp_secret',
        # 'nlp_internal',

    ]
    # Full file will be matched for those in the end and the will be removed
    bad_regex_full_match = [
        r'spark = sparkocr.start\(.*?\)',
        r'spark = sparknlp_jsl.start\(.*?\)'
    ]

    import re
    # Hard matches
    bad_lines = [  # '\n',
        'jsl.install()',
    ]
    new_file = []
    with open(py_script_path, "r") as f:
        for l in f:
            if any(s in l for s in bad_sub_strings): continue
            if '/content/' in l: l = l.replace('/content/', './')
            if l in bad_lines: continue
            # if 'get_ipython().system' in l:
            #     l = l.replace('get_ipython()', 'os')
            # if 'get_ipython().run_line_magic' in l:
            #     continue

            new_file.append(l)
    new_file = prefix + ''.join(new_file) + suffix

    matches_to_clean = [re.findall(r, new_file, re.DOTALL) for r in bad_regex_full_match]

    def flatten(l):
        return [item for sublist in l for item in sublist]

    for m in flatten(matches_to_clean): new_file = new_file.replace(m, '')
    # print(new_file)
    str_to_file(new_file, out_path)
    return out_path


def get_all_nb_in_local_folder(p):
    ## filter all files ending in .ipynb
    return [f'{p}/{f}' for f in os.listdir(p) if '.ipynb' in f]


def convert_notebook(notebookPath):
    out_path = f'{settings.tmp_notebook_dir}/{path_tail(notebookPath)}.nb_converted.py'
    with open(notebookPath) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
    exporter = PythonExporter()
    source, meta = exporter.from_notebook_node(nb)
    str_to_file(source, out_path)
    return out_path


def convert_all_notebooks(nb_folder):
    # Convert a folder which contains .ipynb into .py
    store_folder = f'{nb_folder}/nb_converted/'
    Path(store_folder).mkdir(parents=True, exist_ok=True)
    for nb_path in get_all_nb_in_local_folder(nb_folder):
        save_path = store_folder + nb_path.split('/')[-1] + '.py'
        convert_notebook(nb_path, save_path)


def test_ipynb(file_path_or_url: Union[List[str], str], use_i_py=True, model_cache_dir=None):
    """
    ref can be URL, PATH, DIR,
    or ref= `WORKSHOP` or `WORKSHOP-OS`  or `WORKSHOP-MED` , `WORKSHOP-LEG`, `WORKSHOP-FIN`
        for testing a specific sub-folder of the workshop
    """
    # TODO add GIT BRANCH?!?!
    if not os.path.exists(file_path_or_url):
        # Remote handling
        if 'http' and '//' in file_path_or_url:
            # URL
            file_name = file_path_or_url.split('/')[-1]
            print(f'Downloading {file_path_or_url} to  {file_name}')
            # Download the file from `url` and save it locally under `file_name`:
            with urllib.request.urlopen(file_path_or_url) as response, open(file_name, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                file_path_or_url = file_name

        elif 'WORKSHOP' in file_path_or_url:
            # Workshop handing
            if not os.path.exists(settings.workshop_cert_nb_folder):
                # Clone repo
                cur_dir = os.getcwd()
                os.chdir(f'{settings.tmp_notebook_dir}')
                os.system(f'git clone {settings.workshop_git}')
                os.chdir(cur_dir)
            if 'WORKSHOP-FIN' == file_path_or_url:
                return test_ipynb_folder(settings.workshop_fin_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir)
            if 'WORKSHOP-LEG' == file_path_or_url:
                return test_ipynb_folder(settings.workshop_leg_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir)
            if 'WORKSHOP-MED' == file_path_or_url:
                return test_ipynb_folder(settings.workshop_med_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir)
            if 'WORKSHOP-PUB' == file_path_or_url:
                return test_ipynb_folder(settings.workshop_pub_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir)

            return pd.concat(
                [test_ipynb_folder(settings.workshop_leg_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(settings.workshop_fin_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(settings.workshop_med_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(settings.workshop_pub_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir), ])

    if os.path.isdir(file_path_or_url):
        # Folder
        return test_ipynb_folder(file_path_or_url, use_i_py=use_i_py, model_cache_dir=model_cache_dir)

    if not os.path.isfile(file_path_or_url):
        raise ValueError(f"""Invalid target, must either be: 
                           1. Path to local Notebook
                           2. Path to local Notebook folder
                           3. URL to Remote Notebook (Make sure to use RAW github URL) 
                           4. WORKSHOP, WORKSHOP-OS, WORKSHOP-MED, WORKSHOP-LEG, WORKSHOP-FIN 
                           """)
    # PATH
    nb_converted_path = convert_notebook(file_path_or_url)
    final_py_script_path = clean_workshop_notebook(py_script_path=nb_converted_path,
                                                   model_cache_dir=model_cache_dir)

    succ, proc = execute_py_script_as_new_proc(py_script_path=final_py_script_path, use_i_py=use_i_py)
    return make_log(file_path_or_url, succ, proc, final_py_script_path)


def test_ipynb_folder(nb_folder, work_dir=os.getcwd(), log=True, model_cache_dir=None, use_i_py=True):
    return pd.DataFrame(
        test_list_of_ipynb(get_all_nb_in_local_folder(nb_folder), work_dir, log, model_cache_dir=model_cache_dir,
                           use_i_py=use_i_py))


def test_list_of_ipynb(nb_paths_or_urls, work_dir=os.getcwd(), log=True, model_cache_dir=None, use_i_py=True):
    df = []
    for i, nb_path in enumerate(nb_paths_or_urls):
        print(f'Testing {i}/{len(nb_paths_or_urls)} {nb_path}')
        df.append(test_ipynb(file_path_or_url=nb_path, model_cache_dir=model_cache_dir, use_i_py=use_i_py))
    df = pd.DataFrame(df)
    if log:
        log_multi_run_status(df)
    return df


def make_log(nb_file, suc, proc, final_py_script):
    return {
        'notebook': nb_file,
        'success': suc,
        'stdout': proc.stdout.decode(),
        'stderr': proc.stderr.decode(),
        'test_script': final_py_script}
