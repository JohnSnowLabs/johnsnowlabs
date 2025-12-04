---
layout: model
title: Mapping Entities with Corresponding ICD-10-CM Codes
author: John Snow Labs
name: icd10cm_mapper
date: 2025-12-04
tags: [mapper, icd10cm, en, licensed, clinical, chunk_mapper]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities to their corresponding ICD-10-CM codes. It provides fast and accurate clinical code mapping without requiring embeddings.

## Predicted Entities

`ICD-10-CM Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_en_6.2.0_3.4_1764891297647.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_mapper_en_6.2.0_3.4_1764891297647.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

icd10cm_mapper = ChunkMapperModel.pretrained("icd10cm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd10cm_code"])

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    icd10cm_mapper
])

text = """A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

icd10cm_mapper = medical.ChunkMapperModel.pretrained("icd10cm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["icd10cm_code"])

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter,
    icd10cm_mapper
])

text = """A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerModel = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val icd10cmMapper = ChunkMapperModel.pretrained("icd10cm_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("icd10cm_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerModel,
    nerConverter,
    icd10cmMapper
))

val data = Seq("""A 58-year-old male presents with sciatica and myalgia affecting his lower extremities. He has a history of polymyositis, currently managed with medication. The patient also reports glossitis and beriberi due to nutritional deficiency. Recently, he developed spondylolysis and experiences motion sickness during travel.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|ner_chunk             |mapping_result|
|----------------------|--------------|
|sciatica              |M54.3         |
|myalgia               |M79.1         |
|polymyositis          |M33.2         |
|glossitis             |K14.0         |
|beriberi              |E51.1         |
|nutritional deficiency|E63.9         |
|spondylolysis         |M43.0         |
|motion sickness       |T75.3         |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_mapper|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|24.3 MB|
