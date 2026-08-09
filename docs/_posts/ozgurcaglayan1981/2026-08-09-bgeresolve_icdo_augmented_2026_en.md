---
layout: model
title: Sentence Entity Resolver for ICD-O (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_icdo_augmented_2026
date: 2026-08-09
tags: [licensed, en, clinical, entity_resolution, icdo, bge]
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

This model maps clinical/oncology entities to ICD-O (International Classification of Diseases for Oncology) morphology/topography codes using `bge_base_en_v1_5_onnx` Sentence Embeddings. Trained on the ICD-O-3.2 2026 update dataset.

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icdo_augmented_2026_en_6.4.1_3.4_1786280219156.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icdo_augmented_2026_en_6.4.1_3.4_1786280219156.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

icdo_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

icdo_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_icdo_augmented_2026", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val icdo_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_icdo_augmented_2026", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| mesothelioma in situ                            | Oncological | 9050/2       | mesothelioma in situ                        | 9050/2:::9050/2-C38.4:::9050/2-C38.0:::9050/2-C48.2:::9050/2-C48.1:::8140/2:::80... | 0.0000:::0.4555:::0.4590:::0.4875:::0.5123:::0.5719:::0.6061:::0.6065:::0.6104::... | 0.0000:::0.1037:::0.1053:::0.1188:::0.1312:::0.1635:::0.1837:::0.1839:::0.1863::... | mesothelioma in situ:::mesothelioma in situ of pleura, nos:::mesothelioma in sit... |
| malignant spitz tumor of the external upper lip | Oncological | 8770/3-C00.0 | malignant spitz tumor of external upper lip | 8770/3-C00.0:::8770/3-C00.2:::8770/3-C00.1:::8770/3-C00.9:::8770/3-C00.3:::8770/... | 0.0731:::0.2564:::0.3159:::0.3841:::0.3928:::0.4207:::0.4234:::0.4386:::0.4539::... | 0.0027:::0.0329:::0.0499:::0.0737:::0.0771:::0.0885:::0.0896:::0.0962:::0.1030::... | malignant spitz tumor of external upper lip:::malignant spitz tumor of external ... |
| intraductal papilloma of the nipple             | Oncological | 8503/0-C50.0 | intraductal papilloma of nipple             | 8503/0-C50.0:::8503/0-C50.9:::8507/2-C50.0:::8503/0:::8503/0-C50.1:::8503/0-C50.... | 0.0895:::0.3644:::0.4522:::0.4585:::0.4612:::0.4896:::0.4928:::0.4996:::0.5014::... | 0.0040:::0.0664:::0.1023:::0.1051:::0.1063:::0.1198:::0.1214:::0.1248:::0.1257::... | intraductal papilloma of nipple:::intraductal papilloma of breast:::intraductal ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_icdo_augmented_2026|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|228.8 MB|
|Case sensitive:|false|