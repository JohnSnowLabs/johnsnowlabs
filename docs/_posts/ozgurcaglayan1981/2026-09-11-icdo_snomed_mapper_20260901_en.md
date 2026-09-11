---
layout: model
title: Mapping ICDO Codes with Their Corresponding SNOMED Codes
author: John Snow Labs
name: icdo_snomed_mapper_20260901
date: 2026-09-11
tags: [en, chunk_mapper, licensed, clinical, icdo, snomed]
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

This model maps ICDO codes to their corresponding SNOMED codes.

It performs a direct lookup against the training dictionary, providing fast, exact-match code mapping.

Trained on SNOMED CT US Edition 20260901 crosswalk data.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapper_20260901_en_6.4.1_3.4_1789159523517.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icdo_snomed_mapper_20260901_en_6.4.1_3.4_1789159523517.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunkAssembler = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("icdo_code")

mapper = ChunkMapperModel.pretrained("icdo_snomed_mapper_20260901", "en", "clinical/models")\
    .setInputCols(["icdo_code"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

pipeline = Pipeline(stages=[documentAssembler, chunkAssembler, mapper])

data = spark.createDataFrame([["8000/0"]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunkAssembler = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("icdo_code")

mapper = medical.ChunkMapperModel.pretrained("icdo_snomed_mapper_20260901", "en", "clinical/models")\
    .setInputCols(["icdo_code"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

pipeline = nlp.Pipeline(stages=[documentAssembler, chunkAssembler, mapper])

data = spark.createDataFrame([["8000/0"]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols(Array("document"))
    .setOutputCol("icdo_code")

val mapper = ChunkMapperModel.pretrained("icdo_snomed_mapper_20260901", "en", "clinical/models")
    .setInputCols(Array("icdo_code"))
    .setOutputCol("mappings")
    .setRels(Array("snomed_code"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, mapper))

val data = Seq("8000/0").toDF("text")
val result = pipeline.fit(data).transform(data)

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
|Model Name:|icdo_snomed_mapper_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[icdo_code]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|114.2 KB|