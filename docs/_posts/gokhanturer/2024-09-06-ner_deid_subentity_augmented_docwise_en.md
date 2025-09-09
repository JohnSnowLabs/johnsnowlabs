---
layout: model
title: Detect PHI for Deidentification (Subentity_Augmented - Docwise)
author: John Snow Labs
name: ner_deid_subentity_augmented_docwise
date: 2024-09-06
tags: [en, clinical, licensed, ner, deid]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Named Entity Recognition (NER) annotator works at the document level, allowing it to identify and annotate entities throughout an entire document. It leverages a deep learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired by the former state-of-the-art model for NER developed by Chiu & Nichols: "Named Entity Recognition with Bidirectional LSTM-CNN". This NER model is particularly useful for detecting protected health information (PHI) that may need to be de-identified. It can recognize and annotate specific entities: `MEDICALRECORD`, `LOCATION`, `ORGANIZATION`, `PROFESSION`, `DOCTOR`, `USERNAME`, `DEVICE`, `CITY`, `DATE`, `ZIP`, `STATE`, `PATIENT`, `LOCATION_OTHER`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `DLN`, `IDNUM`, `AGE` .

## Predicted Entities

`MEDICALRECORD`, `LOCATION`, `ORGANIZATION`, `PROFESSION`, `DOCTOR`, `USERNAME`, `DEVICE`, `CITY`, `DATE`, `ZIP`, `STATE`, `PATIENT`, `LOCATION_OTHER`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `DLN`, `IDNUM`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.0.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_docwise_en_5.4.1_3.0_1725653838333.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_augmented_docwise_en_5.4.1_3.0_1725653838333.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

tokenizer = Tokenizer()\
      .setInputCols(["document"])\
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
      .setInputCols(["document", "token"])\
      .setOutputCol("embeddings")

ner_deid = MedicalNerModel.pretrained("ner_deid_subentity_augmented_docwise", "en", "clinical/models")  \
      .setInputCols(["document", "token", "embeddings"]) \
      .setOutputCol("ner_deid_subentity_augmented_docwise")

ner_deid_converter = NerConverterInternal()\
      .setInputCols(["document", "token", "ner_deid_subentity_augmented_docwise"])\
      .setOutputCol("ner_chunk_subentity_augmented_docwise")

nlpPipeline = Pipeline(stages=[
      documentAssembler,
      tokenizer,
      word_embeddings,
      ner_deid,
      ner_deid_converter,
      ])

text = '''Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024. The patient’s medical record number is 56467890. The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 .'''

data = spark.createDataFrame([[text]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val nerDeid = MedicalNerModel.pretrained("ner_deid_subentity_augmented_docwise", "en", "clinical/models")
    .setInputCols(Array("document", "token", "embeddings"))
    .setOutputCol("ner_deid_subentity_augmented_docwise")

val nerDeidConverter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner_deid_subentity_augmented_docwise"))
    .setOutputCol("ner_chunk_subentity_augmented_docwise")

val nlpPipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    wordEmbeddings,
    nerDeid,
    nerDeidConverter
))

val text = Seq("Dr. John Lee, from Royal Medical Clinic in Chicago, attended to the patient on 11/05/2024. The patient’s medical record number is 56467890. The patient, Emma Wilson, is 50 years old, her Contact number: 444-456-7890.").toDF("text")

val data = Seq((text)).toDF("text")
val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------+-----+---+-------------+
|chunk               |begin|end|ner_label    |
+--------------------+-----+---+-------------+
|John Lee            |4    |11 |DOCTOR       |
|Royal Medical Clinic|19   |38 |HOSPITAL     |
|Chicago             |43   |49 |CITY         |
|11/05/2024          |80   |89 |DATE         |
|56467890            |131  |138|MEDICALRECORD|
|Emma Wilson         |154  |164|PATIENT      |
|50                  |170  |171|AGE          |
|444-456-7890        |205  |216|PHONE        |
+--------------------+-----+---+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_augmented_docwise|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|34.5 MB|

## Benchmarking

```bash
          label      tp     fp     fn   total precision  recall      f1
        PATIENT  1328.0  115.0  163.0  1491.0    0.9203  0.8907  0.9052
       HOSPITAL  2160.0  116.0   64.0  2224.0    0.9490  0.9712  0.9600
           DATE  5310.0  115.0   35.0  5345.0    0.9788  0.9935  0.9861
   ORGANIZATION   177.0   23.0   49.0   226.0    0.8850  0.7832  0.8310
           CITY   289.0   21.0   22.0   311.0    0.9323  0.9293  0.9308
 LOCATION_OTHER    22.0    0.0   10.0    32.0    1.0000  0.6875  0.8148
         STREET   415.0   37.0   39.0   454.0    0.9181  0.9141  0.9161
       USERNAME    73.0    2.0    8.0    81.0    0.9733  0.9012  0.9359
         DEVICE    24.0    1.0    3.0    27.0    0.9600  0.8889  0.9231
          IDNUM   157.0   62.0   35.0   192.0    0.7169  0.8177  0.7640
          STATE    98.0   19.0   30.0   128.0    0.8376  0.7656  0.8000
       LOCATION    99.0   36.0   49.0   148.0    0.7333  0.6689  0.6996
            DLN    39.0   17.0    9.0    48.0    0.6964  0.8125  0.7500
            ZIP   136.0    4.0    4.0   140.0    0.9714  0.9714  0.9714
  MEDICALRECORD   376.0    9.0   49.0   425.0    0.9766  0.8847  0.9284
     PROFESSION   409.0   33.0   32.0   441.0    0.9253  0.9274  0.9264
          PHONE   288.0   28.0    9.0   297.0    0.9114  0.9697  0.9396
        COUNTRY   238.0   20.0   16.0   254.0    0.9225  0.9370  0.9297
         DOCTOR  2855.0  256.0  157.0  3012.0    0.9177  0.9479  0.9325
            AGE   789.0   18.0   21.0   810.0    0.9777  0.9741  0.9759
          MACRO      -      -      -      -         -       -    0.8910
          MICRO      -      -      -      -         -       -    0.9460
```
