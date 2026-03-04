---
layout: model
title: Age Contextual Parser Pipeline
author: John Snow Labs
name: age_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, age, pipeline]
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

This pipeline, extracts age entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/age_parser_pipeline_en_6.3.0_3.4_1772585633645.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/age_parser_pipeline_en_6.3.0_3.4_1772585633645.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("age_parser_pipeline", "en", "clinical/models")

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.

A 28 year old female with a history of gestational diabetes mellitus diagnosed 8 years ago.
3 years ago, he reported an episode of HTG-induced pancreatitis. 5 months old boy with repeated concussions.
A 45-year-old patient was admitted for routine examination.
The 72 years old man presented with chest pain."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("age_parser_pipeline", "en", "clinical/models")

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.

A 28 year old female with a history of gestational diabetes mellitus diagnosed 8 years ago.
3 years ago, he reported an episode of HTG-induced pancreatitis. 5 months old boy with repeated concussions.
A 45-year-old patient was admitted for routine examination.
The 72 years old man presented with chest pain."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("age_parser_pipeline", "en", "clinical/models")

val sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13.
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, VIN 4Y1SL65848Z411439, VIN 1HGCM82633A123456 - VIN JH4KA7560MC012345 - VIN 5YJSA1E14HF123456
SSN #333-44-6666, Driver's license no: A334455B, plate 34NLP34. Lic: 12345As. Cert: 12345As
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.

A 28 year old female with a history of gestational diabetes mellitus diagnosed 8 years ago.
3 years ago, he reported an episode of HTG-induced pancreatitis. 5 months old boy with repeated concussions.
A 45-year-old patient was admitted for routine examination.
The 72 years old man presented with chest pain."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk        |   begin |   end | label   |
|:-------------|--------:|------:|:--------|
| 60-year-old  |     119 |   129 | AGE     |
| 28 year old  |     501 |   511 | AGE     |
| 5 months old |     656 |   667 | AGE     |
| 45-year-old  |     702 |   712 | AGE     |
| 72 years old |     764 |   775 | AGE     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|age_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|396.6 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter