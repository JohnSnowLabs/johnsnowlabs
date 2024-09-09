---
layout: model
title: Explain Clinical Document - Cancer Type
author: John Snow Labs
name: explain_clinical_doc_cancer_type
date: 2024-09-09
tags: [licensed, en, oncology, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized oncology pipeline can;

- extract oncological entities,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities from the clinical documents.

In this pipeline, three NER, one assertion and two relation extraction models were used to achieve those tasks.

- Clinical Entity Labels: `Age`, `Gender`, `Race_Ethnicity`, `Oncological`, `Weight`, `Alcohol`, `Communicable_Disease`, `BMI`, `Obesity`, `Diabetes`, `Test`, `Date`,
                          `VS_Finding`, `ImagingFindings`, `Modifier`, `Symptom`, `Disease_Syndrome_Disorder`, `RelativeDate`, `Procedure`, `External_body_part_or_region`,
                          `Imaging_Technique`, `Test_Result`, `Treatment`, `Internal_organ_or_component`, `Cycle_Number`, `Direction`, `Histological_Type`,
                          `Site_Other_Body_Part`, `Hormonal_Therapy`, `Death_Entity`, `Targeted_Therapy`, `Route`, `Tumor_Finding`, `Duration`, `Pathology_Result`,
                          `Chemotherapy`, `Radiotherapy`, `Radiation_Dose`, `Oncogene`, `Cancer_Surgery`, `Tumor_Size`, `Staging`, `Pathology_Test`, `Cancer_Dx`,
                          `Site_Lung`, `Site_Breast`, `Site_Liver`, `Site_Lymph_Node`, `Response_To_Treatment`, `Site_Brain`, `Immunotherapy`, `Race_Ethnicity`,
                          `Metastasis`, `Smoking_Status`, `Imaging_Test`, `Relative_Date`, `Line_Of_Therapy`, `Unspecific_Therapy`, `Site_Bone`, `Cycle_Count`,
                          `Cancer_Score`, `Adenopathy`, `Grade`, `Biomarker`, `Invasion`, `Frequency`, `Performance_Status`, `Dosage`, `Cycle_Day`, `Carcinoma_Type`,
                          `CNS_Tumor_Type`, `Melanoma`, `Biomarker_Result`, `Biomarker_Quant`, `Lymphoma_Type`, `Sarcoma_Type`, `Body_Site`, `Leukemia_Type`

- Assertion Status Labels: `Present`, `Absent`, `Possible`, `Past`, `Family`, `Hypotetical`

- Relation Extraction Labels: `is_size_of`, `is_finding_of`, `is_date_of`

## Predicted Entities

`Age`, `Gender`, `Race_Ethnicity`, `Oncological`, `Weight`, `Alcohol`, `Communicable_Disease`, `BMI`, `Obesity`, `Diabetes`, `Test`, `Date`, `VS_Finding`, `ImagingFindings`, `Modifier`, `Symptom`, `Disease_Syndrome_Disorder`, `RelativeDate`, `Procedure`, `External_body_part_or_region`, `Imaging_Technique`, `Test_Result`, `Treatment`, `Internal_organ_or_component`, `Cycle_Number`, `Direction`, `Histological_Type`, `Site_Other_Body_Part`, `Hormonal_Therapy`, `Death_Entity`, `Targeted_Therapy`, `Route`, `Tumor_Finding`, `Duration`, `Pathology_Result`, `Chemotherapy`, `Radiotherapy`, `Radiation_Dose`, `Oncogene`, `Cancer_Surgery`, `Tumor_Size`, `Staging`, `Pathology_Test`, `Cancer_Dx`, `Site_Lung`, `Site_Breast`, `Site_Liver`, `Site_Lymph_Node`, `Response_To_Treatment`, `Site_Brain`, `Immunotherapy`, `Race_Ethnicity`, `Metastasis`, `Smoking_Status`, `Imaging_Test`, `Relative_Date`, `Line_Of_Therapy`, `Unspecific_Therapy`, `Site_Bone`, `Cycle_Count`, `Cancer_Score`, `Adenopathy`, `Grade`, `Biomarker`, `Invasion`, `Frequency`, `Performance_Status`, `Dosage`, `Cycle_Day`, `Carcinoma_Type`, `CNS_Tumor_Type`, `Melanoma`, `Biomarker_Result`, `Biomarker_Quant`, `Lymphoma_Type`, `Sarcoma_Type`, `Body_Site`, `Leukemia_Type`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_cancer_type_en_5.4.1_3.4_1725903881471.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_cancer_type_en_5.4.1_3.4_1725903881471.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_cancer_type", "en", "clinical/models")

result = ner_pipeline.fullAnnotate("""The patient underwent a magnetic resonance imaging (MRI) of the brain, which revealed a 3 cm lesion in the right temporal lobe.
A biopsy performed two weeks later confirmed the presence of glioblastoma multiforme. The pathological analysis demonstrated infiltration of the tumor into surrounding brain tissue,
with evidence of vascular proliferation and necrosis. The final diagnosis was grade IV glioblastoma. Six months later, the patient developed spinal metastases.
Concurrent chemoradiotherapy with Temozolomide (150 mg/m²) was administered over 6 cycles, with minimal improvement in tumor size.""")
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_cancer_type", "en", "clinical/models")

val result = ner_pipeline.fullAnnotate("""The patient underwent a magnetic resonance imaging (MRI) of the brain, which revealed a 3 cm lesion in the right temporal lobe.
A biopsy performed two weeks later confirmed the presence of glioblastoma multiforme. The pathological analysis demonstrated infiltration of the tumor into surrounding brain tissue,
with evidence of vascular proliferation and necrosis. The final diagnosis was grade IV glioblastoma. Six months later, the patient developed spinal metastases.
Concurrent chemoradiotherapy with Temozolomide (150 mg/m²) was administered over 6 cycles, with minimal improvement in tumor size.""")
```
</div>

## Results

```bash

# NER JSL Result

|    |   sentence_id | chunks                     |   begin |   end | entities                    |
|---:|--------------:|:---------------------------|--------:|------:|:----------------------------|
|  0 |             0 | magnetic resonance imaging |      24 |    49 | Test                        |
|  1 |             0 | MRI                        |      52 |    54 | Test                        |
|  2 |             0 | brain                      |      64 |    68 | Internal_organ_or_component |
|  3 |             0 | lesion                     |      93 |    98 | Symptom                     |
|  4 |             0 | temporal lobe              |     113 |   125 | Internal_organ_or_component |
|  5 |             1 | biopsy                     |     131 |   136 | Procedure                   |
|  6 |             1 | two weeks later            |     148 |   162 | RelativeDate                |
|  7 |             1 | glioblastoma multiforme    |     190 |   212 | Oncological                 |
|  8 |             2 | pathological analysis      |     219 |   239 | Test                        |
|  9 |             2 | infiltration               |     254 |   265 | Symptom                     |
| 10 |             2 | tumor                      |     274 |   278 | Oncological                 |
| 11 |             2 | brain tissue               |     297 |   308 | Internal_organ_or_component |
| 12 |             2 | vascular proliferation     |     329 |   350 | Symptom                     |
| 13 |             2 | necrosis                   |     356 |   363 | Disease_Syndrome_Disorder   |
| 14 |             3 | grade IV                   |     390 |   397 | Modifier                    |
| 15 |             3 | glioblastoma               |     399 |   410 | Oncological                 |
| 16 |             4 | Six months later           |     413 |   428 | RelativeDate                |
| 17 |             4 | spinal metastases          |     453 |   469 | Oncological                 |
| 18 |             5 | chemoradiotherapy          |     484 |   500 | Treatment                   |
| 19 |             5 | tumor                      |     592 |   596 | Oncological                 |

# NER Oncology Result

|    |   sentence_id | chunks                  |   begin |   end | entities       |
|---:|--------------:|:------------------------|--------:|------:|:---------------|
|  0 |             0 | brain                   |      64 |    68 | Body_Site      |
|  1 |             0 | temporal lobe           |     113 |   125 | Body_Site      |
|  2 |             1 | glioblastoma multiforme |     190 |   212 | CNS_Tumor_Type |
|  3 |             2 | brain                   |     297 |   301 | Body_Site      |
|  4 |             3 | glioblastoma            |     399 |   410 | CNS_Tumor_Type |
|  5 |             4 | spinal                  |     453 |   458 | Body_Site      |
|  6 |             4 | metastases              |     460 |   469 | Metastasis     |

# NER Cancer Types Result

|    |   sentence_id | chunks                              |   begin |   end | entities              |
|---:|--------------:|:------------------------------------|--------:|------:|:----------------------|
|  0 |             0 | magnetic resonance imaging          |      24 |    49 | Imaging_Test          |
|  1 |             0 | MRI                                 |      52 |    54 | Imaging_Test          |
|  2 |             0 | brain                               |      64 |    68 | Site_Brain            |
|  3 |             0 | 3 cm                                |      88 |    91 | Tumor_Size            |
|  4 |             0 | lesion                              |      93 |    98 | Tumor_Finding         |
|  5 |             0 | right                               |     107 |   111 | Direction             |
|  6 |             0 | temporal lobe                       |     113 |   125 | Site_Brain            |
|  7 |             1 | biopsy                              |     131 |   136 | Pathology_Test        |
|  8 |             1 | two weeks later                     |     148 |   162 | Relative_Date         |
|  9 |             1 | glioblastoma multiforme             |     190 |   212 | Cancer_Dx             |
| 10 |             2 | pathological analysis               |     219 |   239 | Pathology_Test        |
| 11 |             2 | infiltration                        |     254 |   265 | Invasion              |
| 12 |             2 | tumor                               |     274 |   278 | Tumor_Finding         |
| 13 |             2 | brain tissue                        |     297 |   308 | Site_Brain            |
| 14 |             2 | vascular proliferation and necrosis |     329 |   363 | Pathology_Result      |
| 15 |             3 | grade IV                            |     390 |   397 | Grade                 |
| 16 |             3 | glioblastoma                        |     399 |   410 | Cancer_Dx             |
| 17 |             4 | Six months later                    |     413 |   428 | Relative_Date         |
| 18 |             4 | spinal                              |     453 |   458 | Site_Bone             |
| 19 |             4 | metastases                          |     460 |   469 | Metastasis            |
| 20 |             5 | chemoradiotherapy                   |     484 |   500 | Unspecific_Therapy    |
| 21 |             5 | Temozolomide                        |     507 |   518 | Chemotherapy          |
| 22 |             5 | 150 mg/m²                           |     521 |   529 | Dosage                |
| 23 |             5 | 6 cycles                            |     554 |   561 | Cycle_Count           |
| 24 |             5 | minimal improvement                 |     569 |   587 | Response_To_Treatment |
| 25 |             5 | tumor                               |     592 |   596 | Tumor_Finding         |

# Assertion Result

|    |   sentence_id | chunks                     |   begin |   end | entities                    | assertion   |
|---:|--------------:|:---------------------------|--------:|------:|:----------------------------|:------------|
|  0 |             0 | magnetic resonance imaging |      24 |    49 | Test                        | Past        |
|  1 |             0 | MRI                        |      52 |    54 | Test                        | Past        |
|  2 |             0 | brain                      |      64 |    68 | Internal_organ_or_component | Present     |
|  3 |             0 | lesion                     |      93 |    98 | Symptom                     | Past        |
|  4 |             0 | temporal lobe              |     113 |   125 | Internal_organ_or_component | Present     |
|  5 |             1 | biopsy                     |     131 |   136 | Procedure                   | Past        |
|  6 |             1 | two weeks later            |     148 |   162 | RelativeDate                | Present     |
|  7 |             1 | glioblastoma multiforme    |     190 |   212 | Oncological                 | Present     |
|  8 |             2 | pathological analysis      |     219 |   239 | Test                        | Present     |
|  9 |             2 | infiltration               |     254 |   265 | Symptom                     | Present     |
| 10 |             2 | tumor                      |     274 |   278 | Oncological                 | Present     |
| 11 |             2 | brain tissue               |     297 |   308 | Internal_organ_or_component | Present     |
| 12 |             2 | vascular proliferation     |     329 |   350 | Symptom                     | Past        |
| 13 |             2 | necrosis                   |     356 |   363 | Disease_Syndrome_Disorder   | Present     |


# Relation Extraction Result

|    |   sentence |   entity1_begin |   entity1_end | chunk1                 | entity1                     |   entity2_begin |   entity2_end | chunk2                  | entity2                     | relation                                |   confidence |
|---:|-----------:|----------------:|--------------:|:-----------------------|:----------------------------|----------------:|--------------:|:------------------------|:----------------------------|:----------------------------------------|-------------:|
|  0 |          1 |             131 |           136 | biopsy                 | Procedure                   |             148 |           162 | two weeks later         | RelativeDate                | is_date_of                              |     1        |
|  1 |          1 |             148 |           162 | two weeks later        | RelativeDate                |             190 |           212 | glioblastoma multiforme | Oncological                 | is_date_of                              |     0.968502 |
|  2 |          2 |             219 |           239 | pathological analysis  | Test                        |             274 |           278 | tumor                   | Oncological                 | is_finding_of                           |     0.998728 |
|  3 |          2 |             219 |           239 | pathological analysis  | Test                        |             356 |           363 | necrosis                | Disease_Syndrome_Disorder   | is_finding_of                           |     0.999999 |
|  5 |          0 |              64 |            68 | brain                  | Internal_organ_or_component |              93 |            98 | lesion                  | Symptom                     | Internal_organ_or_component-Symptom     |     1        |
|  6 |          0 |              93 |            98 | lesion                 | Symptom                     |             113 |           125 | temporal lobe           | Internal_organ_or_component | Symptom-Internal_organ_or_component     |     1        |
|  7 |          2 |             254 |           265 | infiltration           | Symptom                     |             297 |           308 | brain tissue            | Internal_organ_or_component | Symptom-Internal_organ_or_component     |     1        |
|  8 |          2 |             254 |           265 | infiltration           | Symptom                     |             356 |           363 | necrosis                | Disease_Syndrome_Disorder   | Symptom-Disease_Syndrome_Disorder       |     1        |
|  9 |          2 |             274 |           278 | tumor                  | Oncological                 |             297 |           308 | brain tissue            | Internal_organ_or_component | Oncological-Internal_organ_or_component |     1        |
| 10 |          2 |             329 |           350 | vascular proliferation | Symptom                     |             356 |           363 | necrosis                | Disease_Syndrome_Disorder   | Symptom-Disease_Syndrome_Disorder       |     1        |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_cancer_type|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.4.1+|
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
- NerConverterInternalModel
- NerConverterInternalModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- GenericREModel
- AnnotationMerger
