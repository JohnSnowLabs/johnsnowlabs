---
layout: model
title: Sentence Entity Resolver for Billable ICD-10-CM HCC Codes
author: John Snow Labs
name: sbiobertresolve_icd10cm_augmented_billable_hcc
date: 2026-07-14
tags: [licensed, en, clinical, icd10cm, entity_resolution, hcc]
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

This model maps extracted medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings and it supports 7-digit codes with Hierarchical Condition Categories (HCC) status. In the result, look for the `all_k_aux_labels` parameter in the metadata to get HCC status: `billable status`, `hcc status`, and `hcc score` (e.g. `1||1||8`). Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_6.4.0_3.4_1784072474994.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_augmented_billable_hcc_en_6.4.0_3.4_1784072474994.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
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
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
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
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
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
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                 | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:--------------------------------------|:---------|:---------------|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                        | E11:::E11.9:::E11.8:::E11.3:::O24.11:::E13.9:::E11.43:::E10.9:::E11.69:::E11.4::... | 0.0000:::0.0134:::0.0212:::0.0357:::0.0360:::0.0397:::0.0455:::0.0462:::0.0499::... | type 2 diabetes mellitus [type 2 diabetes mellitus]:::diabetes mellitus type 2 [... | 0||0||0:::1||1||38:::1||1||38:::0||0||0:::0||0||0:::1||1||38:::1||1||37:::1||1||... |
| essential hypertension                | PROBLEM  | I10            | essential hypertension [essential (primary) hypertension]                                  | I10:::I15.8:::Z87.5:::I15:::I15.2:::P29.2:::Z13.6                                   | 0.0000:::0.0446:::0.0489:::0.0514:::0.0541:::0.0580:::0.0605                        | essential hypertension [essential (primary) hypertension]:::intermittent hyperte... | 1||0||0:::1||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0                 |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                    | K35:::K35.8:::K35.2:::K35.89:::K35.20:::K36:::K37:::K35.80:::Z87.1                  | 0.0000:::0.0218:::0.0331:::0.0379:::0.0385:::0.0414:::0.0579:::0.0604:::0.0627      | acute appendicitis [acute appendicitis]:::acute appendicitis (disorder) [other a... | 0||0||0:::0||0||0:::0||0||0:::0||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::... |
| chronic obstructive pulmonary disease | PROBLEM  | J44.9          | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified] | J44.9:::J62.8:::J84.9:::I27.9:::J44:::J98.4:::J98.9:::Z76.89:::J98.0:::Z87.0:::Z... | 0.0000:::0.0433:::0.0481:::0.0622:::0.0632:::0.0641:::0.0687:::0.0717:::0.0755::... | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, un... | 1||1||280:::1||1||280:::1||1||280:::1||1||226:::0||0||0:::1||0||0:::1||0||0:::1|... |
| major depressive disorder             | PROBLEM  | F32.9          | major depressive disorder [major depressive disorder, single episode, unspecified]         | F32.9:::F32.2:::F33:::F33.9:::F06.3:::F33.3:::F32.8:::F32.3:::F34.1:::F32:::F06.... | 0.0000:::0.0140:::0.0434:::0.0432:::0.0478:::0.0550:::0.0571:::0.0581:::0.0578::... | major depressive disorder [major depressive disorder, single episode, unspecifie... | 1||0||0:::1||1||155:::0||0||0:::1||0||0:::0||0||0:::1||1||152:::0||0||0:::1||1||... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_augmented_billable_hcc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|