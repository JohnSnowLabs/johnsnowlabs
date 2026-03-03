---
layout: model
title: Mapping Entities with Corresponding SNOMED Codes - Pipeline
author: John Snow Labs
name: snomed_mapper_pipeline
date: 2026-03-02
tags: [en, snomed, mapper, licensed, clinical, chunk_mapper, pipeline]
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

This pipeline maps clinical entities to their corresponding SNOMED codes. It provides fast and accurate clinical code mapping without requiring embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_mapper_pipeline_en_6.3.0_3.4_1772413737283.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_mapper_pipeline_en_6.3.0_3.4_1772413737283.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("snomed_mapper_pipeline", "en", "clinical/models")

sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("snomed_mapper_pipeline", "en", "clinical/models")

sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("snomed_mapper_pipeline", "en", "clinical/models")

val sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| ner_chunk         | mapping_result |
| :---------------- | :------------- |
| ofloxacin         | 387551000      |
| secondary         | 2603003        |
| conjunctivitis    | 9826008        |
| cefixime          | 387536009      |
| cystic urethritis | 1259233009     |
| ibuprofen         | 387207008      |
| inflammation      | 257552002      |
| cilnidipine       | 1177123004     |
| hypertension      | 38341003       |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_mapper_pipeline|
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