---
layout: model
title: Hl7 v2 Messages DeIdentification
author: John Snow Labs
name: hl7v2_deidentification_free_text
date: 2026-09-29
tags: [hl7, hl7_v2, deidentification, en, licensed, healthcare, free_text]
task: De-identification
language: en
edition: Healthcare NLP 7.0.0
spark_version: 3.4
supported: true
annotator: Hl7v2DeIdentification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can deidentify HL7 v2 messages related to PHI paths with free texts

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hl7v2_deidentification_free_text_en_7.0.0_3.4_1790683530401.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hl7v2_deidentification_free_text_en_7.0.0_3.4_1790683530401.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
hl7_v2_message = """YOUR_HL7_HERE"""
deid = Hl7v2DeIdentification.pretrained("hl7v2_deidentification_free_text", "en", "clinical/models")\
  .setInputCol("text")\
  .setOutputCol("deid")\
  .setMode("obfuscate")

obfuscated = deid.deidentify(hl7_v2_message )
```
```scala
val hl7_v2_message = """YOUR_HL7_HERE"""
val deid = Hl7v2DeIdentification.pretrained("hl7v2_deidentification_free_text", "en", "clinical/models")
  .setInputCol("text")
  .setOutputCol("deid")
  .setMode("obfuscate")
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hl7v2_deidentification_free_text|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[deid]|
|Language:|en|
|Size:|17.5 KB|