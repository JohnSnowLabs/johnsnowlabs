---
layout: model
title: Mapping ICD10CM Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: icd10cm_umls_mapper
date: 2024-12-10
tags: [umls, chunk_mapper, clinical, icd10cm, en, licensed]
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

This pretrained model maps ICD10CM codes to corresponding UMLS codes under the Unified Medical Language System (UMLS).

## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapper_en_5.5.1_3.0_1733847907484.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_umls_mapper_en_5.5.1_3.0_1733847907484.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('ner_chunk')

mapperModel = ChunkMapperModel.pretrained("icd10cm_umls_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["A01.2"], ["A01.00"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = medical.Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('ner_chunk')

mapperModel = medical.ChunkMapperModel.pretrained("icd10cm_umls_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["A01.2"], ["A01.00"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("ner_chunk")

val chunkerMapper = ChunkMapperModel
      .pretrained("icd10cm_umls_mapper", "en", "clinical/models")
      .setInputCols(Array("ner_chunk"))
      .setOutputCol("mappings")
      .setRels(Array("umls_code"))

val mapper_pipeline = new Pipeline().setStages(Array(
                                                  document_assembler,
                                                  chunk_assembler,
                                                  chunkerMapper))

val data = Seq("A01.2", "A01.00").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+------------+---------+---------+
|icd10cm_code|umls_code| relation|
+------------+---------+---------+
|       A01.2| C0343376|umls_code|
|      A01.00| C0041466|umls_code|
+------------+---------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_umls_mapper|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.4 MB|

## References

Trained on concepts from ICD10CM for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
