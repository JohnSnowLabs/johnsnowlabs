---
layout: model
title: Procedure Text Matcher Pipeline
author: John Snow Labs
name: procedure_matcher_pipeline
date: 2026-02-28
tags: [en, text_matcher, licensed, clinical, procedure, pipeline]
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

This pipeline, extracts medical procedure entities in clinical text. It recognizes procedures including colonoscopy, biopsy, MRI, CT scan, echocardiogram, endoscopy, blood transfusion, and more.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/procedure_matcher_pipeline_en_6.3.0_3.4_1772319087492.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/procedure_matcher_pipeline_en_6.3.0_3.4_1772319087492.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("procedure_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("procedure_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("procedure_matcher_pipeline", "en", "clinical/models")

val sample_text = """ The patient presented with gastrointestinal symptoms. A colonoscopy was performed which revealed a suspicious lesion, and a biopsy was obtained for pathological examination."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk       | begin | end | label     |
| :---------- | ----: | --: | :-------- |
| colonoscopy |    56 |  66 | PROCEDURE |
| biopsy      |   124 | 129 | PROCEDURE |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|procedure_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|965.6 KB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- TextMatcherInternalModel
- ChunkConverter