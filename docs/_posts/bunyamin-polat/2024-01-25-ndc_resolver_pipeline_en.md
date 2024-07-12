---
layout: model
title: Pipeline for National Drug Codes (NDC) Sentence Entity Resolver
author: John Snow Labs
name: ndc_resolver_pipeline
date: 2024-01-25
tags: [licensed, en, entity_resolution, clinical, pipeline, ndc]
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

This advanced pipeline extracts medication entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding National Drug Codes (NDC) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_resolver_pipeline_en_5.2.1_3.0_1706205426957.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_resolver_pipeline_en_5.2.1_3.0_1706205426957.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ndc_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient was given aspirin 81 mg and metformin 500 mg""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ndc_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient was given aspirin 81 mg and metformin 500 mg""")

```
</div>

## Results

```bash
+----------------+-----+---+---------+----------+-------------------+--------------------------------------------------------------------------------+
|           chunk|begin|end|ner_label|       ndc|        description|                                                                      aux_labels|
+----------------+-----+---+---------+----------+-------------------+--------------------------------------------------------------------------------+
|   aspirin 81 mg|   22| 34|     DRUG|41250-0780|      aspirin 81 mg|{'packages': "['1 BOTTLE, PLASTIC in 1 PACKAGE (41250-780-01)  > 120 TABLET, ...|
|metformin 500 mg|   40| 55|     DRUG|62207-0491|metformin er 500 mg|{'packages': "['5000 TABLET in 1 POUCH (62207-491-31)', '25000 TABLET in 1 CA...|
+----------------+-----+---+---------+----------+-------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.0 GB|

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
