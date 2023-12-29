---
layout: model
title: Mapping HCPCS Codes  with Corresponding National Drug Codes (NDC) and Drug Brand Names
author: John Snow Labs
name: hcpcs_ndc_mapper
date: 2023-04-13
tags: [en, licensed, chunk_mappig, hcpcs, ndc, brand_name]
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

This pretrained model maps HCPCS codes with their corresponding National Drug Codes (NDC) and their drug brand names.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`ndc_code`, `brand_name`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcpcs_ndc_mapper_en_4.4.0_3.0_1681405950608.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcpcs_ndc_mapper_en_4.4.0_3.0_1681405950608.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("hcpcs_chunk")

chunkerMapper = DocMapperModel.pretrained("hcpcs_ndc_mapper", "en", "clinical/models")\
      .setInputCols(["hcpcs_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["ndc_code", "brand_name"])

pipeline = Pipeline().setStages([document_assembler,
                                 chunkerMapper])  

model = pipeline.fit(spark.createDataFrame([['']]).toDF('text')) 

lp = LightPipeline(model)

res = lp.fullAnnotate(["Q5106", "J9211", "J7508"])
```
```scala
val document_assembler = new DocumentAssembler()
       .setInputCol("text")\
       .setOutputCol("hcpcs_chunk")

val chunkerMapper = DocMapperModel
       .pretrained("hcpcs_ndc_mapper", "en", "clinical/models")
       .setInputCols(Array("hcpcs_chunk"))
       .setOutputCol("mappings")
       .setRels(Array("ndc_code", "brand_name")) 

val mapper_pipeline = new Pipeline().setStages(Array(
                                                   document_assembler,
                                                   chunkerMapper))


val data = Seq(Array(["Q5106", "J9211", "J7508"])).toDS.toDF("text")
val result = pipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+-----------+-------------------------------------+----------+
|hcpcs_chunk|mappings                             |relation  |
+-----------+-------------------------------------+----------+
|Q5106      |59353-0003-10                        |ndc_code  |
|Q5106      |RETACRIT (PF) 3000 U/1 ML            |brand_name|
|J9211      |59762-2596-01                        |ndc_code  |
|J9211      |IDARUBICIN HYDROCHLORIDE (PF) 1 MG/ML|brand_name|
|J7508      |00469-0687-73                        |ndc_code  |
|J7508      |ASTAGRAF XL 5 MG                     |brand_name|
+-----------+-------------------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcpcs_ndc_mapper|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|20.7 KB|