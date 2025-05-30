---
layout: model
title: Pipeline to Detect Clinical Entities (ner_jsl_greedy)
author: John Snow Labs
name: ner_jsl_greedy_pipeline
date: 2023-06-17
tags: [ner, en, licensed, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_jsl_greedy](https://nlp.johnsnowlabs.com/2021/06/24/ner_jsl_greedy_en.html) model.

## Predicted Entities

`Admission_Discharge`, `Age`, `Alcohol`, `Allergen`, `BMI`, `Birth_Entity`, `Blood_Pressure`, `Cerebrovascular_Disease`, `Clinical_Dept`, `Communicable_Disease`, `Date`, `Death_Entity`, `Diabetes`, `Diet`, `Direction`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Duration`, `EKG_Findings`, `Employment`, `External_body_part_or_region`, `Family_History_Header`, `Fetus_NewBorn`, `Form`, `Frequency`, `Gender`, `HDL`, `Heart_Disease`, `Height`, `Hyperlipidemia`, `Hypertension`, `ImagingFindings`, `Imaging_Technique`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `LDL`, `Labour_Delivery`, `Medical_Device`, `Medical_History_Header`, `Modifier`, `O2_Saturation`, `Obesity`, `Oncological`, `Overweight`, `Oxygen_Therapy`, `Pregnancy`, `Procedure`, `Psychological_Condition`, `Pulse`, `Race_Ethnicity`, `Relationship_Status`, `RelativeDate`, `RelativeTime`, `Respiration`, `Route`, `Section_Header`, `Sexually_Active_or_Sexual_Orientation`, `Smoking`, `Social_History_Header`, `Strength`, `Substance`, `Substance_Quantity`, `Symptom`, `Temperature`, `Test`, `Test_Result`, `Time`, `Total_Cholesterol`, `Treatment`, `Triglycerides`, `VS_Finding`, `Vaccine`, `Vital_Signs_Header`, `Weight`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_greedy_pipeline_en_4.4.4_3.0_1686986330845.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_jsl_greedy_pipeline_en_4.4.4_3.0_1686986330845.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_jsl_greedy_pipeline", "en", "clinical/models")

text = '''The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.'''

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("ner_jsl_greedy_pipeline", "en", "clinical/models")

val text = "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."

val result = pipeline.fullAnnotate(text)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.med_ner.jsl_greedy.pipeline").predict("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""")
```

</div>

## Results

```bash
|    | ner_chunks                                     |   begin |   end | ner_label                    |   confidence |
|---:|:-----------------------------------------------|--------:|------:|:-----------------------------|-------------:|
|  0 | 21-day-old                                     |      17 |    26 | Age                          |     0.9817   |
|  1 | Caucasian                                      |      28 |    36 | Race_Ethnicity               |     0.9998   |
|  2 | male                                           |      38 |    41 | Gender                       |     0.9922   |
|  3 | for 2 days                                     |      48 |    57 | Duration                     |     0.6968   |
|  4 | congestion                                     |      62 |    71 | Symptom                      |     0.875    |
|  5 | mom                                            |      75 |    77 | Gender                       |     0.8156   |
|  6 | suctioning yellow discharge                    |      88 |   114 | Symptom                      |     0.2697   |
|  7 | nares                                          |     135 |   139 | External_body_part_or_region |     0.6216   |
|  8 | she                                            |     147 |   149 | Gender                       |     0.9965   |
|  9 | mild problems with his breathing while feeding |     168 |   213 | Symptom                      |     0.444029 |
| 10 | perioral cyanosis                              |     237 |   253 | Symptom                      |     0.3283   |
| 11 | retractions                                    |     258 |   268 | Symptom                      |     0.957    |
| 12 | One day ago                                    |     272 |   282 | RelativeDate                 |     0.646267 |
| 13 | mom                                            |     285 |   287 | Gender                       |     0.692    |
| 14 | tactile temperature                            |     304 |   322 | Symptom                      |     0.20765  |
| 15 | Tylenol                                        |     345 |   351 | Drug                         |     0.9951   |
| 16 | Baby                                           |     354 |   357 | Age                          |     0.981    |
| 17 | decreased p.o. intake                          |     377 |   397 | Symptom                      |     0.437375 |
| 18 | His                                            |     400 |   402 | Gender                       |     0.999    |
| 19 | 20 minutes                                     |     439 |   448 | Duration                     |     0.20415  |
| 20 | q.2h.                                          |     450 |   454 | Frequency                    |     0.6406   |
| 21 | to 5 to 10 minutes                             |     456 |   473 | Duration                     |     0.12444  |
| 22 | his                                            |     488 |   490 | Gender                       |     0.9904   |
| 23 | respiratory congestion                         |     492 |   513 | Symptom                      |     0.5294   |
| 24 | He                                             |     516 |   517 | Gender                       |     0.9989   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_jsl_greedy_pipeline|
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
- NerConverter