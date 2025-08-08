---
layout: model
title: JSL_MedS_VLM_v1 (3B - q4)
author: John Snow Labs
name: jsl_meds_vlm_3b_q4_v1
date: 2025-08-08
tags: [medical, clinical, vlm, q4, 3b, en, licensed, llamacpp]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_3b_q4_v1_en_6.1.0_3.0_1754665828278.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_vlm_3b_q4_v1_en_6.1.0_3.0_1754665828278.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.base import DocumentAssembler, ImageAssembler
from sparknlp_jsl.annotator import MedicalVisionLLM
from pyspark.sql.functions import lit
from pyspark.ml import Pipeline

!mkdir -p images
!wget -O images/prescription_01.png   "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_01.png"
!wget -O images/prescription_02.png   "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png"

from sparknlp_jsl.utils import *

prompt = """Extract demografig, clinical disease and medication informations"""

input_df = vision_llm_preprocessor(
    spark=spark,
    images_path="./images",
    prompt=prompt,
    output_col_name="prompt"
)

document_assembler = DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document")

image_assembler = ImageAssembler()\
    .setInputCol("image")\
    .setOutputCol("image_assembler")

medical_vision_llm = MedicalVisionLLM.pretrained("jsl_meds_vlm_3b_q4_v1", "en", "clinical/models")\
    .setInputCols(["document", "image_assembler"])\
    .setOutputCol("completions")\
    .setChatTemplate("vicuna")\
    .setBatchSize(4)\
    .setNGpuLayers(99)\
    .setNCtx(4096)\
    .setMinKeep(0)\
    .setMinP(0.05)\
    .setNPredict(-1)\
    .setNProbs(0)\
    .setPenalizeNl(False)\
    .setRepeatLastN(256)\
    .setRepeatPenalty(1.18)\
    .setStopStrings(["</s>", "User:"])\
    .setTemperature(0.05)\
    .setTfsZ(1)\
    .setTypicalP(1)\
    .setTopK(40)\
    .setTopP(0.95)

pipeline = Pipeline().setStages([
    document_assembler,
    image_assembler,
    medical_vision_llm
])

result = pipeline.fit(input_df).transform(input_df)

result.selectExpr(
    "reverse(split(image.origin, '/')) as image_name", "completions.result"
).show(truncate=False)

```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

!mkdir -p images

!wget -O images/prescription_01.png   "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_01.png"
!wget -O images/prescription_02.png   "https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/healthcare-nlp/data/ocr/prescription_02.png"

prompt = """Extract demografig, clinical disease and medication informations"""

data = nlp.ImageAssembler.loadImagesAsBytes(spark, '/content/images')
data = data.withColumn("caption", lit(prompt))

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("caption")
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

model = pipeline.fit(data)
result = model.transform(data)

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

The outpatient summary provided in the document indicates that Ms. Rukhsana Shaheen is 56 years old and female. She has been diagnosed with systemic lupus erythematosus (SLE) along with scleroderma overlap syndrome due to interstitial lung disease on medications. Her current symptoms include tightness of skin around her fists and ulcers appearing at the pulp area of her fingers. The treatment advised includes:

    1. Sildenafil Citrate - 0.5 mg twice daily for five days as an initial step before switching to Prednisone once ulceration does not heal within two weeks.
    2. Mycophenolate Mofetil - 500mg tablets taken twice per day after breakfast.
    3. Clopidogrel - 75mg tablet given every morning until溃疡 heals completely or if there's no improvement over four weeks.
    4. L-Methylfolate Calcium - 400ug one tablet each time it’s mealtime. These treatments aim to manage both conditions effectively while minimizing side effects from long-term steroid use which could potentially lead to complications such as osteoporosis or infections like those mentioned above.

Please note this information should be reviewed by a healthcare professional prior to implementation based upon individual patient needs, medical history, response to previous therapies etc.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_vlm_3b_q4_v1|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[caption_document, image_assembler]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|2.6 GB|
