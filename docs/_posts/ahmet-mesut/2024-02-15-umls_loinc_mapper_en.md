---
layout: model
title: Mapping UMLS Codes with Their Corresponding LOINC Codes
author: John Snow Labs
name: umls_loinc_mapper
date: 2024-02-15
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

This pretrained model maps UMLS codes to corresponding LOINC codes

## Predicted Entities

`loinc_code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_loinc_mapper_en_5.2.1_3.0_1707989243756.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_loinc_mapper_en_5.2.1_3.0_1707989243756.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

umls_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_clinical_drugs", "en", "clinical/models") \
    .setInputCols(["sbert_embeddings"]) \
    .setOutputCol("umls_code")\
    .setDistanceFunction("EUCLIDEAN")

chunkerMapper = ChunkMapperModel.pretrained("umls_loinc_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")\
    .setRels(["loinc_code"])

pipeline = Pipeline(stages = [
    documentAssembler,
    sbert_embedder,
    umls_resolver,
    chunkerMapper])

model = pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

light_pipeline= LightPipeline(model)

result = light_pipeline.fullAnnotate("acebutolol")
```
```scala
val documentAssembler = new DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("ner_chunk")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("sbert_embeddings")

val icd_resolver = SentenceEntityResolverModel.pretrained("UMLS sbiobertresolve_umls_clinical_drugs","en","clinical/models") \ 
    .setInputCols(Array("ner_chunk", "sbert_embeddings")) \
    .setOutputCol("umls_code")\
    .setDistanceFunction("EUCLIDEAN")

val chunkerMapper = ChunkMapperModel.pretrained("umls_loinc_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")\
    .setRels(Array("loinc_code"))

val pipeline = new Pipeline(stages = Array(
    documentAssembler,
    sbert_embedder,
    icd_resolver,
    chunkerMapper
    ))

val data = Seq("acebutolol").toDF("text")

val result= pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|      chunk |     UMLS |     LOINC |   relation |
|-----------:|---------:|----------:|-----------:|
| acebutolol | C0000946 | LP16015-7 | loinc_code |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_loinc_mapper|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|2.9 MB|