---
layout: model
title: Clinical Drugs to UMLS Code Mapping
author: John Snow Labs
name: umls_drug_resolver_pipeline
date: 2024-12-24
tags: [licensed, en, resolver, clinical, umls, pipeline]
task: [Pipeline Healthcare, Chunk Mapping]
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities (Clinical Drugs) with their corresponding UMLS CUI codes. You’ll just feed your text and it will return the corresponding UMLS codes.

## Predicted Entities

`DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_drug_resolver_pipeline_en_5.5.1_3.4_1735038964492.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_drug_resolver_pipeline_en_5.5.1_3.4_1735038964492.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("umls_drug_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""The patient was given Adapin 10 MG, coumadn 5 mg.""")

```

{:.jsl-block}
```python

resolver_pipeline = nlp.PretrainedPipeline("umls_drug_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""The patient was given Adapin 10 MG, coumadn 5 mg.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("umls_drug_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.annotate("""The patient was given Adapin 10 MG, coumadn 5 mg.""")

```
</div>

## Results

```bash

+------------+---------+---------+
|chunk       |ner_label|umls_code|
+------------+---------+---------+
|Adapin 10 MG|DRUG     |C1382178 |
|coumadn 5 mg|DRUG     |C1368171 |
+------------+---------+---------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_drug_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger
