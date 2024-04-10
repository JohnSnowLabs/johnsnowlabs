---
layout: model
title: Pipeline for MedDRA - Preferred Term (PT) Sentence Entity Resolver
author: John Snow Labs
name: meddra_pt_resolver_pipeline
date: 2024-03-26
tags: [licensed, en, meddra, pt, resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This dedicated pipeline extracts clinical terms and utilizes `sbiobert_base_cased_mli` Sentence Bert Embeddings to link them to their corresponding MedDRA PT (Preferred Term) codes. Additionally, it provides the MedDRA Preferred Term codes for each MedDRA PT code within the `meddra_pt_code` metadata's `all_k_aux_labels`. Furthermore, it conducts mappings of MedDRA PT codes to MedDRA Lowest Level Term (LLT) codes using the `meddra_pt_llt_mapper` model and to ICD-10 codes using the `meddra_pt_icd10_mapper` model.

This pipeline can extract the following clincial entities: `Procedure`, `Kidney_Disease`, `Cerebrovascular_Disease`, `Heart_Disease`, `Disease_Syndrome_Disorder`, `ImagingFindings`, `Symptom`, `VS_Finding`, `EKG_Findings`, `Communicable_Disease`, `Substance`, `Internal_organ_or_component`, `External_body_part_or_region`, `Modifier`, `Triglycerides`, `Alcohol`, `Smoking`, `Pregnancy`, `Hypertension`, `Obesity`, `Injury_or_Poisoning`, `Test`, `Hyperlipidemia`, `BMI`, `Oncological`, `Psychological_Condition`, `LDL`, `Diabetes`, `PROBLEM`.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>


## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

meddra_pt_pipeline = PretrainedPipeline.from_disk("meddra_pt_resolver_pipeline")

result = meddra_pt_pipeline.fullAnnotate('This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis.')
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val meddra_pt_pipeline = PretrainedPipeline.from_disk("meddra_pt_resolver_pipeline")

val result = meddra_pt_pipeline.fullAnnotate("This is an 82-year-old male with a history of prior tobacco use, benign hypertension, chronic renal insufficiency, chronic bronchitis, gastritis, and ischemic attack. He initially presented to Braintree with ST elevation and was transferred to St. Margaret’s Center. He underwent cardiac catheterization because of the left main coronary artery stenosis, which was complicated by hypotension and bradycardia. We describe the side effects of 5-FU in a colon cancer patient who suffered mucositis and dermatitis.")
```
</div>

## Results

```bash
+--------------------------------------+-------------------------+--------------+--------------------------+-------------------------------------------------+-----------------------------------+
|chunk                                 |label                    |meddra_pt_code|resolution                |icd10_mappings                                   |meddra_llt_mappings                |
+--------------------------------------+-------------------------+--------------+--------------------------+-------------------------------------------------+-----------------------------------+
|tobacco                               |Smoking                  |10067622      |tobacco interaction       |NONE                                             |10067622:Tobacco interaction       |
|benign hypertension                   |PROBLEM                  |10049079      |labile hypertension       |NONE                                             |10049079:Labile hypertension       |
|chronic renal insufficiency           |Kidney_Disease           |10038435      |renal failure             |N19:Unspecified kidney failure                   |10016149:Failure kidney            |
|chronic bronchitis                    |PROBLEM                  |10006458      |bronchitis chronic        |J41.0:Simple chronic bronchitis                  |10003568:Asthmatoid bronchitis     |
|gastritis                             |Disease_Syndrome_Disorder|10017853      |gastritis                 |K29:Gastritis and duodenitis                     |10000769:Acute gastritis           |
|ischemic attack                       |Cerebrovascular_Disease  |10061216      |infarction                |NONE                                             |10021762:Infarction NOS            |
|ST elevation                          |PROBLEM                  |10049785      |atrial pressure increased |NONE                                             |10049785:Atrial pressure increased |
|cardiac catheterization               |Procedure                |10007815      |catheterisation cardiac   |Y84.0:Cardiac catheterization                    |10007527:Cardiac catheterisation   |
|the left main coronary artery stenosis|PROBLEM                  |10011089      |coronary artery stenosis  |NONE                                             |10011089:Coronary artery stenosis  |
|hypotension                           |VS_Finding               |10021097      |hypotension               |I95:Hypotension                                  |10005753:Blood pressure low        |
|bradycardia                           |VS_Finding               |10006093      |bradycardia               |R00.1:Bradycardia, unspecified                   |10006093:Bradycardia               |
|the side effects                      |PROBLEM                  |10054126      |post procedural discomfort|NONE                                             |10054126:Post procedural discomfort|
|a colon cancer                        |PROBLEM                  |10009944      |colon cancer              |C18:Malignant neoplasm of colon                  |10006903:Caecal cancer             |
|mucositis                             |ADE                      |10028128      |mucositis management      |NONE                                             |10028128:Mucositis management      |
|dermatitis                            |ADE                      |10012431      |dermatitis                |L27:Dermatitis due to substances taken internally|10000593:Acrodermatitis            |
+--------------------------------------+-------------------------+--------------+--------------------------+-------------------------------------------------+-----------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|meddra_pt_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|

## References
This pipeline is prepared using the models that are trained with the January 2024 release (v27) of MedDRA dataset.

**To utilize this pipeline, possession of a valid MedDRA license is requisite. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**

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
