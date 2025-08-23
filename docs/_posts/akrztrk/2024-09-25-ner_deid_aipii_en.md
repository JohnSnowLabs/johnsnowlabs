---
layout: model
title: Detect PHI for Deidentification (ai4privacy/pii-masking-400k)
author: John Snow Labs
name: ner_deid_aipii
date: 2024-09-25
tags: [deid, clinical, en, licensed, ner]
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

This Named Entity Recognition (NER) annotator is trained using the `ai4privacy/pii-masking-400k` dataset. It leverages a deep learning architecture (Char CNNs - BiLSTM - CRF - word embeddings), inspired by the state-of-the-art model from Chiu & Nichols in their work "Named Entity Recognition with Bidirectional LSTM-CNN". This model is particularly effective in identifying and labeling various entities, making it useful for detecting protected health information (PHI) that may need to be masked or de-identified.

## Predicted Entities

`LICENSE`, `SSN`, `ZIP`, `NAME`, `PHONE`, `CITY`, `EMAIL`, `DATE`, `IDNUM`, `STREET`, `ACCOUNT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/01.0.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_aipii_en_5.4.1_3.0_1727266249887.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_aipii_en_5.4.1_3.0_1727266249887.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained('ner_deid_aipii', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])

sample_texts = ["""
Ora Hendrickson, is 50 years old,  Patient's ID no: 3454362A, SSN: 333-44-6666,
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: ora@gmail.com.
"""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_deid_aipii", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""Ora Hendrickson, is 50 years old,  Patient's ID no: 3454362A, SSN: 333-44-6666,
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: ora@gmail.com.""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+-----------------+-----+---+---------+
|chunk            |begin|end|ner_label|
+-----------------+-----+---+---------+
|Ora Hendrickson  |2    |16 |NAME     |
|3454362A         |54   |61 |IDNUM    |
|333-44-6666      |69   |79 |SSN      |
|(302) 786-5227   |88   |101|PHONE    |
|0295 Keats Street|104  |120|STREET   |
|San Francisco    |123  |135|CITY     |
|ora@gmail.com    |146  |158|EMAIL    |
+-----------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_aipii|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
     ACCOUNT       0.86      0.59      0.70       867
        CITY       0.95      0.94      0.94      2735
        DATE       0.91      0.66      0.77      1408
       EMAIL       1.00      1.00      1.00      1469
       IDNUM       0.87      0.87      0.87      2763
     LICENSE       0.95      0.93      0.94       691
        NAME       0.96      0.97      0.97      6071
       PHONE       0.99      0.99      0.99      2182
         SSN       0.83      0.90      0.86       914
      STREET       0.93      0.91      0.92      2882
         ZIP       0.91      0.98      0.94      1271
   micro-avg       0.94      0.91      0.92     23253
   macro-avg       0.92      0.89      0.90     23253
weighted-avg       0.93      0.91      0.92     23253
```
