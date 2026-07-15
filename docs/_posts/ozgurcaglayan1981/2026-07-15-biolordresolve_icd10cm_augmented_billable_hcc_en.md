---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes
author: John Snow Labs
name: biolordresolve_icd10cm_augmented_billable_hcc
date: 2026-07-15
tags: [licensed, en, biolord, icd10cm, entity_resolution, hcc, clinical]
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

This model maps extracted medical entities to ICD-10-CM codes using `mpnet_embeddings_biolord_2023_c` MPNet Embeddings and it supports 7-digit codes with Hierarchical Condition Categories (HCC) status. In the result, look for the `all_k_aux_labels` parameter in the metadata to get HCC status: `billable status`, `hcc status`, and `hcc score` (e.g. `1||1||8`). Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icd10cm_augmented_billable_hcc_en_6.4.0_3.4_1784073997454.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icd10cm_augmented_billable_hcc_en_6.4.0_3.4_1784073997454.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icd10cm_augmented_billable_hcc","en","clinical/models")\
    .setInputCols(["embeddings"])\
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

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_icd10cm_augmented_billable_hcc","en","clinical/models")\
    .setInputCols(["embeddings"])\
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

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
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
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                                      | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:--------------------------------------|:---------|:---------------|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11.8          | disorder due to type 2 diabetes mellitus [type 2 diabetes mellitus with unspecified complications]              | E11.8:::E11.9:::Z86.39:::E11.65:::Z79.4:::E11.6:::E66.9:::E11.64:::E13.9            | 0.0532:::0.0876:::0.0925:::0.0998:::0.1170:::0.1312:::0.1353:::0.1454:::0.1587      | disorder due to type 2 diabetes mellitus [type 2 diabetes mellitus with unspecif... | 1||1||38:::1||1||38:::1||0||0:::1||1||38:::1||1||38:::0||0||0:::1||0||0:::0||0||... |
| essential hypertension                | PROBLEM  | I10            | essential hypertension [essential (primary) hypertension]                                                       | I10:::O10.0:::P29.2:::I11.9:::O10.03:::I16:::I16.1                                  | 0.0925:::0.0953:::0.1958:::0.2210:::0.2442:::0.2446:::0.2662                        | essential hypertension [essential (primary) hypertension]:::benign essential hyp... | 1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0                 |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                                         | K35:::K35.8:::K35.89:::K35.80:::K35.30:::K35.3:::K35.2:::K35.20:::K35.890:::K37:... | 0.0565:::0.0844:::0.0870:::0.0895:::0.0936:::0.0988:::0.1064:::0.1316:::0.1463::... | acute appendicitis [acute appendicitis]:::acute suppurative appendicitis [other ... | 0||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::0||0||0:::0||0||0:::0||0||0:::... |
| chronic obstructive pulmonary disease | PROBLEM  | J44.9          | copd - chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified]               | J44.9:::Z87.0:::J44:::J44.89:::J44.1:::J62.8                                        | 0.0960:::0.1268:::0.1356:::0.1601:::0.1810:::0.1991                                 | copd - chronic obstructive pulmonary disease [chronic obstructive pulmonary dise... | 1||1||280:::0||0||0:::0||0||0:::1||1||280:::1||1||280:::1||1||280                   |
| major depressive disorder             | PROBLEM  | F33.3          | major depression with psychotic features [major depressive disorder, recurrent, severe with psychotic symptoms] | F33.3:::F32.9:::F32:::F32.2:::F32.8:::F06.3:::F32.1:::F32.3:::F32.0:::F33:::G70.... | 0.0834:::0.1032:::0.1113:::0.1165:::0.1268:::0.1726:::0.1767:::0.1785:::0.1859::... | major depression with psychotic features [major depressive disorder, recurrent, ... | 1||1||152:::1||0||0:::0||0||0:::1||1||155:::0||0||0:::0||0||0:::1||1||155:::1||1... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|