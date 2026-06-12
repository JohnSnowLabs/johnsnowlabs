---
layout: model
title: MeSH to UMLS Code Mapping
author: John Snow Labs
name: mesh_umls_mapper
date: 2026-06-12
tags: [en, chunk_mapper, licensed, clinical, umls, mesh]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps MeSH codes to UMLS codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapper_en_6.4.0_3.4_1781304636894.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mesh_umls_mapper_en_6.4.0_3.4_1781304636894.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("doc")

doc2chunk = Doc2Chunk()\
    .setInputCols(["doc"])\
    .setOutputCol("ner_chunk")

mapper = ChunkMapperModel.pretrained("mesh_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["D003924"],["D001172"],["D014943"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("doc")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols(["doc"])\
    .setOutputCol("ner_chunk")

mapper = medical.ChunkMapperModel.pretrained("mesh_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["D003924"],["D001172"],["D014943"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("doc")

val doc2chunk = new Doc2Chunk()
  .setInputCols(Array("doc"))
  .setOutputCol("ner_chunk")

val mapper = ChunkMapperModel.pretrained("mesh_umls_mapper","en","clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, doc2chunk, mapper))
val data = Seq("D003924","D001172","D014943").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| mesh_code   | umls_code   |
|:------------|:------------|
| D003924     | C0011860    |
| D001172     | C0003873    |
| D014943     | C0021788    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mesh_umls_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings_c2u]|
|Language:|en|
|Size:|5.5 MB|