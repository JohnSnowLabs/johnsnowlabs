---
layout: model
title: Chest Radiology Disease Findings with Status Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_chest_radiology_disease_findings_status_onnx
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

This model is a BERT based multi-label sequence classifier for fine-grained disease classification with clinical status detection in chest radiology reports. It is designed to evaluate or analyze free-text radiology report snippets, structured report sections, or individual clinical utterances. This model is the **leaf-level with status** variant, predicting both the most specific disease findings in the ontology and the radiologist's level of certainty (e.g., *Atelectasis (Uncertain)*, *Pneumonia (Certain)*, *Simple pleural effusion (Absent)*).

## Predicted Entities

`Bronchiectasis (Uncertain)`, `Enlarged pulmonary artery (Uncertain)`, `Pericardial effusion (Present)`, `Nodule/Solitary lung nodule (Uncertain)`, `Simple pneumothorax (Absent)`, `Suboptimal central line (Present)`, `Simple pleural effusion (Present)`, `Acute clavicle fracture (Absent)`, `Suboptimal pulmonary arterial catheter (Present)`, `Fibrosis (Present)`, `Pneumomediastinum (Absent)`, `Lung collapse (Present)`, `Acute scapula fracture (Present)`, `Emphysema (Absent)`, `PICC line (Absent)`, `Calcification of the Aorta (Absent)`, `Pleural Other (Present)`, `Cavitating mass with content (Uncertain)`, `Loculated pneumothorax (Present)`, `Pulmonary congestion (Uncertain)`, `LVAD (Uncertain)`, `Pleural scarring (Absent)`, `Suboptimal endotracheal tube (Uncertain)`, `Inferior mediastinal mass (Uncertain)`, `Implantable defibrillator (Present)`, `Hilar lymphadenopathy (Absent)`, `Tortuous Aorta (Absent)`, `Enlarged pulmonary artery (Absent)`, `Air space opacity–multifocal (Uncertain)`, `Lung collapse (Uncertain)`, `Port catheter (Present)`, `Simple pleural effusion (Uncertain)`, `Lung Lesion (Present)`, `Pneumonia (Uncertain)`, `Shoulder dislocation (Uncertain)`, `Atelectasis (Absent)`, `Pleural scarring (Present)`, `Cavitating mass with content (Present)`, `Pleural scarring (Uncertain)`, `Shoulder dislocation (Absent)`, `Pericardial effusion (Uncertain)`, `Nodule/Solitary lung nodule (Present)`, `Acute clavicle fracture (Present)`, `Lung Lesion (Absent)`, `Hydropneumothorax (Uncertain)`, `Hilar lymphadenopathy (Uncertain)`, `Edema (Present)`, `Atelectasis (Uncertain)`, `Tortuous Aorta (Uncertain)`, `Enlarged pulmonary artery (Present)`, `Simple pneumothorax (Uncertain)`, `Suboptimal pulmonary arterial catheter (Uncertain)`, `Mass/Solitary lung mass (Absent)`, `Tracheal deviation (Present)`, `Implantable defibrillator (Absent)`, `Superior mediastinal mass (Present)`, `No Finding`, `Pleural tube (Present)`, `Compression fracture (Uncertain)`, `Emphysema (Present)`, `Intraaortic balloon pump (Absent)`, `Cardiomegaly (Absent)`, `Pulmonary congestion (Absent)`, `Pacemaker (Absent)`, `Port catheter (Absent)`, `Perihilar airspace opacity (Present)`, `Subcutaneous Emphysema (Absent)`, `Lung Lesion (Uncertain)`, `Tracheal deviation (Absent)`, `Emphysema (Uncertain)`, `Edema (Uncertain)`, `Mass/Solitary lung mass (Present)`, `Acute scapula fracture (Uncertain)`, `Shoulder dislocation (Present)`, `Cardiomegaly (Uncertain)`, `Suboptimal nasogastric tube (Absent)`, `Tracheal deviation (Uncertain)`, `Perihilar airspace opacity (Absent)`, `Atelectasis (Present)`, `Air space opacity–multifocal (Present)`, `Suboptimal pulmonary arterial catheter (Absent)`, `Acute humerus fracture (Absent)`, `Pneumonia (Present)`, `Pacemaker (Uncertain)`, `Calcification of the Aorta (Uncertain)`, `PICC line (Present)`, `Compression fracture (Present)`, `Pleural tube (Uncertain)`, `Loculated pleural effusion (Present)`, `Calcification of the Aorta (Present)`, `Suboptimal central line (Uncertain)`, `Cardiomegaly (Present)`, `Loculated pleural effusion (Absent)`, `Port catheter (Uncertain)`, `Subcutaneous Emphysema (Uncertain)`, `Acute humerus fracture (Present)`, `Inferior mediastinal mass (Present)`, `Suboptimal endotracheal tube (Present)`, `Hydropneumothorax (Absent)`, `Tension pneumothorax (Uncertain)`, `Pericardial effusion (Absent)`, `Bronchiectasis (Absent)`, `Pneumomediastinum (Present)`, `Pleural Other (Uncertain)`, `Pulmonary congestion (Present)`, `Hernia (Absent)`, `Pneumonia (Absent)`, `Hydropneumothorax (Present)`, `Cavitating mass with content (Absent)`, `Edema (Absent)`, `Suboptimal central line (Absent)`, `Pneumoperitoneum (Absent)`, `Pleural tube (Absent)`, `Simple pleural effusion (Absent)`, `Air space opacity–multifocal (Absent)`, `Perihilar airspace opacity (Uncertain)`, `Suboptimal nasogastric tube (Uncertain)`, `Loculated pneumothorax (Uncertain)`, `LVAD (Absent)`, `Tension pneumothorax (Present)`, `Pneumoperitoneum (Uncertain)`, `Acute scapula fracture (Absent)`, `Pleural Other (Absent)`, `Hernia (Present)`, `Mass/Solitary lung mass (Uncertain)`, `Subcutaneous Emphysema (Present)`, `Implantable defibrillator (Uncertain)`, `Compression fracture (Absent)`, `Tension pneumothorax (Absent)`, `Cavitating masses (Uncertain)`, `Fibrosis (Absent)`, `Acute rib fracture (Uncertain)`, `Bronchiectasis (Present)`, `Aspiration (Uncertain)`, `Intraaortic balloon pump (Uncertain)`, `Cavitating masses (Absent)`, `Aspiration (Absent)`, `Cavitating masses (Present)`, `PICC line (Uncertain)`, `Pacemaker (Present)`, `Tortuous Aorta (Present)`, `Pneumoperitoneum (Present)`, `Superior mediastinal mass (Uncertain)`, `Intraaortic balloon pump (Present)`, `Hernia (Uncertain)`, `Acute clavicle fracture (Uncertain)`, `Acute humerus fracture (Uncertain)`, `Fibrosis (Uncertain)`, `Lung collapse (Absent)`, `Superior mediastinal mass (Absent)`, `Acute rib fracture (Present)`, `Loculated pneumothorax (Absent)`, `LVAD (Present)`, `Inferior mediastinal mass (Absent)`, `Suboptimal endotracheal tube (Absent)`, `Loculated pleural effusion (Uncertain)`, `Suboptimal nasogastric tube (Present)`, `Simple pneumothorax (Present)`, `Aspiration (Present)`, `Nodule/Solitary lung nodule (Absent)`, `Pneumomediastinum (Uncertain)`, `Acute rib fracture (Absent)`, `Hilar lymphadenopathy (Present)`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_findings_status_onnx_en_6.2.0_3.4_1776033348306.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_chest_radiology_disease_findings_status_onnx_en_6.2.0_3.4_1776033348306.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("bert_sequence_classifier_chest_radiology_disease_findings_status_onnx", "en", "clinical/models")\
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
    .pretrained("bert_sequence_classifier_chest_radiology_disease_findings_status_onnx", "en", "clinical/models")\
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
  .pretrained("bert_sequence_classifier_chest_radiology_disease_findings_status_onnx", "en", "clinical/models")
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

+--------------------------------------------------------------------------------------------------------+-------------------------+
|text                                                                                                    |result                   |
+--------------------------------------------------------------------------------------------------------+-------------------------+
|Patchy consolidation in the left retrocardiac area, suggestive of atelectasis or early airspace disease.|[Atelectasis (Uncertain)]|
+--------------------------------------------------------------------------------------------------------+-------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_chest_radiology_disease_findings_status_onnx|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, document]|
|Output Labels:|[label]|
|Language:|en|
|Size:|442.6 MB|
