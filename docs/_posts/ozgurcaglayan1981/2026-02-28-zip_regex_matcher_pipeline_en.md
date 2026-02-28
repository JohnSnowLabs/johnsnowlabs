---
layout: model
title: ZIP Code Contextual Parser Pipeline
author: John Snow Labs
name: zip_regex_matcher_pipeline
date: 2026-02-28
tags: [en, contextualparser, licensed, clinical, zip, pipeline]
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

This pipeline, extracts ZIP code entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zip_regex_matcher_pipeline_en_6.3.0_3.4_1772316521126.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zip_regex_matcher_pipeline_en_6.3.0_3.4_1772316521126.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("zip_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ John Doe lives at 1234 Maple Street, Springfield, IL 62704. He works at 5678 Oak Avenue, Austin, TX 73301. His previous address was 4321 Pine Street, Los Angeles, CA 90001. His cousin Jane lives at 7890 Elm Street, Chicago, IL 60614."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("zip_regex_matcher_pipeline", "en", "clinical/models")

sample_text = """ John Doe lives at 1234 Maple Street, Springfield, IL 62704. He works at 5678 Oak Avenue, Austin, TX 73301. His previous address was 4321 Pine Street, Los Angeles, CA 90001. His cousin Jane lives at 7890 Elm Street, Chicago, IL 60614."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("zip_regex_matcher_pipeline", "en", "clinical/models")

val sample_text = """ John Doe lives at 1234 Maple Street, Springfield, IL 62704. He works at 5678 Oak Avenue, Austin, TX 73301. His previous address was 4321 Pine Street, Los Angeles, CA 90001. His cousin Jane lives at 7890 Elm Street, Chicago, IL 60614."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|   chunk |   begin |   end | label   |
|--------:|--------:|------:|:--------|
|   62704 |      53 |    57 | ZIP     |
|   73301 |     100 |   104 | ZIP     |
|   90001 |     166 |   170 | ZIP     |
|   60614 |     227 |   231 | ZIP     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zip_regex_matcher_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|397.1 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter