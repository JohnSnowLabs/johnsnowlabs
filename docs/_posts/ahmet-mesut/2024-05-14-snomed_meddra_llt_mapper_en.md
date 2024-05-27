---
layout: model
title: Mapping SNOMED Codes with Their Corresponding MedDRA LLT (Lowest Level Term) Codes
author: John Snow Labs
name: snomed_meddra_llt_mapper
date: 2024-05-14
tags: [en, licensed, snomed, meddra_llt, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps SNOMED codes to corresponding MedDRA LLT (Lowest Level Term) codes. Some of the SNOMED codes map to more than one MedDRA LLT codes. You can find all the mapped MedDRA LLT codes in the `all_k_resolutions` column in the metadata.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>

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

snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_conditions", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["snomed_code"])\
    .setOutputCol("snomed2chunk")

chunkMapper = ChunkMapperModel.load('snomed_meddra_llt_mapper')\
    .setInputCols(["snomed2chunk"])\
    .setOutputCol("mappings")\
    .setRels(["meddra_code"])

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    snomed_resolver,
    resolver2chunk,
    chunkMapper])


data = spark.createDataFrame([["Fungal infection of lung"], ["Abdominal pain"], ["wheezing"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("ner_chunk")
	
val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
	.setInputCols(Array("ner_chunk"))
	.setOutputCol("sbert_embeddings")
	.setCaseSensitive(false)
	
val snomed_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_snomed_conditions","en","clinical/models")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("snomed_code")
	.setDistanceFunction("EUCLIDEAN")
	
val resolver2chunk = new Resolution2Chunk()
	.setInputCols(Array("snomed_code"))
	.setOutputCol("snomed2chunk")
	
val chunkMapper = new ChunkMapperModel.load("snomed_meddra_llt_mapper")
	.setInputCols(Array("snomed2chunk"))
	.setOutputCol("mappings")
	.setRels(Array("meddra_code"))
	
val newPipeline().setStages(Array(
     documentAssembler,
     sbert_embedder,
     snomed_resolver,
     resolver2chunk,
     chunkMapper))
	
val data = Seq("Fungal infection of lung", "Abdominal pain", "wheezing") .toDF("text")
	
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+------------------------+-----------+-------------------------------+------------------------------------------------------------+
|                   chunk|snomed_code|                    meddra_code|                                           all_k_resolutions|
+------------------------+-----------+-------------------------------+------------------------------------------------------------+
|Fungal infection of lung|   63741006|     10037422:Pulmonary mycosis| 10037422:Pulmonary mycosis:::10085440:Lung infection fungal|
|          Abdominal pain|   21522001|10000058:Abdominal crampy pains|10000058:Abdominal crampy pains:::10000081:Abdominal pain...|
|                wheezing|   56018004|                10047921:Wheeze|       10047921:Wheeze:::10047924:Wheezing:::10047927:Wheezy|
+------------------------+-----------+-------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_meddra_llt_mapper|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|136.2 KB|
