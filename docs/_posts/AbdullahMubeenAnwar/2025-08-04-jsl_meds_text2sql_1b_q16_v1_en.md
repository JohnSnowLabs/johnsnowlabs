---
layout: model
title: JSL_MedSQL_T2SQL (t2sql - q16 - v1)
author: John Snow Labs
name: jsl_meds_text2sql_1b_q16_v1
date: 2025-08-04
tags: [medical, clinical, text2sql, q16, quantized, en, licensed, llamacpp]
task: Text Generation
language: en
edition: Healthcare NLP 6.0.0
spark_version: 3.0
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a lightweight Text-to-SQL model fine-tuned by John Snow Labs, built specifically for working with medical and healthcare data.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_text2sql_1b_q16_v1_en_6.0.0_3.0_1754331377777.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_text2sql_1b_q16_v1_en_6.0.0_3.0_1754331377777.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalLLM
from pyspark.ml import Pipeline

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_text2sql_1b_q16_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

pipeline = Pipeline(stages=[
    document_assembler,
    medical_llm
])

medm_prompt = """### Instruction:
Table: students  
- id  
- name  
- grade  

Write an SQL query to get the names of all students who got an A grade.

### Response:
"""

data = spark.createDataFrame([[medm_prompt]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("completions").show(truncate=False)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.MedicalLLM.pretrained(jsl_meds_text2sql_1b_q16_v1, "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    medical_llm
])

medm_prompt = """### Instruction:
Table: students  
- id  
- name  
- grade  

Write an SQL query to get the names of all students who got an A grade.

### Response:
"""

data = spark.createDataFrame([[medm_prompt]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("completions").show(truncate=False)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val medicalLLM = MedicalLLM.pretrained("jsl_meds_text2sql_1b_q16_v1", "en", "clinical/models")
  .setInputCols("document")
  .setOutputCol("completions")
  .setBatchSize(1)
  .setNPredict(100)
  .setUseChatTemplate(true)
  .setTemperature(0)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  medicalLLM
))

val medmPrompt = """### Instruction:
Table: students  
- id  
- name  
- grade  

Write an SQL query to get the names of all students who got an A grade.

### Response:
"""

val data = Seq(medmPrompt).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("completions").show(false)

```
</div>

## Results

```bash
SELECT name FROM students WHERE grade = 'A';
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_text2sql_1b_q16_v1|
|Compatibility:|Healthcare NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|