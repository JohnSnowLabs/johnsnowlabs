---
layout: model
title: Explain Clinical Document Mental Health - Light
author: John Snow Labs
name: explain_clinical_doc_mental_health_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, mental_health]
task: [Pipeline Healthcare, Named Entity Recognition]
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to extract mental health related clinical/medical entities from text. In this pipeline, 2 NER models and a text matcher are used to extract the clinical entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_light_en_6.0.2_3.4_1751063700768.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_mental_health_light_en_6.0.2_3.4_1751063700768.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_mental_health_light", "en", "clinical/models")

result = ner_pipeline.annotate("""
The patient is a 29-year-old female presenting with persistent anxiety, insomnia, and feelings of hopelessness over the past 6 months. 
She reports daily alcohol use and occasional cannabis consumption. She recently lost her job, which has worsened her symptoms. 
The PHQ-9 test was administered, with a score of 18 indicating moderately severe depression. No history of self-harm or suicidal behavior was noted. 
She has a diagnosis of generalized anxiety disorder and is currently prescribed sertraline 50mg daily.
Substance use, including alcohol, marijuana and tobacco, was notably prevalent among young adults, while older adults reported feelings of isolation and untreated mental health issues.
The report also highlighted increasing rates of communicable diseases such as Hepatitis C among individuals with a history of intravenous drug use.
Domestic violence and housing insecurity were frequently mentioned, especially among single mothers.
In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_mental_health_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""
The patient is a 29-year-old female presenting with persistent anxiety, insomnia, and feelings of hopelessness over the past 6 months. 
She reports daily alcohol use and occasional cannabis consumption. She recently lost her job, which has worsened her symptoms. 
The PHQ-9 test was administered, with a score of 18 indicating moderately severe depression. No history of self-harm or suicidal behavior was noted. 
She has a diagnosis of generalized anxiety disorder and is currently prescribed sertraline 50mg daily.
Substance use, including alcohol, marijuana and tobacco, was notably prevalent among young adults, while older adults reported feelings of isolation and untreated mental health issues.
The report also highlighted increasing rates of communicable diseases such as Hepatitis C among individuals with a history of intravenous drug use.
Domestic violence and housing insecurity were frequently mentioned, especially among single mothers.
In response, his doctor prescribed a regimen tailored to his conditions:
Thiamine 100 mg q.day , Folic acid 1 mg q.day , multivitamins q.day , Calcium carbonate plus Vitamin D 250 mg t.i.d. , Heparin 5000 units subcutaneously b.i.d. , Prilosec 20 mg q.day , Senna two tabs qhs.
""")

```
</div>

## Results

```bash
|    | chunks                       |   begin |   end | entities          |
|---:|:-----------------------------|--------:|------:|:------------------|
|  0 | 29-year-old                  |      18 |    28 | Age               |
|  1 | anxiety                      |      64 |    70 | Mental_Health     |
|  2 | insomnia                     |      73 |    80 | Mental_Health     |
|  3 | feelings of hopelessness     |      87 |   110 | Symptom           |
|  4 | alcohol                      |     155 |   161 | Alcohol           |
|  5 | cannabis                     |     182 |   189 | Substance_Use     |
|  6 | PHQ-9 test                   |     269 |   278 | Test              |
|  7 | depression                   |     346 |   355 | Mental_Health     |
|  8 | self-harm                    |     372 |   380 | Mental_Health     |
|  9 | suicidal behavior            |     385 |   401 | Mental_Health     |
| 10 | generalized anxiety disorder |     438 |   465 | Mental_Health     |
| 11 | sertraline                   |     495 |   504 | DRUG              |
| 12 | Substance                    |     518 |   526 | Substance_Use     |
| 13 | alcohol                      |     543 |   549 | Alcohol           |
| 14 | marijuana                    |     552 |   560 | Substance_Use     |
| 15 | tobacco                      |     566 |   572 | Smoking           |
| 16 | isolation                    |     657 |   665 | Social_Exclusion  |
| 17 | mental health issues         |     681 |   700 | Mental_Health     |
| 18 | intravenous drug             |     829 |   844 | Substance_Use     |
| 19 | Domestic violence            |     851 |   867 | Violence_Or_Abuse |
| 20 | mothers                      |     943 |   949 | Family_Member     |
| 21 | Thiamine                     |    1025 |  1032 | DRUG              |
| 22 | Folic acid                   |    1049 |  1058 | DRUG              |
| 23 | multivitamins                |    1073 |  1085 | DRUG              |
| 24 | Calcium carbonate            |    1095 |  1111 | DRUG              |
| 25 | Vitamin D                    |    1118 |  1126 | DRUG              |
| 26 | Heparin                      |    1144 |  1150 | DRUG              |
| 27 | Prilosec                     |    1187 |  1194 | DRUG              |
| 28 | Senna                        |    1210 |  1214 | DRUG              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_mental_health_light|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.0.2+|
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
- TextMatcherInternalModel
- ChunkMergeModel