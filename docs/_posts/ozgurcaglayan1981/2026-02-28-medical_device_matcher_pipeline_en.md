---
layout: model
title: Medical Device Text Matcher Pipeline
author: John Snow Labs
name: medical_device_matcher_pipeline
date: 2026-02-28
tags: [en, text_matcher, licensed, clinical, medical_device, pipeline]
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

This pipeline, extracts medical device entities in clinical text. It recognizes devices including ventilator, defibrillator, stent, insulin pump, glucometer, nebulizer, and more.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_pipeline_en_6.3.0_3.4_1772318715289.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_pipeline_en_6.3.0_3.4_1772318715289.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("medical_device_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("medical_device_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("medical_device_matcher_pipeline", "en", "clinical/models")

val sample_text = """ The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk        | begin | end | label          |
| :----------- | ----: | --: | :------------- |
| ventilator   |    28 |  37 | MEDICAL_DEVICE |
| pacemaker    |    66 |  74 | MEDICAL_DEVICE |
| glucometer   |   160 | 169 | MEDICAL_DEVICE |
| insulin pump |   205 | 216 | MEDICAL_DEVICE |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_device_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|944.4 KB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- TextMatcherInternalModel
- ChunkConverter