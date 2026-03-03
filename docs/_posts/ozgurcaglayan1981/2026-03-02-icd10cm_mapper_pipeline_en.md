---
layout: model
title: Mapping Entities with Corresponding ICD-10-CM Codes - Pipeline
author: John Snow Labs
name: icd10cm_mapper_pipeline
date: 2026-03-02
tags: [en, icd10cm, mapper, licensed, clinical, chunk_mapper, pipeline]
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

This pipeline maps clinical entities to their corresponding ICD-10-CM codes. It provides fast and accurate clinical code mapping without requiring embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_pipeline_en_6.3.0_3.4_1772414126069.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_pipeline_en_6.3.0_3.4_1772414126069.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10cm_mapper_pipeline", "en", "clinical/models")

sample_text = """ A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("icd10cm_mapper_pipeline", "en", "clinical/models")

sample_text = """ A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("icd10cm_mapper_pipeline", "en", "clinical/models")

val sample_text = """ A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|ner_chunk             |mapping_result|
|----------------------|--------------|
|sciatica              |M54.3         |
|myalgia               |M79.1         |
|polymyositis          |M33.2         |
|glossitis             |K14.0         |
|beriberi              |E51.1         |
|nutritional deficiency|E63.9         |
|spondylolysis         |M43.0         |
|motion sickness       |T75.3         |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_mapper_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMapperModel