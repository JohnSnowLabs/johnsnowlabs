---
layout: model
title: Pipeline to Detect Oncology-Specific Entities
author: John Snow Labs
name: ner_oncology_pipeline
date: 2024-01-08
tags: [licensed, en, oncology, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_oncology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_pipeline_en_5.2.0_3.4_1704725635028.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_pipeline_en_5.2.0_3.4_1704725635028.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_oncology_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. He underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_oncology_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. He underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first line therapy.""")

```
</div>

## Results

```bash
|    | chunks                         |   begin |   end | entities              |
|---:|:-------------------------------|--------:|------:|:----------------------|
|  0 | left                           |      31 |    34 | Direction             |
|  1 | mastectomy                     |      36 |    45 | Cancer_Surgery        |
|  2 | axillary lymph node dissection |      54 |    83 | Cancer_Surgery        |
|  3 | left                           |      91 |    94 | Direction             |
|  4 | breast cancer                  |      96 |   108 | Cancer_Dx             |
|  5 | twenty years ago               |     110 |   125 | Relative_Date         |
|  6 | tumor                          |     132 |   136 | Tumor_Finding         |
|  7 | positive                       |     142 |   149 | Biomarker_Result      |
|  8 | ER                             |     155 |   156 | Biomarker             |
|  9 | PR                             |     162 |   163 | Biomarker             |
| 10 | radiotherapy                   |     183 |   194 | Radiotherapy          |
| 11 | breast                         |     229 |   234 | Site_Breast           |
| 12 | cancer                         |     241 |   246 | Cancer_Dx             |
| 13 | recurred                       |     248 |   255 | Response_To_Treatment |
| 14 | right                          |     262 |   266 | Direction             |
| 15 | lung                           |     268 |   271 | Site_Lung             |
| 16 | metastasis                     |     273 |   282 | Metastasis            |
| 17 | 13 years later                 |     284 |   297 | Relative_Date         |
| 18 | He                             |     300 |   301 | Gender                |
| 19 | adriamycin                     |     337 |   346 | Chemotherapy          |
| 20 | 60 mg/m2                       |     349 |   356 | Dosage                |
| 21 | cyclophosphamide               |     363 |   378 | Chemotherapy          |
| 22 | 600 mg/m2                      |     381 |   389 | Dosage                |
| 23 | six courses                    |     397 |   407 | Cycle_Count           |
| 24 | first line                     |     413 |   422 | Line_Of_Therapy       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
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
- NerConverter
