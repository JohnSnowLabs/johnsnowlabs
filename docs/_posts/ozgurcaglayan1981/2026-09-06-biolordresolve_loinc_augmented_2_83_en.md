---
layout: model
title: Sentence Entity Resolver for LOINC (augmented) (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_loinc_augmented_2_83
date: 2026-09-06
tags: [en, entity_resolution, licensed, clinical, loinc, biolord]
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

This model maps extracted clinical NER entities to Logical Observation Identifiers Names and Codes (LOINC) codes using `mpnet_embeddings_biolord_2023_c` embeddings.

Trained on the augmented version of the LOINC 2.83 dataset (LOINC 2.83 official data plus an in-house curated dataset).

This model may also resolve to non-numeric LOINC codes, including LOINC's own internal Part, Answer, Panel, Survey, and other auxiliary/document codes (e.g. "LP...", "LA...", "PANEL...", "SURVEY..."). If you only need numeric, directly orderable/reportable LOINC codes, use `biolordresolve_loinc_numeric_augmented_2_83` instead.

It also provides the official resolution of the codes within the brackets.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_loinc_augmented_2_83_en_6.4.1_3.4_1788722318798.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_loinc_augmented_2_83_en_6.4.1_3.4_1788722318798.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_loinc_augmented_2_83","en","clinical/models")\
    .setInputCols(["biolord_embeddings"])\
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

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("biolord_embeddings")\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_loinc_augmented_2_83","en","clinical/models")\
    .setInputCols(["biolord_embeddings"])\
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

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("biolord_embeddings")
    .setBatchSize(1)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_loinc_augmented_2_83", "en", "clinical/models")
    .setInputCols(Array("biolord_embeddings"))
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
| glucose               | Test     | 2345-7       | glucose [Glucose [Mass/volume] in Serum or Plasma]              | 2345-7:::47621-8:::50016-5:::104638-2:::6883-3:::2344-0:::LP89291-6:::4269-7:::3... | 0.0000:::0.1485:::0.1675:::0.1755:::0.1831:::0.1927:::0.1951:::0.2043:::0.2133::... | glucose [Glucose [Mass/volume] in Serum or Plasma]:::Glucose IV [Glucose.IV [Mas... |
| hemoglobin A1c levels | Test     | 41995-2      | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]          | 41995-2:::4548-4:::51196-4:::4547-6:::112870-1:::96595-4:::17856-6:::74246-0:::6... | 0.0811:::0.1184:::0.1905:::0.2340:::0.2511:::0.2618:::0.2672:::0.2739:::0.2786::... | hemoglobin a1c [Hemoglobin A1c [Mass/volume] in Blood]:::Hgb A1c [Hemoglobin A1c... |
| basic metabolic panel | Test     | 51990-0      | basic metabolic panel [Basic metabolic panel - Blood]           | 51990-0:::24320-4:::24321-2:::24323-8:::24322-0:::LP265616-5:::89044-2:::101655-... | 0.0000:::0.0953:::0.1003:::0.1104:::0.1117:::0.1186:::0.1420:::0.1659:::0.1816::... | basic metabolic panel [Basic metabolic panel - Blood]:::basic metabolic 1998 pan... |
| sodium                | Test     | 2951-2       | sodium [Sodium [Moles/volume] in Serum or Plasma]               | 2951-2:::2950-4:::32340-2:::LA24059-0:::23915-2:::9485-4:::2955-3:::2954-6:::152... | 0.0000:::0.1630:::0.1713:::0.1845:::0.2493:::0.2564:::0.2610:::0.2807:::0.2852::... | sodium [Sodium [Moles/volume] in Serum or Plasma]:::Sodium, Body fluid [Sodium [... |
| potassium             | Test     | 2823-3       | potassium [Potassium [Moles/volume] in Serum or Plasma]         | 2823-3:::2821-7:::32336-0:::59733-6:::9482-1:::2828-2:::28003-2:::2820-9:::50902... | 0.0000:::0.1396:::0.1573:::0.1962:::0.2145:::0.2289:::0.2364:::0.2468:::0.2561::... | potassium [Potassium [Moles/volume] in Serum or Plasma]:::Potassium, Body fluid ... |
| complete blood count  | Test     | 24358-4      | Complete Blood Count [Hemogram without Platelets panel - Blood] | 24358-4:::58410-2:::11282-1:::LP7803-2:::786-4:::33255-1:::112620-0:::74412-8:::... | 0.0000:::0.1648:::0.1689:::0.2476:::0.2574:::0.2604:::0.2844:::0.2986:::0.3003::... | Complete Blood Count [Hemogram without Platelets panel - Blood]:::complete blood... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_loinc_augmented_2_83|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[loinc_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|