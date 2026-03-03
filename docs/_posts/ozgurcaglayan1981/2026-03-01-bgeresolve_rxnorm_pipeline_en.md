---
layout: model
title: Sentence Entity Resolver for RxNorm Codes (bge_base_en_v1_5_onnx) - Pipeline
author: John Snow Labs
name: bgeresolve_rxnorm_pipeline
date: 2026-03-01
tags: [en, rxnorm, resolver, licensed, clinical, bge, sentence_entity_resolver, pipeline]
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

This pipeline maps drug entities to RxNorm codes using bge_base_en_v1_5_onnx embeddings. It leverages contextual embeddings to improve code resolution accuracy for drug concepts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_pipeline_en_6.3.0_3.4_1772409539349.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_pipeline_en_6.3.0_3.4_1772409539349.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bgeresolve_rxnorm_pipeline", "en", "clinical/models")

sample_text = """ The patient was prescribed aspirin and an Albuterol inhaler for respiratory issues. She also takes Apixaban 5 mg, Metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```

{:.jsl-block}
```python

from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("bgeresolve_rxnorm_pipeline", "en", "clinical/models")

sample_text = """ The patient was prescribed aspirin and an Albuterol inhaler for respiratory issues. She also takes Apixaban 5 mg, Metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure."""

result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = PretrainedPipeline("bgeresolve_rxnorm_pipeline", "en", "clinical/models")

val sample_text = """ The patient was prescribed aspirin and an Albuterol inhaler for respiratory issues. She also takes Apixaban 5 mg, Metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure."""

val result = pipeline.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
</div>

## Results

```bash

| sent_id | ner_chunk         | entity | rxnorm_code | resolutions                | all_codes                                                                                            | all_resolutions                                                                                      |
| :------ | :---------------- | :----- | :---------- | :------------------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| 0       | aspirin           | DRUG   | 1191        | aspirin                    | [1191, 1295740, 1154070, 1001473, 218266, 819659, 202547, 215568, 611, 687078, 315424, 317299, 8...] | [aspirin, aspirin product, aspirin pill, ecpirin, med aspirin, aspirin / papain, empirin, bayer...]  |
| 0       | Albuterol inhaler | DRUG   | 1154602     | albuterol inhalant product | [1154602, 745678, 435, 1154606, 1649559, 2108226, 801094, 2665904, 215455, 2108233, 1172174, 266...] | [albuterol inhalant product, albuterol metered dose inhaler, albuterol, albuterol pill, albutero...] |
| 1       | Apixaban 5 mg     | DRUG   | 1364444     | apixaban 5 mg              | [1364444, 1364431, 1364446, 1364445, 1364447, 1364435, 1364437, 1364441, 316619, 855817, 200796,...] | [apixaban 5 mg, apixaban 2.5 mg, apixaban 5 mg [eliquis], apixaban 5 mg oral tablet, apixaban 5 ...] |
| 1       | Metformin 1000 mg | DRUG   | 316255      | metformin 1000 mg          | [316255, 860995, 330861, 860997, 429841, 316256, 861005, 861014, 1862689, 1593059, 1992698, 8610...] | [metformin 1000 mg, metformin hydrochloride 1000 mg, metformin 250 mg, metformin hydrochloride 1...] |
| 1       | Lisinopril 10 mg  | DRUG   | 316151      | lisinopril 10 mg           | [316151, 314076, 563611, 565846, 567576, 316153, 314077, 328290, 316154, 104377, 197885, 316627,...] | [lisinopril 10 mg, lisinopril 10mg 10 mg, lisinopril 10 mg [zestril], lisinopril 10 mg [carace],...] |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_rxnorm_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

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