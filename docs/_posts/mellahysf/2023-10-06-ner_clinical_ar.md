---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Arabic
author: John Snow Labs
name: ner_clinical
date: 2023-10-06
tags: [licensed, clinical, ner, ar]
task: Named Entity Recognition
language: ar
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Arabic. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_ar_5.1.1_3.0_1696604805992.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_ar_5.1.1_3.0_1696604805992.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")\
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "ar", "clinical/models")\
        .setInputCols(["sentence","token","embeddings"])\
        .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(['sentence', 'token', 'ner'])\
    .setOutputCol('ner_chunk')

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text =  """تاريخ الزيارة: 25 سبتمبر 2023 - المريضة: فاطمة علي - العمر: 48 سنة - الجنس: أنثى - المشاكل: 1.  مشكل ارتفاع في مستويات في الدم 2. ارتفاع مستوى الكوليستيرول في الدم 3. اضطراب في وظائف الغدة الدرقية - الفحوصات: 1. قياس مستوى السكر في الدم 2. تحليل مستوى الكوليستيرول في الدم 3. اختبار وظائف الغدة الدرقية - العلاجات: 1. وصف دواء لمراقبة وتنظيم مستوى السكر في الدم (ميتفورمين 500 ملغ يوميا) 2. وصف دواء لتخفيض مستوى الكوليستيرول (ستاتين 20 ملغ يوميا) 3. وصف العلاج اللازم لتحسين وظائف الغدة الدرقية (ليفوتيروكسين 50 ميكروغرام يوميا)، بالإضافة إلى توجيهات بشأن نمط حياة صحي تتضمن اتباع نظام غذائي مناسب وممارسة الرياضة بانتظام."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "ar", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array('sentence', 'token', 'ner'))
    .setOutputCol('ner_chunk')

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
))

sample_data = Seq("""تاريخ الزيارة: 25 سبتمبر 2023 - المريضة: فاطمة علي - العمر: 48 سنة - الجنس: أنثى - المشاكل: 1.  مشكل ارتفاع في مستويات في الدم 2. ارتفاع مستوى الكوليستيرول في الدم 3. اضطراب في وظائف الغدة الدرقية - الفحوصات: 1. قياس مستوى السكر في الدم 2. تحليل مستوى الكوليستيرول في الدم 3. اختبار وظائف الغدة الدرقية - العلاجات: 1. وصف دواء لمراقبة وتنظيم مستوى السكر في الدم (ميتفورمين 500 ملغ يوميا) 2. وصف دواء لتخفيض مستوى الكوليستيرول (ستاتين 20 ملغ يوميا) 3. وصف العلاج اللازم لتحسين وظائف الغدة الدرقية (ليفوتيروكسين 50 ميكروغرام يوميا)، بالإضافة إلى توجيهات بشأن نمط حياة صحي تتضمن اتباع نظام غذائي مناسب وممارسة الرياضة بانتظام.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+-----------------------------------------------------+-------------------+
|chunk                                                  |ner_label|
+----------------------------------------------------+-------------------+
|مشكل ارتفاع في مستويات في الدم                 |PROBLEM  |
|ارتفاع مستوى الكوليستيرول في الدم              |PROBLEM  |
|اضطراب في وظائف الغدة الدرقية                |PROBLEM  |
|قياس مستوى السكر في الدم                         |TEST     |
|تحليل مستوى الكوليستيرول في الدم               |TEST     |
|اختبار وظائف الغدة الدرقية                         |TEST     |
|ميتفورمين                                              |TREATMENT|
|ليفوتيروكسين                                          |TREATMENT|
|نظام غذائي مناسب                                   |TREATMENT|
+---------------------------------+-----------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|ar|
|Size:|2.9 MB|

## Benchmarking

```bash
               precision    recall  f1-score   support

        TEST       0.98      1.00      0.99       450
   TREATMENT       0.96      0.96      0.96       321
     PROBLEM       0.96      0.98      0.97       733

   micro avg       0.96      0.98      0.97      1504
   macro avg       0.96      0.98      0.97      1504
weighted avg       0.96      0.98      0.97      1504
```
