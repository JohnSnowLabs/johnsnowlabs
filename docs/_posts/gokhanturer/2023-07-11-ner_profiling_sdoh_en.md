---
layout: model
title: Named Entity Recognition Profiling (SDOH)
author: John Snow Labs
name: ner_profiling_sdoh
date: 2023-07-11
tags: [licensed, en, clinical, profiling, ner_profiling, ner, sdoh, social_determinants_of_health]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once for Social Determinants of Health. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `embeddings_clinical`.

Here are the NER models that this pretrained pipeline includes:

`ner_sdoh`, `ner_sdoh_social_environment_wip`, `ner_sdoh_mentions`, `ner_sdoh_demographics_wip`, `ner_sdoh_community_condition_wip`, `ner_sdoh_substance_usage_wip`, `ner_sdoh_access_to_healthcare_wip`, `ner_sdoh_health_behaviours_problems_wip`, `ner_sdoh_income_social_status_wip`

## Predicted Entities

`Access_To_Care`, `Age`, `Alcohol`, `Cerebrovascular_Disease`, `Chidhood_Event`, `Childhood_Development`, `Childhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diabetes`, `Diet`, `Disability`, `Disease_Syndrome_Disorder`, `Dosage`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Heart_Disease`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Kidney_Disease`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Psychological_Condition`, `Quality_Of_Life`, `Race_Ethnicity`, `Relationship_Status`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Symptom`, `Transportation`, `Violence_Abuse_Legal`, `Violence_Or_Abuse`, `behavior_alcohol`, `behavior_drug`, `behavior_tobacco`, `sdoh_community`, `sdoh_economics`, `sdoh_education`, `sdoh_environment`


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/27.0.Social_Determinant_of_Health_Models.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_4.4.4_3.4_1689085109838.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_sdoh_en_4.4.4_3.4_1689085109838.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_sdoh", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week.""")

```
</div>

## Results

```bash

 ******************** ner_sdoh_mentions Model Results ********************

[('Smith', 'B-sdoh_community'), ('divorced', 'B-sdoh_community'), ('lives', 'B-sdoh_environment'), ('apartment', 'B-sdoh_environment'), ('blood', 'B-behavior_drug'), ('works', 'B-sdoh_economics'), ('son', 'B-sdoh_community'), ('rehab', 'B-sdoh_environment'), ('etoh', 'B-behavior_alcohol'), ('drinker', 'B-behavior_alcohol'), ('beer', 'B-behavior_alcohol'), ('smokes', 'B-behavior_tobacco'), ('pack', 'B-behavior_tobacco'), ('cigarettes', 'B-behavior_tobacco')]


 ******************** ner_sdoh_community_condition Model Results ********************

[('apartment', 'B-Housing')]


 ******************** ner_sdoh_demographics Model Results ********************

[('55', 'B-Age'), ('years', 'I-Age'), ('old', 'I-Age'), ('New', 'B-Geographic_Entity'), ('York', 'I-Geographic_Entity'), ('American', 'B-Race_Ethnicity'), ('woman', 'B-Gender'), ('She', 'B-Gender'), ('Spanish', 'B-Language'), ('Portuguese', 'B-Language'), ('She', 'B-Gender'), ('She', 'B-Gender'), ('She', 'B-Gender'), ('son', 'B-Family_Member'), ('She', 'B-Gender'), ('she', 'B-Gender'), ('her', 'B-Gender'), ('catholic', 'B-Spiritual_Beliefs'), ('faith', 'I-Spiritual_Beliefs'), ('She', 'B-Gender'), ('her', 'B-Gender'), ('teens', 'B-Age'), ('She', 'B-Gender'), ('she', 'B-Gender'), ('She', 'B-Gender'), ('She', 'B-Gender')]


 ******************** ner_sdoh Model Results ********************

