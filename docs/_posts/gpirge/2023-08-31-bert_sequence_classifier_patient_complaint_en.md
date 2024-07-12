---
layout: model
title: Patient Complaint Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_patient_complaint
date: 2023-08-31
tags: [en, licensed, clinical, text_classification, complaint, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
engine: tensorflow
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_complaint_en_5.0.2_3.0_1693442141882.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_patient_complaint_en_5.0.2_3.0_1693442141882.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_patient_complaint", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier])

data = spark.createDataFrame([["""The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking"""],
 ["""My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn"""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler =new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = new MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_patient_complaint", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking", "My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
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
|Model Name:|bert_sequence_classifier_patient_complaint|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In-house annotated health-related text and google reviews of various healthcare facilities.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
   Complaint       0.99      0.98      0.99       106
No_Complaint       0.98      0.99      0.99       112
    accuracy       -         -         0.99       218
   macro_avg       0.99      0.99      0.99       218
weighted_avg       0.99      0.99      0.99       218
```
