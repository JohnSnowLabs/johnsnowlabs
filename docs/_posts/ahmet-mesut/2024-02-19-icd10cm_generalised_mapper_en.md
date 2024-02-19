---
layout: model
title: Mapping ICD-10-CM codes with Their Corresponding general codes
author: John Snow Labs
name: icd10cm_generalised_mapper
date: 2024-02-19
tags: [en, licensed, mapping, icd10_cm]
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

This pretrained model maps ICD-10-CM codes to their generalised 3-digit ICD-10-CM codes and their main concepts.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_mapper_en_5.2.1_3.0_1708356641248.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_mapper_en_5.2.1_3.0_1708356641248.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
	
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("icd10_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["icd10_code"])\
    .setOutputCol("icd102chunk")

chunkMapper = ChunkMapperModel.pretrained("icd10cm_generalised_mapper", "en", "clinical/models")\
    .setInputCols(["icd102chunk"])\
    .setOutputCol("mappings")\

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    icd10_resolver,
    resolver2chunk,
    chunkMapper])

data = spark.createDataFrame([["gestational diabetes mellitus"],["Chronic obstructive pulmonary disease"]]).toDF("text")

mapper_model = pipeline.fit(data)
result= mapper_model.transform(data)     
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("ner_chunk")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk"))
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)
	
val icd10_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented","en","clinical/models")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("icd10_code")
	.setDistanceFunction("EUCLIDEAN")
	
val resolver2chunk = new Resolution2Chunk()
	.setInputCols(Array("icd10_code"))
	.setOutputCol("icd102chunk")
	
val chunkMapper = ChunkMapperModel.pretrained("icd10cm_generalised_mapper","en","clinical/models")
	.setInputCols(Array("icd102chunk"))
	.setOutputCol("mappings")
	
val Pipeline(stages = Array(
    documentAssembler,
    sbert_embedder,
    icd10_resolver,
    resolver2chunk,
    chunkMapper))
	
val data = Seq("gestational diabetes mellitus"),Array("Chronic obstructive pulmonary disease") .toDF("text")
	
val mapper_model = pipeline.fit(data)
result= mapper_model.transform(data)
```
</div>

## Results

```bash
+-------------------------------------+------------+--------------------------------------------+
|chunk                                |icd10cm_code|generalised_code                            |
+-------------------------------------+------------+--------------------------------------------+
|gestational diabetes mellitus        |O24.4       |O24:Pregnancy, childbirth and the puerperium|
|Chronic obstructive pulmonary disease|J44.9       |J44:Diseases of the respiratory system      |
+-------------------------------------+------------+--------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_generalised_mapper|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|1.3 MB|
