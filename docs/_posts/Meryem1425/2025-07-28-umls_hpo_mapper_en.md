---
layout: model
title: UMLS Code To HPO Code Mapping
author: John Snow Labs
name: umls_hpo_mapper
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

This pretrained model maps UMLS codes to corresponding HPO codes. It also returns all the possible HPO codes in the `all_k_resolutions` in the metadata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_hpo_mapper_en_6.0.4_3.0_1753716239960.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_hpo_mapper_en_6.0.4_3.0_1753716239960.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("umls_code")

mapperModel = ChunkMapperModel.pretrained("umls_hpo_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["C2973529"],["C0000731"],["C0008035"]]).toDF("text")
result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
      .setInputCols(["document"])\
      .setOutputCol("umls_code")

mapperModel = medical.ChunkMapperModel.pretrained("umls_hpo_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")\
    .setRels(["hpo_code"])

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["C2973529"],["C0000731"],["C0008035"]]).toDF("text")
result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("umls_code")

val mapperModel = ChunkMapperModel.pretrained("umls_hpo_mapper", "en", "clinical/models")
    .setInputCols("umls_code")
    .setOutputCol("mappings")
    .setRels(Array("hpo_code"))

val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
))

val data = Seq("C2973529", "C0000731", "C0008035").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------+----------+-----------------+
|umls_code|  hpo_code|all_k_resolutions|
+---------+----------+-----------------+
| C2973529|HP:0011944|    HP:0011944:::|
| C0000731|HP:0003270|    HP:0003270:::|
| C0008035|HP:0006649|    HP:0006649:::|
+---------+----------+-----------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_hpo_mapper|
|Compatibility:|Healthcare NLP 6.0.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|35.4 KB|
