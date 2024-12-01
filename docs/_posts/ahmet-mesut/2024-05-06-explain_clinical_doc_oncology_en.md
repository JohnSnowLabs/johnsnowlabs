---
layout: model
title: Explain Clinical Document - Oncology
author: John Snow Labs
name: explain_clinical_doc_oncology
date: 2024-05-06
tags: [licensed, en, oncology, pipeline, ner, assertion, relation_extraction]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.2
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

In this pipeline, seven NER, one assertion and two relation extraction model were used to achieve those tasks.

- Clinical Entity Labels: `Adenopathy`, `Age`, `Biomarker`,`Biomarker_Result`, `Cancer_Dx`, `Cancer_Score` ,`Cancer_Surgery`, `Chemotherapy`, `Cycle_Count` ,`Cycle_Day`, `Cycle_Number`, `Date` ,`Death_Entity`, `Direction`, `Dosage` ,`Duration`, `Frequency`, `Gender` ,`Grade`, `Histological_Type`, `Hormonal_Therapy` ,`Imaging_Test`, `Immunotherapy`, `Invasion` ,`Line_Of_Therapy`, `Metastasis`, `Oncogene` ,`PROBLEM`, `Pathology_Result`, `Pathology_Test` ,`PROBLEM`, `Performance_Status`, `Race_Ethnicity` ,`Radiotherapy`, `Response_To_Treatment`, `Relative_Date` ,`Route`, `Site_Bone`, `Site_Brain` ,`Site_Breast`, `Site_Liver`, `Site_Lung` ,`Site_Lymph_Node`, `Site_Other_Body_Part`, `Smoking_Status` ,`Staging`, `Targeted_Therapy`, `Tumor_Finding` ,`Tumor_Size`, `Unspecific_Therapy`, `Radiation_Dose` ,`Anatomical_Site`, `Cancer_Therapy`, `Size_Trend` ,`Lymph_Node`, `Tumor_Description`,`Lymph_Node_Modifier`, `Posology_Information`, `Oncological`,`Weight`,`Alcohol`,`Communicable_Disease`,`BMI`,`Obesity`,`Diabetes`

- Assertion Status Labels: `Present`, `Absent`, `Possible`, `Past`, `Family`, `Hypotetical`

- Relation Extraction Labels: `is_size_of`, `is_finding_of`, `is_date_of`, `is_location_of`,
`Chemotherapy-Dosage`,`Chemotherapy-Cycle_Count`,`Chemotherapy-Cycle_Day`,`Chemotherapy-Cycle_Number`, `Chemotherapy-Route`,
`Cancer_Therapy-Dosage`, `Cancer_Therapy-Duration`, `Cancer_Therapy-Frequency`,`Cancer_Therapy-Route`,
`Hormonal_Therapy-Dosage`, `Hormonal_Therapy-Duration`, `Hormonal_Therapy-Frequency`, `Hormonal_Therapy-Route`,
`Immunotherapy-Dosage`, `Immunotherapy-Duration`, `Immunotherapy-Frequency`, `Immunotherapy-Route`,
`Radiotherapy-Radiation_Dose`, `Radiotherapy-Duration`, `Radiotherapy-Frequency`,
`Posology_Information-Dosage`, `Posology_Information-Duration`, `Posology_Information-Frequency`, `Posology_Information-Route`,
`Unspecific_Therapy-Dosage`, `Unspecific_Therapy-Duration`, `Unspecific_Therapy-Frequency`, `Unspecific_Therapy-Route`

## Predicted Entities

