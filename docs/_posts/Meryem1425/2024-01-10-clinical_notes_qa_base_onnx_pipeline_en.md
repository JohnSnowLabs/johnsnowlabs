---
layout: model
title: Medical Question Answering Pipeline on Clinical Notes (ONNX)
author: John Snow Labs
name: clinical_notes_qa_base_onnx_pipeline
date: 2024-01-10
tags: [licensed, en, onnx, pipeline, qa, clinical_notes]
task: [Question Answering, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [clinical_notes_qa_base_onnx](https://nlp.johnsnowlabs.com/2023/08/17/clinical_notes_qa_base_onnx_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_base_onnx_pipeline_en_5.2.0_3.2_1704893753628.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_base_onnx_pipeline_en_5.2.0_3.2_1704893753628.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

qa_pipeline = PretrainedPipeline("clinical_notes_qa_base_onnx_pipeline", "en", "clinical/models")

context = """Patient with a past medical history of hypertension for 15 years.
(Medical Transcription Sample Report)
HISTORY OF PRESENT ILLNESS:
The patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."""

question = """What is the effect of directing attention on memory?"""

result = qa_pipeline.annotate([question], [context])

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val qa_pipeline = PretrainedPipeline("clinical_notes_qa_base_onnx_pipeline", "en", "clinical/models")

val context = """Patient with a past medical history of hypertension for 15 years.
(Medical Transcription Sample Report)
HISTORY OF PRESENT ILLNESS:
The patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."""

val question = """What is the effect of directing attention on memory?"""

val result = qa_pipeline.annotate([question], [context])

```
</div>

## Results

```bash
The primary issue reported by the patient is a heart attack.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_notes_qa_base_onnx_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.0 GB|

## Included Models

- MultiDocumentAssembler
- MedicalQuestionAnswering
