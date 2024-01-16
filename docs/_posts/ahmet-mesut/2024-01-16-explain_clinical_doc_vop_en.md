---
layout: model
title: Explain Clinical Document - Voice Of Patient (VOP)
author: John Snow Labs
name: explain_clinical_doc_vop
date: 2024-01-16
tags: [licensed, clinical, en, vop, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
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

This pipeline is designed to:

    - extract all clinical/medical entities from text,

    - assign assertion status to the extracted entities,

    - establish relations between the extracted entities.

6 NER models, one assertion model and one relation extraction model were used in order to achieve those tasks.

Clinical Entity Labels: `Gender`, `Employment`, `Age`, `BodyPart`, `Substance`, `Form`, `PsychologicalCondition`, `Vaccine`, `Drug`, `DateTime`, `ClinicalDept`, `Laterality`, `Test`, `AdmissionDischarge`, `Disease_Syndrome_Disorder`, `VitalTest`, `Dosage`, `Duration`, `RelationshipStatus`, `Route`, `Allergen`, `Frequency`, `Symptom`, `Procedure`, `HealthStatus`, `InjuryOrPoisoning`, `Modifier`, `Treatment`, `SubstanceQuantity`, `MedicalDevice`, `TestResult`, `Alcohol`, `Smoking`

Assertion Status Labels: `Present_Or_Past`, `Hypothetical_Or_Absent`, `SomeoneElse`

Relation Extraction Labels: `Drug-Dosage`, `Drug-Frequency`, `Drug-Duration`, `Drug-Strength`, `Drug-Drug`, `Test-TestResult`, `Disease_Syndrome_Disorder-Treatment`, `Disease_Syndrome_Disorder-Symptom`, `Disease_Syndrome_Disorder-Modifier`, `Symptom-Modifier`, `Disease_Syndrome_Disorder-BodyPart`, `Symptom-BodyPart`,  `Procedure-DateTime`, `Test-DateTime`, `VitalTest-TestResult`,  `Disease_Syndrome_Disorder-Drug`, `Treatment-Drug`, `Disease_Syndrome_Disorder-Procedure`, `Procedure-Drug`, `Procedure-BodyPart`, `Treatment-BodyPart`, `BodyPart-Procedure`, `MedicalDevice-Procedure`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_en_5.2.0_3.2_1705435295643.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_en_5.2.0_3.2_1705435295643.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop", "en", "clinical/models")

result = ner_pipeline.annotate("""I had been feeling really tired all the time and was losing weight without even trying. My doctor checked my sugar levels and they came out to be high. So, I have type 2 diabetes. 
He put me on two medications - I take metformin 500 mg twice a day, and glipizide 5 mg before breakfast and dinner. I also have to watch what I eat and try to exercise more.
Now, I also have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to reduce the stomach acid and control the heartburn symptoms.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_vop", "en", "clinical/models")

val result = ner_pipeline.annotate("""I had been feeling really tired all the time and was losing weight without even trying. My doctor checked my sugar levels and they came out to be high. So, I have type 2 diabetes. 
He put me on two medications - I take metformin 500 mg twice a day, and glipizide 5 mg before breakfast and dinner. I also have to watch what I eat and try to exercise more.
Now, I also have chronic acid reflux disease or GERD. Now I take a daily pill called omeprazole 20 mg to reduce the stomach acid and control the heartburn symptoms.""")

```
</div>

## Results

```bash
|    | chunks                      |   begin |   end | entities                  |
|---:|:----------------------------|--------:|------:|:--------------------------|
|  0 | feeling really tired        |      11 |    30 | Symptom                   |
|  1 | all the time                |      32 |    43 | Duration                  |
|  2 | losing weight               |      53 |    65 | Symptom                   |
|  3 | doctor                      |      91 |    96 | Employment                |
|  4 | sugar levels                |     109 |   120 | Test                      |
|  5 | high                        |     146 |   149 | TestResult                |
|  6 | type 2 diabetes             |     163 |   177 | Disease_Syndrome_Disorder |
|  7 | He                          |     181 |   182 | Gender                    |
|  8 | metformin                   |     219 |   227 | Drug                      |
|  9 | 500 mg                      |     229 |   234 | Strength                  |
| 10 | twice a day                 |     236 |   246 | Frequency                 |
| 11 | glipizide                   |     253 |   261 | Drug                      |
| 12 | 5 mg                        |     263 |   266 | Strength                  |
| 13 | before breakfast and dinner |     268 |   294 | Frequency                 |
| 14 | exercise                    |     340 |   347 | HealthStatus              |
| 15 | Now                         |     355 |   357 | DateTime                  |
| 16 | chronic acid reflux disease |     372 |   398 | Disease_Syndrome_Disorder |
| 17 | GERD                        |     403 |   406 | Disease_Syndrome_Disorder |
| 18 | Now                         |     409 |   411 | DateTime                  |
| 19 | daily                       |     422 |   426 | Frequency                 |
| 20 | pill                        |     428 |   431 | Drug                      |
| 21 | omeprazole                  |     440 |   449 | Drug                      |
| 22 | 20 mg                       |     451 |   455 | Strength                  |
| 23 | stomach acid                |     471 |   482 | Drug                      |
| 24 | heartburn symptoms          |     500 |   517 | Symptom                   |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_vop|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.8 GB|

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
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- GenericREModel