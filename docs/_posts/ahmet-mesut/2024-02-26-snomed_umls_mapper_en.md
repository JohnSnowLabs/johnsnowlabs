---
layout: model
title: Mapping SNOMED Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: snomed_umls_mapper
date: 2024-02-26
tags: [licensed, en, umls, snomed, mapping]
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

This pretrained model maps SNOMED codes to corresponding UMLS codes.

## Predicted Entities

`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapper_en_5.2.1_3.0_1708984203970.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_umls_mapper_en_5.2.1_3.0_1708984203970.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["snomed_code"])\
    .setOutputCol("snomed2chunk")

chunkerMapper = ChunkMapperModel.pretrained("snomed_umls_mapper", "en", "clinical/models")\
    .setInputCols(["snomed2chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    snomed_resolver,
    resolver2chunk,
    chunkerMapper])


data = spark.createDataFrame([["acebutolol"],["aspirin"]]).toDF("text")

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
	
val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_drug","en","clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
	
val resolver2chunk = new Resolution2Chunk()
    .setInputCols(Array("snomed_code"))
    .setOutputCol("snomed2chunk")
	
val chunkerMapper = ChunkMapperModel.pretrained("snomed_umls_mapper","en","clinical/models")
    .setInputCols(Array("snomed2chunk"))
    .setOutputCol("mappings")
    .setRels(["umls_code"])
	
val Pipeline(stages = Array(
     documentAssembler,
     sbert_embedder,
     snomed_resolver,
     resolver2chunk,
     chunkerMapper))
	
val data = Seq("acebutolol", "aspirin").toDF("text")
	
val mapper_model = pipeline.fit(data)
result= mapper_model.transform(data)
```
</div>

## Results

```bash
+----------+-----------+---------+
|chunk     |snomed_code|umls_code|
+----------+-----------+---------+
|acebutolol|372815001  |C0000946 |
|aspirin   |387458008  |C0004057 |
+----------+-----------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_umls_mapper|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|7.5 MB|
