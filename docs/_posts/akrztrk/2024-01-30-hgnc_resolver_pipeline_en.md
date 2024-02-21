---
layout: model
title: Pipeline for HUGO Gene Nomenclature Committee (HGNC)
author: John Snow Labs
name: hgnc_resolver_pipeline
date: 2024-01-30
tags: [licensed, en, clinical, hgnc, pipeline, resolver]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts `GENE` entities and maps them to their corresponding [HUGO Gene Nomenclature Committee (HGNC)](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HGNC/index.html) codes using `sbiobert_base_cased_mli` sentence embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hgnc_resolver_pipeline_en_5.2.1_3.4_1706635360103.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hgnc_resolver_pipeline_en_5.2.1_3.4_1706635360103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

hgnc_pipeline = PretrainedPipeline("hgnc_resolver_pipeline", "en", "clinical/models")

text = """During today's consultation, we reviewed the results of the comprehensive genetic analysis performed on the patient. This analysis uncovered complex interactions between several genes: DUX4, DUX4L20, FBXO48, MYOD1, and PAX7. These findings are significant as they provide new understanding of the molecular pathways that are involved in muscle differentiation and may play a role in the development and progression of muscular dystrophies in this patient."""

result = hgnc_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val hgnc_pipeline = PretrainedPipeline("hgnc_resolver_pipeline", "en", "clinical/models")

val text = """During today's consultation, we reviewed the results of the comprehensive genetic analysis performed on the patient. This analysis uncovered complex interactions between several genes: DUX4, DUX4L20, FBXO48, MYOD1, and PAX7. These findings are significant as they provide new understanding of the molecular pathways that are involved in muscle differentiation and may play a role in the development and progression of muscular dystrophies in this patient."""

val result = hgnc_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+-------+-----+---+----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
| chunks|begin|end|      code|                                         all_codes|                                       resolutions|                                     all_distances|
+-------+-----+---+----------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|   DUX4|  185|188|HGNC:50800|[HGNC:50800, HGNC:3070, HGNC:32183, HGNC:38686,...|[DUX4 [double homeobox 4], DUSP4 [dual specific...|[0.0000, 0.0210, 0.0221, 0.0239, 0.0276, 0.0302...|
|DUX4L20|  191|197|HGNC:50801|[HGNC:50801, HGNC:39776, HGNC:31982, HGNC:26230...|[DUX4L20 [double homeobox 4 like 20 (pseudogene...|[0.0000, 0.0696, 0.0698, 0.0744, 0.0756, 0.0767...|
| FBXO48|  200|205|HGNC:33857|[HGNC:33857, HGNC:4930, HGNC:16653, HGNC:13114,...|[FBXO48 [F-box protein 48], ZBTB48 [zinc finger...|[0.0000, 0.0495, 0.0503, 0.0510, 0.0601, 0.0593...|
|  MYOD1|  208|212| HGNC:7611|[HGNC:7611, HGNC:13879, HGNC:7613, HGNC:7582, H...|[MYOD1 [myogenic differentiation 1], MYO1H [myo...|[0.0000, 0.0614, 0.0634, 0.0634, 0.0696, 0.0709...|
|   PAX7|  219|222| HGNC:8621|[HGNC:8621, HGNC:8748, HGNC:9351, HGNC:8792, HG...|[PAX7 [paired box 7], PCSK7 [proprotein convert...|[0.0000, 0.1042, 0.1036, 0.1046, 0.1056, 0.1053...|
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
