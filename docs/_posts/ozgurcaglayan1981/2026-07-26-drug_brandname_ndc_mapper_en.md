---
layout: model
title: Mapping Drug Brand Names with Corresponding National Drug Codes
author: John Snow Labs
name: drug_brandname_ndc_mapper
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

This pretrained clinical model performs the task of mapping pharmaceutical brand names to their corresponding National Drug Codes (NDC). The model returns product NDCs for each dosage strength in both the result and metadata fields. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_brandname_ndc_mapper_en_6.4.0_3.4_1785026627678.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_brandname_ndc_mapper_en_6.4.0_3.4_1785026627678.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

chunkerMapper = ChunkMapperModel.pretrained("drug_brandname_ndc_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("ndc")\
    .setRels(["Strength_NDC"])\
    .setLowerCase(True)

pipeline = Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["zytiga"], ["lipitor"], ["crestor"]]).toDF("text")
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

chunkerMapper = medical.ChunkMapperModel.pretrained("drug_brandname_ndc_mapper", "en", "clinical/models")\
    .setInputCols(["chunk"])\
    .setOutputCol("ndc")\
    .setRels(["Strength_NDC"])\
    .setLowerCase(True)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    doc2chunk,
    chunkerMapper
])

data = spark.createDataFrame([["zytiga"], ["lipitor"], ["crestor"]]).toDF("text")
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
    .pretrained("drug_brandname_ndc_mapper", "en", "clinical/models")
    .setInputCols(Array("chunk"))
    .setOutputCol("ndc")
    .setRels(Array("Strength_NDC"))
    .setLowerCase(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    doc2chunk,
    chunkerMapper
))

val data = Seq("zytiga", "lipitor", "crestor").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| Brandname   | Strength_NDC         | All_K_Resolutions                                                                     |
|:------------|:---------------------|:--------------------------------------------------------------------------------------|
| zytiga      | 250 mg/1 | 57894-150 | 250 mg/1 | 57894-150:::500 mg/1 | 57894-195                                           |
| lipitor     | 20 mg/1 | 58151-156  | 20 mg/1 | 58151-156:::80 mg/1 | 58151-158:::10 mg/1 | 58151-155:::40 mg/1 | 58151-157 |
| crestor     | 10 mg/1 | 0310-7570  | 10 mg/1 | 0310-7570:::20 mg/1 | 0310-7580:::40 mg/1 | 0310-7590:::5 mg/1 | 0310-7560  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_brandname_ndc_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[chunk]|
|Output Labels:|[ndc]|
|Language:|en|
|Size:|1.7 MB|