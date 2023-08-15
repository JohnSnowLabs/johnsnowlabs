---
layout: model
title: SNOMED Code Mapping Pipeline
author: John Snow Labs
name: snomed_giant_pipeline
date: 2023-08-15
tags: [licensed, en, clinical, snomed, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps SNOMED codes to their corresponding ICD-10, ICD-O, and UMLS codes. You’ll just feed white space-delimited SNOMED codes and get the result.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_giant_pipeline_en_5.0.1_3.2_1692128865239.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_giant_pipeline_en_5.0.1_3.2_1692128865239.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_giant_pipeline", "en", "clinical/models")

result = snomed_pipeline.fullAnnotate("""10000006 128501000""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = new PretrainedPipeline("snomed_giant_pipeline", "en", "clinical/models")

val result = snomed_pipeline.fullAnnotate("""10000006 128501000""")
```
</div>

## Results

```bash

|    |   snomed_code | icd10_mappings   | icdo_mappings   | umls_mappings   |
|---:|--------------:|:-----------------|:----------------|:----------------|
|  0 |      10000006 | R07.9            | NONE            | C0232289        |
|  1 |     128501000 | NONE             | C49.5           | C0448606        |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_giant_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|6.8 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
