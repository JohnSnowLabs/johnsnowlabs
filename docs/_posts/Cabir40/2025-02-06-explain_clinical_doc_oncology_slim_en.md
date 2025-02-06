---
layout: model
title: Explain Clinical Document - Cancer Type (Slim)
author: John Snow Labs
name: explain_clinical_doc_oncology_slim
date: 2025-02-06
tags: [licensed, en, oncology, pipeline, ner, assertion, relation_extraction, cancer_type, cancer]
task: [Named Entity Recognition, Assertion Status, Relation Extraction, Pipeline Healthcare]
language: en
edition: Healthcare NLP 5.5.2
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This specialized oncology pipeline can;

- extract oncological and cancer type entities,

- assign assertion status to the extracted entities,

- establish relations between the extracted entities from the clinical documents.

In this pipeline, [ner_oncology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_en.html), [ner_oncology_biomarker_docwise](https://nlp.johnsnowlabs.com/2025/01/15/ner_oncology_biomarker_docwise_en.html) and [ner_cancer_types_wip](https://nlp.johnsnowlabs.com/2024/08/16/ner_cancer_types_wip_en.html)
NER models, [assertion_oncology](https://nlp.johnsnowlabs.com/2024/07/03/assertion_oncology_en.html) assertion model and [re_oncology_granular](https://nlp.johnsnowlabs.com/2024/07/03/re_oncology_granular_en.html)
and [posology_re](https://nlp.johnsnowlabs.com/2020/09/01/posology_re.html)  relation extraction models were used to achieve those tasks.

- Clinical Entity Labels: `Adenopathy`, `Age`, `Biomarker`, `Biomarker_Result`, `Cancer_Dx`, `Cancer_Score`, `Cancer_Surgery`,
                          `Chemotherapy`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Date`, `Death_Entity`, `Direction`, `Dosage`,
                          `Duration`, `Frequency`, `Gender`, `Grade`, `Histological_Type`, `Hormonal_Therapy`, `Imaging_Test`,
                          `Immunotherapy`, `Invasion`, `Line_Of_Therapy`, `Metastasis`,`Oncogene`, `Pathology_Result`, `Pathology_Test`,
                          `Performance_Status`, `Race_Ethnicity`, `Radiation_Dose`, `Radiotherapy`, `Relative_Date`, `Response_To_Treatment`,
                          `Route`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part`,
                          `Smoking_Status`, `Staging`, `Targeted_Therapy`, `Tumor_Finding`, `Tumor_Size`, `Unspecific_Therapy`,`Biomarker_Quant`,
                          `Body_Site`, `CNS_Tumor_Type`, `Carcinoma_Type`, `Leukemia_Type`, `Lymphoma_Type`, `Melanoma`,`Sarcoma_Type`

- Assertion Status Labels: `Present`, `Absent`, `Possible`, `Past`, `Family`, `Hypotetical`

- Relation Extraction Labels: `is_size_of`, `is_finding_of`, `is_date_of`, `Date-Cancer_Dx`, `Tumor_Finding-Site_Breast`, `Tumor_Finding-Site_Bone`,
                              `Tumor_Finding-Site_Liver`, `Tumor_Finding-Site_Lung`, `Tumor_Finding-Site_Lymph_Node`, `Tumor_Finding-Site_Other_Body_Part`,
                              `Tumor_Fiding-Relative_Date`, `Tumor_Finding-Tumor_Size`, `Pathology_Test-Cancer_Dx`, `Pathology_Test-Pathology_Result`,
                              `Biomarker_Result-Biomarker`, `Biomarker-Biomarker_Quant`, `Cancer_Dx-Hormonal_Therapy`, `Cancer_Dx-Immunotherapy`,
                              `Cancer_Dx-Radiotherapy`, `Cancer_Dx-Chemotherapy`, `Cancer_Dx-Targeted_Therapy`, `Cancer_Dx-Cancer_Surgery`,
                              `Cancer_Dx-Unspecific_Therapy`, `Cancer_Dx-Invasion`, `Cancer_Dx-Site_Bone`, `Cancer_Dx-Site_Brain`, `Cancer_Dx-Site_Breast`,
                              `Cancer_Dx-Site_Liver`, `Cancer_Dx-Site_Lymph_Node`, `Cancer_Dx-Site_Other_Body_Part`, `Cancer_Dx-Imaging_Test`, `Invasion-Site_Bone`,
                              `Invasion-Site_Brain`, `Invasion-Site_Breast`, `Invasion-Site_Liver`, `Invasion-Site_Lymph_Node`, `Invasion-Site_Other_Body_Part`,
                              `Invasion-Metastasis`, `Invasion-Cancer_Surgery`, `Response_To_Treatment-Chemotherapy`, `Response_To_Treatment-Hormonal_Therapy`,
                              `Response_To_Treatment-Immunotherapy`, `Response_To_Treatment-Radiotherapy`, `Response_To_Treatment-Targeted_Therapy`,
                              `Response_To_Treatment-Unspecific_Therapy`, `Response_To_Treatment-Line_Of_Therapy`, `Chemotherapy-Dosage`, `Chemotherapy-Cycle_Count`,
                              `Chemotherapy-Cycle_Day`, `Chemotherapy-Cycle_Number`, `Cancer_Therapy-Dosage`, `Cancer_Therapy-Duration`, `Cancer_Therapy-Frequency`,
                              `Hormonal_Therapy-Dosage`, `Hormonal_Therapy-Duration`, `Hormonal_Therapy-Frequency`, `Immunotherapy-Dosage`, `Immunotherapy-Duration`,
                              `Immunotherapy-Frequency`, `Radiotherapy-Radiation_Dose`, `Radiotherapy-Duration`, `Radiotherapy-Frequency`, `Posology_Information-Dosage`,
                              `Posology_Information-Duration`, `Posology_Information-Frequency`, `Posology_Information-Route`, `Unspecific_Therapy-Dosage`,
                              `Unspecific_Therapy-Duration`, `Unspecific_Therapy-Frequency`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_slim_en_5.5.2_3.4_1738878873620.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/explain_clinical_doc_oncology_slim_en_5.5.2_3.4_1738878873620.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

from sparknlp.pretrained import PretrainedPipeline

oncology_pipeline = PretrainedPipeline("explain_clinical_doc_oncology_slim", "en", "clinical/models")

result = oncology_pipeline.fullAnnotate("""A 56-year-old man presented with a 2-month history of whole-body weakness, double vision, difficulty swallowing, and a 45 mm anterior mediastinal mass detected via chest CT.
Neurological examination and electromyography confirmed a diagnosis of Lambert-Eaton Myasthenic Syndrome (LEMS), associated with anti-P/Q-type VGCC antibodies. The patient was treated with
cisplatin 75 mg/m² on day 1, combined with etoposide 100 mg/m² on days 1-3, repeated every 3 weeks for four cycles. A video-assisted thoracic surgery revealed histopathological features consistent
with small cell lung cancer (SCLC) with lymph node metastases. The immunohistochemical analysis showed positive markers for AE1/AE3, TTF-1, chromogranin A, and synaptophysin. Notably,
a pulmonary nodule in the left upper lobe disappeared, and FDG-PET/CT post-surgery revealed no primary lesions or metastases.""")

```

{:.jsl-block}
```python

from sparknlp.pretrained import PretrainedPipeline

oncology_pipeline = nlp.PretrainedPipeline("explain_clinical_doc_oncology_slim", "en", "clinical/models")

result = oncology_pipeline.fullAnnotate("""A 56-year-old man presented with a 2-month history of whole-body weakness, double vision, difficulty swallowing, and a 45 mm anterior mediastinal mass detected via chest CT.
Neurological examination and electromyography confirmed a diagnosis of Lambert-Eaton Myasthenic Syndrome (LEMS), associated with anti-P/Q-type VGCC antibodies. The patient was treated with
cisplatin 75 mg/m² on day 1, combined with etoposide 100 mg/m² on days 1-3, repeated every 3 weeks for four cycles. A video-assisted thoracic surgery revealed histopathological features consistent
with small cell lung cancer (SCLC) with lymph node metastases. The immunohistochemical analysis showed positive markers for AE1/AE3, TTF-1, chromogranin A, and synaptophysin. Notably,
a pulmonary nodule in the left upper lobe disappeared, and FDG-PET/CT post-surgery revealed no primary lesions or metastases.""")

```
```scala

import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val oncology_pipeline = PretrainedPipeline("explain_clinical_doc_oncology_slim", "en", "clinical/models")

val result = oncology_pipeline.fullAnnotate("""A 56-year-old man presented with a 2-month history of whole-body weakness, double vision, difficulty swallowing, and a 45 mm anterior mediastinal mass detected via chest CT.
Neurological examination and electromyography confirmed a diagnosis of Lambert-Eaton Myasthenic Syndrome (LEMS), associated with anti-P/Q-type VGCC antibodies. The patient was treated with
cisplatin 75 mg/m² on day 1, combined with etoposide 100 mg/m² on days 1-3, repeated every 3 weeks for four cycles. A video-assisted thoracic surgery revealed histopathological features consistent
with small cell lung cancer (SCLC) with lymph node metastases. The immunohistochemical analysis showed positive markers for AE1/AE3, TTF-1, chromogranin A, and synaptophysin. Notably,
a pulmonary nodule in the left upper lobe disappeared, and FDG-PET/CT post-surgery revealed no primary lesions or metastases.""")

```
</div>

## Results

```bash

# NER Oncology Results

|    |   sentence_id | chunks                          |   begin |   end | entities              |
|---:|--------------:|:--------------------------------|--------:|------:|:----------------------|
|  0 |             0 | man                             |      14 |    16 | Gender                |
|  1 |             0 | 45 mm                           |     119 |   123 | Tumor_Size            |
|  2 |             0 | anterior                        |     125 |   132 | Direction             |
|  3 |             0 | mediastinal                     |     134 |   144 | Site_Other_Body_Part  |
|  4 |             0 | mass                            |     146 |   149 | Tumor_Finding         |
|  5 |             0 | chest CT                        |     164 |   171 | Imaging_Test          |
|  6 |             1 | electromyography                |     203 |   218 | Imaging_Test          |
|  7 |             2 | cisplatin                       |     363 |   371 | Chemotherapy          |
|  8 |             2 | 75 mg/m²                        |     373 |   380 | Dosage                |
|  9 |             2 | day 1                           |     385 |   389 | Cycle_Day             |
| 10 |             2 | etoposide                       |     406 |   414 | Chemotherapy          |
| 11 |             2 | 100 mg/m²                       |     416 |   424 | Dosage                |
| 12 |             2 | days 1-3                        |     429 |   436 | Cycle_Day             |
| 13 |             2 | every 3 weeks                   |     448 |   460 | Frequency             |
| 14 |             2 | for four cycles                 |     462 |   476 | Duration              |
| 15 |             3 | video-assisted thoracic surgery |     481 |   511 | Cancer_Surgery        |
| 16 |             3 | histopathological               |     522 |   538 | Pathology_Test        |
| 17 |             3 | small cell                      |     565 |   574 | Histological_Type     |
| 18 |             3 | lung cancer                     |     576 |   586 | Cancer_Dx             |
| 19 |             3 | SCLC                            |     589 |   592 | Cancer_Dx             |
| 20 |             3 | lymph node                      |     600 |   609 | Site_Lymph_Node       |
| 21 |             3 | metastases                      |     611 |   620 | Metastasis            |
| 22 |             4 | immunohistochemical analysis    |     627 |   654 | Pathology_Test        |
| 23 |             4 | positive                        |     663 |   670 | Biomarker_Result      |
| 24 |             4 | AE1/AE3                         |     684 |   690 | Biomarker             |
| 25 |             4 | TTF-1                           |     693 |   697 | Biomarker             |
| 26 |             4 | chromogranin A                  |     700 |   713 | Biomarker             |
| 27 |             4 | synaptophysin                   |     720 |   732 | Biomarker             |
| 28 |             5 | pulmonary                       |     746 |   754 | Site_Lung             |
| 29 |             5 | nodule                          |     756 |   761 | Tumor_Finding         |
| 30 |             5 | left                            |     770 |   773 | Direction             |
| 31 |             5 | upper lobe                      |     775 |   784 | Site_Lung             |
| 32 |             5 | disappeared                     |     786 |   796 | Response_To_Treatment |
| 33 |             5 | FDG-PET/CT                      |     803 |   812 | Imaging_Test          |
| 34 |             5 | primary lesions                 |     839 |   853 | Tumor_Finding         |
| 35 |             5 | metastases                      |     858 |   867 | Metastasis            |

# NER Biomarker Results

|   |     chunks     | begin | end |     entities     | confidence |
|--:|:--------------:|:-----:|:---:|:----------------:|:----------:|
| 0 |    positive    |  663  | 670 | Biomarker_Result |   0.9875   |
| 1 |     AE1/AE3    |  684  | 690 |     Biomarker    |   0.9985   |
| 2 |      TTF-1     |  693  | 697 |     Biomarker    |   0.9992   |
| 3 | chromogranin A |  700  | 713 |     Biomarker    |    0.924   |
| 4 |  synaptophysin |  720  | 732 |     Biomarker    |   0.9978   |

# NER Cancer Types Results

|    |   sentence_id | chunks                 |   begin |   end | entities             |
|---:|--------------:|:-----------------------|--------:|------:|:---------------------|
|  0 |             0 | mediastinal            |     134 |   144 | Site_Other_Body_Part |
|  1 |             0 | chest                  |     164 |   168 | Site_Other_Body_Part |
|  2 |             1 | VGCC                   |     317 |   320 | Biomarker            |
|  3 |             3 | thoracic               |     496 |   503 | Site_Other_Body_Part |
|  4 |             3 | small cell lung cancer |     565 |   586 | Carcinoma_Type       |
|  5 |             3 | SCLC                   |     589 |   592 | Carcinoma_Type       |
|  6 |             3 | lymph node             |     600 |   609 | Site_Other_Body_Part |
|  7 |             3 | metastases             |     611 |   620 | Metastasis           |
|  8 |             4 | positive               |     663 |   670 | Biomarker_Result     |
|  9 |             4 | AE1/AE3                |     684 |   690 | Biomarker            |
| 10 |             4 | TTF-1                  |     693 |   697 | Biomarker            |
| 11 |             4 | chromogranin A         |     700 |   713 | Biomarker            |
| 12 |             4 | synaptophysin          |     720 |   732 | Biomarker            |
| 13 |             5 | pulmonary              |     746 |   754 | Site_Other_Body_Part |
| 14 |             5 | lobe                   |     781 |   784 | Site_Other_Body_Part |
| 15 |             5 | metastases             |     858 |   867 | Metastasis           |

# Assertion Result

|    |   sentence_id | chunks                          |   begin |   end | entities              | assertion   |
|---:|--------------:|:--------------------------------|--------:|------:|:----------------------|:------------|
|  0 |             0 | mass                            |     146 |   149 | Tumor_Finding         | Present     |
|  1 |             1 | VGCC                            |     317 |   320 | Biomarker             | Present     |
|  2 |             2 | cisplatin                       |     363 |   371 | Chemotherapy          | Past        |
|  3 |             2 | etoposide                       |     406 |   414 | Chemotherapy          | Present     |
|  4 |             2 | for four cycles                 |     462 |   476 | Duration              | Present     |
|  5 |             3 | video-assisted thoracic surgery |     481 |   511 | Cancer_Surgery        | Past        |
|  6 |             3 | small cell lung cancer          |     565 |   586 | Carcinoma_Type        | Present     |
|  7 |             3 | SCLC                            |     589 |   592 | Carcinoma_Type        | Present     |
|  8 |             3 | metastases                      |     611 |   620 | Metastasis            | Present     |
|  9 |             4 | AE1/AE3                         |     684 |   690 | Biomarker             | Present     |
| 10 |             4 | TTF-1                           |     693 |   697 | Biomarker             | Present     |
| 11 |             4 | chromogranin A                  |     700 |   713 | Biomarker             | Present     |
| 12 |             4 | synaptophysin                   |     720 |   732 | Biomarker             | Present     |
| 13 |             5 | nodule                          |     756 |   761 | Tumor_Finding         | Present     |
| 14 |             5 | disappeared                     |     786 |   796 | Response_To_Treatment | Present     |
| 15 |             5 | primary lesions                 |     839 |   853 | Tumor_Finding         | Absent      |
| 16 |             5 | metastases                      |     858 |   867 | Metastasis            | Absent      |


# Relation Extraction Result

|    |   sentence |   entity1_begin |   entity1_end | chunk1            | entity1              |   entity2_begin |   entity2_end | chunk2         | entity2       | relation               |   confidence |
|---:|-----------:|----------------:|--------------:|:------------------|:---------------------|----------------:|--------------:|:---------------|:--------------|:-----------------------|-------------:|
|  0 |          2 |             363 |           371 | cisplatin         | Chemotherapy         |             373 |           380 | 75 mg/m²       | Dosage        | Chemotherapy-Dosage    |     1        |
|  1 |          2 |             363 |           371 | cisplatin         | Chemotherapy         |             385 |           389 | day 1          | Cycle_Day     | Chemotherapy-Cycle_Day |     1        |
|  2 |          2 |             363 |           371 | cisplatin         | Chemotherapy         |             416 |           424 | 100 mg/m²      | Dosage        | Chemotherapy-Dosage    |     1        |
|  3 |          2 |             363 |           371 | cisplatin         | Chemotherapy         |             429 |           436 | days 1-3       | Cycle_Day     | Chemotherapy-Cycle_Day |     1        |
|  4 |          2 |             373 |           380 | 75 mg/m²          | Dosage               |             406 |           414 | etoposide      | Chemotherapy  | Dosage-Chemotherapy    |     1        |
|  5 |          2 |             385 |           389 | day 1             | Cycle_Day            |             406 |           414 | etoposide      | Chemotherapy  | Cycle_Day-Chemotherapy |     1        |
|  6 |          2 |             406 |           414 | etoposide         | Chemotherapy         |             416 |           424 | 100 mg/m²      | Dosage        | Chemotherapy-Dosage    |     1        |
|  7 |          2 |             406 |           414 | etoposide         | Chemotherapy         |             429 |           436 | days 1-3       | Cycle_Day     | Chemotherapy-Cycle_Day |     1        |
|  8 |          0 |             119 |           123 | 45 mm             | Tumor_Size           |             146 |           149 | mass           | Tumor_Finding | is_size_of             |     0.968412 |
|  9 |          0 |             134 |           144 | mediastinal       | Site_Other_Body_Part |             146 |           149 | mass           | Tumor_Finding | is_location_of         |     0.929259 |
| 11 |          3 |             522 |           538 | histopathological | Pathology_Test       |             589 |           592 | SCLC           | Cancer_Dx     | is_finding_of          |     0.738208 |
| 13 |          4 |             663 |           670 | positive          | Biomarker_Result     |             684 |           690 | AE1/AE3        | Biomarker     | is_finding_of          |     0.911877 |
| 14 |          4 |             663 |           670 | positive          | Biomarker_Result     |             693 |           697 | TTF-1          | Biomarker     | is_finding_of          |     0.903363 |
| 15 |          4 |             663 |           670 | positive          | Biomarker_Result     |             700 |           713 | chromogranin A | Biomarker     | is_finding_of          |     0.885989 |
| 16 |          4 |             663 |           670 | positive          | Biomarker_Result     |             720 |           732 | synaptophysin  | Biomarker     | is_finding_of          |     0.720167 |
| 17 |          5 |             746 |           754 | pulmonary         | Site_Lung            |             756 |           761 | nodule         | Tumor_Finding | is_location_of         |     0.932414 |
| 19 |          5 |             756 |           761 | nodule            | Tumor_Finding        |             775 |           784 | upper lobe     | Site_Lung     | is_location_of         |     0.932624 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|explain_clinical_doc_oncology_slim|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.5.2+|
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
- ChunkMergeModel
- ChunkMergeModel
- AssertionDLModel
- PerceptronModel
- DependencyParserModel
- RelationExtractionModel
- PosologyREModel
- AnnotationMerger