---
layout: model
title: Pipeline to Resolve ICD-10-CM Codes
author: John Snow Labs
name: icd10cm_resolver_pipeline
date: 2024-08-22
tags: [licensed, en, resolver, icd_10cm, chunk_mapping, pipeline, clinical]
task: [Pipeline Healthcare, Entity Resolution]
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can extract clinical conditions, and map the clinical conditions to their respective ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. Users can refer to the following entity labels for pertinent concepts:
ICD-10-CM entities: `PROBLEM`, `CEREBROVASCULAR_DISEASE`, `COMMUNICABLE_DISEASE`, `DIABETES`, `DISEASE_SYNDROME_DISORDER`, `EKG_FINDINGS`, `HEART_DISEASE`, `HYPERLIPIDEMIA`, `HYPERTENSION`, `IMAGINGFINDINGS`, `INJURY_OR_POISONING`, `KIDNEY_DISEASE`, `OBESITY`, `ONCOLOGICAL`, `OVERWEIGHT`, `PREGNANCY`, `PSYCHOLOGICAL_CONDITION`, `SYMPTOM`, `VS_FINDING`

## Predicted Entities

`Cerebrovascular_Disease`, `Communicable_Disease`, `Diabetes`, `Disease_Syndrome_Disorder`, `EKG_Findings`, `Heart_Disease`, `Hyperlipidemia`, `Hypertension`, `ImagingFindings`, `Injury_or_Poisoning`, `Kidney_Disease`, `Obesity`, `Oncological`, `Overweight`, `PROBLEM`, `Pregnancy`, `Psychological_Condition`, `Symptom`, `VS_Finding`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.1.Code_Mapping_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_resolver_pipeline_en_5.4.0_3.0_1724329209466.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_resolver_pipeline_en_5.4.0_3.0_1724329209466.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("icd10cm_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years and anisakiasis. Also, it was reported that fetal and neonatal hemorrhage.""")


```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val result = resolver_pipeline.fullAnnotate("""A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years and anisakiasis. Also, it was reported that fetal and neonatal hemorrhage.""")


```
</div>

## Results

```bash


|   |                        chunks | entities | icd10cm_code |
|--:|------------------------------:|---------:|-------------:|
| 0 | gestational diabetes mellitus |  PROBLEM |        O24.4 |
| 1 |                   anisakiasis |  PROBLEM |        B81.0 |
| 2 | fetal and neonatal hemorrhage |  PROBLEM |        P54.5 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.6 GB|

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
- ChunkMapperModel
- ChunkMapperFilterer
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- ResolverMerger
