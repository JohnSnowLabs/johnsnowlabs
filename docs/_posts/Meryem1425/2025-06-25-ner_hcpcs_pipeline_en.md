---
layout: model
title: Pipeline for Extracting Clinical Entities Related to HCPCS Codes
author: John Snow Labs
name: ner_hcpcs_pipeline
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

This pipeline is designed to extract all entities mappable to HCPCS codes.

2 NER models are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_hcpcs_pipeline_en_6.0.2_3.4_1750858394081.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_hcpcs_pipeline_en_6.0.2_3.4_1750858394081.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_hcpcs_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
Mary received a mechanical prosthetic heart valve in June 2020, and the results were successful. 
Diabetes screening test performed, revealing abnormal result. 
She  uses infusion pump for diabetes and a CPAP machine for sleep apnea. 
In 2021, She received a breast prosthesis implant.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_hcpcs_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
Mary received a mechanical prosthetic heart valve in June 2020, and the results were successful. 
Diabetes screening test performed, revealing abnormal result. 
She  uses infusion pump for diabetes and a CPAP machine for sleep apnea. 
In 2021, She received a breast prosthesis implant.
""")

```
</div>

## Results

```bash
|    | chunks                              |   begin |   end | entities   |
|---:|:------------------------------------|--------:|------:|:-----------|
|  0 | a mechanical prosthetic heart valve |      15 |    49 | PROCEDURE  |
|  1 | infusion pump                       |     172 |   184 | PROCEDURE  |
|  2 | a CPAP machine                      |     203 |   216 | PROCEDURE  |
|  3 | a breast prosthesis implant         |     258 |   284 | PROCEDURE  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_hcpcs_pipeline|
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