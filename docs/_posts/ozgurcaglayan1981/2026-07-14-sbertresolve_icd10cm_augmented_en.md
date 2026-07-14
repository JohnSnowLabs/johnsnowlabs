---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (sbertresolve_icd10cm_augmented)
author: John Snow Labs
name: sbertresolve_icd10cm_augmented
date: 2026-07-14
tags: [licensed, en, icd10cm, entity_resolution, clinical]
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

This model maps clinical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings. It also returns the official resolution text within the brackets inside the metadata. The model is augmented with synonyms, and previous augmentations are flexed according to cosine distances to unnormalized terms (ground truths). Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_6.4.0_3.4_1784070427948.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_augmented_en_6.4.0_3.4_1784070427948.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented","en","clinical/models")\
    .setInputCols(["bert_embeddings"])\
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

embedder = nlp.BertSentenceEmbeddings.pretrained("sbert_jsl_medium_uncased","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_augmented","en","clinical/models")\
    .setInputCols(["bert_embeddings"])\
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
    .pretrained("sbert_jsl_medium_uncased", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbertresolve_icd10cm_augmented", "en", "clinical/models")
    .setInputCols(Array("bert_embeddings"))
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
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                        | E11:::E10:::E11.9:::E10.9:::E11.8:::E13.9:::E66.9:::L83:::E11.63:::Z83.3:::E10.8... | 0.0000:::0.0072:::0.0120:::0.0198:::0.0402:::0.0434:::0.0441:::0.0467:::0.0479::... | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type 1 diabetes mellitus [... |
| essential hypertension                | PROBLEM  | I10            | essential hypertension [essential (primary) hypertension]                                  | I10:::K76.6:::I97.88:::O10.03:::O10.02:::I15.0:::I27.0:::I97.8:::P29.2:::I15.8::... | 0.0000:::0.1250:::0.1394:::0.1442:::0.1475:::0.1526:::0.1549:::0.1679:::0.1719::... | essential hypertension [essential (primary) hypertension]:::portal hypertension ... |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                    | K35:::K35.2:::K35.3:::K35.89:::K35.8:::K35.30:::K35.80:::K35.20:::I30.9:::I30:::... | 0.0000:::0.0297:::0.0310:::0.0325:::0.0355:::0.0378:::0.0387:::0.0395:::0.0429::... | acute appendicitis [acute appendicitis]:::acute perforated appendicitis [acute a... |
| chronic obstructive pulmonary disease | PROBLEM  | J44.9          | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified] | J44.9:::Z76.89:::J44:::J44.1:::J44.0:::J44.89                                       | 0.0000:::0.0491:::0.0527:::0.0520:::0.0602:::0.0724                                 | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, un... |
| major depressive disorder             | PROBLEM  | F32.9          | major depressive disorder [major depressive disorder, single episode, unspecified]         | F32.9:::F32.2:::F91.8:::F32.81:::F33:::F33.9:::F34.1:::F33.1:::O99.34:::Z86.5:::... | 0.0000:::0.0496:::0.0627:::0.0657:::0.0696:::0.0687:::0.0773:::0.0922:::0.0916::... | major depressive disorder [major depressive disorder, single episode, unspecifie... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|888.8 MB|
|Case sensitive:|false|