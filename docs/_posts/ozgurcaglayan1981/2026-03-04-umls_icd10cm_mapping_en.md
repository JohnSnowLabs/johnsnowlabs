---
layout: model
title: Pipeline to Mapping UMLS Codes with Their Corresponding ICD10CM Codes
author: John Snow Labs
name: umls_icd10cm_mapping
date: 2026-03-04
tags: [en, umls, icd10cm, mapping, licensed, clinical, chunk_mapper, pipeline]
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

This pretrained pipeline is built on the top of umls_icd10cm_mapper model and maps maps UMLS codes to corresponding ICD10CM codes

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_icd10cm_mapping_en_6.3.0_3.4_1772649037495.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_icd10cm_mapping_en_6.3.0_3.4_1772649037495.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_icd10cm_mapping", "en", "clinical/models")

sample_text = """ [['C0000744'], ['C2875181']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("umls_icd10cm_mapping", "en", "clinical/models")

sample_text = """ [['C0000744'], ['C2875181']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_icd10cm_mapping", "en", "clinical/models")

val sample_text = """ [['C0000744'], ['C2875181']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| umls_code | icd10cm_code |
| :-------- | :----------- |
| C0000744  | E78.6        |
| C2875181  | G43.81       |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_icd10cm_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.5 MB|

## Included Models

- DocumentAssembler
- Doc2Chunk
- ChunkMapperModel