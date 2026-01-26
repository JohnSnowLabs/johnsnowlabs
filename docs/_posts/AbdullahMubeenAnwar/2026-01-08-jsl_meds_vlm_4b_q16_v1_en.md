---
layout: model
title: JSL_MedS_VLM_v1 (4B - q16)
author: John Snow Labs
name: jsl_meds_vlm_4b_q16_v1
date: 2026-01-08
tags: [medical, clinical, vlm, q16, 4b, en, licensed, llamacpp]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q16_v1_en_6.2.0_3.4_1767907642577.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_4b_q16_v1_en_6.2.0_3.4_1767907642577.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp_jsl.annotator import *
from sparknlp_jsl.utils import *
from pyspark.ml import Pipeline

prompt = """
Extract from the document and return strictly as JSON:

{
  "patient": {"name": string, "age": string, "sex": string, "hospital_no": string, "episode_no": string, "episode_date": string},
  "diagnoses": [string],
  "symptoms": [string],
  "treatment": [{"med": string, "dose": string, "freq": string}]
}
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

medicalVisionLLM = MedicalVisionLLM.pretrained("jsl_meds_vlm_4b_q16_v1", "en", "clinical/models") \
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
Extract from the document and return strictly as JSON:

{
  "patient": {"name": string, "age": string, "sex": string, "hospital_no": string, "episode_no": string, "episode_date": string},
  "diagnoses": [string],
  "symptoms": [string],
  "treatment": [{"med": string, "dose": string, "freq": string}]
}
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

medicalVisionLLM = medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_4b_q16_v1", "en", "clinical/models") \
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
Extract from the document and return strictly as JSON:

{
  "patient": {"name": string, "age": string, "sex": string, "hospital_no": string, "episode_no": string, "episode_date": string},
  "diagnoses": [string],
  "symptoms": [string],
  "treatment": [{"med": string, "dose": string, "freq": string}]
}
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
  .pretrained("jsl_meds_vlm_4b_q16_v1", "en", "clinical/models")
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
  "patient": {
    "name": "Ms RUKHSANA SHAHEEN",
    "age": "56 yrs",
    "sex": "Female",
    "hospital_no": "MH005990453",
    "episode_no": "030000528270",
    "episode_date": "02/07/2021 08:31AM"
  },
  "diagnoses": ["systemic lupus erythematosus", "scleroderma overlap", "interstitial lung disease"],
  "symptoms": ["tightness of skin of the fists", "ulcers on the pulp of the fingers"],
  "treatment": [
    {"med": "Linezolid", "dose": "600 mg", "freq": "twice a day for 5 Days"},
    {"med": "Clopidogrel", "dose": "75 mg", "freq": "once a day after meals"},
    {"med": "Amlodipine", "dose": "5 mg", "freq": "once a day"},
    {"med": "Domperidone", "dose": "10 mg", "freq": "twice a day before meals"},
    {"med": "Omeprazole", "dose": "20 Mg", "freq": "Twice a Day before Meal"},
    {"med": "Bosentan", "dose": "62.5 mg", "freq": "twice a day after meals"},
    {"med": "Sildenafil Citrate", "dose": "0.5 mg", "freq": "twice a day after meals"},
    {"med": "Prednisolone", "dose": "5 mg", "freq": "once a day after breakfast"},
    {"med": "Mycophenolate mofetil", "dose": "500 mg 2 tablets", "freq": "twice a day"},
    {"med": "L-methylfolate calcium", "dose": "400 µg 1 tablet", "freq": "once a day"},
    {"med": "ciprofloxacin", "dose": "250 mg", "freq": "twice a day"}
  ]
}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_4b_q16_v1|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[image, document]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|6.8 GB|