[('55', 'B-Age'), ('years', 'I-Age'), ('old', 'I-Age'), ('New', 'B-Geographic_Entity'), ('York', 'I-Geographic_Entity'), ('divorced', 'B-Marital_Status'), ('Mexcian', 'B-Race_Ethnicity'), ('American', 'I-Race_Ethnicity'), ('woman', 'B-Gender'), ('financial', 'B-Financial_Status'), ('problems', 'I-Financial_Status'), ('She', 'B-Gender'), ('Spanish', 'B-Language'), ('Portuguese', 'B-Language'), ('She', 'B-Gender'), ('apartment', 'B-Housing'), ('She', 'B-Gender'), ('diabetes', 'B-Other_Disease'), ('hospitalizations', 'B-Other_SDoH_Keywords'), ('cleaning', 'B-Employment'), ('assistant', 'I-Employment'), ('health', 'B-Insurance_Status'), ('insurance', 'I-Insurance_Status'), ('She', 'B-Gender'), ('son', 'B-Family_Member'), ('student', 'B-Education'), ('college', 'B-Education'), ('depression', 'B-Mental_Health'), ('She', 'B-Gender'), ('she', 'B-Gender'), ('rehab', 'B-Access_To_Care'), ('her', 'B-Gender'), ('catholic', 'B-Spiritual_Beliefs'), ('faith', 'I-Spiritual_Beliefs'), ('support', 'B-Social_Support'), ('She', 'B-Gender'), ('etoh', 'B-Alcohol'), ('abuse', 'I-Alcohol'), ('her', 'B-Gender'), ('teens', 'B-Age'), ('She', 'B-Gender'), ('she', 'B-Gender'), ('daily', 'B-Substance_Frequency'), ('drinker', 'B-Alcohol'), ('30', 'B-Substance_Duration'), ('years', 'I-Substance_Duration'), ('drinking', 'B-Alcohol'), ('beer', 'B-Alcohol'), ('daily', 'B-Substance_Frequency'), ('She', 'B-Gender'), ('smokes', 'B-Smoking'), ('a', 'B-Substance_Quantity'), ('pack', 'I-Substance_Quantity'), ('cigarettes', 'B-Smoking'), ('a', 'B-Substance_Frequency'), ('day', 'I-Substance_Frequency'), ('She', 'B-Gender'), ('DUI', 'B-Legal_Issues')]


 ******************** ner_social_environment Model Results ********************

[('support', 'B-Social_Support'), ('DUI', 'B-Legal_Issues')]


 ******************** ner_sdoh_access_to_healthcare Model Results ********************

[('health', 'B-Insurance_Status'), ('insurance', 'I-Insurance_Status'), ('rehab', 'B-Access_To_Care')]


 ******************** ner_sdoh_health_behaviours_problems Model Results ********************

[('diabetes', 'B-Other_Disease'), ('depression', 'B-Mental_Health')]


  ******************** ner_sdoh_substance_usage Model Results ********************

[('etoh', 'B-Alcohol'), ('abuse', 'I-Alcohol'), ('daily', 'B-Substance_Frequency'), ('drinker', 'B-Alcohol'), ('30', 'B-Substance_Duration'), ('years', 'I-Substance_Duration'), ('drinking', 'B-Alcohol'), ('beer', 'B-Alcohol'), ('daily', 'B-Substance_Frequency'), ('smokes', 'B-Smoking'), ('a', 'B-Substance_Quantity'), ('pack', 'I-Substance_Quantity'), ('cigarettes', 'B-Smoking'), ('a', 'B-Substance_Frequency'), ('day', 'I-Substance_Frequency')]


 ******************** ner_sdoh_income_social_status Model Results ********************

[('divorced', 'B-Marital_Status'), ('financial', 'B-Financial_Status'), ('problems', 'I-Financial_Status'), ('cleaning', 'B-Employment'), ('assistant', 'I-Employment'), ('student', 'B-Education'), ('college', 'B-Education')]


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_sdoh|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

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
