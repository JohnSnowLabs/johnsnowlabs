---
layout: model
title: Date of Death Contextual Parser - Pipeline
author: John Snow Labs
name: date_of_death_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, date_of_death, dod, pipeline]
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

This pipeline, extracts date-of-death (DOD) entities in clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_of_death_parser_pipeline_en_6.3.0_3.4_1772586689613.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_of_death_parser_pipeline_en_6.3.0_3.4_1772586689613.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("date_of_death_parser_pipeline", "en", "clinical/models")

sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
Jane Doe was born on November 4, 1962, in London, and she got married on April 5, 1979.
When she got pregnant on May 15, 1979, the doctor wanted to verify her date of birth, which was confirmed to be November 4, 1962.
Jane was 45 years old when she sadly passed away on September 25, 2007.

PROCEDURES:
Patient Jane Doe was evaluated on March 15, 1988, for allergies. She was seen by the endocrinology service and was discharged on September 23, 1988.

MEDICATIONS:
1. Coumadin 1 mg daily. Jane's last INR was measured on August 14, 2007, and it was 2.3."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("date_of_death_parser_pipeline", "en", "clinical/models")

sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
Jane Doe was born on November 4, 1962, in London, and she got married on April 5, 1979.
When she got pregnant on May 15, 1979, the doctor wanted to verify her date of birth, which was confirmed to be November 4, 1962.
Jane was 45 years old when she sadly passed away on September 25, 2007.

PROCEDURES:
Patient Jane Doe was evaluated on March 15, 1988, for allergies. She was seen by the endocrinology service and was discharged on September 23, 1988.

MEDICATIONS:
1. Coumadin 1 mg daily. Jane's last INR was measured on August 14, 2007, and it was 2.3."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("date_of_death_parser_pipeline", "en", "clinical/models")

val sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
Jane Doe was born on November 4, 1962, in London, and she got married on April 5, 1979.
When she got pregnant on May 15, 1979, the doctor wanted to verify her date of birth, which was confirmed to be November 4, 1962.
Jane was 45 years old when she sadly passed away on September 25, 2007.

PROCEDURES:
Patient Jane Doe was evaluated on March 15, 1988, for allergies. She was seen by the endocrinology service and was discharged on September 23, 1988.

MEDICATIONS:
1. Coumadin 1 mg daily. Jane's last INR was measured on August 14, 2007, and it was 2.3."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk              | begin | end | label |
| :----------------- | ----: | --: | :---- |
| 10.25.23           |    64 |  71 | DOD   |
| September 25, 2007 |   360 | 377 | DOD   |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_of_death_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|397.1 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter