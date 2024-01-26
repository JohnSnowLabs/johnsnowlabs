---
layout: model
title: Mapping ICD-10-CM Codes with Corresponding Medicare Severity-Diagnosis Related Group (MS-DRG)
author: John Snow Labs
name: icd10cm_ms_drg_mapper
date: 2023-08-08
tags: [icd10cm, ms_drg, chunk_mapper, clinical, en, licensed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: DocMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps ICD-10-CM codes with their corresponding Medicare Severity-Diagnosis Related Group (MS-DRG).

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`ms-drg`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_ms_drg_mapper_en_5.0.1_3.0_1691506250054.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_ms_drg_mapper_en_5.0.1_3.0_1691506250054.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

chunkMapper = DocMapperModel.pretrained("icd10cm_ms_drg_mapper", "en", "clinical/models")\
      .setInputCols(["icd_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["ms-drg"])

pipeline = Pipeline().setStages([document_assembler,
                                 chunkMapper])  

model = pipeline.fit(spark.createDataFrame([['']]).toDF('text')) 

lp = LightPipeline(model)

res = lp.fullAnnotate(["L08.1", "U07.1", "C10.0", "J351"])
```
```scala
val document_assembler = new DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("document")

val chunkMapper = DocMapperModel.pretrained("icd10cm_ms_drg_mapper", "en", "clinical/models")
      .setInputCols(Array("icd_chunk"))
      .setOutputCol("mappings")
      .setRels(Array("ms-drg")) 

val mapper_pipeline = new Pipeline().setStages(Array(document_assembler, chunkMapper))

val data = Seq(Array("L08.1", "U07.1", "C10.0", "J351")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+----------+-------------------------------+
|icd10_code|ms-drg                         |
+----------+-------------------------------+
|L08.1     |Erythrasma                     |
|U07.1     |COVID-19                       |
|C10.0     |Malignant neoplasm of vallecula|
|J351      |Hypertrophy of tonsils         |
+----------+-------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_ms_drg_mapper|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|3.6 MB|

## References

This model was trained with data from https://www.icd10data.com/ICD10CM/DRG/Amp