---
layout: model
title: Patient Urgency Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_patient_urgency_onnx
date: 2025-09-12
tags: [urgency, emergency, licensed, en, text_classification, clinical, onnx]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_urgency_onnx_en_6.1.1_3.0_1757684339443.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_urgency_onnx_en_6.1.1_3.0_1757684339443.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_patient_urgency_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

data = spark.createDataFrame([["""I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it."""], 
 ["""My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move."""],
 ["""My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated."""],
 ]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    medical.MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_patient_urgency_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    nlp.NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

data = spark.createDataFrame([["""I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it."""], 
 ["""My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move."""],
 ["""My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated."""],
 ]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols(["document"])
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_sequence_classifier_patient_urgency_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val data = Seq(Array("I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it.", "My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move.", "My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated.")).toDS().toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
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
|Model Name:|bert_sequence_classifier_patient_urgency_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|