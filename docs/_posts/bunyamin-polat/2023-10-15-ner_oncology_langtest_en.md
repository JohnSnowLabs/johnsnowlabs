---
layout: model
title: Detect Oncology-Specific Entities (LangTest)
author: John Snow Labs
name: ner_oncology_langtest
date: 2023-10-15
tags: [en, ner, clinical, licensed, oncology, langtest]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model extracts more than 40 oncology-related entities, including therapies, tests, and staging. It is the version of [ner_oncology](https://nlp.johnsnowlabs.com/2022/11/24/ner_oncology_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **add_ocr_typo**     | 1991                  | 567                  | 1338                  | 2762                 | 70%                   | 40%                  | 83%                 |
| **add_typo**         | 743                   | 603                  | 2507                  | 2669                 | 70%                   | 77%                  | 82%                 |
| **lowercase**        | 899                   | 590                  | 2492                  | 2801                 | 70%                   | 73%                  | 83%                 |
| **swap_entities**    | 613                   | 599                  | 1915                  | 1920                 | 70%                   | 76%                  | 76%                 |
| **titlecase**        | 2171                  | 828                  | 1227                  | 2570                 | 70%                   | 36%                  | 76%                 |
| **uppercase**        | 2825                  | 728                  | 584                   | 2681                 | 70%                   | 17%                  | 79%                 |
| **weighted average** | **9242**              | **3915**             | **10063**             | **15403**            | **70%**               | **52.13%**           | **79.73%**          |


Definitions of Predicted Entities:

- `Adenopathy`: Mentions of pathological findings of the lymph nodes.
- `Age`: All mention of ages, past or present, related to the patient or with anybody else.
- `Biomarker`: Biological molecules that indicate the presence or absence of cancer, or the type of cancer. Oncogenes are excluded from this category.
- `Biomarker_Result`: Terms or values that are identified as the result of biomarkers.
- `Cancer_Dx`: Mentions of cancer diagnoses (such as "breast cancer") or pathological types that are usually used as synonyms for "cancer" (e.g. "carcinoma"). When anatomical references are present, they are included in the Cancer_Dx extraction.
- `Cancer_Score`: Clinical or imaging scores that are specific for cancer settings (e.g. "BI-RADS" or "Allred score").
- `Cancer_Surgery`: Terms that indicate surgery as a form of cancer treatment.
- `Chemotherapy`: Mentions of chemotherapy drugs, or unspecific words such as "chemotherapy".
- `Cycle_Coun`: The total number of cycles being administered of an oncological therapy (e.g. "5 cycles"). 
- `Cycle_Day`: References to the day of the cycle of oncological therapy (e.g. "day 5").
- `Cycle_Number`: The number of the cycle of an oncological therapy that is being applied (e.g. "third cycle").
- `Date`: Mentions of exact dates, in any format, including day number, month, and/or year.
- `Death_Entity`: Words that indicate the death of the patient or someone else (including family members), such as "died" or "passed away".
- `Direction`: Directional and laterality terms, such as "left", "right", "bilateral", "upper" and "lower".
- `Dosage`: The quantity prescribed by the physician for an active ingredient.
- `Duration`: Words indicating the duration of a treatment (e.g. "for 2 weeks").
- `Frequency`: Words indicating the frequency of treatment administration (e.g. "daily" or "bid").
- `Gender`: Gender-specific nouns and pronouns (including words such as "him" or "she", and family members such as "father").
- `Grade`: All pathological grading of tumors (e.g. "grade 1") or degrees of cellular differentiation (e.g. "well-differentiated")
- `Histological_Type`: Histological variants or cancer subtypes, such as "papillary", "clear cell" or "medullary". 
- `Hormonal_Therapy`: Mentions of hormonal drugs used to treat cancer, or unspecific words such as "hormonal therapy".
- `Imaging_Test`: Imaging tests mentioned in texts, such as "chest CT scan".
- `Immunotherapy`: Mentions of immunotherapy drugs, or unspecific words such as "immunotherapy".
- `Invasion`: Mentions that refer to tumor invasion, such as "invasion" or "involvement". Metastases or lymph node involvement are excluded from this category.
- `Line_Of_Therapy`: Explicit references to the line of therapy of an oncological therapy (e.g. "first-line treatment").
- `Metastasis`: Terms that indicate a metastatic disease. Anatomical references are not included in these extractions.
- `Oncogene`: Mentions of genes that are implicated in the etiology of cancer.
- `Pathology_Result`: The findings of a biopsy from the pathology report that is not covered by another entity (e.g. "malignant ductal cells").
- `Pathology_Test`: Mentions of biopsies or tests that use tissue samples.
- `Performance_Status`: Mentions of performance status scores, such as ECOG and Karnofsky. The name of the score is extracted together with the result (e.g. "ECOG performance status of 4").
- `Race_Ethnicity`: The race and ethnicity categories include racial and national origin or sociocultural groups.
- `Radiotherapy`: Terms that indicate the use of Radiotherapy.
- `Response_To_Treatment`: Terms related to the clinical progress of the patient related to cancer treatment, including "recurrence", "bad response" or "improvement".
- `Relative_Date`: Temporal references that are relative to the date of the text or to any other specific date (e.g. "yesterday" or "three years later").
- `Route`: Words indicating the type of administration route (such as "PO" or "transdermal").
- `Site_Bone`: Anatomical terms that refer to the human skeleton.
- `Site_Brain`: Anatomical terms that refer to the central nervous system (including the brain stem and the cerebellum).
- `Site_Breast`: Anatomical terms that refer to the breasts.
- `Site_Liver`: Anatomical terms that refer to the liver.
- `Site_Lung`: Anatomical terms that refer to the lungs.
- `Site_Lymph_Node`: Anatomical terms that refer to lymph nodes, excluding adenopathies.
- `Site_Other_Body_Part`: Relevant anatomical terms that are not included in the rest of the anatomical entities.
- `Smoking_Status`: All mentions of smoking related to the patient or to someone else.
- `Staging`: Mentions of cancer stage such as "stage 2b" or "T2N1M0". It also includes words such as "in situ", "early-stage" or "advanced".
- `Targeted_Therapy`: Mentions of targeted therapy drugs, or unspecific words such as "targeted therapy".
- `Tumor_Finding`: All nonspecific terms that may be related to tumors, either malignant or benign (for example: "mass", "tumor", "lesion", or "neoplasm").
- `Tumor_Size`: Size of the tumor, including numerical value and unit of measurement (e.g. "3 cm").
- `Unspecific_Therapy`: Terms that indicate a known cancer therapy but that is not specific to any other therapy entity (e.g. "chemoradiotherapy" or "adjuvant therapy").

## Predicted Entities

`Histological_Type`, `Direction`, `Staging`, `Cancer_Score`, `Imaging_Test`, `Cycle_Number`, `Tumor_Finding`, `Site_Lymph_Node`, `Invasion`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy`, `Age`, `Biomarker_Result`, `Unspecific_Therapy`, `Site_Breast`, `Chemotherapy`, `Targeted_Therapy`, `Radiotherapy`, `Performance_Status`, `Pathology_Test`, `Site_Other_Body_Part`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Site_Bone`, `Biomarker`, `Immunotherapy`, `Cycle_Day`, `Frequency`, `Route`, `Duration`, `Death_Entity`, `Metastasis`, `Site_Liver`, `Cancer_Dx`, `Grade`, `Date`, `Site_Lung`, `Site_Brain`, `Relative_Date`, `Race_Ethnicity`, `Gender`, `Oncogene`, `Dosage`, `Radiation_Dose`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_oncology_langtest_en_5.1.1_3.0_1697402330566.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_oncology_langtest_en_5.1.1_3.0_1697402330566.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")                

ner = MedicalNerModel.pretrained("ner_oncology_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")
pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter])

