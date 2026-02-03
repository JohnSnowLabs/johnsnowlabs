---
layout: model
title: Bert For Sequence Classification (Metastasis) ONNX
author: John Snow Labs
name: bert_sequence_classifier_metastasis_onnx
date: 2025-09-12
tags: [licensed, en, bfsc, metastasis, classification, oncology, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
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
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_onnx_en_6.1.1_3.0_1757684174420.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_onnx_en_6.1.1_3.0_1757684174420.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_metastasis_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

sample_texts = [
                ["Contrast MRI confirmed the findings of meningeal carcinomatosis."],
                ["A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis."],
                ["The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci."] ,
                ["After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined."],
                ["The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer."],
                ["The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."],
                ]

data = spark.createDataFrame(sample_texts).toDF("text")


model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_metastasis_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
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


model = pipeline.fit(data)
result = model.transform(data)

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer() 
    .setInputCols(Array("document")) 
    .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_metastasis_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("Contrast MRI confirmed the findings of meningeal carcinomatosis.",
                     "A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.",
                     "The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci." ,
                     "After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.",
                     "The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.",
                     "The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."
                    )).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
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
|Model Name:|bert_sequence_classifier_metastasis_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|