---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.0.1
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_0_1
key: docs-licensed-release-notes
modify_date: 2023-08-02
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.0.1

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first NER models that are augmented by LangTest library for robustness and bias as well as a support for RxHCC risk score calculation in latest versions**. 

+ Integrated the Risk Adjustment for Prescription Drug Hierarchical Condition Categories (RxHCC) model into our risk adjustment score calculation engine
+ Advanced entity detection for Section Headers and Diagnoses entities in clinical notes
+ Augmented NER models by leveraging the capabilities of the LangTest library
+ Enhanced Sentence Entity Resolver Models for associating clinical entities with LOINC
+ Strengthen the performance of assertion status detection by reinforcing it with entity type constraints
+ Entity blacklisting in `AssertionFilterer` to manage assertion status effectively
+ Enhanced `ChunkMergeApproach` and `ChunkFilterer` with case sensitivity settings
+ New feature for `ChunkMergeApproach` to enable filtering chunks according to confidence thresholds
+ Included sentence ID information in `Relation Extraction Model` metadata
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - Improved deidentification regex pattern for Romanian language
  - Fixed exploded sentences issue in `RelationExtractionDLModel`
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">


#### Integrated The Risk Adjustment For Prescription Drug Hierarchical Condition Categories (RxHCC) Model Into Our Risk Adjustment Score Calculation Engine

We have integrated the RxHCC into our existing risk adjustment score calculation module. This means more accurate and comprehensive risk adjustment scores, especially for patients whose healthcare costs are significantly influenced by prescription drug usage. This enhancement brings a holistic view of a patient's healthcare needs, further improving the precision of risk assessment.

We are pleased to introduce support for RxHCC risk score calculation in two new versions: v05 (applicable for 2020, 2021, 2022, and 2023) and v08 (applicable for 2022 and 2023). To utilize these versions with specific years, simply use the following formats: `profileRxHCCV05YXX` for v05 and `profileRxHCCV08YXX` for v08.

*Example*:

Input Data Frame:


|      filename|Age|                              icd10_code|                  Extracted_Entities_vs_ICD_Codes|Gender|   eligibility|orec|    esrd|
|--------------|---|----------------------------------------|-------------------------------------------------|------|--------------|----|--------|
|patient_01.txt| 66|C49.9, J18.9, C49.9, D61.81, I26, M06.9 | {leiomyosarcoma, C49.9}, {pneumonia, J18.9}, ...|     F|  CE_NoLowAged|   1|   false|
|patient_02.txt| 59|                   C50.92, P61.4, C80.1 | {breast cancer, C50.92}, {dysplasia, P61.4}, ...|     F|CE_NoLowNoAged|   0|    true|


```python
# v08 year 2023
from sparknlp_jsl.functions import profileRxHCCV08Y23

df = df.withColumn("rxhcc_profile", profileRxHCCV08Y23(df.icd10_code, df.Age, df.Gender, df.eligibility, df.orec, df.esrd))

df = df.withColumn("rxhcc_profile", F.from_json(F.col("rxhcc_profile"), schema))
df = df.withColumn("risk_score", df.rxhcc_profile.getItem("risk_score"))\
       .withColumn("parameters", df.rxhcc_profile.getItem("parameters"))\
       .withColumn("details", df.rxhcc_profile.getItem("details"))\
```

*Results (V08-Y23)*:

