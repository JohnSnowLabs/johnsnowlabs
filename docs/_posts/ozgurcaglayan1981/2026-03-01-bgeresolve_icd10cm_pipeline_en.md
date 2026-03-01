---
layout: model
title: Sentence Entity Resolver for ICD-10-CM Codes (bge_base_en_v1_5_onnx) - Pipeline
author: John Snow Labs
name: bgeresolve_icd10cm_pipeline
date: 2026-03-01
tags: [en, icd10cm, resolver, licensed, clinical, bge, sentence_entity_resolver, pipeline]
task: [Entity Resolution, Pipeline Healthcare]
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

This pipeline, maps clinical entities to ICD-10-CM codes using bge_base_en_v1_5_onnx embeddings. It resolves entities from the following domains: Condition, Observation, Measurement, and Procedure.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_pipeline_en_6.3.0_3.4_1772408368951.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_icd10cm_pipeline_en_6.3.0_3.4_1772408368951.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bgeresolve_icd10cm_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("bgeresolve_icd10cm_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("bgeresolve_icd10cm_pipeline", "en", "clinical/models")

val sample_text = """ A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, associated with acute hepatitis and obesity, presented with a one-week history of polyuria, polydipsia, and vomiting."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| sent_id | ner_chunk                             | entity  | icd10cm_code | resolutions                     | all_codes                                                                                            | all_resolutions                                                                                      |
| :------ | :------------------------------------ | :------ | :----------- | :------------------------------ | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| 0       | gestational diabetes mellitus         | PROBLEM | O24.4        | gestational diabetes mellitus   | [O24.4, O24.41, O24.43, O24.42, O24.414, O24.424, O24.434, O24.439, O24, O24.419, O24.410, O24.4...] | [gestational diabetes mellitus, gestational diabetes mellitus in pregnancy, gestational diabetes...] |
| 0       | subsequent type two diabetes mellitus | PROBLEM | E11          | type 2 diabetes mellitus        | [E11, E11.69, E11.6, E11.64, E13, E11.65, E11.8, E11.622, E11.59, E11.618, E11.621, E11.49, E11....] | [type 2 diabetes mellitus, type 2 diabetes mellitus with other specified complication, type 2 di...] |
| 0       | T2DM                                  | PROBLEM | E11          | type 2 diabetes mellitus        | [E11, E11.65, E11.64, E11.9, E11.44, E11.5, E11.41, E11.42, E11.8, E11.620, E11.62, E11.0, E11.6...] | [type 2 diabetes mellitus, type 2 diabetes mellitus with hyperglycemia, type 2 diabetes mellitus...] |
| 0       | HTG-induced pancreatitis              | PROBLEM | K85.3        | drug induced acute pancreatitis | [K85.3, K86.0, K85.2, K85.31, K85.21, K85.32, K85.22, K85.30, K85.8, K85.20, B25.2, K86.1, K85, ...] | [drug induced acute pancreatitis, alcohol-induced chronic pancreatitis, alcohol induced acute pa...] |
| 0       | acute hepatitis                       | PROBLEM | B15          | acute hepatitis a               | [B15, B16, B17.1, B17, B17.2, B17.9, B17.8, K71.2, B17.11, K72.0, B17.10, B16.9, B16.2, R10.0, K...] | [acute hepatitis a, acute hepatitis b, acute hepatitis c, other acute viral hepatitis, acute hep...] |
| 0       | obesity                               | PROBLEM | E66          | overweight and obesity          | [E66, E66.9, E66.0, E66.8, E66.3, O99.21, E66.09, O99.214, O99.215, E66.1, O99.212, Z68, E66.01,...] | [overweight and obesity, obesity, unspecified, obesity due to excess calories, other obesity, ov...] |
| 0       | polyuria                              | PROBLEM | R35          | polyuria                        | [R35, R35.89, R35.8, R35.81, R80, R80.8, R34, N06.8, R80.9, Q61.3, R35.1, R80.0, Q61.2, N06, R63...] | [polyuria, other polyuria, other polyuria, nocturnal polyuria, proteinuria, other proteinuria, a...] |
| 0       | polydipsia                            | PROBLEM | R63.1        | polydipsia                      | [R63.1, O40, R35, R35.89, R35.8, R63.2, R35.81, T73.1, O40.2, E23.2, E31, E86.0, E31.8, R63.8, N...] | [polydipsia, polyhydramnios, polyuria, other polyuria, other polyuria, polyphagia, nocturnal pol...] |
| 0       | vomiting                              | PROBLEM | R11.1        | vomiting                        | [R11.1, R11, R11.12, R11.10, R11.11, R11.13, P92.0, R11.0, G43.A, O21.9, R11.14, O21.8, R11.2, O...] | [vomiting, nausea and vomiting, projectile vomiting, vomiting, unspecified, vomiting without nau...] |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_icd10cm_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.3 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- Chunk2Doc
- BGEEmbeddings
- SentenceEntityResolverModel
