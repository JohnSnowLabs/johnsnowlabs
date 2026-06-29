---
layout: model
title: ZeroShot Multitask Oncology
author: John Snow Labs
name: zeroshot_multitask_oncology_generic
date: 2026-04-30
tags: [en, licensed, clinical, medical, oncology, ner, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.3.0
spark_version: 3.0
supported: true
engine: onnx
annotator: PretrainedZeroShotMultiTask
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Oncology NER model trained to extract clinical entities from cancer-related clinical notes. Recognizes 27 oncology-specific entity types including cancer diagnoses, therapies, biomarkers, staging, tumor characteristics, and treatment responses.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_oncology_generic_en_6.3.0_3.0_1777556125334.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_multitask_oncology_generic_en_6.3.0_3.0_1777556125334.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology_generic", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result (e.g. ECOG performance status of 4)",
        "Radiation_Dose::Radiation dose values used in radiotherapy (e.g. 40 Gy, 3000 cGy)",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment (e.g. recurrence, bad response, improvement)",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Biomarker::Biological molecules and genes indicating presence, absence, or type of cancer, including oncogenes (e.g. EGFR, HER2, BRCA1)",
        "Body_Part::Anatomical locations and body parts including bones, brain, breast, liver, lungs, lymph nodes, and other body regions",
        "Cancer_Tumor::Cancer diagnoses, pathological cancer types, and nonspecific tumor findings (e.g. carcinoma, adenocarcinoma, mass, lesion, neoplasm)",
        "Cycle_Info::References to oncological therapy cycles including total cycle count (e.g. 5 cycles), cycle day (e.g. day 5), and cycle number (e.g. third cycle)",
        "Date::Date and temporal expressions including exact dates (e.g. March 2023) and relative references (e.g. yesterday, three years later)",
        "Demographics::Patient demographic information including gender-specific terms, racial or ethnic background, and smoking history",
        "Test::Diagnostic procedures including imaging studies (e.g. CT scan, MRI, PET scan) and pathology tests using tissue samples (e.g. biopsy)",
        "Therapy::Any cancer treatment including chemotherapy drugs, hormonal therapy, immunotherapy, targeted therapy, radiotherapy, and unspecific therapies; also includes line of therapy references (e.g. first-line treatment)",
    ])    .setStructures([
        ("cancer_tumor_info", [
            "text::str::cancer diagnosis or tumor finding",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
        ("therapy_info", [
            "text::str::cancer treatment, drug, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
    ])    .setClassifications([
        ("cancer_type",      ["breast", "lung", "colorectal", "prostate", "hematologic", "other", "not_cancer"]),
        ("staging_category", ["early_stage", "locally_advanced", "metastatic", "unknown"]),
    ])    .setRelations([
        "therapy_treats_cancer_tumor",
        "therapy_causes_adverse_effect",
        "test_reveals_finding",
        "biomarker_associated_with_cancer",
        "biomarker_predicts_response_to_therapy",
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

zero_shot = medical.PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology_generic", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("extractions")\
    .setEntityThreshold(0.4)\
    .setEntities([
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result (e.g. ECOG performance status of 4)",
        "Radiation_Dose::Radiation dose values used in radiotherapy (e.g. 40 Gy, 3000 cGy)",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment (e.g. recurrence, bad response, improvement)",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Biomarker::Biological molecules and genes indicating presence, absence, or type of cancer, including oncogenes (e.g. EGFR, HER2, BRCA1)",
        "Body_Part::Anatomical locations and body parts including bones, brain, breast, liver, lungs, lymph nodes, and other body regions",
        "Cancer_Tumor::Cancer diagnoses, pathological cancer types, and nonspecific tumor findings (e.g. carcinoma, adenocarcinoma, mass, lesion, neoplasm)",
        "Cycle_Info::References to oncological therapy cycles including total cycle count (e.g. 5 cycles), cycle day (e.g. day 5), and cycle number (e.g. third cycle)",
        "Date::Date and temporal expressions including exact dates (e.g. March 2023) and relative references (e.g. yesterday, three years later)",
        "Demographics::Patient demographic information including gender-specific terms, racial or ethnic background, and smoking history",
        "Test::Diagnostic procedures including imaging studies (e.g. CT scan, MRI, PET scan) and pathology tests using tissue samples (e.g. biopsy)",
        "Therapy::Any cancer treatment including chemotherapy drugs, hormonal therapy, immunotherapy, targeted therapy, radiotherapy, and unspecific therapies; also includes line of therapy references (e.g. first-line treatment)",
    ])    .setStructures([
        ("cancer_tumor_info", [
            "text::str::cancer diagnosis or tumor finding",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
        ("therapy_info", [
            "text::str::cancer treatment, drug, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]",
        ]),
    ])    .setClassifications([
        ("cancer_type",      ["breast", "lung", "colorectal", "prostate", "hematologic", "other", "not_cancer"]),
        ("staging_category", ["early_stage", "locally_advanced", "metastatic", "unknown"]),
    ])    .setRelations([
        "therapy_treats_cancer_tumor",
        "therapy_causes_adverse_effect",
        "test_reveals_finding",
        "biomarker_associated_with_cancer",
        "biomarker_predicts_response_to_therapy",
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

val zero_shot = PretrainedZeroShotMultiTask.pretrained("zeroshot_multitask_oncology_generic", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("extractions")
    .setEntityThreshold(0.4)
    .setEntities(Array(
        "Adenopathy::Pathological findings of the lymph nodes",
        "Age::All mentions of ages related to the patient or anyone else",
        "Biomarker_Result::Terms or values identified as the result of a biomarker",
        "Cancer_Score::Clinical or imaging scores specific to cancer settings (e.g. BI-RADS, Allred score)",
        "Cancer_Surgery::Terms indicating surgery as a form of cancer treatment",
        "Dosage::Quantity prescribed by the physician for an active ingredient",
        "Duration::Words indicating the duration of a treatment (e.g. for 2 weeks)",
        "Frequency::Words indicating the frequency of treatment administration (e.g. daily, bid)",
        "Grade::Pathological grading of tumors or degrees of cellular differentiation",
        "Histological_Type::Histological variants or cancer subtypes (e.g. papillary, clear cell, medullary)",
        "Invasion::Mentions referring to tumor invasion such as invasion or involvement (metastases excluded)",
        "Metastasis::Terms indicating metastatic disease (anatomical references not included)",
        "Pathology_Result::Biopsy findings from pathology report not covered by another entity (e.g. malignant ductal cells)",
        "Performance_Status::Performance status scores such as ECOG and Karnofsky, including the result",
        "Radiation_Dose::Radiation dose values used in radiotherapy (e.g. 40 Gy, 3000 cGy)",
        "Response_To_Treatment::Terms related to clinical progress of the patient related to cancer treatment",
        "Route::Words indicating the type of administration route (e.g. PO, transdermal)",
        "Staging::Mentions of cancer stage (e.g. stage 2b, T2N1M0, in situ, early-stage, advanced)",
        "Tumor_Size::Size of the tumor including numerical value and unit of measurement (e.g. 3 cm)",
        "Biomarker::Biological molecules and genes indicating presence, absence, or type of cancer (e.g. EGFR, HER2, BRCA1)",
        "Body_Part::Anatomical locations and body parts including bones, brain, breast, liver, lungs, lymph nodes",
        "Cancer_Tumor::Cancer diagnoses, pathological cancer types, and nonspecific tumor findings",
        "Cycle_Info::References to oncological therapy cycles including count, day, and number",
        "Date::Date and temporal expressions including exact dates and relative references",
        "Demographics::Patient demographic information including gender, racial background, and smoking history",
        "Test::Diagnostic procedures including imaging studies and pathology tests",
        "Therapy::Any cancer treatment including chemotherapy, hormonal therapy, immunotherapy, targeted therapy, and radiotherapy"
    ))
    .setStructures(Array(
        ("cancer_tumor_info", Array(
            "text::str::cancer diagnosis or tumor finding",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]"
        )),
        ("therapy_info", Array(
            "text::str::cancer treatment, drug, or therapy",
            "assertion::[present|absent|hypothetical|possible|conditional|associated_with_someone_else]"
        ))
    ))
    .setClassifications(Array(
        ("cancer_type",      Array("breast", "lung", "colorectal", "prostate", "hematologic", "other", "not_cancer")),
        ("staging_category", Array("early_stage", "locally_advanced", "metastatic", "unknown"))
    ))
    .setRelations(Array(
        "therapy_treats_cancer_tumor",
        "therapy_causes_adverse_effect",
        "test_reveals_finding",
        "biomarker_associated_with_cancer",
        "biomarker_predicts_response_to_therapy"
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
|    |   idx |   begin |   end | chunk                         |   sentence | entity            |   confidence |
|---:|------:|--------:|------:|:------------------------------|-----------:|:------------------|-------------:|
|  0 |     0 |       2 |    12 | 58-year-old                   |          0 | Age               |     0.999789 |
|  1 |     0 |      14 |    19 | female                        |          0 | Demographics      |     0.999499 |
|  2 |     0 |      40 |    49 | stage IIIA                    |          0 | Staging           |     0.991417 |
|  3 |     0 |      51 |    63 | HER2-positive                 |          0 | Biomarker         |     0.939996 |
|  4 |     0 |      65 |    72 | invasive                      |          0 | Grade             |     0.682223 |
|  5 |     0 |      65 |    72 | invasive                      |          0 | Histological_Type |     0.996715 |
|  6 |     0 |      74 |    79 | ductal                        |          0 | Grade             |     0.44354  |
|  7 |     0 |      74 |    79 | ductal                        |          0 | Histological_Type |     0.994771 |
|  8 |     0 |      81 |   109 | carcinoma of the right breast |          0 | Cancer_Tumor      |     0.97911  |
|  9 |     0 |     104 |   109 | breast                        |          0 | Body_Part         |     0.432398 |
| 10 |     0 |     112 |   114 | She                           |          0 | Demographics      |     0.999726 |
| 11 |     0 |     125 |   132 | 6 cycles                      |          0 | Cycle_Info        |     0.998358 |
| 12 |     0 |     137 |   147 | neoadjuvant                   |          0 | Therapy           |     0.921425 |
| 13 |     0 |     149 |   159 | carboplatin                   |          0 | Therapy           |     0.577845 |
| 14 |     0 |     166 |   174 | docetaxel                     |          0 | Therapy           |     0.999625 |
| 15 |     0 |     188 |   197 | mastectomy                    |          0 | Cancer_Surgery    |     0.997112 |
| 16 |     0 |     200 |   219 | Adjuvant trastuzumab          |          0 | Therapy           |     0.890815 |
| 17 |     0 |     221 |   227 | 6 mg/kg                       |          0 | Dosage            |     0.999243 |
| 18 |     0 |     229 |   230 | IV                            |          0 | Route             |     0.994162 |
| 19 |     0 |     232 |   244 | every 3 weeks                 |          0 | Frequency         |     0.994471 |
| 20 |     0 |     260 |   272 | for 12 months                 |          0 | Duration          |     0.96816  |

Categories
|    |   idx |   begin |   end | chunk            |   sentence |   confidence | task             |
|---:|------:|--------:|------:|:-----------------|-----------:|-------------:|:-----------------|
|  0 |     0 |       0 |   273 | breast           |          0 |     0.99937  | cancer_type      |
|  1 |     0 |       0 |   273 | locally_advanced |          0 |     0.896815 | staging_category |

Relations
|    |   idx |   begin |   end | chunk                            | entity1   |   sentence |   entity1_begin | entity2   |   chunk1_confidence | chunk1                  | chunk2                        |   entity2_begin |   entity1_end |   entity2_end |   chunk2_confidence |
|---:|------:|--------:|------:|:---------------------------------|:----------|-----------:|----------------:|:----------|--------------------:|:------------------------|:------------------------------|----------------:|--------------:|--------------:|--------------------:|
|  0 |     0 |      51 |   109 | biomarker_associated_with_cancer | head      |          0 |              51 | tail      |            0.853826 | HER2-positive           | carcinoma of the right breast |              81 |            63 |           109 |            0.845844 |
|  1 |     0 |      81 |   159 | therapy_treats_cancer_tumor      | head      |          0 |             137 | tail      |            0.636053 | neoadjuvant carboplatin | carcinoma of the right breast |              81 |           159 |           109 |            0.869209 |
|  2 |     0 |      81 |   174 | therapy_treats_cancer_tumor      | head      |          0 |             166 | tail      |            0.906383 | docetaxel               | carcinoma of the right breast |              81 |           174 |           109 |            0.815702 |


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_multitask_oncology_generic|
|Compatibility:|Healthcare NLP 6.3.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|844.4 MB|