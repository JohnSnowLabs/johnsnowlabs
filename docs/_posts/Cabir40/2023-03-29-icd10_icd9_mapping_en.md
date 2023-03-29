---
layout: model
title: Pipeline to Mapping ICD10-CM Codes with Their Corresponding ICD-9-CM Codes
author: John Snow Labs
name: icd10_icd9_mapping
date: 2023-03-29
tags: [en, licensed, icd10cm, icd9, pipeline, chunk_mapping]
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

This pretrained pipeline is built on the top of icd10_icd9_mapper model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10_icd9_mapping_en_4.3.2_3.2_1680091748981.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10_icd9_mapping_en_4.3.2_3.2_1680091748981.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10_icd9_mapping", "en", "clinical/models")

text = '''Z833 A0100 A000'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd10_icd9_mapping", "en", "clinical/models")

val text = '''Z833 A0100 A000'''

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash

|    | icd10_code          | icd9_code          |
|---:|:--------------------|:-------------------|
|  0 | Z833 | A0100 | A000 | V180 | 0020 | 0010 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10_icd9_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|589.7 KB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel