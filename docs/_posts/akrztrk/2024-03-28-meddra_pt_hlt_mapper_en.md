---
layout: model
title: Mapping MedDRA MedDRA PT (Preferred Term) Codes With Their Corresponding MedDRA HLT (High Level Term) Codes
author: John Snow Labs
name: meddra_pt_hlt_mapper
date: 2024-03-28
tags: [licensed, en, meddra, hlt, pt, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps MedDRA PT (Preferred Term) to corresponding MedDRA HLT (High Level Term) codes. Some of the MedDRA PT codes map to more than one MedDRA HLT codes. You can find all the mapped MedDRA HLT codes in the `all_k_resolutions` column in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/meddra_pt_hlt_mapper_en_5.3.1_3.0_1711628019391.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/meddra_pt_hlt_mapper_en_5.3.1_3.0_1711628019391.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('doc')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['doc'])\
      .setOutputCol('pt_code')
 
mapperModel = ChunkMapperModel.load('meddra_pt_hlt_mapper')\
    .setInputCols(["pt_code"])\
    .setOutputCol("hlt_mapping")\
    .setRels(["hlt_code"])


pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["10014468"], ["10017677"], ["10014490"]]).toDF("text")

mapper_model = pipeline.fit(data)
result = mapper_model.transform(data)
```
```scala
val document_assembler = DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("doc")

val chunk_assembler = Doc2Chunk()
      .setInputCols(Array("doc"))
      .setOutputCol("pt_code")
 
val mapperModel = ChunkMapperModel.load("meddra_pt_hlt_mapper")
    .setInputCols(Array("pt_code"))
    .setOutputCol("hlt_mapping")
    .setRels(["hlt_code"])


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel))

val data = Seq("10014468", "10017677", "10014490").toDF("text")

val mapper_model = pipeline.fit(data)
val result = mapper_model.transform(data)
```
</div>

## Results

```bash
+--------+------------------------------------------------+------------------------------------------------------------------------------------------------------+
|pt_code |hlt_mapping                                     |all_k_resolutions                                                                                     |
+--------+------------------------------------------------+------------------------------------------------------------------------------------------------------+
|10014468|10036998:Protein analyses NEC                   |10036998:Protein analyses NEC:::                                                                      |
|10017677|10006304:Breast radiotherapies                  |10006304:Breast radiotherapies:::                                                                     |
|10014490|10018848:Haematological disorders congenital NEC|10018848:Haematological disorders congenital NEC:::10038185:Red cell membrane and enzyme abnormalities|
+--------+------------------------------------------------+------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_pt_hlt_mapper|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|680.8 KB|

## References

This model is trained with the v27 MedDRA dataset.

**To utilize this model, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**
