---
layout: model
title: Pipeline to Detect Clinical Entities (BertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_jsl_pipeline
date: 2023-06-06
tags: [licensed, en, clinical, ner, ner_jsl, bertfortokenclassification]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [bert_token_classifier_ner_jsl](https://nlp.johnsnowlabs.com/2023/05/04/bert_token_classifier_ner_jsl_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_pipeline_en_4.3.0_3.2_1686088562944.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_pipeline_en_4.3.0_3.2_1686088562944.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("bert_token_classifier_ner_jsl_pipeline", "en", "clinical/models")

text = """The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("bert_token_classifier_ner_jsl_pipeline", "en", "clinical/models")

val text = """The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
|    | ner_chunks                                |   begin |   end | ner_labels                   |   confidence |
|---:|:------------------------------------------|--------:|------:|:-----------------------------|-------------:|
|  0 | 21-day-old                                |      17 |    26 | Age                          |     0.996622 |
|  1 | Caucasian                                 |      28 |    36 | Race_Ethnicity               |     0.999759 |
|  2 | male                                      |      38 |    41 | Gender                       |     0.999847 |
|  3 | 2 days                                    |      52 |    57 | Duration                     |     0.818646 |
|  4 | congestion                                |      62 |    71 | Symptom                      |     0.997344 |
|  5 | mom                                       |      75 |    77 | Gender                       |     0.999601 |
|  6 | yellow                                    |      99 |   104 | Symptom                      |     0.476263 |
|  7 | discharge                                 |     106 |   114 | Symptom                      |     0.704853 |
|  8 | nares                                     |     135 |   139 | External_body_part_or_region |     0.999152 |
|  9 | she                                       |     147 |   149 | Gender                       |     0.999927 |
| 10 | mild                                      |     168 |   171 | Modifier                     |     0.999674 |
| 11 | problems with his breathing while feeding |     173 |   213 | Symptom                      |     0.995353 |
| 12 | perioral cyanosis                         |     237 |   253 | Symptom                      |     0.99852  |
| 13 | retractions                               |     258 |   268 | Symptom                      |     0.999806 |
| 14 | One day ago                               |     272 |   282 | RelativeDate                 |     0.99949  |
| 15 | mom                                       |     285 |   287 | Gender                       |     0.999779 |
| 16 | tactile temperature                       |     304 |   322 | Symptom                      |     0.997475 |
| 17 | Tylenol                                   |     345 |   351 | Drug_BrandName               |     0.998978 |
| 18 | Baby-girl                                 |     354 |   362 | Age                          |     0.990654 |
| 19 | decreased                                 |     382 |   390 | Symptom                      |     0.996808 |
| 20 | intake                                    |     397 |   402 | Symptom                      |     0.983608 |
| 21 | His                                       |     405 |   407 | Gender                       |     0.999922 |
| 22 | breast-feeding                            |     416 |   429 | External_body_part_or_region |     0.994421 |
| 23 | 20 minutes                                |     444 |   453 | Duration                     |     0.992322 |
| 24 | 5 to 10 minutes                           |     464 |   478 | Duration                     |     0.969913 |
| 25 | his                                       |     493 |   495 | Gender                       |     0.999908 |
| 26 | respiratory congestion                    |     497 |   518 | Symptom                      |     0.995677 |
| 27 | He                                        |     521 |   522 | Gender                       |     0.999803 |
| 28 | tired                                     |     555 |   559 | Symptom                      |     0.999463 |
| 29 | fussy                                     |     574 |   578 | Symptom                      |     0.996514 |
| 30 | over the past 2 days                      |     580 |   599 | RelativeDate                 |     0.998001 |
| 31 | albuterol                                 |     642 |   650 | Drug_Ingredient              |     0.99964  |
| 32 | ER                                        |     676 |   677 | Clinical_Dept                |     0.998161 |
| 33 | His                                       |     680 |   682 | Gender                       |     0.999921 |
| 34 | urine output has also decreased           |     684 |   714 | Symptom                      |     0.971606 |
| 35 | he                                        |     726 |   727 | Gender                       |     0.999916 |
| 36 | per 24 hours                              |     765 |   776 | Frequency                    |     0.910935 |
| 37 | he                                        |     783 |   784 | Gender                       |     0.999922 |
| 38 | per 24 hours                              |     812 |   823 | Frequency                    |     0.921849 |
| 39 | Mom                                       |     826 |   828 | Gender                       |     0.999606 |
| 40 | diarrhea                                  |     841 |   848 | Symptom                      |     0.999849 |
| 41 | His                                       |     851 |   853 | Gender                       |     0.999739 |
| 42 | bowel                                     |     855 |   859 | Internal_organ_or_component  |     0.999471 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jsl_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|405.4 MB|

## Included Models

- DocumentAssembler
- SentenceDetectorDLModel
- TokenizerModel
- MedicalBertForTokenClassifier
- NerConverterInternalModel