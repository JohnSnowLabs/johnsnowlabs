---
layout: model
title: Sentence Entity Resolver for Billable ICD10-CM HCC Codes (sbertresolve_icd10cm_slim_billable_hcc)
author: John Snow Labs
name: sbertresolve_icd10cm_slim_billable_hcc
date: 2026-07-15
tags: [icd10cm, licensed, slim, en, clinical, billable, hcc_score]
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

This model maps clinical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings. In this model, synonyms having low cosine similarity to unnormalized terms are dropped. It also returns the official resolution text within the brackets inside the metadata. Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_slim_billable_hcc_en_6.4.0_3.4_1784116092246.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_icd10cm_slim_billable_hcc_en_6.4.0_3.4_1784116092246.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_slim_billable_hcc","en","clinical/models")\
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbertresolve_icd10cm_slim_billable_hcc","en","clinical/models")\
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
    .pretrained("sbertresolve_icd10cm_slim_billable_hcc", "en", "clinical/models")
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
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:--------------------------------------|:---------|:---------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                       | E11:::E10:::E11.65:::E11.630:::E10.630:::E11.0:::E10.65:::E11.5:::E11.3:::E10.5:... | 0.0000:::0.0072:::0.0554:::0.0559:::0.0572:::0.0591:::0.0595:::0.0580:::0.0588::... | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type 1 diabetes mellitus [... | 0||0||0:::0||0||0:::1||1||38:::1||1||37:::1||1||37:::0||0||0:::1||1||38:::0||0||... |
| essential hypertension                | PROBLEM  | I10            | essential (primary) hypertension [essential (primary) hypertension]                       | I10:::K76.6:::I15.0:::O10.03:::O16:::I97.3:::O10.0:::I15:::H40.05:::O10.43:::I27... | 0.1010:::0.1250:::0.1526:::0.1740:::0.1704:::0.1846:::0.1889:::0.1857:::0.1913::... | essential (primary) hypertension [essential (primary) hypertension]:::portal hyp... | 1||0||0:::1||1||63:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::0||0||0:::0||0||0::... |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                   | K35:::K35.3:::K35.89:::K35.2:::I30:::K35.80:::K11.21:::I33:::I40:::K35.30:::K35.... | 0.0000:::0.0310:::0.0386:::0.0426:::0.0446:::0.0455:::0.0559:::0.0588:::0.0579::... | acute appendicitis [acute appendicitis]:::acute appendicitis with localized peri... | 0||0||0:::0||0||0:::0||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::0||0||0:::... |
| chronic obstructive pulmonary disease | PROBLEM  | J44            | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary disease] | J44:::J44.1:::J44.89:::J44.9:::J44.0:::J81.1:::B38.1:::N11.1:::B40.1:::J81.0:::I... | 0.0527:::0.0520:::0.0724:::0.0723:::0.0799:::0.0861:::0.1075:::0.1142:::0.1130::... | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary... | 0||0||0:::1||1||280:::1||1||280:::1||1||280:::1||1||280:::1||0||0:::1||0||0:::1|... |
| major depressive disorder             | PROBLEM  | F33            | major depressive disorder, recurrent [major depressive disorder, recurrent]               | F33:::F33.1:::F33.0:::F33.40:::F33.41:::F33.4:::F33.9:::F33.8:::F25.1:::F33.3:::... | 0.0696:::0.0922:::0.1117:::0.1337:::0.1432:::0.1471:::0.1517:::0.1604:::0.1734::... | major depressive disorder, recurrent [major depressive disorder, recurrent]:::ma... | 0||0||0:::1||1||155:::1||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0:... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_icd10cm_slim_billable_hcc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|299.0 MB|
|Case sensitive:|false|