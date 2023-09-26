---
layout: model
title: Detect Generic PHI for Deidentification (CamelBERT, Arabic)
author: John Snow Labs
name: ner_deid_generic_camelbert
date: 2023-09-16
tags: [licensed, ner, clinical, deidentification, generic, arabic, ar, camelbert, bert]
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

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 8 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model uses CamelBERT Arabic Embeddings.

## Predicted Entities

`CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_camelbert_ar_5.1.0_3.0_1694879591458.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_camelbert_ar_5.1.0_3.0_1694879591458.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = BertEmbeddings.pretrained("bert_embeddings_base_arabic_camel_msa", "ar") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_camelbert", "ar", "clinical/models")\
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

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_camelbert", "ar", "clinical/models")
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

val text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
 '''

val data = Seq(text).toDS.toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------+------------------+
|chunk                              |ner_label|
+----------------------------------+------------------+
|الدكتور محمد                       |NAME     |
|55 سنة                              |AGE      |
|15/05/2000                   |DATE     |
|مستشفى مدينة الرباط             |LOCATION |
|0610948234                 |LOCATION |
|abcd@gmail.com        |CONTACT  |
+----------------------------------+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_camelbert|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|16.3 MB|

## Benchmarking

```bash
label         precision   recall      f1
AGE           99.18       98.54       98.86
CONTACT       97.97       95.39       96.67
DATE          97.96       97.19       97.57
ID            78.38       96.67       86.57
LOCATION      88.80       90.74       89.76
NAME          94.62       87.86       91.11
PROFESSION    91.97       82.09       86.75
SEX           98.45       84.53       90.96
Macro         -           -           0.96
Micro         -           -           0.97
```
