---
layout: model
title: Explain Clinical Document Voice of Patients (VOP) - Light
author: John Snow Labs
name: explain_clinical_doc_vop_light
date: 2025-06-27
tags: [licensed, en, clinical, pipeline, ner, voice_of_patients, vop]
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

This pipeline is designed to extract clinical/medical entities from texts written by non-healthcare professionals. In this pipeline, 3 NER models and 2 text matchers are used to extract the clinical entity labels.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/07.0.Pretrained_Clinical_Pipelines.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_light_en_6.0.2_3.4_1751037839163.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_light_en_6.0.2_3.4_1751037839163.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop_light", "en", "clinical/models")

result = ner_pipeline.annotate("""I am 60 years old and my health problems started around 5 years ago when I began getting constant headaches and feeling dizzy all the time. 
I went to my regular doctor, and they told me I had high blood pressure. They put me on amlodipine, 5 mg a day, to help lower it. 
About 2 years ago, I had an MRI, and they found I had something called an acoustic neuroma — it’s a non-cancerous tumor in the brain. That probably explained why my headaches were getting so bad. 
I went through the surgery, and thankfully there weren’t any big problems. After the surgery, I did lose some hearing on that side and developed ringing in my ear that hasn't gone away.
Last year, I started having chest pain and ended up going to the emergency room. They said I had heart disease and had to put a stent in one of the arteries in my heart (the LAD artery). 
Now I take aspirin 81 mg every day, metoprolol 25 mg twice a day, and atorvastatin 40 mg at night. 
Lately, I’ve been having more pain and stiffness in my joints. Blood tests showed inflammation, and I was diagnosed with rheumatoid arthritis. 
Now I take methotrexate once a week (15 mg) and also folic acid every day. 
On top of all that, my blood sugar has been running high, so my doctors are watching me for type 2 diabetes.
""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop_light", "en", "clinical/models")

val result = ner_pipeline.annotate("""I am 60 years old and my health problems started around 5 years ago when I began getting constant headaches and feeling dizzy all the time. 
I went to my regular doctor, and they told me I had high blood pressure. They put me on amlodipine, 5 mg a day, to help lower it. 
About 2 years ago, I had an MRI, and they found I had something called an acoustic neuroma — it’s a non-cancerous tumor in the brain. That probably explained why my headaches were getting so bad. 
I went through the surgery, and thankfully there weren’t any big problems. After the surgery, I did lose some hearing on that side and developed ringing in my ear that hasn't gone away.
Last year, I started having chest pain and ended up going to the emergency room. They said I had heart disease and had to put a stent in one of the arteries in my heart (the LAD artery). 
Now I take aspirin 81 mg every day, metoprolol 25 mg twice a day, and atorvastatin 40 mg at night. 
Lately, I’ve been having more pain and stiffness in my joints. Blood tests showed inflammation, and I was diagnosed with rheumatoid arthritis. 
Now I take methotrexate once a week (15 mg) and also folic acid every day. 
On top of all that, my blood sugar has been running high, so my doctors are watching me for type 2 diabetes.
""")

```
</div>

## Results

```bash
|    | chunks                           |   begin |   end | entities                  |
|---:|:---------------------------------|--------:|------:|:--------------------------|
|  0 | 60 years old                     |       5 |    16 | Age                       |
|  1 | around 5 years ago               |      49 |    66 | DateTime                  |
|  2 | constant                         |      89 |    96 | Modifier                  |
|  3 | headaches                        |      98 |   106 | Symptom                   |
|  4 | dizzy                            |     120 |   124 | Symptom                   |
|  5 | all the time                     |     126 |   137 | Duration                  |
|  6 | doctor                           |     162 |   167 | Employment                |
|  7 | high blood pressure              |     193 |   211 | TestResult                |
|  8 | amlodipine                       |     229 |   238 | Drug                      |
|  9 | 5 mg                             |     241 |   244 | Dosage                    |
| 10 | a day                            |     246 |   250 | Frequency                 |
| 11 | About 2 years ago                |     272 |   288 | DateTime                  |
| 12 | MRI                              |     300 |   302 | Test                      |
| 13 | acoustic neuroma                 |     346 |   361 | Disease_Syndrome_Disorder |
| 14 | non-cancerous tumor in the brain |     372 |   403 | Disease_Syndrome_Disorder |
| 15 | headaches                        |     437 |   445 | Symptom                   |
| 16 | lose some hearing                |     569 |   585 | Symptom                   |
| 17 | ringing in my ear                |     614 |   630 | Symptom                   |
| 18 | Last year                        |     655 |   663 | DateTime                  |
| 19 | chest pain                       |     683 |   692 | Symptom                   |
| 20 | emergency room                   |     720 |   733 | ClinicalDept              |
| 21 | heart disease                    |     752 |   764 | Disease_Syndrome_Disorder |
| 22 | stent                            |     783 |   787 | MedicalDevice             |
| 23 | arteries                         |     803 |   810 | BodyPart                  |
| 24 | heart                            |     818 |   822 | BodyPart                  |
| 25 | LAD artery                       |     829 |   838 | BodyPart                  |
| 26 | Now                              |     843 |   845 | DateTime                  |
| 27 | aspirin                          |     854 |   860 | Drug                      |
| 28 | 81 mg                            |     862 |   866 | Dosage                    |
| 29 | every day                        |     868 |   876 | Frequency                 |
| 30 | metoprolol                       |     879 |   888 | Drug                      |
| 31 | 25 mg                            |     890 |   894 | Dosage                    |
| 32 | twice a day                      |     896 |   906 | Frequency                 |
| 33 | atorvastatin                     |     913 |   924 | Drug                      |
| 34 | 40 mg                            |     926 |   930 | Dosage                    |
| 35 | at night                         |     932 |   939 | Frequency                 |
| 36 | pain                             |     973 |   976 | Symptom                   |
| 37 | stiffness in my joints           |     982 |  1003 | Symptom                   |
| 38 | Blood tests                      |    1006 |  1016 | Test                      |
| 39 | inflammation                     |    1025 |  1036 | Symptom                   |
| 40 | rheumatoid arthritis             |    1064 |  1083 | Disease_Syndrome_Disorder |
| 41 | Now                              |    1087 |  1089 | DateTime                  |
| 42 | methotrexate                     |    1098 |  1109 | Drug                      |
| 43 | once a week                      |    1111 |  1121 | Frequency                 |
| 44 | 15 mg                            |    1124 |  1128 | Dosage                    |
| 45 | folic acid                       |    1140 |  1149 | Drug                      |
| 46 | every day                        |    1151 |  1159 | Frequency                 |
| 47 | blood sugar                      |    1186 |  1196 | Test                      |
| 48 | high                             |    1215 |  1218 | TestResult                |
| 49 | doctors                          |    1227 |  1233 | Employment                |
| 50 | type 2 diabetes                  |    1255 |  1269 | Disease_Syndrome_Disorder |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_vop_light|
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
- MedicalNerModel
- NerConverterInternalModel
- RegexMatcherInternalModel
- ContextualParserModel
- ChunkConverter
- ChunkMergeModel