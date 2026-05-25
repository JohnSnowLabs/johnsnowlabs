---
layout: model
title: ZeroShot Multitask Oncology
author: John Snow Labs
name: zeroshot_multitask_oncology
date: 2026-05-25
tags: [en, licensed, clinical, medical, oncology, ner, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.0
supported: true
engine: onnx
annotator: PretrainedZeroShotMultiTask
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Oncology NER model trained to extract clinical entities from cancer-related clinical notes. Recognizes 48 oncology-specific entity types including cancer diagnoses, therapies, biomarkers, staging, tumor characteristics, and treatment responses.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_oncology_en_6.4.0_3.0_1779747939889.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_oncology_en_6.4.0_3.0_1779747939889.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker::Biological molecules indicating presence, absence, or type of cancer (oncogenes excluded)",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Dx::Cancer diagnoses or pathological types used as synonyms for cancer (e.g. carcinoma); anatomical references included",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Chemotherapy::Chemotherapy drugs or unspecific words such as chemotherapy",
        "Cycle_Count::Total number of cycles of an oncological therapy (e.g. 5 cycles)",
        "Cycle_Day::References to the day of the cycle of oncological therapy (e.g. day 5)",
        "Cycle_Number::The number of the cycle of an oncological therapy being applied (e.g. third cycle)",
        "Date::Exact dates in any format, including day number, month and/or year",
        "Death_Entity::Words indicating death of the patient or someone else (e.g. died, passed away)",
        "Direction::Directional and laterality terms such as left, right, bilateral, upper, lower",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Gender::Gender-specific nouns and pronouns, including family members such as father",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Hormonal_Therapy::Hormonal drugs used to treat cancer, or unspecific words such as hormonal therapy",
        "Imaging_Test::Imaging tests mentioned in texts (e.g. chest CT scan)",
        "Immunotherapy::Immunotherapy drugs or unspecific words such as immunotherapy",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Line_Of_Therapy::Explicit references to the line of therapy (e.g. first-line treatment)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Oncogene::Mentions of genes implicated in the etiology of cancer",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Pathology_Test::Mentions of biopsies or tests that use tissue samples",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result (e.g. ECOG performance status of 4)",
        "Race_Ethnicity::Racial, national origin, or sociocultural group categories",
        "Radiotherapy::Terms indicating the use of radiotherapy",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment (e.g. recurrence, bad response, improvement)",
        "Relative_Date::Temporal references relative to the date of the text or another specific date (e.g. yesterday, three years later)",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Site_Bone::Anatomical terms referring to the human skeleton",
        "Site_Brain::Anatomical terms referring to the central nervous system including brain stem and cerebellum",
        "Site_Breast::Anatomical terms referring to the breasts",
        "Site_Liver::Anatomical terms referring to the liver",
        "Site_Lung::Anatomical terms referring to the lungs",
        "Site_Lymph_Node::Anatomical terms referring to lymph nodes, excluding adenopathies",
        "Site_Other_Body_Part::Relevant anatomical terms not included in other anatomical entities",
        "Smoking_Status::All mentions of smoking related to the patient or someone else",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Targeted_Therapy::Targeted therapy drugs or unspecific words such as targeted therapy",
        "Tumor_Finding::Nonspecific terms related to tumors, malignant or benign (e.g. mass, tumor, lesion, neoplasm)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Unspecific_Therapy::Known cancer therapy not specific to any other therapy entity (e.g. chemoradiotherapy, adjuvant therapy)",
    ])    .setClassifications([
        ("cancer_type",       ["breast", "lung", "colorectal", "prostate", "hematologic", "other", "not_cancer"]),
        ("staging_category",  ["early_stage", "locally_advanced", "metastatic", "unknown"]),
    ])    .setRelations([
        "therapies_treats_cancer_dx",
        "therapies_treats_tumor_finding",
        "therapies_Response_To_Treatmentt",
        "imaging_test_reveals_finding",
        "biomarker_associated_with_cancer_dx_or_tumor_finding",
        "oncogene_associated_with_cancer_dx",
    ])

pipeline = Pipeline(
    stages = [
        document_assembler,
        zero_shot
])

