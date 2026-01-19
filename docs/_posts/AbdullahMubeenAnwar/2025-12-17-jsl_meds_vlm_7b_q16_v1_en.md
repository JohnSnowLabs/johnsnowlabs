---
layout: model
title: JSL_MedS_VLM_v1 (VLM - 7b - q16)
author: John Snow Labs
name: jsl_meds_vlm_7b_q16_v1
date: 2025-12-17
tags: [medical, clinical, vlm, q16, 7b, en, licensed, llamacpp]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_7b_q16_v1_en_6.2.0_3.0_1765978015987.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_7b_q16_v1_en_6.2.0_3.0_1765978015987.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q16_v1", "en", "clinical/models") \
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

medicalVisionLLM = medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q16_v1", "en", "clinical/models") \
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

val medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_7b_q16_v1", "en", "clinical/models")
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
Most Likely Diagnosis:
Lung cancer (non-small cell lung cancer, likely squamous cell carcinoma given the smoking history and hemoptysis).  

Key Differential Diagnoses: 
1. Tuberculosis (TB): Chronic cough, weight loss, and hemoptysis can mimic TB, but the absence of upper lobe cavitation or calcified lymph nodes on imaging makes this less likely.  
2. Chronic Obstructive Pulmonary Disease (COPD): The patient’s smoking history and chronic cough raise suspicion, but COPD typically presents with hyperinflation and flattened diaphragms on imaging, which are not evident here.  

Next Diagnostic Step:
1. Contrast-enhanced CT scan of the chest: To better characterize the right mid-lung opacity, assess for lymphadenopathy, and evaluate for metastatic disease.  
2. Sputum cytology and bronchoscopy: To obtain tissue diagnosis if the lesion is accessible.  
3. PET-CT scan:*To evaluate for metastatic spread if malignancy is confirmed.  

Additional considerations:  
- Pulmonary function tests (PFTs): To assess for underlying COPD or restrictive lung disease.  
- Tuberculin skin test (TST) or interferon-gamma release assay (IGRA): To rule out latent or active TB.  
- Complete blood count (CBC) and inflammatory markers: To evaluate for infection or systemic inflammation.  

This approach prioritizes confirming malignancy while ruling out other chronic pulmonary conditions.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_7b_q16_v1|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[caption_document, image_assembler]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|13.2 GB|