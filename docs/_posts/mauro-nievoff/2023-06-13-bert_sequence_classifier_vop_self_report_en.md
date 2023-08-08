---
layout: model
title: Self Report Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_vop_self_report
date: 2023-06-13
tags: [licensed, classification, vop, en, self_report, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can classify texts depending on if they are self-reported or if they refer to another person.

## Predicted Entities

`1st_Person`, `3rd_Person`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_en_4.4.3_3.0_1686671270069.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_self_report_en_4.4.3_3.0_1686671270069.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_self_report", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["My friend was treated for her skin cancer two years ago.",
                                  "I started with dysphagia in 2021, then, a few weeks later, felt weakness in my legs, followed by a severe diarrhea."], StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documenter = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_self_report", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("My friend was treated for her skin cancer two years ago.",
                     "I started with dysphagia in 2021, then, a few weeks later, felt weakness in my legs, followed by a severe diarrhea.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------------------------------------------------------------------------------------------------+------------+
|text                                                                                                               |result      |
+-------------------------------------------------------------------------------------------------------------------+------------+
|My friend was treated for her skin cancer two years ago.                                                           |[3rd_Person]|
|I started with dysphagia in 2021, then, a few weeks later, felt weakness in my legs, followed by a severe diarrhea.|[1st_Person]|
+-------------------------------------------------------------------------------------------------------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_self_report|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In-house annotated health-related text in colloquial language.

## Sample text from the training dataset

“Hello,I’m 20 year old girl. I’m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I’m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I’m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I’m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.”

## Benchmarking

```bash
       label  precision    recall  f1-score   support
  1st_Person   0.932432  0.985714  0.958333        70
  3rd_Person   0.975000  0.886364  0.928571        44
    accuracy   -         -         0.947368       114
   macro_avg   0.953716  0.936039  0.943452       114
weighted_avg   0.948862  0.947368  0.946846       114

```
