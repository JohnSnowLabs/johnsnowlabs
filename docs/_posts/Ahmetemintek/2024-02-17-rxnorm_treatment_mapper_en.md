---
layout: model
title: Mapping RxNorm Codes with Corresponding Treatments
author: John Snow Labs
name: rxnorm_treatment_mapper
date: 2024-02-17
tags: [chunk_mapper, treatment, clinical, en, licensed]
task: Chunk Mapping
language: en
edition: Healthcare NLP 5.2.2
spark_version: 3.0
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained model maps RxNorm and RxNorm Extension codes with their corresponding treatment. Treatment refers to which disease the drug is used to treat.

## Predicted Entities

`treatment`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_treatment_mapper_en_5.2.2_3.0_1708129769960.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_treatment_mapper_en_5.2.2_3.0_1708129769960.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("ner_chunk")

sbert_embedder = BertSentenceEmbeddings\
      .pretrained("sbiobert_base_cased_mli", "en","clinical/models")\
      .setInputCols(["ner_chunk"])\
      .setOutputCol("sbert_embeddings")
    
rxnorm_resolver = SentenceEntityResolverModel\
      .pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")\
      .setInputCols(["sbert_embeddings"])\
      .setOutputCol("rxnorm_code")\
      .setDistanceFunction("EUCLIDEAN")

resolver2chunk = Resolution2Chunk()\
    .setInputCols(["rxnorm_code"]) \
    .setOutputCol("resolver2chunk")

chunkMapper = ChunkMapperModel.pretrained("rxnorm_treatment_mapper", "en", "clinical/models")\
      .setInputCols(["resolver2chunk"])\
      .setOutputCol("mappings")\
      .setRels(["treatment"])

pipeline = Pipeline(
    stages = [
        documentAssembler,
        sbert_embedder,
        rxnorm_resolver,
        resolver2chunk,
        chunkMapper
        ])

test_data = spark.createDataFrame([["Eviplera"], ["Zonalon 50 mg"], ["Rompun"], ["Glucovance"], ["Abbokinase"]]).toDF("text")

res= model.fit(test_data).transform(test_data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")
    .setInputCols("ner_chunk")
    .setOutputCol("sbert_embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver2chunk = new Resolution2Chunk()\
    .setInputCols(["rxnorm_code"]) \
    .setOutputCol("resolver2chunk")

val chunkMapper = ChunkMapperModel.pretrained("rxnorm_treatment_mapper", "en", "clinical/models")
    .setInputCols("resolver2chunk")
    .setOutputCol("mappings")
    .setRels("action")

val pipeline = new Pipeline(stages = Array(
    documentAssembler,
    sbert_embedder,
    rxnorm_resolver,
    resolver2chunk,
    chunkMapper
    ))

val data = Seq(Array("Eviplera", "Zonalon 50 mg", "Rompun", "Glucovance", "Abbokinase")).toDS.toDF("text")

val result= pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------+-----------+------------------------+---------+
|ner_chunk    |rxnorm_code|treatment_mapping_result|relation |
+-------------+-----------+------------------------+---------+
|Eviplera     |217010     |Osteoporosis            |treatment|
|Zonalon 50 mg|103971     |Pain                    |treatment|
|Rompun       |1536491    |Pain                    |treatment|
|Glucovance   |284743     |Diabetes Mellitus       |treatment|
|Abbokinase   |204209     |Angiography             |treatment|
+-------------+-----------+------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_treatment_mapper|
|Compatibility:|Healthcare NLP 5.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|5.8 MB|