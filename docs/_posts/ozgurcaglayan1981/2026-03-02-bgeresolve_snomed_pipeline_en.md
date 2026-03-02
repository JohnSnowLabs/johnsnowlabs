---
layout: model
title: Sentence Entity Resolver for SNOMED Codes ( bge_base_en_v1_5_onnx ) - Pipeline
author: John Snow Labs
name: bgeresolve_snomed_pipeline
date: 2026-03-02
tags: [en, snomed, resolver, licensed, clinical, bge, sentence_entity_resolver, pipeline]
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

This pipeline maps maps clinical entities to SNOMED codes using bge_base_en_v1_5_onnx embeddings. It leverages contextual embeddings to improve code resolution accuracy for medical concepts, including diseases, symptoms, procedures, and drugs.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_pipeline_en_6.3.0_3.4_1772410698504.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_pipeline_en_6.3.0_3.4_1772410698504.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bgeresolve_snomed_pipeline", "en", "clinical/models")

sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("bgeresolve_snomed_pipeline", "en", "clinical/models")

sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("bgeresolve_snomed_pipeline", "en", "clinical/models")

val sample_text = """ John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| sent_id | ner_chunk         | entity                    | snomed_code | resolutions       | all_codes                                                                                            | all_resolutions                                                                                      |
| :------ | :---------------- | :------------------------ | :---------- | :---------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| 0       | ofloxacin         | Drug_Ingredient           | 387551000   | ofloxacin         | [387551000, 96086002, 392417006, 392415003, 441553007, 294489002, 292951002, 105272001, 77697300...] | [ofloxacin, ofloxacin product, parenteral ofloxacin, oral ofloxacin, ofloxacin hydrochloride, of...] |
| 0       | secondary         | Modifier                  | 2603003     | secondary         | [2603003, 262134003, 721071000000106, 388872005, 14799000, 67126003, 416035002, 128462008, 16112...] | [secondary, secondary procedure, secondary and tertiary service, secondary onsm, tumor, secondar...] |
| 0       | conjunctivitis    | Disease_Syndrome_Disorder | 9826008     | conjunctivitis    | [9826008, 473460002, 45261009, 128350005, 231861005, 73762008, 231854006, 53726008, 70394001, 12...] | [conjunctivitis, allergic conjunctivitis, viral conjunctivitis, bacterial conjunctivitis, chlamy...] |
| 0       | cefixime          | Drug_Ingredient           | 387536009   | cefixime          | [387536009, 96052006, 713750001, 294548002, 291606002, 1217570005, 293010005, 121487005, 7856970...] | [cefixime, cefixime product, oral form cefixime, cefixime allergy, cefixime poisoning, cefixime ...] |
| 0       | cystic urethritis | Disease_Syndrome_Disorder | 1259233009  | cystic urethritis | [1259233009, 70795003, 31822004, 429728004, 236683007, 179101003, 236682002, 236684001, 89891003...] | [cystic urethritis, urethral cyst, urethritis, bacterial urethritis, chlamydial urethritis, chla...] |
| 0       | ibuprofen         | Drug_Ingredient           | 387207008   | ibuprofen         | [387207008, 350321003, 293619005, 38268001, 396197001, 218613000, 105211002, 725863000, 21260200...] | [ibuprofen, oral ibuprofen, ibuprofen allergy, ibuprofen-containing product, uniprofen, adverse ...] |
| 0       | inflammation      | Symptom                   | 257552002   | inflammation      | [257552002, 225540005, 274144001, 3723001, 64226004, 4532008, 75889009, 65761003, 26889001, 2675...] | [inflammation, wound inflammation, inflammation of bone, joint inflammation, colon inflammation,...] |
| 0       | cilnidipine       | Drug_Ingredient           | 1177123004  | cilnidipine       | [1177123004, 1179035008, 1179037000, 1179036009, 1179039002, 1187452004, 1187453009, 386861009, ...] | [cilnidipine, cilnidipine-containing product, cilnidipine-containing product in oral dose form, ...] |
| 0       | hypertension      | Hypertension              | 38341003    | hypertension      | [38341003, 75367002, 73578008, 28119000, 56218007, 48146000, 255330009, 161501007, 723232008, 64...] | [hypertension, blood pressure, hyperdistension, renal hypertension, systolic hypertension, diast...] |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_snomed_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.6 GB|

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