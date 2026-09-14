---
layout: model
title: Mapping Entities with Corresponding LOINC Codes
author: John Snow Labs
name: loinc_numeric_mapper_2_83
date: 2026-09-06
tags: [en, chunk_mapper, licensed, clinical, loinc]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps entities extracted from text to their corresponding LOINC (Logical Observation Identifiers Names and Codes) codes.

It performs a direct lookup against the training dictionary, providing fast, exact-match code mapping.

Trained on the augmented version of the LOINC 2.83 dataset (LOINC 2.83 official data plus an in-house curated dataset), scoped to numeric LOINC codes, without the inclusion of LOINC's non-numeric Part, Answer, Panel, Survey, and other auxiliary/document codes.

If you also need LOINC's non-numeric auxiliary codes, use `loinc_mapper_2_83` instead.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_mapper_2_83_en_6.4.1_3.4_1788729639223.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/loinc_numeric_mapper_2_83_en_6.4.1_3.4_1788729639223.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

loinc_mapper = ChunkMapperModel.pretrained("loinc_numeric_mapper_2_83", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["loinc_code"])

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, loinc_mapper\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
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

loinc_mapper = medical.ChunkMapperModel.pretrained("loinc_numeric_mapper_2_83", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["loinc_code"])

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,\
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,\
    chunk_merger, loinc_mapper\
])

data = spark.createDataFrame([["The patient's glucose and hemoglobin A1c were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count."]]).toDF("text")
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

val loincMapper = ChunkMapperModel.pretrained("loinc_numeric_mapper_2_83", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("loinc_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner_radiology, ner_converter_radiology, ner_jsl, ner_converter_jsl,
    chunk_merger, loincMapper
))

val data = Seq("The patient's glucose and hemoglobin A1c were checked, along with a basic metabolic panel including sodium and potassium, and a complete blood count.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk             | loinc_code   | all_k_resolutions           |
|:----------------------|:-------------|:----------------------------|
| glucose               | 2345-7       | 2345-7:::                   |
| hemoglobin A1c        | 41995-2      | 41995-2:::                  |
| basic metabolic panel | 51990-0      | 51990-0:::                  |
| sodium                | 2951-2       | 2951-2:::                   |
| potassium             | 2823-3       | 2823-3:::                   |
| complete blood count  | 24317-0      | 24317-0:::24358-4:::24359-2 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|loinc_numeric_mapper_2_83|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|12.8 MB|