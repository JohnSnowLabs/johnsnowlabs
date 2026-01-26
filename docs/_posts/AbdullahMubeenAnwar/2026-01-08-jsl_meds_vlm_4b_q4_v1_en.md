---
layout: model
title: JSL_MedS_VLM_v1 (4B - q4)
author: John Snow Labs
name: jsl_meds_vlm_4b_q4_v1
date: 2026-01-08
tags: [medical, clinical, vlm, q4, 4b, en, licensed, llamacpp]
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

This vision-language model is trained to understand medical images and extract key details such as patient demographics, clinical conditions, and prescribed medications, etc.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q4_v1_en_6.2.0_3.4_1767910605414.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q4_v1_en_6.2.0_3.4_1767910605414.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from sparknlp_jsl.utils import *
from pyspark.ml import Pipeline

prompt = """
Based only on the information visible in this document, extract the following details and return the result strictly as a valid JSON object. Do not include any explanatory text.

The JSON must follow this structure:

{
  "patient_info": {
    "name": string,
    "age": string,
    "sex": string,
    "hospital_number": string,
    "episode_number": string,
    "episode_date_time": string
  },
  "primary_diagnoses": [string],
  "presenting_symptoms": [string],
  "treatment_plan": [
    {
      "medication_name": string,
      "dose": string,
      "frequency": string,
      "timing_with_meals": string,
      "duration": string
    }
  ],
  "consultation": {
    "department": string,
    "doctor": string
  },
  "recommended_follow_up_interval": string
}

Rules:
- Use only information explicitly present in the document.
- Do not infer, assume, or normalize clinical details beyond what is written.
- Keep medication names, doses, frequencies, and timing exactly as stated in the document.
- Do not infer indications or durations for medications unless explicitly stated.
- If a field is not specified in the document, use null.
- Arrays must be empty ([]) if no items are found.
- Ensure the output is valid JSON and nothing else.
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

medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_4b_q4_v1", "en", "clinical/models") \
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
Based only on the information visible in this document, extract the following details and return the result strictly as a valid JSON object. Do not include any explanatory text.

The JSON must follow this structure:

{
  "patient_info": {
    "name": string,
    "age": string,
    "sex": string,
    "hospital_number": string,
    "episode_number": string,
    "episode_date_time": string
  },
  "primary_diagnoses": [string],
  "presenting_symptoms": [string],
  "treatment_plan": [
    {
      "medication_name": string,
      "dose": string,
      "frequency": string,
      "timing_with_meals": string,
      "duration": string
    }
  ],
  "consultation": {
    "department": string,
    "doctor": string
  },
  "recommended_follow_up_interval": string
}

Rules:
- Use only information explicitly present in the document.
- Do not infer, assume, or normalize clinical details beyond what is written.
- Keep medication names, doses, frequencies, and timing exactly as stated in the document.
- Do not infer indications or durations for medications unless explicitly stated.
- If a field is not specified in the document, use null.
- Arrays must be empty ([]) if no items are found.
- Ensure the output is valid JSON and nothing else.
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

medicalVisionLLM = medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_4b_q4_v1", "en", "clinical/models") \
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
Based only on the information visible in this document, extract the following details and return the result strictly as a valid JSON object. Do not include any explanatory text.

The JSON must follow this structure:

{
  "patient_info": {
    "name": string,
    "age": string,
    "sex": string,
    "hospital_number": string,
    "episode_number": string,
    "episode_date_time": string
  },
  "primary_diagnoses": [string],
  "presenting_symptoms": [string],
  "treatment_plan": [
    {
      "medication_name": string,
      "dose": string,
      "frequency": string,
      "timing_with_meals": string,
      "duration": string
    }
  ],
  "consultation": {
    "department": string,
    "doctor": string
  },
  "recommended_follow_up_interval": string
}

Rules:
- Use only information explicitly present in the document.
- Do not infer, assume, or normalize clinical details beyond what is written.
- Keep medication names, doses, frequencies, and timing exactly as stated in the document.
- Do not infer indications or durations for medications unless explicitly stated.
- If a field is not specified in the document, use null.
- Arrays must be empty ([]) if no items are found.
- Ensure the output is valid JSON and nothing else.
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
  .pretrained("jsl_meds_vlm_4b_q4_v1", "en", "clinical/models")
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
{
  "patient_info": {
    "name": "Ms RUKHSANA SHAHEEN",
    "age": "56 yrs",
    "sex": "Female",
    "hospital_number": "MH005990453",
    "episode_number": "030000528270",
    "episode_date_time": "02/07/2021 08:31AM"
  },
  "primary_diagnoses": [
    "systemic lupus erythematosus and scleroderma overlap with interstitial lung disease on medication"
  ],
  "presenting_symptoms": [
    "tightness of skin of the fists and ulcers on the pulp of the fingers"
  ],
  "treatment_plan": [
    {
      "medication_name": "Linezolid",
      "dose": "600 mg",
      "frequency": "twice a day",
      "timing_with_meals": null,
      "duration": "for 5 Days as advised in detail in case the ulcers of the fingers do not heal"
    },
    {
      "medication_name": "Clopidogrel",
      "dose": "75 mg",
      "frequency": "once a day",
      "timing_with_meals": "after meals",
      "duration": null
    },
    {
      "medication_name": "Amlodipine",
      "dose": "5 mg",
      "frequency": "once a day",
      "timing_with_meals": null,
      "duration": null
    },
    {
      "medication_name": "Domperidone",
      "dose": "10 mg",
      "frequency": "twice a day",
      "timing_with_meals": "before meals",
      "duration": null
    },
    {
      "medication_name": "Omeprazole",
      "dose": "20 Mg",
      "frequency": "Twice a Day",
      "timing_with_meals": "before Meal",
      "duration": null
    },
    {
      "medication_name": "Bosentan",
      "dose": "62.5 mg",
      "frequency": "twice a day",
      "timing_with_meals": "after meals",
      "duration": null
    },
    {
      "medication_name": "Sildenafil Citrate",
      "dose": "0.5 mg",
      "frequency": "twice a day",
      "timing_with_meals": "after meals",
      "duration": null
    },
    {
      "medication_name": "Prednisolone",
      "dose": "5 mg",
      "frequency": "once a day",
      "timing_with_meals": "after breakfast",
      "duration": null
    },
    {
      "medication_name": "Mycophenolate mofetil",
      "dose": "500 mg 2 tablets",
      "frequency": "twice a day",
      "timing_with_meals": null,
      "duration": null
    },
    {
      "medication_name": "L-methylfolate calcium",
      "dose": "400 µg 1 tablet",
      "frequency": "once a day",
      "timing_with_meals": null,
      "duration": null
    },
    {
      "medication_name": "ciprofloxacin",
      "dose": "250 mg",
      "frequency": "twice a day",
      "timing_with_meals": null,
      "duration": null
    }
  ],
  "consultation": {
    "department": "RHEUMATOLOGY MHD",
    "doctor": "DR DARSHAN SINGH BHAKUNI"
  },
  "recommended_follow_up_interval": "Review after 4 weeks"
}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_4b_q4_v1|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.9 GB|