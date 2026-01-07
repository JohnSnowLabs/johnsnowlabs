---
layout: model
title: Numind Medical NER LLM v1 (jsl_meds_ner_deid_generic_2b_q8_v1)
author: John Snow Labs
name: jsl_meds_ner_deid_generic_2b_q8_v1
date: 2026-01-07
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_deid_generic_2b_q8_v1_en_6.2.2_3.4_1767781125402.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_deid_generic_2b_q8_v1_en_6.2.2_3.4_1767781125402.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    "NAME": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "LOCATION": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "CONTACT": ["verbatim-string"],
    "ID": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On March 15, 2024, 58-year-old male patient John Smith (medical record number 12345678) was admitted to Memorial Hospital in New York, NY under the care of Dr. Sarah Johnson with chest pain, cough and shortness of breath. He was diagnosed with stage IV non-small cell lung cancer with metastases to the liver and bones. Treatment included osimertinib 80 mg daily, carboplatin and pemetrexed chemotherapy, and pembrolizumab immunotherapy. After three months, imaging showed a 30% reduction in tumor size, his symptoms improved, and follow-up is scheduled for July 22, 2024.


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

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_deid_generic_2b_q8_v1", "en", "clinical/models")\
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
    "NAME": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "LOCATION": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "CONTACT": ["verbatim-string"],
    "ID": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On March 15, 2024, 58-year-old male patient John Smith (medical record number 12345678) was admitted to Memorial Hospital in New York, NY under the care of Dr. Sarah Johnson with chest pain, cough and shortness of breath. He was diagnosed with stage IV non-small cell lung cancer with metastases to the liver and bones. Treatment included osimertinib 80 mg daily, carboplatin and pemetrexed chemotherapy, and pembrolizumab immunotherapy. After three months, imaging showed a 30% reduction in tumor size, his symptoms improved, and follow-up is scheduled for July 22, 2024.


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

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_ner_deid_generic_2b_q8_v1", "en", "clinical/models")\
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
    "NAME": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "LOCATION": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "CONTACT": ["verbatim-string"],
    "ID": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On March 15, 2024, 58-year-old male patient John Smith (medical record number 12345678) was admitted to Memorial Hospital in New York, NY under the care of Dr. Sarah Johnson with chest pain, cough and shortness of breath. He was diagnosed with stage IV non-small cell lung cancer with metastases to the liver and bones. Treatment included osimertinib 80 mg daily, carboplatin and pemetrexed chemotherapy, and pembrolizumab immunotherapy. After three months, imaging showed a 30% reduction in tumor size, his symptoms improved, and follow-up is scheduled for July 22, 2024.


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
  .pretrained("jsl_meds_ner_deid_generic_2b_q8_v1", "en", "clinical/models")
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

|chunk            |begin|end|ner_label |confidence|
|-----------------|-----|---|--------- |----------|
|58-year-old      |41   |51 |AGE       |0.91463907|
|12345678         |64   |71 |CONTACT   |0.98403682|
|March 15, 2024   |3    |16 |DATE      |0.97907713|
|12345678         |64   |71 |ID        |0.90554436|
|Memorial Hospital|91   |107|LOCATION  |0.94546725|
|John Smith.      |27   |36 |NAME      |0.95915806|
|care             |136  |139|PROFESSION|0.98084227|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_deid_generic_2b_q8_v1|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.5 GB|