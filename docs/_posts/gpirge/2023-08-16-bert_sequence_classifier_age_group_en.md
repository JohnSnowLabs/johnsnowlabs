---
layout: model
title: Age Group Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_age_group
date: 2023-08-16
tags: [clinical, licensed, en, text_classification, age, age_group, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a BioBERT-based Age Group Text Classifier and it is trained for analyzing the age group of a person mentioned in health documents. Age of the person may or may not be mentioned explicitly in the training dataset.

The Text Classifier model has been trained using in-house annotated health-related text that have been labeled with three different classes:

Adult: A person who is fully grown or developed. Typically refers to someone who is 18 years or older,

Child: Requires intervention, urgent, not life-threatening cases.

Unknown: Not possible to comprehend/figure out the age group from the given text.

## Predicted Entities

`Adult`, `Child`, `Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_age_group_en_5.0.1_3.0_1692191540781.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_age_group_en_5.0.1_3.0_1692191540781.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_age_group", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier])

data = spark.createDataFrame([["""A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking."""],
 ["""My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear hurt and she said he has an ear infection.She said it's most likely viral but could be bacterial.Mostly they clear on their own.Watch and see about antibiotics.So we held off yestetday and today to see how be went and he perkes up today but then has gone downhill this evening saying his ear hurts still and he just feels poorly."""],
 ["""Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply"""]
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

val sequenceClassifier = new MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_age_group", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking.", "My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear hurt and she said he has an ear infection.She said it's most likely viral but could be bacterial.Mostly they clear on their own.Watch and see about antibiotics.So we held off yestetday and today to see how be went and he perkes up today but then has gone downhill this evening saying his ear hurts still and he just feels poorly.", "Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
|                                                                                                                                                  text|   result|
+------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
|A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30...|  [Adult]|
|My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear h...|  [Child]|
|Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am o...|[Unknown]|
+------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_age_group|
|Compatibility:|Healthcare NLP 5.0.1+|
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
       Adult       0.95      0.95      0.95       360
       Child       0.96      0.93      0.94       188
     Unknown       0.93      0.94      0.94       359
    accuracy       -         -         0.94       907
   macro avg       0.95      0.94      0.94       907
weighted avg       0.94      0.94      0.94       907
```