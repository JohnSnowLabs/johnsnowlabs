---
layout: model
title: Mapping ICD-10-CM Codes with Corresponding Billable and Hierarchical Condition Category (HCC) Scores
author: John Snow Labs
name: icd10cm_billable_hcc_mapper
date: 2026-07-14
tags: [icd10cm, billable, hcc_score, clinical, en, chunk_mapping, licensed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: DocMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps ICD-10-CM codes with their corresponding billable and HCC scores. If there is no HCC score for the corresponding ICD-10-CM code, result will be returned as 0. Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_billable_hcc_mapper_en_6.4.0_3.4_1784068061854.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_billable_hcc_mapper_en_6.4.0_3.4_1784068061854.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

icd10cm_billable_hcc_mapper = DocMapperModel.pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mappings")\
    .setRels(['billable', 'hcc_score'])\
    .setLowerCase(True)\
    .setMultivaluesRelations(True)

pipeline = Pipeline(stages=[document_assembler, icd10cm_billable_hcc_mapper])
data = spark.createDataFrame([["A00.0"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

icd10cm_billable_hcc_mapper = medical.DocMapperModel.pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mappings")\
    .setRels(['billable', 'hcc_score'])\
    .setLowerCase(True)\
    .setMultivaluesRelations(True)

pipeline = nlp.Pipeline(stages=[document_assembler, icd10cm_billable_hcc_mapper])
data = spark.createDataFrame([["A00.0"]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val icd10cm_billable_hcc_mapper = DocMapperModel.pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("mappings")
    .setRels(Array("billable", "hcc_score"))
    .setLowerCase(true)
    .setMultivaluesRelations(true)

val pipeline = new Pipeline().setStages(Array(documentAssembler, icd10cm_billable_hcc_mapper))
val data = Seq("A00.0").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| code   |   billable |   hcc_score |
|:-------|-----------:|------------:|
| A00.0  |          1 |           0 |
| E11.9  |          1 |          38 |
| I10    |          1 |           0 |
| J44.9  |          1 |         280 |
| K35.20 |          0 |           0 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_billable_hcc_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.1 MB|