---
layout: model
title: Pipeline for Anatomic Therapeutic Chemical (ATC) Sentence Entity Resolver
author: John Snow Labs
name: atc_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, entity_resolution, clinical, pipeline, atc]
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

This advanced pipeline extracts `DRUG` entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Anatomic Therapeutic Chemical (ATC) codes. 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/atc_resolver_pipeline_en_5.2.1_3.2_1705491262682.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/atc_resolver_pipeline_en_5.2.1_3.2_1705491262682.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("atc_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("She was immediately given hydrogen peroxide 30 mg and amoxicillin twice daily for 10 days to treat the infection on her leg. She has a history of taking magnesium hydroxide.")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("atc_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("She was immediately given hydrogen peroxide 30 mg and amoxicillin twice daily for 10 days to treat the infection on her leg. She has a history of taking magnesium hydroxide.")

```
</div>

## Results

```bash
|    | chunks              |   begin |   end | entities   | atc_code   | resolutions         |
|---:|:--------------------|--------:|------:|:-----------|:-----------|:--------------------|
|  0 | hydrogen peroxide   |      26 |    42 | DRUG       | A01AB02    | hydrogen peroxide   |
|  1 | amoxicillin         |      54 |    64 | DRUG       | J01CA04    | amoxicillin         |
|  2 | magnesium hydroxide |     153 |   171 | DRUG       | A02AA04    | magnesium hydroxide |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|atc_resolver_pipeline|
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
