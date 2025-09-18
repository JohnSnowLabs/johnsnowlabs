---
layout: model
title: Adverse Drug Events Binary Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_ade_augmented_onnx
date: 2025-09-12
tags: [clinical, licensed, public_health, ade, classifier, sequence_classification, en, onnx]
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

This model is a [BioBERT-based] (https://github.com/dmis-lab/biobert) classifier that can classify tweets reporting ADEs (Adverse Drug Events).

## Predicted Entities

`ADE`, `noADE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_ade_augmented_onnx_en_6.1.1_3.0_1757681251743.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_ade_augmented_onnx_en_6.1.1_3.0_1757681251743.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade_augmented_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame(["So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st",
                              "Religare Capital Ranbaxy has been accepting approval for Diovan since 2012"], StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_ade_augmented_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st",
                                 "Religare Capital Ranbaxy has been accepting approval for Diovan since 2012"], StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade_augmented_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st",
                     "Religare Capital Ranbaxy has been accepting approval for Diovan since 2012")).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------------------------------------------------------------------------------------------------------+-------+
|text                                                                                                                   |result |
+-----------------------------------------------------------------------------------------------------------------------+-------+
|So glad I am off effexor, so sad it ruined my teeth. tip Please be carefull taking antideppresiva and read about it 1st|[ADE]  |
|Religare Capital Ranbaxy has been accepting approval for Diovan since 2012                                             |[noADE]|
+-----------------------------------------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_ade_augmented_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|