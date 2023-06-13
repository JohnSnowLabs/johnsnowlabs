---
layout: model
title: HCP Consult Classifier (BioBERT)
author: John Snow Labs
name: bert_sequence_classifier_vop_hcp_consult
date: 2023-06-13
tags: [licensed, en, classification, vop, clinical, tensorflow]
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

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can identify texts that mention a HCP consult.

## Predicted Entities

`Consulted_By_HCP`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_en_4.4.3_3.0_1686679279680.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_en_4.4.3_3.0_1686679279680.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_hcp_consult", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame(["hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before",
                              "My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)
```
```scala
val documenter = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_hcp_consult", "en", "clinical/models")
    .setInputCols(Array("document","token"))
    .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(documenter, tokenizer, sequenceClassifier))

val data = Seq(Array("hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before",
                      "My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies.")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------------------------------------------------------------------------------------------------+------------------+
|text                                                                                                                   |result            |
+-----------------------------------------------------------------------------------------------------------------------+------------------+
|hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before|[Other]           |
|My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies. |[Consulted_By_HCP]|
+-----------------------------------------------------------------------------------------------------------------------+------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_vop_hcp_consult|
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
Consulted_By_HCP   0.670412  0.730612  0.699219       245
           Other   0.848624  0.807860  0.827740       458
        accuracy   -         -         0.780939       703
       macro_avg   0.759518  0.769236  0.763480       703
    weighted_avg   0.786516  0.780939  0.782950       703
```
