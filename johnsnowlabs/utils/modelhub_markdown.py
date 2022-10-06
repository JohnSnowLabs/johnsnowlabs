import os
from pathlib import Path

import pandas as pd

from johnsnowlabs import settings
from johnsnowlabs.utils.file_utils import path_tail
from johnsnowlabs.utils.py_process import execute_py_script_string_as_new_proc

Path(settings.tmp_markdown_dir).mkdir(exist_ok=True, parents=True)


def get_py_snippet_from_modelhub(url):
    import requests
    from bs4 import BeautifulSoup
    # get_py_snippet_from_modelhub('https://nlp.johnsnowlabs.com/2022/09/06/finclf_augmented_esg_en.html')
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    python_code = soup.find_all("div", {"class": "language-python"})[0]
    return python_code.getText()


def modelhub_md_to_pyscript(path):
    start_s = '```python'
    end_s = '```'
    data = []
    started = False
    with open(path, 'r') as f:
        for l in f:
            if start_s in l:
                started = True
                continue
            if end_s in l:
                return data
            if started:
                data.append(l)
    return ['False']


def get_all_py_scripts_in_md_folder(markdown_folder):
    scripts = {}
    for p in os.listdir(markdown_folder):
        # print("TESTING", p)
        if '.md' not in p:
            continue
        script = ''.join(modelhub_md_to_pyscript(f'{markdown_folder}/{p}'))
        if script == 'False':
            print("Badly Formatted Markdown File!", p)
            continue
        scripts[p] = script
    return scripts


def run_modelhub_md_script(md_path_or_url):
    if 'http' and '//' in md_path_or_url:
        return execute_py_script_string_as_new_proc(''.join(get_py_snippet_from_modelhub(md_path_or_url)),
                                                    file_name=path_tail(md_path_or_url))
    return execute_py_script_string_as_new_proc(
        ''.join(modelhub_md_to_pyscript(md_path_or_url)), file_name=path_tail(md_path_or_url))


def test_folder_of_modelhub_md_files(markdown_folder):
    results = []
    scripts = get_all_py_scripts_in_md_folder(markdown_folder)
    total = len(scripts)
    i = 0
    for file, script in scripts.items():
        print('#' * 10 + f'Testing {i}/{total} {file}' + '#' * 10)
        i += 1
        results.append(execute_py_script_string_as_new_proc(script, file_name=file))
    return pd.DataFrame(results)


def test_markdown(file_path_or_url):
    """
    ref can be URL, PATH, DIR,
    """
    if not os.path.exists(file_path_or_url):
        # Remote handling
        if 'http' and '//' in file_path_or_url:
            # URL
            return run_modelhub_md_script(file_path_or_url)
    if os.path.isdir(file_path_or_url):
        # Folder
        return test_folder_of_modelhub_md_files(file_path_or_url)

    if not os.path.isfile(file_path_or_url):
        raise ValueError(f"""Invalid target, must either be: 
                           1. Path to local Notebook
                           2. Path to local Notebook folder
                           3. URL to Remote Notebook (Make sure to use RAW github URL) 
                           4. WORKSHOP, WORKSHOP-OS, WORKSHOP-MED, WORKSHOP-LEG, WORKSHOP-FIN 
                           """)
    # PATH
    return run_modelhub_md_script(file_path_or_url)
