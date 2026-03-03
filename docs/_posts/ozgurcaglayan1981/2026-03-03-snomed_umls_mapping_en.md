---
layout: model
title: Pipeline to Mapping SNOMED Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: snomed_umls_mapping
date: 2026-03-03
tags: [en, snomed, umls, mapping, licensed, clinical, chunk_mapper, pipeline]
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

This pretrained pipeline is built on the top of snomed_umls_mapper model and maps SNOMED codes to corresponding UMLS codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapping_en_6.3.0_3.4_1772563278450.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapping_en_6.3.0_3.4_1772563278450.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("snomed_umls_mapping", "en", "clinical/models")

sample_text = """ [['acebutolol'], ['fluids']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("snomed_umls_mapping", "en", "clinical/models")

sample_text = """ [['acebutolol'], ['fluids']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("snomed_umls_mapping", "en", "clinical/models")

val sample_text = """ [['acebutolol'], ['fluids']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| chunk      | snomed_code | umls_code |
| :--------- | ----------: | :-------- |
| acebutolol |    68088000 | C0000946  |
| fluids     |   118431008 | C1289919  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|692.6 MB|

## Included Models

- DocumentAssembler
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- Resolution2Chunk
- ChunkMapperModel