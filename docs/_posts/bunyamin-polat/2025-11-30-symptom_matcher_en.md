---
layout: model
title: Symptom Text Matcher
author: John Snow Labs
name: symptom_matcher
date: 2025-11-30
tags: [matcher, symptom, en, licensed, clinical, text_matcher]
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

This is a TextMatcher model that can identify symptom entities in clinical text. It recognizes a comprehensive list of clinical symptoms.

## Predicted Entities

`SYMPTOM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_en_6.2.0_3.2_1764465723113.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_en_6.2.0_3.2_1764465723113.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

symptom_matcher = TextMatcherInternalModel.pretrained("symptom_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_symptom")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    symptom_matcher
])

text = """The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation."""

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

symptom_matcher = medical.TextMatcherInternalModel.pretrained("symptom_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_symptom")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    symptom_matcher
])

text = """The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation."""

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

val symptomMatcher = TextMatcherInternalModel.pretrained("symptom_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_symptom")
    .setMergeOverlapping(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    symptomMatcher
))

val data = Seq("""The patient presents with severe headache and nausea for 3 days. She reports chest pain radiating to left arm with shortness of breath. Review of systems positive for fatigue, dizziness, and palpitations. Patient also complains of abdominal pain and constipation.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------------------+-----+---+-------+
|chunk              |begin|end|label  |
+-------------------+-----+---+-------+
|headache           |35   |42 |SYMPTOM|
|nausea             |48   |53 |SYMPTOM|
|chest pain         |77   |86 |SYMPTOM|
|shortness of breath|110  |128|SYMPTOM|
|fatigue            |160  |166|SYMPTOM|
|dizziness          |169  |177|SYMPTOM|
|palpitations       |184  |195|SYMPTOM|
|abdominal pain     |225  |238|SYMPTOM|
|constipation       |244  |255|SYMPTOM|
+-------------------+-----+---+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|symptom_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_symptom]|
|Language:|en|
|Size:|969.6 KB|
|Case sensitive:|false|