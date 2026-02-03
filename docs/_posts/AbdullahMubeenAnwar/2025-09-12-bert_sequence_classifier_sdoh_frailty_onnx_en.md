---
layout: model
title: Social Determinants of Healthcare for Frailty Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_sdoh_frailty_onnx
date: 2025-09-12
tags: [licenced, en, sdoh, clinical, social_determinants_of_heathcare, public_health, frailty, licensed, onnx]
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

The Frailty classifier employs [BioBERT](https://arxiv.org/abs/1901.08746v2) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: 'High_or_Low_Frailty' and 'No_Frailty_or_Unknown.'

`High_or_Low_Frailty`: This category encompasses statements that indicate the presence of significant concerns or symptoms related to frailty conditions, suggesting either high or low risks. This label reflects substantial worries about frailty and the need for relevant medical measures.

`No_Frailty_or_Unknown`: This category includes statements that do not contain clear concerns related to frailty or where the frailty condition is unknown. This label indicates the absence of frailty-related issues or insufficient information in the text.

## Predicted Entities

`High_or_Low_Frailty`, `No_Frailty_or_Unknown`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_frailty_onnx_en_6.1.1_3.0_1757686136611.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_frailty_onnx_en_6.1.1_3.0_1757686136611.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_frailty_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

sample_texts=[  "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                "Post-chemotherapy, the patient was under regular surveillance for osteosarcoma. Recent imaging showed no signs of local recurrence or distant metastasis. Whereas the recovery was challenging, current evaluation confirms patient is in remission.",
                "The patient was diagnosed with stage II colon cancer and will be undergoing a treatment regimen that includes both chemotherapy and radiation therapy.",
                "Thyroid nodules detected during routine examination; fine-needle aspiration was conducted. Cytology results indicated no malignancy, consistent with a benign thyroid adenoma. However, patient is advised for a follow-up ultrasound in 12 months to monitor nodule size.",
                "The patient's persistent lymphadenopathy led to further tests, which confirmed a diagnosis of AIDS.",
                "Female patient presented with pelvic discomfort. Ovarian cysts were found during ultrasound; however, CA-125 levels are within normal range, and repeat imaging has shown consistent cyst size. No features of ovarian cancer were present, and a follow-up is scheduled in six months."
                ]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_frailty_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

sample_texts=[  "Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                "Post-chemotherapy, the patient was under regular surveillance for osteosarcoma. Recent imaging showed no signs of local recurrence or distant metastasis. Whereas the recovery was challenging, current evaluation confirms patient is in remission.",
                "The patient was diagnosed with stage II colon cancer and will be undergoing a treatment regimen that includes both chemotherapy and radiation therapy.",
                "Thyroid nodules detected during routine examination; fine-needle aspiration was conducted. Cytology results indicated no malignancy, consistent with a benign thyroid adenoma. However, patient is advised for a follow-up ultrasound in 12 months to monitor nodule size.",
                "The patient's persistent lymphadenopathy led to further tests, which confirmed a diagnosis of AIDS.",
                "Female patient presented with pelvic discomfort. Ovarian cysts were found during ultrasound; however, CA-125 levels are within normal range, and repeat imaging has shown consistent cyst size. No features of ovarian cancer were present, and a follow-up is scheduled in six months."
                ]

sample_data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_frailty_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
                "Post-chemotherapy, the patient was under regular surveillance for osteosarcoma. Recent imaging showed no signs of local recurrence or distant metastasis. Whereas the recovery was challenging, current evaluation confirms patient is in remission.",
                "The patient was diagnosed with stage II colon cancer and will be undergoing a treatment regimen that includes both chemotherapy and radiation therapy.",
                "Thyroid nodules detected during routine examination; fine-needle aspiration was conducted. Cytology results indicated no malignancy, consistent with a benign thyroid adenoma. However, patient is advised for a follow-up ultrasound in 12 months to monitor nodule size.",
                "The patient's persistent lymphadenopathy led to further tests, which confirmed a diagnosis of AIDS.",
                "Female patient presented with pelvic discomfort. Ovarian cysts were found during ultrasound; however, CA-125 levels are within normal range, and repeat imaging has shown consistent cyst size. No features of ovarian cancer were present, and a follow-up is scheduled in six months."
)).toDS.toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+-----------------------+
|                                                                                                text|                 result|
+----------------------------------------------------------------------------------------------------+-----------------------+
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|  [High_or_Low_Frailty]|
|Post-chemotherapy, the patient was under regular surveillance for osteosarcoma. Recent imaging sh...|[No_Frailty_or_Unknown]|
|The patient was diagnosed with stage II colon cancer and will be undergoing a treatment regimen t...|  [High_or_Low_Frailty]|
|Thyroid nodules detected during routine examination; fine-needle aspiration was conducted. Cytolo...|[No_Frailty_or_Unknown]|
| The patient's persistent lymphadenopathy led to further tests, which confirmed a diagnosis of AIDS.|  [High_or_Low_Frailty]|
|Female patient presented with pelvic discomfort. Ovarian cysts were found during ultrasound; howe...|[No_Frailty_or_Unknown]|
+----------------------------------------------------------------------------------------------------+-----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_frailty_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|