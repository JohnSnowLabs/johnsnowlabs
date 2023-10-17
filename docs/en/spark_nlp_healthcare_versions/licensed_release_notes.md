---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-09-26
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.1.1

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first clinical NER models in 5 new languages as well as 41 new clinical pretrained models and pipelines**. 

+ Introducing a new State-of-The-Art `Text2SQL` model supporting custom database schemas with single tables
+ 5 new clinical NER models for extracting clinical entities in the Japanese, Vietnamese, Norwegian, Danish and Swedish languages
+ 4 new Arabic De-Identification NER models 
+ 2 new classification models for social determinants of healthcare concepts within financial and food insecurity contexts
+ Introducing a new BioBERT-based drug adverse event classifier
+ 18 new augmented NER models by leveraging the capabilities of the `LangTest` library to boost their robustness significantly
+ 10 new NER-based pretrained pipelines, designed to streamline NER solutions with a single line of code
+ Leveraging the power of Spark NLP with AWS Glue and EMR with practical examples and support
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - ContextualParser metadata update: renaming `confidenceValue` to `confidence`
  - Updated English `profession` faker name list 
+ New and updated demos
  - New [Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER/) for the most popular clinical NER models 
  - New [ICD-10-CM Medicare Severity-Diagnosis Related Group Demo](https://demo.johnsnowlabs.com/healthcare/ICD10CM_MS_DRG_MAPPER/) with new icd10cm mapper and resolver models 
  - Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) with new 5 new Japanese, Vietnamese, Norwegian, Danish, and Swedish language models
  - Updated [Social Determinants Ner Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_NER/) with augmented SDOH NER models
  - Updated [Arabic Demographics NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/) with new `arabert` and `camelbert` models
  - Updated [Social Determinants Classification Generic Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/) updated financial and food insecurity models
  - Updated [Voice of Patient Demo](https://demo.johnsnowlabs.com/healthcare/VOP/) with new assertion models
  - Updated [Social Determinants of Health Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/) with new assertion models
  - Updated [VOP SIDE EFFECT CLASSIFICATION demo](https://demo.johnsnowlabs.com/healthcare/VOP_CLASSIFICATION_SIDE_EFFECT/) with new Adverse Drug Event models
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined healthcare-related natural language data analysis.

</div><div class="h3-box" markdown="1">


#### Introducing a New State-of-The-Art Text2SQL Model Supporting Custom Database Schemas with Single Tables

We are excited to introduce the new State-of-the-Art (SOTA) Large Language Model (LLM) designed to convert natural language questions into SQL queries, with support for custom database schemas containing single tables. This model has demonstrated superior performance compared to the current SOTA model (Defog's SQLCoder) by a margin of 6 points (**0.86 to 0.92**) when evaluated on a novel dataset that was not included in training (specifically tailored for the clinical domain). The model is obtained by finetuning an LLM on an augmented dataset containing schemas with single tables.

*Example*:

```python
query_schema = {
    "medical_treatment":         
        ["patient_id","patient_name","age","gender","diagnosis","treatment","doctor_name","hospital_name","admission_date","discharge_date"]
}

text2sql = Text2SQL.pretrained("text2sql_with_schema_single_table_augmented", "en", "clinical/models")\
    .setMaxNewTokens(200)\
    .setSchema(query_schema)\
    .setInputCols(["document"])\
    .setOutputCol("sql")

question = "What is the average age of male patients with 'Diabetes'?"
```

*Result*:

```bash
[SELECT AVG(age) FROM medical_treatment WHERE gender = 'male' AND diagnosis = 'diabetes']
```


please check: [Model Card](https://nlp.johnsnowlabs.com/2023/09/14/text2sql_with_schema_single_table_augmented_en.html) and [Text2SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) for more information



</div><div class="h3-box" markdown="1">



#### 5 New Clinical NER Models for Extracting Clinical Entities in the Japanese, Vietnamese, Norwegian, Danish, and Swedish Languages

5 new Clinical NER models provide valuable tools for processing and analyzing multi-language clinical texts. They assist in automating the extraction of important clinical information, facilitating research, medical documentation, and other applications within the multi-language healthcare domain.


| Model Name         | Predicted Entities           | Language |
|--------------------|------------------------------|----------|
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/09/20/ner_clinical_da.html)   | `PROBLEM` `TEST` `TREATMENT` | da |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/09/20/ner_clinical_sv.html)   | `PROBLEM` `TEST` `TREATMENT` | sv |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/09/20/ner_clinical_no.html)   | `PROBLEM` `TEST` `TREATMENT` | no |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/09/20/ner_clinical_ja.html)   | `PROBLEM` `TEST` `TREATMENT` | ja |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/09/20/ner_clinical_vi.html)   | `PROBLEM` `TEST` `TREATMENT` | vi |

