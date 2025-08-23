---
layout: model
title: Mapping MESH Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: mesh_umls_mapper
date: 2025-06-21
tags: [licensed, en, umls, mesh, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps MESH codes to corresponding UMLS codes under the Unified Medical Language System (UMLS).

## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapper_en_6.0.2_3.0_1750536283151.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapper_en_6.0.2_3.0_1750536283151.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('doc')

chunkAssembler = Doc2Chunk()\
    .setInputCols("doc")\
    .setOutputCol("mesh_code")

chunkerMapper = ChunkMapperModel.pretrained("mesh_umls_mapper", "en", "clinical/models")\
    .setInputCols(["lmesh_code"])\
    .setOutputCol("mappings")

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C000015"],["C000002"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('doc')

chunkAssembler = nlp.Doc2Chunk()\
    .setInputCols("doc")\
    .setOutputCol("mesh_code")

chunkerMapper = medical.ChunkMapperModel.pretrained("mesh_umls_mapper", "en", "clinical/models")\
    .setInputCols(["mesh_code"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C000015"],["C000002"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("mesh_code")

val chunkerMapper = ChunkMapperModel
      .pretrained("mesh_umls_mapper", "en", "clinical/models")
      .setInputCols(Array("mesh_code"))
      .setOutputCol("mappings")

val mapper_pipeline = Pipeline().setStages(Array(
                                            document_assembler,
                                            chunk_assembler,
                                            chunkerMapper))

val data = Seq("C000015","C000002").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------+---------+
|mesh_code|umls_code|
+---------+---------+
|C000015  |C0067655 |
|C000002  |C0950157 |
+---------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mesh_umls_mapper|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|5.4 MB|

## References

Trained on concepts from MESH for the 2025AA release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html