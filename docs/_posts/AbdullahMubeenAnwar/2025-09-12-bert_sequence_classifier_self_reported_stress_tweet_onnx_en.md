---
layout: model
title: Self Reported Stress Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_self_reported_stress_tweet_onnx
date: 2025-09-12
tags: [en, licenced, clinical, public_health, sequence_classification, classifier, stress, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can identify stress in social media (Twitter) posts in the self-disclosure category. The model finds whether a person claims he/she is stressed or not.

## Predicted Entities

`not-stressed`, `stressed`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_stress_tweet_onnx_en_6.1.1_3.0_1757690850280.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_stress_tweet_onnx_en_6.1.1_3.0_1757690850280.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_stress_tweet_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame([["Do you feel stressed?"], 
                              ["I'm so stressed!"],
                              ["Depression and anxiety will probably end up killing me – I feel so stressed all the time and just feel awful."], 
                              ["Do you enjoy living constantly in this self-inflicted stress?"]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_stress_tweet_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([["Do you feel stressed?"], 
                              ["I'm so stressed!"],
                              ["Depression and anxiety will probably end up killing me – I feel so stressed all the time and just feel awful."], 
                              ["Do you enjoy living constantly in this self-inflicted stress?"]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols(Array("document")) 
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_stress_tweet_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(
  "Do you feel stressed!",
  "I'm so stressed!",
  "Depression and anxiety will probably end up killing me – I feel so stressed all the time and just feel awful.",
  "Do you enjoy living constantly in this self-inflicted stress?"
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-------------------------------------------------------------------------------------------------------------+--------------+
|text                                                                                                         |result        |
+-------------------------------------------------------------------------------------------------------------+--------------+
|Do you feel stressed?                                                                                        |[not-stressed]|
|I'm so stressed!                                                                                             |[stressed]    |
|Depression and anxiety will probably end up killing me – I feel so stressed all the time and just feel awful.|[stressed]    |
|Do you enjoy living constantly in this self-inflicted stress?                                                |[not-stressed]|
+-------------------------------------------------------------------------------------------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_self_reported_stress_tweet_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|