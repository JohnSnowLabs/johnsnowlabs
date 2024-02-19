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

This pretrained model maps LOINC codes to corresponding UMLS codes.

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
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

loinc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("loinc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["loinc_code"])\
    .setOutputCol("loinc2chunk")

chunkMapper = ChunkMapperModel.pretrained("loinc_umls_mapper", "en", "clinical/models")\
    .setInputCols(["loinc2chunk"])\
    .setOutputCol("mappings")\

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    loinc_resolver,
    resolver2chunk,
    chunkMapper])

data = spark.createDataFrame([["aspirin"]]).toDF("text")

mapper_model = pipeline.fit(data)
result= mapper_model.transform(data)                                 
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
  .setInputCols(Array("ner_chunk"))
  .setOutputCol("sbert_embeddings")
  .setCaseSensitive(false)

val loinc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_augmented", "en", "clinical/models")
  .setInputCols(Array("sbert_embeddings"))
  .setOutputCol("loinc_code")
  .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = new Resolution2Chunk()
  .setInputCols(Array("loinc_code"))
  .setOutputCol("loinc2chunk")

val chunkMapper = ChunkMapperModel.pretrained("loinc_umls_mapper", "en", "clinical/models")
  .setInputCols(Array("loinc2chunk"))
  .setOutputCol("mappings")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sbert_embedder,
  loinc_resolver,
  resolver2chunk,
  chunkMapper
))

val data = spark.createDataFrame(Seq(("aspirin"))).toDF("text")

val mapper_model = pipeline.fit(data)
val result = mapper_model.transform(data)

```
</div>

## Results

```bash
+-------+----------+---------+
|chunk  |loinc_code|umls_code|
+-------+----------+---------+
|aspirin|LA26702-3 |C0004057 |
+-------+----------+---------+
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
