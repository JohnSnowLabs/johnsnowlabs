---
layout: model
title: JSL_MedS_VLM_Reasoning_v1 (8B - q16)
author: John Snow Labs
name: jsl_meds_vlm_reasoning_8b_q16_v1
date: 2026-01-09
tags: [medical, clinical, vlm, q16, 8b, en, licensed, llamacpp]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: llamacpp
annotator: MedicalVisionLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This a vision language model designed for medical document understanding and image based clinical reasoning. It processes medical images and accompanying text to identify clinical findings, summarize content, and answer structured questions.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q16_v1_en_6.2.0_3.4_1767919852230.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q16_v1_en_6.2.0_3.4_1767919852230.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from sparknlp_jsl.utils import *
from pyspark.ml import Pipeline

prompt = """
Act as a senior clinical specialist and analyze this medical document. Perform the following steps in order:
1. Clinical Summary: Identify the patient's primary and secondary diagnoses, including any 'overlap' syndromes mentioned.
2. Medication Analysis Table: Create a table listing:
    * Medication Name
    * Dosage & Frequency
    * Clinical Justification: Explain why this specific drug is being used for this patient’s symptoms (e.g., link the vasodilators to the finger ulcers).
3. Conditional Logic & Alerts: Explicitly list any instructions that are 'prn' (as needed) or conditional (e.g., 'in case of...'). Identify any medications that require close monitoring for this patient's condition.
4. Visual Verification: Confirm if there are any handwritten notes or signatures that modify the printed instructions.
Please reason step-by-step before providing your final answer.
"""

input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = DocumentAssembler() \
    .setInputCol("prompt") \
    .setOutputCol("caption_document")

image_assembler = ImageAssembler() \
    .setInputCol("image") \
    .setOutputCol("image_assembler")

medicalVisionLLM = MedicalVisionLLM.load("jsl_meds_vlm_reasoning_8b_q16_v1", "en", "clinical/models") \
    .setInputCols(["caption_document", "image_assembler"]) \
    .setOutputCol("completions")

pipeline = Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical
from sparknlp_jsl.utils import vision_llm_preprocessor

prompt = """
Act as a senior clinical specialist and analyze this medical document. Perform the following steps in order:
1. Clinical Summary: Identify the patient's primary and secondary diagnoses, including any 'overlap' syndromes mentioned.
2. Medication Analysis Table: Create a table listing:
    * Medication Name
    * Dosage & Frequency
    * Clinical Justification: Explain why this specific drug is being used for this patient’s symptoms (e.g., link the vasodilators to the finger ulcers).
3. Conditional Logic & Alerts: Explicitly list any instructions that are 'prn' (as needed) or conditional (e.g., 'in case of...'). Identify any medications that require close monitoring for this patient's condition.
4. Visual Verification: Confirm if there are any handwritten notes or signatures that modify the printed instructions.
Please reason step-by-step before providing your final answer.
"""

input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = nlp.DocumentAssembler() \
    .setInputCol("prompt") \
    .setOutputCol("caption_document")

image_assembler = nlp.ImageAssembler() \
    .setInputCol("image") \
    .setOutputCol("image_assembler")

medicalVisionLLM = medical.MedicalVisionLLM.load("jsl_meds_vlm_reasoning_8b_q16_v1", "en", "clinical/models") \
    .setInputCols(["caption_document", "image_assembler"]) \
    .setOutputCol("completions")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)
```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import com.johnsnowlabs.nlp.pretrained._
import org.apache.spark.ml.Pipeline

val prompt = """
Act as a senior clinical specialist and analyze this medical document. Perform the following steps in order:
1. Clinical Summary: Identify the patient's primary and secondary diagnoses, including any 'overlap' syndromes mentioned.
2. Medication Analysis Table: Create a table listing:
    * Medication Name
    * Dosage & Frequency
    * Clinical Justification: Explain why this specific drug is being used for this patient’s symptoms (e.g., link the vasodilators to the finger ulcers).
3. Conditional Logic & Alerts: Explicitly list any instructions that are 'prn' (as needed) or conditional (e.g., 'in case of...'). Identify any medications that require close monitoring for this patient's condition.
4. Visual Verification: Confirm if there are any handwritten notes or signatures that modify the printed instructions.
Please reason step-by-step before providing your final answer.
"""

val inputDf = VisionLLMPreprocessor(
  spark = spark,
  imagesPath = "images",
  prompt = prompt,
  outputColName = "prompt"
)

val documentAssembler = new DocumentAssembler()
  .setInputCol("prompt")
  .setOutputCol("caption_document")

val imageAssembler = new ImageAssembler()
  .setInputCol("image")
  .setOutputCol("image_assembler")

val medicalVisionLLM = MedicalVisionLLM
  .load("jsl_meds_vlm_reasoning_8b_q16_v1", "en", "clinical/models")
  .setInputCols(Array("caption_document", "image_assembler"))
  .setOutputCol("completions")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  imageAssembler,
  medicalVisionLLM
))

val model = pipeline.fit(inputDf)
val result = model.transform(inputDf)
```
</div>

