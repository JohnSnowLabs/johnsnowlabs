---
layout: model
title: Pipeline for Extracting Clinical Entities Related to SNOMED (Body Structure) Codes
author: John Snow Labs
name: ner_snomed_bodyStructure_pipeline
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

This pipeline is designed to extract all entities mappable to SNOMED (Body Structure) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_snomed_bodyStructure_pipeline_en_6.0.2_3.4_1750870193859.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_snomed_bodyStructure_pipeline_en_6.0.2_3.4_1750870193859.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_snomed_bodyStructure_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; 
chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; 
who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. 
She did receive a course of Bactrim for 14 days for UTI.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_snomed_bodyStructure_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; 
chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; 
who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. 
She did receive a course of Bactrim for 14 days for UTI.""")

```
</div>

## Results

```bash
|    | chunks              |   begin |   end | entities   |
|---:|:--------------------|--------:|------:|:-----------|
|  0 | coronary artery     |      95 |   109 | BodyPart   |
|  1 | renal               |     129 |   133 | BodyPart   |
|  2 | peripheral vascular |     150 |   168 | BodyPart   |
|  3 | lower extremities   |     301 |   317 | BodyPart   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_snomed_bodyStructure_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel