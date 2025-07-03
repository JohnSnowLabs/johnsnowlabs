---
layout: model
title: Pipeline for Extracting Clinical Entities Related to CPT Codes
author: John Snow Labs
name: ner_cpt_pipeline
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

This pipeline is designed to extract all entities mappable to CPT codes.

2 NER models are used to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_cpt_pipeline_en_6.0.2_3.4_1750788966551.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_cpt_pipeline_en_6.0.2_3.4_1750788966551.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_cpt_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_cpt_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.
""")

```
</div>

## Results

```bash
|    | chunks               |   begin |   end | entities   |
|---:|:---------------------|--------:|------:|:-----------|
|  0 | pericardectomy       |     240 |   253 | Procedure  |
|  1 | chest tube placement |     322 |   341 | Procedure  |
|  2 | thoracoscopy         |     382 |   393 | Procedure  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_cpt_pipeline|
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