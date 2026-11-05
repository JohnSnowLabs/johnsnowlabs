---
layout: model
title: PHI Guard v7 — Multi-Task PHI Assessment
author: John Snow Labs
name: phi_guard_v7
date: 2026-11-05
tags: [phi_guard, phi, clinical, healthcare, de_identification, classification, onnx, licensed, en]
task: De-identification
language: en
edition: Healthcare NLP 7.0.0
spark_version: 3.4
supported: true
annotator: PhiGuardModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

PHI Guard v7 classifies original clinical text for PHI presence, or final de-identified text for residual/harmful PHI and exposure level. It does not remove PHI or certify privacy safety.

## Predicted Entities

`PHI_PRESENT`, `NO_PHI_PRESENT`, `PHI_LEAK`, `NO_PHI_LEAK`, `HARMFUL_PHI_LEAK`, `NO_HARMFUL_PHI_LEAK`, `NONE`, `TRACE`, `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH`, `SATURATED`, `UNKNOWN`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phi_guard_v7_en_7.0.0_3.4_1793895417949.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phi_guard_v7_en_7.0.0_3.4_1793895417949.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Provide DOCUMENT annotations. Select exactly one task with setMode: raw on original text; leak, harmful or richness on final de-identified text. Inspect CATEGORY.result and metadata.status; empty or overlength is not a scored privacy assessment. The stage does not mask text.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp_jsl.annotator.classification import PhiGuardModel
# Publication-target example; only works after an approved registry release.
guard = (PhiGuardModel.pretrained("phi_guard_v7", "en", "clinical/models")
         .setMode("leak").setInputCols("document").setOutputCol("phi_guard"))
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phi_guard_v7|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[phi_guard]|
|Language:|en|
|Size:|14.0 MB|
|Dependencies:|DocumentAssembler|