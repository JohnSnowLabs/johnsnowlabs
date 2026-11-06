---
layout: model
title: PHI Guard v6 Raw — PHI Presence Assessment
author: John Snow Labs
name: phi_guard_v6_raw
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

PHI Guard v6 Raw scores original clinical text for whether the note contains PHI. It returns one document-level category. It does not find or remove PHI, and a negative result does not certify that the note is free of PHI.

## Predicted Entities

`PHI_PRESENT`, `NO_PHI_PRESENT`, `REVIEW_REQUIRED`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/phi_guard_v6_raw_en_7.0.0_3.4_1793909412415.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/phi_guard_v6_raw_en_7.0.0_3.4_1793909412415.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

Score the original DOCUMENT before de-identification, not masked text. This artifact is fixed to raw presence, so do not call setMode. Read phi_present. Inspect CATEGORY.result and metadata.status. Scored results use phi_present_prob. Empty input returns NO_PHI_PRESENT with status=empty and is not a scored negative. REVIEW_REQUIRED with status=overlength is unscored. A negative result is not a privacy certificate, and the stage does not mask text.

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.ml import Pipeline
from sparknlp.base import DocumentAssembler
import sparknlp_jsl
from sparknlp_jsl.annotator.classification import PhiGuardModel

spark = sparknlp_jsl.start()  # Requires a licensed runtime that contains PhiGuardModel.
assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")
guard = (PhiGuardModel.pretrained("phi_guard_v6_raw", "en", "clinical/models")
         .setInputCols("document")
         .setOutputCol("phi_present"))
notes = spark.createDataFrame(
    [("Example fictional note: Alex Rivera visited Riverside Clinic on 2024-01-15.",)],
    ["text"])
result = Pipeline(stages=[assembler, guard]).fit(notes).transform(notes)
result.selectExpr("phi_present[0].result AS label",
                  "phi_present[0].metadata AS metadata").show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.classification.PhiGuardModel
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.SparkSession

// Requires a valid Healthcare NLP license and a runtime that contains PhiGuardModel.
val spark = SparkSession.builder().master("local[2]").appName("PHI Guard v6 Raw").getOrCreate()
import spark.implicits._
val notes = Seq("Example fictional note: Alex Rivera visited Riverside Clinic on 2024-01-15.").toDF("text")
val assembler = new DocumentAssembler().setInputCol("text").setOutputCol("document")
val guard = PhiGuardModel.pretrained("phi_guard_v6_raw", "en", "clinical/models")
  .setInputCols("document")
  .setOutputCol("phi_present")
val result = new Pipeline().setStages(Array(assembler, guard)).fit(notes).transform(notes)
result.selectExpr("phi_present[0].result AS label", "phi_present[0].metadata AS metadata").show(false)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|phi_guard_v6_raw|
|Compatibility:|Healthcare NLP 7.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[phi_present]|
|Language:|en|
|Size:|12.0 MB|
|Dependencies:|DocumentAssembler|