text = f"""A 58-year-old female was diagnosed with stage IIIA HER2-positive invasive ductal carcinoma of the right breast. She received 6 cycles of neoadjuvant carboplatin plus docetaxel followed by mastectomy. Adjuvant trastuzumab 6 mg/kg IV every 3 weeks was initiated for 12 months."""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("extractions").show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = medical.PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker::Biological molecules indicating presence, absence, or type of cancer (oncogenes excluded)",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Dx::Cancer diagnoses or pathological types used as synonyms for cancer (e.g. carcinoma); anatomical references included",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Chemotherapy::Chemotherapy drugs or unspecific words such as chemotherapy",
        "Cycle_Count::Total number of cycles of an oncological therapy (e.g. 5 cycles)",
        "Cycle_Day::References to the day of the cycle of oncological therapy (e.g. day 5)",
        "Cycle_Number::The number of the cycle of an oncological therapy being applied (e.g. third cycle)",
        "Date::Exact dates in any format, including day number, month and/or year",
        "Death_Entity::Words indicating death of the patient or someone else (e.g. died, passed away)",
        "Direction::Directional and laterality terms such as left, right, bilateral, upper, lower",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Gender::Gender-specific nouns and pronouns, including family members such as father",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Hormonal_Therapy::Hormonal drugs used to treat cancer, or unspecific words such as hormonal therapy",
        "Imaging_Test::Imaging tests mentioned in texts (e.g. chest CT scan)",
        "Immunotherapy::Immunotherapy drugs or unspecific words such as immunotherapy",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Line_Of_Therapy::Explicit references to the line of therapy (e.g. first-line treatment)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Oncogene::Mentions of genes implicated in the etiology of cancer",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Pathology_Test::Mentions of biopsies or tests that use tissue samples",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result (e.g. ECOG performance status of 4)",
        "Race_Ethnicity::Racial, national origin, or sociocultural group categories",
        "Radiotherapy::Terms indicating the use of radiotherapy",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment (e.g. recurrence, bad response, improvement)",
        "Relative_Date::Temporal references relative to the date of the text or another specific date (e.g. yesterday, three years later)",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Site_Bone::Anatomical terms referring to the human skeleton",
        "Site_Brain::Anatomical terms referring to the central nervous system including brain stem and cerebellum",
        "Site_Breast::Anatomical terms referring to the breasts",
        "Site_Liver::Anatomical terms referring to the liver",
        "Site_Lung::Anatomical terms referring to the lungs",
        "Site_Lymph_Node::Anatomical terms referring to lymph nodes, excluding adenopathies",
        "Site_Other_Body_Part::Relevant anatomical terms not included in other anatomical entities",
        "Smoking_Status::All mentions of smoking related to the patient or someone else",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Targeted_Therapy::Targeted therapy drugs or unspecific words such as targeted therapy",
        "Tumor_Finding::Nonspecific terms related to tumors, malignant or benign (e.g. mass, tumor, lesion, neoplasm)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Unspecific_Therapy::Known cancer therapy not specific to any other therapy entity (e.g. chemoradiotherapy, adjuvant therapy)",
    ])    .setRelations([
        "therapies_treats_cancer_dx",
        "therapies_treats_tumor_finding",
        "therapies_Response_To_Treatmentt",
        "imaging_test_reveals_finding",
        "biomarker_associated_with_cancer_dx_or_tumor_finding", 
        "oncogene_associated_with_cancer_dx",
    ])

pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        zero_shot
])

text = f"""A 58-year-old female was diagnosed with stage IIIA HER2-positive invasive ductal carcinoma of the right breast. She received 6 cycles of neoadjuvant carboplatin plus docetaxel followed by mastectomy. Adjuvant trastuzumab 6 mg/kg IV every 3 weeks was initiated for 12 months."""

data = spark.createDataFrame([[text]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("extractions").show(truncate=False)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("extractions")
    .setEntityThreshold(0.4)
    .setEntities(Array(
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker::Biological molecules indicating presence, absence, or type of cancer (oncogenes excluded)",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Dx::Cancer diagnoses or pathological types used as synonyms for cancer (e.g. carcinoma); anatomical references included",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Chemotherapy::Chemotherapy drugs or unspecific words such as chemotherapy",
        "Cycle_Count::Total number of cycles of an oncological therapy (e.g. 5 cycles)",
        "Cycle_Day::References to the day of the cycle of oncological therapy (e.g. day 5)",
        "Cycle_Number::The number of the cycle of an oncological therapy being applied (e.g. third cycle)",
        "Date::Exact dates in any format, including day number, month and/or year",
        "Death_Entity::Words indicating death of the patient or someone else (e.g. died, passed away)",
        "Direction::Directional and laterality terms such as left, right, bilateral, upper, lower",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Gender::Gender-specific nouns and pronouns, including family members such as father",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Hormonal_Therapy::Hormonal drugs used to treat cancer, or unspecific words such as hormonal therapy",
        "Imaging_Test::Imaging tests mentioned in texts (e.g. chest CT scan)",
        "Immunotherapy::Immunotherapy drugs or unspecific words such as immunotherapy",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Line_Of_Therapy::Explicit references to the line of therapy (e.g. first-line treatment)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Oncogene::Mentions of genes implicated in the etiology of cancer",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Pathology_Test::Mentions of biopsies or tests that use tissue samples",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result (e.g. ECOG performance status of 4)",
        "Race_Ethnicity::Racial, national origin, or sociocultural group categories",
        "Radiotherapy::Terms indicating the use of radiotherapy",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment (e.g. recurrence, bad response, improvement)",
        "Relative_Date::Temporal references relative to the date of the text or another specific date (e.g. yesterday, three years later)",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Site_Bone::Anatomical terms referring to the human skeleton",
        "Site_Brain::Anatomical terms referring to the central nervous system including brain stem and cerebellum",
        "Site_Breast::Anatomical terms referring to the breasts",
        "Site_Liver::Anatomical terms referring to the liver",
        "Site_Lung::Anatomical terms referring to the lungs",
        "Site_Lymph_Node::Anatomical terms referring to lymph nodes, excluding adenopathies",
        "Site_Other_Body_Part::Relevant anatomical terms not included in other anatomical entities",
        "Smoking_Status::All mentions of smoking related to the patient or someone else",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Targeted_Therapy::Targeted therapy drugs or unspecific words such as targeted therapy",
        "Tumor_Finding::Nonspecific terms related to tumors, malignant or benign (e.g. mass, tumor, lesion, neoplasm)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Unspecific_Therapy::Known cancer therapy not specific to any other therapy entity (e.g. chemoradiotherapy, adjuvant therapy)"
    ))
    .setClassifications(Array(
        ("cancer_type", Array("breast", "lung", "colorectal", "prostate", "hematologic", "other", "not_cancer")),
        ("staging_category", Array("early_stage", "locally_advanced", "metastatic", "unknown"))
    ))
    .setRelations(Array(
        "therapies_treats_cancer_dx",
        "therapies_treats_tumor_finding",
        "therapies_Response_To_Treatmentt",
        "imaging_test_reveals_finding",
        "biomarker_associated_with_cancer_dx_or_tumor_finding",
        "oncogene_associated_with_cancer_dx"
    ))


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    zero_shot
))

