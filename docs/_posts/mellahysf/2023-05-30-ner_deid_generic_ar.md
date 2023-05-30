---
layout: model
title: Detect Generic PHI for Deidentification (Arabic)
author: John Snow Labs
name: ner_deid_generic
date: 2023-05-30
tags: [licensed, ner, clinical, deidentifiction, generic, arabic, ar]
task: Named Entity Recognition
language: ar
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Named Entity Recognition annotators allow for a generic model to be trained by using a Deep Learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired on a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM,CNN. 

Deidentification NER (Arabic) is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 8 entities. This NER model is trained with a combination of custom datasets, and several data augmentation mechanisms. This model  Word2Vec Arabic Clinical Embeddings.

## Predicted Entities

`CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_ar_4.4.2_3.0_1685443881012.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_ar_4.4.2_3.0_1685443881012.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner_subentity = MedicalNerModel.pretrained("ner_deid_generic", "ar", "clinical/models")\
        .setInputCols(["sentence","token","embeddings"])\
        .setOutputCol("ner")

ner_converter = NerConverterInternal()\
        .setInputCols(["sentence","token","ner"])\
        .setOutputCol("ner_chunk")

nlpPipelineGeneric = Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        clinical_ner_subentity,
        ner_converter])

text = '''
ملاحظات سريرية - مريض الربو:

التاريخ: 30 مايو 2023
اسم المريض: أحمد سليمان
العنوان: شارع السلام، مبنى رقم 555، حي الصفاء، الرياض
الرمز البريدي: 54321
البلد: المملكة العربية السعودية
اسم المستشفى: مستشفى الأمانة
اسم الطبيب: د. ريم الحمد

تفاصيل الحالة:
المريض أحمد سليمان، البالغ من العمر 30 عامًا، يعاني من مرض الربو المزمن. يشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصه بمرض الربو بناءً على تاريخه الطبي واختبارات وظائف الرئة.
 '''

data = spark.createDataFrame([[text]]).toDF("text")
results = nlpPipeline .fit(data).transform(data)

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

val embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")
.setInputCols(Array("sentence","token"))
.setOutputCol("word_embeddings")

val clinical_ner = MedicalNerModel.pretrained("ner_deid_generic", "ar", "clinical/models")
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
ملاحظات سريرية - مريض الربو:

التاريخ: 30 مايو 2023
اسم المريض: أحمد سليمان
العنوان: شارع السلام، مبنى رقم 555، حي الصفاء، الرياض
الرمز البريدي: 54321
البلد: المملكة العربية السعودية
اسم المستشفى: مستشفى الأمانة
اسم الطبيب: د. ريم الحمد

تفاصيل الحالة:
المريض أحمد سليمان، البالغ من العمر 30 عامًا، يعاني من مرض الربو المزمن. يشكو من ضيق التنفس والسعال المتكرر والشهيق الشديد. تم تشخيصه بمرض الربو بناءً على تاريخه الطبي واختبارات وظائف الرئة.
 '''

val data = Seq(text).toDS.toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------+---------------------+
|chunk          |      ner_label  |
+-----------------+---------------------+
|30 مايو             |DATE            |
|أحمد سليمان        |NAME          |
|الرياض             |LOCATION   |
|54321           |LOCATION   |
|المملكة العربية    |LOCATION   |
|السعودية           |LOCATION   |
|مستشفى الأمانة   |LOCATION   |
|ريم الحمد          |NAME           |
|أحمد                |NAME           |
+---------------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic|
|Compatibility:|Healthcare NLP 4.4.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|15.0 MB|

## References

Custom John Snow Labs datasets

Data augmentation techniques

## Benchmarking

```bash
     label     tp    fp    fn  total  precision  recall      f1
   CONTACT  146.0   0.0   6.0  152.0        1.0  0.9605  0.9799
      NAME  685.0  25.0  25.0  710.0     0.9648  0.9648  0.9648
      DATE  876.0  14.0   9.0  885.0     0.9843  0.9898   0.987
        ID   28.0   9.0   2.0   30.0     0.7568  0.9333  0.8358
       SEX  300.0   8.0  69.0  369.0      0.974   0.813  0.8863
  LOCATION  689.0  48.0  38.0  727.0     0.9349  0.9477  0.9413
PROFESSION  303.0  20.0  32.0  335.0     0.9381  0.9045   0.921
       AGE  608.0   7.0   9.0  617.0     0.9886  0.9854   0.987
     macro     -     -     -      -       -       -      0.9378
     micro     -     -     -      -       -       -      0.9572
```
