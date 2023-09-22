---
layout: model
title: Detect Generic PHI for Deidentification (AraBERT, Arabic)
author: John Snow Labs
name: ner_deid_generic_arabert
date: 2023-09-16
tags: [licensed, ner, clinical, deidentification, generic, arabic, ar, arabert, bert]
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

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 8 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model uses AraBERT Arabic Embeddings.

## Predicted Entities

`CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/DEID_PHI_TEXT_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_arabert_ar_5.1.0_3.0_1694876080801.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_arabert_ar_5.1.0_3.0_1694876080801.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_arabert", "ar", "clinical/models")\
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

val embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_base_arabert", "ar")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(true) 

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic_arabert", "ar", "clinical/models")
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
+---------------------------+--------------------------+
|chunk                         |ner_label|
+---------------------------+--------------------------+
|55 سنة                                  |AGE      |
|15/05/2000                      |DATE     |
|0610948234                     |ID          |
|abcd@gmail.com            |CONTACT  |
+---------------------------+---------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_arabert|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|16.3 MB|

## Benchmarking

```bash
label         precision recall   f1
AGE           95.90     98.70    97.28
CONTACT       99.31     94.74    96.97
DATE          97.62     97.08    97.35
ID            73.17     100.0    84.51
LOCATION      89.93     83.80    86.76
NAME          86.45     89.29    87.84
PROFESSION    88.30     74.33    80.71
SEX           97.14     81.60    88.70
Macro         -          -       94.73
Micro         -          -       95.06
```
