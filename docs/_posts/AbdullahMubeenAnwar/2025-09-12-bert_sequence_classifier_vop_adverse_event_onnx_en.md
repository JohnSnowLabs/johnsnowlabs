---
layout: model
title: Adverse Event Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_vop_adverse_event_onnx
date: 2025-09-12
tags: [clinical, licensed, en, text_classification, adverse_event, ade, vop, biobert, onnx]
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

This model is a BioBERT-based Adverse Event Text Classifier and it is trained for analyzing the adverse events of drugs mentioned in health documents. 

The Text Classifier model has been trained using in-house annotated health-related text that have been labeled with two different classes:

`True`: Text includes signs or symptoms that are unfavorable, unintended, and/or harmful in a patient who is administered a pharmaceutical product or medical device.

`False`: The patient did not experience something unfavorable during the course of treatment.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_adverse_event_onnx_en_6.1.1_3.0_1757691542179.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_adverse_event_onnx_en_6.1.1_3.0_1757691542179.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_adverse_event_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame([
["I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel very weird. I want to reduce my blood pressure naturally. Can I stop this medication? I only took it for 5 days. I was reading here, that a lot of people has been losing weight and exercise and now they have a normal blood pressure. Please let me know, what I can do. The sides effects are horrible"],
["I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pain from the liver area (under right ribs).It comes and goes. Could this be a sign of liver damage?When i get this pain i am usually in the pub drinking.If i press the area under my right rib cage about half way across i can feel pain. Is that pain in the Liver?"]
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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_vop_adverse_event_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([
["I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel very weird. I want to reduce my blood pressure naturally. Can I stop this medication? I only took it for 5 days. I was reading here, that a lot of people has been losing weight and exercise and now they have a normal blood pressure. Please let me know, what I can do. The sides effects are horrible"],
["I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pain from the liver area (under right ribs).It comes and goes. Could this be a sign of liver damage?When i get this pain i am usually in the pub drinking.If i press the area under my right rib cage about half way across i can feel pain. Is that pain in the Liver?"]
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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_adverse_event_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array(
"I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel very weird. I want to reduce my blood pressure naturally. Can I stop this medication? I only took it for 5 days. I was reading here, that a lot of people has been losing weight and exercise and now they have a normal blood pressure. Please let me know, what I can do. The sides effects are horrible",
"I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pain from the liver area (under right ribs).It comes and goes. Could this be a sign of liver damage? When i get this pain i am usually in the pub drinking.If i press the area under my right rib cage about half way across i can feel pain. Is that pain in the Liver?"
)).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|                                                                                                                                                  text| result|
+------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel...|  True |
|I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pa...| False |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_adverse_event_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|