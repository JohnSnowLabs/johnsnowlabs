---
layout: model
title: Oncological Response to Treatment Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_response_to_treatment_onnx
date: 2025-09-12
tags: [licensed, en, clinical, public_health, response, treatment, classifier, onnx]
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

The Oncological Response to Treatment classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: `Yes` and `No`.

- `Yes`: The patient responded to treatment.

- `No`: The patient did not respond to treatment.

## Predicted Entities

`Yes`, `No`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_response_to_treatment_onnx_en_6.1.1_3.0_1757684851181.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_response_to_treatment_onnx_en_6.1.1_3.0_1757684851181.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_response_to_treatment_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

sample_texts = [
    ["Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy."],
    ["The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. "],
    ["MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy."],
    ["A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum."],
    ["Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib."],
    ["Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention."],
    ["The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."]
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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_response_to_treatment_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

sample_texts = [
    ["Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy."],
    ["The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. "],
    ["MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy."],
    ["A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum."],
    ["Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib."],
    ["Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention."],
    ["The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."]
]

data = spark.createDataFrame(sample_texts).toDF("text")


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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_response_to_treatment_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))
val data = Seq(Array(
    "Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy.",
    "The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. ",
    "MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy.",
    "A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum.",
    "Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib.",
    "Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention.",
    "The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."
)).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+------+
|                                                                                                text|result|
+----------------------------------------------------------------------------------------------------+------+
|Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting s...| [Yes]|
|The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion s...| [Yes]|
|MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision a...| [Yes]|
|A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infe...|  [No]|
|Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and numb...|  [No]|
|Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation an...|  [No]|
|The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and F...|  [No]|
+----------------------------------------------------------------------------------------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_response_to_treatment_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|