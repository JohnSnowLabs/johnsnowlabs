---
layout: model
title: Mapping MedDRA LLT (Lowest Level Term) Codes with Their Corresponding SNOMED Codes
author: John Snow Labs
name: meddra_llt_snomed_mapper
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

This pretrained model maps MedDRA LLT (Lowest Level Term) codes to corresponding SNOMED codes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/meddra_llt_snomed_mapper_en_5.3.2_3.0_1715707960676.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/meddra_llt_snomed_mapper_en_5.3.2_3.0_1715707960676.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

meddra_resolver = SentenceEntityResolverModel.load("sbiobertresolve_meddra_lowest_level_term") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("meddra_llt_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["meddra_llt_code"])\
    .setOutputCol("meddra_llt_code2chunk")

chunkMapper = ChunkMapperModel.load('meddra_llt_snomed_mapper')\
    .setInputCols(["meddra_llt_code2chunk"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    meddra_resolver,
    resolver2chunk,
    chunkMapper])

data = spark.createDataFrame([["Chronic renal insufficiency"], ["Gastritis"], ["Transient ischemic attack"]]).toDF("text")

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
	
val snomed_resolver = new SentenceEntityResolverModel.load("sbiobertresolve_meddra_lowest_level_term")
	.setInputCols(Array("sbert_embeddings"))
	.setOutputCol("meddra_llt_code")
	.setDistanceFunction("EUCLIDEAN")
	
val resolver2chunk = new Resolution2Chunk()
	.setInputCols(Array("meddra_llt_code"))
	.setOutputCol("meddra_llt_code2chunk")
	
val chunkMapper = new ChunkMapperModel.load("meddra_llt_snomed_mapper")
	.setInputCols(Array("meddra_llt_code2chunk"))
	.setOutputCol("mappings")
	.setRels(Array("snomed_code"))
	
val newPipeline().setStages(Array(
     documentAssembler,
     sbert_embedder,
     meddra_resolver,
     resolver2chunk,
     chunkMapper))
	
val data = Seq("Chronic renal insufficiency","Gastritis","Transient ischemic attack") .toDF("text")
	
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+---------------------------+-----------+------------------------------------------------+
|                      chunk|meddra_code|                                     snomed_code|
+---------------------------+-----------+------------------------------------------------+
|Chronic renal insufficiency|   10050441|723190009:Chronic renal insufficiency (disorder)|
|                  Gastritis|   10017853|                    4556007:Gastritis (disorder)|
|  Transient ischemic attack|   10072760|  266257000:Transient ischemic attack (disorder)|
+---------------------------+-----------+------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_llt_snomed_mapper|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|173.1 KB|
