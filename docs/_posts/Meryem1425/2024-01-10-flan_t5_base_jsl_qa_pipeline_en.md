---
layout: model
title: Medical Question Answering Pipeline(flan_t5)
author: John Snow Labs
name: flan_t5_base_jsl_qa_pipeline
date: 2024-01-10
tags: [licensed, en, flan_t5, pipeline, qa]
task: [Question Answering, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [flan_t5_base_jsl_qa](https://nlp.johnsnowlabs.com/2023/05/15/flan_t5_base_jsl_qa_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/flan_t5_base_jsl_qa_pipeline_en_5.2.0_3.2_1704850831281.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/flan_t5_base_jsl_qa_pipeline_en_5.2.0_3.2_1704850831281.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

qa_pipeline = PretrainedPipeline("flan_t5_base_jsl_qa_pipeline", "en", "clinical/models")

context = """The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65-97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene."""

question = """What is the effect of directing attention on memory?"""

result = qa_pipeline.annotate([question], [context])

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val qa_pipeline = PretrainedPipeline("flan_t5_base_jsl_qa_pipeline", "en", "clinical/models")

val context = """The visual indexing theory proposed by Zenon Pylyshyn (Cognition, 32, 65-97, 1989) predicts that visual attention mechanisms are employed when mental images are projected onto a visual scene."""

val question = """What is the effect of directing attention on memory?"""

val result = qa_pipeline.annotate([question], [context])

```
</div>

## Results

```bash
The effect of directing attention on memory is that it can help to improve memory retention and recall. It can help to reduce the amount of time spent on tasks, such as focusing on one task at a time, or focusing on 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|flan_t5_base_jsl_qa_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|928.7 MB|

## Included Models

- MultiDocumentAssembler
- MedicalQuestionAnswering
