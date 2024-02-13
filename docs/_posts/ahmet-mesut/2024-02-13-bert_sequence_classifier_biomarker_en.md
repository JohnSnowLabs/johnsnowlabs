---
layout: model
title: Bert For Sequence Classifier for Biomarker
author: John Snow Labs
name: bert_sequence_classifier_biomarker
date: 2024-02-13
tags: [en, licensed, bfsc, biomarker, classification, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT](https://nlp.johnsnowlabs.com/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) based biomarker classification model that can determine whether the clinical sentences include terms related to biomarkers or not.

## Predicted Entities

`1: Contains biomarker related terms.`, `0: Doesn't contain biomarker related terms.`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_biomarker_en_5.2.1_3.0_1707841923776.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_biomarker_en_5.2.1_3.0_1707841923776.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

sentence_detector = SentenceDetector() \
    .setInputCols(['document']) \
    .setOutputCol('sentence')

tokenizer = Tokenizer() \
    .setInputCols(['sentence']) \
    .setOutputCol('token')

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_biomarker","en","clinical/models")\
    .setInputCols(["sentence",'token'])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([["""In the realm of cancer research, several biomarkers have emerged as crucial indicators of disease progression and treatment response. For instance, the expression levels of HER2/neu, a protein receptor, have been linked to aggressive forms of breast cancer. Additionally, the presence of prostate-specific antigen (PSA) is often monitored to track the progression of prostate cancer. Moreover, in cardiovascular health, high-sensitivity C-reactive protein (hs-CRP) serves as a biomarker for inflammation and potential risk of heart disease. Meanwhile, elevated levels of troponin T are indicative of myocardial damage, commonly observed in acute coronary syndrome. In the field of diabetes management, glycated hemoglobin is a widely used to assess long-term blood sugar control. Its levels reflect the average blood glucose concentration over the past two to three months, offering valuable insights into disease management strategies."""]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_biomarker","en","clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  sequenceClassifier
))

val data = spark.createDataFrame(Seq(
  ("""In the realm of cancer research, several biomarkers have emerged as crucial indicators of disease progression and treatment response. For instance, the expression levels of HER2/neu, a protein receptor, have been linked to aggressive forms of breast cancer. Additionally, the presence of prostate-specific antigen (PSA) is often monitored to track the progression of prostate cancer. Moreover, in cardiovascular health, high-sensitivity C-reactive protein (hs-CRP) serves as a biomarker for inflammation and potential risk of heart disease. Meanwhile, elevated levels of troponin T are indicative of myocardial damage, commonly observed in acute coronary syndrome. In the field of diabetes management, glycated hemoglobin is a widely used to assess long-term blood sugar control. Its levels reflect the average blood glucose concentration over the past two to three months, offering valuable insights into disease management strategies.""",)
)).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

```
</div>

## Results

```bash
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|prediction|sentence                                                                                                                                                    |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|0         |In the realm of cancer research, several biomarkers have emerged as crucial indicators of disease progression and treatment response.                       |
|1         |For instance, the expression levels of HER2/neu, a protein receptor, have been linked to aggressive forms of breast cancer.                                 |
|1         |Additionally, the presence of prostate-specific antigen (PSA) is often monitored to track the progression of prostate cancer.                               |
|1         |Moreover, in cardiovascular health, high-sensitivity C-reactive protein (hs-CRP) serves as a biomarker for inflammation and potential risk of heart disease.|
|0         |Meanwhile, elevated levels of troponin T are indicative of myocardial damage, commonly observed in acute coronary syndrome.                                 |
|0         |In the field of diabetes management, glycated hemoglobin is a widely used to assess long-term blood sugar control.                                          |
|0         |Its levels reflect the average blood glucose concentration over the past two to three months, offering valuable insights into disease management strategies.|
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_biomarker|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|false|
|Max sentence length:|512|
