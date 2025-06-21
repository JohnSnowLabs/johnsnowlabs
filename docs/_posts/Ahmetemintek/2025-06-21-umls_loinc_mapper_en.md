---
layout: model
title: Mapping UMLS Codes with Their Corresponding LOINC Codes
author: John Snow Labs
name: umls_loinc_mapper
date: 2025-06-21
tags: [licensed, en, umls, loinc, mapping]
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

This pretrained model maps UMLS codes to corresponding LOINC codes.

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_loinc_mapper_en_6.0.2_3.0_1750534183554.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_loinc_mapper_en_6.0.2_3.0_1750534183554.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

chunkerMapper = ChunkMapperModel.pretrained("umls_loinc_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C0000530"],["C0000726"],["C0000343"],["C0000714"]]).toDF("text")

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

chunkerMapper = medical.ChunkMapperModel.pretrained("umls_loinc_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunkAssembler,
    chunkerMapper
])

data = spark.createDataFrame([["C0000530"],["C0000726"],["C0000343"],["C0000714"]]).toDF("text")

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
      .pretrained("umls_loinc_mapper", "en", "clinical/models")
      .setInputCols(Array("umls_code"))
      .setOutputCol("mappings")

val mapper_pipeline = Pipeline().setStages(Array(
                                            document_assembler,
                                            chunk_assembler,
                                            chunkerMapper))

val data = Seq("C0000530","C0000726","C0000343","C0000714").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+---------+----------+
|umls_code|loinc_code|
+---------+----------+
|C0000530 |LP15844-1 |
|C0000726 |MTHU059270|
|C0000343 |MTHU063786|
|C0000714 |LP101132-1|
+---------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_loinc_mapper|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|3.4 MB|

## References

Trained on concepts from LOINC for the 2025AA release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html