---
layout: model
title: Self Treatment Changes Classifier in Tweets (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx
date: 2025-09-12
tags: [en, clinical, licensed, public_health, classifier, sequence_classification, treatment_changes, sentiment, treatment, onnx]
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

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can classify patients non-adherent to their treatments and their reasons on Twitter.

## Predicted Entities

`negative`, `positive`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx_en_6.1.1_3.0_1757691317212.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx_en_6.1.1_3.0_1757691317212.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame(["I love when they say things like this. I took that ambien instead of my thyroid pill.",
                              "I am a 30 year old man who is not overweight but is still on the verge of needing a Lipitor prescription."], StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["I love when they say things like this. I took that ambien instead of my thyroid pill.",
                              "I am a 30 year old man who is not overweight but is still on the verge of needing a Lipitor prescription."], StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("I love when they say things like this. I took that ambien instead of my thyroid pill.",
                      "I am a 30 year old man who is not overweight but is still on the verge of needing a Lipitor prescription.")).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------------------------+----------+
|text                                                                                                     |result    |
+---------------------------------------------------------------------------------------------------------+----------+
|I love when they say things like this. I took that ambien instead of my thyroid pill.                    |[positive]|
|I am a 30 year old man who is not overweight but is still on the verge of needing a Lipitor prescription.|[negative]|
+---------------------------------------------------------------------------------------------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_treatment_changes_sentiment_tweet_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|