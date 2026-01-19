---
layout: model
title: Medication Named Entity Recognition (Base, ONNX)
author: John Snow Labs
name: roberta_med_ner_onnx
date: 2025-12-26
tags: [roberta, ner, medical, clinical, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: RoBertaForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

RoBERTa-based token classification model trained to identify medication mentions in clinical and biomedical text using the BIO tagging scheme. The model labels medication entities with B-MEDICATION and I-MEDICATION tags while assigning O to non-medication tokens. It is designed for dense medication extraction in free-text clinical notes, discharge summaries, prescriptions, and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/roberta_med_ner_onnx_en_6.2.0_3.4_1766780561461.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/roberta_med_ner_onnx_en_6.2.0_3.4_1766780561461.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

tokenClassifier = RoBertaForTokenClassification \
    .pretrained("roberta_med_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient was initiated on metformin, insulin glargine, insulin lispro, and sitagliptin, later supplemented with aspirin, clopidogrel, warfarin, and heparin, treated concurrently with amoxicillin, azithromycin, ceftriaxone, and doxycycline, and discharged on atorvastatin, rosuvastatin, ezetimibe, lisinopril, losartan, metoprolol, and amlodipine."],
    ["During hospitalization the regimen included vancomycin, piperacillin tazobactam, meropenem, linezolid, and fluconazole, with pain managed using morphine, hydromorphone, fentanyl, acetaminophen, and ibuprofen, nausea controlled by ondansetron and metoclopramide, and gastric protection provided by omeprazole and pantoprazole."],
    ["In the oncology setting the patient received cisplatin, carboplatin, paclitaxel, docetaxel, doxorubicin, cyclophosphamide, and methotrexate, supported with filgrastim, pegfilgrastim, dexamethasone, ondansetron, and prochlorperazine, and later transitioned to tamoxifen, letrozole, anastrozole, and exemestane for long term therapy."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
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

tokenClassifier = medical.RoBertaForTokenClassification \
    .pretrained("roberta_med_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = nlp.NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient was initiated on metformin, insulin glargine, insulin lispro, and sitagliptin, later supplemented with aspirin, clopidogrel, warfarin, and heparin, treated concurrently with amoxicillin, azithromycin, ceftriaxone, and doxycycline, and discharged on atorvastatin, rosuvastatin, ezetimibe, lisinopril, losartan, metoprolol, and amlodipine."],
    ["During hospitalization the regimen included vancomycin, piperacillin tazobactam, meropenem, linezolid, and fluconazole, with pain managed using morphine, hydromorphone, fentanyl, acetaminophen, and ibuprofen, nausea controlled by ondansetron and metoclopramide, and gastric protection provided by omeprazole and pantoprazole."],
    ["In the oncology setting the patient received cisplatin, carboplatin, paclitaxel, docetaxel, doxorubicin, cyclophosphamide, and methotrexate, supported with filgrastim, pegfilgrastim, dexamethasone, ondansetron, and prochlorperazine, and later transitioned to tamoxifen, letrozole, anastrozole, and exemestane for long term therapy."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = RoBertaForTokenClassification
  .pretrained("roberta_med_ner_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("ner")

val converter = new NerConverter()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  tokenClassifier,
  converter
))

val data = Seq(
  "Patient was initiated on metformin, insulin glargine, insulin lispro, and sitagliptin, later supplemented with aspirin, clopidogrel, warfarin, and heparin, treated concurrently with amoxicillin, azithromycin, ceftriaxone, and doxycycline, and discharged on atorvastatin, rosuvastatin, ezetimibe, lisinopril, losartan, metoprolol, and amlodipine.",
  "During hospitalization the regimen included vancomycin, piperacillin tazobactam, meropenem, linezolid, and fluconazole, with pain managed using morphine, hydromorphone, fentanyl, acetaminophen, and ibuprofen, nausea controlled by ondansetron and metoclopramide, and gastric protection provided by omeprazole and pantoprazole.",
  "In the oncology setting the patient received cisplatin, carboplatin, paclitaxel, docetaxel, doxorubicin, cyclophosphamide, and methotrexate, supported with filgrastim, pegfilgrastim, dexamethasone, ondansetron, and prochlorperazine, and later transitioned to tamoxifen, letrozole, anastrozole, and exemestane for long term therapy."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+------------+----------+
|text        |entity    |
+------------+----------+
|metformin   |MEDICATION|
|insulin     |MEDICATION|
|insulin     |MEDICATION|
|lispro      |MEDICATION|
|sitagliptin |MEDICATION|
|aspirin     |MEDICATION|
|clopidogrel |MEDICATION|
|warfarin    |MEDICATION|
|heparin     |MEDICATION|
|amoxicillin |MEDICATION|
|azithromycin|MEDICATION|
|ceftriaxone |MEDICATION|
|doxycycline |MEDICATION|
|atorvastatin|MEDICATION|
|rosuvastatin|MEDICATION|
|ezetimibe   |MEDICATION|
|lisinopril  |MEDICATION|
|losartan    |MEDICATION|
|metoprolol  |MEDICATION|
+------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_med_ner_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|466.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|