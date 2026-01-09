---
layout: model
title: Numind Medical NER LLM v1 (jsl_meds_ner_2b_q8_v1)
author: John Snow Labs
name: jsl_meds_ner_2b_q8_v1
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v1_en_6.2.2_3.4_1767782168823.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q8_v1_en_6.2.2_3.4_1767782168823.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, 10001, under the care of Dr. Sarah Johnson, an oncologist in the Oncology Department. The patient presented with severe chest pain, persistent cough, and shortness of breath that had been worsening over the past 3 months. His medical history revealed a 30-pack-year smoking history, and he had been diagnosed with Stage IIIB non-small cell lung cancer (NSCLC) in the right upper lobe 6 months ago.

Initial diagnostic workup included a CT scan of the chest, which showed a 4.5 cm mass in the right lung with mediastinal lymph node involvement. A PET scan confirmed metastatic disease to the liver and multiple bone sites, including the spine and ribs. Pathology results from a biopsy performed on February 20, 2024, revealed adenocarcinoma with histological type showing moderate differentiation (Grade 2). Biomarker testing showed positive results for EGFR mutation and PD-L1 expression of 65%. The cancer staging was updated to Stage IV (T2N2M1).

Treatment was initiated with targeted therapy using osimertinib 80 mg orally once daily, starting on March 20, 2024. The patient also received concurrent chemotherapy with carboplatin and pemetrexed every 3 weeks for 4 cycles. Additionally, immunotherapy with pembrolizumab 200 mg IV every 3 weeks was administered. Radiation therapy was delivered to the primary lung tumor site with a total dose of 60 Gy in 30 fractions over 6 weeks.

During Cycle 2, Day 8 of treatment, the patient developed grade 2 fatigue and mild nausea. Supportive care included ondansetron 8 mg twice daily for nausea and dexamethasone 4 mg daily. The patient's performance status was ECOG 1. Follow-up imaging after 3 months showed partial response to treatment with a 30% reduction in tumor size. The liver metastasis decreased from 2.3 cm to 1.5 cm.

The patient's vital signs were monitored regularly, including blood pressure, heart rate, and oxygen saturation. Laboratory tests revealed elevated CEA biomarker levels of 45.2 ng/mL (normal <3.0). Complete blood count showed mild anemia with hemoglobin of 10.5 g/dL. Liver function tests were within normal limits.

On follow-up visit dated June 10, 2024, the patient reported improvement in symptoms. The cough had decreased significantly, and pain management was achieved with oxycodone 10 mg every 6 hours as needed. The patient was advised to continue osimertinib and return for reassessment in 6 weeks. Contact information: Phone +1 (555) 123-4567, Email: john.smith@email.com.

The patient's employment status was noted as retired, and he lives at 123 Main Street, Apartment 4B, New York, NY 10001. His next appointment is scheduled for July 22, 2024 at 2:00 PM in the Oncology Clinic.
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

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v1", "en", "clinical/models")\
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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, 10001, under the care of Dr. Sarah Johnson, an oncologist in the Oncology Department. The patient presented with severe chest pain, persistent cough, and shortness of breath that had been worsening over the past 3 months. His medical history revealed a 30-pack-year smoking history, and he had been diagnosed with Stage IIIB non-small cell lung cancer (NSCLC) in the right upper lobe 6 months ago.

Initial diagnostic workup included a CT scan of the chest, which showed a 4.5 cm mass in the right lung with mediastinal lymph node involvement. A PET scan confirmed metastatic disease to the liver and multiple bone sites, including the spine and ribs. Pathology results from a biopsy performed on February 20, 2024, revealed adenocarcinoma with histological type showing moderate differentiation (Grade 2). Biomarker testing showed positive results for EGFR mutation and PD-L1 expression of 65%. The cancer staging was updated to Stage IV (T2N2M1).

Treatment was initiated with targeted therapy using osimertinib 80 mg orally once daily, starting on March 20, 2024. The patient also received concurrent chemotherapy with carboplatin and pemetrexed every 3 weeks for 4 cycles. Additionally, immunotherapy with pembrolizumab 200 mg IV every 3 weeks was administered. Radiation therapy was delivered to the primary lung tumor site with a total dose of 60 Gy in 30 fractions over 6 weeks.

During Cycle 2, Day 8 of treatment, the patient developed grade 2 fatigue and mild nausea. Supportive care included ondansetron 8 mg twice daily for nausea and dexamethasone 4 mg daily. The patient's performance status was ECOG 1. Follow-up imaging after 3 months showed partial response to treatment with a 30% reduction in tumor size. The liver metastasis decreased from 2.3 cm to 1.5 cm.

