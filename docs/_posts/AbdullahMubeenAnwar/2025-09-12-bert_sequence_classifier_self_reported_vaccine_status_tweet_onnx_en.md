---
layout: model
title: Classification of Self Reported Vaccine Status (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx
date: 2025-09-12
tags: [bert, licensed, en, clinical, classifier, sequence_classification, public_health, vaccine, tweet, onnx]
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

Classification of tweets indicating self-reported COVID-19 vaccination status. This model involves the identification of self-reported COVID-19 vaccination status in English tweets.

## Predicted Entities

`Vaccine_chatter`, `Self_reports`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx_en_6.1.1_3.0_1757691113347.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx_en_6.1.1_3.0_1757691113347.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame(["I came to a point finally and i've vaccinated, didnt feel pain.Suggest everyone",
                              "If Pfizer believes we need a booster shot, we need it. Who knows their product better? Following the guidance of @CDCgov is how I wound up w/ Covid-19 and having to shut down my K-2 classroom for an entire week. I will do whatever it takes to protect my students, friends, family."], StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])
example = spark.createDataFrame(["I came to a point finally and i've vaccinated, didnt feel pain.Suggest everyone",
                              "If Pfizer believes we need a booster shot, we need it. Who knows their product better? Following the guidance of @CDCgov is how I wound up w/ Covid-19 and having to shut down my K-2 classroom for an entire week. I will do whatever it takes to protect my students, friends, family."], StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val example = Seq(Array("I came to a point finally and i've vaccinated, didnt feel pain.Suggest everyone",
                        "If Pfizer believes we need a booster shot, we need it. Who knows their product better? Following the guidance of @CDCgov is how I wound up w/ Covid-19 and having to shut down my K-2 classroom for an entire week. I will do whatever it takes to protect my students, friends, family.")).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
|text                                                                                                                                                                                                                                                                                    |result           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
|I came to a point finally and i've vaccinated, didnt feel pain. Suggest everyone                                                                                                                                                                                                        |[Self_reports]   |
|If Pfizer believes we need a booster shot, we need it. Who knows their product better? Following the guidance of @CDCgov is how I wound up w/ Covid-19 and having to shut down my K-2 classroom for an entire week. I will do whatever it takes to protect my students, friends, family.|[Vaccine_chatter]|
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_self_reported_vaccine_status_tweet_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|