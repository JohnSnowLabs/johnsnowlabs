---
layout: model
title: Mapping MedDRA-PT (Preferred Term) Codes With Their Corresponding MedDRA-LLT (Lowest Level Term) Codes
author: John Snow Labs
name: meddra_pt_llt_mapper
date: 2024-03-18
tags: [licensed, en, llt, pt, mapper, meddra, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps MedDRA-PT (Preferred Term) codes to their corresponding MedDRA-LLT (Lowest Level Term) codes. Some of the MedDRA PT codes map to more than MedDRA LLT codes. You can find all the mapped MedDRA LLT codes in the `all_k_resolutions` column in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/meddra_pt_llt_mapper_en_5.3.0_3.0_1710776754238.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/meddra_pt_llt_mapper_en_5.3.0_3.0_1710776754238.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
 
mapperModel = ChunkMapperModel.load('meddra_pt_llt_mapper')\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["llt_code"])


mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["10008684"], ["10014472"], ["10019785"]]).toDF("text")

mapper_model = mapper_pipeline.fit(data)
result = mapper_model.transform(data)
```
```scala
val document_assembler = DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("doc")

val chunk_assembler = Doc2Chunk()
      .setInputCols(Array("doc"))
      .setOutputCol("ner_chunk")
 
val mapperModel = ChunkMapperModel.load("meddra_pt_llt_mapper")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("llt_code"))


val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
)

val data = Seq("10008684", "10014472", "10019785").toDF("text")

val mapper_model = mapper_pipeline.fit(data)
val result = mapper_model.transform(data)
```
</div>

## Results

```bash
+--------+---------------------------+--------------------------------------------------------------+
|pt_code |llt_code                   |all_k_resolutions                                             |
+--------+---------------------------+--------------------------------------------------------------+
|10008684|10004711:Biliuria          |10004711:Biliuria:::10008684:Choluria:::10046617:Urine bilious|
|10014472|10014472:Elephantiasis     |10014472:Elephantiasis:::10014473:Elephantiasis of eyelid     |
|10019785|10019785:Hepatitis neonatal|10019785:Hepatitis neonatal:::                                |
+--------+---------------------------+--------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_pt_llt_mapper|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.3 MB|