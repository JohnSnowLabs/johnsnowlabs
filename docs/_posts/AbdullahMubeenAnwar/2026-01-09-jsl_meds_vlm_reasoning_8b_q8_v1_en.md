---
layout: model
title: JSL_MedS_VLM_Reasoning_v1 (8B - q8)
author: John Snow Labs
name: jsl_meds_vlm_reasoning_8b_q8_v1
date: 2026-01-09
tags: [medical, clinical, vlm, q8, 8b, en, licensed, llamacpp]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 6.3.0
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q8_v1_en_6.2.0_3.4_1767931170926.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q8_v1_en_6.2.0_3.4_1767931170926.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from sparknlp_jsl.utils import *
from pyspark.ml import Pipeline

prompt = """Analyze this clinical document. First, identify the primary diagnoses.
Then, list all prescribed medications and explain the clinical reasoning for why each medication was likely prescribed for this specific patient.
Finally, note any instructions that are conditional (e.g., 'only if...')."""

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

medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_reasoning_8b_q8_v1", "en", "clinical/models") \
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

prompt = """Analyze this clinical document. First, identify the primary diagnoses.
Then, list all prescribed medications and explain the clinical reasoning for why each medication was likely prescribed for this specific patient.
Finally, note any instructions that are conditional (e.g., 'only if...')."""

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

medicalVisionLLM = medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_reasoning_8b_q8_v1", "en", "clinical/models") \
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

val prompt = """Analyze this clinical document. First, identify the primary diagnoses.
Then, list all prescribed medications and explain the clinical reasoning for why each medication was likely prescribed for this specific patient.
Finally, note any instructions that are conditional (e.g., 'only if...')."""

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
  .pretrained("jsl_meds_vlm_reasoning_8b_q8_v1", "en", "clinical/models")
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
Clinical Document Analysis

1. Primary Diagnoses
The patient presents with a complex overlap of connective tissue diseases, specifically:
* Systemic Lupus Erythematosus (SLE)
* Scleroderma Overlap Syndrome (presenting with features of both SLE and Scleroderma)
* Interstitial Lung Disease (ILD)

Clinical Correlates: Symptoms such as skin tightness in the fists and finger pulp ulcers are classic manifestations of scleroderma-related vascular and cutaneous complications.

2. Medication Summary & Clinical Reasoning
-------------------------------------------------------------------------------------------------------------
| Medication            | Dosage       | Clinical Purpose                                                   |
| :-------------------- | :----------- | :----------------------------------------------------------------- |
| Mycophenolate Mofetil | 1000 mg BID  | Core immunosuppression to control autoimmune flares.               |
| Prednisolone          | 5 mg Daily   | Low-dose corticosteroid for ongoing inflammation management.       |
| Bosentan              | 62.5 mg BID  | Manages Pulmonary Arterial Hypertension (PAH) associated with ILD. |
| Sildenafil Citrate    | 0.5 mg BID   | Adjunct therapy to improve vascular blood flow in PAH.             |
| Clopidogrel           | 75 mg Daily  | Antiplatelet therapy to prevent thrombosis in compromised vessels. |
| Amlodipine            | 5 mg Daily   | Calcium channel blocker for hypertension and Raynaud’s management. |
| Linezolid             | 600 mg BID   | Conditional: Short-course antibiotic for infected finger ulcers.   |
| Ciprofloxacin         | 250 mg BID   | Antibiotic coverage/prophylaxis for immunosuppressed states.       |
| Omeprazole            | 20 mg BID    | Manages GERD/acid reflux caused by scleroderma-related GI issues.  |
| Domperidone           | 10 mg BID    | Promotes GI motility to counter esophageal/gastric dysfunction.    |
| L-methylfolate        | 400 µg Daily | Prevents folate deficiency secondary to long-term MMF use.         |
-------------------------------------------------------------------------------------------------------------

3. Critical Instructions
* Conditional Treatment: Linezolid should only be started if the digital ulcers fail to heal as expected.
* Follow-up: A clinical review is required in 4 weeks to assess treatment efficacy and disease progression.

Summary: This regimen follows a multidisciplinary approach, targeting immune suppression, vascular protection, and symptomatic relief for gastrointestinal complications.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_reasoning_8b_q8_v1|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|9.0 GB|