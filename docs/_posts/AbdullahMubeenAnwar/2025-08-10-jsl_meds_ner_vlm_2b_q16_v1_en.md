---
layout: model
title: JSL_MedS_NER_VLM_v1 (VLM - 2b - q16)
author: John Snow Labs
name: jsl_meds_ner_vlm_2b_q16_v1
date: 2025-08-10
tags: [medical, clinical, vlm, q16, 2b, en, licensed, llamacpp]
task: Named Entity Recognition
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_vlm_2b_q16_v1_en_6.1.0_3.0_1754841306490.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_vlm_2b_q16_v1_en_6.1.0_3.0_1754841306490.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

prompt = """
# Template:
{
  "Patient Name": "string",
  "Patient Age": "integer",
  "Patient Gender": "string",
  "Hospital Number": "string",
  "Episode Number": "string",
  "Episode Date": "date-time"
}
# Context:
<image>
"""

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
    MedicalVisionLLM.pretrained("jsl_meds_ner_vlm_2b_q16_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
    .setChatTemplate("")
    .setBatchSize(4)
    .setNGpuLayers(99)
    .setNCtx(4096)
    .setNPredict(512)
    .setTemperature(0.0)
    .setTopK(1)
    .setTopP(1)
    .setRepeatLastN(256)
    .setRepeatPenalty(1.1)
    .setStopStrings(["</s>", "User:", "<|im_start|>"])
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

prompt = """
# Template:
{
  "Patient Name": "string",
  "Patient Age": "integer",
  "Patient Gender": "string",
  "Hospital Number": "string",
  "Episode Number": "string",
  "Episode Date": "date-time"
}
# Context:
<image>
"""

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
    medical.MedicalVisionLLM.pretrained("jsl_meds_ner_vlm_2b_q16_v1", "en", "clinical/models")
    .setInputCols(["caption_document", "image_assembler"])
    .setOutputCol("completions")
    .setChatTemplate("")
    .setBatchSize(4)
    .setNGpuLayers(99)
    .setNCtx(4096)
    .setNPredict(512)
    .setTemperature(0.0)
    .setTopK(1)
    .setTopP(1)
    .setRepeatLastN(256)
    .setRepeatPenalty(1.1)
    .setStopStrings(["</s>", "User:", "<|im_start|>"])
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

val prompt = """
prompt = """
# Template:
{
  "Patient Name": "string",
  "Patient Age": "integer",
  "Patient Gender": "string",
  "Hospital Number": "string",
  "Episode Number": "string",
  "Episode Date": "date-time"
}
# Context:
<image>
"""
"""

val data = ImageAssembler.loadImagesAsBytes(spark, "/content/images")
  .withColumn("caption", lit(prompt))

val documentAssembler = new DocumentAssembler()
  .setInputCol("caption")
  .setOutputCol("caption_document")

val imageAssembler = new ImageAssembler()
  .setInputCol("image")
  .setOutputCol("image_assembler")

val medicalVisionLLM = MedicalVisionLLM
  .pretrained("jsl_meds_ner_vlm_2b_q16_v1", "en", "clinical/models")
  .setInputCols(Array("caption_document", "image_assembler"))
  .setOutputCol("completions")
  .setChatTemplate("")
  .setBatchSize(4)
  .setNGpuLayers(99)
  .setNCtx(4096)
  .setNPredict(512)
  .setTemperature(0.0f)
  .setTopK(1)
  .setTopP(1f)
  .setRepeatLastN(256)
  .setRepeatPenalty(1.1f)
  .setStopStrings(["</s>", "User:", "<|im_start|>"])

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

{
    "Patient Name": "Ms RUKHSANA SHAHEEN",
    "Patient Age": 56,
    "Patient Gender": "Female",
    "Hospital Number": "MH005990453",
    "Episode Number": "030000528270",
    "Episode Date": "2021-07-02T08:31:00"
}

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_vlm_2b_q16_v1|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[caption_document, image_assembler]|
|Output Labels:|[completions]|
|Language:|en|
|Size:|3.5 GB|