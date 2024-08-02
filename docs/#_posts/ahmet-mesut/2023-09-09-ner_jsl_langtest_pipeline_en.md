---
layout: model
title: Pipeline to Detect Clinical Entities (langtest)
author: John Snow Labs
name: ner_jsl_langtest_pipeline
date: 2023-09-09
tags: [licensed, en, jsl, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [ner_jsl_langtest](https://nlp.johnsnowlabs.com/2023/07/31/ner_jsl_langtest_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_langtest_pipeline_en_5.1.0_3.4_1694277196882.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_jsl_langtest_pipeline_en_5.1.0_3.4_1694277196882.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_jsl_langtest_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_jsl_langtest_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""")

```
</div>

## Results

```bash
|    | chunks                                    |   begin |   end | entities                     |
|---:|:------------------------------------------|--------:|------:|:-----------------------------|
|  0 | 21-day-old                                |      17 |    26 | Age                          |
|  1 | Caucasian                                 |      28 |    36 | Race_Ethnicity               |
|  2 | male                                      |      38 |    41 | Gender                       |
|  3 | for 2 days                                |      48 |    57 | Duration                     |
|  4 | congestion                                |      62 |    71 | Symptom                      |
|  5 | mom                                       |      75 |    77 | Gender                       |
|  6 | discharge                                 |     106 |   114 | Admission_Discharge          |
|  7 | nares                                     |     135 |   139 | External_body_part_or_region |
|  8 | she                                       |     147 |   149 | Gender                       |
|  9 | mild                                      |     168 |   171 | Modifier                     |
| 10 | problems with his breathing while feeding |     173 |   213 | Symptom                      |
| 11 | perioral cyanosis                         |     237 |   253 | Symptom                      |
| 12 | retractions                               |     258 |   268 | Symptom                      |
| 13 | Influenza vaccine                         |     325 |   341 | Vaccine_Name                 |
| 14 | One day ago                               |     344 |   354 | RelativeDate                 |
| 15 | mom                                       |     357 |   359 | Gender                       |
| 16 | Tylenol                                   |     417 |   423 | Drug_BrandName               |
| 17 | Baby                                      |     426 |   429 | Age                          |
| 18 | decreased p.o                             |     449 |   461 | Symptom                      |
| 19 | His                                       |     472 |   474 | Gender                       |
| 20 | 20 minutes                                |     511 |   520 | Duration                     |
| 21 | q.2h. to 5 to 10 minutes                  |     522 |   545 | Frequency                    |
| 22 | his                                       |     560 |   562 | Gender                       |
| 23 | respiratory congestion                    |     564 |   585 | Symptom                      |
| 24 | He                                        |     588 |   589 | Gender                       |
| 25 | tired                                     |     622 |   626 | Symptom                      |
| 26 | fussy                                     |     641 |   645 | Symptom                      |
| 27 | over the past 2 days                      |     647 |   666 | RelativeDate                 |
| 28 | albuterol                                 |     709 |   717 | Drug_Ingredient              |
| 29 | ER                                        |     743 |   744 | Clinical_Dept                |
| 30 | His                                       |     747 |   749 | Gender                       |
| 31 | urine output has also decreased           |     751 |   781 | Symptom                      |
| 32 | he                                        |     793 |   794 | Gender                       |
| 33 | per 24 hours                              |     832 |   843 | Frequency                    |
| 34 | he                                        |     850 |   851 | Gender                       |
| 35 | per 24 hours                              |     879 |   890 | Frequency                    |
| 36 | Mom                                       |     893 |   895 | Gender                       |
| 37 | diarrhea                                  |     908 |   915 | Symptom                      |
| 38 | His                                       |     918 |   920 | Gender                       |
| 39 | bowel                                     |     922 |   926 | Internal_organ_or_component  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_jsl_langtest_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.1.0+|
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