*Example*:

```python

ner_model = MedicalNerModel.pretrained("ner_clinical", "sv", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_text = """Patienten hade inga ytterligare klagomål och den 10 mars 2012 var hans vita blodkroppar 2,3, neutrofiler 50%, band 2%, lymfocyter 5% , monocyter 40% och blaster 1%. instruktioner i 250 ml långsam IV-infusion över en timme."""

```

*Result*:

|chunk                |begin|end|ner_label|
|---------------------|-----|---|---------|
|ytterligare klagomål |20   |39 |PROBLEM  |
|hans vita blodkroppar|66   |86 |TEST     |
|neutrofiler          |93   |103|TEST     |
|band                 |110  |113|TEST     |
|lymfocyter           |119  |128|TEST     |
|monocyter            |135  |143|TEST     |
|blaster              |153  |159|TEST     |
|långsam IV-infusion  |188  |206|TREATMENT|


please check [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/)



</div><div class="h3-box" markdown="1">

#### 4 New Arabic De-Identification NER Models 

We're thrilled to present our newly integrated Arabic deidentification Named Entity Recognition (NER) models, featuring two diverse approaches. The first model provides granular entity recognition with 17 entities, while the other offers a more generic approach, identifying 8 entities with AraBERT Arabic Embeddings. These models are accompanied by corresponding pretrained pipelines that can be deployed in a streamlined one-liner format.

Designed explicitly for deidentification tasks in the Arabic language, these models leverage our proprietary dataset curation and specialized augmentation methods. This expansion broadens the linguistic scope of our toolset, underscoring our commitment to providing comprehensive solutions for global healthcare NLP needs.

