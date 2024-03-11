---
layout: model
title: Pipeline for SNOMED Concept, All Concepts Version
author: John Snow Labs
name: snomed_resolver_pipeline
date: 2024-03-11
tags: [licensed, en, snomed, pipeline, resolver, auxconcepts, findings]
task: [Entity Resolution, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline extracts clinical entities and maps them to their corresponding SNOMED codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. This is also capable of extracting `Clinical Findings `, `Morph Abnormality`, `Clinical Drug`, `Clinical Drug Form`, `Procedure`, `Substance`, `Physical Object`, and `Body Structure` concepts of SNOMED codes.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_resolver_pipeline_en_5.3.0_3.0_1710189594337.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_resolver_pipeline_en_5.3.0_3.0_1710189594337.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("snomed_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.fullAnnotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine. He was subsequently transferred to the CCU for close monitoring.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("snomed_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.fullAnnotate("""This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. He required atropine, IV fluids, and dopamine. He was subsequently transferred to the CCU for close monitoring.""")

```
</div>

## Results

```bash

+--------------------------------------+-------------------------+--------------+-----------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                                 chunk|                    label|   snomed_code|                                     resolution|                                                             all_codes|                                                       all_resolutions|                                                        all_aux_labels|
+--------------------------------------+-------------------------+--------------+-----------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+
|                               tobacco|                  Smoking|      57264008|                                        tobacco|57264008:::102407002:::39953003:::159882006:::102408007:::722496004...|tobacco:::tobacco smoke:::tobacco - substance:::tobacco processor::...|Organism:::Substance:::Substance:::Social Context:::Substance:::Phy...|
|                          hypertension|             Hypertension|     161501007|                              h/o: hypertension|161501007:::73578008:::160357008:::268607006:::417312002:::27594400...|h/o: hypertension:::hyperdistension:::fh: hypertension:::hypertensi...|Context-dependent:::Morph Abnormality:::Context-dependent:::Observa...|
|           chronic renal insufficiency|           Kidney_Disease|73901000119107|                 history of renal insufficiency|73901000119107:::414417004:::1259460004:::472953006:::289916006:::1...|history of renal insufficiency:::history of - renal failure:::posto...|Context-dependent:::Context-dependent:::No_Concept_Class:::Context-...|
| chronic obstructive pulmonary disease|Disease_Syndrome_Disorder|     394702007|chronic obstructive pulmonary disease follow-up|394702007:::866204005:::395159008:::390891009:::702839006:::2704730...|chronic obstructive pulmonary disease follow-up:::consultation for ...|Procedure:::Procedure:::Context-dependent:::Procedure:::Location:::...|
|                             gastritis|Disease_Syndrome_Disorder|     413241009|                         suspicion of gastritis|413241009:::1163521007:::1163522000:::1204466001:::1197706007:::956...|suspicion of gastritis:::enterococcal gastritis:::enteroviral gastr...|Context-dependent:::No_Concept_Class:::No_Concept_Class:::No_Concep...|
|             transient ischemic attack|  Cerebrovascular_Disease|     473129008|            suspected transient ischemic attack|473129008:::161511000:::736288002:::1204218005:::1208871009:::55470...|suspected transient ischemic attack:::history of transient ischaemi...|Context-dependent:::Context-dependent:::Record Artifact:::No_Concep...|
|                          ST elevation|              snomed_term|     164931005|                                   st elevation|164931005:::277203001:::117144008:::255456001:::711583000:::2635600...|st elevation:::suprasellar extension:::upper parasternal region:::e...|Observable Entity:::Qualifier Value:::Body Structure:::Qualifier Va...|
|               cardiac catheterization|                Procedure|      41976001|                        cardiac catheterization|41976001:::705923009:::721968000:::467735004:::129085009:::42531500...|cardiac catheterization:::cardiac catheter:::cardiac catheterizatio...|Procedure:::Physical Object:::Record Artifact:::Physical Object:::Q...|
|the left main coronary artery stenosis|                  PROBLEM|    1255621004| distal left coronary artery main stem stenosis|1255621004:::1255569006:::1255624007:::1255265004:::1255622006:::12...|distal left coronary artery main stem stenosis:::ostial left main c...|No_Concept_Class:::No_Concept_Class:::No_Concept_Class:::No_Concept...|
|                           hypotension|               VS_Finding|     241727003|                            induced hypotension|241727003:::1182007:::266695002:::472960000:::408497003:::4382004::...|induced hypotension:::hypotensive agent:::hypothermia with hypotens...|Procedure:::Pharma/Biol Product:::Procedure:::Context-dependent:::P...|
|                           bradycardia|               VS_Finding|    1217429005|                       asymptomatic bradycardia|1217429005:::690461000119106:::65723001:::285666008:::1182007:::241...|asymptomatic bradycardia:::history of bradycardia:::decreased barom...|No_Concept_Class:::Context-dependent:::Physical Force:::Physical Fo...|
|                              atropine|          Drug_Ingredient|      73949004|                                       atropine|73949004:::105075009:::349945006:::410493009:::74237004:::50507004:...|atropine:::atropine measurement:::oral atropine:::atropinization:::...|Pharma/Biol Product:::Procedure:::Clinical Drug Form:::Procedure:::...|
|                             IV fluids|                TREATMENT|     118431008|                                       iv fluid|118431008:::82449006:::47625008:::261841005:::261842003:::9778000::...|iv fluid:::iv catheter:::iv route:::iv/c:::iv/r:::iv cmv:::intraven...|Substance:::Physical Object:::Qualifier Value:::Qualifier Value:::Q...|
|                              dopamine|          Drug_Ingredient|      59187003|                                       dopamine|59187003:::412383006:::37484001:::32779004:::412845004:::713493000:...|dopamine:::dopamine agent:::dopamine receptor:::dopamine measuremen...|Pharma/Biol Product:::Substance:::Substance:::Procedure:::Procedure...|
+--------------------------------------+-------------------------+--------------+-----------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+----------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- MedicalNerModel
- NerConverter
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
