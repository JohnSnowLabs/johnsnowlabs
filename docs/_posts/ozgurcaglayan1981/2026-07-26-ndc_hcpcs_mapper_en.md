---
layout: model
title: Mapping National Drug Codes (NDC) with Corresponding HCPCS Codes and Descriptions
author: John Snow Labs
name: ndc_hcpcs_mapper
date: 2026-07-26
tags: [en, chunk_mapper, licensed, clinical, ndc, hcpcs]
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

This pretrained model establishes mappings between National Drug Codes and their corresponding HCPCS codes along with descriptions. Trained on the PDAC NDC/HCPCS Crosswalk (release pdac-2026-07-05).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_hcpcs_mapper_en_6.4.0_3.4_1785072058210.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_hcpcs_mapper_en_6.4.0_3.4_1785072058210.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

chunkerMapper = ChunkMapperModel.pretrained("ndc_hcpcs_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("hcpcs")\
    .setRels(["hcpcs_code", "hcpcs_description"])

pipeline = Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["16714-0892-01"], ["00990-6138-03"], ["43598-0650-11"]]).toDF("text")
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

chunkerMapper = medical.ChunkMapperModel.pretrained("ndc_hcpcs_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("hcpcs")\
    .setRels(["hcpcs_code", "hcpcs_description"])

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["16714-0892-01"], ["00990-6138-03"], ["43598-0650-11"]]).toDF("text")
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
    .pretrained("ndc_hcpcs_mapper", "en", "clinical/models")
    .setInputCols(Array("chunk"))
    .setOutputCol("hcpcs")
    .setRels(Array("hcpcs_code", "hcpcs_description"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    doc2chunk,
    chunkerMapper
))

val data = Seq("16714-0892-01", "00990-6138-03", "43598-0650-11").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| NDC Code      | HCPCS Code   | HCPCS Description                                  |
|:--------------|:-------------|:---------------------------------------------------|
| 16714-0892-01 | J0878        | INJECTION, DAPTOMYCIN, 1 MG                        |
| 00990-6138-03 | A4217        | STERILE WATER/SALINE, 500 ML                       |
| 43598-0650-11 | J9342        | INJECTION, THIOTEPA, NOT OTHERWISE SPECIFIED, 1 MG |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_hcpcs_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|179.2 KB|
