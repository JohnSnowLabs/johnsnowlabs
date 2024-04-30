---
layout: model
title: Explain Clinical Document - Social Determinants of Health (SDOH)
author: John Snow Labs
name: explain_clinical_doc_sdoh
date: 2024-04-30
tags: [licensed, en, relation_extraction, clinical, pipeline, sdoh, social_determinants, ner, assertion]
task: [Pipeline Healthcare, Named Entity Recognition, Relation Extraction, Assertion Status]
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

This pipeline is designed to

- extract all clinical/medical entities, which may be considered as Social Determinants of Health (SDOH) entities from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

5 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_en_5.3.1_3.0_1714497776833.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_en_5.3.1_3.0_1714497776833.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_sdoh", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life. The patient disclosed that he had recently lost his job and was facing financial difficulties.
The patient reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his current mental health struggles. 
The patient's family history is significant for a first-degree relative with a history of alcohol abuse. 
The patient also reported a history of smoking but had recently quit and was interested in receiving resources for smoking cessation. 
The patient's medical history is notable for hypertension, which is currently well-controlled with medication. 
The patient denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife. 
The patient is an immigrant and speaks English as a second language. He reported difficulty accessing healthcare due to lack of transportation and insurance status. 
He has had a herniated disc, coronary artery disease (CAD) and diabetes mellitus. The patient has a manic disorder, is presently psychotic and shows impulsive behavior. Bipolar affective disorder, manic state. 
Mental status changes are either due to the tumor or other problems. He is living with his wife, next door to one of his children. He has been disabled since 2001.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_sdoh", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life. The patient disclosed that he had recently lost his job and was facing financial difficulties.
The patient reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his current mental health struggles. 
The patient's family history is significant for a first-degree relative with a history of alcohol abuse. 
The patient also reported a history of smoking but had recently quit and was interested in receiving resources for smoking cessation. 
The patient's medical history is notable for hypertension, which is currently well-controlled with medication. 
The patient denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife. 
The patient is an immigrant and speaks English as a second language. He reported difficulty accessing healthcare due to lack of transportation and insurance status. 
He has had a herniated disc, coronary artery disease (CAD) and diabetes mellitus. The patient has a manic disorder, is presently psychotic and shows impulsive behavior. Bipolar affective disorder, manic state. 
Mental status changes are either due to the tumor or other problems. He is living with his wife, next door to one of his children. He has been disabled since 2001.
""")

```
</div>

## Results

```bash
|    | chunks                          |   begin |   end | entities                  |
|---:|:--------------------------------|--------:|------:|:--------------------------|
|  0 | anxiety                         |      47 |    53 | Mental_Health             |
|  1 | depression                      |      59 |    68 | Mental_Health             |
|  2 | quality of life                 |     101 |   115 | Quality_Of_Life           |
|  3 | financial difficulties          |     189 |   210 | Financial_Status          |
|  4 | childhood trauma                |     247 |   262 | Childhood_Event           |
|  5 | violence                        |     275 |   282 | Violence_Or_Abuse         |
|  6 | abuse                           |     288 |   292 | Violence_Or_Abuse         |
|  7 | mental health struggles         |     349 |   371 | Mental_Health             |
|  8 | alcohol                         |     465 |   471 | Alcohol                   |
|  9 | smoking                         |     520 |   526 | Smoking                   |
| 10 | smoking                         |     596 |   602 | Smoking                   |
| 11 | hypertension                    |     661 |   672 | Hypertension              |
| 12 | substance                       |     758 |   766 | Substance_Use             |
| 13 | sexual activity                 |     775 |   789 | Sexual_Activity           |
| 14 | monogamous                      |     810 |   819 | Sexual_Activity           |
| 15 | wife                            |     850 |   853 | Family_Member             |
| 16 | immigrant                       |     875 |   883 | Population_Group          |
| 17 | English                         |     896 |   902 | Language                  |
| 18 | difficulty accessing healthcare |     938 |   968 | Access_To_Care            |
| 19 | lack of transportation          |     977 |   998 | Symptom                   |
| 20 | insurance status                |    1004 |  1019 | Insurance_Status          |
| 21 | herniated disc                  |    1036 |  1049 | Disease_Syndrome_Disorder |
| 22 | coronary artery disease         |    1052 |  1074 | Heart_Disease             |
| 23 | CAD                             |    1077 |  1079 | Heart_Disease             |
| 24 | diabetes mellitus               |    1086 |  1102 | Diabetes                  |
| 25 | manic disorder                  |    1123 |  1136 | Mental_Health             |
| 26 | psychotic                       |    1152 |  1160 | Mental_Health             |
| 27 | impulsive behavior              |    1172 |  1189 | Mental_Health             |
| 28 | Bipolar affective disorder      |    1192 |  1217 | Mental_Health             |
| 29 | manic                           |    1220 |  1224 | Mental_Health             |
| 30 | Mental status changes           |    1234 |  1254 | Mental_Health             |
| 31 | tumor                           |    1278 |  1282 | Tumor_Finding             |
| 32 | wife                            |    1325 |  1328 | Family_Member             |
| 33 | children                        |    1355 |  1362 | Family_Member             |
| 34 | disabled                        |    1377 |  1384 | Disability                |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_sdoh|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel