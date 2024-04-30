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

Clinical Entity Labels:

`Access_To_Care`, `Age`, `Alcohol`, `Childhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diabetes`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`, `Disease_Syndrome_Disorder`, `Heart_Disease`, `Kidney_Disease`, `Hyperlipidemia`, `Hypertension`, `Tumor_Finding`, `Cancer_Diagnosis`, `Cancer_Surgery`, `Metastasis`, `Cerebrovascular_Disease`, `Symptom`, `Drug`

Assertion Status Labels:

`Present`, `Absent`, `Possible`, `Past`, `Hypotetical`, `Someone_Else`

Relation Extraction Labels:

`Access_To_Care-Financial_Status`,`Access_To_Care–Housing`,`Access_To_Care–Income`, `Access_To_Care–Language`, `Access_To_Care-Population_Group`,`Access_To_Care-Race_Ethnicity`, `Access_To_Care-Social_Support`,`Access_To_Care-Substance_Use`,`Access_To_Care–Transportation`,`Age–Alcohol`, `Age-Eating_Disorder`,`Age–Diet`, `Age-Mental_Health`,`Age–Obesity`,`Age-Sexual_Activity`,`Age-Sexual_Orientation`,`Age–Smoking`,`Age-Substance_Use`,`Age-Violence_Or_Abuse`,`Alcohol-Childhood_Event`,`Alcohol–Employment`, `Alcohol–Gender`, `Alcohol–Housing`, `Alcohol-Legal_Issues`, `Alcohol-Mental_Health`, `Alcohol-Quality_Of_Life`,`Alcohol-Race_Ethnicity`,`Alcohol–Smoking`, `Alcohol-Substance_Use`,`Alcohol-Violence_Or_Abuse`, `Childhood_Event–Gender`,`Childhood_Event-Mental_Health`, `Childhood_Event-Race_Ethnicity`, `Childhood_Event–Smoking`, `Childhood_Event-Substance_Use`,`Childhood_Event-Violence_Or_Abuse`, `Community_Safety-Quality_Of_Life`,`Community_Safety-Violence_Or_Abuse`,`Diet-Eating_Disorder`,`Diet–Exercise`,`Diet–Gender`,`Diet–Obesity`, `Disability–Education`,`Disability–Employment`, `Disability-Financial_Status`, `Disability–Housing`,`Disability–Income`,`Disability-Insurance_Status`,`Disability-Mental_Health`, `Disability-Quality_Of_Life`,`Disability-Social_Exclusion`,`Disability-Social_Support`,`Disability-Substance_Use`,`Eating_Disorder-Food_Insecurity`, `Eating_Disorder-Mental_Health`,`Eating_Disorder–Obesity`,`Eating_Disorder-Substance_Use`,`Education–Employment`,`Education-Financial_Status`,`Education–Gender`,`Education–Income`, `Education-Legal_Issues`,`Education-Quality_Of_Life`, `Education-Race_Ethnicity`, `Education-Substance_Use`, `Employment-Financial_Status`,  `Employment–Housing`, `Employment–Income`, `Employment-Insurance_Status`, `Employment-Population_Group`, `Employment-Quality_Of_Life`, `Employment-Race_Ethnicity`, `Environmental_Condition-Quality_Of_Life`, `Exercise-Mental_Health`, `Exercise–Obesity`, `Exercise-Quality_Of_Life`, `Exercise–Smoking`, `Exercise-Substance_Use`, `Financial_Status-Food_Insecurity`,  `Financial_Status-Housing`, `Financial_Status-Income`, `Financial_Status-Insurance_Status`, `Financial_Status-Mental_Health`, `Financial_Status-Quality_Of_Life`, `Financial_Status-Race_Ethnicity`, `Financial_Status-Social_Support`, `Financial_Status-Substance_Use`, `Food_Insecurity-Income`, `Food_Insecurity-Mental_Health`, `Food_Insecurity-Population_Group`, `Food_Insecurity-Quality_Of_Life`, `Food_Insecurity-Race_Ethnicity`, `Food_Insecurity-Social_Support`, `Food_Insecurity-Substance_Use`, `Gender-Income`, `Gender-Mental_Health`, `Gender-Obesity`, `Gender-Quality_Of_Life`, `Gender-Smoking`, `Gender-Substance_Use`, `Gender-Violence_Or_Abuse`, `Geographic_Entity-Substance_Use`, `Housing-Income`, `Housing-Insurance_Status`, `Housing-Quality_Of_Life`, `Housing-Race_Ethnicity`, `Income-Insurance_Status`,  `Income-Marital_Status`, `Income-Population_Group`, `Income-Quality_Of_Life`, `Income-Race_Ethnicity`, `Income-Substance_Use`, `Insurance_Status-Population_Group`, `Insurance_Status-Race_Ethnicity`, `Language-Population_Group`, `Language-Race_Ethnicity`, `Language-Social_Exclusion`, `Legal_Issues-Population_Group`, `Legal_Issues-Race_Ethnicity`, `Legal_Issues-Substance_Use`, `Legal_Issues-Violence_Or_Abuse`, `Marital_Status-Mental_Health`, `Marital_Status-Population_Group`, `Marital_Status-Quality_Of_Life`, `Marital_Status-Race_Ethnicity`,  `Marital_Status-Violence_Or_Abuse`, `Mental_Health-Obesity`, `Mental_Health-Population_Group`, `Mental_Health-Quality_Of_Life`, `Mental_Health-Race_Ethnicity`, `Mental_Health-Sexual_Orientation`, `Mental_Health-Smoking`, `Mental_Health-Social_Exclusion`, `Mental_Health-Social_Support`, `Mental_Health-Substance_Use`, `Mental_Health-Violence_Or_Abuse`, `Obesity-Quality_Of_Life`, `Obesity-Race_Ethnicity`, `Population_Group-Quality_Of_Life`, `Population_Group-Race_Ethnicity`, `Population_Group-Smoking`, `Population_Group-Substance_Use`, `Population_Group-Violence_Or_Abuse`, `Quality_Of_Life-Race_Ethnicity`, `Quality_Of_Life-Substance_Use`, `Race_Ethnicity-Smoking`, `Race_Ethnicity-Social_Exclusion`, `Race_Ethnicity-Social_Support`, `Race_Ethnicity-Substance_Use`, `Race_Ethnicity-Violence_Or_Abuse`, `Sexual_Activity-Sexual_Orientation`, `Sexual_Orientation-Social_Exclusion`, `Sexual_Orientation-Substance_Use`, `Sexual_Orientation-Violence_Or_Abuse`, `Smoking-Substance_Use`, `Social_Exclusion-Substance_Use`, `Substance_Duration-Substance_Frequency`, `Substance_Duration-Substance_Quantity`, `Substance_Duration-Substance_Use`, `Substance_Frequency-Substance_Quantity`, `Substance_Frequency-Substance_Use`, `Substance_Quantity-Substance_Use`, `Substance_Use-Violence_Or_Abuse`, `Heart_Disease-Smoking`, `Tumor_Finding-Cancer_Surgery`, `Cancer_Diagnosis-Cancer_Surgery`, `Substance_Use-Disease_Syndrome_Disorder`, `Substance_Use-Communicable_Disease`, `Substance_Use-Hypertension`, `Substance_Use-Hyperlipidemia`, `Substance_Use-Heart_Disease`, `Substance_Use-Cerebrovascular_Disease`, `Substance_Use-Cancer_Diagnosis`, `Substance_Use-Obesity`, `Alcohol-Disease_Syndrome_Disorder`, `Alcohol-Heart_Disease`, `Alcohol-Cerebrovascular_Disease`, `Alcohol-Cancer_Diagnosis`, `Alcohol-Obesity`, `Childhood_Event-Disease_Syndrome_Disorder`, `Childhood_Event-Communicable_Disease`, `Childhood_Event-Hypertension`, `Childhood_Event-Hyperlipidemia`, `Childhood_Event-Heart_Disease`, `Childhood_Event-Cerebrovascular_Disease`, `Childhood_Event-Obesity`, `Mental_Health-Disease_Syndrome_Disorder`, `Mental_Health-Heart_Disease`, `Mental_Health-Cerebrovascular_Disease`, `Eating_Disorder-Disease_Syndrome_Disorder`, `Eating_Disorder-Heart_Disease`, `Eating_Disorder-Cerebrovascular_Disease`, `Obesity-Disease_Syndrome_Disorder`, `Obesity-Hypertension`, `Obesity-Hyperlipidemia`, `Obesity-Heart_Disease`, `Obesity-Cerebrovascular_Disease`, `Obesity-Cancer_Diagnosis`, `Obesity-Tumor_Finding`, `Race_Ethnicity-Disease_Syndrome_Disorder`, `Race_Ethnicity-Communicable_Disease`, `Race_Ethnicity-Hypertension`, `Race_Ethnicity-Hyperlipidemia`, `Race_Ethnicity-Heart_Disease`, `Race_Ethnicity-Cerebrovascular_Disease`, `Race_Ethnicity-Cancer_Diagnosis`, `Race_Ethnicity-Obesity`, `Symptom-Disease_Syndrome_Disorder`, `Symptom-Communicable_Disease`, `Symptom-Hypertension`, `Symptom-Hyperlipidemia`, `Symptom-Heart_Disease`, `Symptom-Cerebrovascular_Disease`, `Symptom-Cancer_Diagnosis`

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

# NER

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

# Assertion Status

|    | chunks                          | entities                  | assertion    |
|---:|---------------------------------|---------------------------|--------------|
|  0 | anxiety                         | Mental_Health             | Present      |
|  1 | depression                      | Mental_Health             | Present      |
|  2 | childhood trauma                | Childhood_Event           | Past         |
|  3 | violence                        | Violence_Or_Abuse         | Past         |
|  4 | abuse                           | Violence_Or_Abuse         | Past         |
|  5 | mental health struggles         | Mental_Health             | Present      |
|  6 | alcohol                         | Alcohol                   | Present      |
|  7 | smoking                         | Smoking                   | Past         |
|  8 | smoking                         | Smoking                   | Hypothetical |
|  9 | hypertension                    | Hypertension              | Present      |
| 10 | substance                       | Substance_Use             | Absent       |
| 11 | difficulty accessing healthcare | Access_To_Care            | Absent       |
| 12 | lack of transportation          | Symptom                   | Absent       |
| 13 | insurance status                | Insurance_Status          | Present      |
| 14 | herniated disc                  | Disease_Syndrome_Disorder | Past         |
| 15 | coronary artery disease         | Heart_Disease             | Past         |
| 16 | CAD                             | Heart_Disease             | Past         |
| 17 | diabetes mellitus               | Diabetes                  | Present      |
| 18 | manic disorder                  | Mental_Health             | Present      |
| 19 | psychotic                       | Mental_Health             | Present      |
| 20 | impulsive behavior              | Mental_Health             | Present      |
| 21 | Bipolar affective disorder      | Mental_Health             | Present      |
| 22 | manic                           | Mental_Health             | Present      |
| 23 | Mental status changes           | Mental_Health             | Present      |
| 24 | tumor                           | Tumor_Finding             | Present      |
| 25 | disabled                        | Symptom                   | Present      |

# Relation Extraction

|   | sentence | entity1_begin | entity1_end | chunk1           | entity1           | entity2_begin | entity2_end | chunk2                  | entity2           | relation                          | confidence |
|--:|---------:|--------------:|------------:|------------------|-------------------|---------------|-------------|-------------------------|-------------------|-----------------------------------|-----------:|
| 0 | 0        | 47            | 53          | anxiety          | Mental_Health     | 101           | 115         | quality of life         | Quality_Of_Life   | Mental_Health-Quality_Of_Life     |     1.0    |
| 1 | 0        | 59            | 68          | depression       | Mental_Health     | 101           | 115         | quality of life         | Quality_Of_Life   | Mental_Health-Quality_Of_Life     |     1.0    |
| 2 | 2        | 247           | 262         | childhood trauma | Childhood_Event   | 275           | 282         | violence                | Violence_Or_Abuse | Childhood_Event-Violence_Or_Abuse |     1.0    |
| 3 | 2        | 247           | 262         | childhood trauma | Childhood_Event   | 288           | 292         | abuse                   | Violence_Or_Abuse | Childhood_Event-Violence_Or_Abuse |     1.0    |
| 4 | 2        | 247           | 262         | childhood trauma | Childhood_Event   | 349           | 371         | mental health struggles | Mental_Health     | Childhood_Event-Mental_Health     |     1.0    |
| 5 | 2        | 275           | 282         | violence         | Violence_Or_Abuse | 349           | 371         | mental health struggles | Mental_Health     | Violence_Or_Abuse-Mental_Health   |     1.0    |
| 6 | 2        | 288           | 292         | abuse            | Violence_Or_Abuse | 349           | 371         | mental health struggles | Mental_Health     | Violence_Or_Abuse-Mental_Health   |     1.0    |
| 7 | 7        | 875           | 883         | immigrant        | Population_Group  | 896           | 902         | English                 | Language          | Population_Group-Language         |     1.0    |

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
