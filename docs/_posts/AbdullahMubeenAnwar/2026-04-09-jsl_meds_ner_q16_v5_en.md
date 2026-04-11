---
layout: model
title: JSL_MedS_NER (LLM - q16 - v5)
author: John Snow Labs
name: jsl_meds_ner_q16_v5
date: 2026-04-09
tags: [medical, clinical, llm, ner, en, licensed, llamacpp]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model extracts structured entities from clinical trial eligibility criteria. Given unstructured text, it returns JSON with inclusion and exclusion entities. The model supports four entity types: age, lab, condition, and pregnancy. Each entity follows a fixed schema with normalized values and numeric thresholds where applicable. This model is intended for clinical trial eligibility parsing, patient matching, and structured medical information extraction workflows.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q16_v5_en_6.2.0_3.4_1775750133661.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q16_v5_en_6.2.0_3.4_1775750133661.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalLLM
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

llm = MedicalLLMModel.pretrained("jsl_meds_ner_q16_v5", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("llm_output")

pipeline = Pipeline(stages=[documentAssembler, llm])

text = """Inclusion Criteria:
Adults aged 18–75 with confirmed type 2 diabetes mellitus. HbA1c 7.0–10.5%. 
Fasting plasma glucose ≥126 mg/dL. Negative pregnancy test required.

Exclusion Criteria:
Type 1 diabetes mellitus. HbA1c >10.5%. Fasting plasma glucose >300 mg/dL. 
Pregnant or breastfeeding. Diabetic ketoacidosis. Uncontrolled thyroid disease.
"""
data = spark.createDataFrame([[text]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

llm = medical.MedicalLLMModel.pretrained("jsl_meds_ner_q16_v5", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("llm_output")

pipeline = nlp.Pipeline(stages=[documentAssembler, llm])

text = """Inclusion Criteria:
Adults aged 18–75 with confirmed type 2 diabetes mellitus. HbA1c 7.0–10.5%. 
Fasting plasma glucose ≥126 mg/dL. Negative pregnancy test required.

Exclusion Criteria:
Type 1 diabetes mellitus. HbA1c >10.5%. Fasting plasma glucose >300 mg/dL. 
Pregnant or breastfeeding. Diabetic ketoacidosis. Uncontrolled thyroid disease.
"""
data = spark.createDataFrame([[text]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val llm = MedicalLLMModel
  .pretrained("jsl_meds_ner_q16_v5", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("llm_output")

val pipeline = new Pipeline()
  .setStages(Array(documentAssembler, llm))

val text =
  """  Inclusion Criteria:
  Adults aged 18–75 with confirmed type 2 diabetes mellitus. HbA1c 7.0–10.5%.
  Fasting plasma glucose ≥126 mg/dL. Negative pregnancy test required.

  Exclusion Criteria:
  Type 1 diabetes mellitus. HbA1c >10.5%. Fasting plasma glucose >300 mg/dL.
  Pregnant or breastfeeding. Diabetic ketoacidosis. Uncontrolled thyroid disease.
  """
val data = Seq(text).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("llm_output").show(false)
```
</div>

## Results

```bash
{
  "inclusion": [
    {"type":"age","min_years":18,"max_years":75},
    {"type":"condition","name":"type 2 diabetes mellitus"},
    {"type":"lab","name":"HbA1c","min_percent":7.0,"max_percent":10.5},
    {"type":"lab","name":"fasting plasma glucose","min_value":126},
    {"type":"pregnancy","status":"negative_pregnancy_test"}
  ],
  "exclusion": [
    {"type":"condition","name":"type 1 diabetes mellitus"},
    {"type":"lab","name":"HbA1c","max_percent":10.5},
    {"type":"lab","name":"fasting plasma glucose","max_value":300},
    {"type":"pregnancy","status":"pregnant_or_lactating"},
    {"type":"condition","name":"diabetic ketoacidosis"},
    {"type":"condition","name":"uncontrolled thyroid disease"}
  ]
}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_q16_v5|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|6.1 GB|
