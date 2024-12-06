---
layout: model
title: Named Entity Recognition Profiling (Oncology)
author: John Snow Labs
name: ner_profiling_oncology
date: 2024-06-18
tags: [licensed, en, clinical, profiling, ner_profiling, ner, oncology]
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

This pipeline can be used to simultaneously evaluate various pre-trained named entity recognition (NER) models, enabling comprehensive analysis of text data related to oncology.  When you run this pipeline over your text, you will end up with the predictions coming out of each pretrained clinical NER model trained with the`embeddings_clinical`, which are specifically designed for clinical and biomedical text.


`ner_oncology`, `ner_oncology_anatomy_general`, `ner_oncology_anatomy_general_langtest`, `ner_oncology_anatomy_granular`, `ner_oncology_anatomy_granular_langtest`, `ner_oncology_biomarker`, `ner_oncology_biomarker_langtest`, `ner_oncology_demographics`, `ner_oncology_demographics_langtest`, `ner_oncology_diagnosis`, `ner_oncology_diagnosis_langtest`, `ner_oncology_langtest`, `ner_oncology_limited_80p_for_benchmarks`, `ner_oncology_posology`, `ner_oncology_posology_langtest`, `ner_oncology_response_to_treatment`, `ner_oncology_response_to_treatment_langtest`, `ner_oncology_test`, `ner_oncology_test_langtest`,`ner_oncology_therapy`, `ner_oncology_therapy_langtest`, `ner_oncology_tnm`, `ner_oncology_tnm_langtest`, `ner_oncology_unspecific_posology`, `ner_oncology_unspecific_posology_langtest`, `ner_jsl`, `ner_jsl_langtest`, `ner_jsl_greedy`, `ner_jsl_enriched`, `ner_jsl_slim`

## Predicted Entities

`Adenopathy`, `Age`, `Alcohol`, `Anatomical_Site`, `BMI`, `Biomarker`, `Biomarker_Result`, `Cancer_Dx`, `Cancer_Score`, `Cancer_Surgery`, `Cancer_Therapy`, `Chemotherapy`, `Communicable_Disease`, `Cycle_Count`, `Cycle_Day`, `Cycle_Number`, `Date`, `Death_Entity`, `Diabetes`, `Direction`, `Dosage`, `Duration`, `Frequency`, `Gender`, `Grade`, `Histological_Type`, `Hormonal_Therapy`, `Imaging_Test`, `Immunotherapy`, `Invasion`, `Line_Of_Therapy`, `Lymph_Node`, `Lymph_Node_Modifier`, `Metastasis`, `Obesity`, `Oncogene`, `Oncological`, `Overweight`, `Pathology_Result`, `Pathology_Test`, `Performance_Status`, `Posology_Information`, `Race_Ethnicity`, `Radiation_Dose`, `Radiotherapy`, `Relative_Date`, `Response_To_Treatment`, `Route`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part`, `Size_Trend`, `Smoking`, `Smoking_Status`, `Staging`, `Targeted_Therapy`, `Tumor`, `Tumor_Description`, `Tumor_Finding`, `Tumor_Size`, `Unspecific_Therapy`, `Weight`


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_5.3.2_3.0_1718744204554.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_profiling_oncology_en_5.3.2_3.0_1718744204554.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", 'en', 'clinical/models')

text = """
The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. 
A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. 
The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. 
The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. 
Two months later, the patient was diagnosed with lung metastases. 
Neoadjuvant chemotherapy with the regimens of Cyclophosphamide (500 mg/m2) is being given for 6 cycles with poor response.
"""

result = ner_profiling_pipeline.fullAnnotate(text)

```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", "en", "clinical/models")

val text = """
The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. 
A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. 
The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. 
The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. 
Two months later, the patient was diagnosed with lung metastases. 
Neoadjuvant chemotherapy with the regimens of Cyclophosphamide (500 mg/m2) is being given for 6 cycles with poor response.
"""

val result = ner_profiling_pipeline.annotate(text)

```
</div>

## Results

```bash

******************** ner_jsl_greedy Model Results ******************** 

