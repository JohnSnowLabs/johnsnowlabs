---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.1.2
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_1_2
key: docs-licensed-release-notes
modify_date: 2023-10-17
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.1.2

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with a new parameter to AssertionDLModel for renaming assertion labels, a new parameter to DeIdentification for obfuscating ages based on the HIPAA Privacy Rule, enhanced cloud support for ContextualParser, as well as 22 new clinical pretrained models and pipelines**.

+ 13 new augmented NER models by leveraging the capabilities of the `LangTest` library to boost their robustness significantly
+ 3 new clinical NER models for extracting clinical entities in the Arabic, Finnish, and Bulgarian languages
+ 3 new multi-label text classification for respiratory disease, heart disease, and mental disorder
+ 3 New `ChunkMapper` models to map UMLS codes to their MeSH, SNOMED, and ICD-10-CM codes.
+ A new parameter to `AssertionDLModel` to rename the assertion labels
+ A new parameter to `DeIdentification` to obfuscate ages based on HIPAA (Health Insurance Portability and Accountability Act) Privacy Rule
+ Enhanced cloud support for `ContextualParser` with `setJsonPath` and `setDictionary` parameters
+ New features to the SparkNLP Healthcare CMS-HCC Risk-Adjustment module
+ New functionalities for the `OCR Utility Module`
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of SparkNLP for Healthcare
    - The issue with pretrained models that included the `ChunkConverter()` when loading them locally using `from_disk()` has been resolved.
    - The incorrect exception message in `ocr_entity_processor()` has been corrected
    - Resolved the problem with day-shifting in `DeIdentification`, specifically related to masking \<AGE> when using the setAgeRange feature.
