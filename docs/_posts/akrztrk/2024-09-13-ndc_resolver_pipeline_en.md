---
layout: model
title: Pipeline for National Drug Codes (NDC) Sentence Entity Resolver
author: John Snow Labs
name: ndc_resolver_pipeline
date: 2024-09-13
tags: [licensed, en, entity_resolution, clinical, pipeline, ndc]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This advanced pipeline extracts medication entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding National Drug Codes (NDC) codes.

## Predicted Entities

`NDC` 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_resolver_pipeline_en_5.4.1_3.4_1726258876675.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_resolver_pipeline_en_5.4.1_3.4_1726258876675.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ndc_pipeline = PretrainedPipeline("ndc_resolver_pipeline", "en", "clinical/models")

result = ndc_pipeline.fullAnnotate("""The patient was given aspirin 81 mg and metformin 500 mg""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ndc_pipeline = PretrainedPipeline("ndc_resolver_pipeline", "en", "clinical/models")

val result = ndc_pipeline.fullAnnotate("""The patient was given aspirin 81 mg and metformin 500 mg""")

```
</div>

## Results

```bash
+----------------+-----+---+---------+----------+----------------+------------------------------------------------------------+
|           chunk|begin|end|ner_label|  ndc_code|     description|                                                  aux_labels|
+----------------+-----+---+---------+----------+----------------+------------------------------------------------------------+
|   aspirin 81 mg|   22| 34|     DRUG|41250-0780|   aspirin 81 mg|{'packages': "['1 BOTTLE, PLASTIC in 1 PACKAGE (41250-780...|
|metformin 500 mg|   40| 55|     DRUG|62207-0491|metformin 500 mg|{'packages': "['5000 TABLET in 1 POUCH (62207-491-31)', '...|
+----------------+-----+---+---------+----------+----------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.9 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
