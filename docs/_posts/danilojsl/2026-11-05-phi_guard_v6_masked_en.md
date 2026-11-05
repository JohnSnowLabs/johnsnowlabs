---
layout: model
title: PHI Guard v6 Masked — Residual PHI Leak Assessment
author: John Snow Labs
name: phi_guard_v6_masked
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

PHI Guard v6 Masked scores de-identified clinical text for residual PHI that masking may have missed. It returns one document-level category. It does not find or remove PHI, and a negative result does not certify privacy safety.

## Predicted Entities

`PHI_LEAK`, `NO_PHI_LEAK`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phi_guard_v6_masked_en_7.0.0_3.4_1793909026252.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phi_guard_v6_masked_en_7.0.0_3.4_1793909026252.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Provide the final de-identified DOCUMENT in deidentified_document, not the original note. This artifact is fixed to residual leak, so do not call setMode. Read phi_guard_v6_masked. Inspect CATEGORY.result and metadata.status. Empty input returns NO_PHI_LEAK with status=empty and is not a scored negative. REVIEW_REQUIRED with status=overlength is unscored. A negative result is not a privacy certificate, and the stage does not mask text.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
import sparknlp_jsl
from sparknlp_jsl.annotator.classification import PhiGuardModel

spark = sparknlp_jsl.start()  # Requires a licensed runtime that contains PhiGuardModel.
# Synthetic stand-in for a final de-identified document, not a de-identification pipeline.
assembler = DocumentAssembler().setInputCol("text").setOutputCol("deidentified_document")
guard = (PhiGuardModel.pretrained("phi_guard_v6_masked", "en", "clinical/models")
         .setInputCols("deidentified_document")
         .setOutputCol("phi_guard_v6_masked"))
notes = spark.createDataFrame(
    [("Example fictional de-identified note: [NAME] visited [HOSPITAL] on [DATE].",)],
    ["text"])
result = Pipeline(stages=[assembler, guard]).fit(notes).transform(notes)
result.selectExpr("phi_guard_v6_masked[0].result AS label",
                  "phi_guard_v6_masked[0].metadata AS metadata").show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.PhiGuardModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession

// Requires a valid Healthcare NLP license and a runtime that contains PhiGuardModel.
// Synthetic stand-in for a final de-identified document, not a de-identification pipeline.
val spark = SparkSession.builder().master("local[2]").appName("PHI Guard v6 Masked").getOrCreate()
import spark.implicits._
val notes = Seq("Example fictional de-identified note: [NAME] visited [HOSPITAL] on [DATE].").toDF("text")
val assembler = new DocumentAssembler().setInputCol("text").setOutputCol("deidentified_document")
val guard = PhiGuardModel.pretrained("phi_guard_v6_masked", "en", "clinical/models")
  .setInputCols("deidentified_document")
  .setOutputCol("phi_guard_v6_masked")
val result = new Pipeline().setStages(Array(assembler, guard)).fit(notes).transform(notes)
result.selectExpr("phi_guard_v6_masked[0].result AS label", "phi_guard_v6_masked[0].metadata AS metadata").show(false)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phi_guard_v6_masked|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[deidentified_document]|
|Output Labels:|[phi_guard_v6_masked]|
|Language:|en|
|Size:|12.0 MB|
|Dependencies:|DocumentAssembler|