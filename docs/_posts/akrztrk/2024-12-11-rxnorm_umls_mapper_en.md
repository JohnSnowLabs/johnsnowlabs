---
layout: model
title: Mapping RxNorm Codes with Their Corresponding UMLS Codes
author: John Snow Labs
name: rxnorm_umls_mapper
date: 2024-12-11
tags: [licensed, en, umls, rxnorm, mapping]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps RxNorm codes to corresponding UMLS codes.

## Predicted Entities
`umls_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapper_en_5.5.1_3.0_1733921579821.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_umls_mapper_en_5.5.1_3.0_1733921579821.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["rxnorm_code"])\
    .setOutputCol("rxnorm2chunk")

chunkerMapper = ChunkMapperModel.pretrained("rxnorm_umls_mapper", "en", "clinical/models")\
    .setInputCols(["rxnorm2chunk"])\
    .setOutputCol("umls_mappings")\
    .setRels(["umls_code"])

mapper_pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    rxnorm_resolver,
    resolver2chunk,
    chunkerMapper
])

data = spark.createDataFrame([['amlodipine 5 MG'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")

rxnorm_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver2chunk = medical.Resolution2Chunk()\
    .setInputCols(["rxnorm_code"])\
    .setOutputCol("rxnorm2chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("rxnorm_umls_mapper", "en", "clinical/models")\
    .setInputCols(["rxnorm2chunk"])\
    .setOutputCol("umls_mappings")\
    .setRels(["umls_code"])

mapper_pipeline = nlp.Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    rxnorm_resolver,
    resolver2chunk,
    chunkerMapper
])

data = spark.createDataFrame([['amlodipine 5 MG'], ['magnesium hydroxide 100 MG'], ['metformin 1000 MG'], ['dilaudid']]).toDF("text")

result = mapper_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en","clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("sbert_embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = Resolution2Chunk()
    .setInputCols(Array("rxnorm_code"))
    .setOutputCol("rxnorm2chunk")

val chunkerMapper = ChunkMapperModel.pretrained("rxnorm_umls_mapper", "en", "clinical/models")
    .setInputCols(Array("rxnorm_code"))
    .setOutputCol("umls_mappings")
    .setRels(Array("umls_code"))


val mapper_pipeline = Pipeline().setStages(Array(
    documentAssembler,
    sbert_embedder,
    rxnorm_resolver,
    resolver2chunk,
    chunkerMapper)

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

+--------------------------+-----------+---------+
|chunk                     |rxnorm_code|umls_code|
+--------------------------+-----------+---------+
|amlodipine 5 MG           |197361     |C0687883 |
|magnesium hydroxide 100 MG|337012     |C1134402 |
|metformin 1000 MG         |316255     |C0987664 |
|dilaudid                  |224913     |C0728755 |
+--------------------------+-----------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_umls_mapper|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|3.0 MB|

## References

Trained on concepts from RXNORM for the 2024AB release of the Unified Medical Language System® (UMLS) Knowledge Sources: https://www.nlm.nih.gov/research/umls/index.html
