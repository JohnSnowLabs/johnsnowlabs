---
layout: model
title: Mapping LOINC Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: loinc_umls_mapper
date: 2024-02-19
tags: [en, licensed, umls, loinc, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps LOINC codes to corresponding UMLS codes

## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_umls_mapper_en_5.2.1_3.0_1708342975915.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_umls_mapper_en_5.2.1_3.0_1708342975915.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('doc')

chunk_assembler = Doc2Chunk()\
    .setInputCols(['doc'])\
    .setOutputCol('ner_chunk')
 
mapperModel = ChunkMapperModel..pretrained("loinc_umls_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["LP199956-6"]]).toDF("text")

mapper_model = mapper_pipeline.fit(data)
result= mapper_model.transform(data)                                 
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("doc")

val chunkAssembler = new ChunkAssembler()
  .setInputCols(Array("doc"))
  .setOutputCol("ner_chunk")

val mapperModel = PretrainedPipeline("loinc_umls_mapper", "en", "clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("mappings")
  .setRels(Array("umls_code"))

val mapperPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  chunkAssembler,
  mapperModel
))

val data = Seq("LP199956-6").toDF("text")

val mapperModelFit = mapperPipeline.fit(data)
val result = mapperModelFit.transform(data)

```
</div>

## Results

```bash
+----------+---------+-----------------+
|loinc_code|umls_code|relation         |
+----------+---------+-----------------+
|LP199956-6|C0000726 |umls_code        |
+----------+---------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_umls_mapper|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.9 MB|
