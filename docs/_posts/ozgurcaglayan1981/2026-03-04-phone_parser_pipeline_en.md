---
layout: model
title: Phone Number Contextual Parser Pipeline
author: John Snow Labs
name: phone_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, phone, pipeline]
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

This pipeline, extracts phone entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phone_parser_pipeline_en_6.3.0_3.4_1772587885060.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phone_parser_pipeline_en_6.3.0_3.4_1772587885060.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("phone_parser_pipeline", "en", "clinical/models")

sample_text = """ Record date :2093-01-13, David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.
Phone: (818) 342-7353.
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("phone_parser_pipeline", "en", "clinical/models")

sample_text = """ Record date :2093-01-13, David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.
Phone: (818) 342-7353.
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("phone_parser_pipeline", "en", "clinical/models")

val sample_text = """ Record date :2093-01-13, David Hale, M.D. IP 203.120.223.13.
ID: 1231511863, The driver's license no:A334455B and e-mail: hale@gmail.com .
PCP : Oliveira, 25 years-old, Jake 5 year old, Record date : 2079-11-09.
Cocke County Baptist Hospital , 0295 Keats Street, 12345, TX 55555-4444. Phone: (818) 342-7353 Fax No.: (818) 342-7354, SSN# 332255677, The other is ssN: 333-44-6666.
Phone: (818) 342-7353.
Email: medunites@firsthospital.com
Emergency contact phone: (555) 123-4567.
Additional phone number: (310) 987-6543."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk          |   begin |   end | label   |
|:---------------|--------:|------:|:--------|
| (818) 342-7353 |     292 |   305 | PHONE   |
| (818) 342-7354 |     316 |   329 | PHONE   |
| (818) 342-7353 |     386 |   399 | PHONE   |
| (555) 123-4567 |     462 |   475 | PHONE   |
| (310) 987-6543 |     503 |   516 | PHONE   |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phone_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|396.8 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter