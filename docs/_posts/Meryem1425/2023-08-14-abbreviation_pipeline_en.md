---
layout: model
title: Pipeline to Map Abbreviations and Acronyms
author: John Snow Labs
name: abbreviation_pipeline
date: 2023-08-14
tags: [licensed, en, clinical, abbreviation, acronym]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A pretrained pipeline to detect abbreviations and acronyms of medical regulatory activities as well as map them with their definitions and categories.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/abbreviation_pipeline_en_5.0.1_3.0_1692042355925.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/abbreviation_pipeline_en_5.0.1_3.0_1692042355925.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

abbr_pipeline = PretrainedPipeline("abbreviation_pipeline", "en", "clinical/models")

result = abbr_pipeline.fullAnnotate("""Gravid with estimated fetal weight of 6-6/12 pounds.
           LABORATORY DATA: Laboratory tests include a CBC which is normal. 
           VDRL: Nonreactive
           HIV: Negative. One-Hour Glucose: 117. Group B strep has not been done as yet.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val abbr_pipeline = new PretrainedPipeline("abbreviation_pipeline", "en", "clinical/models")

val result = abbr_pipeline.fullAnnotate("""Gravid with estimated fetal weight of 6-6/12 pounds.
           LABORATORY DATA: Laboratory tests include a CBC which is normal. 
           VDRL: Nonreactive
           HIV: Negative. One-Hour Glucose: 117. Group B strep has not been done as yet.""")

```
</div>

## Results

```bash

+-----+------+-----------------+----------------------------------------+
|chunk|entity|category_mappings|                     definition_mappings|
+-----+------+-----------------+----------------------------------------+
|  CBC|  ABBR|          general|complete blood count                 ...|
| VDRL|  ABBR|    clinical_dept|  Venereal Disease Research Laboratories|
|  HIV|  ABBR|medical_condition|            Human immunodeficiency virus|
+-----+------+-----------------+----------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|abbreviation_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ChunkMapperModel
- ChunkMapperModel