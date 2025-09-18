---
layout: model
title: COVID-19 Sentiment Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_covid_sentiment_onnx
date: 2025-09-12
tags: [public_health, covid19_sentiment, en, licenced, licensed, onnx]
task: Sentiment Analysis
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

This model is a [BioBERT](https://nlp.johnsnowlabs.com/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) based sentiment analysis model that can extract information from COVID-19 pandemic-related tweets. The model predicts whether a tweet contains positive, negative, or neutral sentiments about COVID-19 pandemic.

## Predicted Entities

`neutral`, `positive`, `negative`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_covid_sentiment_onnx_en_6.1.1_3.0_1757683384209.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_covid_sentiment_onnx_en_6.1.1_3.0_1757683384209.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_covid_sentiment_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame([
    ["British Department of Health confirms first two cases of in UK"],
    ["so my trip to visit my australian exchange student just got canceled bc of coronavirus. im heartbroken :("], 
    [ "I wish everyone to be safe at home and stop pandemic"]]
).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_covid_sentiment_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([
    ["British Department of Health confirms first two cases of in UK"],
    ["so my trip to visit my australian exchange student just got canceled bc of coronavirus. im heartbroken :("], 
    [ "I wish everyone to be safe at home and stop pandemic"]]
).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_covid_sentiment_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq( "British Department of Health confirms first two cases of in UK",
  "so my trip to visit my australian exchange student just got canceled bc of coronavirus. im heartbroken ",
  "I wish everyone to be safe at home and stop pandemic"
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------------------------+----------+
|text                                                                                                     |result    |
+---------------------------------------------------------------------------------------------------------+----------+
|British Department of Health confirms first two cases of in UK                                           |[neutral] |
|so my trip to visit my australian exchange student just got canceled bc of coronavirus. im heartbroken :(|[negative]|
|I wish everyone to be safe at home and stop pandemic                                                     |[positive]|
+---------------------------------------------------------------------------------------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_covid_sentiment_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|