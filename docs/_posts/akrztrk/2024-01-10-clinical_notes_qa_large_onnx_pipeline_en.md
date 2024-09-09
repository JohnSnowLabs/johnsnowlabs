---
layout: model
title: Medical Question Answering Pipeline on Clinical Notes (Large - ONNX)
author: John Snow Labs
name: clinical_notes_qa_large_onnx_pipeline
date: 2024-01-10
tags: [licensed, en, onnx, pipeline, qa, clinical_notes]
task: [Question Answering, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [clinical_notes_qa_large_onnx](https://nlp.johnsnowlabs.com/2023/08/17/clinical_notes_qa_large_onnx_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_large_onnx_pipeline_en_5.2.0_3.4_1704903195198.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/clinical_notes_qa_large_onnx_pipeline_en_5.2.0_3.4_1704903195198.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

qa_pipeline = PretrainedPipeline("clinical_notes_qa_large_onnx_pipeline", "en", "clinical/models")

context = """his is a 14-month-old with history of chronic recurrent episodes of otitis media, totalling 6 bouts, requiring antibiotics since birth. There is also associated chronic nasal congestion. There had been no bouts of spontaneous tympanic membrane perforation, but there had been elevations of temperature up to 102 during the acute infection. He is being admitted at this time for myringotomy and tube insertion under general facemask anesthesia."""

question = """How many bouts of otitis media has the patient experienced?"""

result = qa_pipeline.fullAnnotate([question], [context])

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val qa_pipeline = PretrainedPipeline("clinical_notes_qa_large_onnx_pipeline", "en", "clinical/models")

context = """his is a 14-month-old with history of chronic recurrent episodes of otitis media, totalling 6 bouts, requiring antibiotics since birth. There is also associated chronic nasal congestion. There had been no bouts of spontaneous tympanic membrane perforation, but there had been elevations of temperature up to 102 during the acute infection. He is being admitted at this time for myringotomy and tube insertion under general facemask anesthesia."""

question = """How many bouts of otitis media has the patient experienced?"""

val result = qa_pipeline.fullAnnotate([question], [context])

```
</div>

## Results

```bash
The patient has experienced 6 bouts of otitis media.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|clinical_notes_qa_large_onnx_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

## Included Models

- MultiDocumentAssembler
- MedicalQuestionAnswering