('adenocarcinoma', 'Oncological') ('tumor', 'Oncological') ('tumor', 'Oncological') ('stage IIIC papillary serous ovarian adenocarcinoma', 'Oncological') ('lung metastases', 'Oncological')

******************** ner_jsl_enriched Model Results ******************** 

('adenocarcinoma', 'Oncological') ('tumor', 'Oncological') ('tumor', 'Oncological') ('papillary serous ovarian adenocarcinoma', 'Oncological') ('lung metastases', 'Oncological')

******************** ner_oncology_anatomy_general Model Results ******************** 

('ovarian', 'Anatomical_Site') ('fallopian tubes', 'Anatomical_Site') ('appendix', 'Anatomical_Site') ('omentum', 'Anatomical_Site') ('lymph nodes', 'Anatomical_Site') ('lung', 'Anatomical_Site')

******************** ner_oncology_test Model Results ******************** 

('computed tomography', 'Imaging_Test') ('CT', 'Imaging_Test') ('scan of the abdomen and pelvis', 'Imaging_Test') ('Pap smear', 'Pathology_Test')

******************** ner_jsl_slim Model Results ******************** 

('adenocarcinoma', 'Oncological') ('tumor', 'Oncological') ('tumor', 'Oncological') ('stage IIIC papillary serous ovarian adenocarcinoma', 'Oncological') ('lung metastases', 'Oncological')

******************** ner_oncology_posology_langtest Model Results ******************** 

('Neoadjuvant chemotherapy', 'Cancer_Therapy') ('Cyclophosphamide', 'Cancer_Therapy') ('500 mg/m2', 'Dosage') ('for 6 cycles', 'Duration')

******************** ner_oncology_biomarker_langtest Model Results ******************** 



******************** ner_oncology_limited_80p_for_benchmarks_ner Model Results ******************** 

('computed tomography', 'Imaging_Test') ('CT', 'Imaging_Test') ('scan of the abdomen and pelvis', 'Imaging_Test') ('ovarian', 'Site_Other_Body_Part') ('mass', 'Tumor_Finding') ('Pap smear', 'Pathology_Test') ('one month later', 'Relative_Date') ('atypical glandular cells', 'Pathology_Result') ('adenocarcinoma', 'Cancer_Dx') ('extension', 'Invasion') ('tumor', 'Tumor_Finding') ('fallopian tubes', 'Site_Other_Body_Part') ('appendix', 'Site_Other_Body_Part') ('omentum', 'Site_Other_Body_Part') ('lymph nodes', 'Site_Lymph_Node') ('tumor', 'Tumor_Finding') ('stage IIIC', 'Staging') ('papillary', 'Histological_Type') ('serous', 'Histological_Type') ('ovarian adenocarcinoma', 'Cancer_Dx') ('Two months later', 'Relative_Date') ('lung', 'Site_Lung') ('metastases', 'Metastasis') ('Neoadjuvant chemotherapy', 'Chemotherapy') ('Cyclophosphamide', 'Chemotherapy') ('500 mg/m2', 'Dosage') ('6 cycles', 'Cycle_Count') ('poor response', 'Response_To_Treatment')

******************** ner_oncology_tnm Model Results ******************** 

('mass', 'Tumor') ('atypical glandular cells', 'Tumor_Description') ('adenocarcinoma', 'Cancer_Dx') ('extension', 'Tumor_Description') ('tumor', 'Tumor') ('enlarged', 'Lymph_Node_Modifier') ('lymph nodes', 'Lymph_Node') ('tumor', 'Tumor') ('stage IIIC', 'Staging') ('papillary', 'Tumor_Description') ('serous', 'Tumor_Description') ('ovarian adenocarcinoma', 'Cancer_Dx') ('metastases', 'Metastasis')

******************** ner_oncology Model Results ******************** 

