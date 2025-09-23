---
layout: model
title: Pipeline for Extracting Clinical Entities Related to HGNC Codes
author: John Snow Labs
name: ner_hgnc_pipeline
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

This pipeline is designed to extract all entities mappable to HGNC codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_hgnc_pipeline_en_6.0.2_3.4_1750796503084.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_hgnc_pipeline_en_6.0.2_3.4_1750796503084.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_hgnc_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""During today's consultation, we reviewed the results of the comprehensive genetic analysis performed on the patient. 
This analysis uncovered complex interactions between several genes: DUX4, DUX4L20, FBXO48, MYOD1, and PAX7. 
These findings are significant as they provide new understanding of the molecular pathways that are involved in muscle differentiation and may play a role in the development and progression of muscular dystrophies in this patient.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_hgnc_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""During today's consultation, we reviewed the results of the comprehensive genetic analysis performed on the patient. 
This analysis uncovered complex interactions between several genes: DUX4, DUX4L20, FBXO48, MYOD1, and PAX7. 
These findings are significant as they provide new understanding of the molecular pathways that are involved in muscle differentiation and may play a role in the development and progression of muscular dystrophies in this patient.""")

```
</div>

## Results

```bash
|    | chunks   |   begin |   end | entities   |
|---:|:---------|--------:|------:|:-----------|
|  0 | DUX4     |     187 |   190 | GENE       |
|  1 | DUX4L20  |     193 |   199 | GENE       |
|  2 | FBXO48   |     202 |   207 | GENE       |
|  3 | MYOD1    |     210 |   214 | GENE       |
|  4 | PAX7     |     221 |   224 | GENE       |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_hgnc_pipeline|
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