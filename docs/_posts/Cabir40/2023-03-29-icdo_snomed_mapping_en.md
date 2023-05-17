---
layout: model
title: Pipeline to Mapping ICDO Codes with Their Corresponding SNOMED Codes
author: John Snow Labs
name: icdo_snomed_mapping
date: 2023-03-29
tags: [en, licensed, clinical, resolver, pipeline, chunk_mapping, icdo, snomed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of `icdo_snomed_mapper` model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapping_en_4.3.2_3.2_1680120340177.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapping_en_4.3.2_3.2_1680120340177.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icdo_snomed_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(8120/1 8170/3 8380/3)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icdo_snomed_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(8120/1 8170/3 8380/3)
```
</div>

## Results

```bash

|    | icdo_code                | snomed_code                    |
|---:|:-------------------------|:-------------------------------|
|  0 | 8120/1 | 8170/3 | 8380/3 | 45083001 | 25370001 | 30289006 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icdo_snomed_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|133.3 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel