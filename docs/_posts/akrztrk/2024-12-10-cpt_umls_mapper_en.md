---
layout: model
title: Mapping CPT Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: cpt_umls_mapper
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

This pretrained model maps CPT codes to corresponding UMLS codes.

## Predicted Entities

`umls_code`


## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('cpt_code')

mapperModel = ChunkMapperModel.load("cpt_umls_mapper")\
    .setInputCols(["cpt_code"])\
    .setOutputCol("mappings")

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["2016F"],["48155"],["64823"],["4500F"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('document')

chunk_assembler = medical.Doc2Chunk()\
      .setInputCols(['document'])\
      .setOutputCol('cpt_code')

mapperModel = medical.ChunkMapperModel.load("cpt_umls_mapper")\
    .setInputCols(["cpt_code"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["2016F"],["48155"],["64823"],["4500F"]]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("cpt_code")

val chunkerMapper = ChunkMapperModel
      .load("cpt_umls_mapper")
      .setInputCols(Array("cpt_code"))
      .setOutputCol("mappings")

val mapper_pipeline = new Pipeline().setStages(Array(
                                                  document_assembler,
                                                  chunk_assembler,
                                                  chunkerMapper))

val data = Seq("2016F","48155","64823","4500F").toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+--------+---------+
|cpt_code|umls_code|
+--------+---------+
|2016F   |C3248275 |
|48155   |C0040511 |
|64823   |C0973430 |
|4500F   |C3248301 |
+--------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_umls_mapper|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|324.5 KB|

## References

**CPT resolver models are removed from the Models Hub due to license restrictions and can only be shared with the users who already have a valid CPT license. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**

Trained on concepts from CPT for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
