---
layout: model
title: Named Entity Recognition Profiling (VOP)
author: John Snow Labs
name: ner_profiling_vop
date: 2024-06-03
tags: [licensed, en, clinical, profiling, ner_profiling, ner, vop, voice_of_patients]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.3.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline can be used to simultaneously evaluate various pre-trained named entity recognition (NER) models, enabling comprehensive analysis of text data pertaining to patient perspectives and experiences, also known as the "Voice of Patients”.  When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with the`embeddings_clinical`, which are specifically designed for clinical and biomedical text.

`ner_vop`, `ner_vop_langtest`, `ner_vop_anatomy`, `ner_vop_anatomy_langtest`, `ner_vop_clinical_dept`, `ner_vop_clinical_dept_langtest`, `ner_vop_demographic`, `ner_vop_demographic_langtest`, `ner_vop_problem`, `ner_vop_problem_langtest`, `ner_vop_problem_reduced`, `ner_vop_problem_reduced_langtest`, `ner_vop_temporal`, `ner_vop_temporal_langtest`, `ner_vop_test`, `ner_vop_test_langtest`, `ner_vop_treatment`, `ner_vop_treatment_langtest`, `ner_jsl`, `ner_jsl_langtest`, `ner_jsl_greedy`, `ner_jsl_enriched`, `ner_jsl_slim`

## Predicted Entities

`AdmissionDischarge`, `Admission_Discharge`, `Age`, `Allergen`, `BodyPart`, `Cancer_Modifier`, `Cerebrovascular_Disease`, `ClinicalDept`, `Clinical_Dept`, `Communicable_Disease`, `Date`, `DateTime`, `Diabetes`, `Direction`, `Disease`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Drug_BrandName`, `Drug_Ingredient`, `Duration`, `Employment`, `External_body_part_or_region`, `Form`, `Frequency`, `Gender`, `HealthStatus`, `Heart_Disease`, `Hyperlipidemia`, `Hypertension`, `InjuryOrPoisoning`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `Laterality`, `Measurements`, `MedicalDevice`, `Medical_Device`, `Modifier`, `Obesity`, `Oncological`, `Problem`, `Procedure`, `PsychologicalCondition`, `Psychological_Condition`, `RaceEthnicity`, `RelationshipStatus`, `Relationship_Status`, `RelativeDate`, `Route`, `Substance`, `SubstanceQuantity`, `Substance_Quantity`, `Symptom`, `Test`, `TestResult`, `Test_Result`, `Treatment`, `VS_Finding`, `Vaccine`, `Vaccine_Name`, `VitalTest`

`AdmissionDischarge`, `Age`, `Allergen`, `BodyPart`, `ClinicalDept`, `DateTime`, `Disease`, `Dosage`, `Drug`, `Duration`, `Employment`, `Form`, `Frequency`, `Gender`, `HealthStatus`, `InjuryOrPoisoning`, `Laterality`, `Measurements`, `MedicalDevice`, `Modifier`, `Problem`, `Procedure`, `PsychologicalCondition`, `RaceEthnicity`, `RelationshipStatus`, `Route`, `Substance`, `SubstanceQuantity`, `Symptom`, `Test`, `TestResult`, `Treatment`, `Vaccine`, `VitalTest`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_vop_en_5.3.2_3.0_1717441626868.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_vop_en_5.3.2_3.0_1717441626868.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_vop", 'en', 'clinical/models')

text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,
from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to
diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and
vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now.
I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine
or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance
as i can develop some serious problems. """

result = ner_profiling_pipeline.fullAnnotate(text)

```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_vop", "en", "clinical/models")

