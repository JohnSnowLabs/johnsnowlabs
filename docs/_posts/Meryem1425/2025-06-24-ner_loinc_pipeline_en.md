---
layout: model
title: Pipeline for Extracting Clinical Entities Related to LOINC Codes
author: John Snow Labs
name: ner_loinc_pipeline
date: 2025-06-24
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

This pipeline is designed to extract all entities mappable to LOINC codes.

2 NER models are used to achieve this task.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_loinc_pipeline_en_6.0.2_3.4_1750777763241.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_loinc_pipeline_en_6.0.2_3.4_1750777763241.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_loinc_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Vital signs are
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL,
  Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_loinc_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
A 65-year-old woman presents to the office with generalized fatigue for the last 4 months.
  She used to walk 1 mile each evening but now gets tired after 1-2 blocks. She has a history of Crohn disease and hypertension
  for which she receives appropriate medications. She is married and lives with her husband. She eats a balanced diet that
  includes chicken, fish, pork, fruits, and vegetables. She rarely drinks alcohol and denies tobacco use. Vital signs are
  within normal limits. A physical examination is unremarkable. Laboratory studies show the following: Hemoglobin: 9.8g/dL,
  Hematocrit: 32%, Mean Corpuscular Volume: 110 μm3.
""")

```
</div>

## Results

```bash
|    | chunks                  |   begin |   end | entities   |
|---:|:------------------------|--------:|------:|:-----------|
|  0 | Vital signs             |     449 |   459 | Test       |
|  1 | A physical examination  |     489 |   510 | Test       |
|  2 | Laboratory studies      |     529 |   546 | Test       |
|  3 | Hemoglobin              |     568 |   577 | Test       |
|  4 | Hematocrit              |     591 |   600 | Test       |
|  5 | Mean Corpuscular Volume |     608 |   630 | Test       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_loinc_pipeline|
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
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel