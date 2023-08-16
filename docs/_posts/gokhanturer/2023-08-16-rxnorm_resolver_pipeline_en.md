---
layout: model
title: Pipeline to Resolve RxNorm Codes
author: John Snow Labs
name: rxnorm_resolver_pipeline
date: 2023-08-16
tags: [licensed, en, clinical, rxnorm, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps entities with their corresponding RxNorm codes. You’ll just feed your text and it will return the corresponding RxNorm codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.0.1_3.4_1692196822349.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_resolver_pipeline_en_5.0.1_3.4_1692196822349.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("rxnorm_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.fullAnnotate("""The patient was given Adapin 10 MG, coumadn 5 mg""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = new PretrainedPipeline("rxnorm_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.fullAnnotate("""The patient was given Adapin 10 MG, coumadn 5 mg""")

```
</div>

## Results

```bash

+------------+---------+-----------+
|chunk       |ner_chunk|rxnorm_code|
+------------+---------+-----------+
|Adapin 10 MG|DRUG     |1000049    |
|coumadn 5 mg|DRUG     |200883     |
+------------+---------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger