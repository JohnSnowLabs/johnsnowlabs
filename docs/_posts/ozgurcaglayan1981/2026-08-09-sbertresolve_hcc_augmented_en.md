---
layout: model
title: Sentence Entity Resolver for Hierarchical Condition Categories (HCC) codes (Augmented)
author: John Snow Labs
name: sbertresolve_hcc_augmented
date: 2026-08-09
tags: [licensed, en, entity_resolution, hcc, clinical, sbert]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps extracted medical entities to Hierarchical Condition Categories (HCC) codes using `sbert_jsl_medium_uncased` Sentence Bert Embeddings. Trained on the ICD-10-CM 20260401 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbertresolve_hcc_augmented_en_6.4.1_3.4_1786292921547.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbertresolve_hcc_augmented_en_6.4.1_3.4_1786292921547.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbertresolve_hcc_augmented","en","clinical/models")\
    .setInputCols(["bert_embeddings"])\
    .setOutputCol("hcc_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus, essential hypertension, and end stage renal disease, presented with acute appendicitis, and was noted to have chronic obstructive pulmonary disease and other heart failure on exam."]]).toDF("text")
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbertresolve_hcc_augmented","en","clinical/models")\
    .setInputCols(["bert_embeddings"])\
    .setOutputCol("hcc_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus, essential hypertension, and end stage renal disease, presented with acute appendicitis, and was noted to have chronic obstructive pulmonary disease and other heart failure on exam."]]).toDF("text")
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
    .pretrained("sbertresolve_hcc_augmented", "en", "clinical/models")
    .setInputCols(Array("bert_embeddings"))
    .setOutputCol("hcc_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient has a history of type 2 diabetes mellitus, essential hypertension, and end stage renal disease, presented with acute appendicitis, and was noted to have chronic obstructive pulmonary disease and other heart failure on exam.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                             | entity   |   hcc_code | resolution                                                                                 | all_k_results           | all_k_cosine_distances                     | all_k_resolutions                                                                   | all_k_aux_labels   |
|:--------------------------------------|:---------|-----------:|:-------------------------------------------------------------------------------------------|:------------------------|:-------------------------------------------|:------------------------------------------------------------------------------------|:-------------------|
| type 2 diabetes mellitus              | PROBLEM  |          0 | type 2 diabetes mellitus [type 2 diabetes mellitus]                                        | 0:::19:::18             | 0.0000:::0.0120:::0.0402                   | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type ii diabetes mellitus ... |                    |
| essential hypertension                | PROBLEM  |          0 | essential hypertension [essential (primary) hypertension]                                  | 0:::27:::85             | 0.0000:::0.1250:::0.1549                   | essential hypertension [essential (primary) hypertension]:::portal hypertension ... |                    |
| end stage renal disease               | PROBLEM  |        136 | end stage renal disease [end stage renal disease]                                          | 136:::0:::27:::134:::18 | 0.0000:::0.0916:::0.1079:::0.1148:::0.1434 | end stage renal disease [end stage renal disease]:::esrd - end stage renal disea... |                    |
| acute appendicitis                    | PROBLEM  |          0 | acute appendicitis [acute appendicitis]                                                    | 0:::33                  | 0.0000:::0.0550                            | acute appendicitis [acute appendicitis]:::acute peritonitis [generalized (acute)... |                    |
| chronic obstructive pulmonary disease | PROBLEM  |        111 | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified] | 111:::0                 | 0.0000:::0.0491                            | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, un... |                    |
| other heart failure                   | PROBLEM  |         85 | other heart failure [other heart failure]                                                  | 85:::0:::186            | 0.0000:::0.1030:::0.1055                   | other heart failure [other heart failure]:::heart failure [heart failure]:::hear... |                    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbertresolve_hcc_augmented|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[hcc_code]|
|Language:|en|
|Size:|886.8 MB|
|Case sensitive:|false|