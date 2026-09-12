---
layout: model
title: Mapping Entities with Corresponding SNOMED Codes - Pipeline
author: John Snow Labs
name: snomed_mapping_pipeline_20260901
date: 2026-09-12
tags: [en, chunk_mapper, licensed, clinical, pipeline, snomed]
task: [Chunk Mapping, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts clinical entities from text and maps them to their corresponding SNOMED CT concept codes via a direct dictionary lookup.

Wraps the `snomed_mapper_20260901` mapper, trained on the SNOMED CT US Edition 20260901 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789234521112.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789234521112.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient underwent an appendectomy for acute appendicitis and was diagnosed with type 2 diabetes mellitus. She reported hemolysis and chest pain on recent labs, was noted to have coronary artery disease, and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["The patient underwent an appendectomy for acute appendicitis and was diagnosed with type 2 diabetes mellitus. She reported hemolysis and chest pain on recent labs, was noted to have coronary artery disease, and was started on aspirin."]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_mapping_pipeline_20260901", "en", "clinical/models")

val data = Seq("The patient underwent an appendectomy for acute appendicitis and was diagnosed with type 2 diabetes mellitus. She reported hemolysis and chest pain on recent labs, was noted to have coronary artery disease, and was started on aspirin.").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| ner_chunk                |   snomed_code | all_k_resolutions                |
|:-------------------------|--------------:|:---------------------------------|
| appendectomy             |      80146002 | 80146002:::                      |
| appendicitis             |      74400008 | 74400008:::                      |
| type 2 diabetes mellitus |      44054006 | 44054006:::                      |
| hemolysis                |     260882000 | 260882000:::404227002:::73320003 |
| chest pain               |      29857009 | 29857009:::                      |
| coronary artery disease  |      53741008 | 53741008:::                      |
| aspirin                  |     387458008 | 387458008:::                     |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_mapping_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
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