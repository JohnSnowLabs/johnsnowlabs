---
layout: model
title: Numind Medical NER LLM v1 (jsl_meds_ner_2b_q8_v2)
author: John Snow Labs
name: jsl_meds_ner_2b_q8_v2
date: 2025-12-28
tags: [medical, clinical, ner, llm, en, licensed, numind, llamacpp]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This medical LLM model is trained to extract medical entities from clinical notes and return them in structured JSON format. It supports various entity types such as AGE, CITY, DRUG, PATIENT, PROBLEM, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v2_en_6.2.2_3.4_1766947560933.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v2_en_6.2.2_3.4_1766947560933.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, under the care of Dr. Sarah Johnson. The patient presented with chest pain, cough, and shortness of breath. He was diagnosed with Stage IV non-small cell lung cancer (NSCLC) with metastases to the liver and bones.

Treatment included osimertinib 80 mg daily, chemotherapy with carboplatin and pemetrexed, and pembrolizumab immunotherapy. After 3 months, imaging showed partial response with 30% reduction in tumor size. The patient's symptoms improved, and he continues treatment with follow-up scheduled for July 22, 2024.


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

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v2", "en", "clinical/models")\
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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, under the care of Dr. Sarah Johnson. The patient presented with chest pain, cough, and shortness of breath. He was diagnosed with Stage IV non-small cell lung cancer (NSCLC) with metastases to the liver and bones.

Treatment included osimertinib 80 mg daily, chemotherapy with carboplatin and pemetrexed, and pembrolizumab immunotherapy. After 3 months, imaging showed partial response with 30% reduction in tumor size. The patient's symptoms improved, and he continues treatment with follow-up scheduled for July 22, 2024.


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

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v2", "en", "clinical/models")\
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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, under the care of Dr. Sarah Johnson. The patient presented with chest pain, cough, and shortness of breath. He was diagnosed with Stage IV non-small cell lung cancer (NSCLC) with metastases to the liver and bones.

Treatment included osimertinib 80 mg daily, chemotherapy with carboplatin and pemetrexed, and pembrolizumab immunotherapy. After 3 months, imaging showed partial response with 30% reduction in tumor size. The patient's symptoms improved, and he continues treatment with follow-up scheduled for July 22, 2024.


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
  .pretrained("jsl_meds_ner_2b_q8_v2", "en", "clinical/models")
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

|chunk                     |begin|end|ner_label|confidence|
|--------------------------|-----|---|---------|----------|
|58-year-old               |41   |51 |AGE      |0.99690467|
|liver                     |323  |327|BODY_PART|0.99508887|
|non-small cell lung cancer|265  |290|CANCER   |0.90104083|
|New York                  |112  |119|CITY     |0.98038649|
|March 15, 2024            |3    |16 |DATE     |0.9467498 |
|Sarah Johnson             |148  |160|DOCTOR   |0.92927407|
|80 mg                     |372  |376|DOSAGE   |0.96529836|
|osimertinib               |360  |370|DRUG     |0.92001022|
|3 months                  |470  |477|DURATION |0.91608679|
|daily                     |378  |382|FREQUENCY|0.96884026|
|Memorial Hospital         |91   |107|HOSPITAL |0.94301283|
|John Smith                |27   |36 |PATIENT  |0.93512589|
|12345678                  |64   |71 |PHONE    |0.91850522|
|chest pain                |190  |199|PROBLEM  |0.98347442|
|partial response          |495  |510|STRENGTH |0.96074057|
|imaging                   |480  |486|TEST     |0.90409901|
|chemotherapy              |385  |396|TREATMENT|0.97091188|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_2b_q8_v2|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.5 GB|