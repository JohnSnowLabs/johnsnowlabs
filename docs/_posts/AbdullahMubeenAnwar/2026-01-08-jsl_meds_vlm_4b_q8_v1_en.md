---
layout: model
title: JSL_MedS_VLM_v1 (4B - q8)
author: John Snow Labs
name: jsl_meds_vlm_4b_q8_v1
date: 2026-01-08
tags: [medical, clinical, vlm, q8, 4b, en, licensed, llamacpp]
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

This vision-language model is trained to understand medical images and extract key details such as patient demographics, clinical conditions, and prescribed medications, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q8_v1_en_6.2.0_3.4_1767909380535.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q8_v1_en_6.2.0_3.4_1767909380535.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from sparknlp_jsl.utils import *
from pyspark.ml import Pipeline

prompt = """Based only on the information visible in this document, identify the patient’s primary diagnoses,
current presenting symptoms, and the complete treatment plan.
For the treatment plan, list each medication with its dose, frequency, timing in relation to meals, and duration if specified.
Also state the consulting department, consulting doctor, and the recommended follow-up interval."""

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

medicalVisionLLM = MedicalVisionLLM.load("jsl_meds_vlm_4b_q8_v1", "en", "clinical/models") \
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

prompt = """Based only on the information visible in this document, identify the patient’s primary diagnoses,
current presenting symptoms, and the complete treatment plan.
For the treatment plan, list each medication with its dose, frequency, timing in relation to meals, and duration if specified.
Also state the consulting department, consulting doctor, and the recommended follow-up interval."""

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

medicalVisionLLM = medical.MedicalVisionLLM.load("jsl_meds_vlm_4b_q8_v1", "en", "clinical/models") \
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

val prompt = """Based only on the information visible in this document, identify the patient’s primary diagnoses,
current presenting symptoms, and the complete treatment plan.
For the treatment plan, list each medication with its dose, frequency, timing in relation to meals, and duration if specified.
Also state the consulting department, consulting doctor, and the recommended follow-up interval."""

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
  .load("jsl_meds_vlm_4b_q8_v1", "en", "clinical/models")
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
Based on the information visible in the document, the patient has systemic lupus erythematosus with scleroderma overlap and interstitial lung disease, is currently presenting with tightness of the skin of the fists and ulcers on the pulp of the fingers, and has been advised treatment including linezolid 600 mg twice daily for 5 days if the ulcers do not heal, clopidogrel 75 mg once daily after meals, amlodipine 5 mg once daily, domperidone 10 mg twice daily before meals, omeprazole 20 mg twice daily before meals, bosentan 62.5 mg twice daily after meals, sildenafil citrate 0.5 mg twice daily after meals, prednisolone 5 mg once daily after breakfast, mycophenolate mofetil 500 mg two tablets twice daily, L-methylfolate calcium 400 µg once daily, and ciprofloxacin 250 mg twice daily, with care provided by the Rheumatology department under Dr. Darshan Singh Bhakuni and a recommended follow up after 4 weeks.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_4b_q8_v1|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|4.5 GB|