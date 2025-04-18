---
layout: model
title: RE Pipeline between Tests, Results, and Dates
author: John Snow Labs
name: re_test_result_date_pipeline
date: 2023-06-17
tags: [licensed, clinical, relation_extraction, tests, results, dates, en]
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

This pretrained pipeline is built on the top of [re_test_result_date](https://nlp.johnsnowlabs.com/2021/02/24/re_test_result_date_en.html) model.

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Route`, `Admission_Discharge`, `Death_Entity`, `Triglycerides`, `Oxygen_Therapy`, `Relationship_Status`, `Duration`, `Alcohol`, `Date`, `Drug`, `Hyperlipidemia`, `Respiration`, `Birth_Entity`, `VS_Finding`, `Age`, `Social_History_Header`, `Family_History_Header`, `Medical_Device`, `Labour_Delivery`, `BMI`, `Fetus_NewBorn`, `Temperature`, `Section_Header`, `Communicable_Disease`, `ImagingFindings`, `Psychological_Condition`, `Obesity`, `Sexually_Active_or_Sexual_Orientation`, `Modifier`, `Vaccine`, `Symptom`, `Pulse`, `Kidney_Disease`, `Oncological`, `EKG_Findings`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Blood_Pressure`, `Diabetes`, `O2_Saturation`, `Heart_Disease`, `Employment`, `Frequency`, `Disease_Syndrome_Disorder`, `Pregnancy`, `RelativeDate`, `Procedure`, `Overweight`, `Race_Ethnicity`, `Hypertension`, `External_body_part_or_region`, `Imaging_Technique`, `Test_Result`, `Treatment`, `Substance`, `Clinical_Dept`, `LDL`, `Diet`, `Substance_Quantity`, `Allergen`, `Gender`, `RelativeTime`, `Total_Cholesterol`, `Internal_organ_or_component`, `Smoking`, `Vital_Signs_Header`, `Height`, `Form`, `Strength`, `Weight`, `Time`, `Dosage`, `HDL`



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.0_1686989676790.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/re_test_result_date_pipeline_en_4.4.4_3.0_1686989676790.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("re_test_result_date_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("re_test_result_date_pipeline", "en", "clinical/models")

pipeline.fullAnnotate("He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%")
```


{:.nlu-block}
```python
import nlu
nlu.load("en.relation.date_test_result.pipeline").predict("""He was advised chest X-ray or CT scan after checking his SpO2 which was <= 93%""")
```

</div>



## Results

```bash
| index | relations    | entity1      | chunk1              | entity2      |  chunk2 |
|-------|--------------|--------------|---------------------|--------------|---------|
| 0     | O            | TEST         | chest X-ray         | MEASUREMENTS |  93%    | 
| 1     | O            | TEST         | CT scan             | MEASUREMENTS |  93%    |
| 2     | is_result_of | TEST         | SpO2                | MEASUREMENTS |  93%    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|re_test_result_date_pipeline|
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