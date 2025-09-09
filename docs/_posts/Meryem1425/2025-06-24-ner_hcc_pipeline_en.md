---
layout: model
title: Pipeline for Extracting Clinical Entities Related to HCC Codes
author: John Snow Labs
name: ner_hcc_pipeline
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

This pipeline is designed to extract all entities mappable to HCC codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_hcc_pipeline_en_6.0.2_3.4_1750797180085.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_hcc_pipeline_en_6.0.2_3.4_1750797180085.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_hcc_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient's medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease, requiring comprehensive care and management.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_hcc_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient's medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease, requiring comprehensive care and management.""")

```
</div>

## Results

```bash
|    | chunks                                |   begin |   end | entities   |
|---:|:--------------------------------------|--------:|------:|:-----------|
|  0 | Diabetes                              |      55 |    62 | PROBLEM    |
|  1 | Chronic Obstructive Pulmonary Disease |      68 |   104 | PROBLEM    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_hcc_pipeline|
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