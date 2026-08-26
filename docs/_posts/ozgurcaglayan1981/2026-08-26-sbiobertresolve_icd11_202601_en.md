---
layout: model
title: Sentence Entity Resolver for ICD11
author: John Snow Labs
name: sbiobertresolve_icd11_202601
date: 2026-08-26
tags: [licensed, en, clinical, entity_resolution, icd11, sbiobert]
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

This model performs entity mapping to ICD-11 standards using sentence embeddings. It takes clinical concepts and returns corresponding ICD-11 codes along with official resolution text in metadata. Trained on the WHO ICD-11 2026-01 release.

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_202601_en_6.4.1_3.4_1787725782920.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_202601_en_6.4.1_3.4_1787725782920.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd11_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_202601", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, icd11_resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension, and was recently diagnosed with Parkinson disease."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icd11_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_202601", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, icd11_resolver
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension, and was recently diagnosed with Parkinson disease."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val icd11_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_202601", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, icd11_resolver
))

val data = Seq("The patient has a history of type 2 diabetes mellitus and essential hypertension, and was recently diagnosed with Parkinson disease.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                | entity   | icd11_code   | resolution_text          | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:-------------------------|:---------|:-------------|:-------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus | PROBLEM  | 5A11         | type 2 diabetes mellitus | 5A11:::SP60:::5A12:::5A13:::5A10:::KB60.2:::5A14:::5A24:::8D88.1:::JA63.1:::5A13... | 0.0000:::0.0648:::0.0940:::0.0966:::0.1016:::0.1025:::0.1238:::0.1278:::0.1262::... | type 2 diabetes mellitus:::diabetes mellitus disorder (tm2):::malnutrition-relat... |
| essential hypertension   | PROBLEM  | BA00         | essential hypertension   | BA00:::BA04:::BA01:::9C61.01:::BA00.0:::BA04.0:::BA00.Z:::BB01:::BA03:::BA00.Y::... | 0.0000:::0.0514:::0.0849:::0.0869:::0.0877:::0.0918:::0.1010:::0.0970:::0.1041::... | essential hypertension:::secondary hypertension:::hypertensive heart disease:::o... |
| Parkinson disease        | PROBLEM  | 8A00.0       | parkinson disease        | 8A00.0:::8A00:::8A00.3:::8A00.2:::8A00.24:::8A00.23:::8A00.1:::8A00.01:::8A00.0Y... | 0.0000:::0.0533:::0.0630:::0.0883:::0.0894:::0.0937:::0.1033:::0.1127:::0.1456::... | parkinson disease:::parkinsonism:::functional parkinsonism:::secondary parkinson... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd11_202601|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[icd11_code]|
|Language:|en|
|Size:|103.4 MB|
|Case sensitive:|false|