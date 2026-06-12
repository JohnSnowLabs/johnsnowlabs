---
layout: model
title: SNOMED CT to UMLS Code Mapping
author: John Snow Labs
name: snomed_umls_mapper
date: 2026-06-12
tags: [en, chunk_mapper, licensed, clinical, umls, snomed]
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

This model maps SNOMED CT codes to UMLS codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapper_en_6.4.0_3.4_1781298933354.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapper_en_6.4.0_3.4_1781298933354.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

mapper = ChunkMapperModel.pretrained("snomed_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["73211009"],["69896004"],["22298006"]]).toDF("text")
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

mapper = medical.ChunkMapperModel.pretrained("snomed_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["73211009"],["69896004"],["22298006"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("doc")

val doc2chunk = new Doc2Chunk()
  .setInputCols(Array("doc"))
  .setOutputCol("ner_chunk")

val mapper = ChunkMapperModel.pretrained("snomed_umls_mapper","en","clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, doc2chunk, mapper))
import spark.implicits._
val data = Seq("73211009","69896004","22298006").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|   snomed_code | umls_code   |
|--------------:|:------------|
|      73211009 | C0011849    |
|      69896004 | C0003873    |
|      22298006 | C0027051    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_umls_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|5.5 MB|
