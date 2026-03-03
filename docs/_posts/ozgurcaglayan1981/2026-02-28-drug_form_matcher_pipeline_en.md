---
layout: model
title: Drug Form Text Matcher
author: John Snow Labs
name: drug_form_matcher_pipeline
date: 2026-02-28
tags: [en, text_matcher, licensed, clinical, drug_form, pipeline]
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

This pipeline, can identify drug form entities in clinical text. It recognizes various pharmaceutical forms including tablet, capsule, injection, cream, solution, spray, and many more drug delivery forms commonly found in medication prescriptions and clinical documentation.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_pipeline_en_6.3.0_3.4_1772317631445.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_pipeline_en_6.3.0_3.4_1772317631445.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("drug_form_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("drug_form_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("drug_form_matcher_pipeline", "en", "clinical/models")

val sample_text = """ The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk             | begin | end | label     |
| :---------------- | ----: | --: | :-------- |
| tablet            |    43 |  48 | DRUG_FORM |
| capsule           |    98 | 104 | DRUG_FORM |
| injection         |   157 | 165 | DRUG_FORM |
| cream             |   227 | 231 | DRUG_FORM |
| transdermal patch |   282 | 298 | DRUG_FORM |
| solution          |   334 | 341 | DRUG_FORM |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_form_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|933.3 KB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- TextMatcherInternalModel
- ChunkConverter