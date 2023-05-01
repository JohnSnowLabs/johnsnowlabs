---
layout: model
title: Pipeline to Mapping RxNorm Codes with Corresponding National Drug Codes (NDC)
author: John Snow Labs
name: rxnorm_ndc_mapping
date: 2023-03-29
tags: [en, licensed, clinical, pipeline, chunk_mapping, rxnorm, ndc]
task: Chunk Mapping
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps RXNORM codes to NDC codes without using any text data. You’ll just feed white space-delimited RXNORM codes and it will return the corresponding two different types of ndc codes which are called `package ndc` and `product ndc`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.3.2_3.2_1680121244814.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_ndc_mapping_en_4.3.2_3.2_1680121244814.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")

result = pipeline.fullAnnotate(1652674 259934)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("rxnorm_ndc_mapping", "en", "clinical/models")

val result = pipeline.fullAnnotate(1652674 259934)
```
</div>

## Results

```bash

{'document': ['1652674 259934'],
'package_ndc': ['62135-0625-60', '13349-0010-39'],
'product_ndc': ['46708-0499', '13349-0010'],
'rxnorm_code': ['1652674', '259934']}

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_ndc_mapping|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.0 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel
- ChunkMapperModel