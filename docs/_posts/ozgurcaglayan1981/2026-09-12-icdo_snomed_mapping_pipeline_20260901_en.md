---
layout: model
title: Mapping ICDO Codes with Their Corresponding SNOMED Codes - Pipeline
author: John Snow Labs
name: icdo_snomed_mapping_pipeline_20260901
date: 2026-09-12
tags: [en, chunk_mapper, licensed, clinical, pipeline, icdo, snomed]
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

This pipeline maps ICDO codes to their corresponding SNOMED codes via a direct dictionary lookup.

Wraps the `icdo_snomed_mapper_20260901` mapper, trained on SNOMED CT US Edition 20260901 crosswalk data.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789234308226.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789234308226.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("icdo_snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["8000/0"]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("icdo_snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["8000/0"]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("icdo_snomed_mapping_pipeline_20260901", "en", "clinical/models")

val data = Seq("8000/0").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| icdo_code   |   snomed_code | all_k_resolutions                            |
|:------------|--------------:|:---------------------------------------------|
| 8000/0      |       3898006 | 3898006:::                                   |
| 8000/1      |     400095002 | 400095002:::414389009:::783219005:::86251006 |
| 8170/3      |      25370001 | 25370001:::                                  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icdo_snomed_mapping_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|119.6 KB|

## Included Models

- DocumentAssembler
- Doc2Chunk
- ChunkMapperModel