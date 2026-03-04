---
layout: model
title: Symptom Text Matcher Pipeline
author: John Snow Labs
name: symptom_matcher_pipeline
date: 2026-03-04
tags: [en, text_matcher, licensed, clinical, symptom, pipeline]
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

This pipeline, extracts symptom entities in clinical text. It recognizes a comprehensive list of clinical symptoms.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_pipeline_en_6.3.0_3.4_1772592800794.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_pipeline_en_6.3.0_3.4_1772592800794.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("symptom_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("symptom_matcher_pipeline", "en", "clinical/models")

sample_text = """ The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("symptom_matcher_pipeline", "en", "clinical/models")

val sample_text = """ The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk               | begin | end | label   |
| :------------------ | ----: | --: | :------ |
| severe headache     |    26 |  40 | SYMPTOM |
| nausea              |    46 |  51 | SYMPTOM |
| chest pain          |    77 |  86 | SYMPTOM |
| shortness of breath |   115 | 133 | SYMPTOM |
| fatigue             |   167 | 173 | SYMPTOM |
| dizziness           |   176 | 184 | SYMPTOM |
| palpitations        |   191 | 202 | SYMPTOM |
| abdominal pain      |   231 | 244 | SYMPTOM |
| constipation        |   250 | 261 | SYMPTOM |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|symptom_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|963.9 KB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- TextMatcherInternalModel
- ChunkConverter