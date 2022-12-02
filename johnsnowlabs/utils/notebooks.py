import os
import shutil
import urllib
from pathlib import Path
from pprint import pprint
from typing import Union, List
import pandas as pd
from nbclient.exceptions import CellExecutionError
from nbconvert import PythonExporter

import johnsnowlabs.utils.testing.test_settings
from johnsnowlabs.utils.file_utils import path_tail
from johnsnowlabs.utils.py_process import str_to_file, log_multi_run_status
import nbformat
from johnsnowlabs.utils.testing.jsl_pre_processor import JslPreprocessor

Path(johnsnowlabs.utils.testing.test_settings.tmp_notebook_dir).mkdir(exist_ok=True, parents=True)


def nbformat_to_ipynb(out_path, nb):
    with open(out_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)


def ipynb_to_nbformat(in_path):
    with open(in_path) as f:
        return nbformat.read(f, as_version=4)


def get_all_nb_in_local_folder(p):
    ## filter all files ending in .ipynb
    return [f'{p}/{f}' for f in os.listdir(p) if '.ipynb' in f]


def convert_notebook(notebookPath):
    out_path = f'{johnsnowlabs.utils.testing.test_settings.tmp_notebook_dir}/{path_tail(notebookPath)}.nb_converted.py'
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


def test_ipynb(file_path_or_url: Union[List[str], str], use_i_py=True, model_cache_dir=None, out_dir=None,
               branch='master'):
    """
    ref can be URL, PATH, DIR,
    or ref= `WORKSHOP` or `WORKSHOP-OS`  or `WORKSHOP-MED` , `WORKSHOP-LEG`, `WORKSHOP-FIN`
        for testing a specific sub-folder of the workshop
    use branch parameter to test a specific branch
    """
    if out_dir:
        os.chdir(out_dir)
    if isinstance(file_path_or_url, List):
        return test_list_of_ipynb(file_path_or_url, out_dir=out_dir)

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
            if not os.path.exists(johnsnowlabs.utils.testing.test_settings.workshop_cert_nb_folder):
                # Clone repo
                cur_dir = os.getcwd()
                os.chdir(f'{johnsnowlabs.utils.testing.test_settings.tmp_notebook_dir}')
                os.system(f'git clone {johnsnowlabs.utils.testing.test_settings.workshop_git} -b {branch}')
                os.chdir(cur_dir)
            if 'WORKSHOP-FIN' == file_path_or_url:
                return test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_fin_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir, out_dir=out_dir)
            if 'WORKSHOP-LEG' == file_path_or_url:
                return test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_leg_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir, out_dir=out_dir)
            if 'WORKSHOP-MED' == file_path_or_url:
                return test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_med_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir, out_dir=out_dir)
            if 'WORKSHOP-PUB' == file_path_or_url:
                return test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_pub_folder, use_i_py=use_i_py,
                                         model_cache_dir=model_cache_dir, out_dir=out_dir)

            return pd.concat(
                [test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_leg_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_fin_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_med_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir),
                 test_ipynb_folder(johnsnowlabs.utils.testing.test_settings.workshop_pub_folder, use_i_py=use_i_py, model_cache_dir=model_cache_dir), ])

    if os.path.isdir(file_path_or_url):
        # Folder
        return test_ipynb_folder(file_path_or_url, use_i_py=use_i_py, model_cache_dir=model_cache_dir, out_dir=out_dir)

    if not os.path.isfile(file_path_or_url):
        raise ValueError(f"""Invalid target, must either be: 
                           1. Path to local Notebook
                           2. Path to local Notebook folder
                           3. URL to Remote Notebook (Make sure to use RAW github URL) 
                           4. WORKSHOP, WORKSHOP-OS, WORKSHOP-MED, WORKSHOP-LEG, WORKSHOP-FIN 
                           """)

    if not out_dir:
        out_dir = file_path_or_url + '_EXECUTED.ipynb'
    else:
        out_dir = f'{out_dir}/{path_tail(file_path_or_url)}'
    result = execute_nb_as_nb(file_path_or_url, out_dir)
    return result


