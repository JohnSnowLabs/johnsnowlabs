---
layout: model
title: Chest Radiology Disease Categories Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_chest_radiology_disease_categories_onnx
date: 2026-04-12
tags: [medical, clinical, public_health, sequence_classification, en, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a BERT based multi-label sequence classifier for broad-category disease classification in chest radiology reports. It is based on [microsoft/BiomedVLP-CXR-BERT-general](https://huggingface.co/microsoft/BiomedVLP-CXR-BERT-general) and fine-tuned on the StructUtterances dataset, a large corpus of over 1.5 million structured radiology utterances derived from chest X-ray reports (MIMIC-CXR, CheXpert Plus). The model classifies input text into **24 upper-level disease categories** following a hierarchical chest radiology ontology covering findings across six anatomical regions: lungs & airways, pleura, cardiovascular, mediastinal, musculoskeletal, and upper abdominal. It is designed to evaluate or analyze free-text radiology report snippets, structured report sections, or individual clinical utterances. This model is the **category-level** variant, predicting broader disease groupings in the ontology (e.g., *Consolidation*, *Pleural Effusion*, *Cardiomegaly*).

## Predicted Entities

`Pneumothorax`, `Diffuse air space opacity`, `Air space opacity`, `Consolidation`, `No Finding`, `Pleural finding`, `Widened aortic contour`, `Subdiaphragmatic gas`, `Focal air space opacity`, `Segmental collapse`, `Widened cardiac silhouette`, `Pleural Effusion`, `Chest wall finding`, `Fracture`, `Pleural Thickening`, `Masslike opacity`, `Lung Finding`, `Mediastinal finding`, `Solitary masslike opacity`, `Upper abdominal finding`, `Vascular finding`, `Mediastinal mass`, `Musculoskeletal finding`, `Support Devices`, `Multiple masslike opacities`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_categories_onnx_en_6.2.0_3.4_1776032582989.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_categories_onnx_en_6.2.0_3.4_1776032582989.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

sequenceClassifier = MedicalBertForSequenceClassification \
    .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_onnx", "en", "clinical/models")\
    .setInputCols(["token", "document"]) \
    .setOutputCol("label")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([
    ["Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease."]
]).toDF("text")

result = pipeline.fit(data).transform(data)
result.select("text", "label.result").show(1, False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

sequenceClassifier = medical.MedicalBertForSequenceClassification \
    .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_onnx", "en", "clinical/models")\
    .setInputCols(["token", "document"]) \
    .setOutputCol("label")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    sequenceClassifier
])

data = spark.createDataFrame([
    ["Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease."]
]).toDF("text")

result = pipeline.fit(data).transform(data)
result.select("text", "label.result").show(1, False)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotator._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val sequenceClassifier = MedicalBertForSequenceClassification
  .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("label")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  sequenceClassifier
))

val data = Seq(
  "Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.select("text", "label.result").show(1, false)
```
</div>

## Results

```bash

+--------------------------------------------------------------------------------------------------------+---------------+
|text                                                                                                    |result         |
+--------------------------------------------------------------------------------------------------------+---------------+
|Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease.|[Consolidation]|
+--------------------------------------------------------------------------------------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_chest_radiology_disease_categories_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, document]|
|Output Labels:|[label]|
|Language:|en|
|Size:|442.2 MB|