---
layout: model
title: Pipeline to Mapping RxNORM Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: rxnorm_umls_mapping
date: 2026-03-04
tags: [en, rxnorm, umls, mapping, licensed, clinical, chunk_mapper, pipeline]
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

This pretrained pipeline is built on the top of rxnorm_umls_mapper model and maps RxNorm codes to corresponding UMLS codes

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapping_en_6.3.0_3.4_1772647310665.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapping_en_6.3.0_3.4_1772647310665.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("rxnorm_umls_mapping", "en", "clinical/models")

sample_text = """ [['amlodipine 5 MG'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("rxnorm_umls_mapping", "en", "clinical/models")

sample_text = """ [['amlodipine 5 MG'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("rxnorm_umls_mapping", "en", "clinical/models")

val sample_text = """ [['amlodipine 5 MG'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| chunk                      | rxnorm_code | umls_code |
| :------------------------- | ----------: | :-------- |
| amlodipine 5 MG            |      197361 | C0687883  |
| magnesium hydroxide 100 MG |      337012 | C1134402  |
| metformin 1000 MG          |      316255 | C0987664  |
| dilaudid                   |      224913 | C0728755  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_umls_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.5 GB|

## Included Models

- DocumentAssembler
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- Resolution2Chunk
- ChunkMapperModel