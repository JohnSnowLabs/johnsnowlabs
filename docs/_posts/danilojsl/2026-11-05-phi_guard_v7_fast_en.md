---
layout: model
title: PHI Guard v7 Fast — Multi-Task PHI Assessment
author: John Snow Labs
name: phi_guard_v7_fast
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

PHI Guard v7 Fast assesses PHI in original clinical text or residual/harmful PHI and exposure level after de-identification. It does not remove PHI or certify privacy safety. Fast is a variant name, not a speed claim.

## Predicted Entities

`PHI_PRESENT`, `NO_PHI_PRESENT`, `PHI_LEAK`, `NO_PHI_LEAK`, `HARMFUL_PHI_LEAK`, `NO_HARMFUL_PHI_LEAK`, `NONE`, `TRACE`, `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH`, `SATURATED`, `UNKNOWN`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phi_guard_v7_fast_en_7.0.0_3.4_1793901725084.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phi_guard_v7_fast_en_7.0.0_3.4_1793901725084.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Provide DOCUMENT annotations. Select exactly one task with setMode: raw on original text; leak, harmful or richness on final de-identified text. Inspect CATEGORY.result and metadata.status; empty or overlength is not a scored privacy assessment. The stage does not mask text.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
import sparknlp_jsl
from sparknlp_jsl.annotator.classification import PhiGuardModel

spark = sparknlp_jsl.start()  # Requires a licensed compatible Healthcare NLP runtime.
notes = spark.createDataFrame(
    [("Fictional note: [NAME] visited [HOSPITAL] on [DATE].",)], ["text"])
assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")
guard = (PhiGuardModel.pretrained("phi_guard_v7_fast", "en", "clinical/models")
         .setMode("leak").setInputCols("document").setOutputCol("phi_guard"))
result = Pipeline(stages=[assembler, guard]).fit(notes).transform(notes)
result.selectExpr("phi_guard[0].result AS label", "phi_guard[0].metadata AS metadata").show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.PhiGuardModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession

// Requires a valid Healthcare NLP license and matching licensed/public JARs.
val spark = SparkSession.builder().master("local[2]").appName("PHI Guard v7 Fast").getOrCreate()
import spark.implicits._
val notes = Seq("Fictional note: [NAME] visited [HOSPITAL] on [DATE].").toDF("text")
val assembler = new DocumentAssembler().setInputCol("text").setOutputCol("document")
val guard = PhiGuardModel.pretrained("phi_guard_v7_fast", "en", "clinical/models")
  .setMode("leak").setInputCols("document").setOutputCol("phi_guard")
val result = new Pipeline().setStages(Array(assembler, guard)).fit(notes).transform(notes)
result.selectExpr("phi_guard[0].result AS label", "phi_guard[0].metadata AS metadata").show(false)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phi_guard_v7_fast|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[phi_guard]|
|Language:|en|
|Size:|3.6 MB|
|Dependencies:|DocumentAssembler|