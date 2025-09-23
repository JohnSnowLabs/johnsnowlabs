---
layout: model
title: Adverse Drug Events Binary Classifier (LargeFewShot)
author: John Snow Labs
name: large_fewshot_classifier_ade
date: 2024-08-12
tags: [clinical, licensed, public_health, fewshot_classification, en, ade, classifier]
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

This model is a few-shot classification model designed to identify and classify tweets reporting Adverse Drug Events (ADEs). Utilizing the few-shot learning approach, it can effectively learn from a small number of labeled examples, making it highly adaptable to new and unseen classes.

## Predicted Entities

`ADE`, `noADE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/08.6.Text_Classification_with_FewShotClassifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/large_fewshot_classifier_ade_en_5.4.0_3.0_1723469859173.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/large_fewshot_classifier_ade_en_5.4.0_3.0_1723469859173.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

large_few_shot_classifier = LargeFewShotClassifierModel()\
    .pretrained('large_fewshot_classifier_ade')\
    .setInputCols("document")\
    .setOutputCol("prediction")

pipeline = Pipeline().setStages([
    document_assembler,
    large_few_shot_classifier
])

text_list = [
    ["The patient developed severe liver toxicity after taking the medication for three weeks"],
    ["He experienced no complications during the treatment and reported feeling much better."],
    ["She experienced a sudden drop in blood pressure after the administration of the new drug."],
    ["The doctor recommended a daily dosage of the vitamin supplement to improve her health."]
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
    .pretrained("large_fewshot_classifier_ade")
    .setInputCols("document")
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    largeFewShotClassifier
))

val textList = Seq(
    ("The patient developed severe liver toxicity after taking the medication for three weeks"),
    ("He experienced no complications during the treatment and reported feeling much better."),
    ("She experienced a sudden drop in blood pressure after the administration of the new drug."),
    ("The doctor recommended a daily dosage of the vitamin supplement to improve her health.")
)

val data = spark.createDataFrame(textList).toDF("text")

val result = pipeline.fit(data).transform(data)

result.select(col("text"), col("prediction.result").getItem(0).alias("result")).show(truncate = false)
```
</div>

## Results

```bash
+-----------------------------------------------------------------------------------------+------+
|text                                                                                     |result|
+-----------------------------------------------------------------------------------------+------+
|The patient developed severe liver toxicity after taking the medication for three weeks  |ADE   |
|He experienced no complications during the treatment and reported feeling much better.   |noADE |
|She experienced a sudden drop in blood pressure after the administration of the new drug.|ADE   |
|The doctor recommended a daily dosage of the vitamin supplement to improve her health.   |noADE |
+-----------------------------------------------------------------------------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|large_fewshot_classifier_ade|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|406.9 MB|
|Case sensitive:|false|

## References

This model has been trained using internal datasets.

## Benchmarking

```bash
       label  precision    recall  f1-score   support
         ADE     0.9560    0.9136    0.9343      2732
       noADE     0.9329    0.9661    0.9492      3397
    accuracy        -        -       0.9427      6129
   macro-avg     0.9444    0.9399    0.9418      6129
weighted-avg     0.9432    0.9427    0.9426      6129
```
