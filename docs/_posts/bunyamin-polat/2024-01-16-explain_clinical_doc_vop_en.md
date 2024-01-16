---
layout: model
title: Explain Clinical Document - Voice Of Patient (VOP)
author: John Snow Labs
name: explain_clinical_doc_vop
date: 2024-01-16
tags: [licensed, clinical, en, vop, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pipeline is designed to:

- extract healthcare-related entities
- designate assertion status for the identified entities
- establish connections between the recognized entities

These actions are performed on documents obtained from patient sentences. To accomplish these tasks, a set of six Named Entity Recognition (NER) models, one assertion model, and one relation extraction model are employed.

- Clinical Entity Labels: `Gender`, `Employment`, `Age`, `BodyPart`, `Substance`, `Form`, `PsychologicalCondition`, `Vaccine`, `Drug`, `DateTime`, `ClinicalDept`, `Laterality`, `Test`, `AdmissionDischarge`, `Disease_Syndrome_Disorder`, `VitalTest`, `Dosage`, `Duration`, `RelationshipStatus`, `Route`, `Allergen`, `Frequency`, `Symptom`, `Procedure`, `HealthStatus`, `InjuryOrPoisoning`, `Modifier`, `Treatment`, `SubstanceQuantity`, `MedicalDevice`, `TestResult`, `Alcohol`, `Smoking`

- Assertion Status Labels: `Present_Or_Past`, `Hypothetical_Or_Absent`, `SomeoneElse`

- Relation Extraction Labels: `Drug-Dosage`, `Drug-Frequency`, `Drug-Duration`, `Drug-Strength`, `Drug-Drug`, `Test-TestResult`, `Disease_Syndrome_Disorder-Treatment`, `Disease_Syndrome_Disorder-Symptom`, `Disease_Syndrome_Disorder-Modifier`, `Symptom-Modifier`, `Disease_Syndrome_Disorder-BodyPart`, `Symptom-BodyPart`,  `Procedure-DateTime`, `Test-DateTime`, `VitalTest-TestResult`,  `Disease_Syndrome_Disorder-Drug`, `Treatment-Drug`, `Disease_Syndrome_Disorder-Procedure`, `Procedure-Drug`, `Procedure-BodyPart`, `Treatment-BodyPart`, `BodyPart-Procedure`, `MedicalDevice-Procedure`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_en_5.2.1_3.0_1705433668760.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_vop_en_5.2.1_3.0_1705433668760.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
#NER and Assertion Status Results

|    | chunks                      | entities                  | assertion              |
|---:|-----------------------------|---------------------------|------------------------|
|  0 | feeling really tired        | Symptom                   | Present_Or_Past        |
|  1 | losing weight               | Symptom                   | Present_Or_Past        |
|  2 | sugar levels                | Test                      | Present_Or_Past        |
|  3 | high                        | TestResult                | Present_Or_Past        |
|  4 | type 2 diabetes             | Disease_Syndrome_Disorder | Present_Or_Past        |
|  5 | metformin                   | Drug                      | Present_Or_Past        |
|  6 | glipizide                   | Drug                      | Present_Or_Past        |
|  7 | exercise                    | HealthStatus              | Hypothetical_Or_Absent |
|  8 | chronic acid reflux disease | Disease_Syndrome_Disorder | Present_Or_Past        |
|  9 | GERD                        | Disease_Syndrome_Disorder | Present_Or_Past        |
| 10 | pill                        | Drug                      | Present_Or_Past        |
| 11 | omeprazole                  | Drug                      | Present_Or_Past        |
| 12 | stomach acid                | Drug                      | Present_Or_Past        |
| 13 | heartburn symptoms          | Symptom                   | Present_Or_Past        |

# Relation Extraction Results
|    | sentence | entity1_begin | entity1_end | chunk1       | entity1   | entity2_begin | entity2_end | chunk2                      | entity2    | relation        | confidence |
|---:|----------|---------------|-------------|--------------|-----------|---------------|-------------|-----------------------------|------------|-----------------|------------|
|  0 |     1    |      109      |     120     | sugar levels | Test      |      146      |     149     | high                        | TestResult | Test-TestResult |     1.0    |
|  1 |     3    |      219      |     227     | metformin    | Drug      |      229      |     234     | 500 mg                      | Strength   | Drug-Strength   |     1.0    |
|  2 |     3    |      219      |     227     | metformin    | Drug      |      236      |     246     | twice a day                 | Frequency  | Drug-Frequency  |     1.0    |
|  3 |     3    |      219      |     227     | metformin    | Drug      |      253      |     261     | glipizide                   | Drug       | Drug-Drug       |     1.0    |
|  4 |     3    |      219      |     227     | metformin    | Drug      |      263      |     266     | 5 mg                        | Strength   | Drug-Strength   |     1.0    |
|  5 |     3    |      229      |     234     | 500 mg       | Strength  |      253      |     261     | glipizide                   | Drug       | Strength-Drug   |     1.0    |
|  6 |     3    |      253      |     261     | glipizide    | Drug      |      263      |     266     | 5 mg                        | Strength   | Drug-Strength   |     1.0    |
|  7 |     3    |      253      |     261     | glipizide    | Drug      |      268      |     294     | before breakfast and dinner | Frequency  | Drug-Frequency  |     1.0    |
|  8 |     6    |      422      |     426     | daily        | Frequency |      428      |     431     | pill                        | Drug       | Frequency-Drug  |     1.0    |
|  9 |     6    |      422      |     426     | daily        | Frequency |      440      |     449     | omeprazole                  | Drug       | Frequency-Drug  |     1.0    |
| 10 |     6    |      428      |     431     | pill         | Drug      |      440      |     449     | omeprazole                  | Drug       | Drug-Drug       |     1.0    |
| 11 |     6    |      428      |     431     | pill         | Drug      |      451      |     455     | 20 mg                       | Strength   | Drug-Strength   |     1.0    |
| 12 |     6    |      440      |     449     | omeprazole   | Drug      |      451      |     455     | 20 mg                       | Strength   | Drug-Strength   |     1.0    |
| 13 |     6    |      440      |     449     | omeprazole   | Drug      |      471      |     482     | stomach acid                | Drug       | Drug-Drug       |     1.0    |
| 14 |     6    |      451      |     455     | 20 mg        | Strength  |      471      |     482     | stomach acid                | Drug       | Strength-Drug   |     1.0    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_vop|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
