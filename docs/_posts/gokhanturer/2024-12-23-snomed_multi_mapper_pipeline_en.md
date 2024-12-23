---
layout: model
title: SNOMED Code Mapping Pipeline
author: John Snow Labs
name: snomed_multi_mapper_pipeline
date: 2024-12-23
tags: [licensed, en, snomed, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps SNOMED codes to their corresponding ICD-10, ICD-O, and UMLS codes.

## Predicted Entities

`snomed_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_multi_mapper_pipeline_en_5.5.1_3.4_1734958604723.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_multi_mapper_pipeline_en_5.5.1_3.4_1734958604723.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

mapper_pipeline = PretrainedPipeline("snomed_multi_mapper_pipeline", "en", "clinical/models")

result = mapper_pipeline.fullAnnotate(["10000006", "128501000"])

```

{:.jsl-block}
```python

mapper_pipeline = nlp.PretrainedPipeline("snomed_multi_mapper_pipeline", "en", "clinical/models")

result = mapper_pipeline.fullAnnotate(["10000006", "128501000"])

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val mapper_pipeline = PretrainedPipeline("snomed_multi_mapper_pipeline", "en", "clinical/models")

val result = mapper_pipeline.fullAnnotate(["10000006", "128501000"])

```
</div>

## Results

```bash

+-----------+------------+---------+---------+
|snomed_code|icd10cm_code|icdo_code|umls_code|
+-----------+------------+---------+---------+
|   10000006|       R07.9|     NONE| C0232289|
|  128501000|        NONE|    C49.5| C0448606|
+-----------+------------+---------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_multi_mapper_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|9.4 MB|

## Included Models

- DocumentAssembler
- DocMapperModel
- DocMapperModel
- DocMapperModel