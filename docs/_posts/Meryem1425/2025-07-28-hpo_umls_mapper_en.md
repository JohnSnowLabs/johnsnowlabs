---
layout: model
title: HPO Code To UMLS Code Mapping
author: John Snow Labs
name: hpo_umls_mapper
date: 2025-07-28
tags: [licensed, en, umls, hpo, mapping]
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

This pretrained model maps HPO codes to corresponding UMLS codes. It also returns all the possible UMLS codes in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_umls_mapper_en_6.0.4_3.0_1753716162526.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_umls_mapper_en_6.0.4_3.0_1753716162526.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

mapperModel = ChunkMapperModel.pretrained("hpo_umls_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000010"],["HP:0200039"],["HP:0000951"]]).toDF("text")
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

mapperModel = medical.ChunkMapperModel.pretrained("hpo_umls_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_code"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["HP:0000010"],["HP:0200039"],["HP:0000951"]]).toDF("text")
result = mapper_pipeline.fit(data).transform(data)

```
```scala

val ocument_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("hpo_code")

val mapperModel = ChunkMapperModel.pretrained("hpo_umls_mapper", "en", "clinical/models")
    .setInputCols("hpo_code")
    .setOutputCol("mappings")
    .setRels(Array("umls_code"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
))

val data = Seq("HP:0000010", "HP:0200039", "HP:0000951").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------+---------+-----------------------------------------+
|  hpo_code|umls_code|                        all_k_resolutions|
+----------+---------+-----------------------------------------+
|HP:0000010| C0262421|C0262421:::C0262655:::C0034186:::C0520575|
|HP:0200039| C0877055|           C0877055:::C0152081:::C0241157|
|HP:0000951| C0037268|C0037268:::C0241164:::C0043345:::C0038325|
+----------+---------+-----------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_umls_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|27.7 KB|
