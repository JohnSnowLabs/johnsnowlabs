---
layout: model
title: Pipeline for HGNC Codes
author: John Snow Labs
name: hgnc_resolver_pipeline
date: 2024-01-28
tags: [licensed, en, clinical, hgnc, pipeline, resolver]
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

This pipline extracts `GENE` entities and maps them to their corresponding HGNC codes using `sbiobert_base_cased_mli` sentence embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hgnc_resolver_pipeline_en_5.2.1_3.0_1706406345731.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hgnc_resolver_pipeline_en_5.2.1_3.0_1706406345731.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

hgnc_pipeline = PretrainedPipeline("hgnc_resolver_pipeline", "en", "clinical/models")

text = """Recent studies have suggested a potential link between the double homeobox 4 like 20 (pseudogene), also known as DUX4L20, and FBXO48 and RNA guanine-7 methyltransferase"""

result = hgnc_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val hgnc_pipeline = PretrainedPipeline("hgnc_resolver_pipeline", "en", "clinical/models")

val text = """Recent studies have suggested a potential link between the double homeobox 4 like 20 (pseudogene), also known as DUX4L20, and FBXO48 and RNA guanine-7 methyltransferase"""

val result = hgnc_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-------+-----+---+----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
| chunks|begin|end|      code|                                         all_codes|                                       resolutions|                                     all_distances|
+-------+-----+---+----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|DUX4L20|  113|119|HGNC:50801|[HGNC:50801, HGNC:39776, HGNC:31982, HGNC:26230...|[DUX4L20 [double homeobox 4 like 20 (pseudogene...|[0.0000, 0.0696, 0.0698, 0.0744, 0.0756, 0.0767...|
| FBXO48|  126|131|HGNC:33857|[HGNC:33857, HGNC:4930, HGNC:16653, HGNC:13114,...|[FBXO48 [F-box protein 48], ZBTB48 [zinc finger...|[0.0000, 0.0495, 0.0503, 0.0510, 0.0601, 0.0593...|
+-------+-----+---+----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hgnc_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

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
