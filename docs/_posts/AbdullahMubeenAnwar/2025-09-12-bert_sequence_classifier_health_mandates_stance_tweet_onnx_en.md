---
layout: model
title: Stance About Health Mandates Related to Covid-19 Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_health_mandates_stance_tweet_onnx
date: 2025-09-12
tags: [en, clinical, licensed, public_health, classifier, sequence_classification, covid_19, tweet, stance, mandate, onnx]
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

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can classify stance about health mandates related to Covid-19 from tweets. 
This model is intended for direct use as a classification model and the target classes are: Support, Disapproval, Not stated.

## Predicted Entities

`Support`, `Disapproval`, `Not stated`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_health_mandates_stance_tweet_onnx_en_6.1.1_3.0_1757683930719.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_health_mandates_stance_tweet_onnx_en_6.1.1_3.0_1757683930719.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_health_mandates_stance_tweet_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame(["""It's too dangerous to hold the RNC, but let's send students and teachers back to school.""",
"""So is the flu and pneumonia what are their s stop the Media Manipulation covid has treatments Youre Speaker Pelosi nephew so stop the agenda LIES.""",
"""Just a quick update to my U.S. followers, I'll be making a stop in all 50 states this spring!  No tickets needed, just don't wash your hands, cough on each other.""",
"""Go to a restaurant no mask Do a food shop wear a mask INCONSISTENT No Masks No Masks.""",
"""But if schools close who is gonna occupy those graves Cause politiciansprotected smokers protected drunkardsprotected school kids amp teachers""",
"""New title Maskhole I think Im going to use this very soon coronavirus."""], StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_health_mandates_stance_tweet_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])
data = spark.createDataFrame(["""It's too dangerous to hold the RNC, but let's send students and teachers back to school.""",
"""So is the flu and pneumonia what are their s stop the Media Manipulation covid has treatments Youre Speaker Pelosi nephew so stop the agenda LIES.""",
"""Just a quick update to my U.S. followers, I'll be making a stop in all 50 states this spring!  No tickets needed, just don't wash your hands, cough on each other.""",
"""Go to a restaurant no mask Do a food shop wear a mask INCONSISTENT No Masks No Masks.""",
"""But if schools close who is gonna occupy those graves Cause politiciansprotected smokers protected drunkardsprotected school kids amp teachers""",
"""New title Maskhole I think Im going to use this very soon coronavirus."""], StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_health_mandates_stance_tweet_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(
  "It's too dangerous to hold the RNC, but let's send students and teachers back to school.",
  "So is the flu and pneumonia what are their s stop the Media Manipulation covid has treatments Youre Speaker Pelosi nephew so stop the agenda LIES.",
  "Just a quick update to my U.S. followers, I'll be making a stop in all 50 states this spring!  No tickets needed, just don't wash your hands, cough on each other.",
  "Go to a restaurant no mask Do a food shop wear a mask INCONSISTENT No Masks No Masks.",
  "But if schools close who is gonna occupy those graves Cause politiciansprotected smokers protected drunkardsprotected school kids amp teachers",
  "New title Maskhole I think Im going to use this very soon coronavirus."
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|text                                                                                                                                                              |result       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|It's too dangerous to hold the RNC, but let's send students and teachers back to school.                                                                          |[Support]    |
|So is the flu and pneumonia what are their s stop the Media Manipulation covid has treatments Youre Speaker Pelosi nephew so stop the agenda LIES.                |[Disapproval]|
|Just a quick update to my U.S. followers, I'll be making a stop in all 50 states this spring!  No tickets needed, just don't wash your hands, cough on each other.|[Not stated] |
|Go to a restaurant no mask Do a food shop wear a mask INCONSISTENT No Masks No Masks.                                                                             |[Disapproval]|
|But if schools close who is gonna occupy those graves Cause politiciansprotected smokers protected drunkardsprotected school kids amp teachers                    |[Support]    |
|New title Maskhole I think Im going to use this very soon coronavirus.                                                                                            |[Not stated] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_health_mandates_stance_tweet_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|