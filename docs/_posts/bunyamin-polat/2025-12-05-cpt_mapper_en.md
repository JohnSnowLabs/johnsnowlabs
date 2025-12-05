---
layout: model
title: Mapping Entities with Corresponding CPT Codes
author: John Snow Labs
name: cpt_mapper
date: 2025-12-05
tags: [mapper, cpt, en, licensed, clinical, chunk_mapper]
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

This model maps clinical entities (procedures, tests, treatments) to their corresponding CPT (Current Procedural Terminology) codes. It provides fast and accurate procedural code mapping without requiring embeddings.

## Predicted Entities

`CPT Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_mapper_en_6.2.0_3.4_1764898398392.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_mapper_en_6.2.0_3.4_1764898398392.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test", "Treatment", "Clinical_Dept"])

cpt_mapper = ChunkMapperModel.load("cpt_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["cpt_code"])\
    .setLowerCase(True)

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    cpt_mapper
])

text = """A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test", "Treatment", "Clinical_Dept"])

cpt_mapper = medical.ChunkMapperModel.load("cpt_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["cpt_code"])\
    .setLowerCase(True)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    cpt_mapper
])

text = """A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerModel = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerModelConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test", "Treatment", "Clinical_Dept"))

val cptMapper = ChunkMapperModel.pretrained("cpt_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("cpt_code"))
    .setLowerCase(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerModel,
    nerModelConverter,
    cptMapper
))

val data = Seq("""A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|ner_chunk         |mapping_result|
|------------------|--------------|
|episiotomy        |59300         |
|Pulse oximetry    |94760         |
|blood transfusion |36430         |
|inpatient hospital|1021881       |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_mapper|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|5.1 MB|