`Adenopathy`, `Age`, `Alcohol`, `Anatomical_Site`, `BMI`, `Biomarker`, `Biomarker_Measurement`, `Biomarker_Quant`, `Biomarker_Result`, `Body_Site`, `CNS_Tumor_Type`, `CancerModifier`, `Cancer_Dx`, `Cancer_Score`, `Cancer_Surgery`, `Cancer_Therapy`, `Cancer_dx`, `Cancer_dx"`, `Carcinoma_Type`, `Chemotherapy`, `Communicable_Disease`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Date`, `Death_Entity`, `Diabetes`, `Direction`, `Dosage`, `Duration`, `Frequency`, `Gender`, `Grade`, `Histological_Type`, `Hormonal_Therapy`, `Imaging_Test`, `Immunotherapy`, `Invasion`, `Leukemia_Type`, `Line_Of_Therapy`, `Lymph_Node`, `Lymph_Node_Modifier`, `Lymphoma_Type`, `Melanoma`, `Metastasis`, `Obesity`, `Oncogene`, `Oncological`, `Overweight`, `Pathology_Result`, `Pathology_Test`, `Performance_Status`, `Posology_Information`, `Predictive_Biomarkers`, `Prognostic_Biomarkers`, `Race_Ethnicity`, `Radiation_Dose`, `Radiotherapy`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Sarcoma_Type`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part`, `Size_Trend`, `Smoking_Status`, `Staging`, `Targeted_Therapy`, `Tumor_Description`, `Tumor_Finding`, `Tumor_Size`, `Unspecific_Therapy`, `Weight`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_en_5.2.1_3.2_1715031815850.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_en_5.2.1_3.2_1715031815850.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("explain_clinical_doc_oncology", "en", "clinical/models")

result = ner_pipeline.annotate("""The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. Two months later, the patient was diagnosed with lung metastases.Neoadjuvant chemotherapy with the regimens of Cyclophosphamide (500 mg/m2) is being given for 6 cycles with poor response""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_pipeline = PretrainedPipeline("explain_clinical_doc_oncology", "en", "clinical/models")

val result = ner_pipeline.annotate("""The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. Two months later, the patient was diagnosed with lung metastases.Neoadjuvant chemotherapy with the regimens of Cyclophosphamide (500 mg/m2) is being given for 6 cycles with poor response""")

```
</div>

## Results

