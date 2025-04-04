---
layout: model
title: Mapping UMLS Codes with Their Corresponding CPT Codes
author: John Snow Labs
name: umls_cpt_mapper
date: 2024-12-10
tags: [licensed, en, umls, cpt, mapping]
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

This pretrained model maps UMLS codes to corresponding CPT codes.

## Predicted Entities

`cpt_code`


## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('umls_code')

mapperModel = ChunkMapperModel.load("umls_cpt_mapper")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")


mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["C3248275"],["C3496535"],["C0973430"],["C3248301"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = medical.Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('umls_code')

mapperModel = medical.ChunkMapperModel.load("umls_cpt_mapper")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["C3248275"],["C3496535"],["C0973430"],["C3248301"]]).toDF("text")

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
      .load("umls_cpt_mapper")
      .setInputCols(Array("umls_code"))
      .setOutputCol("mappings")
      
val mapper_pipeline = Pipeline().setStages(Array(
                                                  document_assembler,
                                                  chunk_assembler,
                                                  chunkerMapper))

val data = Seq("C3248275","C3496535","C0973430","C3248301").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------+--------+
|umls_code|cpt_code|
+---------+--------+
|C3248275 |2016F   |
|C3496535 |48155   |
|C0973430 |64823   |
|C3248301 |4500F   |
+---------+--------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_cpt_mapper|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|617.4 KB|

## References

**CPT mapper models are removed from the Models Hub due to license restrictions and can only be shared with the users who already have a valid CPT license. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**

Trained on concepts from CPT for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
