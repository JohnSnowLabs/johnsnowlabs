---
layout: model
title: Pipeline to Detect Clinical Events (langtest)
author: John Snow Labs
name: ner_events_clinical_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, events, clinical, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_events_clinical_langtest](https://nlp.johnsnowlabs.com/2023/08/31/ner_events_clinical_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_events_clinical_langtest_pipeline_en_5.1.0_3.4_1694284368845.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_events_clinical_langtest_pipeline_en_5.1.0_3.4_1694284368845.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_events_clinical_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient presented to the emergency room last evening""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_events_clinical_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient presented to the emergency room last evening""")

```
</div>

## Results

```bash
|    | chunks             |   begin |   end | entities      |
|---:|:-------------------|--------:|------:|:--------------|
|  0 | presented          |      12 |    20 | EVIDENTIAL    |
|  1 | the emergency room |      25 |    42 | CLINICAL_DEPT |
|  2 | last evening       |      44 |    55 | DATE          |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_events_clinical_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter