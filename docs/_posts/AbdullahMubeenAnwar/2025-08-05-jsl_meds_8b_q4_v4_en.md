---
layout: model
title: JSL_MedS_v4 (LLM - 8B - q4)
author: John Snow Labs
name: jsl_meds_8b_q4_v4
date: 2025-08-05
tags: [medical, clinical, llm, q4, 8b, en, licensed, llamacpp]
task: [Summarization, Question Answering, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to perform Q&A, Summarization, RAG, and Chat.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_8b_q4_v4_en_6.1.0_3.0_1754426316794.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_8b_q4_v4_en_6.1.0_3.0_1754426316794.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

medical_llm = MedicalLLM.pretrained("jsl_meds_8b_q4_v4", "en", "clinical/models")\
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

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

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

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_8b_q4_v4", "en", "clinical/models")\
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

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.select("completions").show(truncate=False)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val medicalLLM = MedicalLLM.pretrained("jsl_meds_8b_q4_v4", "en", "clinical/models")
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

val prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

val data = Seq(prompt).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.select("completions").show(false)

```
</div>

## Results

```bash
Nitrofurantoin (E) is the best treatment option for this patient, as it is effective, safe, and appropriate for uncomplicated UTIs during pregnancy.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_8b_q4_v4|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.9 GB|
