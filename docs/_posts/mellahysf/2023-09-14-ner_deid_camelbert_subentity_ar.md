---
layout: model
title: Detect Subentity PHI for Deidentification (CamelBERT, Arabic)
author: John Snow Labs
name: ner_deid_subentity_camelbert
date: 2023-09-14
tags: [licensed, ner, clinical, deidentification, subentity, arabic, ar, camelbert, bert]
task: Named Entity Recognition
language: ar
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition annotators allow for a generic model to be trained by using a Deep Learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM,CNN.

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 17 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model uses CamelBERT Arabic Embeddings.

## Predicted Entities

`PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_camelbert_ar_5.1.0_3.0_1694712542093.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_camelbert_ar_5.1.0_3.0_1694712542093.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = BertEmbeddings.pretrained("bert_embeddings_base_arabic_camel_msa","ar") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity_camelbert", "ar", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = Pipeline(
    stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        clinical_ner,
        ner_converter
    ])

text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''
data = spark.createDataFrame([[text]]).toDF("text")
results = nlpPipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_base_arabic_camel_msa", "ar")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(true)  

val clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity_camelbert", "ar", "clinical/models")
    .setInputCols(Array("sentence","token","word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, 
    sentenceDetector, 
    tokenizer, 
    embeddings, 
    clinical_ner, 
    ner_converter))

text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''

val data = Seq(text).toDS.toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------+--------------------------+
|chunk           |ner_label|
+--------------+--------------------------+
|الدكتور محمد                |DOCTOR   |
|55 سنة                       |AGE      |
|15/05/2000           |DATE     |
|الرباط                         |CITY     |
|0610948234          |PHONE    |
|abcd@gmail.com |EMAIL    |
+--------------+---------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_camelbert|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|16.4 MB|

## Benchmarking

```bash
label         Precision   Recall      F1
AGE           98.08       99.51       98.79
CITY          87.17       92.03       89.53
COUNTRY       90.32       84.85       87.50
DATE          98.07       97.30       97.68
DOCTOR        92.09       91.90       91.99
EMAIL         100.00      100.00      100.00
HOSPITAL      84.32       91.28       87.67
IDNUM         92.86       100.00      96.30
MEDICALRECORD 61.54       94.12       74.42
ORGANIZATION  81.58       68.89       74.70
PATIENT       75.00       83.41       78.98
PHONE         97.06       82.50       89.19
PROFESSION    89.72       85.97       87.80
SEX           98.71       81.33       89.18
STREET        100.00      96.77       98.36
USERNAME      100.00      100.00      100.00
ZIP           95.24       100.00      97.56
Macro         -           -           94.00
Micro         -           -           95.00
```
