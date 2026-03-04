---
layout: model
title: Date Regex Matcher Pipeline
author: John Snow Labs
name: date_regex_matcher_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, date, pipeline]
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

This pipeline,  extracts date entities in clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_regex_matcher_pipeline_en_6.3.0_3.4_1772591760399.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_regex_matcher_pipeline_en_6.3.0_3.4_1772591760399.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("date_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("date_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("date_regex_matcher_pipeline", "en", "clinical/models")

val sample_text = """ 
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988.

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk            |   begin |   end | label   |
|:-----------------|--------:|------:|:--------|
| 2081-01-04       |      15 |    24 | DATE    |
| 11.04.1962       |      31 |    40 | DATE    |
| 12-03-1978       |      47 |    56 | DATE    |
| 10.25.23         |      64 |    71 | DATE    |
| Nov 04, 1962     |     106 |   117 | DATE    |
| 04/05/1979       |     148 |   157 | DATE    |
| 15 May           |     185 |   190 | DATE    |
| November 4, 1962 |     238 |   253 | DATE    |
| 11-04-1962       |     294 |   303 | DATE    |
| 25 Sep 2007      |     337 |   347 | DATE    |
| 1988-03-15       |     388 |   397 | DATE    |
| 9/23/1988        |     482 |   490 | DATE    |
| August 14, 2007  |     546 |   560 | DATE    |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_regex_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|7.2 KB|

## Included Models

- DocumentAssembler
- RegexMatcherInternalModel
- ChunkConverter