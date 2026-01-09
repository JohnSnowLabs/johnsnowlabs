---
layout: model
title: JSL_MedS_VLM_Reasoning_v1 (8B - q4)
author: John Snow Labs
name: jsl_meds_vlm_reasoning_8b_q4_v1
date: 2026-01-09
tags: [medical, clinical, vlm, q4, 8b, en, licensed, llamacpp]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q4_v1_en_6.2.0_3.4_1767931711129.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_reasoning_8b_q4_v1_en_6.2.0_3.4_1767931711129.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

medicalVisionLLM = MedicalVisionLLM.load("jsl_meds_vlm_reasoning_8b_q4_v1", "en", "clinical/models") \
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

medicalVisionLLM = medical.MedicalVisionLLM.load("jsl_meds_vlm_reasoning_8b_q4_v1", "en", "clinical/models") \
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
  .load("jsl_meds_vlm_reasoning_8b_q4_v1", "en", "clinical/models")
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
Clinical Analysis: SLE & Scleroderma Overlap

1. Primary Diagnoses
The patient presents with an Overlap Syndrome involving:
* Systemic Lupus Erythematosus (SLE)
* Scleroderma (indicated by skin tightness and finger pulp ulcers)
* Interstitial Lung Disease (ILD) (a secondary complication of the overlap)

2. Medication Summary & Clinical Reasoning
--------------------------------------------------------------------------------------------------------
| Medication            | Dosage       | Clinical Reasoning                                            |
| :-------------------- | :----------- | :------------------------------------------------------------ |
| Mycophenolate Mofetil | 1000 mg BID  | Primary immunosuppressant to prevent organ damage/flares.     |
| Prednisolone          | 5 mg Daily   | Low-dose steroid to manage active immune inflammation.        |
| Bosentan              | 62.5 mg BID  | Endothelin antagonist for Pulmonary Hypertension (PAH).       |
| Sildenafil Citrate    | 0.5 mg BID   | PDE5 inhibitor used as adjunct therapy for PAH management.    |
| Clopidogrel           | 75 mg Daily  | Antiplatelet to prevent thrombosis in damaged microvessels.   |
| Amlodipine            | 5 mg Daily   | Vasodilator for Raynaud’s phenomenon and skin ischemia.       |
| Linezolid             | 600 mg BID   | Conditional: Antibiotic if finger ulcers fail to heal.        |
| Ciprofloxacin         | 250 mg BID   | Prophylactic antibiotic coverage for immunosuppressed state.  |
| Omeprazole            | 20 mg BID    | PPI to manage GERD/reflux caused by esophageal involvement.   |
| Domperidone           | 10 mg BID    | Prokinetic to improve GI motility and reduce nausea.          |
| L-methylfolate        | 400 µg Daily | Supports cellular health and counters drug-induced deficiency.|
--------------------------------------------------------------------------------------------------------

3. Critical Instructions
* Conditional Use: Linezolid should only be initiated if the digital ulcers do not show signs of healing.
* Monitoring: Patient review is required in 4 weeks to evaluate the healing of ulcers and the effectiveness of the PAH/ILD regimen.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_reasoning_8b_q4_v1|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|5.6 GB|