---
layout: model
title: Detect Problems, Tests and Treatments (ner_clinical) in Hebrew
author: John Snow Labs
name: ner_clinical
date: 2023-10-23
tags: [ner, clinical, licensed, he]
task: Named Entity Recognition
language: he
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Hebrew. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_he_5.1.1_3.0_1698090197863.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_he_5.1.1_3.0_1698090197863.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = BertEmbeddings.pretrained("alephbertgimmel_base_512","he") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "he", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text = """פה רגיל צוואר רגיל תרואיד תקין שדיים רגילים ללא גושים בולטים פטילות רגילות הפוכות [ב] , מתפשטות עם גירוי חזה רגיל LCTA COR תקין RRR בטן רגילה מעוברת רגליים רגילות עור רגיל צמיגים רגילים פרטים רגילים ללא גידולים פלפים רגילים ללא תסמין נמוך רגיל פרטים לבנים דקים כמות קטנה של פ 4.5 , קוה + אמין , NS + רמז , טריש - רגיל רחם רגיל 1/100/0 SROM ברור סגור נפשות רגילות ללא גידולים פלפים NT רגיל רחם רגיל גודל בשבועות תקין מעי רגיל ללא גידולים חיצוניים."""


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

val embeddings = BertEmbeddings.pretrained("alephbertgimmel_base_512","he")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "he", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
))

sample_data = Seq("""פה רגיל צוואר רגיל תרואיד תקין שדיים רגילים ללא גושים בולטים פטילות רגילות הפוכות [ב] , מתפשטות עם גירוי חזה רגיל LCTA COR תקין RRR בטן רגילה מעוברת רגליים רגילות עור רגיל צמיגים רגילים פרטים רגילים ללא גידולים פלפים רגילים ללא תסמין נמוך רגיל פרטים לבנים דקים כמות קטנה של פ 4.5 , קוה + אמין , NS + רמז , טריש - רגיל רחם רגיל 1/100/0 SROM ברור סגור נפשות רגילות ללא גידולים פלפים NT רגיל רחם רגיל גודל בשבועות תקין מעי רגיל ללא גידולים חיצוניים.""").toDS.toDF("text")


val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+--------------------+-----+---+---------+
|chunk               |begin|end|ner_label|
+--------------------+-----+---+---------+
|גושים בולטים        |48   |59 |PROBLEM  |
|הפוכות              |75   |80 |PROBLEM  |
|מתפשטות עם גירוי חזה|88   |107|TREATMENT|
|כמות קטנה של פ      |261  |274|TEST     |
|קוה                 |282  |284|TEST     |
|NS                  |295  |296|TEST     |
|טריש                |306  |309|TEST     |
|SROM                |335  |338|PROBLEM  |
+--------------------+-----+---+---------+
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
|Language:|he|
|Size:|3.4 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
     PROBLEM       0.80      0.78      0.79       607
   TREATMENT       0.80      0.64      0.71       280
        TEST       0.85      0.85      0.85       354
   micro-avg       0.81      0.77      0.79      1241
   macro-avg       0.82      0.75      0.78      1241
weighted-avg       0.81      0.77      0.79      1241
```