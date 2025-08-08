---
layout: model
title: JSL_MedS_VLM_v1 (VLM - 3b - q8)
author: John Snow Labs
name: jsl_meds_vlm_3b_q8_v1
date: 2025-08-08
tags: [medical, clinical, vlm, q8, 3b, en, licensed, llamacpp]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_3b_q8_v1_en_6.1.0_3.0_1754686030561.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_3b_q8_v1_en_6.1.0_3.0_1754686030561.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler, ImageAssembler
from sparknlp_jsl.utils import vision_llm_preprocessor
from sparknlp_jsl.annotator import MedicalVisionLLM
from pyspark.ml import Pipeline

!mkdir -p images

!wget -O images/prescription_01.png -q "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_01.png"
!wget -O images/prescription_02.png -q "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png"
 
prompt = """Extract demografig, clinical disease and medication informations"""
 
input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = (
    DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("caption_document")
)

image_assembler = (
    ImageAssembler()
    .setInputCol("image")
    .setOutputCol("image_assembler")
)

medicalVisionLLM = (
    MedicalVisionLLM.pretrained("jsl_meds_vlm_3b_q4_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
    .setChatTemplate("vicuna")
    .setBatchSize(4)
    .setNGpuLayers(99)
    .setNCtx(4096)
    .setMinKeep(0)
    .setMinP(0.05)
    .setNPredict(-1)
    .setNProbs(0)
    .setPenalizeNl(False)
    .setRepeatLastN(256)
    .setRepeatPenalty(1.18)
    .setStopStrings(["</s>", "User:"])
    .setTemperature(0.05)
    .setTfsZ(1)
    .setTypicalP(1)
    .setTopK(40)
    .setTopP(0.95)
)

pipeline = Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)

result.selectExpr(
    "reverse(split(image.origin, '/')) as image_name", "completions.result"
).show(truncate=False)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

!mkdir -p images

!wget -O images/prescription_01.png -q "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_01.png"
!wget -O images/prescription_02.png -q "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png"
 
prompt = """Extract demografig, clinical disease and medication informations"""
 
input_df = nlp.vision_llm_preprocessor(
    spark=spark,
    images_path="images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("caption_document")
)

image_assembler = (
    nlp.ImageAssembler()
    .setInputCol("image")
    .setOutputCol("image_assembler")
)

medicalVisionLLM = (
    medical.MedicalVisionLLM.pretrained("jsl_meds_vlm_3b_q4_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
    .setChatTemplate("vicuna")
    .setBatchSize(4)
    .setNGpuLayers(99)
    .setNCtx(4096)
    .setMinKeep(0)
    .setMinP(0.05)
    .setNPredict(-1)
    .setNProbs(0)
    .setPenalizeNl(False)
    .setRepeatLastN(256)
    .setRepeatPenalty(1.18)
    .setStopStrings(["</s>", "User:"])
    .setTemperature(0.05)
    .setTfsZ(1)
    .setTypicalP(1)
    .setTopK(40)
    .setTopP(0.95)
)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    image_assembler,
    medicalVisionLLM
])

model = pipeline.fit(input_df)
result = model.transform(input_df)

result.selectExpr(
    "reverse(split(image.origin, '/')) as image_name", "completions.result"
).show(truncate=False)

```
```scala

import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

import sys.process._
"mkdir -p images".!
"wget -O images/prescription_01.png https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_01.png".!
"wget -O images/prescription_02.png https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png".!

val prompt = """Extract demografig, clinical disease and medication informations"""

val data = ImageAssembler.loadImagesAsBytes(spark, "/content/images")
  .withColumn("caption", lit(prompt))

val documentAssembler = new DocumentAssembler()
  .setInputCol("caption")
  .setOutputCol("caption_document")

val imageAssembler = new ImageAssembler()
  .setInputCol("image")
  .setOutputCol("image_assembler")

val medicalVisionLLM = MedicalVisionLLM
  .pretrained("jsl_meds_vlm_3b_q4_v1", "en", "clinical/models")
  .setInputCols(Array("caption_document", "image_assembler"))
  .setOutputCol("completions")
  .setChatTemplate("vicuna")
  .setBatchSize(4)
  .setNGpuLayers(99)
  .setNCtx(4096)
  .setMinKeep(0)
  .setMinP(0.05)
  .setNPredict(-1)
  .setNProbs(0)
  .setPenalizeNl(false)
  .setRepeatLastN(256)
  .setRepeatPenalty(1.18f)
  .setStopStrings(Array("</s>", "User:"))
  .setTemperature(0.05f)
  .setTfsZ(1f)
  .setTypicalP(1f)
  .setTopK(40)
  .setTopP(0.95f)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  imageAssembler,
  medicalVisionLLM
))

val model = pipeline.fit(data)
val result = model.transform(data)

result.selectExpr(
  "reverse(split(image.origin, '/'))[0] as image_name",
  "completions.result"
).show(false)

```
</div>

## Results

```bash

The document you provided is an outpatient summary from the Department of Rheumatology at Human Care Medical Charitable Trust. Here's the extracted information:

Demographic Information:
    Name: Ms Rukhsana Shaheen
    Age / Sex: 56 yrs / Female

Clinical Disease Information:
    Disease Diagnosis: Systemic Lupus Erythematosus (SLE) with Scleroderma overlap syndrome.
    Additional Conditions: Interstitial Lung Disease on Medication.

Medications Prescribed:
    Systemic Steroids:
        Prednisolone 0.5 mg twice daily
    Antimalarials:
        Mycophenolate mofetil 500 mg two tablets before meals
    Immunosuppressants:
        Azathioprine 75 mg once daily after breakfast
    Antiplatelet Agents:
        Clopidogrel 75 mg once daily
    Corticosteroid Injections:
        Triamcinolone acetonide injection in finger joints as needed for flare-ups
    Other Medications:
        L-Methylfolate calcium 400 µg one tablet per day
        Amlodipine 5 mg once a day
        Ciprofloxacin 250 mg twice a day
        Other medications not specified but likely related to systemic lupus erythematosus management such as methotrexate or cyclophosphamide depending on the severity of symptoms

This summary provides an overview of Ms Rukhsana Shaheen's medical condition along with her current treatment regimen under the care of Dr Darshan Singh Bhakuni at Human Care Medical Charitable Trust.

If you need further details about any specific medication or if there are additional questions regarding this information, please let me know!

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_3b_q8_v1|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[caption_document, image_assembler]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|3.9 GB|