def test_ipynb_folder(nb_folder, work_dir=os.getcwd(), log=True, model_cache_dir=None, use_i_py=True, out_dir=None):
    return test_list_of_ipynb(
        get_all_nb_in_local_folder(nb_folder), work_dir, log, model_cache_dir=model_cache_dir, out_dir=out_dir,
        use_i_py=use_i_py)


def test_list_of_ipynb(nb_paths_or_urls, work_dir=os.getcwd(), log=True, model_cache_dir=None, use_i_py=True,
                       out_dir=None):
    df = []
    for i, nb_path in enumerate(nb_paths_or_urls):
        print(f'Testing {i}/{len(nb_paths_or_urls)} {nb_path}')
        df.append(
            test_ipynb(file_path_or_url=nb_path, model_cache_dir=model_cache_dir, use_i_py=use_i_py, out_dir=out_dir))
    df = pd.DataFrame(df)
    if log:
        log_multi_run_status(df)
    return df


def execute_nb_as_nb(nb_path, out_file, work_dir=None):
    # Execute Notebook with custom JSL Preprocessor
    if not work_dir:
        work_dir = johnsnowlabs.utils.testing.test_settings.testing_work_dir
    Path(johnsnowlabs.utils.testing.test_settings.testing_work_dir, ).mkdir(exist_ok=True, parents=True)

    nb_name = nb_path.split('/')[-1]
    # Load file, Pre-Process and Write new File to Disk
    nb = ipynb_to_nbformat(nb_path)
    ep = JslPreprocessor(timeout=600, kernel_name='python3', allow_errors=True)
    failed = False
    exception_message = None
    try:
        ep.preprocess(nb, {'metadata': {'path': work_dir}})
        nbformat_to_ipynb(out_file, nb)
    except CellExecutionError as err:
        exception_message = err
        print(f'🚨 Failure Executing notebook cell \n{err}', )
        nbformat_to_ipynb(out_file, nb)
    except Exception as err:
        exception_message = err
        print(f'🚨 Unknown Exception while trying to run Notebook  \n{err}', )
        nbformat_to_ipynb(out_file, nb)
    if exception_message:
        failed = True

    bad_cells = []
    code_cells = list(filter(lambda x: x['cell_type'] == 'code', nb['cells']))
    for cell in code_cells:
        if 'outputs' in cell:
            for cell_output in cell['outputs']:
                if cell_output['output_type'] == 'error':
                    bad_cells.append(make_nbconvert_exec_log(bad_cell_content=cell['source'],
                                                             error_output_type=cell_output['output_type'],
                                                             error_name=cell_output['ename'],
                                                             error_value=cell_output['evalue'],
                                                             error_traceback='\n'.join(cell_output['traceback'])))

                    print(f"\n🚨 Failure Executing Cell!  in {out_file}\n", )
                    pprint(bad_cells[-1])
    success = len(bad_cells) == 0
    if not success:
        print(f'🚨 Failures in Notebook {nb_name} ')
    else:
        print(f'👌 No Failures in Notebook {nb_name} ')

    return make_nb_run_log(
        nb_name=nb_name,
        success=success,
        out_file=out_file,
        failed_cells_logs=bad_cells, )


def make_nbconvert_exec_log(bad_cell_content, error_output_type, error_name, error_value, error_traceback):
    # Log for failed Cells
    return {
        'bad_cell_content': bad_cell_content,
        'error_output_type': error_output_type,
        'error_name': error_name,
        'error_value': error_value,
        'error_traceback': error_traceback
    }
    pass


def make_nb_run_log(nb_name, success, out_file, failed_cells_logs):
    return {
        'success': success,
        'nb_name': nb_name,
        'output_notebook_path': out_file,
        'failed_cells_logs': failed_cells_logs,

    }
