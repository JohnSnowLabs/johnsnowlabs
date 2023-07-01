---
layout: model
title: Pipeline to Resolve ICD10-GM Codes (German)
author: John Snow Labs
name: icd10gm_resolver_pipeline
date: 2023-07-01
tags: [licensed, de, clinical, icd10gm, resolver, pretrained_pipeline]
task: Entity Resolution
language: de
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps extracted entities to ICD10-GM codes. You’ll just feed your text and it will return the corresponding  ICD10-GM codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10gm_resolver_pipeline_de_4.4.4_3.0_1688200429898.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10gm_resolver_pipeline_de_4.4.4_3.0_1688200429898.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("icd10gm_resolver_pipeline", "de", "clinical/models")

text = """Dyspnoe"""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("icd10gm_resolver_pipeline", "de", "clinical/models")

val text = """Dyspnoe"""

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash

|    | chunks  | code    | resolutions                                                            | all_codes                                       | all_distances                                             |
|---:|:--------|:--------|:----------------------------------------------------------------------:|------------------------------------------------:|:----------------------------------------------------------|
|  0 | Dyspnoe | R06.0   |Dyspnoe:::Dysphagie:::Dysurie:::Dyspareunie:::Dysthymia:::Dystonie:::...| R06.0:::R13:::R30.0:::N94.1:::F34.1:::G24:::... | 0.0000:::1.0966:::1.1766:::1.2127:::1.2228:::1.3126:::... |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10gm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|de|
|Size:|1.1 GB|

## Included Models

- DocumentAssembler
- TokenizerModel
- XlmRoBertaEmbeddings
- SentenceEmbeddings
- SentenceEntityResolverModel