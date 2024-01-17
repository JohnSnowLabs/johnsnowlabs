---
layout: model
title: Pipeline for Snomed Concept, Body Structure Version
author: John Snow Labs
name: snomed_body_structure_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, snomed, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts anatomical structure entities and maps them to their corresponding SNOMED (body structure version) codes using  `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_body_structure_resolver_pipeline_en_5.2.1_3.4_1705499903900.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_body_structure_resolver_pipeline_en_5.2.1_3.4_1705499903900.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_body_structure_resolver_pipeline", "en", "clinical/models")

text = """The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI."""

result = snomed_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_body_structure_resolver_pipeline", "en", "clinical/models")

val text = """The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI."""

val result = snomed_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|             chunks|begin|end|     code|                                         all_codes|                                       resolutions|                                     all_distances|
+-------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|    coronary artery|   95|109|119204004|[119204004, 360487004, 41801008, 312553002, 181...|[Coronary artery part, Segment of coronary arte...|[0.0384, 0.0437, 0.0624, 0.0738, 0.0749, 0.0805...|
|              renal|  128|132|243968009|[243968009, 84924000, 363530009, 119219003, 640...|[Renal area, Structure of renal segment, Struct...|[0.0594, 0.0790, 0.1002, 0.1007, 0.1013, 0.1052...|
|peripheral vascular|  149|167| 51833009|[51833009, 361391003, 371671000000102, 36200600...|[Peripheral vascular system structure, Regional...|[0.0796, 0.0809, 0.0847, 0.0864, 0.0881, 0.0940...|
|  lower extremities|  299|315|120575009|[120575009, 61685007, 69548008, 229757002, 1282...|[Lower extremity part, Lower limb structure, Lo...|[0.0313, 0.0385, 0.0454, 0.0462, 0.0500, 0.0546...|
+-------------------+-----+---+---------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_body_structure_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
