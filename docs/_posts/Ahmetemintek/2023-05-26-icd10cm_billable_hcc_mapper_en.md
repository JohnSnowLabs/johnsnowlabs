---
layout: model
title: Mapping ICD-10-CM Codes with Corresponding Billable and Hierarchical Condition Category (HCC) Scores
author: John Snow Labs
name: icd10cm_billable_hcc_mapper
date: 2023-05-26
tags: [icd10cm, billable, hcc_score, clinical, en, chunk_mapping, licensed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: DocMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps ICD-10-CM codes with their corresponding billable and HCC scores. If there is no HCC score for the corresponding ICD-10-CM code, result will be returned as 0.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`billable`, `hcc_score`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_billable_hcc_mapper_en_4.4.2_3.0_1685107034729.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_billable_hcc_mapper_en_4.4.2_3.0_1685107034729.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

docMapper= DocMapperModel().pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("mappings")\
    .setRels(["billable", "hcc_score"]) \
    .setLowerCase(True) \
    .setMultivaluesRelations(True)

pipeline = Pipeline().setStages([
    document_assembler,
    docMapper])


data = spark.createDataFrame([["D66"], ["S22.00"], ["Z3A.10"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val docMapper = DocMapperModel.pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("mappings")
    .setRels(Array(["billable", "hcc_score"]))

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    docMapper))


val data = Seq(["D66"], ["S22.00"], ["Z3A.10"]).toDS.toDF("text")

val result= pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------+----------+-----------+
| icd10cm_code | billable | hcc_score |
+--------------+----------+-----------+
| D66          | 1        | 46        |
| S22.00       | 0        | 0         |
| Z3A.10       | 1        | 0         |
+--------------+----------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_billable_hcc_mapper|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.1 MB|
