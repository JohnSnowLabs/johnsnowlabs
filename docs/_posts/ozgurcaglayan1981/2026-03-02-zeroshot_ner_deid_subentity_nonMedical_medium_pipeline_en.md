---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_deid_subentity_nonMedical_medium) - Pipeline
author: John Snow Labs
name: zeroshot_ner_deid_subentity_nonMedical_medium_pipeline
date: 2026-03-02
tags: [en, ner, deid, licensed, clinical, zeroshot, subentity, pipeline]
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

This pipeline implements Zero-shot Named Entity Recognition (NER) using a pre-trained language model with contextual understanding. It enables entity extraction across different domains without task-specific fine-tuning.

Unlike fully flexible zero-shot setups, this pipeline operates with a fixed label schema to ensure consistent and standardized outputs. The supported entity labels are:

"ACCOUNTNUM", "AGE", "CITY", "COUNTRY", "DATE", "DEVICE", "DLN", "DOCTOR", "EMAIL", "GENDER", "HOSPITAL", "IDNUM", "IP", "LOCATION_OTHER", "MEDICALRECORD", "NAME", "ORGANIZATION", "PATIENT", "PHONE", "PLATE", "PROFESSION", "SSN", "STATE", "STREET", "TIME", "URL", "USERNAME", "VIN", "ZIP"

All predictions are restricted to this predefined set of labels. This design ensures production stability, output consistency, and reliable performance within the defined entity scope.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_medium_pipeline_en_6.3.0_3.4_1772491967828.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_deid_subentity_nonMedical_medium_pipeline_en_6.3.0_3.4_1772491967828.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_medium_pipeline", "en", "clinical/models")

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

pipeline = nlp.PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_medium_pipeline", "en", "clinical/models")

sample_text = """ 
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023. 
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199. 
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zeroshot_ner_deid_subentity_nonMedical_medium_pipeline", "en", "clinical/models")

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

| chunk                   | begin | end | ner_label | confidence |
| :---------------------- | ----: | --: | :-------- | ---------: |
| James Wilson            |     5 |  16 | PATIENT   |  0.9983292 |
| 65-year-old             |    23 |  33 | AGE       | 0.99516994 |
| male                    |    35 |  38 | GENDER    |  0.9980227 |
| Boston General Hospital |    85 | 107 | HOSPITAL  | 0.99748915 |
| 10/25/2023              |   112 | 121 | DATE      |  0.9826188 |
| 123 Oak Street          |   137 | 150 | STREET    | 0.99730396 |
| Springfield             |   153 | 163 | CITY      |  0.9925425 |
| IL                      |   166 | 167 | STATE     |  0.9956291 |
| 62704                   |   169 | 173 | ZIP       |  0.9997737 |
| 555-0199                |   199 | 206 | PHONE     |  0.9964192 |
| 999-00-1234             |   221 | 231 | SSN       |  0.9997788 |
| Gregory House           |   238 | 250 | DOCTOR    |  0.9921366 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_deid_subentity_nonMedical_medium_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|789.8 MB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PretrainedZeroShotNER
- NerConverterInternalModel