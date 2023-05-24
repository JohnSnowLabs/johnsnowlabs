---
layout: model
title: Side Effect Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_vop_side_effect
date: 2023-05-24
tags: [en, clinical, licensed, classifier, side_effect, adverse_event, vop, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that classifies texts written by patients as True if side effects from treatments or procedures are mentioned.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_side_effect_en_4.4.2_3.0_1684930827651.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_side_effect_en_4.4.2_3.0_1684930827651.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_side_effect", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["I felt kind of dizzy after taking that medication for a month.",
                              "I had a dental procedure last week and everything went well."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)

# Checking results
result.select("text", "class.result").show(truncate=False)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_side_effect", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("I felt kind of dizzy after taking that medication for a month.",
                              "I had a dental procedure last week and everything went well.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------------------------------------------------------------+-------+
|text                                                          |result |
+--------------------------------------------------------------+-------+
|I felt kind of dizzy after taking that medication for a month.|[True] |
|I had a dental procedure last week and everything went well.  |[False]|
+--------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_side_effect|
|Compatibility:|Healthcare NLP 4.4.2+|
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

Hello,I”m 20 year old girl. I”m diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I”m taking weekly supplement of vitamin D and 1000 mcg b12 daily. I”m taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I”m facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you.

## Benchmarking

```bash
         col  precision    recall  f1-score   support
       False   0.881423  0.822878  0.851145       271
        True   0.717647  0.802632  0.757764       152
    accuracy   -         -         0.815603       423
   macro-avg   0.799535  0.812755  0.804455       423
weighted-avg   0.822572  0.815603  0.817590       423
```
