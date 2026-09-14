---
layout: model
title: Mapping ICD10-CM Codes with Their Corresponding SNOMED Codes - Pipeline
author: John Snow Labs
name: icd10cm_snomed_mapping_pipeline_20260901
date: 2026-09-12
tags: [en, chunk_mapper, licensed, clinical, pipeline, icd10cm, snomed]
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

This pipeline maps ICD10-CM codes to their corresponding SNOMED codes via a direct dictionary lookup.

Wraps the `icd10cm_snomed_mapper_20260901` mapper, trained on SNOMED CT US Edition 20260901 crosswalk data.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789233676151.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_snomed_mapping_pipeline_20260901_en_6.4.1_3.4_1789233676151.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("icd10cm_snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["A02.20"]]).toDF("text")
result = snomed_pipeline.transform(data)

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

snomed_pipeline = nlp.PretrainedPipeline("icd10cm_snomed_mapping_pipeline_20260901", "en", "clinical/models")

data = spark.createDataFrame([["A02.20"]]).toDF("text")
result = snomed_pipeline.transform(data)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("icd10cm_snomed_mapping_pipeline_20260901", "en", "clinical/models")

val data = Seq("A02.20").toDF("text")
val result = snomed_pipeline.transform(data)

```
</div>

## Results

```bash
| icd10cm_code   |   snomed_code | all_k_resolutions                                                                                                                 |
|:---------------|--------------:|:----------------------------------------------------------------------------------------------------------------------------------|
| A02.20         |      47375003 | 47375003:::                                                                                                                       |
| A00.0          |     240349003 | 240349003:::447282003:::63650001                                                                                                  |
| Z83.3          |     160303001 | 160303001:::160402005:::416855002:::430678008:::430679000:::444094009:::444161008:::704144000:::719761003:::719763000:::721151003 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_snomed_mapping_pipeline_20260901|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.3 MB|

## Included Models

- DocumentAssembler
- Doc2Chunk
- ChunkMapperModel