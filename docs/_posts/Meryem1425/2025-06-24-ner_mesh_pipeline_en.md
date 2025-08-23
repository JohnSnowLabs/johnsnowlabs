---
layout: model
title: Pipeline for Extracting Clinical Entities Related to MESH Codes
author: John Snow Labs
name: ner_mesh_pipeline
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

This pipeline is designed to extract all entities mappable to MESH codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_mesh_pipeline_en_6.0.2_3.4_1750791811731.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_mesh_pipeline_en_6.0.2_3.4_1750791811731.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_mesh_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""
She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. 
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. 
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, 
which were performed, which revealed malignant mesothelioma.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_mesh_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""
She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. 
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. 
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, 
which were performed, which revealed malignant mesothelioma.
""")

```
</div>

## Results

```bash
|    | chunks                     |   begin |   end | entities   |
|---:|:---------------------------|--------:|------:|:-----------|
|  0 | chest pain                 |      39 |    48 | PROBLEM    |
|  1 | bilateral pleural effusion |      68 |    93 | PROBLEM    |
|  2 | the pathology              |     142 |   154 | TEST       |
|  3 | the pericardectomy         |     170 |   187 | TREATMENT  |
|  4 | mesothelioma               |     228 |   239 | PROBLEM    |
|  5 | chest tube placement       |     257 |   276 | TREATMENT  |
|  6 | drainage of the fluid      |     282 |   302 | PROBLEM    |
|  7 | thoracoscopy               |     317 |   328 | TREATMENT  |
|  8 | fluid biopsies             |     335 |   348 | TEST       |
|  9 | malignant mesothelioma     |     389 |   410 | PROBLEM    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_mesh_pipeline|
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