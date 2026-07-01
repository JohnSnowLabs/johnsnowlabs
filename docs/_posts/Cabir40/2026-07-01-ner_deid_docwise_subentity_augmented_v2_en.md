---
layout: model
title: Detect PHI for Deidentification (Subentity Augmented - Docwise) (ner_deid_docwise_subentity_augmented_v2)
author: John Snow Labs
name: ner_deid_docwise_subentity_augmented_v2
date: 2026-07-01
tags: [licensed, en, ner, deid, deidentification, clinical, docwise, subentity, augmented]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition model that detects PHI (Protected Health Information) entities in clinical text for de-identification purposes, using a fine-grained sub-entity set (DOCTOR, PATIENT, HOSPITAL, DATE, AGE, PHONE, EMAIL, SSN, IDNUM, MEDICALRECORD, ORGANIZATION, STREET, CITY, STATE, COUNTRY, ZIP, LOCATION, PROFESSION, USERNAME, URL, IP, DEVICE, ACCOUNT, LICENSE, PLATE, VIN, BIOID, and more). Trained with additional augmented data for improved robustness, for document-wise processing of clinical notes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_docwise_subentity_augmented_v2_en_6.4.1_3.0_1782946285387.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_docwise_subentity_augmented_v2_en_6.4.1_3.0_1782946285387.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_deid_docwise_subentity_augmented_v2", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter
])

data = spark.createDataFrame([["""
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = medical.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_deid_docwise_subentity_augmented_v2", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter
])

data = spark.createDataFrame([["""
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
"""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_deid_docwise_subentity_augmented_v2", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_converter
))

val data = Seq("""
Mr. James Wilson is a 65-year-old male who presented to the emergency department at Boston General Hospital on 10/25/2023.
He lives at 123 Oak Street, Springfield, IL 62704. He can be contacted at 555-0199.
His SSN is 999-00-1234. Dr. Gregory House is the attending physician.
""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------+------+
|chunk_text |entity|
+-----------+------+
|            |      |
+-----------+------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_docwise_subentity_augmented_v2|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[splitter, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.1 MB|