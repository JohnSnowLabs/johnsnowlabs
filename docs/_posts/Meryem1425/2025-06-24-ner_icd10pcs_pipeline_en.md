---
layout: model
title: Pipeline for Extracting Clinical Entities Related to ICD-10-PCS Codes
author: John Snow Labs
name: ner_icd10pcs_pipeline
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

This pipeline is designed to extract all entities mappable to ICD-10-PCS codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_icd10pcs_pipeline_en_6.0.2_3.4_1750798177135.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_icd10pcs_pipeline_en_6.0.2_3.4_1750798177135.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_icd10pcs_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Given the severity of her abdominal examination and her persistence of her symptoms,
            it is detected that need for laparoscopic appendectomy and possible jejunectomy
            as well as pyeloplasty. We recommend performing a mediastinoscopy""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_icd10pcs_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Given the severity of her abdominal examination and her persistence of her symptoms,
            it is detected that need for laparoscopic appendectomy and possible jejunectomy
            as well as pyeloplasty. We recommend performing a mediastinoscopy""")

```
</div>

## Results

```bash
|    | chunks                    |   begin |   end | entities   |
|---:|:--------------------------|--------:|------:|:-----------|
|  0 | laparoscopic appendectomy |     127 |   151 | Procedure  |
|  1 | jejunectomy               |     166 |   176 | Procedure  |
|  2 | pyeloplasty               |     201 |   211 | Procedure  |
|  3 | mediastinoscopy           |     240 |   254 | Procedure  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_icd10pcs_pipeline|
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