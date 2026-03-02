---
layout: model
title: Mapping Entities with Corresponding CPT Codes - Pipeline
author: John Snow Labs
name: cpt_mapper_pipeline
date: 2026-03-02
tags: [en, cpt, mapper, licensed, clinical, chunk_mapper, pipeline]
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

This pipeline maps clinical entities (procedures, tests, treatments) to their corresponding CPT (Current Procedural Terminology) codes. It provides fast and accurate procedural code mapping without requiring embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_mapper_pipeline_en_6.3.0_3.4_1772414517303.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_mapper_pipeline_en_6.3.0_3.4_1772414517303.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("cpt_mapper_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("cpt_mapper_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("cpt_mapper_pipeline", "en", "clinical/models")

val sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|ner_chunk         |mapping_result|
|------------------|--------------|
|episiotomy        |59300         |
|Pulse oximetry    |94760         |
|blood transfusion |36430         |
|inpatient hospital|1021881       |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_mapper_pipeline|
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