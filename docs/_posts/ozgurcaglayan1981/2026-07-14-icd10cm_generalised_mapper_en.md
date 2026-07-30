---
layout: model
title: Mapping ICD-10-CM codes with Their Corresponding general codes
author: John Snow Labs
name: icd10cm_generalised_mapper
date: 2026-07-14
tags: [en, chunk_mapper, licensed, clinical, icd10cm, generalised]
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

This pretrained model maps ICD-10-CM codes to their generalised 3-digit ICD-10-CM codes and the main concepts. Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_mapper_en_6.4.0_3.4_1784066939569.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_mapper_en_6.4.0_3.4_1784066939569.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

icd10cm_generalised_mapper = ChunkMapperModel.pretrained("icd10cm_generalised_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["generalised_code"])

pipeline = Pipeline(stages=[document_assembler, chunk_assembler, icd10cm_generalised_mapper])
data = spark.createDataFrame([["A00.0"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

chunk_assembler = nlp.Doc2Chunk()\
    .setInputCols(["document"])\
    .setOutputCol("ner_chunk")

icd10cm_generalised_mapper = medical.ChunkMapperModel.pretrained("icd10cm_generalised_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["generalised_code"])

pipeline = nlp.Pipeline(stages=[document_assembler, chunk_assembler, icd10cm_generalised_mapper])
data = spark.createDataFrame([["A00.0"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val chunkAssembler = new Doc2Chunk()
    .setInputCols("document")
    .setOutputCol("ner_chunk")

val icd10cm_generalised_mapper = ChunkMapperModel.pretrained("icd10cm_generalised_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("generalised_code"))

val pipeline = new Pipeline().setStages(Array(documentAssembler, chunkAssembler, icd10cm_generalised_mapper))
val data = Seq("A00.0").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| code   | generalised_code                                            |
|:-------|:------------------------------------------------------------|
| A00.0  | ['A00:Certain infectious and parasitic diseases']           |
| E11.9  | ['E11:Endocrine, nutritional and metabolic diseases']       |
| I10    | ['I10:Diseases of the circulatory system']                  |
| J44.9  | ['J44:Diseases of the respiratory system']                  |
| F32.9  | ['F32:Mental, Behavioral and Neurodevelopmental disorders'] |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_generalised_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.4 MB|