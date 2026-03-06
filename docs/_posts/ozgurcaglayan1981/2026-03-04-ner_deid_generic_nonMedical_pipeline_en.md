---
layout: model
title: Detect PHI for Deidentification(Generic) Pipeline
author: John Snow Labs
name: ner_deid_generic_nonMedical_pipeline
date: 2026-03-04
tags: [en, clinical, licensed, deid, ner, phi, generic, pipeline]
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

This pipeline, detects PHI (Protected Health Information) entities for deidentification purposes. It is a generic pipeline capable of detecting various PHI entities such as DATE, NAME, LOCATION, ID, CONTACT, AGE, PROFESSION, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_nonMedical_pipeline_en_6.3.0_3.4_1772642103432.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_nonMedical_pipeline_en_6.3.0_3.4_1772642103432.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_generic_nonMedical_pipeline", "en", "clinical/models")

sample_text = """ 
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("ner_deid_generic_nonMedical_pipeline", "en", "clinical/models")

sample_text = """ 
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("ner_deid_generic_nonMedical_pipeline", "en", "clinical/models")

val sample_text = """ 
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk                   | begin | end | ner_label |
| :---------------------- | ----: | --: | :-------- |
| James Wilson            |     5 |  16 | NAME      |
| 65-year-old             |    23 |  33 | AGE       |
| Boston General Hospital |    85 | 107 | LOCATION  |
| 10/25/2023              |   112 | 121 | DATE      |
| 123 Oak Street          |   137 | 150 | LOCATION  |
| Springfield             |   153 | 163 | LOCATION  |
| IL                      |   166 | 167 | LOCATION  |
| 555-0199                |   199 | 206 | CONTACT   |
| 999-00-1234             |   221 | 231 | ID        |
| Gregory House           |   238 | 250 | NAME      |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_nonMedical_pipeline|
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