+ New and updated demos
  - New [LANGTEST NER](https://demo.johnsnowlabs.com/healthcare/LANGTEST_NER/) for the most popular clinical NER models
  - New [Date Shifting and Date Normalization Demo](https://demo.johnsnowlabs.com/healthcare/DATE_SHIFTING_AND_NORMALIZATION/) demonstrates the most popular deidentification date operation
  - New [Respiratory Disease Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPIRATORY/) with new `multiclassifierdl_respiratory_disease` model
  - New [Mental Disorder demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_MENTAL_DISORDER/) with new `multiclassifierdl_mental_disorder` model
  - New [Heart Disease demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_HEART_DISEASE/) with new `multiclassifierdl_heart_disease` model
  - New [Abbreviation Mapper demo](https://demo.johnsnowlabs.com/healthcare/ABBREVIATION_MAPPER/) for the most popular MAPPER models
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined healthcare-related natural language data analysis.

</div><div class="h3-box" markdown="1">



#### 13 New Augmented NER Models by Leveraging the Capabilities of the LangTest Library to Boost Their Robustness Significantly

| Model Name               |   Predicted Entities        |
|--------------------------|-----------------------------|
| [`ner_biomarker_langtest`](https://nlp.johnsnowlabs.com/2023/10/10/ner_biomarker_langtest_en.html)             |  `Oncogenes`, `Tumor_Finding`, `ResponseToTreatment`, `Biomarker`, `HormonalTherapy`, `Staging`, `Drug`, `CancerDx`, `Radiotherapy`, `CancerSurgery`, `TargetedTherapy`, `CancerModifier`, `Biomarker_Measurement`, `Metastasis`, `Chemotherapy`, `Test`, `Dosage`, `Test_Result`, `Immunotherapy`...|
| [`ner_bionlp_langtest`](https://nlp.johnsnowlabs.com/2023/10/10/ner_bionlp_langtest_en.html)             |  `Amino_acid`, `Anatomical_system`, `Cancer`, `Cell`, `Cellular_component`, `Developing_anatomical_Structure`, `Gene_or_gene_product`, `Immaterial_anatomical_entity`, `Multi-tissue_structure`, `Organ`, `Organism`, `Organism_subdivision`, `Simple_chemical`, `Tissue` |
| [`ner_clinical_large_langtest`](https://nlp.johnsnowlabs.com/2023/10/10/ner_clinical_large_langtest_en.html)             | `PROBLEM`, `TEST`, `TREATMENT` |
| [`ner_living_species_langtest`](https://nlp.johnsnowlabs.com/2023/10/10/ner_living_species_langtest_en.html)             | `HUMAN`, `SPECIES` |
| [`ner_vop_langtest`](https://nlp.johnsnowlabs.com/2023/10/10/ner_vop_langtest_en.html)             | `Gender`, `Employment`, `Age`, `Substance`, `Form`, `PsychologicalCondition`, `Vaccine`, `Drug`, `DateTime`, `ClinicalDept`, `Test`, `AdmissionDischarge`, `Disease`,  `Dosage`, `Duration`, `RelationshipStatus`, `Symptom`, `Procedure`, `HealthStatus`, `InjuryOrPoisoning`, `Modifier`, `Treatment`,  |
| [`ner_chemprot_clinical_langtest`](https://nlp.johnsnowlabs.com/2023/10/12/ner_chemprot_clinical_langtest_en.html)             | `CHEMICAL`, `GENE-Y`, `GENE-N` |
| [`ner_bacterial_species_langtest`](https://nlp.johnsnowlabs.com/2023/10/15/ner_bacterial_species_langtest_en.html) | `SPECIES` |
| [`ner_cellular_langtest`](https://nlp.johnsnowlabs.com/2023/10/15/ner_cellular_langtest_en.html) | `DNA`, `Cell_type`, `Cell_line`, `RNA`, `Protein` |
| [`ner_deid_enriched_langtest`](https://nlp.johnsnowlabs.com/2023/10/15/ner_deid_enriched_langtest_en.html) | `AGE`, `CITY`, `COUNTRY`, `DATE`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `PROFESSION`, `STATE`, `STREET`, `USERNAME`, `ZIP` |
| [`ner_deid_large_langtest`](https://nlp.johnsnowlabs.com/2023/10/15/ner_deid_large_langtest_en.html) | `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION` |
| [`ner_diseases_langtest`](https://nlp.johnsnowlabs.com/2023/10/17/ner_diseases_langtest_en.html) | `Disease` |
| [`ner_oncology_langtest`](https://nlp.johnsnowlabs.com/2023/10/15/ner_oncology_langtest_en.html) | `Staging`, `Cancer_Score`, `Tumor_Finding`, `Site_Lymph_Node`, `Response_To_Treatment`, `Smoking_Status`, `Tumor_Size`, `Cycle_Count`, `Adenopathy` `Biomarker_Result`,  `Chemotherapy`, `Cancer_Surgery`, `Line_Of_Therapy`, `Pathology_Result`, `Hormonal_Therapy`, `Biomarker`, `Immunotherapy`, `Metastasis`, `Cancer_Dx`, `Grade`... |
| [`ner_deid_generic_augmented_allUpperCased_langtest`](https://nlp.johnsnowlabs.com/2023/10/16/ner_deid_generic_augmented_allUpperCased_langtest_en.html) | `DATE`, `NAME`, `LOCATION`, `PROFESSION`, `CONTACT`, `AGE`, `ID` |


- The table below shows the robustness of overall test results for 13 different models.

| model names        | original robustness  |  new robustness  |
|-------------------------------------------|---------|--------|
| ner_biomarker_langtest                    | 45.49%  | 78.84% |
| ner_bionlp_langtest                       | 49.56%  | 76.70% |
| ner_clinical_large_langtest               | 50.66%  | 77.64% |
| ner_living_species_langtest               | 68.42%  | 90.86% |
| ner_vop_langtest                          | 50.74%  | 78.21% |
| ner_chemprot_clinical_langtest            | 49.53%  | 81.74% |
| ner_bacterial_species_langtest            | 76.04%  | 90.65% |
| ner_cellular_langtest                     | 33.74%  | 77.52% |
| ner_deid_enriched_langtest                | 94.78%  | 97.48% |
| ner_deid_large_langtest                   | 86.98%  | 95.22% |
| ner_diseases_langtest                     | 60.01%  | 86.03% |
| ner_oncology_langtest                     | 52.13%  | 79.73% |
| ner_deid_generic_augmented_allUpperCased_langtest  | 94.73%  | 97.60% |


*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_clinical_large_langtest", "en", "clinical/models") \
     .setInputCols(["sentence", "token", "embeddings"]) \
     .setOutputCol("ner")

text= """She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation. Physical examination on presentation was significant for dry oral mucosa; significantly, her abdominal examination was benign with no tenderness, guarding, or rigidity. """
```

*Result*:

```bash
+-------------------------------------+---------+
|chunk                                |ner_label|
+-------------------------------------+---------+
|metformin                            |TREATMENT|
|glipizide                            |TREATMENT|
|dapagliflozin                        |TREATMENT|
|T2DM                                 |PROBLEM  |
|atorvastatin                         |TREATMENT|
|gemfibrozil                          |TREATMENT|
|HTG                                  |PROBLEM  |
|dapagliflozin                        |TREATMENT|
|Physical examination                 |TEST     |
|dry oral mucosa                      |PROBLEM  |
|her abdominal examination            |TEST     |
|tenderness                           |PROBLEM  |
|guarding                             |PROBLEM  |
|rigidity                             |PROBLEM  |
+-------------------------------------+---------+
```


</div><div class="h3-box" markdown="1">

#### 3 New Clinical NER Models for Extracting Clinical Entities in the Arabic, Finnish, and Bulgarian Languages

3 new Clinical NER models provide valuable tools for processing and analyzing multi-language clinical texts. They assist in automating the extraction of important clinical information, facilitating research, medical documentation, and other applications within the multi-language healthcare domain.


| Model Name         | Predicted Entities           | Language |
|--------------------|------------------------------|----------|
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/10/06/ner_clinical_ar.html)   | `PROBLEM` `TEST` `TREATMENT` | ar |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/10/16/ner_clinical_bg.html)   | `PROBLEM` `TEST` `TREATMENT` | bg |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/10/16/ner_clinical_fi.html)   | `PROBLEM` `TEST` `TREATMENT` | fi |

*Example*:

```python
embeddings = WordEmbeddingsModel.pretrained("arabic_w2v_cc_300d", "ar")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "ar", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_text = """تاريخ الزيارة: 25 سبتمبر 2023 - المريضة: فاطمة علي - العمر: 48 سنة - الجنس: أنثى - المشاكل: 1. مشكل ارتفاع في مستويات في الدم 2. ارتفاع مستوى الكوليستيرول في الدم 3. اضطراب في وظائف الغدة الدرقية - الفحوصات: 1. قياس مستوى السكر في الدم 2. تحليل مستوى الكوليستيرول في الدم 3. اختبار وظائف الغدة الدرقية - العلاجات: 1. وصف دواء لمراقبة وتنظيم مستوى السكر في الدم (ميتفورمين 500 ملغ يوميا) 2. وصف دواء لتخفيض مستوى الكوليستيرول (ستاتين 20 ملغ يوميا) 3. وصف العلاج اللازم لتحسين وظائف الغدة الدرقية (ليفوتيروكسين 50 ميكروغرام يوميا)، بالإضافة إلى توجيهات بشأن نمط حياة صحي تتضمن اتباع نظام غذائي مناسب وممارسة الرياضة بانتظام."""
```

*Result*:
|chunk                                               |ner_label|
|----------------------------------------------------|-------------------|
|مشكل ارتفاع في مستويات في الدم                 |PROBLEM  |
|ارتفاع مستوى الكوليستيرول في الدم              |PROBLEM  |
|اضطراب في وظائف الغدة الدرقية                |PROBLEM  |
|قياس مستوى السكر في الدم                         |TEST     |
|تحليل مستوى الكوليستيرول في الدم               |TEST     |
|اختبار وظائف الغدة الدرقية                         |TEST     |
|ميتفورمين                                              |TREATMENT|
|ليفوتيروكسين                                          |TREATMENT|
|نظام غذائي مناسب                                   |TREATMENT|


</div><div class="h3-box" markdown="1">

#### 3 New Multilabel Text Classification For Respiratory Disease, Heart Disease, and Mental Disorder

The PHS-BERT Respiratory Disease Classifier Model is a specialized text classification system, engineered to accurately identify and categorize textual mentions of four prominent respiratory diseases: Asthma, Chronic Obstructive Pulmonary Disease (COPD), Emphysema, and Chronic bronchitis


|Model|Description|Predicted Labels|
|-|-|-|
|[`multiclassifierdl_respiratory_disease`](https://nlp.johnsnowlabs.com/2023/10/03/multiclassifierdl_respiratory_disease_en.html) |This model identifies and categorizes textual mentions of four prominent respiratory diseases: Asthma, Chronic Obstructive Pulmonary Disease (COPD), Emphysema, and Chronic bronchitis.| `Astham`, `COPD`, `Emphysema`, `Chronic bronchitis`, `Other/Unknown`, `No` |
|[`multiclassifierdl_heart_disease`](https://nlp.johnsnowlabs.com/2023/10/17/multiclassifierdl_heart_disease_en.html)|This model identifies and categorize textual mentions of three prominent cardiovascular diseases: Hypertension, Coronary Artery Disease, and Myocardial Infarction.| `Hypertension`, `MI`, `CAD`, `Other/Unknown`, `No` |
|[`multiclassifierdl_mental_disorder`](https://nlp.johnsnowlabs.com/2023/10/17/multiclassifierdl_mental_disorder_en.html)|This model classifies text based on the following mental disorders. (Schizophrenia, Depression, Bipolar disorder, Anxiety disorder).| `Anxiety Disorder`, `No`, `Schizophrenia`, `Depression`, `Other/Unknown` |

*Example*:

```python
multiclassifierdl = MultiClassifierDLModel.pretrained("multiclassifierdl_respiratory_disease", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("predicted_class")

text = [
 ["""The patient, experiencing recurrent episodes of wheezing and shortness of breath, has been diagnosed with Asthma and is advised to use a daily controller inhaler to manage the symptoms."""],
    ["""Due to the patient's long history of tobacco use and persistent cough producing large amounts of sputum, a diagnosis of Chronic Obstructive Pulmonary Disease (COPD) has been established, necessitating bronchodilators for management."""],
    ["""The presence of dyspnea, chronic cough, and a history of smoking have led to the diagnosis of Emphysema for the patient, warranting the initiation of long-term oxygen therapy."""],
    ["""The patient has been diagnosed with Chronic Bronchitis following the prolonged occurrence of cough and mucus production, and is recommended to undergo pulmonary rehabilitation and pharmacotherapy."""],
    ["""With a clinical presentation of persistent wheezing and respiratory discomfort, the patient has been conclusively diagnosed with Asthma, necessitating immediate commencement of anti-inflammatory medications."""],
    ["""Manifesting prolonged symptoms of breathlessness and a productive cough, the patient has received a diagnosis of Chronic Obstructive Pulmonary Disease (COPD), and a comprehensive treatment involving bronchodilators and lifestyle modifications has been recommended."""],
    ]
```

*Result*:

|                   text  |                               result|
|-------------------------|-------------------------------------|
|The patient, experiencing recurrent episodes of wheezing and shortness of breath, has been diagn...|         Asthma, Chronic bronchitis|
|Due to the patient s long history of tobacco use and persistent cough producing large amounts of...|           COPD, Chronic bronchitis|
|The presence of dyspnea, chronic cough, and a history of smoking have led to the diagnosis of Em...|Emphysema, COPD, Chronic bronchitis|
|The patient has been diagnosed with Chronic Bronchitis following the prolonged occurrence of cou...|                 Chronic bronchitis|
|With a clinical presentation of persistent wheezing and respiratory discomfort, the patient has ...|              Asthma, Other/Unknown|
|Manifesting prolonged symptoms of breathlessness and a productive cough, the patient has receive...|           COPD, Chronic bronchitis|

Please see the  [Respiratory Disease](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPIRATORY/), [Heart Disease](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_HEART_DISEASE/), and 
[Mental Disorder](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_MENTAL_DISORDER/) demos






</div><div class="h3-box" markdown="1">

#### 3 New `ChunkMapper` Models to Map UMLS Codes to Their MeSH, SNOMED, and ICD-10-CM Codes.

We have introduced 3 new `ChunkMapper` models to map UMLS codes to their MeSH, SNOMED, and ICD-10-CM codes.

| Model Name          | Relations    | Description                        |
|---------------------|--------------|------------------------------------|
| [umls_mesh_mapper](https://nlp.johnsnowlabs.com/2023/10/17/umls_mesh_mapper_en.html)    | mesh_code    | Maps UMLS codes to MeSH codes      |
| [umls_snomed_mapper](https://nlp.johnsnowlabs.com/2023/10/17/umls_snomed_mapper_en.html)  | snomed_code  | Maps UMLS codes to SNOMED codes    |
| [umls_icd10cm_mapper](https://nlp.johnsnowlabs.com/2023/10/17/umls_icd10cm_mapper_en.html) | icd10cm_code | Maps UMLS codes to ICD-10-CM codes |

*Example*:

```python
chunkerMapper = DocMapperModel.pretrained("umls_icd10cm_mapper", "en", "clinical/models")\
      .setInputCols(["document"])\
      .setOutputCol("mappings")\
      .setRels(["icd10cm_code"])

text= """["C0000744"], ["C2875181"]"""
```

*Result*:

```bash
+---------+------------+------------+
|umls_code|icd10cm_code|relation    |
+---------+------------+------------+
|C0000744 |E786        |icd10cm_code|
|C2875181 |G4381       |icd10cm_code|
+---------+------------+------------+
```


</div><div class="h3-box" markdown="1">

#### New Parameter to `AssertionDLModel` to Rename the Assertion Labels

We have introduced a new parameter called `ReplaceLabels(dict[str, str])` to `AssertionDLModel`.
This parameter enables users to customize the assertion labels.

*Example*:

```python
clinical_assertion = AssertionDLModel.pretrained("assertion_dl_large", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion") \
    .setReplaceLabels({"PRESENT": "available", "absent": "none", "Conditional": "Optional"})

text= """Patient with severe fever and sore throat. He shows no stomach pain and he maintained on an epidural and PCA
for pain control. He also became short of breath with climbing a flight of stairs."""
```

*Result*:

| chunks          | entities   | assertion                    |
|:----------------|:-----------|:-----------------------------|
| severe fever    | PROBLEM    | available                    |
| sore throat     | PROBLEM    | available                    |
| stomach pain    | PROBLEM    | none                         |
| an epidural     | TREATMENT  | available                    |
| PCA             | TREATMENT  | available                    |
| pain control    | PROBLEM    | hypothetical                 |
| short of breath | PROBLEM    | Optional                     |

Please see [Clinical Assertion Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb) for more information 



</div><div class="h3-box" markdown="1">

#### A New Parameter to `DeIdentification` to Obfuscate Ages Based on HIPAA (Health Insurance Portability and Accountability Act) Privacy Rule

We have introduced a new parameter called `AgeRangesByHipaa()` which determines whether to obfuscate ages in compliance with the HIPAA (Health Insurance Portability and Accountability Act) Privacy Rule.

The HIPAA Privacy Rule mandates that ages of patients older than 90 years must be obfuscated,
while the age for patients 90 years or younger can remain unchanged.
If the parameter is set as `True`, age entities larger than 90 will be obfuscated as per HIPAA Privacy Rule, and the others will remain unchanged.
If the parameter is set as `False`, `AgeRanges` parameter is considered for obfuscation. The default value of the `AgeRangesByHipaa` is `False`.

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "age_chunk"]) \
    .setOutputCol("obfuscation") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker") \
    .setAgeRangesByHipaa(True)

dates = [
  '1 year old baby',
  '4 year old kids',
  'Record date: 2093-01-13, Age: 25',
  'A 92 year old female with',
  'Patient is 108 years-old',
  'He is 120 years-old male',
]
```

*Result*:

| text                             |   age_chunk | obfuscation                      |
|:---------------------------------|------------:|:---------------------------------|
| 1 year old baby                  |           1 | 1 year old baby                  |
| 4 year old kids                  |           4 | 4 year old kids                  |
| Record date: 2093-01-13, Age: 25 |          25 | Record date: 2093-03-10, Age: 25 |
| A 92 year old female with        |          92 | A 99 year old female with        |
| Patient is 108 years-old         |         108 | Patient is 119 years-old         |
| He is 120 years-old male         |         120 | He is 140 years-old male         |


Please see [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) for more information 



</div><div class="h3-box" markdown="1">

#### Enhanced Cloud Support for ContextualParser with `setJsonPath` and `setDictionary`

Explore the new capabilities of the ContextualParserApproach, featuring extended cloud support for path configuration using setJsonPath and setDictionary. This example demonstrates how to leverage these enhancements to improve entity recognition in your NLP projects, providing flexibility and scalability with cloud-based resources.

*Example*:

```python
contextual_parser = ContextualParserApproach() \
    .setInputCols(["sentence", "token"])\
    .setOutputCol("entity")\
    .setCaseSensitive(True)\
    .setJsonPath("s3a://YOUR_S3_BUCKET/data/cities.json")\
    .setDictionary("s3a://YOUR_S3_BUCKET/data/cities.tsv", 
                   read_as = "SPARK",
                   options={"orientation": "vertical",
                            "format": "text"})
```


</div><div class="h3-box" markdown="1">

#### New Features to the SparkNLP Healthcare CMS-HCC Risk-Adjustment Module

We  are introducing 3 new functions SparkNLP Healthcare CMS-HCC Risk-Adjustment Module.

- `HCC_from_ICD`: A mapping of ICD-10 codes to their corresponding RXHCC or HCC codes. Retrieves the mapping of Risk Adjustment Hierarchical Condition Categories (RXHCC) or Hierarchical Condition Categories (HCC) based on a list of International Classification of Diseases, 10th Revision (ICD-10) codes for a specific measurement year. This method allows for the retrieval of RXHCC or HCC associated with the provided ICD-10 codes for a particular year.

*Example*:

```python
from sparknlp_jsl.utils.risk_adjustment_utils import RiskAdjustmentUtil

RiskAdjustmentUtil.HCC_from_ICD("hcc", "ESRDv21", 2019, ["A021", "I209", "E103559"])

OUTPUT:{'A021': ['HCC2'], 'I209': ['HCC88'], 'E103559': ['HCC18', 'HCC122']}
```

- `HCC_labels`: A mapping of RXHCCs and HCCs to their respective medical descriptions. Retrieves the medical descriptions associated with a given list of Risk Adjustment Hierarchical Condition Categories (RXHCCs) and Hierarchical Condition Categories (HCCs) for a specified measurement year. This method allows for the retrieval of medical descriptions corresponding to the provided RXHCCs and HCCs for a particular year.

*Example*:

```python
from sparknlp_jsl.utils.risk_adjustment_utils import RiskAdjustmentUtil

RiskAdjustmentUtil.HCC_labels("hcc", "24", 2021, ["HCC1", "HCC37", "HCC321"])

OUTPUT:{'HCC1': 'HIV/AIDS'}
```

- `diff_between_HCCs`: Calculates the difference between two lists of Hierarchical Condition Categories (HCCs) or Risk Adjustment Hierarchical Condition Categories (RXHCCs) for a specific measurement year. This method identifies and categorizes the added, deleted, and upgraded HCCs between the "before_HCC_list" and "after_HCC_list" states. HCCs and RXHCCs evolve over time. New conditions emerge with age, causing additions and removals of CCs. Some CCs might escalate to higher levels of severity, representing an upgrade.

*Example*:

```python
from sparknlp_jsl.utils.risk_adjustment_utils import RiskAdjustmentUtil

RiskAdjustmentUtil.diff_between_HCCs("rxhcc", "08", 2023, ["RXHCC77", "RXHCC262"], ["RXHCC1", "RXHCC78", "RXHCC261"])

OUTPUT :{'added_list': ['RXHCC1', 'RXHCC78', 'RXHCC261'], 'deleted_list': ['RXHCC77']}
```


Please see [Calculate Medicare Risk Adjustment Score Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) for more information 


</div><div class="h3-box" markdown="1">

#### New Functionalities for the `OCR Utility Module`

Explore the latest enhancements in the OCR Utility Module, which now allow you to insert custom text onto colored bands using the `text_band` parameter. Customize your document annotations even further by configuring specific colors with RGB tuples through the `outline_color` parameter. Additionally, you can adjust the outline width for bounding boxes using the `outline_width` parameter. Elevate your OCR processing capabilities with these new functionalities.

- Introduced the option to configure a desired specific color using RGB tuples with the `outline_color` parameter for the bounding box style.

*Example*:

```python
path='content/*.pdf'
box = "bounding_box"

ocr_entity_processor(spark=spark,
                    file_path = path,
                    ner_pipeline = nlp_model,
                    chunk_col = "merged_chunk",
                    ...
                    label_color = "blue",
                    display_result = True,
                    outline_color = (155,0,0)) ##Takes Tuple
```

- Users can now adjust the outline width of the bounding box style using the `outline_width` parameter.

*Example*:

```python
path='content/*.pdf'
box = "highlight"
ocr_entity_processor(spark=spark,
                    file_path = path,
                    ner_pipeline = nlp_model,
                    style = box,
                    ...
                    label_color = "red",
                    outline_width = 6 )  ## Width of the outline
```

Please see [Spark OCR Utility Module Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb) for more information 


</div><div class="h3-box" markdown="1">

#### Various Core Improvements; Bug Fixes, Enhanced Overall Robustness and Reliability of SparkNLP for Healthcare

- The issue with pretrained models that included the `ChunkConverter()` when loading them locally using `from_disk()` has been resolved.
- The incorrect exception message in `ocr_entity_processor()` has been corrected
- Resolved the problem with day-shifting in `DeIdentification`, specifically related to masking \<AGE> when using the setAgeRange feature.


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand


- New [LANGTEST NER](https://demo.johnsnowlabs.com/healthcare/LANGTEST_NER/) for the most popular clinical NER models
- New [Date Shifting and Date Normalization Demo](https://demo.johnsnowlabs.com/healthcare/DATE_SHIFTING_AND_NORMALIZATION/) demonstrates the most popular deidentification date operation
- New [Respiratory Disease Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_RESPIRATORY/) with new `multiclassifierdl_respiratory_disease` model
- New [Mental Disorder demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_MENTAL_DISORDER/) with new `multiclassifierdl_mental_disorder` model
- New [Heart Disease demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_HEART_DISEASE/) with new `multiclassifierdl_heart_disease` model
- New [Abbreviation Mapper demo](https://demo.johnsnowlabs.com/healthcare/ABBREVIATION_MAPPER/) for the most popular MAPPER models
- Updated [Spark OCR Utility Module Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb) with latest improvements
- [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) with new `setAgeRangesByHipaa` examples
- [Calculate Medicare Risk Adjustment Score Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb) with new Risk-Adjustment feature examples




</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.



+ `ner_clinical` -> `ar`
+ `ner_clinical` -> `bg`
+ `ner_clinical` -> `fi`
+ `multiclassifierdl_respiratory_disease`
+ `multiclassifierdl_mental_disorder`
+ `multiclassifierdl_heart_disease`
+ `ner_biomarker_langtest`
+ `ner_bionlp_langtest`
+ `ner_clinical_large_langtest`
+ `ner_living_species_langtest`
+ `ner_cellular_langtest`
+ `ner_vop_langtest`
+ `ner_chemprot_clinical_langtest`
+ `ner_bacterial_species_langtest`
+ `ner_deid_enriched_langtest`
+ `ner_deid_large_langtest`
+ `ner_diseases_langtest`
+ `ner_oncology_langtest`
+ `ner_deid_generic_augmented_allUpperCased_langtest`
+ `umls_mesh_mapper`
+ `umls_snomed_mapper`
+ `umls_icd10cm_mapper`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
