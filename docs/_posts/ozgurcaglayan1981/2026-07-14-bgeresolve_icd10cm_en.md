---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (bge_base_en_v1_5_onnx)
author: John Snow Labs
name: bgeresolve_icd10cm
date: 2026-07-14
tags: [resolver, icd10cm, en, licensed, clinical, bge, sentence_entity_resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to ICD-10-CM codes using `bge_base_en_v1_5_onnx` embeddings. It resolves entities from the following domains: Condition, Observation, Measurement, and Procedure. Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_en_6.4.0_3.4_1784071529214.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_en_6.4.0_3.4_1784071529214.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension, presented with acute appendicitis and was noted to have chronic obstructive pulmonary disease on exam. Past psychiatric history notable for major depressive disorder."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['PROBLEM'])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_icd10cm","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension, presented with acute appendicitis and was noted to have chronic obstructive pulmonary disease on exam. Past psychiatric history notable for major depressive disorder."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_icd10cm", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("icd10cm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient has a history of type 2 diabetes mellitus and essential hypertension, presented with acute appendicitis and was noted to have chronic obstructive pulmonary disease on exam. Past psychiatric history notable for major depressive disorder.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                 | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:--------------------------------------|:---------|:---------------|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                        | E11:::E11.9:::E10.9:::E11.65:::E11.8:::E66.9:::E11.64:::Z86.39:::E11.6:::E11.22:... | 0.0000:::0.0359:::0.1077:::0.1225:::0.1244:::0.1302:::0.1329:::0.1392:::0.1393::... | type 2 diabetes mellitus [type 2 diabetes mellitus]:::diabetes mellitus type 2 [... |
| essential hypertension                | PROBLEM  | I10            | essential hypertension [essential (primary) hypertension]                                  | I10:::I27.0:::O10.0:::O10.03:::O10.02:::O10.01                                      | 0.0000:::0.1449:::0.1474:::0.1683:::0.1950:::0.2024                                 | essential hypertension [essential (primary) hypertension]:::essential pulmonary ... |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                    | K35:::K35.8:::K35.20:::K37:::K35.2:::K35.80:::K35.3:::K35.89:::K36:::K35.33:::R1... | 0.0000:::0.0773:::0.0809:::0.0854:::0.1106:::0.1172:::0.1225:::0.1407:::0.1551::... | acute appendicitis [acute appendicitis]:::acute appendicitis (disorder) [other a... |
| chronic obstructive pulmonary disease | PROBLEM  | J44.9          | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified] | J44.9:::J98.4:::J62.8:::Z91.89:::J98.9:::J44                                        | 0.0000:::0.1381:::0.1396:::0.1444:::0.1465:::0.1583                                 | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, un... |
| major depressive disorder             | PROBLEM  | F32.9          | major depressive disorder [major depressive disorder, single episode, unspecified]         | F32.9:::F32.2:::F41.8:::F33:::F33.9:::F33.1:::F33.0:::O99.34:::F32.1:::F33.4:::O... | 0.0000:::0.0122:::0.1628:::0.1658:::0.1665:::0.1710:::0.1828:::0.1833:::0.1947::... | major depressive disorder [major depressive disorder, single episode, unspecifie... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_icd10cm|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|