---
layout: model
title: ICD-10-CM Code Mapping Pipeline
author: John Snow Labs
name: icd10cm_multi_mapper_pipeline
date: 2023-08-16
tags: [licensed, en, clinical, icd10cm, pipeline]
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

This pretrained pipeline maps ICD-10-CM codes to their corresponding billable mappings, hcc codes, cause mappings, claim mappings, SNOMED codes, UMLS codes and ICD-9 codes without using any text data. You’ll just feed white space-delimited ICD-10-CM codes and get the result.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_multi_mapper_pipeline_en_5.0.1_3.4_1692196062006.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_multi_mapper_pipeline_en_5.0.1_3.4_1692196062006.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

icd10cm_pipeline = PretrainedPipeline("icd10cm_multi_mapper_pipeline", "en", "clinical/models")

result = icd10cm_pipeline.fullAnnotate("""Z833 D66 G43.83""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val icd10cm_pipeline = new PretrainedPipeline("icd10cm_multi_mapper_pipeline", "en", "clinical/models")

val result = icd10cm_pipeline.fullAnnotate("""Z833 D66 G43.83""")

```
</div>

## Results

```bash

|    | icd10cm_code   | bill_mappings   | hcc_mappings   | cause_mappings           | claim_mappings   | snomed_mappings   | umls_mappings   | icd9_mappings   |
|---:|:---------------|:----------------|:---------------|:-------------------------|:-----------------|:------------------|:----------------|:----------------|
|  0 | D66            | 1               | 46             | Nutritional deficiencies | NONE             | 438599002         | C0019069        | 2860            |
|  1 | Z833           | NONE            | NONE           | NONE                     | NONE             | 160402005         | C0260526        | V180            |
|  2 | G43.83         | 0               | 0              | Headache disorders       | G43.83           | NONE              | NONE            | NONE            |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_multi_mapper_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|5.9 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- DocMapperModel
- DocMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel