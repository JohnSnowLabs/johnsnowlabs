---
layout: model
title: Mapping ICD10CM Codes with Corresponding Causes and Claim Analysis Code
author: John Snow Labs
name: icd10cm_cause_claim_mapper
date: 2023-05-01
tags: [en, licensed, clinical, mapper, cause, claim, icd10cm]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

this mapper takes icd10 code and returns causes and claim analyses codes for each icd10 code.

## Predicted Entities

`icd10cm_cause`, `icd10cm_claim_analysis_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_cause_claim_mapper_en_4.4.0_3.0_1682952571606.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_cause_claim_mapper_en_4.4.0_3.0_1682952571606.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunk_assembler = Doc2Chunk()\
      .setInputCols("document")\
      .setOutputCol("icd_chunk")

chunkerMapper = ChunkMapperModel.pretrained("icd10cm_cause_claim_mapper", "en", "clinical/models")\
      .setInputCols(["icd_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["icd10cm_cause", "icd10cm_claim_analysis_code"])

pipeline = Pipeline().setStages([document_assembler,
                                 chunk_assembler,
                                 chunkerMapper])  

model = pipeline.fit(spark.createDataFrame([['']]).toDF('text')) 

lp = LightPipeline(model)

res = lp.fullAnnotate(["X99.9", "G43.83", "Z83.51"])
```
```scala
val document_assembler = new DocumentAssembler()
       .setInputCol("text")\
       .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()\
      .setInputCols("document")\
      .setOutputCol("icd_chunk")

val chunkerMapper = ChunkMapperModel
       .pretrained("icd10cm_cause_claim_mapper", "en", "clinical/models")
       .setInputCols(Array("icd_chunk"))
       .setOutputCol("mappings")
       .setRels(Array("icd10cm_cause", "icd10cm_claim_analysis_code")) 

val mapper_pipeline = new Pipeline().setStages(Array(document_assembler, chunk_assembler, chunkerMapper))

val data = Seq(Array("X99.9", "G43.83", "Z83.51")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+------+---------------------------------+---------------------------+
|icd10 |mappings                         |relation                   |
+------+---------------------------------+---------------------------+
|X99.9 |Physical violence by sharp object|icd10cm_cause              |
|X99.9 |X99.9                            |icd10cm_claim_analysis_code|
|G43.83|Migraine                         |icd10cm_cause              |
|G43.83|G43.83                           |icd10cm_claim_analysis_code|
|Z83.51|Digestive diseases               |icd10cm_cause              |
|Z83.51|NONE                             |icd10cm_claim_analysis_code|
+------+---------------------------------+---------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_cause_claim_mapper|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|550.0 KB|