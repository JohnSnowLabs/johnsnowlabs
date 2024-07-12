---
layout: model
title: Pipeline for RxNorm Concept Unique Identifier (RxCUI) Sentence Entity Resolver
author: John Snow Labs
name: rxcui_resolver_pipeline
date: 2024-02-01
tags: [licensed, en, entity_resolution, clinical, pipeline, rxcui]
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

This advanced pipeline extracts medical entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding RxNorm Concept Unique Identifier (RxCUI) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxcui_resolver_pipeline_en_5.2.1_3.0_1706791242663.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxcui_resolver_pipeline_en_5.2.1_3.0_1706791242663.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("rxcui_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""He was seen by the endocrinology service and she was discharged on 50 mg of eltrombopag oral at night, 5 mg amlodipine with meals, and metformin 1000 mg two times a day.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("rxcui_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""He was seen by the endocrinology service and she was discharged on 50 mg of eltrombopag oral at night, 5 mg amlodipine with meals, and metformin 1000 mg two times a day.""")

```
</div>

## Results

```bash
+-------------------------+-----+---+---------+------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|                    chunk|begin|end|ner_label|  Code|                                description|                                                 resolutions|                                                   all_codes|
+-------------------------+-----+---+---------+------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|50 mg of eltrombopag oral|   67| 91|     DRUG|825427|              eltrombopag 50 MG Oral Tablet|eltrombopag 50 MG Oral Tablet:::alpelisib 50 MG Oral Tabl...|825427:::2169316:::2049111:::1804806:::1940374:::1597587:...|
|          5 mg amlodipine|  103|117|     DRUG|197361|                amlodipine 5 MG Oral Tablet|amlodipine 5 MG Oral Tablet:::levamlodipine 5 MG Oral Tab...|197361:::2377371:::387013:::212549:::311354:::2377373:::4...|
|        metformin 1000 mg|  135|151|     DRUG|861004|metformin hydrochloride 1000 MG Oral Tablet|metformin hydrochloride 1000 MG Oral Tablet:::cefepime 10...|861004:::1665093:::1791593:::311625:::1665050:::1722919::...|
+-------------------------+-----+---+---------+------+-------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxcui_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

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
