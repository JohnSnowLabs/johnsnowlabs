---
layout: model
title: Chest Radiology Disease Categories with Status Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_chest_radiology_disease_categories_status_onnx
date: 2026-04-12
tags: [medical, clinical, public_health, sequence_classification, en, licensed, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a BERT based multi-label sequence classifier for broad-category disease classification with clinical status detection in chest radiology reports. It is designed to evaluate or analyze free-text radiology report snippets, structured report sections, or individual clinical utterances. This model is the **category-level with status** variant, predicting both broader disease groupings and the radiologist's level of certainty (e.g., *Consolidation (Uncertain)*, *Pleural Effusion (Certain)*, *Cardiomegaly (Absent)*).

## Predicted Entities

`Mediastinal finding (Present)`, `Support Devices (Absent)`, `Focal air space opacity (Uncertain)`, `Air space opacity (Present)`, `Fracture (Present)`, `Support Devices (Present)`, `Solitary masslike opacity (Absent)`, `Widened cardiac silhouette (Uncertain)`, `Multiple masslike opacities (Absent)`, `Chest wall finding (Uncertain)`, `Chest wall finding (Present)`, `Pleural finding (Absent)`, `Mediastinal finding (Uncertain)`, `Widened cardiac silhouette (Absent)`, `Diffuse air space opacity (Present)`, `Widened aortic contour (Uncertain)`, `Vascular finding (Uncertain)`, `Chest wall finding (Absent)`, `Focal air space opacity (Absent)`, `Pneumothorax (Absent)`, `Diffuse air space opacity (Uncertain)`, `Subdiaphragmatic gas (Present)`, `Widened aortic contour (Present)`, `No Finding`, `Solitary masslike opacity (Present)`, `Multiple masslike opacities (Uncertain)`, `Lung Finding (Uncertain)`, `Air space opacity (Absent)`, `Pleural Thickening (Absent)`, `Support Devices (Uncertain)`, `Pleural Thickening (Uncertain)`, `Air space opacity (Uncertain)`, `Widened aortic contour (Absent)`, `Musculoskeletal finding (Present)`, `Pleural Effusion (Present)`, `Fracture (Absent)`, `Lung Finding (Absent)`, `Musculoskeletal finding (Absent)`, `Segmental collapse (Present)`, `Masslike opacity (Uncertain)`, `Pneumothorax (Present)`, `Pleural Effusion (Absent)`, `Upper abdominal finding (Absent)`, `Consolidation (Uncertain)`, `Vascular finding (Absent)`, `Mediastinal mass (Absent)`, `Multiple masslike opacities (Present)`, `Segmental collapse (Uncertain)`, `Subdiaphragmatic gas (Absent)`, `Focal air space opacity (Present)`, `Musculoskeletal finding (Uncertain)`, `Upper abdominal finding (Uncertain)`, `Subdiaphragmatic gas (Uncertain)`, `Widened cardiac silhouette (Present)`, `Pleural Effusion (Uncertain)`, `Mediastinal finding (Absent)`, `Solitary masslike opacity (Uncertain)`, `Consolidation (Present)`, `Diffuse air space opacity (Absent)`, `Pleural finding (Present)`, `Pleural Thickening (Present)`, `Pneumothorax (Uncertain)`, `Segmental collapse (Absent)`, `Upper abdominal finding (Present)`, `Vascular finding (Present)`, `Lung Finding (Present)`, `Pleural finding (Uncertain)`, `Mediastinal mass (Present)`, `Consolidation (Absent)`, `Masslike opacity (Absent)`, `Masslike opacity (Present)`, `Fracture (Uncertain)`, `Mediastinal mass (Uncertain)`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_categories_status_onnx_en_6.2.0_3.4_1776033926340.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_categories_status_onnx_en_6.2.0_3.4_1776033926340.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_status_onnx", "en", "clinical/models")\
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
    .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_status_onnx", "en", "clinical/models")\
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
  .pretrained("bert_sequence_classifier_chest_radiology_disease_categories_status_onnx", "en", "clinical/models")
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

+--------------------------------------------------------------------------------------------------------+---------------------------+
|text                                                                                                    |result                     |
+--------------------------------------------------------------------------------------------------------+---------------------------+
|Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease.|[Consolidation (Uncertain)]|
+--------------------------------------------------------------------------------------------------------+---------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_chest_radiology_disease_categories_status_onnx|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, document]|
|Output Labels:|[label]|
|Language:|en|
|Size:|442.3 MB|
