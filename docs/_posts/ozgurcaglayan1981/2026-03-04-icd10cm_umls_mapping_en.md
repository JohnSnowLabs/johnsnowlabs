---
layout: model
title: Pipeline to Mapping ICD10CM Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: icd10cm_umls_mapping
date: 2026-03-04
tags: [en, icd10cm, umls, mapping, licensed, clinical, chunk_mapper, pipeline]
task: [Chunk Mapping, Pipeline Healthcare]
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

This pretrained pipeline is built on the top of icd10cm_umls_mapper model and maps ICD10CM codes to corresponding UMLS codes

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_6.3.0_3.4_1772645882574.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapping_en_6.3.0_3.4_1772645882574.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

sample_text = """ [['A01.2'], ['F10.220']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

sample_text = """ [['A01.2'], ['F10.220']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("icd10cm_umls_mapping", "en", "clinical/models")

val sample_text = """ [['A01.2'], ['F10.220']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| icd10cm_code | umls_code |
| :----------- | :-------- |
| A01.2        | C0343376  |
| F10.220      | C2874385  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.4 MB|

## Included Models

- DocumentAssembler
- Doc2Chunk
- ChunkMapperModel