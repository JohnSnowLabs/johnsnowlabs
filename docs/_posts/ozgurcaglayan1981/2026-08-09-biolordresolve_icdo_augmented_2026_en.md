---
layout: model
title: Sentence Entity Resolver for ICD-O (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_icdo_augmented_2026
date: 2026-08-09
tags: [licensed, en, clinical, entity_resolution, icdo, biolord]
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

This model maps clinical/oncology entities to ICD-O (International Classification of Diseases for Oncology) morphology/topography codes using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings. Trained on the ICD-O-3.2 2026 update dataset.

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icdo_augmented_2026_en_6.4.1_3.4_1786279454429.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_icdo_augmented_2026_en_6.4.1_3.4_1786279454429.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

icdo_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
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

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

icdo_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
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

val embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)
    .setBatchSize(1)

val icdo_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icdo_augmented_2026", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
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
| mesothelioma in situ                            | Oncological | 9050/2       | mesothelioma in situ                        | 9050/2:::9050/2-C38.4:::9050/2-C48.1:::9050/2-C48.2:::9050/3:::9051/3:::9052/3::... | 0.0000:::0.5000:::0.6029:::0.6103:::0.6616:::0.6904:::0.7085:::0.7418:::0.7736::... | 0.0000:::0.1250:::0.1817:::0.1862:::0.2188:::0.2383:::0.2510:::0.2751:::0.2992::... | mesothelioma in situ:::mesothelioma in situ of pleura, nos:::mesothelioma in sit... |
| malignant spitz tumor of the external upper lip | Oncological | 8770/3-C00.0 | malignant spitz tumor of external upper lip | 8770/3-C00.0:::8770/3-C00.3:::8770/3-C00.2:::8770/3-C44.0:::8770/3-C00.9:::8770/... | 0.1179:::0.2887:::0.2930:::0.3589:::0.3743:::0.4274:::0.4550:::0.4902:::0.5282::... | 0.0069:::0.0417:::0.0429:::0.0644:::0.0701:::0.0913:::0.1035:::0.1202:::0.1395::... | malignant spitz tumor of external upper lip:::malignant spitz tumor of mucosa of... |
| intraductal papilloma of the nipple             | Oncological | 8503/0-C50.0 | intraductal papilloma of nipple             | 8503/0-C50.0:::8503/0-C50.9:::8505/0-C50.9:::8503/0-C50.1:::8050/0-C50.9:::8503/... | 0.1385:::0.3271:::0.3699:::0.4277:::0.4762:::0.4777:::0.4964:::0.5253:::0.5268::... | 0.0096:::0.0535:::0.0684:::0.0914:::0.1134:::0.1141:::0.1232:::0.1380:::0.1388::... | intraductal papilloma of nipple:::intraductal papilloma of breast:::intraductal ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_icdo_augmented_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|228.9 MB|
|Case sensitive:|false|