---
layout: model
title: Sentence Entity Resolver for ICD10-CM (general 3 character codes)
author: John Snow Labs
name: sbiobertresolve_icd10cm_generalised
date: 2026-07-15
tags: [licensed, icd10cm, clinical, en, generalised, entity_resolution]
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

This model maps extracted medical entities to ICD10-CM codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. It predicts ICD codes up to 3 characters (according to ICD10 code structure the first three characters represent general type of the injury or disease). Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_en_6.4.0_3.4_1784117487208.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_generalised_en_6.4.0_3.4_1784117487208.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
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

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_generalised","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
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

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_icd10cm_generalised", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
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
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                | all_k_results                                                               | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:--------------------------------------|:---------|:---------------|:------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                       | E11:::E09                                                                   | 0.0000:::0.0968                                                                     | type 2 diabetes mellitus [type 2 diabetes mellitus]:::drug or chemical induced d... |
| essential hypertension                | PROBLEM  | I10            | essential (primary) hypertension [essential (primary) hypertension]                       | I10:::I15:::I1A:::I11:::H40:::O10:::I16:::L68:::I27:::I87:::P29:::K76       | 0.0296:::0.0514:::0.0690:::0.0849:::0.0869:::0.1027:::0.1041:::0.1225:::0.1222::... | essential (primary) hypertension [essential (primary) hypertension]:::secondary ... |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                   | K35:::K36:::K37:::K38:::K61:::L02:::K60:::L03:::K65                         | 0.0000:::0.1417:::0.1435:::0.1588:::0.1671:::0.1680:::0.1743:::0.1804:::0.1835      | acute appendicitis [acute appendicitis]:::other appendicitis [other appendicitis... |
| chronic obstructive pulmonary disease | PROBLEM  | J44            | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary disease] | J44:::J96:::J70:::J84:::I50:::J4A:::Q24:::E84:::I27:::I25:::J81:::J63:::F18 | 0.0632:::0.1173:::0.1218:::0.1387:::0.1426:::0.1499:::0.1583:::0.1635:::0.1670::... | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary... |
| major depressive disorder             | PROBLEM  | F33            | major depressive disorder, recurrent [major depressive disorder, recurrent]               | F33:::F32:::F43:::F25:::F31:::F34:::F06:::F10:::F60:::F19:::F45:::F18       | 0.0434:::0.0586:::0.0636:::0.1006:::0.1144:::0.1164:::0.1233:::0.1400:::0.1410::... | major depressive disorder, recurrent [major depressive disorder, recurrent]:::de... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_generalised|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|442.8 MB|
|Case sensitive:|false|