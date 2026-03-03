---
layout: model
title: Pipeline to Mapping UMLS Codes with Their Corresponding RxNORM Codes
author: John Snow Labs
name: umls_rxnorm_mapping
date: 2026-03-03
tags: [en, umls, rxnorm, mapping, licensed, clinical, chunk_mapper, pipeline]
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

This pretrained pipeline is built on the top of umls_rxnorm_mapper model and maps UMLS codes to corresponding RxNorm codes

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_rxnorm_mapping_en_6.3.0_3.4_1772496195857.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_rxnorm_mapping_en_6.3.0_3.4_1772496195857.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_rxnorm_mapping", "en", "clinical/models")

sample_text = """ [['Hydrogen peroxide 30 mg'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("umls_rxnorm_mapping", "en", "clinical/models")

sample_text = """ [['Hydrogen peroxide 30 mg'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_rxnorm_mapping", "en", "clinical/models")

val sample_text = """ [['Hydrogen peroxide 30 mg'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]"""

val result = pipeline.transform(spark.createDataFrame(sample_text).toDF("text"))

```
</div>

## Results

```bash

| chunk                      | umls_code | rxnorm_code |
| :------------------------- | :-------- | ----------: |
| Hydrogen peroxide 30 mg    | C1126248  |      330565 |
| magnesium hydroxide 100 MG | C1134402  |      337012 |
| metformin 1000 MG          | C0987664  |      316255 |
| dilaudid                   | C0728755  |      224913 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_rxnorm_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.4 GB|

## Included Models

- DocumentAssembler
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- Resolution2Chunk
- ChunkMapperModel