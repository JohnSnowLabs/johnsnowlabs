---
layout: model
title: Pipeline for Snomed Codes - Procedure and Measurements Version
author: John Snow Labs
name: snomed_procedures_measurements_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, snomed, pipeline, resolver, procedure, measurements]
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

This pipeline extracts `Procedure` and `Measurements` entities and maps them to their corresponding SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705511450333.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705511450333.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

snomed_pipeline = PretrainedPipeline("snomed_procedures_measurements_resolver_pipeline", "en", "clinical/models")

text = """She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma."""

result = snomed_pipeline.fullAnnotate(text)

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val snomed_pipeline = PretrainedPipeline("snomed_procedures_measurements_resolver_pipeline", "en", "clinical/models")

val text = """She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma."""

val result = snomed_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

+--------------------+-----+---+---------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
|              chunks|begin|end|     code|                                                        all_codes|                                                      resolutions|                                                    all_distances|
+--------------------+-----+---+---------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+
|      pericardectomy|  239|252| 34646007|[34646007, 13830001, 58380004, 67057001, 232191001, 50070009, ...|[Pericardiectomy, Incision of pericardium, Pericardiostomy, Ph...|[0.0000, 0.0703, 0.0763, 0.1048, 0.1031, 0.1148, 0.1167, 0.119...|
|chest tube placement|  321|340|264957007|[264957007, 55628002, 290649006, 238327005, 297941000000109, 1...|[Insertion of pleural tube drain, Maintenance of thoracic drai...|[0.0331, 0.0768, 0.1047, 0.1082, 0.1126, 0.1143, 0.1245, 0.128...|
|        thoracoscopy|  381|392| 14671001|[14671001, 430927004, 367408005, 229317003, 387640008, 1201600...|[Thoracoscopy, Thoracoscopic procedure, Incision of chest wall...|[0.0000, 0.0437, 0.0875, 0.0943, 0.1135, 0.1081, 0.1159, 0.123...|
+--------------------+-----+---+---------+-----------------------------------------------------------------+-----------------------------------------------------------------+-----------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_procedures_measurements_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.5 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
