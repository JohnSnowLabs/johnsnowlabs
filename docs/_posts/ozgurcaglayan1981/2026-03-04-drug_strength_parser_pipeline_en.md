---
layout: model
title: Drug Strength Contextual Parser Pipeline
author: John Snow Labs
name: drug_strength_parser_pipeline
date: 2026-03-04
tags: [en, contextualparser, licensed, clinical, drug_strength, pipeline]
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

This pipeline, identifies drug strength entities in clinical text. It recognizes dosage patterns including mg, mcg, g, ml, IU, units, and various numeric formats.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_strength_parser_pipeline_en_6.3.0_3.4_1772587068417.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_strength_parser_pipeline_en_6.3.0_3.4_1772587068417.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("drug_strength_parser_pipeline", "en", "clinical/models")

sample_text = """ Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("drug_strength_parser_pipeline", "en", "clinical/models")

sample_text = """ Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("drug_strength_parser_pipeline", "en", "clinical/models")

val sample_text = """ Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

|   chunk |   begin |   end | label         |
|--------:|--------:|------:|:--------------|
| 500mg   |      33 |    37 | DRUG_STRENGTH |
| 10mg    |      66 |    69 | DRUG_STRENGTH |
| 200mg   |      93 |    97 | DRUG_STRENGTH |
| 1000 IU |     123 |   129 | DRUG_STRENGTH |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_strength_parser_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|401.8 KB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- ContextualParserModel
- ChunkConverter