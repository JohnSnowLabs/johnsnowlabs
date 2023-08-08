---
layout: model
title: Medically Sound Suggestion Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_vop_sound_medical
date: 2023-06-13
tags: [licensed, clinical, classification, en, vop, tensorflow]
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

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier is meant to identify whether the suggestion that is mentioned in the text is medically sound.

## Predicted Entities

`True`, `False`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/VOP/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/VOICE_OF_PATIENT.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_sound_medical_en_4.4.3_3.0_1686673701807.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_sound_medical_en_4.4.3_3.0_1686673701807.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_sound_medical", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["I had a lung surgery for emphyema and after surgery my xray showing some recovery.",
                              "I was advised to put honey on a burned skin."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_sound_medical", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("I had a lung surgery for emphyema and after surgery my xray showing some recovery.",
                              "I was advised to put honey on a burned skin.")).toDS.toDF("text")
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------+-------+
|text                                                                              |result |
+----------------------------------------------------------------------------------+-------+
|I had a lung surgery for emphyema and after surgery my xray showing some recovery.|[True] |
|I was advised to put honey on a burned skin.                                      |[False]|
+----------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_sound_medical|
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
       False   0.848564  0.752315  0.797546       432
        True   0.664577  0.785185  0.719864       270
    accuracy   -         -         0.764957       702
   macro_avg   0.756570  0.768750  0.758705       702
weighted_avg   0.777800  0.764957  0.767668       702
```
