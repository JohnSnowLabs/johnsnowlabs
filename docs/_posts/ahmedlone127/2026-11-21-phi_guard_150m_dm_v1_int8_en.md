---
layout: model
title: PHI Guard Decision Model (150M, int8)
author: John Snow Labs
name: phi_guard_150m_dm_v1_int8
date: 2026-11-21
tags: [en, licensed, clinical, deidentification, phi, onnx, int8]
task: De-identification
language: en
edition: Healthcare NLP 7.0.2
spark_version: 3.0
supported: true
annotator: DecisionModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

## Description

This is the int8 version of `phi_guard_150m_dm_v1`. It checks a de-identified (masked) clinical note for protected health information (PHI) that was not removed. It is a 150M-parameter ModernBERT decision model, a clinical ModernBERT-base encoder with one shared answer head. Each `DecisionModel` stage answers one fixed question, selected with `setMode`:

- `leak`: is any PHI or personal identifier still readable? Gives `PHI_LEAK` or `NO_PHI_LEAK`.
- `harmful`: did something leak that could identify a person on its own, such as a name, an ID or record number, a phone number, an email, a street address, a ZIP code or a date of birth? Gives `HARMFUL_PHI_LEAK` or `NO_HARMFUL_PHI_LEAK`.
- `richness`: how much PHI is still exposed? Gives `NONE`, `TRACE`, `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH` or `SATURATED`.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phi_guard_150m_dm_v1_int8_en_7.0.2_3.0_1795285742674.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phi_guard_150m_dm_v1_int8_en_7.0.2_3.0_1795285742674.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator.classification import DecisionModel

document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

phi_guard = DecisionModel.pretrained("phi_guard_150m_dm_v1_int8", "en", "clinical/models")

leak = phi_guard.copy().setMode("leak") \
    .setInputCols(["document"]) \
    .setOutputCol("leak")

harmful = phi_guard.copy().setMode("harmful") \
    .setInputCols(["document"]) \
    .setOutputCol("harmful")

richness = phi_guard.copy().setMode("richness") \
    .setInputCols(["document"]) \
    .setOutputCol("richness")

pipeline = Pipeline(stages=[document_assembler, leak, harmful, richness])

data = spark.createDataFrame([
    ["Patient <NAME> was seen on <DATE> at <HOSPITAL>. Follow up in two weeks."],
    ["<NAME>, a retired schoolteacher from Springfield, was admitted to Mercy General Hospital on <DATE> with community acquired pneumonia."],
    ["Patient <NAME> was seen on <DATE>. Please call the patient back at 617-555-0142 to confirm the appointment."],
    ["Signed Electronically By: Dr. <DOCTOR> Scarce - <IDNUM> - <DATE> 9:33 PM"]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr(
    "leak[0].result as leak", "leak[0].metadata['phi_leak_prob'] as phi_leak_prob",
    "harmful[0].result as harmful", "harmful[0].metadata['harmful_leak_prob'] as harmful_leak_prob",
    "harmful[0].metadata['harm_if_leak_prob'] as harm_if_leak_prob",
    "richness[0].result as richness", "richness[0].metadata['level'] as level"
).show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.DecisionModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.param.ParamMap
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val phiGuard = DecisionModel.pretrained("phi_guard_150m_dm_v1_int8", "en", "clinical/models")

val leak = phiGuard.copy(ParamMap.empty).setMode("leak")
  .setInputCols("document")
  .setOutputCol("leak")

val harmful = phiGuard.copy(ParamMap.empty).setMode("harmful")
  .setInputCols("document")
  .setOutputCol("harmful")

val richness = phiGuard.copy(ParamMap.empty).setMode("richness")
  .setInputCols("document")
  .setOutputCol("richness")

val pipeline = new Pipeline().setStages(Array(documentAssembler, leak, harmful, richness))

val data = Seq(
  "Patient <NAME> was seen on <DATE> at <HOSPITAL>. Follow up in two weeks.",
  "<NAME>, a retired schoolteacher from Springfield, was admitted to Mercy General Hospital on <DATE> with community acquired pneumonia.",
  "Patient <NAME> was seen on <DATE>. Please call the patient back at 617-555-0142 to confirm the appointment.",
  "Signed Electronically By: Dr. <DOCTOR> Scarce - <IDNUM> - <DATE> 9:33 PM"
).toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------+-------------+-------------------+-----------------+-----------------+--------+-----+
|leak               |phi_leak_prob|harmful            |harmful_leak_prob|harm_if_leak_prob|richness|level|
+-------------------+-------------+-------------------+-----------------+-----------------+--------+-----+
|NO_PHI_LEAK        |0.0001       |NO_HARMFUL_PHI_LEAK|0.0001           |0.8509           |NONE    |0    |
|PHI_LEAK           |0.9928       |NO_HARMFUL_PHI_LEAK|0.0045           |0.0045           |LOW     |2    |
|PHI_LEAK           |0.9997       |HARMFUL_PHI_LEAK   |0.9997           |1.0000           |TRACE   |1    |
|PHI_LEAK           |0.9999       |HARMFUL_PHI_LEAK   |0.9999           |0.9999           |TRACE   |1    |
+-------------------+-------------+-------------------+-----------------+-----------------+--------+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phi_guard_150m_dm_v1_int8|
|Compatibility:|Healthcare NLP 7.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|157.4 MB|