---
layout: model
title: Symptom Text Matcher
author: John Snow Labs
name: symptom_matcher
date: 2025-11-29
tags: [matcher, symptom, en, licensed, clinical]
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

This is a TextMatcher model that can identify symptom entities in clinical text. It recognizes various symptoms including headache, nausea, vomiting, fever, fatigue, chest pain, shortness of breath, dizziness, abdominal pain, cough, and many more clinical symptoms.

## Predicted Entities

`SYMPTOM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_en_6.2.0_3.2_1764375272180.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/symptom_matcher_en_6.2.0_3.2_1764375272180.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

text = """Patient presents with severe headache, nausea, and vomiting for the past 3 days. She also reports photophobia and neck stiffness. On examination, patient appears fatigued with mild fever."""

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

symptom_matcher = medical.TextMatcherModel.pretrained("symptom_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_symptom")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    symptom_matcher
])

text = """Patient presents with severe headache, nausea, and vomiting for the past 3 days. She also reports photophobia and neck stiffness. On examination, patient appears fatigued with mild fever."""

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

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    symptomMatcher
))

val data = Seq("""Patient presents with severe headache, nausea, and vomiting for the past 3 days. She also reports photophobia and neck stiffness. On examination, patient appears fatigued with mild fever.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------------+-----+---+-------+
|chunk           |begin|end|label  |
+----------------+-----+---+-------+
|headache        |28   |35 |SYMPTOM|
|nausea          |38   |43 |SYMPTOM|
|vomiting        |50   |57 |SYMPTOM|
|photophobia     |96   |106|SYMPTOM|
|neck stiffness  |112  |125|SYMPTOM|
|fatigued        |161  |168|SYMPTOM|
|fever           |180  |184|SYMPTOM|
+----------------+-----+---+-------+

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
|Size:|960.1 KB|
|Case sensitive:|false|