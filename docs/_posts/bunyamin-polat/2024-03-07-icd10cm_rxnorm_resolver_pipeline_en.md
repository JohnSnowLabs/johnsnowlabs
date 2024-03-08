---
layout: model
title: Pipeline for ICD-10-CM and RxNorm Sentence Entity Resolver
author: John Snow Labs
name: icd10cm_rxnorm_resolver_pipeline
date: 2024-03-07
tags: [licensed, en, icd-10, rxnorm, pipeline, resolver]
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

This resolver pipeline enables the mapping of extracted clinical entities to ICD10-CM and RxNorm codes. Leveraging sbiobert_base_cased_mli Sentence Bert Embeddings, the model ensures accurate and context-aware associations between clinical entities and relevant medical codes. Users can refer to the following entity labels for pertinent concepts:



**ICD-10-CM entities:** `PROBLEM`, `TEST`, `TREATMENT`, `CEREBROVASCULAR_DISEASE`, `COMMUNICABLE_DISEASE`, `DIABETES`, `DISEASE_SYNDROME_DISORDER`, `EKG_FINDINGS`, `HEART_DISEASE`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `IMAGINGFINDINGS`, `INJURY_OR_POISONING`, `KIDNEY_DISEASE`, `OBESITY`, `ONCOLOGICAL`, `OVERWEIGHT`, `PREGNANCY`, `PSYCHOLOGICAL_CONDITION`, `SYMPTOM`, `VS_FINDING`



**RxNorm entities:** `DRUG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_rxnorm_resolver_pipeline_en_5.3.0_3.0_1709847067810.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_rxnorm_resolver_pipeline_en_5.3.0_3.0_1709847067810.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline
 
resolver_pipeline = PretrainedPipeline("icd10cm_rxnorm_resolver_pipeline", "en", "clinical/models")
 
result = resolver_pipeline.annotate("""The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right upper quadrant pain radiating to her back starting yesterday.
She has a history of infective pericarditis and gestational diabetes mellitus in May 2006.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline
 
val resolver_pipeline = PretrainedPipeline("icd10cm_rxnorm_resolver_pipeline", "en", "clinical/models")
 
val result = resolver_pipeline.annotate("""The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right upper quadrant pain radiating to her back starting yesterday.
She has a history of infective pericarditis and gestational diabetes mellitus in May 2006.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.
""")

```
</div>

## Results

```bash


# RXNORM RESULT

+-------+----------+------+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+
|sent_id| ner_chunk|entity|rxnorm_code| resolution|                                                   all_codes|                                                 resolutions|
+-------+----------+------+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+
|      5|  Coumadin|  DRUG|     202421|  coumadin |202421:::2898:::374998:::1855075:::128793:::1598:::152085...|coumadin [coumadin]:::coumarin [coumarin]:::coumarin Oral...|
|      6|Amiodarone|  DRUG|        703|amiodarone |703:::1663223:::1151983:::1663270:::1151982:::203114:::37...|amiodarone [amiodarone]:::amiodarone Injection:::amiodaro...|
+-------+----------+------+-----------+-----------+------------------------------------------------------------+------------------------------------------------------------+

# ICD-10-CM RESULT

+-------+-----------------------------+-------+------------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|sent_id|                    ner_chunk| entity|icd10cm_code|                    resolution|                                                   all_codes|                                                 resolutions|                                                    hcc_list|
+-------+-----------------------------+-------+------------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+
|      0|                      a cough|PROBLEM|         R05|                        cough |R05:::R05.3:::R05.1:::A37:::R05.2:::R06.01:::R06.7:::R06....|cough [cough]:::chronic cough [chronic cough]:::acute cou...|0||0||0:::1||0||0:::1||0||0:::0||0||0:::1||0||0:::1||0||0...|
|      1|    right upper quadrant pain|PROBLEM|      R10.11|    right upper quadrant pain |R10.11:::M79.621:::R10.31:::M79.651:::M79.631:::M79.601::...|right upper quadrant pain [right upper quadrant pain]:::p...|1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0...|
|      2|       infective pericarditis|PROBLEM|       I30.1|       infective pericarditis |I30.1:::I30:::I31.0:::B33.23:::I01.0:::I30.0:::I31.1:::A3...|infective pericarditis [infective pericarditis]:::acute p...|1||0||0:::0||0||0:::1||0||0:::1||0||0:::1||0||0:::1||0||0...|
|      2|gestational diabetes mellitus|PROBLEM|       O24.4|gestational diabetes mellitus |O24.4:::O24.41:::Z86.32:::O24.11:::O24.81:::P70.2:::O24.0...|gestational diabetes mellitus [gestational diabetes melli...|0||0||0:::0||0||0:::1||0||0:::0||0||0:::0||0||0:::1||0||0...|
+-------+-----------------------------+-------+------------+------------------------------+------------------------------------------------------------+------------------------------------------------------------+------------------------------------------------------------+



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_rxnorm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- TextMatcherInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- Router
- Router
- SentenceEntityResolverModel
- SentenceEntityResolverModel
