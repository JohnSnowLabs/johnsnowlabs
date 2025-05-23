---
layout: model
title: Pipeline to Detect Radiology Concepts (WIP)
author: John Snow Labs
name: jsl_rd_ner_wip_greedy_clinical_pipeline
date: 2023-06-16
tags: [ner, clinical, licensed, en]
task: Named Entity Recognition
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

This pretrained pipeline is built on the top of [jsl_rd_ner_wip_greedy_clinical](https://nlp.johnsnowlabs.com/2021/04/01/jsl_rd_ner_wip_greedy_clinical_en.html) model.

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Route`, `Admission_Discharge`, `ImagingTest`, `Units`, `Death_Entity`, `Oxygen_Therapy`, `Relationship_Status`, `Triglycerides`, `Duration`, `Alcohol`, `Date`, `OtherFindings`, `BodyPart`, `Drug`, `Hyperlipidemia`, `Respiration`, `Birth_Entity`, `VS_Finding`, `Age`, `ManualFix`, `Social_History_Header`, `Family_History_Header`, `Medical_Device`, `Labour_Delivery`, `BMI`, `Fetus_NewBorn`, `Temperature`, `Section_Header`, `Communicable_Disease`, `ImagingFindings`, `Psychological_Condition`, `Obesity`, `Sexually_Active_or_Sexual_Orientation`, `Modifier`, `Vaccine`, `Symptom`, `Kidney_Disease`, `Pulse`, `Oncological`, `EKG_Findings`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Blood_Pressure`, `Diabetes`, `O2_Saturation`, `Heart_Disease`, `Employment`, `Frequency`, `Disease_Syndrome_Disorder`, `Pregnancy`, `RelativeDate`, `Procedure`, `Overweight`, `Race_Ethnicity`, `Hypertension`, `Imaging_Technique`, `Test_Result`, `Treatment`, `Substance`, `Clinical_Dept`, `LDL`, `Measurements`, `Diet`, `Substance_Quantity`, `Allergen`, `Gender`, `RelativeTime`, `Score`, `Total_Cholesterol`, `Vital_Signs_Header`, `Height`, `Smoking`, `Form`, `Strength`, `Weight`, `Time`, `Dosage`, `HDL`




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_rd_ner_wip_greedy_clinical_pipeline_en_4.4.4_3.4_1686923043583.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_rd_ner_wip_greedy_clinical_pipeline_en_4.4.4_3.4_1686923043583.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("jsl_rd_ner_wip_greedy_clinical_pipeline", "en", "clinical/models")

text = '''The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature..'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("jsl_rd_ner_wip_greedy_clinical_pipeline", "en", "clinical/models")

val text = "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.jsl_rd_wip_greedy.pipeline").predict("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature..""")
```

</div>



## Results

```bash
|    | ner_chunks                  |   begin |   end | ner_label      |   confidence |
|---:|:----------------------------|--------:|------:|:---------------|-------------:|
|  0 | 21-day-old                  |      17 |    26 | Age            |     0.9913   |
|  1 | Caucasian                   |      28 |    36 | Race_Ethnicity |     0.9988   |
|  2 | male                        |      38 |    41 | Gender         |     0.9996   |
|  3 | for 2 days                  |      48 |    57 | Duration       |     0.5107   |
|  4 | congestion                  |      62 |    71 | Symptom        |     0.8608   |
|  5 | mom                         |      75 |    77 | Gender         |     0.9711   |
|  6 | suctioning yellow discharge |      88 |   114 | Symptom        |     0.345967 |
|  7 | nares                       |     135 |   139 | BodyPart       |     0.3583   |
|  8 | she                         |     147 |   149 | Gender         |     0.997    |
|  9 | his                         |     187 |   189 | Gender         |     0.9866   |
| 10 | breathing while feeding     |     191 |   213 | Symptom        |     0.2221   |
| 11 | perioral cyanosis           |     237 |   253 | Symptom        |     0.82215  |
| 12 | retractions                 |     258 |   268 | Symptom        |     0.9902   |
| 13 | One day ago                 |     272 |   282 | RelativeDate   |     0.6992   |
| 14 | mom                         |     285 |   287 | Gender         |     0.9588   |
| 15 | tactile temperature         |     304 |   322 | Symptom        |     0.18075  |
| 16 | Tylenol                     |     345 |   351 | Drug           |     0.9919   |
| 17 | Baby                        |     354 |   357 | Age            |     0.9988   |
| 18 | decreased p.o. intake       |     377 |   397 | Symptom        |     0.477125 |
| 19 | His                         |     400 |   402 | Gender         |     0.9993   |
| 20 | q.2h. to 5 to 10 minutes    |     450 |   473 | Frequency      |     0.3258   |
| 21 | his                         |     488 |   490 | Gender         |     0.9909   |
| 22 | respiratory congestion      |     492 |   513 | Symptom        |     0.25015  |
| 23 | He                          |     516 |   517 | Gender         |     0.9998   |
| 24 | tired                       |     550 |   554 | Symptom        |     0.8179   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_rd_ner_wip_greedy_clinical_pipeline|
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
