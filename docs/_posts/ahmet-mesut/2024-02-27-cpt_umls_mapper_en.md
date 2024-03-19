---
layout: model
title: Mapping CPT Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: cpt_umls_mapper
date: 2024-02-27
tags: [en, licensed, cpt, umls, mapping]
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

This pretrained model maps CPT codes to corresponding UMLS codes.

## Predicted Entities

`umls_code`

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
    .setOutputCol('cpt_code')
 
mapperModel = ChunkMapperModel.load("cpt_umls_mapper")\
    .setInputCols(["cpt_code"])\
    .setOutputCol("mappings")\

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    chunk_assembler,
    mapperModel
])

data = spark.createDataFrame([["2016F"],["48155"],["64823"],["4500F"]]).toDF("text")

mapper_model = mapper_pipeline.fit(data)
result= mapper_model.transform(data)                                 
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("doc")
	
val chunk_assembler = new Doc2Chunk()
    .setInputCols(Array("doc"))
    .setOutputCol("cpt_code")
	
val mapperModel = ChunkMapperModel.load("cpt_umls_mapper")
    .setInputCols(Array("cpt_code"))
    .setOutputCol("mappings")
	
val mapper_pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    chunk_assembler, 
    mapperModel ))
	
val data = Seq("2016F", "48155", "64823", "4500F").toDF("text")
	
val mapper_model = mapper_pipeline.fit(data)
result= mapper_model.transform(data)
```
</div>

## Results

```bash
+--------+---------+
|cpt_code|umls_code|
+--------+---------+
|2016F   |C3248275 |
|48155   |C0040511 |
|64823   |C0973430 |
|4500F   |C3248301 |
+--------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_umls_mapper|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|319.8 KB|

## References

**CPT resolver models are removed from the Models Hub due to license restrictions and can only be shared with the users who already have a valid CPT license. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**