| NER model                                                                 |            predicted entities             |
|---------------------------------------------------------------------------|-------------------------------------------|
| [`ner_deid_subentity_arabert`](https://nlp.johnsnowlabs.com/2023/09/16/ner_deid_subentity_arabert_en.html) | `PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE` |
| [`ner_deid_generic_arabert`](https://nlp.johnsnowlabs.com/2023/09/16/ner_deid_generic_arabert_en.html)     | `CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE` |
| [`ner_deid_subentity_camelbert`](https://nlp.johnsnowlabs.com/2023/09/22/ner_deid_subentity_camelbert_en.html) | `PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE` |
| [`ner_deid_generic_camelbert`](https://nlp.johnsnowlabs.com/2023/09/16/ner_deid_generic_camelbert_en.html)     | `CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE` |




*Example*:

```python

embeddings = BertEmbeddings.pretrained("bert_embeddings_bert_base_arabert","ar") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity_arabert", "ar", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

text = """
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948234 وبريده الإلكتروني
abcd@gmail.com.
"""
```

*Result*:


|chunk                          |ner_label|
|-------------------------------:|:---------|
|الدكتور محمد المريض           |DOCTOR   |
|55 سنة                         |AGE      |
|15/05/2000                     |DATE     |
|مستشفى مدينة الرباط           |HOSPITAL |
|abcd@gmail.com                  |EMAIL    |


please check [Arabic Ner Demographics Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/)


</div><div class="h3-box" markdown="1">
       
#### 2 New Classification Models for Healthcare Social Determinants of Healthcare Concepts within Financial and Food Insecurity Contexts

Introducing two cutting-edge classification models tailored to address critical social determinants of healthcare: financial and food insecurity. These models, [genericclassifier_sdoh_financial_insecurity_mpnet](https://nlp.johnsnowlabs.com/2023/09/19/genericclassifier_sdoh_financial_insecurity_mpnet_en.html) and [genericclassifier_sdoh_food_insecurity_mpnet](https://nlp.johnsnowlabs.com/2023/09/19/genericclassifier_sdoh_food_insecurity_mpnet_en.html) have been meticulously designed to categorize healthcare-related text into key classifications.


*Example*:

```python
embeddings = MPNetEmbeddings.pretrained("mpnet_embedding_nli_mpnet_base_v2", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence_embeddings")\

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

gen_clf = GenericClassifierModel.pretrained("genericclassifier_sdoh_financial_insecurity_mpnet", "en", "clinical/models")\
    .setInputCols("features")\
    .setOutputCol("prediction")\

text_list = [
"Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy.",
"The patient a 35-year-old woman, visited her healthcare provider with concerns about her health. She bravely shared that she was facing financial difficultie, which was affecting her ability to afford necessary medical care and prescriptions. The caring healthcare provider listened attentively and discussed various options. They helped Sarah explore low-cost alternatives for her medications and connected her with local resources that could assist with healthcare expenses. By addressing the financial aspect, Sarah's healthcare provider ensured that she could receive the care she needed without further straining her finances. Leaving the appointment, Sarah felt relieved and grateful for the support in managing her health amidst her financial challenges."
]

```

*Result*:

| text                                                                           |                              result|
|--------------------------------------------------------------------------------|------------------------------------|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She h...| No_Financial_Insecurity_Or_Unknown |
|The patient a 35-year-old woman, visited her healthcare provider with concern...|               Financial_Insecurity |


Please check [Social Determinant Classification Generic Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/)

</div><div class="h3-box" markdown="1">
       

#### Introducing a New BioBERT-Based Drug Adverse Event Classifier

This [bert_sequence_classifier_vop_adverse_event](https://nlp.johnsnowlabs.com/2023/09/20/bert_sequence_classifier_vop_adverse_event_en.html) model is specialized for analyzing adverse events related to drugs in health documents. Trained on in-house annotated health text, it classifies text into two categories:

`True`: Signifying the presence of unfavorable, unintended, or harmful signs or symptoms in patients receiving pharmaceutical products or medical devices.

`False`: Denoting the absence of unfavorable experiences during the course of treatment.


*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_adverse_event", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

text_list = [
"I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel very weird. I want to reduce my blood pressure naturally. Can I stop this medication? I only took it for 5 days. I was reading here, that a lot of people has been losing weight and exercise and now they have a normal blood pressure. Please let me know, what I can do. The sides effects are horrible",
"I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pain from the liver area (under right ribs).It comes and goes. Could this be a sign of liver damage?When i get this pain i am usually in the pub drinking.If i press the area under my right rib cage about half way across i can feel pain. Is that pain in the Liver?"
]

```

*Result*:

|           text| result|
|---------------|-------|
|I am taking this medication once a day for the last 3 days. I am feeling very bad, pressure on my head, some chest pain, cramps on my neck and feel...|  True |
|I go the pub about 3-4 times a week and drink quite a bit. I like socialising, been doing so for years now.Recently been getting this occasional pa...| False |

Please check [VOP SIDE EFFECT CLASSIFICATION demo](https://demo.johnsnowlabs.com/healthcare/VOP_CLASSIFICATION_SIDE_EFFECT/)


</div><div class="h3-box" markdown="1">


#### 18 New Augmented NER Models by Leveraging the Capabilities of the LangTest Library to Boost Their Robustness Significantly

Newly introduced augmented NER models are powered by the innovative LangTest library. This cutting-edge NLP toolkit is at the forefront of language processing advancements, incorporating state-of-the-art techniques and algorithms to enhance the capabilities of our models significantly.


| Model Name               |   Predicted Entities        |
|--------------------------|-----------------------------|
| [`ner_vop_anatomy_langtest`](https://nlp.johnsnowlabs.com/2023/09/21/ner_vop_anatomy_langtest_en.html)             |  `BodyPart`, `Laterality` |
| [`ner_vop_clinical_dept_langtest`](https://nlp.johnsnowlabs.com/2023/09/21/ner_vop_clinical_dept_langtest_en.html) |  `AdmissionDischarge`, `ClinicalDept`, `MedicalDevice` |
| [`ner_vop_demographic_langtest`](https://nlp.johnsnowlabs.com/2023/09/21/ner_vop_demographic_langtest_en.html)     |  `Gender`, `Employment`, `RaceEthnicity`, `Age`, `Substance`, `RelationshipStatus`, `SubstanceQuantity` |
| [`ner_vop_problem_langtest`](https://nlp.johnsnowlabs.com/2023/09/21/ner_vop_problem_langtest_en.html)             | `PsychologicalCondition`, `Disease`, `Symptom`, `HealthStatus`, `Modifier`, `InjuryOrPoisoning` |
| [`ner_vop_problem_reduced_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_vop_problem_reduced_langtest_en.html) |  `Problem`, `HealthStatus`, `Modifier` |
| [`ner_vop_temporal_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_vop_temporal_langtest_en.html)           | `DateTime`, `Duration`, `Frequency`|
| [`ner_vop_test_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_vop_test_langtest_en.html)                   | `VitalTest`, `Test`, `Measurements`, `TestResult` |
| [`ner_vop_treatment_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_vop_treatment_langtest_en.html)         | `Drug`, `Form`, `Dosage`, `Frequency`, `Route`, `Duration`, `Procedure`, `Treatment` |
| [`ner_oncology_unspecific_posology_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_unspecific_posology_langtest_en.html) | `Cancer_Therapy`, `Posology_Information` |
| [`ner_oncology_therapy_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_therapy_langtest_en.html)  | `Cancer_Surgery`, `Chemotherapy`,  `Dosage`, `Hormonal_Therapy`, `Immunotherapy`, `Line_Of_Therapy`, `Radiotherapy`, `Radiation_Dose`, `Response_To_Treatment`, `Targeted_Therapy`, `Unspecific_Therapy` ...|
| [`ner_oncology_tnm_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_tnm_langtest_en.html)          | `Cancer_Dx`, `Lymph_Node`, `Lymph_Node_Modifier`, `Metastasis`, `Staging`, `Tumor`, `Tumor_Description` |
| [`ner_oncology_test_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_test_langtest_en.html)        | `Biomarker`, `Biomarker_Result`, `Imaging_Test`, `Oncogene`, `Pathology_Test` |
| [`ner_oncology_diagnosis_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_diagnosis_langtest_en.html) |  `Adenopathy`, `Cancer_Dx`, `Cancer_Score`, `Grade`, `Histological_Type`, `Invasion`, `Metastasis`, `Pathology_Result`, `Performance_Status`, `Staging`, `Tumor_Finding`, `Tumor_Size` |
| [`ner_oncology_biomarker_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_oncology_biomarker_langtest_en.html) | `Biomarker`, `Biomarker_Result` |
| [`ner_eu_clinical_condition_langtest`](https://nlp.johnsnowlabs.com/2023/09/22/ner_eu_clinical_condition_langtest_en.html) | `clinical_condition` |


- These models are strengthened against various perturbations (lowercase, uppercase, title case, punctuation removal, etc.).

- The table below shows the robustness of overall test results for 15 different models.
  
| model names        | original robustness  |  new robustness  |
|-------------------------------------------|---------|--------|
| ner_clinical_langtest                     | 71.72%  | 84.75% |
| ner_deid_subentity_augmented_langtest     | 95.78%  | 97.73% |
| ner_deid_generic_augmented_langtest       | 95.09%  | 97.13% |
| ner_vop_anatomy_langtest                  | 79.87%  | 89.70% |
| ner_vop_clinical_dept_langtest            | 67.99%  | 84.43% |
| ner_vop_demographic_langtest              | 74.84%  | 91.34% |
| ner_vop_problem_langtest                  | 62.17%  | 81.63% |
| ner_vop_problem_reduced_langtest          | 74.89%  | 84.75% |
| ner_vop_temporal_langtest                 | 67.76%  | 83.73% |
| ner_vop_test_langtest                     | 61.52%  | 81.86% |
| ner_vop_treatment_langtest                | 69.58%  | 84.33% |
| ner_oncology_unspecific_posology_langtest | 63.69%  | 87.47% |
| ner_oncology_therapy_langtest             | 62.03%  | 86.15% |
| ner_oncology_tnm_langtest                 | 81.22%  | 90.33% |
| ner_oncology_test_langtest                | 82.13%  | 91.72% |
| ner_oncology_diagnosis_langtest           | 72.44%  | 83.98% |
| ner_oncology_biomarker_langtest           | 93.79%  | 95.28% |
| ner_eu_clinical_condition_langtest        | 86.08%  | 91.68% |



</div><div class="h3-box" markdown="1">


####  10 New NER-based Pretrained Pipelines, Designed to Streamline Solutions with a Single Line of Code

We have 10 new named entity recognition pipelines that are meticulously designed to enhance your solutions by efficiently identifying entities and their resolutions within the clinical note. You can easily integrate this advanced capability using just a single line of code.

| Model Name         | Predicted Entities      |
|--------------------|---------------------------|
| [ner_posology_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/08/ner_posology_langtest_pipeline_en.html)   | `DOSAGE, DRUG, DURATION, FORM, FREQUENCY, ROUTE, STRENGTH` | 
| [ner_ade_clinical_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_ade_clinical_langtest_pipeline_en.html)   | `DRUG`, `ADE` |  
| [ner_events_clinical_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_events_clinical_langtest_pipeline_en.html)   | `DATE`, `TIME`, `PROBLEM`, `TEST`, `TREATMENT`, `OCCURENCE`, `CLINICAL_DEPT`, `EVIDENTIAL`, `DURATION`, `FREQUENCY`, `ADMISSION`, `DISCHARGE` |
| [ner_jsl_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_jsl_langtest_pipeline_en.html)   | `Hyperlipidemia`, `BMI`, `Kidney_Disease`, `Oncological`, `Heart_Disease`, `Obesity`, `Symptom`, `Treatment`, `Substance`, `Allergen`, `Diabetes`, `Modifier`, `Hypertension` ... |
| [ner_oncology_anatomy_general_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_oncology_anatomy_general_langtest_pipeline_en.html)   | `Anatomical_Site`, `Direction` |
| [ner_oncology_anatomy_granular_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_oncology_anatomy_granular_langtest_pipeline_en.html)   | `Direction`, `Site_Bone`, `Site_Brain`, `Site_Breast`, `Site_Liver`, `Site_Lung`, `Site_Lymph_Node`, `Site_Other_Body_Part` |
| [ner_oncology_demographics_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_oncology_demographics_langtest_pipeline_en.html)   | `Age`, `Gender`, `Race_Ethnicity`, `Smoking_Status` |
| [ner_oncology_posology_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_oncology_posology_langtest_pipeline_en.html)   | `Cancer_Surgery, Cancer_Therapy, Cycle_Count, Cycle_Day, Cycle_Number, Dosage, Duration, Frequency, Radiotherapy, Radiation_Dose, Rout` |
| [ner_oncology_response_to_treatment_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_oncology_response_to_treatment_langtest_pipeline_en.html)   | `Line_Of_Therapy`, `Response_To_Treatment`, `Size_Trend` |
| [ner_sdoh_langtest_pipeline](https://nlp.johnsnowlabs.com/2023/09/09/ner_sdoh_langtest_pipeline_en.html)   | `Alcohol`, `Disability`, `Food_Insecurity`, `Housing`, `Income`, `Insurance_Status`, `Mental_Health`, `Obesity`,  `Smoking`, `Social_Support`, `Substance_Use`, `Violence_Or_Abuse` ... |



*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

ner_pipeline = PretrainedPipeline("ner_oncology_anatomy_granular_langtest_pipeline", "en", "clinical/models")

text = """The patient presented a mass in her left breast, and a possible metastasis in her lungs and in her liver."""
```

*Result*:

| chunks   |   begin |   end | entities    |
|:---------|--------:|------:|:------------|
| left     |      36 |    39 | Direction   |
| breast   |      41 |    46 | Site_Breast |
| lungs    |      82 |    86 | Site_Lung   |
| liver    |      99 |   103 | Site_Liver  |


</div><div class="h3-box" markdown="1">



#### Leveraging the Power of SparkNLP with AWS Glue and EMR with Practical Examples and Support

Explore the seamless integration of SparkNLP with AWS Glue and EMR notebooks in this comprehensive guide. Discover how SparkNLP, a cutting-edge natural language processing library, can supercharge your data processing and analysis workflows on AWS. With step-by-step examples, learn how to harness the combined capabilities of Healthcare SparkNLP and AWS services to unlock new insights from your medical data. Whether you're a data engineer, data scientist, or NLP enthusiast, this resource will empower you to leverage the full potential of SparkNLP within the AWS ecosystem.

- [AWS EMR Notebookooks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/products/emr)
- [AWS Glue Notebookooks](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/products/glue)


</div><div class="h3-box" markdown="1">

#### Various Core Improvements; Bug Fixes, Enhanced Overall Robustness and Reliability of Spark NLP for Healthcare

- ContextualParser Metadata Update: Renaming `confidenceValue` to `confidence`
- Updated English Profession Faker Name List 




</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER/) for the most known NER models 
- New [ICD-10-CM Medicare Severity-Diagnosis Related Group Demo](https://demo.johnsnowlabs.com/healthcare/ICD10CM_MS_DRG_MAPPER/) with new icd10cm mapper and resolver models 
- Updated [Multi Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/) with new 5 new Japanese, Vietnamese, Norwegian, Danish, and Swedish language models
- Updated [Social Determinants Ner Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_NER/) with augmented SDOH NER models
- Updated [Arabic Demographics NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/) with new arabert and camelbert models
- Updated [Social Determinants Classification Generic Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/) updated financial and food insecurity models
- Updated [Voice of Patient Demo](https://demo.johnsnowlabs.com/healthcare/VOP/) with new assertion models
- Updated [Social Determinants of Health Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/) with new assertion models
- Updated [VOP SIDE EFFECT CLASSIFICATION demo](https://demo.johnsnowlabs.com/healthcare/VOP_CLASSIFICATION_SIDE_EFFECT/) with new Adverse Drug Event models

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `text2sql_with_schema_single_table_augmented`
+ `ner_clinical` -> `da`
+ `ner_clinical` -> `nv`
+ `ner_clinical` -> `no`
+ `ner_clinical` -> `ja`
+ `ner_clinical` -> `vi`
+ `ner_deid_generic_arabert` -> `ar`
+ `ner_deid_generic_camelbert` -> `ar`
+ `ner_deid_subentity_arabert` -> `ar`
+ `ner_deid_subentity_camelbert` -> `ar`
+ `bert_sequence_classifier_vop_adverse_event`
+ `genericclassifier_sdoh_food_insecurity_mpnet`
+ `genericclassifier_sdoh_financial_insecurity_mpnet`
+ `ner_posology_langtest_pipeline`
+ `ner_ade_clinical_langtest_pipeline`
+ `ner_events_clinical_langtest_pipeline`
+ `ner_jsl_langtest_pipeline`
+ `ner_oncology_anatomy_general_langtest_pipeline`
+ `ner_oncology_anatomy_granular_langtest_pipeline`
+ `ner_oncology_demographics_langtest_pipeline`
+ `ner_oncology_posology_langtest_pipeline`
+ `ner_oncology_response_to_treatment_langtest_pipeline`
+ `ner_sdoh_langtest_pipeline`
+ `ner_clinical_langtest`
+ `ner_deid_subentity_augmented_langtest`
+ `ner_deid_generic_augmented_langtest`
+ `ner_vop_anatomy_langtest` 
+ `ner_vop_clinical_dept_langtest`
+ `ner_vop_demographic_langtest`
+ `ner_vop_problem_langtest`
+ `ner_vop_problem_reduced_langtest`
+ `ner_vop_temporal_langtest`
+ `ner_vop_test_langtest`
+ `ner_vop_treatment_langtest`
+ `ner_oncology_unspecific_posology_langtest`
+ `ner_oncology_therapy_langtest`
+ `ner_oncology_tnm_langtest`
+ `ner_oncology_test_langtest`
+ `ner_oncology_diagnosis_langtest`
+ `ner_oncology_biomarker_langtest`
+ `ner_eu_clinical_condition_langtest`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
