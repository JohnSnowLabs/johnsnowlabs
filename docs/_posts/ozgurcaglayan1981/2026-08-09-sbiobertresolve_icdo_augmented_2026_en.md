---
layout: model
title: Sentence Entity Resolver for ICD-O (sbiobertresolve_icdo_augmented)
author: John Snow Labs
name: sbiobertresolve_icdo_augmented_2026
date: 2026-08-09
tags: [licensed, en, clinical, entity_resolution, icdo, sbiobert]
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

This model maps clinical/oncology entities to ICD-O (International Classification of Diseases for Oncology) morphology/topography codes using `sbiobert_base_cased_mli_onnx` Sentence Embeddings. Trained on the ICD-O-3.2 2026 update dataset.

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_augmented_2026_en_6.4.1_3.4_1786277790803.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icdo_augmented_2026_en_6.4.1_3.4_1786277790803.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

jsl_ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("jsl_ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "jsl_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Oncological"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icdo_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    jsl_ner, ner_converter, c2doc, embedder, icdo_resolver
])

data = spark.createDataFrame([["The patient's pathology report noted mesothelioma in situ, along with a malignant spitz tumor of the external upper lip and intraductal papilloma of the nipple."]]).toDF("text")
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

jsl_ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("jsl_ner")

ner_converter = medical.NerConverter()\
    .setInputCols(["sentence", "token", "jsl_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Oncological"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

icdo_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    jsl_ner, ner_converter, c2doc, embedder, icdo_resolver
])

data = spark.createDataFrame([["The patient's pathology report noted mesothelioma in situ, along with a malignant spitz tumor of the external upper lip and intraductal papilloma of the nipple."]]).toDF("text")
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

val jsl_ner = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("jsl_ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "jsl_ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Oncological"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val icdo_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icdo_augmented_2026", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    jsl_ner, ner_converter, c2doc, embedder, icdo_resolver
))

val data = Seq("The patient's pathology report noted mesothelioma in situ, along with a malignant spitz tumor of the external upper lip and intraductal papilloma of the nipple.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                                       | entity      | icdo_code    | resolution_text                             | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:------------------------------------------------|:------------|:-------------|:--------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| mesothelioma in situ                            | Oncological | 9050/2       | mesothelioma in situ                        | 9050/2:::9050/3:::9055/0:::9051/3:::9052/3:::9055/1:::9052/3-C80.9:::9053/3:::90... | 0.0000:::6.5613:::6.7346:::6.7901:::7.0371:::7.7245:::7.8921:::7.9652:::8.0512::... | 0.0000:::0.0751:::0.0780:::0.0803:::0.0849:::0.1053:::0.1109:::0.1127:::0.1148::... | mesothelioma in situ:::mesothelioma:::cystic mesothelioma:::spindled mesotheliom... |
| malignant spitz tumor of the external upper lip | Oncological | 8770/3-C00.0 | malignant spitz tumor of external upper lip | 8770/3-C00.0:::8770/3-C00.2:::8770/3-C00.3:::8770/3-C00.1:::8094/3-C00.0:::8247/... | 1.3439:::4.7281:::5.5956:::6.5958:::6.6993:::7.0178:::7.0823:::7.0877:::7.1931::... | 0.0031:::0.0386:::0.0538:::0.0751:::0.0782:::0.0859:::0.0884:::0.0881:::0.0897::... | malignant spitz tumor of external upper lip:::malignant spitz tumor of external ... |
| intraductal papilloma of the nipple             | Oncological | 8503/0-C50.0 | intraductal papilloma of nipple             | 8503/0-C50.0:::8503/0-C50.9:::8505/0-C50.9:::8503/0-C50.4:::8503/0-C50.6:::8503/... | 1.4973:::5.8629:::6.0240:::6.6566:::6.6785:::6.8037:::6.8932:::6.9585:::7.3957::... | 0.0036:::0.0549:::0.0577:::0.0715:::0.0719:::0.0751:::0.0761:::0.0776:::0.0877::... | intraductal papilloma of nipple:::intraductal papilloma of breast:::intraductal ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icdo_augmented_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|228.5 MB|
|Case sensitive:|false|