---
layout: model
title: Drug Route Text Matcher Pipeline
author: John Snow Labs
name: drug_route_matcher_pipeline
date: 2026-03-04
tags: [en, text_matcher, licensed, clinical, drug_route, pipeline]
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

This pipeline, extracts drug administration route entities in clinical text. It recognizes routes including oral, IV, IM, subcutaneous, topical, transdermal, inhalation, sublingual, rectal, and more.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_route_matcher_pipeline_en_6.3.0_3.4_1772592143798.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_route_matcher_pipeline_en_6.3.0_3.4_1772592143798.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("drug_route_matcher_pipeline", "en", "clinical/models")

sample_text = """ Metformin 500mg orally twice daily. Insulin glargine subcutaneously at bedtime. Morphine 4mg IV for pain. Albuterol via inhalation every 4 hours PRN."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("drug_route_matcher_pipeline", "en", "clinical/models")

sample_text = """ Metformin 500mg orally twice daily. Insulin glargine subcutaneously at bedtime. Morphine 4mg IV for pain. Albuterol via inhalation every 4 hours PRN."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("drug_route_matcher_pipeline", "en", "clinical/models")

val sample_text = """ Metformin 500mg orally twice daily. Insulin glargine subcutaneously at bedtime. Morphine 4mg IV for pain. Albuterol via inhalation every 4 hours PRN."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk      | begin | end | label      |
| :--------- | ----: | --: | :--------- |
| orally     |    16 |  21 | DRUG_ROUTE |
| IV         |    93 |  94 | DRUG_ROUTE |
| inhalation |   120 | 129 | DRUG_ROUTE |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_route_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|937.8 KB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- TextMatcherInternalModel
- ChunkConverter