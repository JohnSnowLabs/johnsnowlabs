---
layout: model
title: Detect PHI for Deidentification (Subentity - Docwise)
author: John Snow Labs
name: ner_deid_subentity_docwise
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

The Named Entity Recognition (NER) annotator works at the document level, allowing it to identify and annotate entities throughout an entire document. It leverages a deep learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired by the former state-of-the-art model for NER developed by Chiu & Nichols: "Named Entity Recognition with Bidirectional LSTM-CNN". This NER model is particularly useful for detecting protected health information (PHI) that may need to be de-identified. It can recognize and annotate  specific entities: `MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `DATE`, `ZIP`, `PATIENT`, `COUNTRY`, `AGE`, `FAX`, `HOSPITAL`, `BIOID`, `IDNUM`, `STREET`, `EMAIL` .

## Predicted Entities

`MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `DATE`, `ZIP`, `PATIENT`, `COUNTRY`, `AGE`, `FAX`, `HOSPITAL`, `BIOID`, `IDNUM`, `STREET`, `EMAIL`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_docwise_en_5.4.1_3.0_1725652947001.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_docwise_en_5.4.1_3.0_1725652947001.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical") \
      .setInputCols(["document", "token"])\
      .setOutputCol("embeddings")

ner_deid = MedicalNerModel.pretrained("ner_deid_subentity_docwise", "en", "clinical/models")  \
      .setInputCols(["document", "token", "embeddings"]) \
      .setOutputCol("ner_deid_subentity_docwise")

ner_deid_converter = NerConverterInternal()\
      .setInputCols(["document", "token", "ner_deid_subentity_docwise"])\
      .setOutputCol("ner_chunk_subentity_docwise")

nlpPipeline = Pipeline(stages=[
      documentAssembler,
      tokenizer,
      word_embeddings,
      ner_deid,
      ner_deid_converter,
      ])

text = '''Emily Davis, a 34-year-old woman, Dr. Michael Johnson cares wit her, at CarePlus Clinic, located at 456 Elm Street, NewYork, NY has recommended starting insulin therapy. She has an appointment scheduled for March 15, 2024.'''

deid_model = nlpPipeline.fit(empty_data)

result = deid_model.transform(spark.createDataFrame([[text]]).toDF("text"))
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

val nerDeid = MedicalNerModel.pretrained("ner_deid_subentity_docwise", "en", "clinical/models")
    .setInputCols(Array("document", "token", "embeddings"))
    .setOutputCol("ner_deid_subentity_docwise")

val nerDeidConverter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner_deid_subentity_docwise"))
    .setOutputCol("ner_chunk_subentity_docwise")

val nlpPipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    wordEmbeddings,
    nerDeid,
    nerDeidConverter
))

val text = Seq("Emily Davis, a 34-year-old woman, Dr. Michael Johnson cares with her, at CarePlus Clinic, located at 456 Elm Street, New York, NY has recommended starting insulin therapy. She has an appointment scheduled for March 15, 2024.").toDF("text")

val model = nlpPipeline.fit(spark.emptyDataFrame)
l
val result = model.transform(text)

```
</div>

## Results

```bash
+---------------+-----+---+---------+
|chunk          |begin|end|ner_label|
+---------------+-----+---+---------+
|Emily Davis    |0    |10 |PATIENT  |
|34-year-old    |15   |25 |AGE      |
|Michael Johnson|38   |52 |DOCTOR   |
|CarePlus Clinic|72   |86 |HOSPITAL |
|456 Elm Street |100  |113|STREET   |
|NewYork        |116  |122|CITY     |
|NY             |125  |126|STATE    |
|March 15, 2024 |207  |220|DATE     |
+---------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_docwise|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|9.3 MB|

## Benchmarking

```bash
        label      tp    fp    fn    total  precision  recall      f1
      PATIENT  1216.0  60.0   64.0  1280.0     0.9530  0.9500  0.9515
     HOSPITAL  1030.0  68.0  125.0  1155.0     0.9381  0.8918  0.9143
         DATE  3859.0  63.0   89.0  3948.0     0.9839  0.9775  0.9807
 ORGANIZATION    60.0  41.0   27.0    87.0     0.5941  0.6897  0.6383
         CITY   226.0  20.0   30.0   256.0     0.9187  0.8828  0.9004
       STREET   305.0   6.0    2.0   307.0     0.9807  0.9935  0.9871
     USERNAME    57.0  10.0   11.0    68.0     0.8507  0.8382  0.8444
       DEVICE     5.0   0.0    3.0     8.0     1.0000  0.6250  0.7692
          FAX     0.0   0.0    4.0     4.0     0.0000  0.0000  0.0000
        IDNUM   128.0  12.0   35.0   163.0     0.9143  0.7853  0.8449
        STATE   156.0  19.0   16.0   172.0     0.8914  0.9070  0.8991
        EMAIL     0.0   0.0    1.0     1.0     0.0000  0.0000  0.0000
          ZIP   102.0   1.0    0.0   102.0     0.9903  1.0000  0.9951
MEDICALRECORD   310.0   6.0   16.0   326.0     0.9810  0.9509  0.9657
        OTHER     4.0   9.0    0.0     4.0     0.3077  1.0000  0.4706
   PROFESSION   234.0  20.0   64.0   298.0     0.9213  0.7852  0.8478
        PHONE   253.0  10.0    7.0   260.0     0.9620  0.9731  0.9675
      COUNTRY    35.0   3.0   18.0    53.0     0.9211  0.6604  0.7692
       DOCTOR  2566.0  25.0  211.0  2777.0     0.9904  0.9240  0.9560
          AGE   498.0  23.0   26.0   524.0     0.9559  0.9504  0.9531
        MACRO      -      -     -      -          -       -    0.7826
        MICRO      -      -     -      -          -       -    0.9504
```