|      filename|Age|                             icd10_code|                  Extracted_Entities_vs_ICD_Codes|Gender|   eligibility|orec|    esrd|                                     rxhcc_profile|risk_score|                       parameters|                     details|
|--------------|---|---------------------------------------|-------------------------------------------------|------|--------------|----|--------|--------------------------------------------------|----------|---------------------------------|----------------------------|
|patient_01.txt| 66|C49.9, J18.9, C49.9, D61.81, I26, M06.9| {leiomyosarcoma, C49.9}, {pneumonia, J18.9}, ...|     F|  CE_NoLowAged|   1|   false|{0.575, null, {"elig":"CE_NoLowAged","age":66, ...|     0.575|{"elig":"CE_NoLowAged","age": ...|{"Rx_CE_NoLowAged_F65_69"...|
|patient_02.txt| 59|                   C50.92, P61.4, C80.1| {breast cancer, C50.92}, {dysplasia, P61.4}, ...|     F|CE_NoLowNoAged|   0|    true|{0.367, null, {"elig":"CE_NoLowNoAged","age":59...|     0.367|{"elig":"CE_NoLowNoAged","age"...|{ Rx_CE_NoLowNoAged_F55_5...|

</div><div class="h3-box" markdown="1">
  
#### Advanced Entity Detection For Section Headers And Diagnoses Entities In Clinical Notes

We have a new state-of-the-art NER model that is specifically designed to extract vital data from clinical documents, focusing on two key aspects: *Section Headers* and *Diagnoses*. By accurately identifying and labeling various medical conditions like heart disease, diabetes, and Alzheimer's disease, this model provides unparalleled insights into diagnosis and treatment trends.

*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_section_header_diagnosis", "en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\
    .setLabelCasing("upper")

text = """
Medical History:
Patient has a history of Chronic respiratory disease.
Clinical History:
Patient presented with shortness of breath and chest pain.
Chief Complaint:
Patient complained of chest pain and difficulty breathing.
History of Present Illness:
Patient has been experiencing chest pain and shortness of breath for the past week. Symptoms were relieved by medication at first but became worse over time.
Past Medical History:
Patient has a history of Asthma and was previously diagnosed with Bronchitis.
Medications:
Patient is currently taking Albuterol, Singulair, and Advair for respiratory issues.
Allergies:
Patient has a documented allergy to Penicillin.
"""

```


*Result*:

chunks                      | entities                    | confidence
----------------------------|-----------------------------|----------
Medical History             | MEDICAL_HISTORY_HEADER      | 0.81
Chronic respiratory disease | RESPIRATORY_DISEASE         | 0.74
Clinical History            | CLINICAL_HISTORY_HEADER     | 0.77
Chief Complaint             | CHIEF_COMPLAINT_HEADER      | 0.85
History of Present Illness  | HISTORY_PRES_ILNESS_HEADER  | 0.99
Past Medical History        | MEDICAL_HISTORY_HEADER      | 0.71
Asthma                      | RESPIRATORY_DISEASE         | 0.99
Bronchitis                  | RESPIRATORY_DISEASE         | 0.84
Medications                 | MEDICATIONS_HEADER          | 0.99
Allergies                   | ALLERGIES_HEADER            | 0.99



Please check: [ner_section_header_diagnosis](https://nlp.johnsnowlabs.com/2023/07/26/ner_section_header_diagnosis_en.html) model card for more information.


</div><div class="h3-box" markdown="1">

#### Augmented NER Models Leveraging LangTest Library Capabilities

Newly introduced augmented NER models, namely [`ner_posology_langtest`](https://nlp.johnsnowlabs.com/2023/07/28/ner_posology_langtest_en.html), [`ner_jsl_langtest`](https://nlp.johnsnowlabs.com/2023/07/31/ner_jsl_langtest_en.html), [`ner_ade_clinical_langtest`](https://nlp.johnsnowlabs.com/2023/07/31/ner_ade_clinical_langtest_en.html), and [`ner_sdoh_langtest`](https://nlp.johnsnowlabs.com/2023/07/31/ner_sdoh_langtest_en.html), are powered by the innovative [`LangTest`](https://langtest.org/) library. This cutting-edge NLP toolkit is at the forefront of language processing advancements, incorporating state-of-the-art techniques and algorithms to enhance the capabilities of our models significantly.


*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_sdoh_langtest", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")


text = """Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave."""

```


*Result*:

|               chunk|begin|end|          ner_label|
|--------------------|-----|---|-------------------|
|        55 years old|    9| 20|                Age|
|            New York|   33| 40|  Geographic_Entity|
|            divorced|   45| 52|     Marital_Status|
|    Mexcian American|   54| 69|     Race_Ethnicity|
|               woman|   71| 75|             Gender|
|  financial problems|   82| 99|   Financial_Status|
|                 She|  102|104|             Gender|
|             Spanish|  113|119|           Language|
|          Portuguese|  125|134|           Language|
|                 She|  137|139|             Gender|
|           apartment|  153|161|            Housing|
|                 She|  164|166|             Gender|
|            diabetes|  193|200|      Other_Disease|
|    hospitalizations|  268|283|Other_SDoH_Keywords|
|  cleaning assistant|  342|359|         Employment|
|access health ins...|  372|394|   Insurance_Status|



</div><div class="h3-box" markdown="1">
  
#### Enhanced Sentence Entity Resolver Models For Associating Clinical Entities With LOINC

Introducing the new `sbiobertresolve_loinc_numeric` model and improving the `sbiobertresolve_loinc_augmented` model, both offering enhanced accuracy for mapping medical laboratory observations and clinical measurements to their corresponding Logical Observation Identifiers Names and Codes (LOINC). The `sbiobertresolve_loinc_numeric` model is specialized in numeric LOINC codes, as it was trained without the inclusion of LOINC "Document Ontology" codes starting with the letter "L". On the other hand, the `sbiobertresolve_loinc_augmented` model offers broader functionality, capable of returning both numeric and document ontology codes for enhanced versatility.

*Example*:

```python
resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_loinc_numeric","en", "clinical/models") \
  .setInputCols(["sbert_embeddings"]) \
  .setOutputCol("loinc_code")\
  .setDistanceFunction("EUCLIDEAN")

sample_text = "The patient is a 22-year-old female with a history of obesity. She has a Body mass index (BMI) of 33.5 kg/m2, aspartate aminotransferase 64, and alanine aminotransferase 126."
```  

*Results:*

|                     chunk|entity|loinc_code|                     all_codes|                                                                        resolutions|
|--------------------------|------|----------|------------------------------|-----------------------------------------------------------------------------------|
|                       BMI|  Test|   39156-5| 39156-5, 89270-3, 100847-3...| [BMI [Body mass index], BMI Est [Body mass index], BldA [Gas & ammonia panel], ...|
|aspartate aminotransferase|  Test|   14409-7| 14409-7, 1916-6, 16324-6, ...| [Aspartate aminotransferase [Aspartate aminotransferase], Aspartate aminotransf...|
|  alanine aminotransferase|  Test|   16324-6| 16324-6, 16325-3, 1916-6, ...| [Alanine aminotransferase [Alanine aminotransferase], Alanine aminotransferase/...|





</div><div class="h3-box" markdown="1">

#### Strengthen The Performance Of Assertion Status Detection By Reinforcing With Entity Type Constraints

Introducing the latest enhancements to our `AssertionDLModel` - the `setEntityAssertion` and `setEntityAssertionCaseSensitive` parameters. Now, you can effortlessly constrain assertions based on specific entity types using a convenient dictionary format: `{"entity": [assertion_label1, assertion_label2, .. assertion_labelN]}`. When an entity is not found in the dictionary, no constraints are applied, ensuring flexibility in your data processing. With the `setEntityAssertionCaseSensitive` parameter, you can control the case sensitivity for both entities and assertion labels. Unleash the full potential of your NLP model with these cutting-edge additions to the AssertionDLModel.

*Example*:

```python
clinical_assertion = AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")\
    .setEntityAssertionCaseSensitive(False)\
    .setEntityAssertion({
        "PROBLEM": ["hypothetical", "absent"],
        "treAtment": ["present"],
        "TEST": ["POssible"],
    })

text = '''
A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus (T2DM), one prior episode of HTG-induced pancreatitis three years prior to presentation, and associated with an acute hepatitis, presented with a one-week history of polyuria, poor appetite, and vomiting.
She was on metformin, glipizide, and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG. She had been on dapagliflozin for six months at the time of presentation.
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness, guarding, or rigidity. Pertinent laboratory findings on admission were: serum glucose 111 mg/dl,  creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27.
'''

```


*Result*:

|idx|chunks         |entities  |assertion   |confidence|
|---|---------------|----------|------------|----|
| 0 | metformin     |TREATMENT |Present     |0.54|
| 1 | glipizide     |TREATMENT |Present     |0.99|
| 2 | dapagliflozin |TREATMENT |Present     |1.0|
| 3 | HTG           |PROBLEM   |Hypothetical|1.0|
| 4 | Physical examination|TEST|Possible    |0.94|
| 5 | tenderness    |PROBLEM   |Absent      |1.0|
| 6 | guarding      |PROBLEM   |Absent      |1.0|
| 7 | rigidity      |PROBLEM   |Hypothetical|0.99|



</div><div class="h3-box" markdown="1">

#### Entity Blacklisting In `AssertionFilterer` For Effective Assertion Status Management

With the `setBlackList` option in the `AssertionFilterer` annotator, you can now blacklist specific entities based on their assertion labels.

*Example*:

```python
clinical_assertion = AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")


assertion_filterer = AssertionFilterer()\
    .setInputCols("sentence","ner_chunk","assertion")\
    .setOutputCol("assertion_filtered")\
    .setBlackList(["Hypothetical"])\

text = """Patient has a headache for the last 2 weeks, needs to get a head CT, and appears anxious when she walks fast. No alopecia and pain noted"""

```

*Without Filtering Results*:

|   | chunks     | entities| assertion    |confidence|
|--:|:-----------|:--------|:-------------|---------:|
| 0 | a headache | PROBLEM | Present      |    1    |
| 1 | a head CT  | TEST    | Hypothetical |    1    |
| 2 | anxious    | PROBLEM | SomeoneElse  |    0.77 |
| 3 | alopecia   | PROBLEM | Hypothetical |    0.97 |
| 4 | pain       | PROBLEM | Hypothetical |    0.99 |


*Filtered Results*:

|   | chunks     | entities| assertion   | confidence|
|--:|:-----------|:--------|:------------|---------:|
| 0 | a headache | PROBLEM | Present     |     0.97 |
| 1 | anxious    | PROBLEM | SomeoneElse |     0.99 |



</div><div class="h3-box" markdown="1">

#### Enhanced `ChunkMergeApproach` And `ChunkFilterer` With Case Sensitivity Settings

The `setCaseSensitive` parameter now applies to the whitelist and blacklist functionalities. As part of the enhancement, this parameter has been included in the filtering feature, which serves as a superclass for, `ChunkFilterer` and `ChunkMergeApproach`. With this update, the caseSensitive setting can be conveniently utilized across these classes, offering improved control and consistency in the filtering process.

*Example*:

```python
posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

chunk_filterer = ChunkFilterer()\
    .setInputCols("sentence","ner_chunk")\
    .setOutputCol("chunk_filtered")\
    .setCriteria("isin")\
    .setWhiteList(['ADVIL','Metformin', 'Insulin Lispro'])\
    .setCaseSensitive(False)

text ="""The patient was prescribed 1 capsule of Advil for 5 days . She was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night , 12 units of insulin lispro with meals , metformin 1000 mg two times a day."""

```


*Result*:

```bash
# detected ner chunks
['1', 'capsule', 'Advil', 'for 5 days', '40 units', 'insulin glargine', 'at night', '12 units', 'insulin lispro', 'with meals', 'metformin', '1000 mg', 'two times a day']

# filtered ner chunks
['Advil', 'insulin lispro', 'metformin']
```

</div><div class="h3-box" markdown="1">

#### New Feature For `ChunkMergeApproach` To Enable Filtering Chunks According To Confidence Thresholds

We have added a new `setEntitiesConfidence` parameter to `ChunkMergeApproach` annotator that enables filtering the chunks according to the confidence thresholds. The only thing you need to do is provide a csv file that has the NER labels as keys and the confidence thresholds as values.

*Example*:

```python
conf_dict = """DRUG,0.99
FREQUENCY,0.99
DOSAGE,0.99
DURATION,0.99
STRENGTH,0.99
"""
with open('conf_dict.csv', 'w') as f:
    f.write(conf_dict)

chunk_merger = ChunkMergeApproach()\
    .setInputCols("posology_ner_chunk")\
    .setOutputCol('merged_ner_chunk')\
    .setEntitiesConfidenceResource("conf_dict.csv")


sample_text = 'The patient was prescribed 1 capsule of Advil for 5 days. He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night.'  
```

*Detected chunks*:

| chunks           | begin | end | entities  | confidence |
|:-----------------|------:|----:|:----------|-----------:|
| 1                |    27 |  27 | DOSAGE    |   0.99|
| capsule          |    29 |  35 | FORM      |   0.99|
| Advil            |    40 |  44 | DRUG      |   0.99|
| for 5 days       |    46 |  55 | DURATION  |   0.71|
| 40 units         |   125 | 132 | DOSAGE    |   0.85|
| insulin glargine |   137 | 152 | DRUG      |   0.83|
| at night         |   154 | 161 | FREQUENCY |   0.81|

*Filtered by confidence scores*:

| chunks  | begin | end | entities|confidence |
|:--------|------:|----:|:--------|----------:|
| 1       |    27 |  27 | DOSAGE  |    0.99 |
| capsule |    29 |  35 | FORM    |    0.99 |
| Advil   |    40 |  44 | DRUG    |    0.99 |



</div><div class="h3-box" markdown="1">


#### Included Sentence Id Information In `RelationExtractionModel` Metadata

Our Relation Extraction Models have been upgraded with the inclusion of `sentence` information in the metadata. This enhancement offers a deeper understanding of the extracted relationships and facilitates more precise analysis and interpretation of the results.

*Example*:

```python
re_dl_model = RelationExtractionDLModel.pretrained('redl_bodypart_direction_biobert', "en", "clinical/models")\
    .setInputCols(["re_ner_chunks", "sentences"]) \
    .setOutputCol("relations_dl")\
    .setPredictionThreshold(0.5)

text = '''MRI demonstrated infarction in the upper brain stem , and  right basil ganglia.
No neurologic deficits other than some numbness in his left hand.
there is a problem at right chest.'''
```

*Result*:

|idx|sentence|chunk1|entity1|chunk2         |entity2|relation|confidence|
|---|---|-------|-----------|---------------|------------------------------|---|---|
| 0 | 0 | upper | Direction | brain stem    | Internal_organ_or_component  | 1 |1.0 |
| 1 | 0 | upper | Direction | basil ganglia | Internal_organ_or_component  | 0 |0.99|
| 2 | 0 | right | Direction | basil ganglia | Internal_organ_or_component  | 1 |1.0 |
| 3 | 1 | left  | Direction | hand          | External_body_part_or_region | 1 |1.0 |
| 4 | 2 | right | Direction | chest         | External_body_part_or_region | 1 |1.0 |




</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Improved deidentification regex pattern for Romanian language
- Fixed exploded sentences issue in Relation Extraction DL (when `.setExplodeSentences(True)` is used in `SentenceDetector`, `RelationExtractionDLModel`'s relation output has only the `sentence#0` relations, other sentences' relations are not displayed.)


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- Updated [Clinical_Named_Entity_Recognition_Model](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb) notebook according to latest improvement in ChunkFilterer
- Updated [Clinical_Assertion_Model](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.Clinical_Assertion_Model.ipynb) notebook according to latest improvement in AssertionFilterer
- Updated [Clinical_NER_Chunk_Merger](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/7.Clinical_NER_Chunk_Merger.ipynb) notebook according to latest improvement in ChunkMergerApproach
- Updated [Clinical_Relation_Extraction](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/10.Clinical_Relation_Extraction.ipynb) notebook according to latest improvement in RelationExtractionModel's metadata
- Updated [Calculate_Medicare_Risk_Adjustment_Score](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb#scrollTo=L6qvg0X7BbnU) notebook according to latest improvement in HCC implementation

  
</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `ner_section_header_diagnosis`
+ `ner_posology_langtest`
+ `ner_jsl_langtest`
+ `ner_sdoh_langtest`
+ `ner_ade_clinical_langtest`
+ `sbiobertresolve_loinc_numeric`
+ `sbiobertresolve_loinc_augmented`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
