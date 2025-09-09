---
layout: model
title: HPO Code To Extraocular Movements (EOM) Mapping
author: John Snow Labs
name: hpo_code_eom_mapper
date: 2025-07-28
tags: [licensed, en, hpo, eom, mapping, extraocular]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.4
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps HPO codes to their related extraocular movements (EOM). It also returns all the possible EOMs in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_code_eom_mapper_en_6.0.4_3.0_1753716005895.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_code_eom_mapper_en_6.0.4_3.0_1753716005895.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("hpo_code")

mapperModel = ChunkMapperModel.pretrained("hpo_code_eom_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["eom"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000154"],["HP:0400001"],["HP:0009765"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("hpo_code")

mapperModel = medical.ChunkMapperModel.pretrained("hpo_code_eom_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["eom"])

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000154"],["HP:0400001"],["HP:0009765"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("hpo_code")

val mapperModel = ChunkMapperModel.pretrained("hpo_code_eom_mapper", "en", "clinical/models")
    .setInputCols("hpo_code")
    .setOutputCol("mappings")
    .setRels(Array("eom"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
))


val data = Seq("HP:0000154","HP:0400001","HP:0009765").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------+--------------------+-----------------------+
|  hpo_code|                 eom|      all_k_resolutions|
+----------+--------------------+-----------------------+
|HP:0000154|EOM:a6a2d57a281ead72|EOM:a6a2d57a281ead72:::|
|HP:0400001|EOM:8a5493c72e0dd13c|EOM:8a5493c72e0dd13c:::|
|HP:0009765|EOM:49acd433e354541b|EOM:49acd433e354541b:::|
+----------+--------------------+-----------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_code_eom_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|10.3 KB|
