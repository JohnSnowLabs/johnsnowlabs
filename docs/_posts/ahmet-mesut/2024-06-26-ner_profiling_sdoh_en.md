---
layout: model
title: Named Entity Recognition Profiling (SDOH)
author: John Snow Labs
name: ner_profiling_sdoh
date: 2024-06-26
tags: [licensed, en, clinical, profiling, ner_profiling, ner, sdoh, social_determinants_of_health]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to simultaneously evaluate various pre-trained named entity recognition (NER) models, enabling comprehensive analysis of text data pertaining to the social determinants of health (SDOH).  When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with the `embeddings_clinical`, which are specifically designed for clinical and biomedical text.

`ner_sdoh`, `ner_sdoh_wip`, `ner_sdoh_langtest`, `ner_sdoh_core`, `ner_sdoh_demographics`, `ner_sdoh_demographics_wip`, `ner_sdoh_mentions`, `ner_sdoh_community_condition`,`ner_sdoh_community_condition_wip`, `ner_sdoh_social_environment`, `ner_sdoh_social_environment_wip`, `ner_sdoh_substance_usage`, `ner_sdoh_substance_usage_wip`, `ner_sdoh_slim_wip`, `ner_sdoh_access_to_healthcare`, `ner_sdoh_access_to_healthcare_wip`, `ner_sdoh_health_behaviours_problems`, `ner_sdoh_health_behaviours_problems_wip`, `ner_sdoh_income_social_status`, `ner_sdoh_income_social_status_wip`, `ner_jsl`, `ner_jsl_langtest`, `ner_jsl_greedy`, `ner_jsl_enriched`, `ner_jsl_slim`

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Cerebrovascular_Disease`, `Chidhood_Event`, `Childhood_Development`, `Childhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diabetes`, `Diet`, `Disability`, `Disease_Syndrome_Disorder`, `Dosage`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Heart_Disease`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Kidney_Disease`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Psychological_Condition`, `Quality_Of_Life`, `Race_Ethnicity`, `Relationship_Status`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Symptom`, `Transportation`, `Violence_Abuse_Legal`, `Violence_Or_Abuse`, `behavior_alcohol`, `behavior_drug`, `behavior_tobacco`, `sdoh_community`, `sdoh_economics`, `sdoh_education`, `sdoh_environment`

`Access_To_Care`, `Age`, `Alcohol`, `Chidhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`, `behavior_alcohol`, `behavior_drug`, `behavior_tobacco`, `sdoh_community`, `sdoh_economics`, `sdoh_education`, `sdoh_environment`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_5.3.2_3.4_1719411413141.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_5.3.2_3.4_1719411413141.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""
The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life.
He reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his smoking, alcohol use and current mental health struggles.
He denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife.
The patient is an immigrant and speaks English as a second language.
He reported difficulty accessing healthcare due to lack of medical insurance.
He has a herniated disc, hypertension, coronary artery disease (CAD) and diabetes mellitus.
The patient has a manic disorder, is presently psychotic and shows impulsive behavior. He has been disabled since 2001.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""
The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life.
He reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his smoking, alcohol use and current mental health struggles.
He denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife.
The patient is an immigrant and speaks English as a second language.
He reported difficulty accessing healthcare due to lack of medical insurance.
He has a herniated disc, hypertension, coronary artery disease (CAD) and diabetes mellitus.
The patient has a manic disorder, is presently psychotic and shows impulsive behavior. He has been disabled since 2001.
""")

```
</div>

## Results

