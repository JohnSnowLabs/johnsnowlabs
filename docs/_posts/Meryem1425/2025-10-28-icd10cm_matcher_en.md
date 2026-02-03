---
layout: model
title: ICD10CM Text Matcher
author: John Snow Labs
name: icd10cm_matcher
date: 2025-10-28
tags: [licensed, en, clinical, icd10cm, matcher, textmatcher]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
annotator: TextMatcherInternalModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts icd10cm entities in clinical notes using rule-based TextMatcherInternal annotator.

## Predicted Entities

`ICD10_ENTITY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_matcher_en_6.1.1_3.0_1761674746255.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_matcher_en_6.1.1_3.0_1761674746255.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
 documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

text_matcher = TextMatcherInternalModel.pretrained("icd10cm_matcher","en","clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("icd10cm")\
    .setMergeOverlapping(True)

mathcer_pipeline = Pipeline().setStages([
    documentAssembler,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

result = mathcer_pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

text_matcher = medical.TextMatcherInternalModel.pretrained("icd10cm_matcher","en","clinical/models") \
    .setInputCols(["document", "token"])\
    .setOutputCol("icd10cm")\
    .setMergeOverlapping(True)

mathcer_pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    tokenizer,
    text_matcher])

data = spark.createDataFrame([["""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""]]).toDF("text")

result = mathcer_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val text_matcher = TextMatcherInternalModel.pretrained("icd10cm_matcher","en","clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("icd10cm")
    .setMergeOverlapping(true)

val mathcer_pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    text_matcher))

val data = Seq("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection.""").toDF("text")

val result = mathcer_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------+-----+---+------------+
|chunk                        |begin|end|ner_label   |
+-----------------------------+-----+---+------------+
|gestational diabetes mellitus|39   |67 |ICD10_ENTITY|
|polyuria                     |261  |268|ICD10_ENTITY|
|polydipsia                   |271  |280|ICD10_ENTITY|
|vomiting                     |302  |309|ICD10_ENTITY|
+-----------------------------+-----+---+------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_matcher|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[entity_text]|
|Language:|en|
|Size:|9.8 MB|
|Case sensitive:|false|
