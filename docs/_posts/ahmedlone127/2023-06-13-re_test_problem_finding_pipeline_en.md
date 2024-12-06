---
layout: model
title: RE Pipeline between Problem, Test, and Findings in Reports
author: John Snow Labs
name: re_test_problem_finding_pipeline
date: 2023-06-13
tags: [licensed, clinical, relation_extraction, problem, test, findings, en]
task: Relation Extraction
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

This pretrained pipeline is built on the top of [re_test_problem_finding](https://nlp.johnsnowlabs.com/2021/04/19/re_test_problem_finding_en.html) model.

## Predicted Entities

`Admission_Discharge`, `Age`, `Alcohol`, `Allergen`, `BMI`, `Birth_Entity`, `Blood_Pressure`, `Cerebrovascular_Disease`, `Clinical_Dept`, `Communicable_Disease`, `Date`, `Death_Entity`, `Diabetes`, `Diet`, `Direction`, `Disease_Syndrome_Disorder`, `Dosage`, `Drug`, `Duration`, `EKG_Findings`, `Employment`, `External_body_part_or_region`, `Family_History_Header`, `Fetus_NewBorn`, `Form`, `Frequency`, `Gender`, `HDL`, `Heart_Disease`, `Height`, `Hyperlipidemia`, `Hypertension`, `ImagingFindings`, `Imaging_Technique`, `Injury_or_Poisoning`, `Internal_organ_or_component`, `Kidney_Disease`, `LDL`, `Labour_Delivery`, `Medical_Device`, `Medical_History_Header`, `Modifier`, `O2_Saturation`, `Obesity`, `Oncological`, `Overweight`, `Oxygen_Therapy`, `Pregnancy`, `Procedure`, `Psychological_Condition`, `Pulse`, `Race_Ethnicity`, `Relationship_Status`, `RelativeDate`, `RelativeTime`, `Respiration`, `Route`, `Section_Header`, `Sexually_Active_or_Sexual_Orientation`, `Smoking`, `Social_History_Header`, `Strength`, `Substance`, `Substance_Quantity`, `Symptom`, `Temperature`, `Test`, `Test_Result`, `Time`, `Total_Cholesterol`, `Treatment`, `Triglycerides`, `VS_Finding`, `Vaccine`, `Vital_Signs_Header`, `Weight`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_test_problem_finding_pipeline_en_4.4.4_3.0_1686651821511.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_test_problem_finding_pipeline_en_4.4.4_3.0_1686651821511.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("re_test_problem_finding_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("Targeted biopsy of this lesion for histological correlation should be considered.")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("re_test_problem_finding_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("Targeted biopsy of this lesion for histological correlation should be considered.")
```

{:.nlu-block}
```python
import nlu
nlu.load("en.relation.test_problem_finding.pipeline").predict("""Targeted biopsy of this lesion for histological correlation should be considered.""")
```
</div>

## Results

```bash
| index | relations    | entity1      | chunk1              | entity2      |  chunk2 |
|-------|--------------|--------------|---------------------|--------------|---------|
| 0     | 1            | PROCEDURE    | biopsy              | SYMPTOM      |  lesion | 
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_test_problem_finding_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 4.4.4+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.7 GB|

## Included Models

- DocumentAssembler
- SentenceDetector
- TokenizerModel
- PerceptronModel
- WordEmbeddingsModel
- MedicalNerModel
- NerConverter
- DependencyParserModel
- RelationExtractionModel