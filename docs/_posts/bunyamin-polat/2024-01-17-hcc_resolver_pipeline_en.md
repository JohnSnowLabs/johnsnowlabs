---
layout: model
title: Pipeline for Hierarchical Condition Categories (HCC) Sentence Entity Resolver
author: John Snow Labs
name: hcc_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, entity_resolution, clinical, pipeline, hcc]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts clinical conditions from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Hierarchical Condition Categories (HCC) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hcc_resolver_pipeline_en_5.2.1_3.0_1705486699832.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hcc_resolver_pipeline_en_5.2.1_3.0_1705486699832.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("hcc_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient's medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease, requiring comprehensive care and management.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("hcc_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient's medical record indicates a diagnosis of Diabetes and Chronic Obstructive Pulmonary Disease, requiring comprehensive care and management.""")

```
</div>

## Results

```bash
|    | chunks                                |   begin |   end | entities   |   hcc_code | resolutions                                                                                                                                                                                                                                                                                                                                 | all_codes          |
|---:|:--------------------------------------|--------:|------:|:-----------|-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|  0 | Diabetes                              |      54 |    61 | PROBLEM    |         19 | diabetes monitored [type 2 diabetes mellitus without complications]:::anaemia of diabetes [anemia, unspecified]:::anemia of diabetes (disorder) [type 2 diabetes mellitus with other specified complication]                                                                                                                                | 19:::0:::18        |
|  1 | Chronic Obstructive Pulmonary Disease |      67 |   103 | PROBLEM    |        111 | chronic obstructive pulmonary disease [chronic obstructive pulmonary disease, unspecified]:::chronic lung disease [pneumoconiosis due to other dust containing silica]:::chronic pulmonary heart disease [pulmonary heart disease, unspecified]:::other chronic obstructive pulmonary disease [other chronic obstructive pulmonary disease] | 111:::112:::85:::0 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hcc_resolver_pipeline|
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
- NerConverterInternalModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
