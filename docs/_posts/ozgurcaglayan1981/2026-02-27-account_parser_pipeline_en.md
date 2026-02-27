---
layout: model
title: Account Number Contextual Parser Pipeline
author: John Snow Labs
name: account_parser_pipeline
date: 2026-02-27
tags: [en, contextualparser, licensed, clinical, account, pipeline]
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

This pipeline, extracts account number entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/account_parser_pipeline_en_6.3.0_3.4_1772230269771.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/account_parser_pipeline_en_6.3.0_3.4_1772230269771.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("account_parser_pipeline", 'en', 'clinical/models')

sample_text = """
Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("account_parser_pipeline", 'en', 'clinical/models')

sample_text = """
Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments.
"""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("account_parser_pipeline", 'en', 'clinical/models')

val sample_text = """
Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments.
"""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|         chunk |   begin |   end | label   |
|--------------:|--------:|------:|:--------|
| 1234567890120 |     121 |   133 | ACCOUNT |
|        123567 |     149 |   154 | ACCOUNT |
| 9876543210987 |     426 |   438 | ACCOUNT |
| 4567890123456 |     488 |   500 | ACCOUNT |
| 7890123456789 |     539 |   551 | ACCOUNT |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|account_parser_pipeline|
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