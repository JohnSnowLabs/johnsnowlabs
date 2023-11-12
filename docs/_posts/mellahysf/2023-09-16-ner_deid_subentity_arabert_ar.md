---
layout: model
title: Detect Subentity PHI for Deidentification (AraBERT, Arabic)
author: John Snow Labs
name: ner_deid_subentity_arabert
date: 2023-09-16
tags: [licensed, clinical, deidentification, subentity, arabic, ar, arabert, bert]
task: [Named Entity Recognition, De-identification]
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

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 17 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model uses AraBERT Arabic Embeddings.

## Predicted Entities

`PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_arabert_ar_5.1.0_3.0_1694877264289.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_subentity_arabert_ar_5.1.0_3.0_1694877264289.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_base_arabert","ar") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity_arabert", "ar", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
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

val sentenceDetector = SentenceDetector
        .pretrained("sentence_detector_dl", "xx")
        .setInputCols(Array("document"))
        .setOutputCol("sentence")

val tokenizer = new Tokenizer()
        .setInputCols(Array("sentence"))
        .setOutputCol("token")

val embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_base_arabert", "ar")
        .setInputCols(Array("document", "token"))
        .setOutputCol("embeddings")
        .setCaseSensitive(true) 

val clinicalNer = MedicalNerModel.pretrained("ner_deid_subentity_arabert", "ar", "clinical/models")
        .setInputCols(Array("sentence", "token", "embeddings"))
        .setOutputCol("ner")

val nerConverter = new NerConverter()
        .setInputCols(Array("sentence", "token", "ner"))
        .setOutputCol("ner_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        clinicalNer,
        nerConverter
        ))

val text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''

val data: DataFrame = spark.createDataFrame(Seq((text,))).toDF("text")

val results = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------+------------------------+
|chunk                          |ner_label|
+----------------------------+-----------------------+
|الدكتور محمد المريض   |DOCTOR   |
|55 سنة                      |AGE      |
|15/05/2000          |DATE     |
|مستشفى مدينة الرباط     |HOSPITAL |
|abcd@gmail.com  |EMAIL    |
+----------------------------+------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_subentity_arabert|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|16.3 MB|

## Benchmarking

```bash
label         precision  recall    f1
AGE           97.86      97.24     97.56
CITY          90.68      85.26     87.89
COUNTRY       87.58      85.45     86.50
DATE          97.75      97.75     97.75
DOCTOR        88.04      91.04     89.52
EMAIL         100.0      99.11     99.55
HOSPITAL      79.56      82.11     80.81
IDNUM         92.86      100.0     96.30
MEDICALRECORD 83.33      88.24     85.71
ORGANIZATION  63.41      57.78     60.47
PATIENT       90.0       68.61     77.86
PHONE         90.24      92.5      91.36
PROFESSION    85.90      80.0      82.84
SEX           97.76      81.6      88.95
STREET        96.88      100.0     98.41
USERNAME      100.0      100.0     100.0
ZIP           91.95      100.0     95.81
Macro         -          -         91.78
Micro         -          -         94.19
```
