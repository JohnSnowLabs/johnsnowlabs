---
layout: model
title: Mapping UMLS Codes with Their Corresponding RxNorm Codes
author: John Snow Labs
name: umls_rxnorm_mapper
date: 2025-06-21
tags: [licensed, en, umls, rxnorm, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps UMLS codes to corresponding RxNorm codes.

## Predicted Entities

`rxnorm_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_rxnorm_mapper_en_6.0.2_3.0_1750524637857.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_rxnorm_mapper_en_6.0.2_3.0_1750524637857.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

umls_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("umls_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["umls_code"])\
    .setOutputCol("umls2chunk")

chunkerMapper = ChunkMapperModel.pretrained("umls_rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["umls2chunk"])\
    .setOutputCol("mappings")\
    .setRels(["rxnorm_code"])

mapper_pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    umls_resolver,
    resolver2chunk,
    chunkerMapper])

data = spark.createDataFrame([['Hydrogen peroxide 30 mg'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

umls_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("umls_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = medical.Resolution2Chunk()\
    .setInputCols(["umls_code"])\
    .setOutputCol("umls2chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("umls_rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["umls2chunk"])\
    .setOutputCol("mappings")

mapper_pipeline = nlp.Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    umls_resolver,
    resolver2chunk,
    chunkerMapper])

data = spark.createDataFrame([['Hydrogen peroxide 30 mg'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(False)

val umls_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_drug_substance", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("umls_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = Resolution2Chunk()
    .setInputCols(Array("umls_code"))
    .setOutputCol("umls2chunk")

val chunkerMapper = ChunkMapperModel.pretrained("umls_rxnorm_mapper", "en", "clinical/models")    .setInputCols(Array("umls2chunk"))
    .setOutputCol("mappings")
    	
val mapper_pipeline = new Pipeline().setStages(Array( 
    document_assembler,
    sbert_embedder,
    umls_resolver,
    resolver2chunk,
    chunkerMapper))

val data = Seq(
  ("amlodipine 5 MG"),
  ("magnesium hydroxide 100 MG"),
  ("metformin 1000 MG"),
  ("dilaudid")
).toDF("text")

val result = mapper_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+--------------------------+---------+-----------+
|chunk                     |umls_code|rxnorm_code|
+--------------------------+---------+-----------+
|Hydrogen peroxide 30 mg   |C1126248 |330565     |
|magnesium hydroxide 100 MG|C1134402 |337012     |
|metformin 1000 MG         |C0987664 |316255     |
|dilaudid                  |C0728755 |224913     |
+--------------------------+---------+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_rxnorm_mapper|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|3.0 MB|

## References

Trained on concepts from RXNORM for the 2025AA release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html