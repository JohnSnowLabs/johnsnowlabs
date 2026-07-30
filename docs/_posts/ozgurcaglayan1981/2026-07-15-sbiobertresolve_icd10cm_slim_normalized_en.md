---
layout: model
title: ICD10CM Sentence Entity Resolver (Slim, normalized)
author: John Snow Labs
name: sbiobertresolve_icd10cm_slim_normalized
date: 2026-07-15
tags: [licensed, en, clinical, icd10cm, entity_resolution]
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

This model maps clinical entities and concepts to ICD10 CM codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. In this model, synonyms having low cosine similarity to unnormalized terms are dropped, making the model slim. It also returns the official resolution text within the brackets inside the metadata. Trained on the ICD-10-CM 20260401 (FY2026, effective April 1, 2026) code set.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_normalized_en_6.4.0_3.4_1784116624596.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd10cm_slim_normalized_en_6.4.0_3.4_1784116624596.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_normalized","en","clinical/models")\
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

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_slim_normalized","en","clinical/models")\
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
    .pretrained("sbiobertresolve_icd10cm_slim_normalized", "en", "clinical/models")
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
| ner_chunk                             | entity   | icd10cm_code   | resolution                                                                                | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:--------------------------------------|:---------|:---------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus              | PROBLEM  | E11            | type 2 diabetes mellitus [type 2 diabetes mellitus]                                       | E11:::E11.62:::E11.5:::E11.8:::E11.59:::E11.628:::E11.3:::E11.69:::E11.6:::E11.6... | 0.0000:::0.0549:::0.0621:::0.0648:::0.0666:::0.0787:::0.0792:::0.0792:::0.0806::... | type 2 diabetes mellitus [type 2 diabetes mellitus]:::type 2 diabetes mellitus w... |
| essential hypertension                | PROBLEM  | I10            | essential (primary) hypertension [essential (primary) hypertension]                       | I10:::I15:::I1A.0:::I11:::H40.05:::I1A:::O10:::O10.0:::I16:::I16.1:::O10.9:::I15... | 0.0296:::0.0514:::0.0690:::0.0849:::0.0869:::0.0993:::0.1027:::0.1029:::0.1041::... | essential (primary) hypertension [essential (primary) hypertension]:::secondary ... |
| acute appendicitis                    | PROBLEM  | K35            | acute appendicitis [acute appendicitis]                                                   | K35:::K35.89:::K35.80:::K35.3:::K35.8:::K35.2:::K35.200:::K35.30:::K36:::K37:::K... | 0.0000:::0.0751:::0.0917:::0.1047:::0.1122:::0.1235:::0.1259:::0.1407:::0.1417::... | acute appendicitis [acute appendicitis]:::other acute appendicitis [other acute ... |
| chronic obstructive pulmonary disease | PROBLEM  | J44            | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary disease] | J44:::J44.89:::J44.1:::J44.0:::J96.1:::J70.3:::J84.170:::I50.32:::I50.3:::J4A:::... | 0.0632:::0.0920:::0.1022:::0.1092:::0.1173:::0.1218:::0.1387:::0.1426:::0.1495::... | other chronic obstructive pulmonary disease [other chronic obstructive pulmonary... |
| major depressive disorder             | PROBLEM  | F33            | major depressive disorder, recurrent [major depressive disorder, recurrent]               | F33:::F32:::F43.21:::F33.1:::F33.9:::F25.1:::F33.3:::F43.23:::F33.8:::F31.5:::F3... | 0.0434:::0.0586:::0.0636:::0.0793:::0.0954:::0.1006:::0.0976:::0.0985:::0.1064::... | major depressive disorder, recurrent [major depressive disorder, recurrent]:::de... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd10cm_slim_normalized|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[icd10cm_code]|
|Language:|en|
|Size:|443.7 MB|
|Case sensitive:|false|