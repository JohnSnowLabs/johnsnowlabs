---
layout: model
title: Mapping MedDRA-HLT (High Level Term) Codes With Their Corresponding MedDRA-PT (Preferred Term) Codes
author: John Snow Labs
name: meddra_hlt_pt_mapper
date: 2024-03-28
tags: [licensed, en, hlt, pt, meddra, mapping]
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

This pretrained model maps MedDRA-HLT (High Level Term) codes to their corresponding MedDRA-PT (Preferred Term) codes. Some of the MedDRA HLT codes map to more than one MedDRA PT codes. You can find all the mapped MedDRA PT codes in the `all_k_resolutions` column in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
      .setInputCol('text')\
      .setOutputCol('doc')

chunk_assembler = Doc2Chunk()\
      .setInputCols(['doc'])\
      .setOutputCol('hlt_code')
 
mapperModel = ChunkMapperModel.load('meddra_hlt_pt_mapper')\
    .setInputCols(["hlt_code"])\
    .setOutputCol("pt_mappings")\
    .setRels(["pt_code"])


mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["10000135"], ["10017329"], ["10000332"]]).toDF("text")

mapper_model = mapper_pipeline.fit(data)
result = mapper_model.transform(data)
```
```scala
val document_assembler = DocumentAssembler()
      .setInputCol("text")
      .setOutputCol("doc")

val chunk_assembler = Doc2Chunk()
      .setInputCols(Array("doc"))
      .setOutputCol("hlt_code")
 
val mapperModel = ChunkMapperModel.load("meddra_hlt_pt_mapper")
    .setInputCols(Array("hlt_code"))
    .setOutputCol("pt_mappings")
    .setRels(Array("pt_code"))


val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler,
    chunk_assembler,
    mapperModel
)

val data = Seq("10000135", "10017329", "10000332").toDF("text")

val mapper_model = mapper_pipeline.fit(data)
val result = mapper_model.transform(data)
```
</div>

## Results

```bash
+--------+-----------------------------+---------------------------------------------------------------------------------------------------------------+
|hlt_code|pt_mappings                  |all_k_resolutions                                                                                              |
+--------+-----------------------------+---------------------------------------------------------------------------------------------------------------+
|10000135|10037544:Purging             |10037544:Purging:::10048636:Self-induced vomiting                                                              |
|10017329|10035736:Pneumonia tularaemia|10035736:Pneumonia tularaemia:::10045146:Tularaemia                                                            |
|10000332|10034759:Petit mal epilepsy  |10034759:Petit mal epilepsy:::10083376:Generalised onset non-motor seizure:::10085031:Juvenile absence epilepsy|
+--------+-----------------------------+---------------------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_hlt_pt_mapper|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[pt_mappings]|
|Language:|en|
|Size:|499.2 KB|

## References

This model is trained with the v27 MedDRA dataset.

**To utilize this model, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**
