---
layout: model
title: Numind Medical NER LLM v1 (jsl_meds_ner_deid_subentity_2b_q8_v1)
author: John Snow Labs
name: jsl_meds_ner_deid_subentity_2b_q8_v1
date: 2026-01-07
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

This medical LLM model is trained to extract medical entities from clinical notes and return them in structured JSON format. It supports various entity types such as AGE, CITY, COUNTRY, DATE, DEVICE, DLN, DOCTOR etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_deid_subentity_2b_q8_v1_en_6.2.2_3.4_1767777958544.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_deid_subentity_2b_q8_v1_en_6.2.2_3.4_1767777958544.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    "ACCOUNTNUM": ["verbatim-string"],
    "AGE": ["verbatim-string"],
    "CITY": ["verbatim-string"],
    "COUNTRY": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "DEVICE": ["verbatim-string"],
    "DLN": ["verbatim-string"],
    "DOCTOR": ["verbatim-string"],
    "EMAIL": ["verbatim-string"],
    "GENDER": ["verbatim-string"],
    "HOSPITAL": ["verbatim-string"],
    "IDNUM": ["verbatim-string"],
    "IP": ["verbatim-string"],
    "LOCATION_OTHER": ["verbatim-string"],
    "MEDICALRECORD": ["verbatim-string"],
    "NAME": ["verbatim-string"],
    "ORGANIZATION": ["verbatim-string"],
    "PATIENT": ["verbatim-string"],
    "PHONE": ["verbatim-string"],
    "PLATE": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "SSN": ["verbatim-string"],
    "STATE": ["verbatim-string"],
    "STREET": ["verbatim-string"],
    "TIME": ["verbatim-string"],
    "URL": ["verbatim-string"],
    "USERNAME": ["verbatim-string"],
    "VIN": ["verbatim-string"],
    "ZIP": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024 at 14:30, patient Emily Rodriguez, also registered as emily_r45, a 45-year-old female, holding ID number TR12345678901, SSN 123-45-6789, account number ACC-998877, medical record MR## 98765432, and driver's license number D1234567, was admitted to City General Hospital, operated by City Health Organization.

She resides at 742 Evergreen Terrace, Los Angeles, CA, 90001, USA, in the Downtown Medical District.

The patient was brought in using an iPhone 14, connected via IP address 192.168.1.45, and accessed the hospital portal at https://citygeneralhospital.org/patient using email emily.rodriguez@email.com and phone number +1-310-555-0198.

She arrived by personal vehicle with license plate CA-7XYZ123 and VIN 1HGCM82633A004352, and her listed profession is Graphic Designer.

Under the care of Dr. Michael Chen, the patient was evaluated on January 10, 2024 and diagnosed with Stage II glioblastoma multiforme.

Follow-up communication was scheduled for 09:00 AM on May 15, 2024, and all records were securely stored under the patient's verified profile for Emily Rodriguez.

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

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_deid_subentity_2b_q8_v1", "en", "clinical/models")\
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
    "ACCOUNTNUM": ["verbatim-string"],
    "AGE": ["verbatim-string"],
    "CITY": ["verbatim-string"],
    "COUNTRY": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "DEVICE": ["verbatim-string"],
    "DLN": ["verbatim-string"],
    "DOCTOR": ["verbatim-string"],
    "EMAIL": ["verbatim-string"],
    "GENDER": ["verbatim-string"],
    "HOSPITAL": ["verbatim-string"],
    "IDNUM": ["verbatim-string"],
    "IP": ["verbatim-string"],
    "LOCATION_OTHER": ["verbatim-string"],
    "MEDICALRECORD": ["verbatim-string"],
    "NAME": ["verbatim-string"],
    "ORGANIZATION": ["verbatim-string"],
    "PATIENT": ["verbatim-string"],
    "PHONE": ["verbatim-string"],
    "PLATE": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "SSN": ["verbatim-string"],
    "STATE": ["verbatim-string"],
    "STREET": ["verbatim-string"],
    "TIME": ["verbatim-string"],
    "URL": ["verbatim-string"],
    "USERNAME": ["verbatim-string"],
    "VIN": ["verbatim-string"],
    "ZIP": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024 at 14:30, patient Emily Rodriguez, also registered as emily_r45, a 45-year-old female, holding ID number TR12345678901, SSN 123-45-6789, account number ACC-998877, medical record MR## 98765432, and driver's license number D1234567, was admitted to City General Hospital, operated by City Health Organization.

She resides at 742 Evergreen Terrace, Los Angeles, CA, 90001, USA, in the Downtown Medical District.

The patient was brought in using an iPhone 14, connected via IP address 192.168.1.45, and accessed the hospital portal at https://citygeneralhospital.org/patient using email emily.rodriguez@email.com and phone number +1-310-555-0198.

