---
layout: model
title: Mapping National Drug Codes (NDC) Codes with Corresponding Drug Brand Names
author: John Snow Labs
name: ndc_drug_brandname_mapper
date: 2026-07-26
tags: [en, chunk_mapper, licensed, clinical, ndc, drug_brandname]
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

This pretrained model maps National Drug Codes (NDC) codes with their corresponding drug brand names. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_drug_brandname_mapper_en_6.4.0_3.4_1785071156813.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_drug_brandname_mapper_en_6.4.0_3.4_1785071156813.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("chunk")

chunkerMapper = ChunkMapperModel.pretrained("ndc_drug_brandname_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("mappings")\
    .setRels(["drug_brand_name"])

pipeline = Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["57894-150"], ["0363-0221"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

doc2chunk = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("ndc_drug_brandname_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("mappings")\
    .setRels(["drug_brand_name"])

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["57894-150"], ["0363-0221"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val doc2chunk = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("chunk")

val chunkerMapper = ChunkMapperModel
    .pretrained("ndc_drug_brandname_mapper", "en", "clinical/models")
    .setInputCols(Array("chunk"))
    .setOutputCol("mappings")
    .setRels(Array("drug_brand_name"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    doc2chunk,
    chunkerMapper
))

val data = Seq("57894-150", "0363-0221").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| NDC Code   | drug_brand_name   |
|:-----------|:------------------|
| 57894-150  | Zytiga            |
| 0363-0221  | Ibuprofen         |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_drug_brandname_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[chunk]|
|Output Labels:|[brandname]|
|Language:|en|
|Size:|2.7 MB|