```bash

# NER Result

|    |   sentence_id | chunks                                  |   begin |   end | entities              |
|---:|--------------:|:----------------------------------------|--------:|------:|:----------------------|
|  0 |             0 | computed tomography                     |      24 |    42 | Imaging_Test          |
|  1 |             0 | CT                                      |      45 |    46 | Imaging_Test          |
|  2 |             0 | abdomen                                 |      61 |    67 | Site_Other_Body_Part  |
|  3 |             0 | pelvis                                  |      73 |    78 | Site_Other_Body_Part  |
|  4 |             0 | ovarian                                 |     104 |   110 | Site_Other_Body_Part  |
|  5 |             0 | mass                                    |     112 |   115 | Tumor_Finding         |
|  6 |             1 | Pap smear                               |     120 |   128 | Pathology_Test        |
|  7 |             1 | one month later                         |     140 |   154 | Relative_Date         |
|  8 |             1 | atypical glandular cells                |     173 |   196 | Pathology_Result      |
|  9 |             1 | adenocarcinoma                          |     213 |   226 | Cancer_Dx             |
| 10 |             2 | pathologic specimen                     |     233 |   251 | Pathology_Test        |
| 11 |             2 | extension                               |     260 |   268 | Invasion              |
| 12 |             2 | tumor                                   |     277 |   281 | Tumor_Finding         |
| 13 |             2 | fallopian tubes                         |     298 |   312 | Site_Other_Body_Part  |
| 14 |             2 | appendix                                |     315 |   322 | Site_Other_Body_Part  |
| 15 |             2 | omentum                                 |     325 |   331 | Site_Other_Body_Part  |
| 16 |             2 | enlarged                                |     349 |   356 | Lymph_Node_Modifier   |
| 17 |             2 | lymph nodes                             |     358 |   368 | Site_Lymph_Node       |
| 18 |             3 | tumor                                   |     409 |   413 | Tumor_Finding         |
| 19 |             3 | stage IIIC                              |     419 |   428 | Staging               |
| 20 |             3 | papillary serous ovarian adenocarcinoma |     430 |   468 | Oncological           |
| 21 |             4 | Two months later                        |     471 |   486 | Relative_Date         |
| 22 |             4 | lung metastases                         |     520 |   534 | Oncological           |
| 23 |             5 | Neoadjuvant chemotherapy                |     536 |   559 | Chemotherapy          |
| 24 |             5 | Cyclophosphamide                        |     582 |   597 | Chemotherapy          |
| 25 |             5 | 500 mg/m2                               |     600 |   608 | Dosage                |
| 26 |             5 | 6 cycles                                |     630 |   637 | Cycle_Count           |
| 27 |             5 | poor response                           |     644 |   656 | Response_To_Treatment |

# Assertion Result

|    |   sentence_id | chunks                                  |   begin |   end | entities            | assertion   |
|---:|--------------:|:----------------------------------------|--------:|------:|:--------------------|:------------|
|  0 |             0 | computed tomography                     |      24 |    42 | Imaging_Test        | Past        |
|  1 |             0 | CT                                      |      45 |    46 | Imaging_Test        | Past        |
|  2 |             0 | mass                                    |     112 |   115 | Tumor_Finding       | Present     |
|  3 |             1 | Pap smear                               |     120 |   128 | Pathology_Test      | Past        |
|  4 |             1 | atypical glandular cells                |     173 |   196 | Pathology_Result    | Present     |
|  5 |             1 | adenocarcinoma                          |     213 |   226 | Cancer_Dx           | Possible    |
|  6 |             2 | pathologic specimen                     |     233 |   251 | Pathology_Test      | Past        |
|  7 |             2 | extension                               |     260 |   268 | Invasion            | Present     |
|  8 |             2 | tumor                                   |     277 |   281 | Tumor_Finding       | Present     |
|  9 |             2 | enlarged                                |     349 |   356 | Lymph_Node_Modifier | Present     |
| 10 |             3 | tumor                                   |     409 |   413 | Tumor_Finding       | Present     |
| 11 |             3 | papillary serous ovarian adenocarcinoma |     430 |   468 | Oncological         | Present     |
| 12 |             4 | lung metastases                         |     520 |   534 | Oncological         | Present     |
| 13 |             5 | Neoadjuvant chemotherapy                |     536 |   559 | Chemotherapy        | Present     |
| 14 |             5 | Cyclophosphamide                        |     582 |   597 | Chemotherapy        | Present     |
| 15 |             5 | 6 cycles                                |     630 |   637 | Cycle_Count         | Present     |


# Relation Extraction Result

|    |   sentence |   entity1_begin |   entity1_end | chunk1                   | entity1              |   entity2_begin |   entity2_end | chunk2          | entity2              | relation                 |
|---:|-----------:|----------------:|--------------:|:-------------------------|:---------------------|----------------:|--------------:|:----------------|:---------------------|:-------------------------|
|  2 |          0 |             104 |           110 | ovarian                  | Site_Other_Body_Part |             112 |           115 | mass            | Tumor_Finding        | is_location_of           |
|  3 |          1 |             120 |           128 | Pap smear                | Pathology_Test       |             213 |           226 | adenocarcinoma  | Cancer_Dx            | is_finding_of            |
|  4 |          2 |             277 |           281 | tumor                    | Tumor_Finding        |             298 |           312 | fallopian tubes | Site_Other_Body_Part | is_location_of           |
|  5 |          2 |             277 |           281 | tumor                    | Tumor_Finding        |             315 |           322 | appendix        | Site_Other_Body_Part | is_location_of           |
|  7 |          5 |             536 |           559 | Neoadjuvant chemotherapy | Chemotherapy         |             600 |           608 | 500 mg/m2       | Dosage               | Chemotherapy-Dosage      |
|  8 |          5 |             536 |           559 | Neoadjuvant chemotherapy | Chemotherapy         |             630 |           637 | 6 cycles        | Cycle_Count          | Chemotherapy-Cycle_Count |
|  9 |          5 |             582 |           597 | Cyclophosphamide         | Chemotherapy         |             600 |           608 | 500 mg/m2       | Dosage               | Chemotherapy-Dosage      |
| 10 |          5 |             582 |           597 | Cyclophosphamide         | Chemotherapy         |             630 |           637 | 6 cycles        | Cycle_Count          | Chemotherapy-Cycle_Count |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_oncology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.2.1+|
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
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- PosologyREModel
- AnnotationMerger
