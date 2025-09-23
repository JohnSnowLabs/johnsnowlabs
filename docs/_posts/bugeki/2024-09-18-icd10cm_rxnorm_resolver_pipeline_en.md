---
layout: model
title: Pipeline for ICD-10-CM and RxNorm Sentence Entity Resolver
author: John Snow Labs
name: icd10cm_rxnorm_resolver_pipeline
date: 2024-09-18
tags: [licensed, en, resolver, icd_10_cm, rxnorm, pipeline]
task: Pipeline Healthcare
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can extract clinical conditions and medication entities, map the clinical conditions to their respective ICD-10-CM codes, and medication entities to RxNorm codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. Users can refer to the following entity labels for pertinent concepts: 
- ICD-10-CM entities: PROBLEM, CEREBROVASCULAR_DISEASE, COMMUNICABLE_DISEASE, DIABETES, DISEASE_SYNDROME_DISORDER, EKG_FINDINGS, HEART_DISEASE, HYPERLIPIDEMIA, HYPERTENSION, IMAGINGFINDINGS, INJURY_OR_POISONING, KIDNEY_DISEASE, OBESITY, ONCOLOGICAL, OVERWEIGHT, PREGNANCY, PSYCHOLOGICAL_CONDITION, SYMPTOM, VS_FINDING
- RxNorm entities: DRUG

## Predicted Entities

`ICD-10-CM Code` `Rxnorm Code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10cm_rxnorm_resolver_pipeline_en_5.4.1_3.4_1726643468958.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10cm_rxnorm_resolver_pipeline_en_5.4.1_3.4_1726643468958.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

resolver_pipeline = PretrainedPipeline("icd10cm_rxnorm_resolver_pipeline", "en", "clinical/models")

result = resolver_pipeline.annotate("""The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right-sided chest pain radiating to her back with fever starting yesterday.
She has a history of pericarditis in May 2006 and developed cough with right-sided chest pain.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val resolver_pipeline = PretrainedPipeline("icd10cm_rxnorm_resolver_pipeline", "en", "clinical/models")

val result = resolver_pipeline.annotate("""The patient is a 41-year-old Vietnamese female with a cough that started last week.
She has had right-sided chest pain radiating to her back with fever starting yesterday.
She has a history of pericarditis in May 2006 and developed cough with right-sided chest pain.
MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on Tuesday, August 14, 2007, and her INR was 2.3.
2. Amiodarone 100 mg p.o. daily.""")
```
</div>

## Results

```bash
# RXNORM RESULT

| chunks        | begin | end | code   | all_codes                                           | resolutions                                                                                                                                                                                                                                                                        |
| ------------- | ----- | --- | ------ | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coumadin 1 mg | 282   | 294 | 855289 | [855289, 438737, 208469, 205489, 447086, 205485...  | [warfarin sodium 1 MG [Coumadin], coumarin 1 MG[coumarin 1 MG], terazosin 1 MG Oral Capsule [Hytrin], bumetanide 1 MG Oral Tablet [Bumex], propinox 1 MG[propinox 1 MG], dextrothyroxine 1 MG Oral Tablet [Choloxin]...                                                            |
| Amiodarone    | 369   | 378 | 703    | [703, 1663223, 1151983, 1663270, 1151982, 203114... | [amiodarone[amiodarone], amiodarone Injection[amiodarone Injection], amiodarone Pill[amiodarone Pill], amiodarone Injection [Nexterone][amiodarone Injection [Nexterone]], amiodarone Oral Product[amiodarone Oral Product], amiodarone hydrochloride[amiodarone hydrochloride]... |


# ICD-10-CM RESULT

| chunks                 | begin | end | code   | all_codes                                                | resolutions                                                                                                                                                       |
|------------------------|-------|-----|--------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a cough                | 52    | 58  | R05    | [R05, R05.3, R05.1, A37, R05.2, R06.01...]               | [cough, chronic cough, acute cough, whooping cough, subacute cough, orthopnea...]                                                                                 |
| right-sided chest pain | 96    | 117 | R10.11 | [R10.11, M79.621, M79.604, M79.601, M25.511, M79.631...] | [right upper quadrant pain, pain in right upper arm, pain in right leg, pain in right arm, pain in right shoulder, pain in right forearm...]                      |
| fever                  | 146   | 150 | A68    | [A68, A78, R50.2, M04.1, A96.2, A68.9...]                | [relapsing fevers, q fever, drug induced fever, periodic fever syndromes, lassa fever, relapsing fever, unspecified...]                                           |
| pericarditis           | 193   | 204 | I30.1  | [I30.1, B33.23, I30, I31.0, I01.0, I30.9...]             | [infective pericarditis, viral pericarditis, acute pericarditis, chronic adhesive pericarditis, acute rheumatic pericarditis, acute pericarditis, unspecified...] |
| cough                  | 232   | 236 | R05    | [R05, A37, R05.3, R05.1, R05.2, R06.7...]                | [cough, whooping cough, chronic cough, acute cough, subacute cough, sneezing...]                                                                                  |
| right-sided chest pain | 243   | 264 | R10.11 | [R10.11, M79.621, M79.604, M79.601, M25.511, M79.631...] | [right upper quadrant pain, pain in right upper arm, pain in right leg, pain in right arm, pain in right shoulder, pain in right forearm...]                      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10cm_rxnorm_resolver_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
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
