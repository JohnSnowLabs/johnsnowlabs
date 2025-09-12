---
layout: model
title: Patient Complaint Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_patient_complaint_onnx
date: 2025-09-12
tags: [en, licensed, clinical, text_classification, complaint, onnx]
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

This model is a BioBERT-based Classifier and it is trained for analyzing texts (email, google review, text messages etc.) written by patients about the performance of the healthcare facility and its personnel. 

The Text Classifier model has been trained using in-house annotated health-related text and also google reviews of various healthcare facilities. The dataset has been labeled with two different classes:

`Complaint`: The text includes dissatisfaction or frustration with some aspect of the healthcare provided to the patient. Most often, negative or critical language is used to describe the experience,

`No_Complaint`: The review expresses positive or neutral sentiment about the service. There is no criticism or expressing of dissatisfaction.

## Predicted Entities

`Complaint`, `No_Complaint`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_complaint_onnx_en_6.1.1_3.0_1757684241542.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_complaint_onnx_en_6.1.1_3.0_1757684241542.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_sequence_classifier_patient_complaint_onnx",
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

data = spark.createDataFrame([["""The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking"""],
 ["""My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn"""]]).toDF("text")

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
        "bert_sequence_classifier_patient_complaint_onnx",
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

data = spark.createDataFrame([["""The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking"""],
 ["""My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn"""]]).toDF("text")

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
  .pretrained("bert_sequence_classifier_patient_complaint_onnx", "en", "clinical/models")
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

val data = Seq(Array("The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking", "My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn")).toDS().toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
|                                                                                                                                                  text|        result|
+------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
|The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, ...|[No_Complaint]|
|My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad co...|   [Complaint]|
+------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_patient_complaint_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|