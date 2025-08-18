---
layout: model
title: Pipeline to JSL_MedS_NER_VLM_v2 (VLM - 2b - q16)
author: John Snow Labs
name: jsl_meds_ner_vlm_2b_q16_v2_pipeline
date: 2025-08-16
tags: [licensed, en, clinical, meds, vlm, ner]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is a built on top of the [jsl_meds_ner_vlm_2b_q16_v2](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_vlm_2b_q16_v2_pipeline_en_6.1.0_3.4_1755355815327.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_vlm_2b_q16_v2_pipeline_en_6.1.0_3.4_1755355815327.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline
from sparknlp_jsl.utils import vision_llm_preprocessor

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

pipeline = PretrainedPipeline("jsl_meds_ner_vlm_2b_q16_v2_pipeline", "en", "clinical/models")
result = pipeline.transform(input_df)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp

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

pipeline = nlp.PretrainedPipeline("jsl_meds_ner_vlm_2b_q16_v2_pipeline", "en", "clinical/models")
result = pipeline.transform(input_df)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline
import com.johnsnowlabs.nlp.util.VisionLLMPreprocessor

val prompt = """
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

val inputDF = VisionLLMPreprocessor(
  spark = spark,
  imagesPath = "images",
  prompt = prompt,
  outputColName = "prompt"
)

val pipeline = new PretrainedPipeline("jsl_meds_ner_vlm_2b_q16_v2_pipeline", "en", "clinical/models")
val result = pipeline.transform(inputDF)
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
|Model Name:|jsl_meds_ner_vlm_2b_q16_v2_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.5 GB|

## Included Models

- DocumentAssembler
- ImageAssembler
- MedicalVisionLLM