She arrived by personal vehicle with license plate CA-7XYZ123 and VIN 1HGCM82633A004352, and her listed profession is Graphic Designer.

Under the care of Dr. Michael Chen, the patient was evaluated on January 10, 2024 and diagnosed with Stage II glioblastoma multiforme.

Follow-up communication was scheduled for 09:00 AM on May 15, 2024, and all records were securely stored under the patient's verified profile for Emily Rodriguez.

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

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_ner_deid_subentity_2b_q8_v1", "en", "clinical/models")\
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
    "ACCOUNTNUM": ["verbatim-string"],
    "AGE": ["verbatim-string"],
    "CITY": ["verbatim-string"],
    "COUNTRY": ["verbatim-string"],
    "DATE": ["verbatim-string"],
    "DEVICE": ["verbatim-string"],
    "DLN": ["verbatim-string"],
    "DOCTOR": ["verbatim-string"],
    "EMAIL": ["verbatim-string"],
    "GENDER": ["verbatim-string"],
    "HOSPITAL": ["verbatim-string"],
    "IDNUM": ["verbatim-string"],
    "IP": ["verbatim-string"],
    "LOCATION_OTHER": ["verbatim-string"],
    "MEDICALRECORD": ["verbatim-string"],
    "NAME": ["verbatim-string"],
    "ORGANIZATION": ["verbatim-string"],
    "PATIENT": ["verbatim-string"],
    "PHONE": ["verbatim-string"],
    "PLATE": ["verbatim-string"],
    "PROFESSION": ["verbatim-string"],
    "SSN": ["verbatim-string"],
    "STATE": ["verbatim-string"],
    "STREET": ["verbatim-string"],
    "TIME": ["verbatim-string"],
    "URL": ["verbatim-string"],
    "USERNAME": ["verbatim-string"],
    "VIN": ["verbatim-string"],
    "ZIP": ["verbatim-string"]
    }}
  ]
}}

#### Clinical Note:
On January 10, 2024 at 14:30, patient Emily Rodriguez, also registered as emily_r45, a 45-year-old female, holding ID number TR12345678901, SSN 123-45-6789, account number ACC-998877, medical record MR## 98765432, and driver's license number D1234567, was admitted to City General Hospital, operated by City Health Organization.

She resides at 742 Evergreen Terrace, Los Angeles, CA, 90001, USA, in the Downtown Medical District. Her primary contact name on file is Sarah Martinez, and her billing address is listed as 1234 Oak Street, Los Angeles, CA, 90002.

The patient was brought in using an iPhone 14, connected via IP address 192.168.1.45, and accessed the hospital portal at https://citygeneralhospital.org/patient using email emily.rodriguez@email.com and phone number +1-310-555-0198.

She arrived by personal vehicle with license plate CA-7XYZ123 and VIN 1HGCM82633A004352, and her listed profession is Graphic Designer.

Under the care of Dr. Michael Chen, the patient was evaluated on January 10, 2024 and diagnosed with Stage II glioblastoma multiforme.

Follow-up communication was scheduled for 09:00 AM on May 15, 2024, and all records were securely stored under the patient's verified profile for Emily Rodriguez.

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
  .pretrained("jsl_meds_ner_deid_subentity_2b_q8_v1", "en", "clinical/models")
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
    "ACCOUNTNUM": ["ACC-998877"]
    "AGE": ["45-year-old"]
    "CITY": ["Los Angeles", "Downtown Medical District"]
    "COUNTRY": ["USA"]
    "DATE": ["January 10, 2024", "May 15, 2024"]
    "DEVICE": ["iPhone 14"]
    "DLN": ["D1234567"]
    "DOCTOR": ["Michael Chen"]
    "EMAIL": ["emily.rodriguez@email.com"]
    "GENDER": ["female"]
    "HOSPITAL": ["City General Hospital"]
    "IDNUM": ["TR12345678901"]
    "IP": ["192.168.1.45"]
    "LOCATION_OTHER": ["742 Evergreen Terrace"]
    "MEDICALRECORD": ["98765432"]
    "NAME": ["Sarah Martinez"]
    "ORGANIZATION": ["City Health Organization"]
    "PATIENT": ["Emily Rodriguez"]
    "PHONE": ["+1-310-555-0198"]
    "PLATE": ["CA-7XYZ123"]
    "PROFESSION": ["Graphic Designer"]
    "SSN": ["123-45-6789"]
    "STATE": ["CA"]
    "STREET": ["1234 Oak Street"]
    "TIME": ["09:00 AM", "14:30"]
    "URL": ["https://citygeneralhospital.org/patient"]
    "VIN": ["1HGCM82633A004352"]
    "ZIP": ["90001", "90002"]

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_deid_subentity_2b_q8_v1|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.3 GB|
