---
layout: model
title: Pipeline to Summarize Clinical Guidelines
author: John Snow Labs
name: summarizer_clinical_guidelines_large_pipeline
date: 2023-06-22
tags: [licensed, en, clinical, summarization, guidelines]
task: Summarization
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [summarizer_clinical_guidelines_large](https://nlp.johnsnowlabs.com/2023/05/08/summarizer_clinical_guidelines_large_en.html) model.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_guidelines_large_pipeline_en_4.4.4_3.4_1687456058394.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/summarizer_clinical_guidelines_large_pipeline_en_4.4.4_3.4_1687456058394.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("summarizer_clinical_guidelines_large_pipeline", "en", "clinical/models")

text = """Clinical Guidelines for Breast Cancer:

Breast cancer is the most common type of cancer among women. It occurs when the cells in the breast start growing abnormally, forming a lump or mass. This can result in the spread of cancerous cells to other parts of the body. Breast cancer may occur in both men and women but is more prevalent in women.

The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy

Breast cancer may not present symptoms during its early stages. Symptoms typically manifest as the disease progresses. Some notable symptoms include:
- A lump or thickening in the breast or underarm area
- Changes in the size or shape of the breast
- Nipple discharge
- Nipple changes in appearance, such as inversion or flattening
- Redness or swelling in the breast

Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include:
- Surgery (such as lumpectomy or mastectomy)
- Radiation therapy
- Chemotherapy
- Hormone therapy
- Targeted therapy

Early detection is crucial for the successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40. If you notice any changes in your breast tissue, consult with your healthcare provider immediately.
"""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("summarizer_clinical_guidelines_large_pipeline", "en", "clinical/models")

val text = """Clinical Guidelines for Breast Cancer:

Breast cancer is the most common type of cancer among women. It occurs when the cells in the breast start growing abnormally, forming a lump or mass. This can result in the spread of cancerous cells to other parts of the body. Breast cancer may occur in both men and women but is more prevalent in women.

The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy

Breast cancer may not present symptoms during its early stages. Symptoms typically manifest as the disease progresses. Some notable symptoms include:
- A lump or thickening in the breast or underarm area
- Changes in the size or shape of the breast
- Nipple discharge
- Nipple changes in appearance, such as inversion or flattening
- Redness or swelling in the breast

Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include:
- Surgery (such as lumpectomy or mastectomy)
- Radiation therapy
- Chemotherapy
- Hormone therapy
- Targeted therapy

Early detection is crucial for the successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40. If you notice any changes in your breast tissue, consult with your healthcare provider immediately.
"""

val result = pipeline.fullAnnotate(text)
```
</div>



## Results

```bash
Overview of the disease: Breast cancer is the most common type of cancer among women, occurring when the cells in the breast start growing abnormally, forming a lump or mass. It can result in the spread of cancerous cells to other parts of the body. 

Causes: The exact cause of breast cancer is unknown, but several risk factors can increase the likelihood of developing it, such as a personal or family history, a genetic mutation, exposure to radiation, age, early onset of menstruation or late menopause, obesity, and hormonal factors. 

Symptoms: Symptoms of breast cancer typically manifest as the disease progresses, including a lump or thickening in the breast or underarm area, changes in the size or shape of the breast, nipple discharge, nipple changes in appearance, and redness or swelling in the breast. 

Treatment recommendations: Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include surgery, radiation therapy, chemotherapy, hormone therapy, and targeted therapy. Early detection is crucial for successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|summarizer_clinical_guidelines_large_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.9 GB|

## Included Models

- DocumentAssembler
- MedicalSummarizer