---
layout: model
title: NER Pipeline - Voice of the Patient
author: John Snow Labs
name: ner_vop_pipeline
date: 2024-01-10
tags: [licensed, en, vop, pipeline, ner]
task: [Named Entity Recognition, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.0
spark_version: 3.2
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline includes the full taxonomy Named-Entity Recognition model to extract information from health-related text in colloquial language. This pipeline extracts diagnoses, treatments, tests, anatomical references and demographic entities.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_vop_pipeline_en_5.2.0_3.2_1704890865951.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_vop_pipeline_en_5.2.0_3.2_1704890865951.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_vop_pipeline", "en", "clinical/models")

result = ner_pipeline.annotate("""Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you..""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("ner_vop_pipeline", "en", "clinical/models")

val result = ner_pipeline.annotate("""Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss,  from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you..""")

```
</div>

## Results

```bash
|    | chunks               |   begin |   end | entities               |
|---:|:---------------------|--------:|------:|:-----------------------|
|  0 | 20 year old          |      10 |    20 | Age                    |
|  1 | girl                 |      22 |    25 | Gender                 |
|  2 | hyperthyroid         |      47 |    58 | Disease                |
|  3 | 1 month ago          |      60 |    70 | DateTime               |
|  4 | weak                 |      87 |    90 | Symptom                |
|  5 | light                |      93 |    97 | Symptom                |
|  6 | panic attacks        |     122 |   134 | PsychologicalCondition |
|  7 | depression           |     137 |   146 | PsychologicalCondition |
|  8 | left                 |     149 |   152 | Laterality             |
|  9 | chest                |     154 |   158 | BodyPart               |
| 10 | pain                 |     160 |   163 | Symptom                |
| 11 | increased            |     166 |   174 | TestResult             |
| 12 | heart rate           |     176 |   185 | VitalTest              |
| 13 | rapidly              |     188 |   194 | Modifier               |
| 14 | weight loss          |     196 |   206 | Symptom                |
| 15 | 4 months             |     215 |   222 | Duration               |
| 16 | hospital             |     258 |   265 | ClinicalDept           |
| 17 | discharged           |     276 |   285 | AdmissionDischarge     |
| 18 | hospital             |     292 |   299 | ClinicalDept           |
| 19 | blood tests          |     319 |   329 | Test                   |
| 20 | brain                |     332 |   336 | BodyPart               |
| 21 | mri                  |     338 |   340 | Test                   |
| 22 | ultrasound scan      |     343 |   357 | Test                   |
| 23 | endoscopy            |     360 |   368 | Procedure              |
| 24 | doctors              |     391 |   397 | Employment             |
| 25 | homeopathy doctor    |     486 |   502 | Employment             |
| 26 | he                   |     512 |   513 | Gender                 |
| 27 | hyperthyroid         |     546 |   557 | Disease                |
| 28 | TSH                  |     566 |   568 | Test                   |
| 29 | 0.15                 |     574 |   577 | TestResult             |
| 30 | T3                   |     579 |   580 | Test                   |
| 31 | T4                   |     586 |   587 | Test                   |
| 32 | normal               |     592 |   597 | TestResult             |
| 33 | b12 deficiency       |     613 |   626 | Disease                |
| 34 | vitamin D deficiency |     632 |   651 | Disease                |
| 35 | weekly               |     667 |   672 | Frequency              |
| 36 | supplement           |     674 |   683 | Drug                   |
| 37 | vitamin D            |     688 |   696 | Drug                   |
| 38 | 1000 mcg             |     702 |   709 | Dosage                 |
| 39 | b12                  |     711 |   713 | Drug                   |
| 40 | daily                |     715 |   719 | Frequency              |
| 41 | homeopathy medicine  |     733 |   751 | Drug                   |
| 42 | 40 days              |     757 |   763 | Duration               |
| 43 | 2nd test             |     774 |   781 | Test                   |
| 44 | after 30 days        |     783 |   795 | DateTime               |
| 45 | TSH                  |     801 |   803 | Test                   |
| 46 | 0.5                  |     808 |   810 | TestResult             |
| 47 | now                  |     812 |   814 | DateTime               |
| 48 | weakness             |     849 |   856 | Symptom                |
| 49 | depression           |     862 |   871 | PsychologicalCondition |
| 50 | last week            |     912 |   920 | DateTime               |
| 51 | rapid heartrate      |     960 |   974 | Symptom                |
| 52 | allopathy medicine   |    1015 |  1032 | Treatment              |
| 53 | homeopathy           |    1037 |  1046 | Treatment              |
| 54 | thyroid              |    1074 |  1080 | BodyPart               |
| 55 | allopathy            |    1217 |  1225 | Treatment              |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_vop_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
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