data = spark.createDataFrame([["The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first-line therapy."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
    
val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")
    
val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")
    
val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                
    
val ner = MedicalNerModel.pretrained("ner_oncology_langtest", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")
    
val ner_converter = new NerConverter()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter))    

val data = Seq("The had previously undergone a left mastectomy and an axillary lymph node dissection for a left breast cancer twenty years ago.
The tumor was positive for ER and PR. Postoperatively, radiotherapy was administered to the residual breast.
The cancer recurred as a right lung metastasis 13 years later. The patient underwent a regimen consisting of adriamycin (60 mg/m2) and cyclophosphamide (600 mg/m2) over six courses, as first-line therapy.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.metadata)).alias("cols")) \
      .select(F.expr("cols['0']").alias("chunk"),
              F.expr("cols['1']['entity']").alias("ner_label")).show(100, truncate=False)
output
+------------------------------+---------------------+
|chunk                         |ner_label            |
+------------------------------+---------------------+
|left                          |Direction            |
|mastectomy                    |Cancer_Surgery       |
|axillary lymph node dissection|Cancer_Surgery       |
|left                          |Direction            |
|breast cancer                 |Cancer_Dx            |
|twenty years ago              |Relative_Date        |
|tumor                         |Tumor_Finding        |
|positive                      |Biomarker_Result     |
|ER                            |Biomarker            |
|PR                            |Biomarker            |
|radiotherapy                  |Radiotherapy         |
|breast                        |Site_Breast          |
|cancer                        |Cancer_Dx            |
|recurred                      |Response_To_Treatment|
|right                         |Direction            |
|lung                          |Site_Lung            |
|metastasis                    |Metastasis           |
|13 years later                |Relative_Date        |
|adriamycin                    |Chemotherapy         |
|60 mg/m2                      |Dosage               |
|cyclophosphamide              |Chemotherapy         |
|600 mg/m2                     |Dosage               |
|six courses                   |Cycle_Count          |
|first line therapy            |Line_Of_Therapy      |
+------------------------------+---------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_oncology_langtest|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