## Results

```bash
Step-by-Step Analysis as a Senior Clinical Specialist  

1. Clinical Summary  
- Primary Diagnoses: Systemic Lupus Erythematosus (SLE) and scleroderma overlap syndrome (explicitly stated: "Known case of systemic lupus erythematosus and scleroderma overlap with interstitial lung disease").  
- Secondary Diagnoses:  
  - Interstitial lung disease (ILD) (part of the overlap syndrome).  
  - Digital ulcers and skin tightening (tightness of skin of the fists and ulcers on the pulp of the fingers—classic manifestations of scleroderma).  
- Key Overlap Syndrome: SLE-scleroderma overlap, which increases the risk of severe complications like ILD, Pulmonary Arterial Hypertension (PAH), and digital ischemia.

2. Medication Analysis Table  

--------------------------------------------------------------------------------------------------------------------------------------------------
| Medication Name        | Dosage & Frequency              | Clinical Justification                                                              |
| :----------------------| :-------------------------------| :-----------------------------------------------------------------------------------|
| Linzolid               | 600 mg twice daily for 5 days   | Conditional use for possible bacterial infection in non-healing finger ulcers.      |
| Clopidogrel            | 75 mg once daily after meals    | Antiplatelet therapy to prevent thrombosis in vascular complications or vasculitis. |
| Amlodipine             | 5 mg once daily                 | Vasodilator for hypertension or Raynaud’s phenomenon to improve digital perfusion.  |
| Domperidone            | 10 mg twice daily before meals  | Antiemetic to manage nausea from immunosuppressants or other GI side effects.       |
| Omeprazole             | 20 mg twice daily before meal   | Proton pump inhibitor (PPI) to protect gastric mucosa from corticosteroids/NSAIDs.  |
| Bosentan               | 62.5 mg twice daily             | Endothelin receptor antagonist for PAH (common in scleroderma).                     |
| Sildenafil Citrate     | 0.5 mg twice daily after meals  | PDE-5 inhibitor for PAH; dilates pulmonary vasculature to reduce pressure.          |
| Prednisolone           | 5 mg once daily after breakfast | Corticosteroid to suppress autoimmunity and control inflammation.                   |
| Mycophenolate Mofetil  | 500 mg twice daily (2 tablets)  | Immunosuppressant to treat SLE and scleroderma disease activity.                    |
| L-methylfolate Calcium | 400 μg once daily               | Folate supplement to mitigate deficiency from chronic inflammation/medication.      |
| Ciprofloxacin          | 250 mg twice daily              | Antibiotic for prophylaxis or treatment in an immunocompromised state.              |
--------------------------------------------------------------------------------------------------------------------------------------------------

3. Conditional Logic & Alerts  

Prn/Conditional Instructions  
- Linzolid: "as advised in detail in case the ulcers of the fingers do not heal" (only to be started if initial management fails).  
- Review after 4 weeks: Explicit follow-up to monitor response and safety.  

Medications Requiring Close Monitoring  

----------------------------------------------------------------------------------------------------
| Medication            | Monitoring Focus                                                         |
| :---------------------| :------------------------------------------------------------------------|
| Bosentan              | Liver function (transaminases), hemoglobin (anemia), and blood pressure. |
| Sildenafil            | Blood pressure (hypotension risk) and liver function.                    |
| Mycophenolate Mofetil | WBC count (infection risk), platelet count, and renal function.          |
| Prednisolone          | Bone density (osteoporosis), blood glucose, and blood pressure.          |
| Linzolid              | Liver function and screening for peripheral neuropathy.                  |
| Ciprofloxacin         | QT interval prolongation and monitoring for tendon pain/inflammation.    |
----------------------------------------------------------------------------------------------------

4. Visual Verification  
- The document is printed text with no handwritten notes or signatures visible. All instructions are part of the official outpatient summary.  

Final Answer  
1. Clinical Summary: Primary SLE-Scleroderma overlap with ILD and digital ulcers.  
2. Medication Analysis: Comprehensive regimen targeting inflammation, vascular issues (PAH/Raynaud's), and infection control.  
3. Conditional Logic & Alerts: Linzolid is conditional; high-risk monitoring for Bosentan and Mycophenolate is essential.  
4. Visual Verification: Printed instructions only; no handwritten modifications.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_reasoning_8b_q16_v1|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|13.5 GB|