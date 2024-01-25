---
layout: model
title: Pipeline for Medical Subject Heading (MeSH) Sentence Entity Resolver
author: John Snow Labs
name: mesh_resolver_pipeline
date: 2024-01-25
tags: [licensed, en, entity_resolution, clinical, pipeline, mesh]
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

This advanced pipeline extracts clinical entities from clinical texts and utilizes the `sbiobert_base_cased_mli` Sentence Bert Embeddings to map these entities to their corresponding Medical Subject Heading (MeSH) codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/mesh_resolver_pipeline_en_5.2.1_3.0_1706187452795.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/mesh_resolver_pipeline_en_5.2.1_3.0_1706187452795.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("mesh_resolver_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, which were performed, which revealed malignant mesothelioma.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("mesh_resolver_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy with fluid biopsies, which were performed, which revealed malignant mesothelioma.""")

```
</div>

## Results

```bash
|   |                     chunks | begin | end |  entities |  mesh_code |             description |                                       resolutions |
|--:|---------------------------:|------:|----:|----------:|-----------:|------------------------:|--------------------------------------------------:|
| 0 |                 chest pain |    38 |  47 |   PROBLEM |    D002637 |              Chest Pain | Chest Pain:::Chronic Pain:::Neck Pain:::Should... |
| 1 | bilateral pleural effusion |    67 |  92 |   PROBLEM |    D010996 |        Pleural Effusion | Pleural Effusion:::Pericardial Effusion:::Pulm... |
| 2 |              the pathology |   140 | 152 |      TEST |    D010336 |               Pathology | Pathology:::Pathologic Processes:::Anus Diseas... |
| 3 |         the pericardectomy |   168 | 185 | TREATMENT |    D010492 |         Pericardiectomy | Pericardiectomy:::Pulpectomy:::Pleurodesis:::C... |
| 4 |               mesothelioma |   226 | 237 |   PROBLEM | D000086002 | Mesothelioma, Malignant | Mesothelioma, Malignant:::Malignant mesenchyma... |
| 5 |       chest tube placement |   254 | 273 | TREATMENT |    D015505 |             Chest Tubes | Chest Tubes:::Thoracic Surgical Procedures:::T... |
| 6 |      drainage of the fluid |   279 | 299 |   PROBLEM |    D004322 |                Drainage | Drainage:::Fluid Shifts:::Bonain's liquid:::Li... |
| 7 |               thoracoscopy |   314 | 325 | TREATMENT |    D013906 |            Thoracoscopy | Thoracoscopy:::Thoracoscopes:::Thoracic Cavity... |
| 8 |             fluid biopsies |   332 | 345 |      TEST | D000073890 |           Liquid Biopsy | Liquid Biopsy:::Peritoneal Lavage:::Cyst Fluid... |
| 9 |     malignant mesothelioma |   385 | 406 |   PROBLEM | D000086002 | Mesothelioma, Malignant | Mesothelioma, Malignant:::Malignant mesenchyma... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|mesh_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|

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
