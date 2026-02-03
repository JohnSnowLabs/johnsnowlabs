---
layout: model
title: SDOH Community Absent Binary Classification ONNX
author: John Snow Labs
name: bert_sequence_classifier_sdoh_community_absent_status_onnx
date: 2025-09-12
tags: [en, licensed, clinical, sequence_classification, classifier, community_absent, sdoh, onnx]
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

This model classifies related to the loss of social support such as a family member or friend in the clinical documents. A discharge summary was classified True for Community-Absent if the discharge summary had passages related to the loss of social support and False if such passages were not found in the discharge summary.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_community_absent_status_onnx_en_6.1.1_3.0_1757685124418.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_sdoh_community_absent_status_onnx_en_6.1.1_3.0_1757685124418.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_community_absent_status_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])
sample_texts =["She has two adult sons. She is a widow. She was employed with housework. She quit smoking 20 to 30 years ago, but smoked two packs per day for 20 to 30 years. She drinks one glass of wine occasionally. She avoids salt in her diet. ",
            "65 year old male presented with several days of vice like chest pain. He states that he felt like his chest was being crushed from back to the front. Lives with spouse and two sons moved to US 1 month ago."]

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_community_absent_status_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])

sample_texts =["She has two adult sons. She is a widow. She was employed with housework. She quit smoking 20 to 30 years ago, but smoked two packs per day for 20 to 30 years. She drinks one glass of wine occasionally. She avoids salt in her diet. ",
            "65 year old male presented with several days of vice like chest pain. He states that he felt like his chest was being crushed from back to the front. Lives with spouse and two sons moved to US 1 month ago."]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_sdoh_community_absent_status_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq("She has two adult sons. She is a widow. She was employed with housework. She quit smoking 20 to 30 years ago, but smoked two packs per day for 20 to 30 years. She drinks one glass of wine occasionally. She avoids salt in her diet.").toDF("text")


val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+-------+
|                                                                                                text| result|
+----------------------------------------------------------------------------------------------------+-------+
|She has two adult sons. She is a widow. She was employed with housework. She quit smoking 20 to 3...| [True]|
|65 year old male presented with several days of vice like chest pain. He states that he felt like...|[False]|
+----------------------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_sdoh_community_absent_status_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|442.4 MB|
|Case sensitive:|true|