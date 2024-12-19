---
layout: model
title: Mapping UMLS Codes with Their Corresponding MESH Codes
author: John Snow Labs
name: umls_mesh_mapper
date: 2024-12-12
tags: [licensed, en, umls, mesh, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps UMLS codes to corresponding MESH codes.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.

## Predicted Entities

`mesh_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_mesh_mapper_en_5.5.1_3.0_1734028763207.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_mesh_mapper_en_5.5.1_3.0_1734028763207.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('doc')

chunkAssembler = Doc2Chunk()\
    .setInputCols("doc")\
    .setOutputCol("umls_code")

chunkerMapper = ChunkMapperModel.pretrained("umls_mesh_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C0000530"],["C0000726"],["C0000343"],["C5416820"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('doc')

chunkAssembler = nlp.Doc2Chunk()\
    .setInputCols("doc")\
    .setOutputCol("umls_code")

chunkerMapper = medical.ChunkMapperModel.pretrained("umls_mesh_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C0000530"],["C0000726"],["C0000343"],["C5416820"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("umls_code")

val chunkerMapper = ChunkMapperModel
      .pretrained("umls_mesh_mapper", "en", "clinical/models")
      .setInputCols(Array("umls_code"))
      .setOutputCol("mappings")

val mapper_pipeline = Pipeline().setStages(Array(
                                            document_assembler,
                                            chunk_assembler,
                                            chunkerMapper))

val data = Seq("C0000530","C0000726","C0000343","C5416820").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)


```
</div>

## Results

```bash

+---------+----------+
|umls_code|mesh_code|
+---------+----------+
|C0000530 |D015720   |
|C0000726 |D000005   |
|C0000343 |D015652   |
|C5416820 |C000706269|
+---------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_mesh_mapper|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|6.2 MB|

## References

Trained on concepts from MESH for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
