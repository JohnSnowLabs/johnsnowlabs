---
layout: model
title: Explain Clinical Document - Social Determinants of Health (SDOH)-Small
author: John Snow Labs
name: explain_clinical_doc_sdoh_small
date: 2024-09-27
tags: [en, licensed, clinical, pipeline, social_determinants, sdoh, ner, assertion, relation_extraction]
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

This pipeline is designed to

- extract all social determinants of health (SDOH) entities from text,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities.

In this pipeline, [ner_sdoh](https://nlp.johnsnowlabs.com/2023/06/13/ner_sdoh_en.html) 
NER model, [assertion_sdoh_wip](https://nlp.johnsnowlabs.com/2023/08/13/assertion_sdoh_wip_en.html) assertion model and [generic_re](https://nlp.johnsnowlabs.com/2022/12/20/generic_re.html)
relation extraction model were used to achieve those tasks.

Clinical Entity Labels:

`Access_To_Care`, `Age`, `Alcohol`, `Chidhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`


Assertion Status Labels:

`Present`, `Absent`, `Possible`, `Past`, `Hypotetical`, `Someone_Else`

Relation Extraction Labels:

`Access_To_Care-Financial_Status`, `Access_To_Care–Income`, `Access_To_Care-Social_Support`, `Access_To_Care-Substance_Use`, `Alcohol-Mental_Health`, `Alcohol-Quality_Of_Life`, `Alcohol–Smoking`, `Alcohol-Substance_Use`, `Alcohol-Violence_Or_Abuse`, `Childhood_Event-Violence_Or_Abuse`, `Community_Safety-Quality_Of_Life`, `Community_Safety-Violence_Or_Abuse`, `Diet-Eating_Disorder`, `Diet–Exercise`, `Diet–Gender`, `Diet–Obesity`, `Disability-Insurance_Status`, `Disability-Mental_Health`, `Disability-Quality_Of_Life`, `Disability-Social_Exclusion`, `Eating_Disorder-Food_Insecurity`, `Eating_Disorder-Mental_Health`, `Eating_Disorder–Obesity`, `Education–Employment`, `Education-Financial_Status`, `Education–Income`, `Education-Legal_Issues`, `Education-Quality_Of_Life`, `Education-Substance_Use`, `Employment-Financial_Status`, `Employment–Income`, `Employment-Insurance_Status`, `Employment-Quality_Of_Life`, `Environmental_Condition-Quality_Of_Life`, `Exercise-Mental_Health`, `Exercise–Obesity`, `Exercise-Quality_Of_Life`, `Exercise–Smoking`, `Exercise-Substance_Use`, `Financial_Status-Food_Insecurity`, `Financial_Status-Housing`, `Financial_Status-Income`, `Financial_Status-Insurance_Status`, `Financial_Status-Mental_Health`, `Financial_Status-Quality_Of_Life`, `Financial_Status-Social_Support`, `Food_Insecurity-Income`, `Food_Insecurity-Mental_Health`, `Food_Insecurity-Quality_Of_Life`, `Housing-Income`, `Housing-Insurance_Status`, `Housing-Quality_Of_Life`, `Income-Insurance_Status`, `Income-Quality_Of_Life`, `Language-Population_Group`, `Language-Race_Ethnicity`, `Language-Social_Exclusion`, `Legal_Issues-Race_Ethnicity`, `Legal_Issues-Substance_Use`, `Legal_Issues-Violence_Or_Abuse`, `Marital_Status-Mental_Health`, `Marital_Status-Violence_Or_Abuse`, `Mental_Health-Obesity`, `Mental_Health-Quality_Of_Life`, `Mental_Health-Smoking`, `Mental_Health-Social_Exclusion`, `Mental_Health-Social_Support`, `Mental_Health-Substance_Use`, `Mental_Health-Violence_Or_Abuse`, `Obesity-Quality_Of_Life`, `Population_Group-Violence_Or_Abuse`, `Quality_Of_Life-Substance_Use`, `Race_Ethnicity-Social_Exclusion`, `Race_Ethnicity-Social_Support`, `Race_Ethnicity-Violence_Or_Abuse`, `Sexual_Activity-Sexual_Orientation`, `Sexual_Orientation-Social_Exclusion`, `Sexual_Orientation-Substance_Use`, `Sexual_Orientation-Violence_Or_Abuse`, `Smoking-Substance_Use`, `Social_Exclusion-Substance_Use`, `Substance_Duration-Substance_Use`, `Substance_Frequency-Substance_Use`, `Substance_Quantity-Substance_Use`, `Substance_Use-Violence_Or_Abuse`, `Substance_Use-Communicable_Disease`, `Alcohol-Obesity`

 ## Predicted Entities
`Access_To_Care`, `Age`, `Alcohol`, `Chidhood_Event`, `Communicable_Disease`, `Community_Safety`, `Diet`, `Disability`, `Eating_Disorder`, `Education`, `Employment`, `Environmental_Condition`, `Exercise`, `Family_Member`, `Financial_Status`, `Food_Insecurity`, `Gender`, `Geographic_Entity`, `Healthcare_Institution`, `Housing`, `Hyperlipidemia`, `Hypertension`, `Income`, `Insurance_Status`, `Language`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Obesity`, `Other_Disease`, `Other_SDoH_Keywords`, `Population_Group`, `Quality_Of_Life`, `Race_Ethnicity`, `Sexual_Activity`, `Sexual_Orientation`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Spiritual_Beliefs`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`, `Transportation`, `Violence_Or_Abuse`
 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_small_en_5.4.1_3.4_1727457167099.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_sdoh_small_en_5.4.1_3.4_1727457167099.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

sdoh_pipeline = PretrainedPipeline('explain_clinical_doc_sdoh_small', 'en', 'clinical/models')

result = sdoh_pipeline.fullAnnotate("""The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life.
He reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his smoking, alcohol use and current mental health struggles.
He denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife.
The patient is an immigrant and speaks English as a second language.
He reported difficulty accessing healthcare due to lack of medical insurance.
He has a herniated disc, hypertension, coronary artery disease (CAD) and diabetes mellitus.
The patient has a manic disorder, is presently psychotic and shows impulsive behavior. He has been disabled since 2001.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val sdoh_pipeline = new PretrainedPipeline("explain_clinical_doc_sdoh_small", "en", "clinical/models")

val result = sdoh_pipeline.fullAnnotate("""The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life.
He reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his smoking, alcohol use and current mental health struggles.
He denied any recent substance use or sexual activity and reported being monogamous in his relationship with his wife.
The patient is an immigrant and speaks English as a second language.
He reported difficulty accessing healthcare due to lack of medical insurance.
He has a herniated disc, hypertension, coronary artery disease (CAD) and diabetes mellitus.
The patient has a manic disorder, is presently psychotic and shows impulsive behavior. He has been disabled since 2001.""")
```
</div>

## Results

```bash
# NER_Result

|    | chunks                          |   begin |   end |   sentence_id | entities          |   confidence |
|---:|:--------------------------------|--------:|------:|--------------:|:------------------|-------------:|
|  0 | anxiety                         |      47 |    53 |             0 | Mental_Health     |     0.9897   |
|  1 | depression                      |      59 |    68 |             0 | Mental_Health     |     0.9938   |
|  2 | his                             |      97 |    99 |             0 | Gender            |     0.992    |
|  3 | quality of life                 |     101 |   115 |             0 | Quality_Of_Life   |     0.6252   |
|  4 | He                              |     118 |   119 |             1 | Gender            |     0.9996   |
|  5 | childhood trauma                |     143 |   158 |             1 | Chidhood_Event    |     0.7466   |
|  6 | violence                        |     171 |   178 |             1 | Violence_Or_Abuse |     0.5394   |
|  7 | abuse                           |     184 |   188 |             1 | Violence_Or_Abuse |     0.6209   |
|  8 | his                             |     193 |   195 |             1 | Gender            |     0.9536   |
|  9 | his                             |     233 |   235 |             1 | Gender            |     0.9772   |
| 10 | smoking                         |     237 |   243 |             1 | Smoking           |     0.9858   |
| 11 | alcohol use                     |     246 |   256 |             1 | Alcohol           |     0.68065  |
| 12 | mental health struggles         |     270 |   292 |             1 | Mental_Health     |     0.248033 |
| 13 | He                              |     295 |   296 |             2 | Gender            |     0.9995   |
| 14 | substance use                   |     316 |   328 |             2 | Substance_Use     |     0.6921   |
| 15 | sexual activity                 |     333 |   347 |             2 | Sexual_Activity   |     0.62915  |
| 16 | monogamous                      |     368 |   377 |             2 | Sexual_Activity   |     0.6915   |
| 17 | his                             |     382 |   384 |             2 | Gender            |     0.9883   |
| 18 | his                             |     404 |   406 |             2 | Gender            |     0.978    |
| 19 | wife                            |     408 |   411 |             2 | Family_Member     |     0.9833   |
| 20 | immigrant                       |     432 |   440 |             3 | Population_Group  |     0.9974   |
| 21 | English                         |     453 |   459 |             3 | Language          |     0.9979   |
| 22 | He                              |     483 |   484 |             4 | Gender            |     0.9996   |
| 23 | difficulty accessing healthcare |     495 |   525 |             4 | Access_To_Care    |     0.3998   |
| 24 | medical insurance               |     542 |   558 |             4 | Insurance_Status  |     0.6721   |
| 25 | He                              |     561 |   562 |             5 | Gender            |     0.9996   |
| 26 | herniated disc                  |     570 |   583 |             5 | Other_Disease     |     0.71515  |
| 27 | hypertension                    |     586 |   597 |             5 | Hypertension      |     0.9984   |
| 28 | coronary artery disease         |     600 |   622 |             5 | Other_Disease     |     0.847933 |
| 29 | CAD                             |     625 |   627 |             5 | Other_Disease     |     0.9884   |
| 30 | diabetes mellitus               |     634 |   650 |             5 | Other_Disease     |     0.81115  |
| 31 | manic disorder                  |     671 |   684 |             6 | Mental_Health     |     0.7929   |
| 32 | psychotic                       |     700 |   708 |             6 | Mental_Health     |     0.9743   |
| 33 | impulsive behavior              |     720 |   737 |             6 | Mental_Health     |     0.41135  |
| 34 | He                              |     740 |   741 |             7 | Gender            |     0.9996   |
| 35 | disabled                        |     752 |   759 |             7 | Disability        |     0.9999   |

# Assertıon_Result:

|    | chunks                          | entities          | assertion   |
|---:|:--------------------------------|:------------------|:------------|
|  0 | anxiety                         | Mental_Health     | Present     |
|  1 | depression                      | Mental_Health     | Present     |
|  2 | quality of life                 | Quality_Of_Life   | Present     |
|  3 | violence                        | Violence_Or_Abuse | Past        |
|  4 | abuse                           | Violence_Or_Abuse | Past        |
|  5 | smoking                         | Smoking           | Present     |
|  6 | alcohol use                     | Alcohol           | Present     |
|  7 | mental health struggles         | Mental_Health     | Present     |
|  8 | substance use                   | Substance_Use     | Absent      |
|  9 | sexual activity                 | Sexual_Activity   | Present     |
| 10 | monogamous                      | Sexual_Activity   | Absent      |
| 11 | difficulty accessing healthcare | Access_To_Care    | Absent      |
| 12 | medical insurance               | Insurance_Status  | Present     |
| 13 | hypertension                    | Hypertension      | Present     |
| 14 | manic disorder                  | Mental_Health     | Present     |
| 15 | psychotic                       | Mental_Health     | Present     |
| 16 | impulsive behavior              | Mental_Health     | Present     |


# RE Result

|    |   sentence |   entity1_begin |   entity1_end | chunk1      | entity1           |   entity2_begin |   entity2_end | chunk2                  | entity2         | relation                        |   confidence |
|---:|-----------:|----------------:|--------------:|:------------|:------------------|----------------:|--------------:|:------------------------|:----------------|:--------------------------------|-------------:|
|  0 |          0 |              47 |            53 | anxiety     | Mental_Health     |             101 |           115 | quality of life         | Quality_Of_Life | Mental_Health-Quality_Of_Life   |            1 |
|  1 |          0 |              59 |            68 | depression  | Mental_Health     |             101 |           115 | quality of life         | Quality_Of_Life | Mental_Health-Quality_Of_Life   |            1 |
|  2 |          1 |             171 |           178 | violence    | Violence_Or_Abuse |             246 |           256 | alcohol use             | Alcohol         | Violence_Or_Abuse-Alcohol       |            1 |
|  3 |          1 |             171 |           178 | violence    | Violence_Or_Abuse |             270 |           292 | mental health struggles | Mental_Health   | Violence_Or_Abuse-Mental_Health |            1 |
|  4 |          1 |             184 |           188 | abuse       | Violence_Or_Abuse |             246 |           256 | alcohol use             | Alcohol         | Violence_Or_Abuse-Alcohol       |            1 |
|  5 |          1 |             184 |           188 | abuse       | Violence_Or_Abuse |             270 |           292 | mental health struggles | Mental_Health   | Violence_Or_Abuse-Mental_Health |            1 |
|  6 |          1 |             237 |           243 | smoking     | Smoking           |             270 |           292 | mental health struggles | Mental_Health   | Smoking-Mental_Health           |            1 |
|  7 |          1 |             246 |           256 | alcohol use | Alcohol           |             270 |           292 | mental health struggles | Mental_Health   | Alcohol-Mental_Health           |            1 |
|  8 |          3 |             432 |           440 | immigrant   | Population_Group  |             453 |           459 | English                 | Language        | Population_Group-Language       |            1 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_sdoh_small|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
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
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel
