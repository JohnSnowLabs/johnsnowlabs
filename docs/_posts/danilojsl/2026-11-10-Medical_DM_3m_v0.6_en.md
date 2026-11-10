---
layout: model
title: PHI Guard v6 — Residual PHI Leak Assessment
author: John Snow Labs
name: Medical_DM_3m_v0.6
date: 2026-11-10
tags: [phi_guard, phi, clinical, healthcare, de_identification, classification, onnx, licensed, en]
task: De-identification
language: en
edition: Healthcare NLP 7.0.1
spark_version: 3.4
supported: true
annotator: PhiGuardModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

PHI Guard v6 scores de-identified clinical text for residual PHI that masking may have missed. It returns one document-level category per input document. It does not find or remove PHI, and a negative result does not certify privacy safety.

## Predicted Entities

`PHI_LEAK`, `NO_PHI_LEAK`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/Medical_DM_3m_v0.6_en_7.0.1_3.4_1794351105568.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/Medical_DM_3m_v0.6_en_7.0.1_3.4_1794351105568.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Convert text to a DOCUMENT with DocumentAssembler. Score the **final de-identified** document, not the original note. The stage reads DOCUMENT.result and does not check that the text was masked. Load the assumed published entry with PhiGuardModel.pretrained("Medical_DM_3m_v0.6", "en", "clinical/models") and set input/output columns. Do **not** call setMode: this saved artifact is fixed to residual leak, and the unstaged no-argument .pretrained() default is phi_guard_v7, so the v6 name must be explicit. Inspect CATEGORY.result and metadata.status. Empty and overlength results are not scored privacy assessments. The example uses fictional already-masked text, not a de-identification pipeline and not a training excerpt.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
import sparknlp_jsl
from sparknlp_jsl.annotator.classification import PhiGuardModel

spark = sparknlp_jsl.start()  # Requires a licensed runtime that contains PhiGuardModel.
assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")
guard = (PhiGuardModel.pretrained("Medical_DM_3m_v0.6", "en", "clinical/models")
         .setInputCols("document")
         .setOutputCol("phi_guard"))
notes = spark.createDataFrame(
    [("Example fictional de-identified note: [NAME] visited [HOSPITAL] on [DATE].",)],
    ["text"])
result = Pipeline(stages=[assembler, guard]).fit(notes).transform(notes)
result.selectExpr("phi_guard[0].result AS label",
                  "phi_guard[0].metadata AS metadata").show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.PhiGuardModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession

// Requires a valid Healthcare NLP license and a runtime that contains PhiGuardModel.
val spark = SparkSession.builder().master("local[2]").appName("PHI Guard v6").getOrCreate()
import spark.implicits._
val notes = Seq("Example fictional de-identified note: [NAME] visited [HOSPITAL] on [DATE].").toDF("text")
val assembler = new DocumentAssembler().setInputCol("text").setOutputCol("document")
val guard = PhiGuardModel.pretrained("Medical_DM_3m_v0.6", "en", "clinical/models")
  .setInputCols("document")
  .setOutputCol("phi_guard")
val result = new Pipeline().setStages(Array(assembler, guard)).fit(notes).transform(notes)
result.selectExpr("phi_guard[0].result AS label", "phi_guard[0].metadata AS metadata").show(false)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|Medical_DM_3m_v0.6|
|Compatibility:|Healthcare NLP 7.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[phi_guard]|
|Language:|en|
|Size:|12.0 MB|
|Dependencies:|DocumentAssembler|