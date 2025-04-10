---
layout: model
title: 'Medical SOAP Note Generator for Clinical Notes (LLM - jsl_meds_text2soap_v1)
author: John Snow Labs
name: jsl_meds_text2soap_v1
date: 2025-04-09
tags: [en, licensed, clinical, medical, llm, soap, llamacpp]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.0
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Model a medical expert large language model to generate structured SOAP (Subjective, Objective, Assessment, Plan) summaries from patient-provider dialogues.
It ensures medically accurate documentation using standardized terminology and professional clinical formatting, suitable for real-world healthcare communication. 
The model strictly follows SOAP conventions without using special formatting or markdown.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_text2soap_v1_en_5.5.3_3.0_1744233560928.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_text2soap_v1_en_5.5.3_3.0_1744233560928.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_text2soap_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(1024)\
    .setUseChatTemplate(True)\
    .setTemperature(0)\
    .setNGpuLayers(1000)

pipeline = Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

prompt = """
<|im_start|>user
You are an expert medical professor assisting in the creation of medically accurate SOAP summaries.
Please ensure the response follows the structured format: S:, O:, A:, P: without using markdown or special formatting.
Create a Medical SOAP note summary from the dialogue, following these guidelines:
    S (Subjective): Summarize the patient's reported symptoms, including chief complaint and relevant history. Rely on the patient's statements as the primary source and ensure standardized terminology.
    O (Objective): Highlight critical findings such as vital signs, lab results, and imaging, emphasizing important details like the side of the body affected and specific dosages. Include normal ranges where relevant.
    A (Assessment): Offer a concise assessment combining subjective and objective data. State the primary diagnosis and any differential diagnoses, noting potential complications and the prognostic outlook.
    P (Plan): Outline the management plan, covering medication, diet, consultations, and education. Ensure to mention necessary referrals to other specialties and address compliance challenges.
    Considerations: Compile the report based solely on the transcript provided. Maintain confidentiality and document sensitively. Use concise medical jargon and abbreviations for effective doctor communication.
    Please format the summary in a clean, simple list format without using markdown or bullet points. Use 'S:', 'O:', 'A:', 'P:' directly followed by the text. Avoid any styling or special characters.
### Dialogue:

A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , and associated with an acute hepatitis , presented with a one-week history of polyuria , poor appetite , and vomiting .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG . She had been on dapagliflozin for six months at the time of presentation .
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness , guarding , or rigidity . Pertinent laboratory findings on admission were : serum glucose 111 mg/dl ,  creatinine 0.4 mg/dL , triglycerides 508 mg/dL , total cholesterol 122 mg/dL , and venous pH 7.27 .

<|im_end|>
<|im_start|>assistant
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.AutoGGUFModel.pretrained("jsl_meds_text2soap_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)


pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

prompt = """
<|im_start|>user
You are an expert medical professor assisting in the creation of medically accurate SOAP summaries.
Please ensure the response follows the structured format: S:, O:, A:, P: without using markdown or special formatting.
Create a Medical SOAP note summary from the dialogue, following these guidelines:
    S (Subjective): Summarize the patient's reported symptoms, including chief complaint and relevant history. Rely on the patient's statements as the primary source and ensure standardized terminology.
    O (Objective): Highlight critical findings such as vital signs, lab results, and imaging, emphasizing important details like the side of the body affected and specific dosages. Include normal ranges where relevant.
    A (Assessment): Offer a concise assessment combining subjective and objective data. State the primary diagnosis and any differential diagnoses, noting potential complications and the prognostic outlook.
    P (Plan): Outline the management plan, covering medication, diet, consultations, and education. Ensure to mention necessary referrals to other specialties and address compliance challenges.
    Considerations: Compile the report based solely on the transcript provided. Maintain confidentiality and document sensitively. Use concise medical jargon and abbreviations for effective doctor communication.
    Please format the summary in a clean, simple list format without using markdown or bullet points. Use 'S:', 'O:', 'A:', 'P:' directly followed by the text. Avoid any styling or special characters.
