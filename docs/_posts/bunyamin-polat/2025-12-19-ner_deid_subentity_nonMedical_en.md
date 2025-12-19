---
layout: model
title: Detect PHI for Deidentification(Subentity)
author: John Snow Labs
name: ner_deid_subentity_nonMedical
date: 2025-12-19
tags: [en, licensed, clinical, deid, ner, phi, subentity]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects PHI (Protected Health Information) entities for deidentification purposes. It is a subentity model capable of detecting various PHI entities with granular labels such as PATIENT, DOCTOR, HOSPITAL, STREET, CITY, ZIP, etc.

## Predicted Entities

`ACCOUNTNUM`, `AGE`, `CITY`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `DOCTOR`, `EMAIL`, `GENDER`, `HOSPITAL`, `IDNUM`, `IP`, `LOCATION_OTHER`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `TIME`, `URL`, `USERNAME`, `VIN`, `ZIP`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_nonMedical_en_6.2.2_3.4_1766168717542.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_nonMedical_en_6.2.2_3.4_1766168717542.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_deid_subentity_nonMedical", "en", "clinical/models")\
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

text = """Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA. 
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729. 
She works as a Nurse at City General Hospital. Her account number is 8003591. 
She has an appointment scheduled for March 15, 2024 at 10:30 AM."""

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
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.MedicalNerModel.pretrained("ner_deid_subentity_nonMedical", "en", "clinical/models")\
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

text = """Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA. 
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729. 
She works as a Nurse at City General Hospital. Her account number is 8003591. 
She has an appointment scheduled for March 15, 2024 at 10:30 AM."""

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

val nerModel = MedicalNerModel.pretrained("ner_deid_subentity_nonMedical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerModel,
    nerConverter
))

val data = Seq("""Emily Davis, a 34-year-old Female, Dr. Michael Johnson cares with her at CarePlus Clinic, located at 456 Elm Street, NewYork, NY 10001, USA. 
She can be reached at 555-642-1725 or via email emily.davis@gmail.com. Her SSN is 725-46-2729. 
She works as a Nurse at City General Hospital. Her account number is 8003591. 
She has an appointment scheduled for March 15, 2024 at 10:30 AM.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|chunk                |begin|end|ner_label|
|---------------------|-----|---|---------|
|Emily Davis          |0    |10 |NAME     |
|34-year-old          |15   |25 |AGE      |
|Female               |27   |32 |GENDER   |
|Michael Johnson      |39   |53 |DOCTOR   |
|CarePlus Clinic      |73   |87 |HOSPITAL |
|456 Elm Street       |101  |114|STREET   |
|NewYork              |117  |123|CITY     |
|NY                   |126  |127|STATE    |
|10001                |129  |133|ZIP      |
|USA                  |136  |138|COUNTRY  |
|555-642-1725         |164  |175|PHONE    |
|davis@gmail.com      |196  |210|EMAIL    |
|725-46-2729          |224  |234|SSN      |
|City General Hospital|262  |282|HOSPITAL |
|March 15, 2024       |354  |367|DATE     |
|10:30 AM             |372  |379|TIME     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_nonMedical|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.9 MB|