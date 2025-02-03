---
layout: model
title: Detect Assertion Status (assertion_classifier_base)
author: John Snow Labs
name: AssertionBertForSequence_i2b2_3label
date: 2025-02-03
tags: [licensed, clinical, en, assertion, classification, tensorflow]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/AssertionBertForSequence_i2b2_3label_en_5.5.2_3.0_1738591058660.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/AssertionBertForSequence_i2b2_3label_en_5.5.2_3.0_1738591058660.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

# Test classifier in Spark NLP pipeline
document_assembler = DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer()     .setInputCols(["document"]) \
    .setOutputCol("token")

# Load newly trained classifier
assertion_classifier = MedicalBertForSequenceClassification\
    .pretrained("AssertionBertForSequence_i2b2_3label", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    assertion_classifier
])

# Generating example
data = spark.createDataFrame(["he was begun on physical therapy but remained agitated .",
                              "there were no meatal blood ."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)

# Checking results
result.select("text", "prediction.result").show(truncate=False)


```

{:.jsl-block}
```python

# Test classifier in Spark NLP pipeline
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

# Load newly trained classifier
assertion_classifier = medical.BertForSequenceClassification\
    .pretrained("AssertionBertForSequence_i2b2_3label", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    assertion_classifier
])

# Generating example
data = spark.createDataFrame(["he was begun on physical therapy but remained agitated .",
                              "there were no meatal blood ."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)

```
```scala

val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("token")

val assertion_classifier = MedicalBertForSequenceClassification
    .pretrained("AssertionBertForSequence_i2b2_3label", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, assertion_classifier))


val data = Seq(Array("he was begun on physical therapy but remained agitated .",
                    "there were no meatal blood .")).toDF("text")

val result = pipeline.fit(data).transform(data)


```
</div>

## Results

```bash

+----------------------------------------------------------------+-------+
|text                                                            |result |
+----------------------------------------------------------------+-------+
|he was begun on physical therapy but remained agitated  .       |present|
|there were no meatal blood .                                    |absent |
+----------------------------------------------------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|AssertionBertForSequence_i2b2_3label|
|Compatibility:|Healthcare NLP 5.5.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[assertion_class]|
|Language:|en|
|Size:|406.3 MB|
|Case sensitive:|false|
|Max sentence length:|512|