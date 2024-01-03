---
layout: model
title: Mapping National Drug Codes (NDC) with Corresponding HCPCS Codes and Descriptions
author: John Snow Labs
name: ndc_hcpcs_mapper
date: 2023-04-13
tags: [en, licensed, clinical, chunk_mapping, ndc, hcpcs, brand_name]
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

This pretrained model maps National Drug Codes (NDC) with their corresponding HCPCS codes and their descriptions.

`Important Note`: Mappers extract additional information such as extended descriptions and categories related to Concept codes (such as RxNorm, ICD10, CPT, MESH, NDC, UMLS, etc.). They generally take Concept Codes, which are the outputs of EntityResolvers, as input. When creating a pipeline that contains 'Mapper', it is necessary to use the ChunkMapperModel after an EntityResolverModel.


## Predicted Entities

`hcpcs_code`, `hcpcs_description`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_hcpcs_mapper_en_4.4.0_3.0_1681405091593.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_hcpcs_mapper_en_4.4.0_3.0_1681405091593.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ndc_chunk")

chunkerMapper = DocMapperModel.pretrained("ndc_hcpcs_mapper", "en", "clinical/models")\
      .setInputCols(["ndc_chunk"])\
      .setOutputCol("hcpcs")\
      .setRels(["hcpcs_code", "hcpcs_description"])

pipeline = Pipeline().setStages([document_assembler,
                                 chunkerMapper])  

model = pipeline.fit(spark.createDataFrame([['']]).toDF('text')) 

lp = LightPipeline(model)

res = lp.fullAnnotate(["16714-0892-01", "00990-6138-03", "43598-0650-11"])
```
```scala
val document_assembler = new DocumentAssembler()
       .setInputCol("text")\
       .setOutputCol("ndc_chunk")

val chunkerMapper = DocMapperModel
       .pretrained("ndc_hcpcs_mapper", "en", "clinical/models")
       .setInputCols(Array("ndc_chunk"))
       .setOutputCol("mappings")
       .setRels(Array("hcpcs_code", "hcpcs_description")) 

val mapper_pipeline = new Pipeline().setStages(Array(
                                                   document_assembler,
                                                   chunkerMapper))


val data = Seq(Array("16714-0892-01", "00990-6138-03", "43598-0650-11")).toDS.toDF("text")
val result = pipeline.fit(data).transform(data) 
```
</div>

## Results

```bash
+-------------+----------------------------+-----------------+
|ndc_chunk    |mappings                    |relation         |
+-------------+----------------------------+-----------------+
|16714-0892-01|J0878                       |hcpcs_code       |
|16714-0892-01|INJECTION, DAPTOMYCIN, 1 MG |hcpcs_description|
|00990-6138-03|A4217                       |hcpcs_code       |
|00990-6138-03|STERILE WATER/SALINE, 500 ML|hcpcs_description|
|43598-0650-11|J9340                       |hcpcs_code       |
|43598-0650-11|INJECTION, THIOTEPA, 15 MG  |hcpcs_description|
+-------------+----------------------------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_hcpcs_mapper|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|203.1 KB|