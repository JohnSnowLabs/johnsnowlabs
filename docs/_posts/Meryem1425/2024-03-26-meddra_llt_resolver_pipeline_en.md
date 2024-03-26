---
layout: model
title: Pipeline for MedDRA - Lowest Level Term (LLT) Sentence Entity Resolver
author: John Snow Labs
name: meddra_llt_resolver_pipeline
date: 2024-03-26
tags: [licensed, en, meddra, llt, resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This dedicated pipeline utilizes `sbiobert_base_cased_mli` Sentence Bert Embeddings to extract clinical terms and link them to their corresponding MedDRA LLT (Lowest Level Term) codes. Additionally, it provides the MedDRA Preferred Term codes for each MedDRA LLT code within the `meddra_llt_code` metadata's `all_k_aux_labels`. Furthermore, it conducts mappings of MedDRA LLT codes to MedDRA Preferred Term (PT) codes using the `meddra_llt_pt_mapper` model and to ICD-10 codes using the `meddra_llt_icd10_mapper` model.

This pipeline can extract the following clincial entities: `Procedure`, `Kidney_Disease`, `Cerebrovascular_Disease`, `Heart_Disease`, `Disease_Syndrome_Disorder`, `ImagingFindings`, `Symptom`, `VS_Finding`, `EKG_Findings`, `Communicable_Disease`, `Substance`, `Internal_organ_or_component`, `External_body_part_or_region`, `Modifier`, `Triglycerides`, `Alcohol`, `Smoking`, `Pregnancy`, `Hypertension`, `Obesity`, `Injury_or_Poisoning`, `Test`, `Hyperlipidemia`, `BMI`, `Oncological`, `Psychological_Condition`, `LDL`, `Diabetes`, `PROBLEM`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/meddra_llt_resolver_pipeline_en_5.3.1_3.4_1711474115662.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/meddra_llt_resolver_pipeline_en_5.3.1_3.4_1711474115662.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

meddra_llt_pipeline = PretrainedPipeline.from_disk("meddra_llt_resolver_pipeline")

result = meddra_llt_pipeline.fullAnnotate('This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia.')
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val meddra_llt_pipeline = PretrainedPipeline.from_disk("meddra_llt_resolver_pipeline")

val result = meddra_llt_pipeline.fullAnnotate("This is an 82-year-old male with a history of prior tobacco use, hypertension, chronic renal insufficiency, chronic obstructive pulmonary disease, gastritis, and transient ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia.")
```
</div>

## Results

```bash
+--------------------------------------+-------------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------+
|chunk                                 |label                    |meddra_llt_code|resolution                           |icd10_mappings                                                                     |meddra_pt_mappings                             |
+--------------------------------------+-------------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------+
|tobacco                               |Smoking                  |10067622       |tobacco interaction                  |NONE                                                                               |10067622:Tobacco interaction                   |
|hypertension                          |Hypertension             |10020772       |hypertension                         |O10:Pre-existing hypertension complicating pregnancy, childbirth and the puerperium|10020772:Hypertension                          |
|chronic renal insufficiency           |Kidney_Disease           |10050441       |chronic renal insufficiency          |NONE                                                                               |10064848:Chronic kidney disease                |
|chronic obstructive pulmonary disease |Disease_Syndrome_Disorder|10009033       |chronic obstructive pulmonary disease|J44:Other chronic obstructive pulmonary disease                                    |10009033:Chronic obstructive pulmonary disease |
|gastritis                             |Disease_Syndrome_Disorder|10017853       |gastritis                            |K29.6:Other gastritis                                                              |10017853:Gastritis                             |
|transient ischemic attack             |Cerebrovascular_Disease  |10072760       |transient ischemic attack            |NONE                                                                               |10044390:Transient ischaemic attack            |
|ST elevation                          |PROBLEM                  |10041887       |st elevated                          |NONE                                                                               |10014392:Electrocardiogram ST segment elevation|
|cardiac catheterization               |Procedure                |10048606       |cardiac catheterization              |Y84.0:Cardiac catheterization                                                      |10007815:Catheterisation cardiac               |
|the left main coronary artery stenosis|PROBLEM                  |10090240       |left main coronary artery stenosis   |NONE                                                                               |10011089:Coronary artery stenosis              |
|hypotension                           |VS_Finding               |10021097       |hypotension                          |I95:Hypotension                                                                    |10021097:Hypotension                           |
|bradycardia                           |VS_Finding               |10006093       |bradycardia                          |R00.1:Bradycardia, unspecified                                                     |10006093:Bradycardia                           |
+--------------------------------------+-------------------------+---------------+-------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_llt_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
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
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- Chunk2Doc
- BertSentenceEmbeddings
- SentenceEntityResolverModel
- Resolution2Chunk
- ChunkMapperModel
- ChunkMapperModel