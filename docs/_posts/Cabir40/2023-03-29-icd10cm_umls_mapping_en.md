---
layout: model
title: Pipeline to Mapping ICD10-CM Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: icd10cm_umls_mapping
date: 2023-03-29
tags: [en, licensed, icd10cm, umls, pipeline, chunk_mapping]
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

This pretrained pipeline is built on the top of `icd10cm_umls_mapper` model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.3.2_3.2_1680096605333.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_4.3.2_3.2_1680096605333.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(['M8950', 'R822', 'R0901'])
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(['M8950', 'R822', 'R0901'])
```
</div>

## Results

```bash

|    | icd10cm_code   | umls_code   |
|---:|:---------------|:------------|
|  0 | M8950          | C4721411    |
|  1 | R822           | C0159076    |
|  2 | R0901          | C0004044    |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|952.6 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel