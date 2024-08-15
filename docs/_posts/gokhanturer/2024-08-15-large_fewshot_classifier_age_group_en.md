---
layout: model
title: Age Group Classifier (LargeFewShot)
author: John Snow Labs
name: large_fewshot_classifier_age_group
date: 2024-08-15
tags: [clinical, licensed, age, classification, fewshot, en]
task: Text Classification
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: LargeFewShotClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a few-shot classification model designed to identify and classify the age group of a person mentioned in health documents. Age of the person may or may not be mentioned explicitly in the training dataset. Utilizing the few-shot learning approach, it can effectively learn from a small number of labeled examples, making it highly adaptable to new and unseen classes.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/large_fewshot_classifier_age_group_en_5.4.0_3.0_1723734419677.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/large_fewshot_classifier_age_group_en_5.4.0_3.0_1723734419677.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

large_few_shot_classifier = LargeFewShotClassifierModel()\
    .pretrained('large_fewshot_classifier_age_group')\
    .setInputCols("document")\
    .setOutputCol("prediction")

pipeline = Pipeline().setStages([
    document_assembler,
    large_few_shot_classifier
])

text_list = [
    ("A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking.",),
    ("My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear hurt and she said he has an ear infection.She said it's most likely viral but could be bacterial.Mostly they clear on their own.Watch and see about antibiotics.So we held off yestetday and today to see how be went and he perkes up today but then has gone downhill this evening saying his ear hurts still and he just feels poorly.",),
    ("Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply",)
]

data = spark.createDataFrame(text_list, ["text"])

result = pipeline.fit(data).transform(data)

result.select("text", col("prediction.result").getItem(0).alias("result")).show(truncate=False)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val largeFewShotClassifier = LargeFewShotClassifierModel()
    .pretrained("large_fewshot_classifier_age_group")
    .setInputCols("document")
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    largeFewShotClassifier
))

val textList = Seq(
    ("A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking.",),
    ("My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear hurt and she said he has an ear infection.She said it's most likely viral but could be bacterial.Mostly they clear on their own.Watch and see about antibiotics.So we held off yestetday and today to see how be went and he perkes up today but then has gone downhill this evening saying his ear hurts still and he just feels poorly.",),
    ("Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply.",)
)

val data = spark.createDataFrame(textList).toDF("text")

val result = pipeline.fit(data).transform(data)

result.select(col("text"), col("prediction.result").getItem(0).alias("result")).show(truncate = false)
```
</div>

## Results

```bash
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |result |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking.|Adult  |
|My 4.5 year old has been poorly this week with a cold and thismorning he saw the doctors because he was up in the night last night saying his ear hurt and she said he has an ear infection.She said it's most likely viral but could be bacterial.Mostly they clear on their own.Watch and see about antibiotics.So we held off yestetday and today to see how be went and he perkes up today but then has gone downhill this evening saying his ear hurts still and he just feels poorly.  |Child  |
|Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply.                                                                                                                                               |Unknown|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|large_fewshot_classifier_age_group|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|407.1 MB|
|Case sensitive:|false|

## References

This model has been trained using internal datasets.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       Adult     0.7764    0.8132    0.7943       380
       Child     0.9364    0.8663    0.9000       187
     Unknown     0.7679    0.7588    0.7633       340
    accuracy       -          -      0.8037       907
   macro-avg     0.8269    0.8128    0.8192       907
weighted-avg     0.8062    0.8037    0.8045       907
```