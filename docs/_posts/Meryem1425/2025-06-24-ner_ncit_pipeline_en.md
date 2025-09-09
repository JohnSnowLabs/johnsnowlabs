---
layout: model
title: Pipeline for Extracting Clinical Entities Related to NCI-t Codes
author: John Snow Labs
name: ner_ncit_pipeline
date: 2025-06-24
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to NCI-t codes.

1 NER model and a Text Matcher are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_ncit_pipeline_en_6.0.2_3.4_1750794269667.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_ncit_pipeline_en_6.0.2_3.4_1750794269667.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_ncit_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, 
total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. 
Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). 
Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_ncit_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
A 65-year-old woman had a history of debulking surgery, bilateral oophorectomy with omentectomy, 
total hysterectomy with radical pelvic lymph nodes dissection due to ovarian carcinoma (mucinous-type carcinoma, stage Ic) 1 year ago. 
Patient's medical compliance was poor and failed to complete her chemotherapy (cyclophosphamide 750 mg/m2, carboplatin 300 mg/m2). 
Recently, she noted a palpable right breast mass, 15 cm in size which nearly occupied the whole right breast in 2 months. Core needle biopsy revealed metaplastic carcinoma.
""")

```
</div>

## Results

```bash
|    | chunks                                |   begin |   end | entities       |
|---:|:--------------------------------------|--------:|------:|:---------------|
|  0 | debulking surgery                     |      38 |    54 | Cancer_Surgery |
|  1 | bilateral oophorectomy                |      57 |    78 | Cancer_Surgery |
|  2 | omentectomy                           |      85 |    95 | Cancer_Surgery |
|  3 | total hysterectomy                    |      99 |   116 | Cancer_Surgery |
|  4 | radical pelvic lymph nodes dissection |     123 |   159 | Cancer_Surgery |
|  5 | ovarian carcinoma                     |     168 |   184 | Cancer_dx      |
|  6 | mucinous-type carcinoma               |     187 |   209 | Cancer_dx      |
|  7 | stage Ic                              |     212 |   219 | Staging        |
|  8 | chemotherapy                          |     300 |   311 | Chemotherapy   |
|  9 | cyclophosphamide                      |     314 |   329 | Chemotherapy   |
| 10 | carboplatin                           |     342 |   352 | Chemotherapy   |
| 11 | right                                 |     398 |   402 | Direction      |
| 12 | breast                                |     404 |   409 | Site_Breast    |
| 13 | mass                                  |     411 |   414 | Tumor_Finding  |
| 14 | right                                 |     463 |   467 | Direction      |
| 15 | breast                                |     469 |   474 | Site_Breast    |
| 16 | Core needle biopsy                    |     489 |   506 | Pathology_Test |
| 17 | metaplastic carcinoma                 |     517 |   537 | Cancer_dx      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_ncit_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- ChunkMergeModel