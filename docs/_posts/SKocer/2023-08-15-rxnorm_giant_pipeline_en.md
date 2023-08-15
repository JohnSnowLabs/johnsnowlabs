---
layout: model
title: RxNorm Code Mapping Pipeline
author: John Snow Labs
name: rxnorm_giant_pipeline
date: 2023-08-15
tags: [licensed, en, clinical, rxnorm, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline maps RxNorm codes to their corresponding drug brand names, rxnorm extension brand names, action mappings, treatment mappings, UMLS codes, NDC product codes and NDC package codes. You’ll just feed white space-delimited RxNorm codes and get the result.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_giant_pipeline_en_5.0.1_3.2_1692125511164.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_giant_pipeline_en_5.0.1_3.2_1692125511164.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```pytho
from sparknlp.pretrained import PretrainedPipeline

rxnorm_pipeline = PretrainedPipeline("rxnorm_giant_pipeline", "en", "clinical/models")

result = rxnorm_pipeline.fullAnnotate("""6809 153010 103971""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val rxnorm_pipeline = new PretrainedPipeline("rxnorm_giant_pipeline", "en", "clinical/models")

val result = rxnorm_pipeline.fullAnnotate("""6809 153010 103971""")
```
</div>

## Results

```bash

+-----------+--------------------------------------------------+--------------------------------------------------+---------------+------------------+-------------+--------------------+--------------------+
|rxnorm_code|                                brandname_mappings|                                extension_mappings|action_mappings|treatment_mappings|umls_mappings|ndc_product_mappings|ndc_package_mappings|
+-----------+--------------------------------------------------+--------------------------------------------------+---------------+------------------+-------------+--------------------+--------------------+
|       6809|Actoplus Met (metformin):::Avandamet (metformin...|A FORMIN (metformin):::ABERIN MAX (metformin)::...|           NONE|              NONE|     C0025598|          38779-2126|       38779-2126-04|
|     153010|                                     Advil (Advil)|                                              NONE|      Analgesic|       Period Pain|     C0593507|                NONE|                NONE|
|     103971|Zydol (tramadol hydrochloride 50 MG Oral Capsul...|                                              NONE|      Analgesic|              Pain|     C0353664|                NONE|                NONE|
+-----------+--------------------------------------------------+--------------------------------------------------+---------------+------------------+-------------+--------------------+--------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_giant_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|56.2 MB|

## Included Models

- DocumentAssembler
- TokenizerModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
- ChunkMapperModel
