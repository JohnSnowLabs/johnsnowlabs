---
layout: model
title: NER Pipeline for Temporal Mentions - Voice of the Patient
author: John Snow Labs
name: ner_vop_temporal_pipeline
date: 2023-06-22
tags: [pipeline, licensed, temporal, ner, en, vop]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts mentions of temporal entities from health-related text in colloquial language.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_temporal_pipeline_en_4.4.4_3.0_1687442219296.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_temporal_pipeline_en_4.4.4_3.0_1687442219296.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_vop_temporal_pipeline", "en", "clinical/models")

pipeline.annotate("
I broke my arm playing football last month and had to get surgery in the orthopedic department. The cast just came off yesterday and I'm excited to start physical therapy and get back to the game.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_vop_temporal_pipeline", "en", "clinical/models")

val result = pipeline.annotate("
I broke my arm playing football last month and had to get surgery in the orthopedic department. The cast just came off yesterday and I'm excited to start physical therapy and get back to the game.")
```
</div>

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_vop_temporal_pipeline", "en", "clinical/models")

pipeline.annotate("
I broke my arm playing football last month and had to get surgery in the orthopedic department. The cast just came off yesterday and I'm excited to start physical therapy and get back to the game.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_vop_temporal_pipeline", "en", "clinical/models")

val result = pipeline.annotate("
I broke my arm playing football last month and had to get surgery in the orthopedic department. The cast just came off yesterday and I'm excited to start physical therapy and get back to the game.")
```
</div>

## Results

```bash
Results


| chunk      | ner_label   |
|:-----------|:------------|
| last month | DateTime    |
| yesterday  | DateTime    |


{:.model-param}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_temporal_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|791.6 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter