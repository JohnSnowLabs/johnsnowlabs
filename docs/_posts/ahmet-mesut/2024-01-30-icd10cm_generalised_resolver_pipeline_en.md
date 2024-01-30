---
layout: model
title: Pipeline for ICD-10-CM (General 3-character Codes)
author: John Snow Labs
name: icd10cm_generalised_resolver_pipeline
date: 2024-01-30
tags: [licensed, en, clinical, icd10cm, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts the following entities and maps them to their ICD-10-CM codes using `sbiobert_base_cased_mli` sentence embeddings. It predicts ICD-10-CM codes up to 3 characters (according to ICD-10-CM code structure the first three characters represent the general type of injury or disease).
Predicted Entities:
`COMMUNICABLE_DISEASE`,
`DIABETES`,
`DISEASE_SYNDROME_DISORDER`,
`EKG_FINDINGS`,
`HEART_DISEASE`,
`HYPERLIPIDEMIA`,
`HYPERTENSION`,
`IMAGINGFINDINGS`,
`INJURY_OR_POISONING`,
`KIDNEY_DISEASE`,
`OBESITY`,
`ONCOLOGICAL`,
`OVERWEIGHT`,
`PREGNANCY`,
`PSYCHOLOGICAL_CONDITION`,
`SYMPTOM`,
`VS_FINDING`,

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_resolver_pipeline_en_5.2.1_3.2_1706633992078.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_generalised_resolver_pipeline_en_5.2.1_3.2_1706633992078.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

icd10cm_pipeline = PretrainedPipeline("icd10cm_generalised_resolver_pipeline", "en", "clinical/models")

text = """A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""

result = icd10cm_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val icd10cm_pipeline = PretrainedPipeline("icd10cm_generalised_resolver_pipeline", "en", "clinical/models")

val text = """A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus, associated with obesity with a body mass index (BMI) of 33.5 kg/m2, presented with a one-week history of polyuria, polydipsia, poor appetite, and vomiting. Two weeks prior to presentation, she was treated with a five-day course of amoxicillin for a respiratory tract infection."""

val result = icd10cm_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-----------------------------+-----+---+----+-----------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|                       chunks|begin|end|code|                                                        all_codes|                                                                     resolutions|                                                                   all_distances|
+-----------------------------+-----+---+----+-----------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|gestational diabetes mellitus|   39| 67| O24|                                                  [O24, Z86, Z87]|[gestational diabetes mellitus [gestational diabetes mellitus], history of ge...|                                                        [0.0000, 0.0432, 0.0438]|
|   type two diabetes mellitus|  128|153| E11|                                             [E11, O24, E13, E10]|[type 2 diabetes mellitus [type 2 diabetes mellitus], pre-existing type 2 dia...|                                                [0.0065, 0.0374, 0.0388, 0.0394]|
|                      obesity|  172|178| E66|                         [E66, Z68, Q13, Z86, E34, H35, Z83, Q55]|[obesity [obesity, unspecified], obese [body mass index [bmi] 40.0-44.9, adul...|                [0.0000, 0.0264, 0.0278, 0.0403, 0.0414, 0.0449, 0.0473, 0.0482]|
|                     polyuria|  261|268| R35|[R35, E23, R31, R82, N40, E72, O04, R30, R80, E88, N03, P96, N02]|[polyuria [polyuria], polyuric state (disorder) [diabetes insipidus], hematur...|[0.0000, 0.1016, 0.1103, 0.1126, 0.1237, 0.1303, 0.1319, 0.1303, 0.1346, 0.13...|
|                   polydipsia|  271|280| R63|[R63, F63, E23, O40, G47, M79, R06, H53, I44, Q30, I45, R00, M35]|[polydipsia [polydipsia], psychogenic polydipsia [other impulse disorders], p...|[0.0000, 0.0455, 0.0635, 0.1474, 0.1520, 0.1553, 0.1641, 0.1675, 0.1648, 0.17...|
|                poor appetite|  283|295| R63|[R63, P92, R43, E86, R19, F52, Z72, R06, Z76, R53, R45, F50, R10]|[poor appetite [anorexia], poor feeding [feeding problem of newborn, unspecif...|[0.0000, 0.0603, 0.0730, 0.0837, 0.0844, 0.0847, 0.0861, 0.0870, 0.0871, 0.08...|
|                     vomiting|  302|309| R11|                                                  [R11, G43, P92]|[vomiting [vomiting], periodic vomiting [cyclical vomiting, in migraine, intr...|                                                        [0.0000, 0.0484, 0.0492]|
|  respiratory tract infection|  405|431| J98|               [J98, J06, A49, J04, J22, P28, Z59, T17, J20, J18]|[respiratory tract infection [other specified respiratory disorders], upper r...|[0.0000, 0.0472, 0.0524, 0.0698, 0.0706, 0.0803, 0.0798, 0.0789, 0.0885, 0.0911]|
+-----------------------------+-----+---+----+-----------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_generalised_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.5 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
