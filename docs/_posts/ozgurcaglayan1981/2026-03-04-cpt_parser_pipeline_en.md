---
layout: model
title: CPT Contextual Parser Pipeline
author: John Snow Labs
name: cpt_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, cpt, pipeline]
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

This pipeline, extracts CPT entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_parser_pipeline_en_6.3.0_3.4_1772585997153.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_parser_pipeline_en_6.3.0_3.4_1772585997153.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("cpt_parser_pipeline", "en", "clinical/models")

sample_text = """ The patient underwent procedure CPT 99213 for office visit.
Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel.
The radiology department billed CPT 93000 for electrocardiogram.
Surgical procedure was coded as CPT 36415 for routine venipuncture.
The final billing included CPT 85025 for complete blood count with differential."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("cpt_parser_pipeline", "en", "clinical/models")

sample_text = """ The patient underwent procedure CPT 99213 for office visit.
Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel.
The radiology department billed CPT 93000 for electrocardiogram.
Surgical procedure was coded as CPT 36415 for routine venipuncture.
The final billing included CPT 85025 for complete blood count with differential."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("cpt_parser_pipeline", "en", "clinical/models")

val sample_text = """ The patient underwent procedure CPT 99213 for office visit.
Laboratory tests were performed using CPT code 80053 for comprehensive metabolic panel.
The radiology department billed CPT 93000 for electrocardiogram.
Surgical procedure was coded as CPT 36415 for routine venipuncture.
The final billing included CPT 85025 for complete blood count with differential."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|   cpt_id |   begin |   end | label   |
|---------:|--------:|------:|:--------|
|    99213 |      36 |    41 | CPT     |
|    80053 |     107 |   112 | CPT     |
|    93000 |     184 |   189 | CPT     |
|    36415 |     249 |   254 | CPT     |
|    85025 |     312 |   317 | CPT     |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|396.6 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter