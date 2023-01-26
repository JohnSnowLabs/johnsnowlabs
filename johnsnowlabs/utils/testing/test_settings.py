"""
Settings for the JSL-Notebook-Preprocessor

These settings are applied for Pre-Processing on Entire Notebook Cells.
One Notebook consists of multiple Cells and a Cell consists of Multiple Lines seperated by \n
There are 2 Levels of Settings :
Cell Based Rules : Treats entire Cell as a string and applies Rule
Line Based Settings : Applies rule to lines of code in cell individually.

Note:
Lines are derived by splitting on \n are not always valid python code, since actual code can be multi-line
"""

# Print content of cells before running them or not

from johnsnowlabs.utils.testing.nb_nodes import Nodes

print_cell_before_executing = False

inject_header_nodes = [Nodes.imports]

# Applied to entire Cell. Handy when Code appears in Multi-Line Formats (Like Pipeline Definitions)
# Only first Match is applied if multiple keys are matches
sub_string_replacement_cells = {
    # 'spark = jsl.start()': 'spark = nlp.start()',
    # This rule means Replace 'Pipeline(' with 'nlp.Pipeline('
    # 'Pipeline(': 'nlp.Pipeline(',
}

sub_string_replacement_lines = {
    # This rule means if a single line contains '/content/' replace '/content/' with './'
    "/content/": "./",
    # 'spark = jsl.start()': 'spark = nlp.start()',
    # 'spark = jsl.start()': 'spark = nlp.start()',
}

# Hard matches Line Drops
equal_string_drop_lines = [
    # This means if a cell contains a line with 'jsl.install()', drop that line but keep rest of cell
    "nlp.install()",
]

# Hard matches replace
equal_string_replacement_lines = {
    # This means if a cell contains a line equal to 'spark = jsl.start()' replace it with 'spark = nlp.start();from nlp import *'
    # 'spark = nlp.start()': 'spark = nlp.start()',
    "spark = nlp.start()": 'spark = nlp.start(model_cache_folder="/home/ckl/dump/cache_pretrained")',
    # CONVERSION FIXES
}

sub_string_drop_lines = [
    # This means if a line in a cell contains 'files.upload()' drop that line but keep the rest
    "files.upload()",
    # 'get_ipython',
    "pip install",
    "pip -q",
    "from google",
    "google.colab",
    "google.",
    "colab",
    "nlp.install",
    "license_keys",
    "spark_ocr.json",
    "spark_jsl.json",
    "plt.",
]

# These Regexes are applied to the entire cell as very last step, after applying all rules
regex_cell_content_drop_matcher = [
    # This rule means drop any lines matching r'spark = sparkocr.start\(.*?\)' but keep rest of cell intact
    r"spark = sparkocr.start\(.*?\)",
    r"spark = sparknlp_jsl.start\(.*?\)",
]

#### General Testing Configs and Folders
# testing_dir = f'{settings.root_dir}/tmp_tests'
success_worker_print = "$$JSL_TESTING_WORKER_SUC$$"
workshop_git = "https://github.com/JohnSnowLabs/spark-nlp-workshop.git"
testing_dir = (
    "/home/ckl/Documents/freelance/jsl/johnsnowlabs-4-real/tests/test_notebooks/workdir"
)
tmp_notebook_dir = f"{testing_dir}/notebook_tests"
tmp_py_script_dir = f"{testing_dir}/notebook_tests"
tmp_markdown_dir = f"{testing_dir}/markdown_tests"
workshop_local_folder = f"{tmp_notebook_dir}/spark-spark_nlp-workshop"
workshop_cert_nb_folder = (
    f"{workshop_local_folder}/tutorials/Certification_Trainings_JSL"
)
workshop_fin_folder = f"{workshop_cert_nb_folder}/Finance"
workshop_leg_folder = f"{workshop_cert_nb_folder}/Healthcare"
workshop_med_folder = f"{workshop_cert_nb_folder}/Legal"
workshop_pub_folder = f"{workshop_cert_nb_folder}/Public"
testing_work_dir = f"{tmp_notebook_dir}/executed_notebooks"
