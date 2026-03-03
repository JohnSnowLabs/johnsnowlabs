---
layout: model
title: Sentence Entity Resolver for CPT Codes (bge_base_en_v1_5_onnx) - Pipeline
author: John Snow Labs
name: bgeresolve_cpt_pipeline
date: 2026-03-02
tags: [en, cpt, resolver, licensed, clinical, bge, sentence_entity_resolver, pipeline]
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

This pipeline maps clinical entities (Observation, Procedures, Tests, Treatments, Drug) to their corresponding CPT (Current Procedural Terminology) codes using bge_base_en_v1_5_onnx embeddings. It uses bge_base_en_v1_5_onnx embeddings and provides multiple resolution candidates with confidence scores, making it ideal for accurate procedural code assignment in clinical documentation.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_cpt_pipeline_en_6.3.0_3.4_1772411720486.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_cpt_pipeline_en_6.3.0_3.4_1772411720486.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bgeresolve_cpt_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("bgeresolve_cpt_pipeline", "en", "clinical/models")

sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("bgeresolve_cpt_pipeline", "en", "clinical/models")

val sample_text = """ A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| sent_id | ner_chunk          | entity        | cpt_code | resolutions        | all_codes                                                                                            | all_resolutions                                                                                      |
| :------ | :----------------- | :------------ | :------- | :----------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| 0       | episiotomy         | Procedure     | 59300    | episiotomy         | [59300, 59409, 59410, 59614, 59612, 59610, 1008583, 1008584, 54700]                                  | [episiotomy, vaginal delivery with episiotomy, vaginal delivery with episiotomy, including postp...] |
| 1       | Pulse oximetry     | Test          | 94760    | pulse oximetry     | [94760, 99453, 94761, 82810, 94762, 1013256, 82805, 94617]                                           | [pulse oximetry, device pulse oximetry, noninvasive pulse oximetry for oxygen saturation, multip...] |
| 2       | blood transfusion  | Procedure     | 36430    | blood transfusion  | [36430, 86950, 38243, 36450, 0232T, 36460, 38241, 36516, 36455, 36440]                               | [blood transfusion, white blood cell transfusion, transfusion of bone marrow, whole blood transf...] |
| 3       | inpatient hospital | Clinical_Dept | 1021881  | inpatient hospital | [1021881, 94003, 1021895, 99236, 1013660, 1013659, 1013682, 1013675, 59855, 1013661, 1021883, 10...] | [inpatient hospital, inpatient care, inpatient psychiatric facility, evaluation and management o...] |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_cpt_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

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