---
layout: model
title: Medical Device Text Matcher
author: John Snow Labs
name: medical_device_matcher
date: 2025-11-30
tags: [matcher, medical_device, en, licensed, clinical, text_matcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.2
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a TextMatcher model that identifies medical device entities in clinical text. It recognizes devices including ventilator, defibrillator, stent, insulin pump, glucometer, nebulizer, and more.

## Predicted Entities

`MEDICAL_DEVICE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_en_6.2.0_3.2_1764466935484.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medical_device_matcher_en_6.2.0_3.2_1764466935484.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

medical_device_matcher = TextMatcherInternalModel.pretrained("medical_device_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_medical_device")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    medical_device_matcher
])

text = """The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

medical_device_matcher = medical.TextMatcherModel.pretrained("medical_device_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_medical_device")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    medical_device_matcher
])

text = """The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val medicalDeviceMatcher = TextMatcherInternalModel.pretrained("medical_device_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_medical_device")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    medicalDeviceMatcher
))

val data = Seq("""The patient was placed on a ventilator for respiratory support. A pacemaker was implanted to regulate heart rhythm. Blood glucose levels were monitored using a glucometer, and insulin was delivered via an insulin pump.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------+-----+---+--------------+
|chunk      |begin|end|label         |
+-----------+-----+---+--------------+
|ventilator |30   |39 |MEDICAL_DEVICE|
|pacemaker  |65   |73 |MEDICAL_DEVICE|
|glucometer |145  |153|MEDICAL_DEVICE|
|insulin pump|193 |203|MEDICAL_DEVICE|
+-----------+-----+---+--------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medical_device_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_medical_device]|
|Language:|en|
|Size:|947.3 KB|
|Case sensitive:|false|