```bash

******************** ner_sdoh_substance_usage_wip Model Results ********************

('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('substance use', 'Substance_Use')

******************** ner_sdoh_health_behaviours_problems_wip Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('quality of life', 'Quality_Of_Life') ('mental health struggles', 'Mental_Health') ('sexual activity', 'Sexual_Activity') ('monogamous', 'Sexual_Activity') ('herniated disc', 'Other_Disease') ('hypertension', 'Hypertension') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('disabled', 'Disability')

******************** ner_jsl_greedy Model Results ********************

('anxiety', 'Psychological_Condition') ('depression', 'Psychological_Condition') ('smoking', 'Smoking') ('alcohol', 'Alcohol') ('substance', 'Substance') ('sexual activity', 'Symptom') ('difficulty accessing healthcare', 'Symptom') ('herniated disc', 'Disease_Syndrome_Disorder') ('hypertension', 'Hypertension') ('coronary artery disease', 'Heart_Disease') ('CAD', 'Heart_Disease') ('diabetes mellitus', 'Diabetes') ('manic disorder', 'Psychological_Condition') ('psychotic', 'Psychological_Condition') ('impulsive behavior', 'Symptom')

******************** ner_jsl_enriched Model Results ********************

('anxiety', 'Psychological_Condition') ('depression', 'Psychological_Condition') ('smoking', 'Smoking') ('alcohol', 'Alcohol') ('substance', 'Substance') ('difficulty accessing healthcare', 'Symptom') ('lack of medical insurance', 'Symptom') ('herniated disc', 'Disease_Syndrome_Disorder') ('hypertension', 'Hypertension') ('coronary artery disease', 'Heart_Disease') ('CAD', 'Heart_Disease') ('diabetes mellitus', 'Diabetes') ('manic disorder', 'Psychological_Condition') ('psychotic', 'Symptom') ('impulsive behavior', 'Symptom') ('disabled', 'Symptom')

******************** ner_sdoh_health_behaviours_problems Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('quality of life', 'Quality_Of_Life') ('mental health struggles', 'Mental_Health') ('sexual activity', 'Sexual_Activity') ('monogamous', 'Sexual_Activity') ('herniated disc', 'Other_Disease') ('hypertension', 'Hypertension') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('disabled', 'Disability')

******************** ner_sdoh_social_environment Model Results ********************

('childhood trauma', 'Chidhood_Event') ('violence', 'Violence_Or_Abuse') ('abuse', 'Violence_Or_Abuse')

******************** ner_jsl_slim Model Results ********************

('anxiety', 'Disease_Syndrome_Disorder') ('depression', 'Disease_Syndrome_Disorder') ('childhood trauma', 'Disease_Syndrome_Disorder') ('herniated disc', 'Disease_Syndrome_Disorder') ('hypertension', 'Disease_Syndrome_Disorder') ('coronary artery disease', 'Disease_Syndrome_Disorder') ('CAD', 'Disease_Syndrome_Disorder') ('diabetes mellitus', 'Disease_Syndrome_Disorder') ('manic disorder', 'Disease_Syndrome_Disorder') ('presently psychotic', 'Symptom') ('impulsive behavior', 'Symptom') ('disabled', 'Symptom')

******************** ner_sdoh_mentions Model Results ********************

('childhood', 'sdoh_community') ('smoking', 'behavior_tobacco') ('alcohol', 'behavior_alcohol') ('substance', 'behavior_drug') ('wife', 'sdoh_community')

******************** ner_sdoh_access_to_healthcare Model Results ********************

('accessing healthcare', 'Access_To_Care') ('medical insurance', 'Insurance_Status')

******************** ner_sdoh_substance_usage Model Results ********************

('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('substance use', 'Substance_Use')

******************** ner_sdoh_slim_wip Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('his', 'Gender') ('He', 'Gender') ('his', 'Gender') ('his', 'Gender') ('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('He', 'Gender') ('substance use', 'Substance_Use') ('monogamous', 'Marital_Status') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('He', 'Gender') ('He', 'Gender') ('hypertension', 'Other_Disease') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('He', 'Gender') ('disabled', 'Disability')

******************** ner_sdoh_income_social_status Model Results ********************

('monogamous', 'Marital_Status') ('immigrant', 'Population_Group')
******************** ner_sdoh_demographics Model Results ********************

('his', 'Gender') ('He', 'Gender') ('his', 'Gender') ('his', 'Gender') ('He', 'Gender') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('English', 'Language') ('He', 'Gender') ('He', 'Gender') ('He', 'Gender')

******************** ner_sdoh_access_to_healthcare_wip Model Results ********************

('medical insurance', 'Insurance_Status')

******************** ner_jsl Model Results ********************

('anxiety', 'Psychological_Condition') ('depression', 'Psychological_Condition') ('smoking', 'Smoking') ('alcohol', 'Alcohol') ('substance', 'Substance') ('monogamous', 'Relationship_Status') ('immigrant', 'Relationship_Status') ('herniated disc', 'Disease_Syndrome_Disorder') ('hypertension', 'Hypertension') ('coronary artery disease', 'Heart_Disease') ('CAD', 'Heart_Disease') ('diabetes mellitus', 'Diabetes') ('manic disorder', 'Psychological_Condition') ('psychotic', 'Psychological_Condition') ('impulsive behavior', 'Psychological_Condition') ('disabled', 'Symptom')

******************** ner_sdoh_income_social_status_wip Model Results ********************

('mental health struggles', 'Financial_Status') ('monogamous', 'Marital_Status') ('immigrant', 'Population_Group')

******************** ner_sdoh_langtest Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('his', 'Gender') ('quality of life', 'Quality_Of_Life') ('He', 'Gender') ('childhood trauma', 'Childhood_Event') ('violence', 'Violence_Or_Abuse') ('abuse', 'Violence_Or_Abuse') ('his', 'Gender') ('his', 'Gender') ('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('mental health struggles', 'Mental_Health') ('He', 'Gender') ('substance use', 'Substance_Use') ('sexual activity', 'Sexual_Activity') ('monogamous', 'Sexual_Activity') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('immigrant', 'Population_Group') ('English', 'Language') ('He', 'Gender') ('accessing healthcare', 'Access_To_Care') ('medical insurance', 'Insurance_Status') ('He', 'Gender') ('herniated disc', 'Other_Disease') ('hypertension', 'Hypertension') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('He', 'Gender') ('disabled', 'Disability')

******************** ner_sdoh_wip Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('his', 'Gender') ('quality of life', 'Quality_Of_Life') ('He', 'Gender') ('childhood trauma related to violence', 'Violence_Or_Abuse') ('abuse', 'Violence_Or_Abuse') ('his', 'Gender') ('his', 'Gender') ('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('mental health struggles', 'Mental_Health') ('He', 'Gender') ('substance use', 'Substance_Use') ('sexual activity', 'Sexual_Activity') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('immigrant', 'Population_Group') ('English', 'Language') ('He', 'Gender') ('accessing healthcare', 'Access_To_Care') ('medical insurance', 'Insurance_Status') ('He', 'Gender') ('herniated disc', 'Other_Disease') ('hypertension', 'Hypertension') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('He', 'Gender') ('disabled', 'Disability')

******************** ner_sdoh_demographics_wip Model Results ********************

('his', 'Gender') ('He', 'Gender') ('his', 'Gender') ('his', 'Gender') ('He', 'Gender') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('English', 'Language') ('He', 'Gender') ('He', 'Gender') ('He', 'Gender')

******************** ner_jsl_langtest Model Results ********************

('anxiety', 'Psychological_Condition') ('depression', 'Psychological_Condition') ('smoking', 'Smoking') ('alcohol', 'Alcohol') ('substance', 'Substance') ('difficulty accessing healthcare due to lack of medical insurance', 'Symptom') ('herniated disc', 'Disease_Syndrome_Disorder') ('hypertension', 'Hypertension') ('coronary artery disease', 'Heart_Disease') ('CAD', 'Heart_Disease') ('diabetes mellitus', 'Diabetes') ('manic disorder', 'Psychological_Condition') ('psychotic', 'Psychological_Condition') ('impulsive behavior', 'Symptom')

******************** ner_sdoh Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('his', 'Gender') ('quality of life', 'Quality_Of_Life') ('He', 'Gender') ('childhood trauma', 'Chidhood_Event') ('violence', 'Violence_Or_Abuse') ('abuse', 'Violence_Or_Abuse') ('his', 'Gender') ('his', 'Gender') ('smoking', 'Smoking') ('alcohol use', 'Alcohol') ('mental health struggles', 'Mental_Health') ('He', 'Gender') ('substance use', 'Substance_Use') ('sexual activity', 'Sexual_Activity') ('monogamous', 'Sexual_Activity') ('his', 'Gender') ('his', 'Gender') ('wife', 'Family_Member') ('immigrant', 'Population_Group') ('English', 'Language') ('He', 'Gender') ('difficulty accessing healthcare', 'Access_To_Care') ('medical insurance', 'Insurance_Status') ('He', 'Gender') ('herniated disc', 'Other_Disease') ('hypertension', 'Hypertension') ('coronary artery disease', 'Other_Disease') ('CAD', 'Other_Disease') ('diabetes mellitus', 'Other_Disease') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('He', 'Gender') ('disabled', 'Disability')

******************** ner_sdoh_community_condition_converter Model Results ********************



******************** ner_sdoh_social_environment_wip Model Results ********************

('childhood trauma', 'Chidhood_Event') ('violence', 'Violence_Abuse_Legal') ('abuse', 'Violence_Abuse_Legal') ('sexual activity', 'Violence_Abuse_Legal') ('herniated disc', 'Violence_Abuse_Legal') ('impulsive behavior', 'Violence_Abuse_Legal')

******************** ner_sdoh_core Model Results ********************

('anxiety', 'Mental_Health') ('depression', 'Mental_Health') ('quality of life', 'Quality_Of_Life') ('childhood trauma', 'Childhood_Event') ('violence', 'Violence_Or_Abuse') ('abuse', 'Violence_Or_Abuse') ('mental health struggles', 'Mental_Health') ('substance use', 'Substance_Use') ('wife', 'Family_Member') ('immigrant', 'Population_Group') ('difficulty accessing healthcare', 'Access_To_Care') ('medical insurance', 'Insurance_Status') ('manic disorder', 'Mental_Health') ('psychotic', 'Mental_Health') ('impulsive behavior', 'Mental_Health') ('disabled', 'Disability')


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_sdoh|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.2+|
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
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel
- MedicalNerModel
- NerConverterInternalModel