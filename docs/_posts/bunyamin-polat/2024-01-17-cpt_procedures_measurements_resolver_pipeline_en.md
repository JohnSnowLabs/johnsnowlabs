---
layout: model
title: Pipeline for Current Procedural Terminology (CPT) Sentence Entity Resolver
author: John Snow Labs
name: cpt_procedures_measurements_resolver_pipeline
date: 2024-01-17
tags: [licensed, en, entity_resolution, clinical, pipeline, cpt]
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

This pipeline extracts `Procedure` and `Measurement` entities and maps them to corresponding Current Procedural Terminology (CPT) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/cpt_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705493213071.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/cpt_procedures_measurements_resolver_pipeline_en_5.2.1_3.0_1705493213071.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("cpt_procedures_measurements_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("cpt_procedures_measurements_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node.
We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma.
At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed, which revealed epithelioid malignant mesothelioma.""")

```
</div>

## Results

```bash
+--------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+
|               chunk|begin|end|ner_label|cpt_code|                                                 resolutions|                                                 all_k_codes|
+--------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+
|      pericardectomy|  239|252|Procedure|   33030|Pericardectomy [Pericardiectomy, subtotal or complete; wi...|33030:::33020:::64746:::49250:::27350:::68520:::32310:::2...|
|chest tube placement|  321|340|Procedure|   39503|Insertion of chest tube [Repair, neonatal diaphragmatic h...|39503:::96440:::32553:::35820:::32100:::36226:::21899:::2...|
|        thoracoscopy|  381|392|Procedure| 1020900|Thoracoscopy [Thoracoscopy]:::Thoracoscopy, surgical; wit...|1020900:::32654:::32668:::1006014:::35820:::32606:::32555...|
+--------------------+-----+---+---------+--------+------------------------------------------------------------+------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_procedures_measurements_resolver_pipeline|
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