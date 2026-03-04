---
layout: model
title: Pipeline to Mapping Entities (Clinical Findings) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_clinical_findings_mapping
date: 2026-03-04
tags: [en, umls, clinical_findings, mapping, licensed, clinical, chunk_mapper, pipeline]
task: [Chunk Mapping, Pipeline Healthcare]
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

This pretrained pipeline is built on the top of umls_clinical_findings_mapper model and maps clinical entities with corresponding UMLS CUI codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_clinical_findings_mapping_en_6.3.0_3.4_1772648564197.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_clinical_findings_mapping_en_6.3.0_3.4_1772648564197.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("umls_clinical_findings_mapping", "en", "clinical/models")

sample_text = """ A 28-year-old female with a history of obesity with BMI of 33.5 kg/m2, presented with a one-week history of reduced fatigue."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("umls_clinical_findings_mapping", "en", "clinical/models")

sample_text = """ A 28-year-old female with a history of obesity with BMI of 33.5 kg/m2, presented with a one-week history of reduced fatigue."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("umls_clinical_findings_mapping", "en", "clinical/models")

val sample_text = """ A 28-year-old female with a history of obesity with BMI of 33.5 kg/m2, presented with a one-week history of reduced fatigue."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| chunk           | umls_code |
| :-------------- | :-------- |
| obesity         | C4759928  |
| BMI             | C0578022  |
| reduced fatigue | C5547024  |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_clinical_findings_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
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
- NerConverterInternalModel
- ChunkMapperModel