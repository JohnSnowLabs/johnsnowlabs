---
layout: model
title: Mapping HCPCS Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: hcpcs_umls_mapper
date: 2026-06-13
tags: [en, chunk_mapper, licensed, clinical, umls, hcpcs]
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

This model maps HCPCS codes to UMLS codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcpcs_umls_mapper_en_6.4.0_3.4_1781311212004.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcpcs_umls_mapper_en_6.4.0_3.4_1781311212004.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

mapper = ChunkMapperModel.pretrained("hcpcs_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["E0100"],["A9150"],["S8040"]]).toDF("text")
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

mapper = medical.ChunkMapperModel.pretrained("hcpcs_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["E0100"],["A9150"],["S8040"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("doc")

val doc2chunk = new Doc2Chunk()
  .setInputCols(Array("doc"))
  .setOutputCol("ner_chunk")

val mapper = ChunkMapperModel.pretrained("hcpcs_umls_mapper","en","clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, doc2chunk, mapper))
val data = Seq("E0100","A9150","S8040").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| hcpcs_code   | umls_code   |
|:-------------|:------------|
| E0100        | C0006856    |
| A9150        | C0013231    |
| S8040        | C0040469    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcpcs_umls_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings_c2u]|
|Language:|en|
|Size:|99.9 KB|