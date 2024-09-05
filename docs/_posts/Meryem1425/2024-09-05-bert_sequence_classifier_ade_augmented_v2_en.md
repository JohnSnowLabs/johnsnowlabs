---
layout: model
title: Adverse Drug Events Binary Classifier
author: John Snow Labs
name: bert_sequence_classifier_ade_augmented_v2
date: 2024-09-05
tags: [clinical, licensed, en, text_classification, ade, classifier, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Classify texts/sentences in two categories:


- `True` : The sentence is talking about a possible ADE.


- `False` : The sentence doesn’t have any information about an ADE.


This model is a [BioBERT-based](https://github.com/dmis-lab/biobert) classifier.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_ADE/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/08.3.MedicalBertForSequenceClassification_in_SparkNLP.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_ade_augmented_v2_en_5.4.1_3.0_1725544845106.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_ade_augmented_v2_en_5.4.1_3.0_1725544845106.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade_augmented_v2", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = Pipeline().setStages([document_assembler, tokenizer, sequenceClassifier])

data = spark.createDataFrame([["I felt a bit drowsy and had blurred vision after taking Aspirin."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler() 
.setInputCol("text") 
.setOutputCol("document")


val tokenizer = new Tokenizer()
.setInputCols("document")
.setOutputCol("token")


val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_ade_augmented_v2", "en", "clinical/models")
.setInputCols(Array("document","token"))
.setOutputCol("class")


val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))


val data = Seq("I felt a bit drowsy and had blurred vision after taking Aspirin.").toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------+----------------------------------------------------------------+
|result|text                                                            |
+------+----------------------------------------------------------------+
|[True]|I felt a bit drowsy and had blurred vision after taking Aspirin.|
+------+----------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_ade_augmented_v2|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.6 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       False       0.97      0.97      0.97      2000
        True       0.90      0.89      0.90       530
    accuracy         -         -       0.96      2530
   macro-avg       0.93      0.93      0.93      2530
weighted-avg       0.96      0.96      0.96      2530
```