val text = f"""A 58-year-old female was diagnosed with stage IIIA HER2-positive invasive ductal carcinoma of the right breast. She received 6 cycles of neoadjuvant carboplatin plus docetaxel followed by mastectomy. Adjuvant trastuzumab 6 mg/kg IV every 3 weeks was initiated for 12 months."""

val data = Seq(text).toDF("text")

val results = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
Entities
|    |   idx |   begin |   end | chunk         |   sentence | ner_source   | entity             |   confidence |
|---:|------:|--------:|------:|:--------------|-----------:|:-------------|:-------------------|-------------:|
|  0 |     0 |       2 |    12 | 58-year-old   |          0 | extractions  | Age                |     0.999955 |
|  1 |     0 |      40 |    49 | stage IIIA    |          0 | extractions  | Staging            |     0.998781 |
|  2 |     0 |      51 |    63 | HER2-positive |          0 | extractions  | Oncogene           |     0.928906 |
|  3 |     0 |      65 |    72 | invasive      |          0 | extractions  | Histological_Type  |     0.996087 |
|  4 |     0 |      98 |   102 | right         |          0 | extractions  | Direction          |     0.988863 |
|  5 |     0 |     104 |   109 | breast        |          0 | extractions  | Site_Breast        |     0.986516 |
|  6 |     0 |     112 |   114 | She           |          0 | extractions  | Gender             |     0.999793 |
|  7 |     0 |     125 |   132 | 6 cycles      |          0 | extractions  | Cycle_Count        |     0.966434 |
|  8 |     0 |     137 |   147 | neoadjuvant   |          0 | extractions  | Line_Of_Therapy    |     0.933257 |
|  9 |     0 |     149 |   159 | carboplatin   |          0 | extractions  | Chemotherapy       |     0.960494 |
| 10 |     0 |     188 |   197 | mastectomy    |          0 | extractions  | Cancer_Surgery     |     0.998887 |
| 11 |     0 |     200 |   207 | Adjuvant      |          0 | extractions  | Unspecific_Therapy |     0.503498 |
| 12 |     0 |     209 |   219 | trastuzumab   |          0 | extractions  | Targeted_Therapy   |     0.591788 |
| 13 |     0 |     221 |   227 | 6 mg/kg       |          0 | extractions  | Dosage             |     0.992292 |
| 14 |     0 |     229 |   230 | IV            |          0 | extractions  | Route              |     0.994224 |
| 15 |     0 |     232 |   244 | every 3 weeks |          0 | extractions  | Frequency          |     0.997765 |
| 16 |     0 |     260 |   272 | for 12 months |          0 | extractions  | Duration           |     0.980083 |

Categories
|    |   idx |   begin |   end | chunk            |   sentence | category_type   | task             |   confidence |
|---:|------:|--------:|------:|:-----------------|-----------:|:----------------|:-----------------|-------------:|
|  0 |     0 |       0 |   273 | breast           |          0 | classification  | cancer_type      |     0.999504 |
|  1 |     0 |       0 |   273 | locally_advanced |          0 | classification  | staging_category |     0.899837 |

Relations
|    |   idx |   begin |   end | chunk                              | entity1   |   sentence |   entity1_begin | entity2   |   chunk1_confidence | chunk1        | chunk2                        |   entity2_begin |   entity1_end | category_type   |   entity2_end |   chunk2_confidence |
|---:|------:|--------:|------:|:-----------------------------------|:----------|-----------:|----------------:|:----------|--------------------:|:--------------|:------------------------------|----------------:|--------------:|:----------------|--------------:|--------------------:|
|  0 |     0 |      51 |   109 | oncogene_associated_with_cancer_dx | head      |          0 |              51 | tail      |            0.878524 | HER2-positive | carcinoma of the right breast |              81 |            63 | relation        |           109 |            0.634918 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_oncology|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|844.5 MB|