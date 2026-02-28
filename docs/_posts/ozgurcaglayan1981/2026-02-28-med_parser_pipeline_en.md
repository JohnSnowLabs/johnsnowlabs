---
layout: model
title: Medical Record Contextual Parser Pipeline
author: John Snow Labs
name: med_parser_pipeline
date: 2026-02-28
tags: [en, contextualparser, licensed, clinical, medical_record, pipeline]
task: [Contextual Parser, Pipeline Healthcare]
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

This pipeline, extracts medical_record entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/med_parser_pipeline_en_6.3.0_3.4_1772239803654.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/med_parser_pipeline_en_6.3.0_3.4_1772239803654.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("med_parser_pipeline", "en", "clinical/models")

sample_text = """ Month DD, YYYY
XYZ
RE: ABC
MEDICAL RECORD#: 12332
MRN: 1233567
MEDICAL RECORD#: 45678
MRN: 9876543
MEDICAL RECORD#: 11111
Dear Dr. XYZ:

I saw ABC back in Neuro-Oncology Clinic today."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("med_parser_pipeline", "en", "clinical/models")

sample_text = """ Month DD, YYYY
XYZ
RE: ABC
MEDICAL RECORD#: 12332
MRN: 1233567
MEDICAL RECORD#: 45678
MRN: 9876543
MEDICAL RECORD#: 11111
Dear Dr. XYZ:

I saw ABC back in Neuro-Oncology Clinic today."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("med_parser_pipeline", "en", "clinical/models")

val sample_text = """ Month DD, YYYY
XYZ
RE: ABC
MEDICAL RECORD#: 12332
MRN: 1233567
MEDICAL RECORD#: 45678
MRN: 9876543
MEDICAL RECORD#: 11111
Dear Dr. XYZ:

I saw ABC back in Neuro-Oncology Clinic today."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|   chunk |   begin |   end | label         |
|--------:|--------:|------:|:--------------|
|   12332 |      44 |    48 | MEDICALRECORD |
| 1233567 |      55 |    61 | MEDICALRECORD |
|   45678 |      80 |    84 | MEDICALRECORD |
| 9876543 |      91 |    97 | MEDICALRECORD |
|   11111 |     116 |   120 | MEDICALRECORD |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|med_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|397.0 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter