---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED (Findings and Concepts) Codes
author: John Snow Labs
name: ner_snomed_term_pipeline
date: 2025-06-25
tags: [licensed, en, clinical, pipeline, ner]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract all entities mappable to SNOMED (Findings and Concepts) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_term_pipeline_en_6.0.2_3.4_1750883741626.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_term_pipeline_en_6.0.2_3.4_1750883741626.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_term_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.",
"Due to experiencing chronic pain the patient was referred to a fibromyalgia specialist for further evaluation.",
"His hypertension is currently managed with a combination of lifestyle modifications and medication.",
"The child was brought in with symptoms of acute otitis including ear pain and fever.",
"Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.",
"The radiograph showed evidence of a distal radius fracture from a recent fall.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_term_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.",
"Due to experiencing chronic pain the patient was referred to a fibromyalgia specialist for further evaluation.",
"His hypertension is currently managed with a combination of lifestyle modifications and medication.",
"The child was brought in with symptoms of acute otitis including ear pain and fever.",
"Laboratory tests indicate the individual has hyperthyroidism requiring further endocrinological assessment.",
"The radiograph showed evidence of a distal radius fracture from a recent fall.
""")

```
</div>

## Results

```bash
|    | chunks                 |   begin |   end | entities    |
|---:|:-----------------------|--------:|------:|:------------|
|  0 | acute appendicitis     |      32 |    49 | snomed_term |
|  1 | chronic pain           |     111 |   122 | snomed_term |
|  2 | fibromyalgia           |     154 |   165 | snomed_term |
|  3 | hypertension           |     209 |   220 | snomed_term |
|  4 | otitis                 |     356 |   361 | snomed_term |
|  5 | ear pain               |     373 |   380 | snomed_term |
|  6 | fever                  |     386 |   390 | snomed_term |
|  7 | hyperthyroidism        |     441 |   455 | snomed_term |
|  8 | radiograph             |     511 |   520 | snomed_term |
|  9 | distal radius fracture |     543 |   564 | snomed_term |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_term_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel