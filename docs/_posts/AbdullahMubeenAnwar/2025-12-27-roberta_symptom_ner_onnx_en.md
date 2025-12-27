---
layout: model
title: Symptom Named Entity Recognition (Base, ONNX)
author: John Snow Labs
name: roberta_symptom_ner_onnx
date: 2025-12-27
tags: [roberta, ner, medical, clinical, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: RoBertaForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

RoBERTa-based token classification model for extracting symptom mentions from text using BIO labels (B-SYMPTOM, I-SYMPTOM, O). Intended for dense symptom recognition in clinical and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/roberta_symptom_ner_onnx_en_6.2.0_3.4_1766826571184.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/roberta_symptom_ner_onnx_en_6.2.0_3.4_1766826571184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = RoBertaForTokenClassification \
    .pretrained("roberta_symptom_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient reported fever, chills, night sweats, fatigue, malaise, weight loss, headache, dizziness, blurred vision, chest pain, palpitations, shortness of breath, cough, wheezing, nausea, vomiting, abdominal pain, diarrhea, constipation, dysphagia, and loss of appetite."],
    ["During evaluation the patient complained of severe back pain, joint stiffness, muscle weakness, numbness, tingling, tremors, gait instability, confusion, memory loss, anxiety, depression, insomnia, irritability, mood swings, difficulty concentrating, and episodes of syncope."],
    ["Postoperatively the patient experienced incisional pain, swelling, redness, warmth, bruising, bleeding, wound drainage, fever spikes, chills, shortness of breath, rapid heartbeat, lightheadedness, nausea, vomiting, bloating, constipation, urinary retention, dysuria, and generalized weakness."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = medical.RoBertaForTokenClassification \
    .pretrained("roberta_symptom_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = nlp.NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient reported fever, chills, night sweats, fatigue, malaise, weight loss, headache, dizziness, blurred vision, chest pain, palpitations, shortness of breath, cough, wheezing, nausea, vomiting, abdominal pain, diarrhea, constipation, dysphagia, and loss of appetite."],
    ["During evaluation the patient complained of severe back pain, joint stiffness, muscle weakness, numbness, tingling, tremors, gait instability, confusion, memory loss, anxiety, depression, insomnia, irritability, mood swings, difficulty concentrating, and episodes of syncope."],
    ["Postoperatively the patient experienced incisional pain, swelling, redness, warmth, bruising, bleeding, wound drainage, fever spikes, chills, shortness of breath, rapid heartbeat, lightheadedness, nausea, vomiting, bloating, constipation, urinary retention, dysuria, and generalized weakness."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = RoBertaForTokenClassification
  .pretrained("roberta_symptom_ner_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("ner")

val converter = new NerConverter()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  tokenClassifier,
  converter
))

val data = Seq(
  "Patient reported fever, chills, night sweats, fatigue, malaise, weight loss, headache, dizziness, blurred vision, chest pain, palpitations, shortness of breath, cough, wheezing, nausea, vomiting, abdominal pain, diarrhea, constipation, dysphagia, and loss of appetite.",
  "During evaluation the patient complained of severe back pain, joint stiffness, muscle weakness, numbness, tingling, tremors, gait instability, confusion, memory loss, anxiety, depression, insomnia, irritability, mood swings, difficulty concentrating, and episodes of syncope.",
  "Postoperatively the patient experienced incisional pain, swelling, redness, warmth, bruising, bleeding, wound drainage, fever spikes, chills, shortness of breath, rapid heartbeat, lightheadedness, nausea, vomiting, bloating, constipation, urinary retention, dysuria, and generalized weakness."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+---------+-------+
|text     |entity |
+---------+-------+
|chills   |SYMPTOM|
|night    |SYMPTOM|
|sweats   |SYMPTOM|
|fatigue  |SYMPTOM|
|malaise  |SYMPTOM|
|abdominal|SYMPTOM|
|back     |SYMPTOM|
|joint    |SYMPTOM|
|muscle   |SYMPTOM|
|numbness |SYMPTOM|
|tingling |SYMPTOM|
|dysuria  |SYMPTOM|
+---------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_symptom_ner_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|466.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|