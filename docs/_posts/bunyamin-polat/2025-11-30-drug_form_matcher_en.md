---
layout: model
title: Drug Form Text Matcher
author: John Snow Labs
name: drug_form_matcher
date: 2025-11-30
tags: [matcher, drug_form, en, licensed, clinical, text_matcher]
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

This is a TextMatcher model that can identify drug form entities in clinical text. It recognizes various pharmaceutical forms including tablet, capsule, injection, cream, solution, spray, and many more drug delivery forms commonly found in medication prescriptions and clinical documentation.

## Predicted Entities

`DRUG_FORM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_en_6.2.0_3.2_1764465316039.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_form_matcher_en_6.2.0_3.2_1764465316039.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

drug_form_matcher = TextMatcherInternalModel.pretrained("drug_form_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_form")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_form_matcher
])

text = """The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

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

drug_form_matcher = medical.TextMatcherModel.pretrained("drug_form_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("matched_drug_form")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_form_matcher
])

text = """The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN."""

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

val drugFormMatcher = TextMatcherInternalModel.pretrained("drug_form_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("matched_drug_form")
    .setMergeOverlapping(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    drugFormMatcher
))

val data = Seq("""The patient was started on Metformin 500mg tablet twice daily with meals. For pain, Oxycodone 5mg capsule every 6 hours PRN was prescribed. Insulin glargine injection 20 units subcutaneously at bedtime. Apply Hydrocortisone 1% cream to affected areas twice daily. Fentanyl 25mcg/hr transdermal patch applied every 72 hours. Albuterol solution via nebulizer every 4 hours PRN.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------+-----+---+---------+
|chunk            |begin|end|label    |
+-----------------+-----+---+---------+
|tablet           |44   |49 |DRUG_FORM|
|capsule          |97   |103|DRUG_FORM|
|injection        |149  |157|DRUG_FORM|
|cream            |220  |224|DRUG_FORM|
|transdermal patch|270  |286|DRUG_FORM|
|solution         |330  |337|DRUG_FORM|
|nebulizer        |343  |351|DRUG_FORM|
+-----------------+-----+---+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_form_matcher|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[matched_drug_form]|
|Language:|en|
|Size:|934.3 KB|
|Case sensitive:|false|
