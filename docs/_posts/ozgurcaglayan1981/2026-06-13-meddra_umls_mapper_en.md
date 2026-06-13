---
layout: model
title: Mapping MedDRA Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: meddra_umls_mapper
date: 2026-06-13
tags: [en, chunk_mapper, licensed, clinical, umls, meddra]
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

This model maps MedDRA codes to UMLS codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. MedDRA mapper models are removed from the Models Hub due to license restrictions and can only be shared with the users who already have a valid MedDRA license. Please contact support@johnsnowlabs.com for access.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}

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

mapper = ChunkMapperModel.pretrained("meddra_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["10012594"],["10003268"],["10047699"]]).toDF("text")
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

mapper = medical.ChunkMapperModel.pretrained("meddra_umls_mapper","en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")

pipeline = nlp.Pipeline(stages=[document_assembler, doc2chunk, mapper])
data = spark.createDataFrame([["10012594"],["10003268"],["10047699"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("doc")

val doc2chunk = new Doc2Chunk()
  .setInputCols(Array("doc"))
  .setOutputCol("ner_chunk")

val mapper = ChunkMapperModel.pretrained("meddra_umls_mapper","en","clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, doc2chunk, mapper))
val data = Seq("10012594","10003268","10047699").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|   meddra_code | umls_code   |
|--------------:|:------------|
|      10012594 | C0011849    |
|      10003268 | C0003873    |
|      10047699 | C0042963    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_umls_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|739.9 KB|
