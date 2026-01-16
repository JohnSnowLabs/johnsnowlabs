---
layout: model
title: JSL_MedS_VLM_v1 (VLM - 7b - q8)
author: John Snow Labs
name: jsl_meds_vlm_7b_q8_v1
date: 2025-12-17
tags: [medical, clinical, vlm, q8, 7b, en, licensed, llamacpp]
task: Text Generation
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.0
supported: true
engine: llamacpp
annotator: MedicalVisionLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This multimodal medical reasoning model is trained to interpret medical images and textual data, generate structured internal reasoning traces, and deliver accurate clinical insights.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_7b_q8_v1_en_6.2.0_3.0_1765979442861.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_7b_q8_v1_en_6.2.0_3.0_1765979442861.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler, ImageAssembler
from sparknlp_jsl.annotator import MedicalVisionLLM
from sparknlp_jsl.utils import vision_llm_preprocessor
from pyspark.ml import Pipeline

prompt = """
Given the attached chest X-ray image and the patient’s clinical notes below, determine the most likely diagnosis, list two key differential diagnoses, and recommend the next appropriate diagnostic step.
Clinical notes: A 62-year-old male with a 40-pack-year smoking history presents with progressive dyspnea, chronic cough, unintentional weight loss, and occasional hemoptysis. Vital signs are stable. No prior imaging is available.
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

medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q8_v1", "en", "clinical/models") \
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
Given the attached chest X-ray image and the patient’s clinical notes below, determine the most likely diagnosis, list two key differential diagnoses, and recommend the next appropriate diagnostic step.
Clinical notes: A 62-year-old male with a 40-pack-year smoking history presents with progressive dyspnea, chronic cough, unintentional weight loss, and occasional hemoptysis. Vital signs are stable. No prior imaging is available.
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

medicalVisionLLM = medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q8_v1", "en", "clinical/models") \
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
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.ImageAssembler
import com.johnsnowlabs.nlp.jsl.annotators.MedicalVisionLLM
import com.johnsnowlabs.nlp.jsl.utils.VisionLLMPreprocessor
import org.apache.spark.ml.Pipeline

val prompt =
  """
    |Given the attached chest X-ray image and the patient’s clinical notes below, determine the most likely diagnosis, list two key differential diagnoses, and recommend the next appropriate diagnostic step.
    |Clinical notes: A 62-year-old male with a 40-pack-year smoking history presents with progressive dyspnea, chronic cough, unintentional weight loss, and occasional hemoptysis. Vital signs are stable. No prior imaging is available.
  """.stripMargin

val inputDF = VisionLLMPreprocessor.preprocess(
  spark,
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

val medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q8_v1", "en", "clinical/models")
  .setInputCols(Array("caption_document", "image_assembler"))
  .setOutputCol("completions")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  imageAssembler,
  medicalVisionLLM
))

val model = pipeline.fit(inputDF)
val result = model.transform(inputDF)
```
</div>

## Results

```bash
Most Likely Diagnosis: Lung cancer  

Differential Diagnoses:
1. Chronic obstructive pulmonary disease (COPD) exacerbation  
2. Tuberculosis (TB)  

Next Diagnostic Step:
- Contrast-enhanced chest CT scan to evaluate for masses, lymphadenopathy, or subtle parenchymal abnormalities.  
- Consider sputum cytology and/or bronchoscopy if a mass is identified.  
- Tuberculin skin test or interferon-gamma release assay (IGRA) to rule out TB.  

Additional Notes:
- The patient’s significant smoking history, progressive symptoms, and hemoptysis strongly favor malignancy.  
- TB should be considered given weight loss and hemoptysis, but is less likely without fever or night sweats.  
- COPD may contribute to chronic symptoms but does not explain weight loss or hemoptysis.  

This approach balances the need for urgent evaluation of malignancy while considering other possibilities.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_7b_q8_v1|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[caption_document, image_assembler]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|8.9 GB|