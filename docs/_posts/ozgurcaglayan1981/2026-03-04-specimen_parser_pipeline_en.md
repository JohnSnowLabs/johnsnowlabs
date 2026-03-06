---
layout: model
title: Specimen Contextual Parser Pipeline
author: John Snow Labs
name: specimen_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, specimen, pipeline]
task: [Contextual Parser, Pipeline Healthcare]
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline, extracts specimen entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/specimen_parser_pipeline_en_6.3.0_3.4_1772588332341.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/specimen_parser_pipeline_en_6.3.0_3.4_1772588332341.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("specimen_parser_pipeline", "en", "clinical/models")

sample_text = """ Specimen ID: AB123-456789 was collected from the patient.
The laboratory processed Specimen Number CD987654 yesterday.
Use Specimen Code: XYZ12-3456 for tracking purposes.
Sample was labeled as Specimen#EF34-789.
Specimen No. GH56-123456 was sent to the pathology department."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("specimen_parser_pipeline", "en", "clinical/models")

sample_text = """ Specimen ID: AB123-456789 was collected from the patient.
The laboratory processed Specimen Number CD987654 yesterday.
Use Specimen Code: XYZ12-3456 for tracking purposes.
Sample was labeled as Specimen#EF34-789.
Specimen No. GH56-123456 was sent to the pathology department."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("specimen_parser_pipeline", "en", "clinical/models")

val sample_text = """ Specimen ID: AB123-456789 was collected from the patient.
The laboratory processed Specimen Number CD987654 yesterday.
Use Specimen Code: XYZ12-3456 for tracking purposes.
Sample was labeled as Specimen#EF34-789.
Specimen No. GH56-123456 was sent to the pathology department."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| specimen_id   |   begin |   end | label    |
|:--------------|--------:|------:|:---------|
| AB123         |      13 |    18 | SPECIMEN |
| CD987654      |     100 |   108 | SPECIMEN |
| XYZ12-3456    |     140 |   150 | SPECIMEN |
| EF34-789      |     206 |   214 | SPECIMEN |
| GH56-123456   |     230 |   241 | SPECIMEN |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|specimen_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|396.5 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter