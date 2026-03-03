---
layout: model
title: Mapping Entities with Corresponding RxNorm Codes - Pipeline
author: John Snow Labs
name: rxnorm_mapper_pipeline
date: 2026-03-02
tags: [en, rxnorm, mapper, licensed, clinical, chunk_mapper, pipeline]
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

This pipeline maps drug entities to their corresponding RxNorm codes. It provides fast and accurate drug code mapping without requiring embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_pipeline_en_6.3.0_3.4_1772413015137.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_pipeline_en_6.3.0_3.4_1772413015137.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("rxnorm_mapper_pipeline", "en", "clinical/models")

sample_text = """ The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("rxnorm_mapper_pipeline", "en", "clinical/models")

sample_text = """ The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("rxnorm_mapper_pipeline", "en", "clinical/models")

val sample_text = """ The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| ner_chunk                 | mapping_result |
| :------------------------ | :------------- |
| ibuprofen topical cream   | 377732         |
| selenium sulfide 25 mg/ml | 328880         |
| salicylamide 250 mg       | 316651         |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_mapper_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMapperModel