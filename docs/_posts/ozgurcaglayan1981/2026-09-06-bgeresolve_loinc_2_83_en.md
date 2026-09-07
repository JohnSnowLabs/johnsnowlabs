---
layout: model
title: Sentence Entity Resolver for LOINC (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_loinc_2_83
date: 2026-09-06
tags: [en, entity_resolution, licensed, clinical, loinc, bge]
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

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes (LOINC) codes using `bge_base_en_v1_5_onnx` embeddings.

Trained on the official LOINC 2.83 dataset.

This model may also resolve to non-numeric LOINC codes, including LOINC's own internal Part codes (prefixed "LP"). If you only need numeric, directly orderable/reportable LOINC codes, use `bgeresolve_loinc_numeric_2_83` instead.

It also provides the official resolution of the codes within the brackets.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_loinc_2_83_en_6.4.1_3.4_1788715373419.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_loinc_2_83_en_6.4.1_3.4_1788715373419.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_radiology = MedicalNerModel.pretrained("ner_radiology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_radiology")

ner_converter_radiology = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_radiology"])\
    .setOutputCol("ner_chunk_radiology")\
    .setWhiteList(["Test"])

ner_jsl = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter_jsl = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Test"])

chunk_merger = ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol("ner_chunk")

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_loinc_2_83","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, chunk2doc,\
    embedder, resolver\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_radiology = medical.NerModel.pretrained("ner_radiology","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_radiology")

ner_converter_radiology = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_radiology"])\
    .setOutputCol("ner_chunk_radiology")\
    .setWhiteList(["Test"])

ner_jsl = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_jsl")

ner_converter_jsl = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_jsl"])\
    .setOutputCol("ner_chunk_jsl")\
    .setWhiteList(["Test"])

chunk_merger = medical.ChunkMergeApproach()\
    .setInputCols("ner_chunk_jsl", "ner_chunk_radiology")\
    .setOutputCol("ner_chunk")

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_loinc_2_83","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, chunk2doc,\
    embedder, resolver\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_radiology = MedicalNerModel
    .pretrained("ner_radiology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_radiology")

val ner_converter_radiology = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_radiology"))
    .setOutputCol("ner_chunk_radiology")
    .setWhiteList(Array("Test"))

val ner_jsl = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl")

val ner_converter_jsl = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk_jsl")
    .setWhiteList(Array("Test"))

val chunk_merger = new ChunkMergeApproach()
    .setInputCols(Array("ner_chunk_jsl", "ner_chunk_radiology"))
    .setOutputCol("ner_chunk")

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_loinc_2_83", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,
    chunk_merger, chunk2doc,
    embedder, resolver
))

val data = Seq("The patient's glucose and hemoglobin A1c levels were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk             | entity   | LOINC Code   | Resolution                                                      | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:----------------------|:---------|:-------------|:----------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| glucose               | Test     | 2345-7       | glucose [Glucose [Mass/volume] in Serum or Plasma]              | 2345-7:::104638-2:::62418-9:::50016-5:::6883-3:::4269-7:::2349-9:::54487-4:::LP7... | 0.0000:::0.1421:::0.1465:::0.1497:::0.1604:::0.1643:::0.1693:::0.1709:::0.1721::... | glucose [Glucose [Mass/volume] in Serum or Plasma]:::Glucose SD [Glucose standar... |
| hemoglobin A1c levels | Test     | 41995-2      | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]          | 41995-2:::4548-4:::86910-7:::17856-6:::112870-1:::17855-8:::71875-9:::4549-2:::9... | 0.0678:::0.1064:::0.1390:::0.1409:::0.1531:::0.1654:::0.1654:::0.1668:::0.1808::... | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]:::Hgb A1c [Hemoglobin A1c... |
| basic metabolic panel | Test     | 51990-0      | basic metabolic panel [Basic metabolic panel - Blood]           | 51990-0:::89044-2:::101655-9:::24321-2:::24320-4:::104076-5:::54233-2:::70219-1:... | 0.0000:::0.0534:::0.0710:::0.0733:::0.0872:::0.1042:::0.1393:::0.1453:::0.1473::... | basic metabolic panel [Basic metabolic panel - Blood]:::basic metabolic & albumi... |
| sodium                | Test     | 2951-2       | sodium [Sodium [Moles/volume] in Serum or Plasma]               | 2951-2:::81011-9:::28003-2:::23915-2:::9485-4:::32553-0:::35678-2:::34548-8:::16... | 0.0000:::0.1499:::0.1508:::0.1727:::0.1768:::0.1892:::0.1922:::0.1935:::0.1935::... | sodium [Sodium [Moles/volume] in Serum or Plasma]:::sodium intake [Sodium intake... |
| potassium             | Test     | 2823-3       | potassium [Potassium [Moles/volume] in Serum or Plasma]         | 2823-3:::10322-6:::32550-6:::75940-7:::86919-8:::28003-2:::35677-4:::6940-1:::90... | 0.0000:::0.1556:::0.1817:::0.1926:::0.1938:::0.1938:::0.2008:::0.2056:::0.2076::... | potassium [Potassium [Moles/volume] in Serum or Plasma]:::potassium intake [Pota... |
| complete blood count  | Test     | 24358-4      | Complete Blood Count [Hemogram without Platelets panel - Blood] | 24358-4:::58410-2:::47288-6:::74412-8:::51876-1:::1335-9:::LP71083-7:::11282-1::... | 0.0000:::0.1182:::0.1736:::0.1781:::0.1821:::0.1907:::0.1925:::0.2017:::0.2021::... | Complete Blood Count [Hemogram without Platelets panel - Blood]:::complete blood... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_loinc_2_83|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|877.7 MB|
|Case sensitive:|false|