### Dialogue:

A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , and associated with an acute hepatitis , presented with a one-week history of polyuria , poor appetite , and vomiting .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG . She had been on dapagliflozin for six months at the time of presentation .
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness , guarding , or rigidity . Pertinent laboratory findings on admission were : serum glucose 111 mg/dl ,  creatinine 0.4 mg/dL , triglycerides 508 mg/dL , total cholesterol 122 mg/dL , and venous pH 7.27 .

<|im_end|>
<|im_start|>assistant
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medical_llm = MedicalLLM.pretrained("jsl_meds_text2soap_v1", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("completions")
    .setBatchSize(1)
    .setNPredict(100)
    .setUseChatTemplate(True)
    .setTemperature(0)


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    medical_llm
))

val prompt = """
<|im_start|>user
You are an expert medical professor assisting in the creation of medically accurate SOAP summaries.
Please ensure the response follows the structured format: S:, O:, A:, P: without using markdown or special formatting.
Create a Medical SOAP note summary from the dialogue, following these guidelines:
    S (Subjective): Summarize the patient's reported symptoms, including chief complaint and relevant history. Rely on the patient's statements as the primary source and ensure standardized terminology.
    O (Objective): Highlight critical findings such as vital signs, lab results, and imaging, emphasizing important details like the side of the body affected and specific dosages. Include normal ranges where relevant.
    A (Assessment): Offer a concise assessment combining subjective and objective data. State the primary diagnosis and any differential diagnoses, noting potential complications and the prognostic outlook.
    P (Plan): Outline the management plan, covering medication, diet, consultations, and education. Ensure to mention necessary referrals to other specialties and address compliance challenges.
    Considerations: Compile the report based solely on the transcript provided. Maintain confidentiality and document sensitively. Use concise medical jargon and abbreviations for effective doctor communication.
    Please format the summary in a clean, simple list format without using markdown or bullet points. Use 'S:', 'O:', 'A:', 'P:' directly followed by the text. Avoid any styling or special characters.
### Dialogue:

A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , and associated with an acute hepatitis , presented with a one-week history of polyuria , poor appetite , and vomiting .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG . She had been on dapagliflozin for six months at the time of presentation .
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness , guarding , or rigidity . Pertinent laboratory findings on admission were : serum glucose 111 mg/dl ,  creatinine 0.4 mg/dL , triglycerides 508 mg/dL , total cholesterol 122 mg/dL , and venous pH 7.27 .

<|im_end|>
<|im_start|>assistant
"""

val data = Seq(prompt).toDF("text")

val results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
</div>

## Results

```bash
S: The patient is a 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years ago and type two diabetes mellitus (T2DM), with a prior episode of HTG-induced pancreatitis three years ago. She presented with a one-week history of polyuria, poor appetite, and vomiting. She was on metformin, glipizide, dapagliflozin, atorvastatin, and gemfibrozil for her conditions.
O: Physical examination showed dry oral mucosa but was otherwise benign with no tenderness, guarding, or rigidity. Laboratory findings included serum glucose 111 mg/dL, creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27. She was on dapagliflozin for six months prior to presentation.
A: The primary diagnosis is diabetic ketoacidosis (DKA) based on the patient's symptoms of polyuria, poor appetite, vomiting, and elevated triglycerides and total cholesterol. Differential diagnoses could include other causes of polyuria such as diabetes insipidus or a complication from her underlying diabetes. The patient's history of HTG and recent use of dapagliflozin are also relevant.
P: The management plan includes close monitoring of her glucose levels and electrolyte balance. She will be started on intravenous insulin and hydration to treat DKA. Dietary adjustments will be made to manage her diabetes and HTG. Regular follow-up appointments will be scheduled to monitor her glucose levels and adjust her medications as necessary. Education on the importance of adherence to the treatment plan and monitoring for signs of complications such as worsening of symptoms or new symptoms will be provided.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_text2soap_v1|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.9 GB|