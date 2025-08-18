---
layout: model
title: Pipeline to JSL_MedS_NER_v2 (LLM - 2b - q16)
author: John Snow Labs
name: jsl_meds_ner_2b_q16_v2_pipeline
date: 2025-08-16
tags: [licensed, en, clinical, meds, llm, ner]
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

This pretrained pipeline is a text-only version built on top of the [jsl_meds_ner_vlm_2b_q16_v2](https://nlp.johnsnowlabs.com/2025/08/10/jsl_meds_ner_vlm_2b_q16_v2_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q16_v2_pipeline_en_6.1.0_3.4_1755316162690.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_2b_q16_v2_pipeline_en_6.1.0_3.4_1755316162690.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("jsl_meds_ner_2b_q16_v2_pipeline", "en", "clinical/models")

text = """
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
The patient, Johnathan Miller, is a 54-year-old male admitted under hospital number HN382914. 
His most recent episode number is EP2024-1178, recorded on 2025-08-10. 
The patient presented with chronic knee pain and swelling. 
Past medical history includes hypertension and type 2 diabetes.
"""

result = pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("jsl_meds_ner_2b_q16_v2_pipeline", "en", "clinical/models")

text = """
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
The patient, Johnathan Miller, is a 54-year-old male admitted under hospital number HN382914. 
His most recent episode number is EP2024-1178, recorded on 2025-08-10. 
The patient presented with chronic knee pain and swelling. 
Past medical history includes hypertension and type 2 diabetes.
"""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("jsl_meds_ner_2b_q16_v2_pipeline", "en", "clinical/models")

val text = """
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
The patient, Johnathan Miller, is a 54-year-old male admitted under hospital number HN382914. 
His most recent episode number is EP2024-1178, recorded on 2025-08-10. 
The patient presented with chronic knee pain and swelling. 
Past medical history includes hypertension and type 2 diabetes.
"""

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
{
    "Patient Name": "Johnathan Miller",
    "Patient Age": 54,
    "Patient Gender": "male",
    "Hospital Number": "HN382914",
    "Episode Number": "EP2024-1178",
    "Episode Date": "2025-08-10"
}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_2b_q16_v2_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.5 GB|

## Included Models

- DocumentAssembler
- MedicalLLM