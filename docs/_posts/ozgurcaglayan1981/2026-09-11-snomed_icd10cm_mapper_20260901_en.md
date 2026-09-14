---
layout: model
title: Mapping SNOMED Codes with Their Corresponding ICD10-CM Codes
author: John Snow Labs
name: snomed_icd10cm_mapper_20260901
date: 2026-09-11
tags: [en, chunk_mapper, licensed, clinical, icd10cm, snomed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps SNOMED codes to their corresponding ICD10-CM codes.

It performs a direct lookup against the training dictionary, providing fast, exact-match code mapping.

Trained on SNOMED CT US Edition 20260901 crosswalk data.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_icd10cm_mapper_20260901_en_6.4.1_3.4_1789158604565.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_icd10cm_mapper_20260901_en_6.4.1_3.4_1789158604565.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunkAssembler = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("snomed_code")

mapper = ChunkMapperModel.pretrained("snomed_icd10cm_mapper_20260901", "en", "clinical/models")\
    .setInputCols(["snomed_code"])\
    .setOutputCol("mappings")\
    .setRels(["icd10cm_code"])

pipeline = Pipeline(stages=[documentAssembler, chunkAssembler, mapper])

data = spark.createDataFrame([["1001000119102"]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunkAssembler = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("snomed_code")

mapper = medical.ChunkMapperModel.pretrained("snomed_icd10cm_mapper_20260901", "en", "clinical/models")\
    .setInputCols(["snomed_code"])\
    .setOutputCol("mappings")\
    .setRels(["icd10cm_code"])

pipeline = nlp.Pipeline(stages=[documentAssembler, chunkAssembler, mapper])

data = spark.createDataFrame([["1001000119102"]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols(Array("document"))
    .setOutputCol("snomed_code")

val mapper = ChunkMapperModel.pretrained("snomed_icd10cm_mapper_20260901", "en", "clinical/models")
    .setInputCols(Array("snomed_code"))
    .setOutputCol("mappings")
    .setRels(Array("icd10cm_code"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, mapper))

val data = Seq("1001000119102").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|   snomed_code | icd10cm_code   | all_k_resolutions   |
|--------------:|:---------------|:--------------------|
| 1001000119102 | I26.99         | I26.99:::           |
|      10001005 | A41.9          | A41.9:::P36.9       |
|      10000006 | R07.9          | R07.9:::            |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_icd10cm_mapper_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[snomed_code]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|2.3 MB|