('computed tomography', 'Imaging_Test') ('CT', 'Imaging_Test') ('abdomen', 'Site_Other_Body_Part') ('pelvis', 'Site_Other_Body_Part') ('ovarian', 'Site_Other_Body_Part') ('mass', 'Tumor_Finding') ('Pap smear', 'Pathology_Test') ('one month later', 'Relative_Date') ('atypical glandular cells', 'Pathology_Result') ('adenocarcinoma', 'Cancer_Dx') ('pathologic specimen', 'Pathology_Test') ('extension', 'Invasion') ('tumor', 'Tumor_Finding') ('fallopian tubes', 'Site_Other_Body_Part') ('appendix', 'Site_Other_Body_Part') ('omentum', 'Site_Other_Body_Part') ('lymph nodes', 'Site_Lymph_Node') ('tumor', 'Tumor_Finding') ('stage IIIC', 'Staging') ('papillary', 'Histological_Type') ('serous', 'Histological_Type') ('ovarian adenocarcinoma', 'Cancer_Dx') ('Two months later', 'Relative_Date') ('lung', 'Site_Lung') ('metastases', 'Metastasis') ('Neoadjuvant chemotherapy', 'Chemotherapy') ('Cyclophosphamide', 'Chemotherapy') ('500 mg/m2', 'Dosage') ('6 cycles', 'Cycle_Count') ('poor response', 'Response_To_Treatment')

******************** ner_oncology_therapy Model Results ******************** 

('Neoadjuvant chemotherapy', 'Chemotherapy') ('Cyclophosphamide', 'Chemotherapy') ('500 mg/m2', 'Dosage') ('6 cycles', 'Cycle_Count') ('poor response', 'Response_To_Treatment')

******************** ner_jsl Model Results ******************** 

('adenocarcinoma', 'Oncological') ('tumor', 'Oncological') ('tumor', 'Oncological') ('papillary serous ovarian adenocarcinoma', 'Oncological') ('lung metastases', 'Oncological')

******************** ner_oncology_therapy_langtest Model Results ******************** 

('complex', 'Response_To_Treatment') ('enlarged', 'Response_To_Treatment') ('Neoadjuvant chemotherapy', 'Chemotherapy') ('Cyclophosphamide', 'Chemotherapy') ('500 mg/m2', 'Chemotherapy') ('6 cycles', 'Cycle_Count') ('poor response', 'Response_To_Treatment')

******************** ner_oncology_response_to_treatment_langtest_ner Model Results ******************** 

('enlarged', 'Size_Trend') ('poor response', 'Response_To_Treatment')

******************** ner_oncology_anatomy_granular_langtest Model Results ******************** 

('abdomen', 'Site_Other_Body_Part') ('pelvis', 'Site_Other_Body_Part') ('ovarian', 'Site_Other_Body_Part') ('fallopian tubes', 'Site_Other_Body_Part') ('appendix', 'Site_Other_Body_Part') ('omentum', 'Site_Other_Body_Part') ('lymph nodes', 'Site_Lymph_Node') ('lung', 'Site_Lung')

******************** ner_oncology_biomarker Model Results ******************** 



******************** ner_oncology_tnm_langtest Model Results ******************** 

('mass', 'Tumor') ('atypical glandular cells', 'Tumor_Description') ('adenocarcinoma', 'Cancer_Dx') ('extension', 'Tumor_Description') ('tumor', 'Tumor') ('enlarged', 'Lymph_Node_Modifier') ('lymph nodes', 'Lymph_Node') ('tumor', 'Tumor') ('stage IIIC', 'Staging') ('papillary', 'Tumor_Description') ('serous', 'Tumor_Description') ('ovarian adenocarcinoma', 'Cancer_Dx') ('metastases', 'Metastasis')

******************** ner_oncology_anatomy_general_langtest Model Results ******************** 

('ovarian', 'Anatomical_Site') ('fallopian tubes', 'Anatomical_Site') ('appendix', 'Anatomical_Site') ('omentum', 'Anatomical_Site') ('lymph nodes', 'Anatomical_Site') ('lung', 'Anatomical_Site')

******************** ner_oncology_demographics Model Results ******************** 



******************** ner_oncology_response_to_treatment Model Results ******************** 

('poor response', 'Response_To_Treatment')

******************** ner_oncology_posology Model Results ******************** 

('Neoadjuvant chemotherapy', 'Cancer_Therapy') ('Cyclophosphamide', 'Cancer_Therapy') ('500 mg/m2', 'Dosage') ('6 cycles', 'Cycle_Count')

******************** ner_oncology_demographics_langtest Model Results ******************** 