val text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,
from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to
diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and
vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now.
I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine
or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance
as i can develop some serious problems."""

val result = ner_profiling_pipeline.fullAnnotate(text)

```
</div>

## Results

```bash

******************** ner_vop_problem_reduced Model Results ******************** 

('hyperthyroid', 'Problem') ('weak', 'Problem') ('light headed,poor digestion', 'Problem') ('panic attacks', 'Problem') ('depression', 'Problem') ('pain', 'Problem') ('rapidly', 'Modifier') ('weight loss', 'Problem') ('hyperthyroid', 'Problem') ('b12 deficiency', 'Problem') ('vitamin D deficiency', 'Problem') ('weakness', 'Problem') ('depression', 'Problem') ('Bcs', 'Problem')

******************** ner_jsl_greedy Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('1 month ago', 'RelativeDate') ('feeling weak', 'Symptom') ('light', 'Symptom') ('digestion', 'Symptom') ('panic attacks', 'Symptom') ('depression', 'Psychological_Condition') ('left', 'Direction') ('chest pain', 'Symptom') ('increased heart rate', 'Symptom') ('rapidly weight loss', 'Symptom') ('4 months', 'RelativeDate') ('hospital', 'Clinical_Dept') ('discharged', 'Admission_Discharge') ('hospital', 'Clinical_Dept') ('blood tests', 'Test') ('brain mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('TSH', 'Test') ('0.15 T3', 'Test_Result') ('T4', 'Test') ('normal', 'Test_Result') ('b12 deficiency', 'Disease_Syndrome_Disorder') ('vitamin D deficiency', 'Disease_Syndrome_Disorder') ('after 30 days', 'RelativeDate') ('TSH', 'Test') ('0.5', 'Test_Result') ('weakness', 'Symptom') ('depression', 'Psychological_Condition') ('from last week', 'RelativeDate') ('thyroid', 'Internal_organ_or_component')

******************** ner_jsl_enriched Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('1 month ago', 'RelativeDate') ('feeling weak', 'Symptom') ('light headed,poor digestion', 'Symptom') ('panic attacks', 'Disease_Syndrome_Disorder') ('depression', 'Psychological_Condition') ('left', 'Direction') ('chest pain', 'Symptom') ('increased heart rate', 'Symptom') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('hospital', 'Clinical_Dept') ('discharged', 'Admission_Discharge') ('hospital', 'Clinical_Dept') ('blood tests', 'Test') ('brain mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('TSH', 'Test') ('0.15', 'Test_Result') ('T3', 'Test') ('T4', 'Test') ('normal', 'Test_Result') ('b12 deficiency', 'Disease_Syndrome_Disorder') ('vitamin D deficiency', 'Disease_Syndrome_Disorder') ('vitamin D', 'Drug_Ingredient') ('b12', 'Drug_Ingredient') ('homeopathy medicine', 'Drug_Ingredient') ('after 30 days', 'RelativeDate') ('TSH', 'Test') ('0.5', 'Test_Result') ('weakness', 'Symptom') ('depression', 'Psychological_Condition') ('from last week', 'RelativeDate') ('very', 'Modifier') ('rapid heartrate', 'Symptom') ('thyroid', 'Internal_organ_or_component')

******************** ner_jsl_slim Model Results ******************** 

('20 year old', 'Age') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('weak', 'Symptom') ('light headed,poor digestion', 'Symptom') ('panic attacks', 'Symptom') ('depression', 'Disease_Syndrome_Disorder') ('chest pain', 'Symptom') ('increased heart rate', 'Symptom') ('rapidly weight loss', 'Symptom') ('hospital', 'Clinical_Dept') ('discharged', 'Admission_Discharge') ('hospital', 'Clinical_Dept') ('blood tests', 'Test') ('brain mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('TSH', 'Test') ('0.15', 'Test_Result') ('T3', 'Test') ('T4', 'Test') ('normal', 'Test_Result') ('b12 deficiency', 'Disease_Syndrome_Disorder') ('vitamin D deficiency', 'Disease_Syndrome_Disorder') ('2nd test', 'Test') ('TSH', 'Test') ('0.5', 'Test_Result') ('weakness', 'Symptom') ('depression', 'Disease_Syndrome_Disorder') ('very rapid heartrate', 'Symptom') ('homeopathy', 'Treatment')

******************** ner_vop_problem_reduced_langtest Model Results ******************** 

('hyperthyroid', 'Problem') ('weak', 'Problem') ('light', 'Problem') ('digestion', 'Problem') ('panic attacks', 'Problem') ('depression', 'Problem') ('pain', 'Problem') ('rapidly', 'Modifier') ('weight loss', 'Problem') ('bcs', 'Problem') ('hyperthyroid', 'Problem') ('b12 deficiency', 'Problem') ('vitamin D deficiency', 'Problem') ('weakness', 'Problem') ('depression', 'Problem') ('rapid heartrate', 'Problem') ('Bcs', 'Problem')

******************** ner_vop_clinical_dept_ner Model Results ******************** 

('hospital', 'ClinicalDept') ('discharged', 'AdmissionDischarge') ('hospital', 'ClinicalDept')

******************** ner_vop_problem Model Results ******************** 

('hyperthyroid', 'Disease') ('weak', 'Symptom') ('light', 'Symptom') ('panic attacks', 'PsychologicalCondition') ('depression', 'PsychologicalCondition') ('pain', 'Symptom') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('hyperthyroid', 'Disease') ('b12 deficiency', 'Disease') ('vitamin D deficiency', 'Disease') ('weakness', 'Symptom') ('depression', 'PsychologicalCondition')

******************** ner_vop Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease') ('1 month ago', 'DateTime') ('weak', 'Symptom') ('light', 'Symptom') ('panic attacks', 'PsychologicalCondition') ('depression', 'PsychologicalCondition') ('left', 'Laterality') ('chest', 'BodyPart') ('pain', 'Symptom') ('increased', 'TestResult') ('heart rate', 'VitalTest') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('4 months', 'Duration') ('hospital', 'ClinicalDept') ('discharged', 'AdmissionDischarge') ('hospital', 'ClinicalDept') ('blood tests', 'Test') ('brain', 'BodyPart') ('mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease') ('TSH', 'Test') ('0.15', 'TestResult') ('T3', 'Test') ('T4', 'Test') ('normal', 'TestResult') ('b12 deficiency', 'Disease') ('vitamin D deficiency', 'Disease') ('weekly', 'Frequency') ('supplement', 'Drug') ('vitamin D', 'Drug') ('1000 mcg', 'Dosage') ('b12', 'Drug') ('daily', 'Frequency') ('homeopathy medicine', 'Drug') ('40 days', 'Duration') ('2nd test', 'Test') ('after 30 days', 'DateTime') ('TSH', 'Test') ('0.5', 'TestResult') ('now', 'DateTime') ('weakness', 'Symptom') ('depression', 'PsychologicalCondition') ('last week', 'DateTime') ('rapid heartrate', 'Symptom') ('allopathy medicine', 'Treatment') ('homeopathy', 'Treatment') ('thyroid', 'BodyPart') ('allopathy', 'Treatment')

******************** ner_vop_clinical_dept_langtest_ner Model Results ******************** 

('hospital', 'ClinicalDept') ('discharged', 'AdmissionDischarge') ('hospital', 'ClinicalDept')

******************** ner_jsl Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('1 month ago', 'RelativeDate') ('weak', 'Symptom') ('light headed,poor digestion', 'Symptom') ('panic attacks', 'Symptom') ('depression', 'Psychological_Condition') ('left', 'Direction') ('chest pain', 'Symptom') ('increased heart rate', 'Symptom') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('hospital', 'Clinical_Dept') ('discharged', 'Admission_Discharge') ('hospital', 'Clinical_Dept') ('blood tests', 'Test') ('brain mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('TSH', 'Test') ('0.15 T3', 'Test_Result') ('T4', 'Test') ('normal', 'Test_Result') ('b12 deficiency', 'Disease_Syndrome_Disorder') ('vitamin D', 'Drug_Ingredient') ('deficiency', 'Disease_Syndrome_Disorder') ('vitamin D', 'Drug_Ingredient') ('b12', 'Drug_Ingredient') ('homeopathy medicine', 'Treatment') ('after 30 days', 'RelativeDate') ('TSH', 'Test') ('0.5', 'Test_Result') ('weakness', 'Symptom') ('depression', 'Psychological_Condition') ('from last week', 'RelativeDate') ('allopathy medicine', 'Treatment') ('homeopathy', 'Treatment') ('thyroid', 'Internal_organ_or_component') ('allopathy', 'Drug_BrandName')

******************** ner_vop_anatomy Model Results ******************** 

('left', 'Laterality') ('chest', 'BodyPart') ('brain', 'BodyPart') ('thyroid', 'BodyPart')

******************** ner_vop_langtest Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease') ('1 month ago', 'DateTime') ('weak', 'Symptom') ('light', 'Symptom') ('digestion', 'Symptom') ('panic attacks', 'PsychologicalCondition') ('depression', 'PsychologicalCondition') ('left', 'Laterality') ('chest', 'BodyPart') ('pain', 'Symptom') ('increased', 'TestResult') ('heart rate', 'VitalTest') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('4 months', 'Duration') ('hospital', 'ClinicalDept') ('discharged', 'AdmissionDischarge') ('hospital', 'ClinicalDept') ('blood tests', 'Test') ('brain', 'BodyPart') ('mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease') ('TSH', 'Test') ('0.15', 'TestResult') ('T3', 'Test') ('T4', 'Test') ('normal', 'TestResult') ('b12 deficiency', 'Disease') ('vitamin D deficiency', 'Disease') ('weekly', 'Frequency') ('supplement', 'Drug') ('vitamin D', 'Drug') ('1000 mcg', 'Dosage') ('b12', 'Drug') ('daily', 'Frequency') ('homeopathy medicine', 'Drug') ('40 days', 'Duration') ('2nd test', 'Test') ('after 30 days', 'DateTime') ('TSH', 'Test') ('0.5', 'TestResult') ('now', 'DateTime') ('weakness', 'Symptom') ('depression', 'PsychologicalCondition') ('last week', 'DateTime') ('rapid heartrate', 'Symptom') ('allopathy medicine', 'Drug') ('homeopathy', 'Treatment') ('thyroid', 'BodyPart') ('allopathy', 'Treatment')

******************** ner_vop_treatment_langtest Model Results ******************** 

('20 year', 'Duration') ('4 months', 'Duration') ('endoscopy', 'Procedure') ('weekly', 'Frequency') ('supplement', 'Drug') ('vitamin D', 'Drug') ('1000 mcg', 'Dosage') ('b12', 'Drug') ('daily', 'Frequency') ('homeopathy medicine', 'Drug') ('40 days', 'Duration') ('now', 'Frequency') ('allopathy', 'Treatment') ('homeopathy', 'Treatment') ('allopathy', 'Treatment')

******************** ner_vop_test_langtest_ner Model Results ******************** 

('increased', 'TestResult') ('heart rate', 'VitalTest') ('blood tests', 'Test') ('mri', 'Test') ('ultrasound scan', 'Test') ('TSH', 'Test') ('0.15', 'TestResult') ('T3', 'Test') ('T4', 'Test') ('normal', 'TestResult') ('2nd test', 'Test') ('TSH', 'Test') ('0.5', 'TestResult') ('rapid', 'TestResult') ('heartrate', 'VitalTest') ('okay', 'TestResult')

******************** ner_vop_test_ner Model Results ******************** 

('increased', 'TestResult') ('heart rate', 'VitalTest') ('blood tests', 'Test') ('mri', 'Test') ('ultrasound scan', 'Test') ('TSH', 'Test') ('0.15', 'TestResult') ('T3', 'Test') ('T4', 'Test') ('normal', 'TestResult') ('2nd test', 'Test') ('TSH', 'Test') ('0.5', 'TestResult')

******************** ner_vop_treatment Model Results ******************** 

('4 months', 'Duration') ('endoscopy', 'Procedure') ('weekly', 'Frequency') ('supplement', 'Drug') ('vitamin D', 'Drug') ('1000 mcg', 'Dosage') ('b12', 'Drug') ('daily', 'Frequency') ('homeopathy medicine', 'Drug') ('40 days', 'Duration') ('allopathy', 'Treatment') ('homeopathy', 'Treatment') ('allopathy', 'Treatment')

******************** ner_vop_temporal Model Results ******************** 

('1 month ago', 'DateTime') ('4 months', 'Duration') ('weekly', 'Frequency') ('daily', 'Frequency') ('40 days', 'Duration') ('after 30 days', 'DateTime') ('now', 'DateTime') ('last week', 'DateTime')

******************** ner_vop_temporal_langtest Model Results ******************** 

('1 month ago', 'DateTime') ('4 months', 'Duration') ('weekly', 'Frequency') ('daily', 'Frequency') ('40 days', 'Duration') ('after 30 days', 'DateTime') ('now', 'DateTime') ('from last week', 'DateTime') ('same time', 'DateTime')

******************** ner_vop_anatomy_langtest Model Results ******************** 

('left', 'Laterality') ('chest', 'BodyPart') ('brain', 'BodyPart') ('heartrate', 'BodyPart') ('thyroid', 'BodyPart')

******************** ner_jsl_langtest Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('1 month ago', 'RelativeDate') ('weak', 'Symptom') ('light headed,poor digestion', 'Symptom') ('panic attacks', 'Symptom') ('depression', 'Psychological_Condition') ('left', 'Direction') ('chest pain', 'Symptom') ('increased heart rate', 'Symptom') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('hospital', 'Clinical_Dept') ('discharged', 'Admission_Discharge') ('hospital', 'Clinical_Dept') ('blood tests', 'Test') ('brain mri', 'Test') ('ultrasound scan', 'Test') ('endoscopy', 'Procedure') ('dumb doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender') ('hyperthyroid', 'Disease_Syndrome_Disorder') ('TSH', 'Test') ('0.15', 'Test_Result') ('T3', 'Test') ('T4', 'Test') ('normal', 'Test_Result') ('b12 deficiency', 'Disease_Syndrome_Disorder') ('vitamin D deficiency', 'Disease_Syndrome_Disorder') ('vitamin D', 'Drug_Ingredient') ('homeopathy medicine', 'Clinical_Dept') ('after 30 days', 'RelativeDate') ('TSH', 'Test') ('0.5', 'Test_Result') ('weakness', 'Symptom') ('depression', 'Psychological_Condition') ('from last week', 'RelativeDate') ('very', 'Modifier') ('rapid heartrate', 'Symptom') ('allopathy medicine', 'Clinical_Dept') ('Bcs i', 'Internal_organ_or_component') ('thyroid', 'Internal_organ_or_component')

******************** ner_vop_demographic Model Results ******************** 

('20 year old', 'Age') ('girl', 'Gender') ('doctors', 'Employment') ('homeopathy doctor', 'Employment') ('he', 'Gender')

******************** ner_vop_problem_langtest Model Results ******************** 

('hyperthyroid', 'Disease') ('weak', 'Symptom') ('light', 'Symptom') ('digestion', 'Symptom') ('panic attacks', 'PsychologicalCondition') ('depression', 'PsychologicalCondition') ('pain', 'Symptom') ('rapidly', 'Modifier') ('weight loss', 'Symptom') ('bcs', 'Disease') ('hyperthyroid', 'Disease') ('b12 deficiency', 'Disease') ('vitamin D deficiency', 'Disease') ('weakness', 'Symptom') ('depression', 'PsychologicalCondition') ('Bcs', 'Disease') ('allopathy', 'Symptom')

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_vop|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.9 GB|

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