In-house annotated oncology case reports.

## Benchmarking

```bash
label                  precision  recall  f1-score  support 
Adenopathy             0.67       0.69    0.68      29      
Age                    0.94       0.90    0.92      165     
Biomarker              0.84       0.80    0.82      597     
Biomarker_Result       0.79       0.78    0.78      514     
Cancer_Dx              0.85       0.89    0.87      551     
Cancer_Score           0.58       0.70    0.64      10      
Cancer_Surgery         0.76       0.79    0.78      339     
Chemotherapy           0.91       0.93    0.92      491     
Cycle_Count            0.78       0.85    0.81      86      
Cycle_Day              0.78       0.79    0.79      91      
Cycle_Number           0.72       0.54    0.62      24      
Date                   0.96       0.95    0.96      288     
Death_Entity           0.93       0.97    0.95      29      
Direction              0.81       0.81    0.81      634     
Dosage                 0.87       0.88    0.87      264     
Duration               0.66       0.73    0.70      168     
Frequency              0.82       0.90    0.86      104     
Gender                 0.99       0.99    0.99      914     
Grade                  0.69       0.72    0.70      67      
Histological_Type      0.81       0.63    0.71      191     
Hormonal_Therapy       0.94       0.89    0.91      82      
Imaging_Test           0.79       0.82    0.81      646     
Immunotherapy          0.86       0.65    0.74      48      
Invasion               0.82       0.79    0.80      118     
Line_Of_Therapy        0.81       0.85    0.83      26      
Metastasis             0.91       0.93    0.92      229     
Oncogene               0.68       0.70    0.69      178     
Pathology_Result       0.45       0.34    0.38      247     
Pathology_Test         0.76       0.76    0.76      391     
Performance_Status     0.73       0.65    0.69      17      
Race_Ethnicity         0.88       0.95    0.91      38      
Radiation_Dose         0.97       0.90    0.93      39      
Radiotherapy           0.80       0.81    0.81      118     
Relative_Date          0.75       0.77    0.76      283     
Response_To_Treatment  0.70       0.64    0.67      284     
Route                  0.92       0.83    0.87      70      
Site_Bone              0.76       0.75    0.75      170     
Site_Brain             0.85       0.78    0.81      134     
Site_Breast            0.89       0.87    0.88      71      
Site_Liver             0.77       0.80    0.79      117     
Site_Lung              0.76       0.73    0.75      251     
Site_Lymph_Node        0.84       0.82    0.83      181     
Site_Other_Body_Part   0.70       0.66    0.68      808     
Smoking_Status         0.74       0.74    0.74      42      
Staging                0.71       0.77    0.74      124     
Targeted_Therapy       0.85       0.89    0.87      126     
Tumor_Finding          0.92       0.88    0.90      769     
Tumor_Size             0.84       0.83    0.84      180     
Unspecific_Therapy     0.77       0.71    0.74      104     
micro-avg              0.82       0.81    0.81      11447   
macro-avg              0.80       0.79    0.79      11447   
weighted-avg           0.82       0.81    0.81      11447   
```
