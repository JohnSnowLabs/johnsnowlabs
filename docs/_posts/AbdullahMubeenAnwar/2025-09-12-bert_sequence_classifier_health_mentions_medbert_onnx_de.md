---
layout: model
title: German Public Health Mention Sequence Classifier (German-MedBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_health_mentions_medbert_onnx
date: 2025-09-12
tags: [public_health, de, licensed, sequence_classification, health_mention, onnx]
task: Text Classification
language: de
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

This model is a [German-MedBERT](https://opus4.kobv.de/opus4-rhein-waal/frontdoor/index/index/searchtype/collection/id/16225/start/0/rows/10/doctypefq/masterthesis/docId/740) based sequence classification model that can classify public health mentions in German social media text.

## Predicted Entities

`non-health`, `health-related`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_health_mentions_medbert_onnx_de_6.1.1_3.0_1757683983274.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_health_mentions_medbert_onnx_de_6.1.1_3.0_1757683983274.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_health_mentions_medbert_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame([
      ["Diabetes habe ich schon seit meiner Kindheit, seit der Pubertätch nehme Insulin."],
      ["Die Hochzeitszeitung ist zum Glück sehr schön geworden. Das Brautpaar gat sich gefreut."]
    ]).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_health_mentions_medbert_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([
      ["Diabetes habe ich schon seit meiner Kindheit, seit der Pubertätch nehme Insulin."],
      ["Die Hochzeitszeitung ist zum Glück sehr schön geworden. Das Brautpaar gat sich gefreut."]
    ]).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_health_mentions_medbert_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("Diabetes habe ich schon seit meiner Kindheit, seit der Pubertätch nehme Insulin.",
                     "Die Hochzeitszeitung ist zum Glück sehr schön geworden. Das Brautpaar gat sich gefreut.")).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------+----------------+
|text                                                                                   |result          |
+---------------------------------------------------------------------------------------+----------------+
|Diabetes habe ich schon seit meiner Kindheit, seit der Pubertätch nehme Insulin.       |[health-related]|
|Die Hochzeitszeitung ist zum Glück sehr schön geworden. Das Brautpaar gat sich gefreut.|[non-health]    |
+---------------------------------------------------------------------------------------+----------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_health_mentions_medbert_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|de|
|Size:|440.8 MB|
|Case sensitive:|true|