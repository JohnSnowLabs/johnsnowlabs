---
layout: model
title: PHI Guard v6 Richness — PHI Exposure Level
author: John Snow Labs
name: Medical_DM_3m_v0.6_richness
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

PHI Guard v6 Richness estimates how much PHI a clinical document exposes, as one ordinal level. It does not locate or remove PHI, and a low level does not certify privacy safety.

## Predicted Entities

`NONE`, `TRACE`, `LOW`, `MODERATE`, `HIGH`, `VERY_HIGH`, `SATURATED`, `UNKNOWN`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/Medical_DM_3m_v0.6_richness_en_7.0.1_3.4_1794351110805.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/Medical_DM_3m_v0.6_richness_en_7.0.1_3.4_1794351110805.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Feed a DOCUMENT in column deidentified_document. Load PhiGuardModel.pretrained("Medical_DM_3m_v0.6_richness", "en", "clinical/models") and read phi_richness. Do not call setMode, and do not use the no-argument .pretrained() default (phi_guard_v7). Inspect result, metadata.level, metadata.status, and score_1 through score_6. These are not entity spans. The example text is synthetic, not a training excerpt.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
import sparknlp_jsl
from sparknlp_jsl.annotator.classification import PhiGuardModel

spark = sparknlp_jsl.start()  # Requires a licensed runtime that contains PhiGuardModel.
# Synthetic stand-in for the saved input column, not a de-identification pipeline.
assembler = DocumentAssembler().setInputCol("text").setOutputCol("deidentified_document")
guard = (PhiGuardModel.pretrained("Medical_DM_3m_v0.6_richness", "en", "clinical/models")
         .setInputCols("deidentified_document")
         .setOutputCol("phi_richness"))
notes = spark.createDataFrame(
    [("Example fictional note: [NAME] visited [HOSPITAL] on [DATE].",)],
    ["text"])
result = Pipeline(stages=[assembler, guard]).fit(notes).transform(notes)
result.selectExpr("phi_richness[0].result AS label",
                  "phi_richness[0].metadata AS metadata").show(truncate=False)
```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.PhiGuardModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession

// Requires a valid Healthcare NLP license and a runtime that contains PhiGuardModel.
// Synthetic stand-in for the saved input column, not a de-identification pipeline.
val spark = SparkSession.builder().master("local[2]").appName("PHI Guard v6 Richness").getOrCreate()
import spark.implicits._
val notes = Seq("Example fictional note: [NAME] visited [HOSPITAL] on [DATE].").toDF("text")
val assembler = new DocumentAssembler().setInputCol("text").setOutputCol("deidentified_document")
val guard = PhiGuardModel.pretrained("Medical_DM_3m_v0.6_richness", "en", "clinical/models")
  .setInputCols("deidentified_document")
  .setOutputCol("phi_richness")
val result = new Pipeline().setStages(Array(assembler, guard)).fit(notes).transform(notes)
result.selectExpr("phi_richness[0].result AS label", "phi_richness[0].metadata AS metadata").show(false)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|Medical_DM_3m_v0.6_richness|
|Compatibility:|Healthcare NLP 7.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[deidentified_document]|
|Output Labels:|[phi_richness]|
|Language:|en|
|Size:|12.0 MB|
|Dependencies:|DocumentAssembler|