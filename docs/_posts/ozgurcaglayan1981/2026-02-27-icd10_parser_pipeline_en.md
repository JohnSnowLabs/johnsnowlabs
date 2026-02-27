---
layout: model
title: ICD10 Contextual Parser Pipeline
author: John Snow Labs
name: icd10_parser_pipeline
date: 2026-02-27
tags: [en, contextualparser, licensed, clinical, icd10, pipeline]
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

This pipeline, extracts icd10 entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10_parser_pipeline_en_6.3.0_3.4_1772230773796.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10_parser_pipeline_en_6.3.0_3.4_1772230773796.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10_parser_pipeline", 'en', 'clinical/models')

sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A.
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("icd10_parser_pipeline", 'en', 'clinical/models')

sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A.
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("icd10_parser_pipeline", 'en', 'clinical/models')

val sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A.
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk    |   begin |   end | label       |
|:---------|--------:|------:|:------------|
| A334455B |     169 |   176 | ICD10_CODE  |
| E11.9    |     774 |   778 | ICD10_CODE  |
| I10      |     976 |   978 | ICD10_CODE  |
| N18.3    |    1229 |  1233 | ICD10_CODE  |
| J45.909  |    1318 |  1324 | ICD10_CODE  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10_parser_pipeline|
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