---
layout: model
title: Mapping ICD10CM Codes with Corresponding Causes and Claim Analysis Codes
author: John Snow Labs
name: icd10cm_cause_claim_mapper
date: 2023-05-11
tags: [en, licensed, chunk_mapping, icd10cm, cause, claim]
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

This pretrained model maps ICD-10-CM codes, subsequently providing corresponding causes and generating claim analysis codes for each respective ICD-10-CM code. If there is no equivalent claim analysis code, the result will be `None`.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`icd10cm_cause`, `icd10cm_claim_analysis_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_cause_claim_mapper_en_4.4.0_3.0_1683819210044.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_cause_claim_mapper_en_4.4.0_3.0_1683819210044.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

res = lp.fullAnnotate(["D69.51", "G43.83", "A18.03"])
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunk_assembler = new Doc2Chunk()
      .setInputCols("document")
      .setOutputCol("icd_chunk")

val chunkerMapper = ChunkMapperModel.pretrained("icd10cm_cause_claim_mapper", "en", "clinical/models")
      .setInputCols(Array("icd_chunk"))
      .setOutputCol("mappings")
      .setRels(Array("icd10cm_cause", "icd10cm_claim_analysis_code")) 

val mapper_pipeline = new Pipeline().setStages(Array(document_assembler, chunk_assembler, chunkerMapper))

val data = Seq(Array("D69.51", "G43.83", "A18.03")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+------------+------------------------------------+---------------------------+
|icd10cm_code|cause                               |icd10cm_claim_analysis_code|
+------------+------------------------------------+---------------------------+
|D69.51      |Unintentional injuries              |D69.51                     |
|D69.51      |Adverse effects of medical treatment|D69.51                     |
|G43.83      |Headache disorders                  |G43.83                     |
|G43.83      |Tension-type headache               |G43.83                     |
|G43.83      |Migraine                            |G43.83                     |
|A18.03      |Whooping cough                      |A18.03                     |  
+------------+------------------------------------+---------------------------+
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
|Size:|600.2 KB|
