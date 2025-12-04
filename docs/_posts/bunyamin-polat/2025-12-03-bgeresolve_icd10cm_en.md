---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (bge_base_en_v1_5_onnx)
author: John Snow Labs
name: bgeresolve_icd10cm
date: 2025-12-03
tags: [resolver, icd10cm, en, licensed, clinical, bge, sentence_entity_resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to ICD-10-CM codes using `bge_base_en_v1_5_onnx` embeddings. It resolves entities from the following domains: Condition, Observation, Measurement, and Procedure.

## Predicted Entities

`ICD-10-CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_en_6.2.0_3.4_1764803701916.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_en_6.2.0_3.4_1764803701916.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner_clinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_clinical_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

icd10cm_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_clinical,
    ner_clinical_converter,
    chunk2doc,
    bge_embeddings,
    icd10cm_resolver
])

text = """A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner_clinical = medical.MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_clinical_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

icd10cm_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_clinical,
    ner_clinical_converter,
    chunk2doc,
    bge_embeddings,
    icd10cm_resolver
])

text = """A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val nerClinical = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val nerClinicalConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val bgeEmbeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")

val icd10cmResolver = SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("icd10cm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerClinical,
    nerClinicalConverter,
    chunk2doc,
    bgeEmbeddings,
    icd10cmResolver
))

val data = Seq("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|sent_id|ner_chunk                             |entity |icd10cm_code|resolutions                  |all_codes                                      |all_resolutions                                |
|-------|--------------------------------------|-------|------------|-----------------------------|-----------------------------------------------|-----------------------------------------------|
|0      |gestational diabetes mellitus         |PROBLEM|O24.4       |gestational diabetes mellitus|[O24.4, O24.41, O24.43, O24.42, O24.414, ...]  |[gestational diabetes mellitus, gestational di...]|
|0      |subsequent type two diabetes mellitus |PROBLEM|E11         |type 2 diabetes mellitus     |[E11, E11.69, E11.6, E11.64, E13, E11.65, ...] |[type 2 diabetes mellitus, type 2 diabetes mel...]|
|0      |T2DM                                  |PROBLEM|E11         |type 2 diabetes mellitus     |[E11, E11.65, E11.64, E11.9, E11.44, E11.5, ...]|[type 2 diabetes mellitus, type 2 diabetes mel...]|
|0      |HTG-induced pancreatitis              |PROBLEM|K85.3       |drug induced acute pancreatitis|[K85.3, K86.0, K85.2, K85.31, K85.21, ...]    |[drug induced acute pancreatitis, alcohol-indu...]|
|0      |acute hepatitis                       |PROBLEM|B15         |acute hepatitis a            |[B15, B16, B17.1, B17, B17.2, B17.9, ...]      |[acute hepatitis a, acute hepatitis b, acute h...]|
|0      |obesity                               |PROBLEM|E66         |overweight and obesity       |[E66, E66.9, E66.0, E66.8, E66.3, O99.21, ...] |[overweight and obesity, obesity, unspecified,...]|
|0      |polyuria                              |PROBLEM|R35         |polyuria                     |[R35, R35.89, R35.8, R35.81, R80, R80.8, ...]  |[polyuria, other polyuria, other polyuria, noc...]|
|0      |polydipsia                            |PROBLEM|R63.1       |polydipsia                   |[R63.1, O40, R35, R35.89, R35.8, R63.2, ...]   |[polydipsia, polyhydramnios, polyuria, other p...]|
|0      |vomiting                              |PROBLEM|R11.1       |vomiting                     |[R11.1, R11, R11.12, R11.10, R11.11, R11.13, ...]|[vomiting, nausea and vomiting, projectile vom...]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_icd10cm|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|281.4 MB|
|Case sensitive:|false|
