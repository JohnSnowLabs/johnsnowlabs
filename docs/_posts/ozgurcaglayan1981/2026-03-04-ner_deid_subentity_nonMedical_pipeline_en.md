---
layout: model
title: Detect PHI for Deidentification (Subentity) Pipeline
author: John Snow Labs
name: ner_deid_subentity_nonMedical_pipeline
date: 2026-03-04
tags: [en, clinical, licensed, deid, ner, phi, subentity, pipeline]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline, detects PHI (Protected Health Information) entities for deidentification purposes. It is a subentity pipeline capable of detecting various PHI entities with granular labels such as PATIENT, DOCTOR, HOSPITAL, STREET, CITY, ZIP, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_nonMedical_pipeline_en_6.3.0_3.4_1772642476036.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_nonMedical_pipeline_en_6.3.0_3.4_1772642476036.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_subentity_nonMedical_pipeline", "en", "clinical/models")

sample_text = """ 
Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA.
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729.
She works as a Nurse at City General Hospital. Her account number is 8003591.
She has an appointment scheduled for March 15, 2024 at 10:30 AM.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("ner_deid_subentity_nonMedical_pipeline", "en", "clinical/models")

sample_text = """ 
Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA.
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729.
She works as a Nurse at City General Hospital. Her account number is 8003591.
She has an appointment scheduled for March 15, 2024 at 10:30 AM.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("ner_deid_subentity_nonMedical_pipeline", "en", "clinical/models")

val sample_text = """ 
Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA.
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729.
She works as a Nurse at City General Hospital. Her account number is 8003591.
She has an appointment scheduled for March 15, 2024 at 10:30 AM.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                                     | begin | end | ner_label |
| :---------------------------------------- | ----: | --: | :-------- |
| Emily Davis                               |     1 |  11 | NAME      |
| 34-year-old                               |    16 |  26 | AGE       |
| Female                                    |    28 |  33 | GENDER    |
| Michael Johnson                           |    40 |  54 | DOCTOR    |
| CarePlus Clinic                           |    74 |  88 | HOSPITAL  |
| 456 Elm Street                            |   102 | 115 | STREET    |
| NewYork                                   |   118 | 124 | CITY      |
| NY                                        |   127 | 128 | STATE     |
| 10001                                     |   130 | 134 | ZIP       |
| USA                                       |   137 | 139 | COUNTRY   |
| 555-642-1725                              |   165 | 176 | PHONE     |
| [davis@gmail.com](mailto:davis@gmail.com) |   197 | 211 | EMAIL     |
| 725-46-2729                               |   225 | 235 | SSN       |
| City General Hospital                     |   263 | 283 | HOSPITAL  |
| March 15, 2024                            |   355 | 368 | DATE      |
| 10:30 AM                                  |   373 | 380 | TIME      |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_nonMedical_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
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