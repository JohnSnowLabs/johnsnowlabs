---
layout: model
title: Bert For Sequence Classification (Metastasis)
author: John Snow Labs
name: bert_sequence_classifier_metastasis
date: 2024-08-02
tags: [licensed, en, bfsc, metastasis, classification, oncology, tensorflow]
task: Text Classification
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT](https://nlp.johnsnowlabs.com/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) based metastasis classification model that can determine whether the clinical sentences include terms related to metastasis or not.
- `1`: Contains metastasis related terms.
- `0`: Doesn't contain metastasis related terms.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/08.3.MedicalBertForSequenceClassification_in_SparkNLP.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_en_5.4.0_3.0_1722598256861.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_en_5.4.0_3.0_1722598256861.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol('text')\
    .setOutputCol('document')

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(['sentence'])\
    .setOutputCol('token')

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_metastasis","en","clinical/models")\
    .setInputCols(["sentence",'token'])\
    .setOutputCol("prediction")

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    sequenceClassifier
])

sample_texts = [
                ["Contrast MRI confirmed the findings of meningeal carcinomatosis."],
                ["A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis."],
                ["The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci."] ,
                ["After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined."],
                ["The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer."],
                ["The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."],
                ]

sample_data = spark.createDataFrame(sample_texts).toDF("text")

result = pipeline.fit(sample_data).transform(sample_data)

result.select("text", "prediction.result").show(truncate=False)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol(Array("text"))
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_metastasis","en","clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("prediction")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  sequenceClassifier
))


val data = Seq(Array("Contrast MRI confirmed the findings of meningeal carcinomatosis.",
                     "A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.",
                     "The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci." ,
                     "After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.",
                     "The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.",
                     "The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."
                    )).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|text                                                                                                                                                                                                                 |result|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|Contrast MRI confirmed the findings of meningeal carcinomatosis.                                                                                                                                                     |[1]   |
|A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.                                                                                                                          |[0]   |
|The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci.|[1]   |
|After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.                                                                                       |[0]   |
|The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.                                                                                                                       |[1]   |
|The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease.                                                                                                       |[0]   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_metastasis|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|false|
|Max sentence length:|512|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
           0     0.9979    0.9986    0.9983      4357
           1     0.9944    0.9916    0.9930      1072
    accuracy        -         -      0.9972      5429
   macro-avg     0.9962    0.9951    0.9956      5429
weighted-avg     0.9972    0.9972    0.9972      5429
```
