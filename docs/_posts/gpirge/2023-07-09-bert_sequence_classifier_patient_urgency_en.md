---
layout: model
title: Patient Urgency Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_patient_urgency
date: 2023-07-09
tags: [urgency, emergency, licensed, en, text_classification, clinical, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Patient Urgency Text Classifier is for analyzing the emergency level of medical situations that require immediate assistance from the medical organizations.

The Text Classifier model has been trained on a collection of emergency calls that have been labeled with three different classes:

High: Requires immediate intervention, life-threatening or potentially life-threatening cases,

Medium: Requires intervention, urgent, not life-threatening cases.

Low: Non-urgent, needs treatment when time permits.

## Predicted Entities

`High`, `Medium`, `Low`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_urgency_en_4.4.4_3.0_1688867233593.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_urgency_en_4.4.4_3.0_1688867233593.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_patient_urgency", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier])

data = spark.createDataFrame([["""I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it."""], 
 ["""My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move."""],
 ["""My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated."""],
 ]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler =new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = new MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_patient_urgency", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it.", "My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move.", "My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated.")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+--------+
|                                                                                                text|  result|
+----------------------------------------------------------------------------------------------------+--------+
|I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s...|  [High]|
|My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and c...|[Medium]|
|My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke...|   [Low]|
+----------------------------------------------------------------------------------------------------+--------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_patient_urgency|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In-house annotated health-related text.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        High       0.93      0.90      0.91       152
         Low       0.89      0.76      0.82        54
      Medium       0.65      0.78      0.71        63
    accuracy       -         -         0.84       269
   macro avg       0.82      0.81      0.81       269
weighted avg       0.85      0.84      0.85       269
```