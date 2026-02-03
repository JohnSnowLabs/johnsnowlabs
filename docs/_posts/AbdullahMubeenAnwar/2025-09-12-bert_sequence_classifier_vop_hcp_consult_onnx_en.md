---
layout: model
title: HCP Consult Classifier (BioBERT) ONNX
author: John Snow Labs
name: bert_sequence_classifier_vop_hcp_consult_onnx
date: 2025-09-12
tags: [licensed, en, classification, vop, clinical, onnx]
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

This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that can identify texts that mention a HCP consult.

## Predicted Entities

`Consulted_By_HCP`, `Other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_onnx_en_6.1.1_3.0_1757691703712.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_vop_hcp_consult_onnx_en_6.1.1_3.0_1757691703712.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequence_classifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_hcp_consult_onnx", "en", "clinical/models")\
  .setInputCols(["document", "token"])\
  .setOutputCol("class")

pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequence_classifier    
])

data = spark.createDataFrame(["hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before",
                              "My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies."], StringType()).toDF("text")

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

sequenceClassifier = medical.BertForSequenceClassification.pretrained("bert_sequence_classifier_vop_hcp_consult_onnx", "en", "clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("classes")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    sequenceClassifier
])
data = spark.createDataFrame(["hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before",
                              "My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies."], StringType()).toDF("text")

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

val sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_hcp_consult_onnx", "en", "clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, sequenceClassifier))

val data = Seq(Array("hi does anybody have feet aches with anxiety, i do suffer from anxiety but never had anything wrong with my feet before",
                      "My son has been to two doctors who gave him antibiotic drops but they also say the problem might related to allergies.")).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
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
|Model Name:|bert_sequence_classifier_vop_hcp_consult_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|