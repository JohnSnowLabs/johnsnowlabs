---
layout: model
title: Numind Medical NER LLM v1 (jsl_meds_ner_2b_q8_v3)
author: John Snow Labs
name: jsl_meds_ner_2b_q8_v3
date: 2025-12-28
tags: [medical, clinical, ner, llm, en, licensed, numind, llamacpp]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
engine: llamacpp
annotator: MedicalVisionLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This medical LLM model is trained to extract medical entities from clinical notes and return them in structured JSON format. It supports various entity types such as AGE, CITY, DRUG, PATIENT, PROBLEM, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v3_en_6.2.2_3.4_1766953267755.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v3_en_6.2.2_3.4_1766953267755.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp_jsl.annotator import MedicalLLM
from sparknlp.base import DocumentAssembler
from pyspark.ml import Pipeline

prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024, patient Emily Rodriguez, a 45-year-old female (MR## 98765432), was admitted to City General Hospital in Los Angeles, CA, under the care of Dr. Michael Chen. The patient presented with severe headaches, blurred vision, and persistent nausea. She was diagnosed with Stage II glioblastoma multiforme (GBM) with involvement of the frontal lobe and temporal regions.
Treatment included temozolomide 150 mg twice daily, radiation therapy with 60 Gy over 6 weeks, and bevacizumab 10 mg/kg every 2 weeks. After 4 months, MRI scans showed stable disease with no significant progression. The patient's neurological symptoms improved, and she continues treatment with follow-up scheduled for May 15, 2024.


#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v3", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(3000)\
    .setUseChatTemplate(True)\
    .setTemperature(0.1)\
    .setTopK(40)\
    .setTopP(0.9)

pipeline = Pipeline(stages=[
    document_assembler,
    medical_llm
])

model = pipeline.fit(data)
results = model.transform(data)

output = results.select("completions").collect()[0].completions[0].result
print(output)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024, patient Emily Rodriguez, a 45-year-old female (MR## 98765432), was admitted to City General Hospital in Los Angeles, CA, under the care of Dr. Michael Chen. The patient presented with severe headaches, blurred vision, and persistent nausea. She was diagnosed with Stage II glioblastoma multiforme (GBM) with involvement of the frontal lobe and temporal regions.
Treatment included temozolomide 150 mg twice daily, radiation therapy with 60 Gy over 6 weeks, and bevacizumab 10 mg/kg every 2 weeks. After 4 months, MRI scans showed stable disease with no significant progression. The patient's neurological symptoms improved, and she continues treatment with follow-up scheduled for May 15, 2024.


#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

data = nlp.SparkSession.builder.getOrCreate().createDataFrame([[prompt]]).toDF("text")

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v3", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(3000)\
    .setUseChatTemplate(True)\
    .setTemperature(0.1)\
    .setTopK(40)\
    .setTopP(0.9)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    medical_llm
])

model = pipeline.fit(data)
results = model.transform(data)

output = results.select("completions").collect()[0].completions[0].result
print(output)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val prompt = """Extract all medical entities from the clinical note below and return them in JSON format according to the template.

#### Template:
{{
  "entities": [
    {{
      "AGE": ["verbatim-string"],
      "CITY": ["verbatim-string"],
      "COUNTRY": ["verbatim-string"],
      "DATE": ["verbatim-string"],
      "DOCTOR": ["verbatim-string"],
      "DOSAGE": ["verbatim-string"],
      "DRUG": ["verbatim-string"],
      "DURATION": ["verbatim-string"],
      "CANCER": ["verbatim-string"],
      "FREQUENCY": ["verbatim-string"],
      "HOSPITAL": ["verbatim-string"],
      "BODY_PART": ["verbatim-string"],
      "PATIENT": ["verbatim-string"],
      "PHONE": ["verbatim-string"],
      "PROBLEM": ["verbatim-string"],
      "PROFESSION": ["verbatim-string"],
      "STATE": ["verbatim-string"],
      "STRENGTH": ["verbatim-string"],
      "TEST": ["verbatim-string"],
      "TREATMENT": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024, patient Emily Rodriguez, a 45-year-old female (MR## 98765432), was admitted to City General Hospital in Los Angeles, CA, under the care of Dr. Michael Chen. The patient presented with severe headaches, blurred vision, and persistent nausea. She was diagnosed with Stage II glioblastoma multiforme (GBM) with involvement of the frontal lobe and temporal regions.
Treatment included temozolomide 150 mg twice daily, radiation therapy with 60 Gy over 6 weeks, and bevacizumab 10 mg/kg every 2 weeks. After 4 months, MRI scans showed stable disease with no significant progression. The patient's neurological symptoms improved, and she continues treatment with follow-up scheduled for May 15, 2024.


#### Instructions:
- Extract all entities exactly as they appear in the text
- Return only valid JSON format
- Use empty lists for categories with no entities found
- Do not add explanations, only return the JSON

#### Output:
"""

val data = Seq(prompt).toDF("text")

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val medicalLLM = MedicalLLM
  .pretrained("jsl_meds_ner_2b_q8_v3", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("completions")
  .setBatchSize(1)
  .setNPredict(3000)
  .setUseChatTemplate(true)
  .setTemperature(0.1)
  .setTopK(40)
  .setTopP(0.9)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  medicalLLM
))

val model = pipeline.fit(data)
val result = model.transform(data)

val output = result.select("completions").collect()(0).getAs[Seq[Row]]("completions")(0).getAs[String]("result")
println(output)

```
</div>

## Results

```bash

| chunk                   | begin | end | ner_label | confidence |
|-------------------------|-------|-----|-----------|------------|
| January 10, 2024        | 3     | 18  | DATE      | 0.99       |
| Emily Rodriguez         | 29    | 43  | PATIENT   | 0.92       |
| 45-year-old             | 48    | 58  | AGE       | 0.93       |
| 98765432                | 73    | 80  | PHONE     | 0.92       |
| City General Hospital   | 100   | 120 | HOSPITAL  | 0.92       |
| Los Angeles             | 125   | 135 | CITY      | 0.92       |
| under the care          | 142   | 155 | PROFESSION| 0.91       |
| CA                      | 152   | 153 | COUNTRY   | 0.93       |
| Michael Chen            | 164   | 175 | DOCTOR    | 0.92       |
| severe headaches        | 205   | 220 | PROBLEM   | 0.93       |
| glioblastoma multiforme | 294   | 316 | CANCER    | 0.93       |
| temporal regions        | 365   | 380 | BODY_PART | 0.93       |
| temozolomide            | 403   | 414 | DRUG      | 0.93       |
| 150 mg twice daily      | 416   | 433 | DOSAGE    | 0.92       |
| 6 weeks                 | 470   | 476 | DURATION  | 0.94       |
| every 2 weeks           | 504   | 516 | FREQUENCY | 0.93       |
| MRI                     | 535   | 537 | TEST      | 0.93       |
| stable disease          | 552   | 565 | STRENGTH  | 0.92       |
| CA                      | 623   | 624 | STATE     | 0.94       |
| follow-up               | 679   | 687 | TREATMENT | 0.92       |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_2b_q8_v3|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.3 GB|