The patient's vital signs were monitored regularly, including blood pressure, heart rate, and oxygen saturation. Laboratory tests revealed elevated CEA biomarker levels of 45.2 ng/mL (normal <3.0). Complete blood count showed mild anemia with hemoglobin of 10.5 g/dL. Liver function tests were within normal limits.

On follow-up visit dated June 10, 2024, the patient reported improvement in symptoms. The cough had decreased significantly, and pain management was achieved with oxycodone 10 mg every 6 hours as needed. The patient was advised to continue osimertinib and return for reassessment in 6 weeks. Contact information: Phone +1 (555) 123-4567, Email: john.smith@email.com.

The patient's employment status was noted as retired, and he lives at 123 Main Street, Apartment 4B, New York, NY 10001. His next appointment is scheduled for July 22, 2024 at 2:00 PM in the Oncology Clinic.
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

medical_llm = medical.MedicalLLM.pretrained("jsl_meds_ner_2b_q8_v1", "en", "clinical/models")\
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
On March 15, 2024, patient John Smith, a 58-year-old male (MR## 12345678), was admitted to Memorial Hospital in New York, NY, 10001, under the care of Dr. Sarah Johnson, an oncologist in the Oncology Department. The patient presented with severe chest pain, persistent cough, and shortness of breath that had been worsening over the past 3 months. His medical history revealed a 30-pack-year smoking history, and he had been diagnosed with Stage IIIB non-small cell lung cancer (NSCLC) in the right upper lobe 6 months ago.

Initial diagnostic workup included a CT scan of the chest, which showed a 4.5 cm mass in the right lung with mediastinal lymph node involvement. A PET scan confirmed metastatic disease to the liver and multiple bone sites, including the spine and ribs. Pathology results from a biopsy performed on February 20, 2024, revealed adenocarcinoma with histological type showing moderate differentiation (Grade 2). Biomarker testing showed positive results for EGFR mutation and PD-L1 expression of 65%. The cancer staging was updated to Stage IV (T2N2M1).

Treatment was initiated with targeted therapy using osimertinib 80 mg orally once daily, starting on March 20, 2024. The patient also received concurrent chemotherapy with carboplatin and pemetrexed every 3 weeks for 4 cycles. Additionally, immunotherapy with pembrolizumab 200 mg IV every 3 weeks was administered. Radiation therapy was delivered to the primary lung tumor site with a total dose of 60 Gy in 30 fractions over 6 weeks.

During Cycle 2, Day 8 of treatment, the patient developed grade 2 fatigue and mild nausea. Supportive care included ondansetron 8 mg twice daily for nausea and dexamethasone 4 mg daily. The patient's performance status was ECOG 1. Follow-up imaging after 3 months showed partial response to treatment with a 30% reduction in tumor size. The liver metastasis decreased from 2.3 cm to 1.5 cm.

The patient's vital signs were monitored regularly, including blood pressure, heart rate, and oxygen saturation. Laboratory tests revealed elevated CEA biomarker levels of 45.2 ng/mL (normal <3.0). Complete blood count showed mild anemia with hemoglobin of 10.5 g/dL. Liver function tests were within normal limits.

On follow-up visit dated June 10, 2024, the patient reported improvement in symptoms. The cough had decreased significantly, and pain management was achieved with oxycodone 10 mg every 6 hours as needed. The patient was advised to continue osimertinib and return for reassessment in 6 weeks. Contact information: Phone +1 (555) 123-4567, Email: john.smith@email.com.

The patient's employment status was noted as retired, and he lives at 123 Main Street, Apartment 4B, New York, NY 10001. His next appointment is scheduled for July 22, 2024 at 2:00 PM in the Oncology Clinic.
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
  .pretrained("jsl_meds_ner_2b_q8_v1", "en", "clinical/models")
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

    "AGE": ["58-year-old"],
    "BODY_PART": ["chest"],
    "CANCER": ["non-small cell lung cancer"],
    "CITY": ["New York"],
    "COUNTRY": ["United States"],
    "DATE": ["March 15, 2024"],
    "DOCTOR": ["Sarah Johnson"],
    "DOSAGE": ["30-pack-year"],
    "DRUG": ["osimertinib"],
    "DURATION": ["once daily"],
    "FREQUENCY": ["daily"],
    "HOSPITAL": ["Memorial Hospital"],
    "PATIENT": ["John Smith"],
    "PHONE": ["+1 (555) 123-4567"],
    "PROBLEM": ["chest pain"],
    "PROFESSION": ["oncologist"],
    "STATE": ["New York"],
    "STRENGTH": ["80 mg"],
    "TEST": ["CT scan of the chest"],
    "TREATMENT": ["targeted therapy"],

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_2b_q8_v1|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.5 GB|