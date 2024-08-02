---
layout: model
title: Pipeline for Snomed Concept, Body Structure Version
author: John Snow Labs
name: snomed_body_structure_resolver_pipeline
date: 2024-03-05
tags: [licensed, en, snomed, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts anatomical structure entities and maps them to their corresponding SNOMED (body structure version) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_body_structure_resolver_pipeline_en_5.3.0_3.2_1709669263188.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_body_structure_resolver_pipeline_en_5.3.0_3.2_1709669263188.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_body_structure_resolver_pipeline", "en", "clinical/models")

result = snomed_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_body_structure_resolver_pipeline", "en", "clinical/models")

val result = snomed_pipeline.annotate("""The patient is a 30-year-old female with a long history of insulin-dependent diabetes, type 2; coronary artery disease; chronic renal insufficiency; peripheral vascular disease, also secondary to diabetes; who was originally admitted to an outside hospital for what appeared to be acute paraplegia, lower extremities. She did receive a course of Bactrim for 14 days for UTI.""")

```
</div>

## Results

```bash

+-------------------+-----+---+---------+-----------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|              chunk|begin|end|ner_label|snomed_code|                resolution|                                           all_k_resolutions|                                                 all_k_codes|
+-------------------+-----+---+---------+-----------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+
|    coronary artery|   95|109| BodyPart|  181294004|           coronary artery|coronary artery:::coronary artery part:::segment of coron...|181294004:::119204004:::360487004:::55537005:::41801008::...|
|              renal|  128|132| BodyPart|   64033007|           renal structure|renal structure:::renal area:::renal segment:::renal vess...|64033007:::243968009:::84924000:::303402001:::361332007::...|
|peripheral vascular|  149|167| BodyPart|   51833009|peripheral vascular system|peripheral vascular system:::peripheral artery:::peripher...|51833009:::840581000:::3058005:::300054001:::281828002:::...|
|  lower extremities|  299|315| BodyPart|   61685007|           lower extremity|lower extremity:::lower extremity region:::lower extremit...|61685007:::127951001:::120575009:::182281004:::276744008:...|
+-------------------+-----+---+---------+-----------+--------------------------+------------------------------------------------------------+------------------------------------------------------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_body_structure_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
