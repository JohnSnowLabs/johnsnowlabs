---
layout: model
title: Named Entity Recognition Profiling (VOP)
author: John Snow Labs
name: ner_profiling_vop
date: 2023-07-03
tags: [licensed, en, clinical, profiling, ner_profiling, ner, vop, voice_of_patients]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 4.4.4
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to explore all the available pretrained NER models at once for Voice of Patients. When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with `embeddings_clinical`.

Here are the NER models that this pretrained pipeline includes:

`ner_vop_clinical_dept`, `ner_vop_temporal`, `ner_vop_test`, `ner_vop`, `ner_vop_problem`, `ner_vop_problem_reduced`, `ner_vop_treatment`, `ner_vop_demographic`, `ner_vop_anatomy`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_vop_en_4.4.4_3.2_1688352121249.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_vop_en_4.4.4_3.2_1688352121249.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_vop", 'en', 'clinical/models')

result = ner_profiling_pipeline.annotate("""Hello, I am a 20-year-old woman who was diagnosed with hyperthyroidism around a month ago. For approximately four months, I've been experiencing symptoms such as feeling light-headed, battling poor digestion, dealing with anxiety attacks, depression, a sharp pain on my left side chest, an elevated heart rate, and a significant loss of weight. Due to these conditions, I was admitted to the hospital and just got discharged recently. During my hospital stay, a number of different tests were carried out by various physicians who initially struggled to pinpoint my actual medical condition. These tests included numerous blood tests, a brain MRI, an ultrasound scan, and an endoscopy. At long last, I was examined by a homeopathic doctor who finally diagnosed me with hyperthyroidism, indicating my TSH level was at a low 0.15 while my T3 and T4 levels were normal. Additionally, I was found to be deficient in vitamins B12 and D. Hence, I've been on a regimen of vitamin D supplements once a week and a daily dose of 1000 mcg of vitamin B12. I've been undergoing homeopathic treatment for the last 40 days and underwent a second test after a month which showed my TSH level increased to 0.5. While I'm noticing a slight improvement in my feelings of weakness and depression, over the last week, I've encountered two new challenges: difficulty breathing and a dramatically increased heart rate. I'm now at a crossroads where I am unsure if I should switch to allopathic treatment or continue with homeopathy. I understand that thyroid conditions take a while to improve, but I'm wondering if both treatments would require the same duration for recovery. Several of my acquaintances have recommended transitioning to allopathy and warn against taking risks, given the potential of developing severe complications. Please forgive any errors in my English and thank you for your understanding.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_vop", "en", "clinical/models")

val result = ner_profiling_pipeline.annotate("""Hello, I am a 20-year-old woman who was diagnosed with hyperthyroidism around a month ago. For approximately four months, I've been experiencing symptoms such as feeling light-headed, battling poor digestion, dealing with anxiety attacks, depression, a sharp pain on my left side chest, an elevated heart rate, and a significant loss of weight. Due to these conditions, I was admitted to the hospital and just got discharged recently. During my hospital stay, a number of different tests were carried out by various physicians who initially struggled to pinpoint my actual medical condition. These tests included numerous blood tests, a brain MRI, an ultrasound scan, and an endoscopy. At long last, I was examined by a homeopathic doctor who finally diagnosed me with hyperthyroidism, indicating my TSH level was at a low 0.15 while my T3 and T4 levels were normal. Additionally, I was found to be deficient in vitamins B12 and D. Hence, I've been on a regimen of vitamin D supplements once a week and a daily dose of 1000 mcg of vitamin B12. I've been undergoing homeopathic treatment for the last 40 days and underwent a second test after a month which showed my TSH level increased to 0.5. While I'm noticing a slight improvement in my feelings of weakness and depression, over the last week, I've encountered two new challenges: difficulty breathing and a dramatically increased heart rate. I'm now at a crossroads where I am unsure if I should switch to allopathic treatment or continue with homeopathy. I understand that thyroid conditions take a while to improve, but I'm wondering if both treatments would require the same duration for recovery. Several of my acquaintances have recommended transitioning to allopathy and warn against taking risks, given the potential of developing severe complications. Please forgive any errors in my English and thank you for your understanding.""")

```
</div>

## Results

```bash

 ******************** ner_vop_clinical_dept Model Results ******************** 

[('admitted', 'B-AdmissionDischarge'), ('hospital', 'B-ClinicalDept'), ('discharged', 'B-AdmissionDischarge'), ('hospital', 'B-ClinicalDept')]

 
 ******************** ner_vop_temporal Model Results ******************** 

[('a', 'B-DateTime'), ('month', 'I-DateTime'), ('ago', 'I-DateTime'), ('four', 'B-Duration'), ('months', 'I-Duration'), ('recently', 'B-DateTime'), ('once', 'B-Frequency'), ('a', 'I-Frequency'), ('week', 'I-Frequency'), ('daily', 'B-Frequency'), ('40', 'B-Duration'), ('days', 'I-Duration'), ('after', 'B-DateTime'), ('a', 'I-DateTime'), ('month', 'I-DateTime'), ('over', 'B-Duration'), ('the', 'I-Duration'), ('last', 'I-Duration'), ('week', 'I-Duration'), ('now', 'B-DateTime')]


 ******************** ner_vop_test Model Results ******************** 

[('elevated', 'B-TestResult'), ('heart', 'B-VitalTest'), ('rate', 'I-VitalTest'), ('weight', 'B-TestResult'), ('blood', 'B-Test'), ('tests', 'I-Test'), ('MRI', 'B-Test'), ('ultrasound', 'B-Test'), ('scan', 'I-Test'), ('TSH', 'B-Test'), ('low', 'B-TestResult'), ('0.15', 'B-TestResult'), ('T3', 'B-Test'), ('T4', 'B-Test'), ('normal', 'B-TestResult'), ('TSH', 'B-Test'), ('0.5', 'B-TestResult'), ('increased', 'B-TestResult'), ('heart', 'B-VitalTest'), ('rate', 'I-VitalTest')]

 
 ******************** ner_vop Model Results ******************** 

[('20-year-old', 'B-Age'), ('woman', 'B-Gender'), ('hyperthyroidism', 'B-Disease'), ('a', 'B-DateTime'), ('month', 'I-DateTime'), ('ago', 'I-DateTime'), ('four', 'B-Duration'), ('months', 'I-Duration'), ('light-headed', 'B-Symptom'), ('anxiety', 'B-PsychologicalCondition'), ('attacks', 'I-PsychologicalCondition'), ('depression', 'B-PsychologicalCondition'), ('sharp', 'B-Modifier'), ('pain', 'B-Symptom'), ('left', 'B-Laterality'), ('side', 'I-Laterality'), ('chest', 'B-BodyPart'), ('elevated', 'B-TestResult'), ('heart', 'B-VitalTest'), ('rate', 'I-VitalTest'), ('significant', 'B-Modifier'), ('loss', 'B-Symptom'), ('of', 'I-Symptom'), ('weight', 'I-Symptom'), ('admitted', 'B-AdmissionDischarge'), ('hospital', 'B-ClinicalDept'), ('discharged', 'B-AdmissionDischarge'), ('recently', 'B-DateTime'), ('hospital', 'B-ClinicalDept'), ('physicians', 'B-Employment'), ('blood', 'B-Test'), ('tests', 'I-Test'), ('brain', 'B-BodyPart'), ('MRI', 'B-Test'), ('ultrasound', 'B-Test'), ('scan', 'I-Test'), ('endoscopy', 'B-Procedure'), ('homeopathic', 'B-Employment'), ('doctor', 'I-Employment'), ('hyperthyroidism', 'B-Disease'), ('TSH', 'B-Test'), ('low', 'B-TestResult'), ('0.15', 'I-TestResult'), ('T3', 'B-Test'), ('T4', 'B-Test'), ('levels', 'I-Test'), ('normal', 'B-TestResult'), ('deficient', 'B-Disease'), ('vitamins', 'B-Drug'), ('B12', 'I-Drug'), ('D', 'B-Drug'), ('vitamin', 'B-Drug'), ('D', 'I-Drug'), ('supplements', 'I-Drug'), ('once', 'B-Frequency'), ('a', 'I-Frequency'), ('week', 'I-Frequency'), ('daily', 'B-Frequency'), ('1000', 'B-Dosage'), ('mcg', 'I-Dosage'), ('vitamin', 'B-Drug'), ('B12', 'I-Drug'), ('homeopathic', 'B-Treatment'), ('treatment', 'I-Treatment'), ('40', 'B-Duration'), ('days', 'I-Duration'), ('after', 'B-DateTime'), ('a', 'I-DateTime'), ('month', 'I-DateTime'), ('TSH', 'B-Test'), ('0.5', 'B-TestResult'), ('weakness', 'B-Symptom'), ('depression', 'B-PsychologicalCondition'), ('over', 'B-Duration'), ('the', 'I-Duration'), ('last', 'I-Duration'), ('week', 'I-Duration'), ('difficulty', 'B-Symptom'), ('breathing', 'I-Symptom'), ('increased', 'B-TestResult'), ('heart', 'B-VitalTest'), ('rate', 'I-VitalTest'), ('now', 'B-DateTime'), ('allopathic', 'B-Treatment'), ('treatment', 'I-Treatment'), ('homeopathy', 'B-Treatment'), ('thyroid', 'B-BodyPart')]

 
 ******************** ner_vop_problem Model Results ******************** 

[('hyperthyroidism', 'B-Disease'), ('light-headed', 'B-Symptom'), ('anxiety', 'B-PsychologicalCondition'), ('attacks', 'I-PsychologicalCondition'), ('depression', 'B-PsychologicalCondition'), ('sharp', 'B-Modifier'), ('pain', 'B-Symptom'), ('significant', 'B-Modifier'), ('loss', 'B-Symptom'), ('of', 'I-Symptom'), ('weight', 'I-Symptom'), ('hyperthyroidism', 'B-Disease'), ('weakness', 'B-Symptom'), ('depression', 'B-PsychologicalCondition'), ('difficulty', 'B-Symptom'), ('breathing', 'I-Symptom')]

 
 ******************** ner_vop_problem_reduced Model Results ******************** 

[('hyperthyroidism', 'B-Problem'), ('light-headed', 'B-Problem'), ('poor', 'B-Problem'), ('digestion', 'I-Problem'), ('anxiety', 'B-Problem'), ('attacks', 'I-Problem'), ('depression', 'B-Problem'), ('sharp', 'B-Modifier'), ('pain', 'B-Problem'), ('significant', 'B-Modifier'), ('loss', 'B-Problem'), ('of', 'I-Problem'), ('weight', 'I-Problem'), ('hyperthyroidism', 'B-Problem'), ('deficient', 'B-Problem'), ('weakness', 'B-Problem'), ('depression', 'B-Problem'), ('difficulty', 'B-Problem'), ('breathing', 'I-Problem')]

 
 ******************** ner_vop_treatment Model Results ******************** 

[('four', 'B-Duration'), ('months', 'I-Duration'), ('endoscopy', 'B-Procedure'), ('vitamins', 'B-Drug'), ('B12', 'I-Drug'), ('D', 'B-Drug'), ('vitamin', 'B-Drug'), ('D', 'I-Drug'), ('supplements', 'B-Drug'), ('once', 'B-Frequency'), ('a', 'I-Frequency'), ('week', 'I-Frequency'), ('daily', 'B-Frequency'), ('1000', 'B-Dosage'), ('mcg', 'I-Dosage'), ('vitamin', 'B-Drug'), ('B12', 'I-Drug'), ('homeopathic', 'B-Treatment'), ('treatment', 'I-Treatment'), ('40', 'B-Duration'), ('days', 'I-Duration'), ('over', 'B-Duration'), ('the', 'I-Duration'), ('last', 'I-Duration'), ('week', 'I-Duration'), ('homeopathy', 'B-Treatment'), ('allopathy', 'B-Treatment')]


 ******************** ner_vop_demographic Model Results ******************** 

[('20-year-old', 'B-Age'), ('woman', 'B-Gender'), ('physicians', 'B-Employment'), ('homeopathic', 'B-Employment'), ('doctor', 'I-Employment')]

 
 ******************** ner_vop_anatomy Model Results ******************** 

[('left', 'B-Laterality'), ('side', 'I-Laterality'), ('chest', 'B-BodyPart'), ('brain', 'B-BodyPart'), ('thyroid', 'B-BodyPart')]


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_vop|
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