******************** ner_oncology_test_langtest Model Results ******************** 

('computed tomography', 'Imaging_Test') ('CT', 'Imaging_Test') ('scan of the abdomen and pelvis', 'Imaging_Test') ('Pap smear', 'Pathology_Test')

******************** ner_jsl_langtest Model Results ******************** 

('adenocarcinoma', 'Oncological') ('tumor', 'Oncological') ('tumor', 'Oncological') ('papillary serous ovarian adenocarcinoma', 'Oncological') ('lung metastases', 'Oncological')

******************** ner_oncology_diagnosis Model Results ******************** 

('mass', 'Tumor_Finding') ('atypical glandular cells', 'Pathology_Result') ('adenocarcinoma', 'Cancer_Dx') ('extension', 'Invasion') ('tumor', 'Tumor_Finding') ('tumor', 'Tumor_Finding') ('stage IIIC', 'Staging') ('papillary', 'Histological_Type') ('serous', 'Histological_Type') ('ovarian adenocarcinoma', 'Cancer_Dx') ('metastases', 'Metastasis')

******************** ner_oncology_langtest Model Results ******************** 

('computed tomography', 'Imaging_Test') ('CT', 'Imaging_Test') ('scan of the abdomen and pelvis', 'Imaging_Test') ('ovarian', 'Site_Other_Body_Part') ('mass', 'Tumor_Finding') ('Pap smear', 'Pathology_Test') ('one month later', 'Relative_Date') ('positive', 'Pathology_Result') ('atypical glandular cells', 'Pathology_Result') ('adenocarcinoma', 'Cancer_Dx') ('pathologic specimen', 'Pathology_Test') ('extension', 'Invasion') ('tumor', 'Tumor_Finding') ('fallopian tubes', 'Site_Other_Body_Part') ('appendix', 'Site_Other_Body_Part') ('omentum', 'Site_Other_Body_Part') ('lymph nodes', 'Site_Lymph_Node') ('tumor', 'Tumor_Finding') ('stage IIIC', 'Staging') ('papillary', 'Histological_Type') ('serous', 'Histological_Type') ('ovarian adenocarcinoma', 'Cancer_Dx') ('Two months later', 'Relative_Date') ('lung', 'Site_Lung') ('metastases', 'Metastasis') ('Neoadjuvant chemotherapy', 'Chemotherapy') ('Cyclophosphamide', 'Chemotherapy') ('500 mg/m2', 'Dosage') ('6 cycles', 'Cycle_Count') ('poor response', 'Response_To_Treatment')

******************** ner_oncology_unspecific_posology_langtest Model Results ******************** 

('Neoadjuvant chemotherapy', 'Cancer_Therapy') ('Cyclophosphamide', 'Cancer_Therapy') ('500 mg/m2', 'Posology_Information') ('6 cycles', 'Posology_Information')

******************** ner_oncology_unspecific_posology Model Results ******************** 

('Neoadjuvant chemotherapy', 'Cancer_Therapy') ('Cyclophosphamide', 'Cancer_Therapy') ('500 mg/m2', 'Posology_Information') ('6 cycles', 'Posology_Information')

******************** ner_oncology_diagnosis_langtest Model Results ******************** 

('mass', 'Tumor_Finding') ('atypical glandular cells', 'Pathology_Result') ('adenocarcinoma', 'Cancer_Dx') ('extension', 'Invasion') ('tumor', 'Tumor_Finding') ('tumor', 'Tumor_Finding') ('stage IIIC', 'Staging') ('papillary', 'Histological_Type') ('serous', 'Histological_Type') ('ovarian adenocarcinoma', 'Cancer_Dx') ('metastases', 'Metastasis')

******************** ner_oncology_anatomy_granular Model Results ******************** 
('abdomen', 'Site_Other_Body_Part') ('pelvis', 'Site_Other_Body_Part') ('ovarian', 'Site_Other_Body_Part') ('fallopian tubes', 'Site_Other_Body_Part') ('appendix', 'Site_Other_Body_Part') ('omentum', 'Site_Other_Body_Part') ('lymph nodes', 'Site_Lymph_Node') ('lung', 'Site_Lung')

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_profiling_oncology|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 5.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|

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