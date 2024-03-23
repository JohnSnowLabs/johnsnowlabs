---
layout: docs
seotitle: NLP | John Snow Labs
title: Utilities for Testing Notebooks
permalink: /docs/en/jsl/testing-utils-notebooks
key: docs-install
modify_date: "2020-05-26"
header: true
show_nav: true
sidebar:
    nav: jsl
---



<div class="main-docs" markdown="1"><div class="h3-box" markdown="1">

You can use the John Snow Labs library to automatically test 10000+ models and 100+ Notebooks in 1 line of code within
a small machine like a **single Google Colab Instance** and generate very handy error reports of potentially broken Models, Notebooks or Models hub Markdown Snippets.

You can test the following things with the `test_ipynb()` function :


- A `local` .ipynb file
- a `remote` .ipynb URL, point to RAW githubuser content URL of the file when using git.
- a `local` folder of ipynb files, generates report
- a `list` of local paths or urls to .ipynb files. Generates a Report
- The entire [John Snow Labs Workshop Certification Folder](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings) Generates a Report 
- A sub-folder of the [John Snow Labs Workshop Certification Folder](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/tutorials/Certification_Trainings) , i.e. only OCR or only Legal. Generates a Report



The generated Test-Report Pandas Dataframe has the columns:

| Report Column | Description                                                                                                                         | 
|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `test_script` | is the generated script for testing. If you think the notebook should not crash, check the file, there could be a generation error. |
| `stderr`      | Error logs of process ran. Print this to easily read                                                                                |
| `stdout`      | Standard Print logs of process ran. Print this to easily read                                                                       |
| `success`     | True if script ran successfully from top to bottom                                                                                  |
| `notebook`    | The Source notebook for testing                                                                                                     |

</div><div class="h3-box" markdown="1">

### Test a Local Notebook

```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_ipynb('path/to/local/notebook.ipynb')
```

</div><div class="h3-box" markdown="1">

### Test a Remote Notebook

```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_ipynb('https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Certification_Trainings/Healthcare/5.Spark_OCR.ipynb',)
```

</div><div class="h3-box" markdown="1">

### Test a Folder with Notebooks
This will scan the folder for all files ending with `.ipynb` , test them and generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_ipynb('my/notebook/folder')
```

</div><div class="h3-box" markdown="1">

### Test a List of Notebook References
Can be mixed with Urls and paths, will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
nb_to_test = [
  'https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Certification_Trainings/Healthcare/5.Spark_OCR.ipynb',
  'path/to/local/notebook.ipynb',]
test_ipynb(nb_to_test)
```

</div><div class="h3-box" markdown="1">

### Run All Certification Notebooks
Will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_result = test_ipynb('WORKSHOP')
```

</div><div class="h3-box" markdown="1">

### Run Finance Certification Notebooks only
Will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_result = test_ipynb('WORKSHOP-FIN')
```

</div><div class="h3-box" markdown="1">

### Run Legal notebooks only
Will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_result = test_ipynb('WORKSHOP-LEG')
```

</div><div class="h3-box" markdown="1">

### Run Medical notebooks only
Will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_result = test_ipynb('WORKSHOP-MED')
```

</div><div class="h3-box" markdown="1">

### Run Open Source notebooks only
Will generate a report
```python
from johnsnowlabs.utils.notebooks import test_ipynb
test_result = test_ipynb('WORKSHOP-OS')
```

</div></div>