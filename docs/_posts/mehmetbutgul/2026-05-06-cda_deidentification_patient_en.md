---
layout: model
title: CDA DeIdentification for Patient
author: John Snow Labs
name: cda_deidentification_patient
date: 2026-05-06
tags: [cda, ccd, licensed, healthcare, xml, deidentification, en]
task: De-identification
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: CdaDeIdentification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can deidentify CDA documents related to Patient XML paths

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cda_deidentification_patient_en_6.3.0_3.4_1778069129208.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cda_deidentification_patient_en_6.3.0_3.4_1778069129208.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

cda_xml = """YOUR_CDA_HERE"""
deid = CdaDeIdentification.pretrained("cda_deidentification_patient", "en", "clinical/models")\
  .setInputCol("text")\
  .setOutputCol("deid")\
  .setMode("obfuscate")

obfuscated = deid.deidentify(cda_xml)

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
cda_xml = """YOUR_CDA_HERE"""
deid = CdaDeIdentification.pretrained("cda_deidentification_patient", "en", "clinical/models")\
  .setInputCol("text")\
  .setOutputCol("deid")\
  .setMode("obfuscate")

obfuscated = deid.deidentify(cda_xml)
```
```scala
val cda_xml = """YOUR_CDA_HERE"""
val deid = CdaDeIdentification.pretrained("cda_deidentification_patient")
  .setInputCol("text")
  .setOutputCol("deid")
  .setMode("obfuscate")

val obfuscated = deid.deidentify(cda_xml)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cda_deidentification_patient|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[deid]|
|Language:|en|
|Size:|16.3 KB|