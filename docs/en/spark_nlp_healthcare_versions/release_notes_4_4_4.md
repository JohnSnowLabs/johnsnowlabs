---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 4.4.4
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_4_4_4
key: docs-licensed-release-notes
modify_date: 2023-06-15
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.4

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. This release comes with 40+ new clinical pretrained models and pipelines, and is a testament to our commitment to continuously innovate and improve, furnishing you with a more sophisticated and powerful toolkit for healthcare natural language processing.

+ New module focused on extracting the most relevant information with Extractive Summarization
+ Customized prompts in `TextGenerator` Annotator
+ Arabic language obfuscation support in Deidentification
+ One liner Arabic language Clinical Deidentification Pipeline
+ 36 New Voice of Patient (VOP) NER models and pipelines for entity extraction from patient's own words (usually in non-medical jargon)
+ New BioBERT-based VOP Classification Models for classifying certain tones (if HCP consult, medically sound, mention of ADE, self-reported etc.) in patient's own words
+ Enhanced entity detection accuracy with the official version of Social Determinants of Health (SDOH) model
+ New NER model for precise detection of demographic characteristics in clinical notes
+ Updated Medicare Risk Adjustment score calculation module incorporating CMS's latest proposed updates including the Version 28 support
+ New Resources Downloader Notebook that includes comprehensive guideline for model downloading
+ Pretrained pipelines now compatible with all PySpark versions
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">


#### New Module Focused On Extracting The Most Relevant Information With Extractive Summarization

Extractive summarization focuses on extracting the most relevant information rather than generating new content. The process typically includes preprocessing the text, identifying important sentences using various criteria, ranking them based on their importance, and selecting the top-ranked sentences for the final summary. Extractive summarization is favored for its objectivity, preserving the factual accuracy of the original text.

Parameters:
- `similarityThreshold`: Sets the minimal cosine similarity between sentences to consider them similar.
- `summarySize`: Sets the number of sentences to summarize the text

*Example*:

```python
sentence_embeddings = BertSentenceEmbeddings()\
    .pretrained("sent_small_bert_L2_128")\
    .setInputCols(["sentences"])\
    .setOutputCol("sentence_embeddings")

summarizer = ExtractiveSummarization()\
    .setInputCols(["sentences", "sentence_embeddings"])\
    .setOutputCol("summaries")\
    .setSummarySize(2)\
    .setSimilarityThreshold(0)

text = """Residual disease after initial surgery for ovarian cancer is the strongest prognostic factor for survival. However, the extent of surgical resection required to achieve optimal cytoreduction is controversial. Our goal was to estimate the effect of aggressive surgical resection on ovarian cancer patient survival.
A retrospective cohort study of consecutive patients with International Federation of Gynecology and Obstetrics stage IIIC ovarian cancer undergoing primary surgery was conducted between January 1, 1994, and December 31, 1998. The main outcome measures were residual disease after cytoreduction, frequency of radical surgical resection, and 5-year disease-specific survival.
The study comprised 194 patients, including 144 with carcinomatosis. The mean patient age and follow-up time were 64.4 and 3.5 years, respectively. After surgery, 131 (67.5%) of the 194 patients had less than 1 cm of residual disease (definition of optimal cytoreduction). Considering all patients, residual disease was the only independent predictor of survival; the need to perform radical procedures to achieve optimal cytoreduction was not associated with a decrease in survival. For the subgroup of patients with carcinomatosis, residual disease and the performance of radical surgical procedures were the only independent predictors. Disease-specific survival was markedly improved for patients with carcinomatosis operated on by surgeons who most frequently used radical procedures compared with those least likely to use radical procedures (44% versus 17%, P < .001).
Overall, residual disease was the only independent predictor of survival. Minimizing residual disease through aggressive surgical resection was beneficial, especially in patients with carcinomatosis."""
```


*Result*:

```
'The main outcome measures were residual disease after cytoreduction, frequency of radical surgical resection, and 5-year disease-specific survival.\nThe study comprised 194 patients, including 144 with carcinomatosis.',
'Considering all patients, residual disease was the only independent predictor of survival; the need to perform radical procedures to achieve optimal cytoreduction was not associated with a decrease in survival. For the subgroup of patients with carcinomatosis, residual disease and the performance of radical surgical procedures were the only independent predictors.'
```

See [Extractive Summarization Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.2.ExtractiveSummarization.ipynb) for examples.



</div><div class="h3-box" markdown="1">

####  Customized Prompts in `TextGenerator` Annotator

The MedicalTextGenerator() function incorporates a powerful feature called SetCustomPrompt, designed to enhance text generation capabilities. By utilizing this feature, users can input a custom prompt, typically in the format of "question: {DOCUMENT} answer:". This structure allows for the generation of informative and contextually relevant medical text responses.  This feature enhances the flexibility and usability of the MedicalTextGenerator() function, empowering users to generate accurate and contextually appropriate medical text with ease.


*Example*:

```python
gpt_qa = MedicalTextGenerator().pretrained("biogpt_chat_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("answer")\
    .setMaxNewTokens(299)\
    .setStopAtEos(True)\
    .setDoSample(False)\
    .setTopK(3)\
    .setRandomSeed(42)\
    .setCustomPrompt("question: {DOCUMENT} answer:")

text = "What medications are commonly used to treat emphysema?"

```


*Result*:

```
question: What medications are commonly used to treat emphysema ? 
answer: Hello, There are two types of medications to treat emphysema: 1. Alpha agonists ( like albuterol or albuterol / levosalbutamol ) are used to treat symptoms of shortness of breath ( SOB ) and tightness in the chest ( tightness in chest ). These meds cause a mild to moderate increase in heart rate ( tachycardia ). 2. Beta blockers ( like propranolol or metoprolol ) are used to treat or to prevent symptoms of heart failure ( ejection fraction is 20 % or less ). These medications cause or worsen shortness of breath, tightness in chest, heart rate. You can take a combination of these medications. The combination that you will work best is a two - pill combination of albuterol and propranolol ( half tablet twice a day ). This will reduce or eliminate the need for albuterol and albuterol / levosalbutamol in your case. The other medications are used in consultation with your physician.

```

See [Medical Text Generation Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Biogpt_Chat_JSL.ipynb) for examples.





</div><div class="h3-box" markdown="1">

#### One Liner Arabic Language Clinical Deidentification Pipeline

We're thrilled to announce that Spark NLP for Healthcare now supports obfuscation in Arabic De-identification (Deid) models. This feature enhances data privacy by substituting sensitive Protected Health Information (PHI) with corresponding synthetic data, while preserving data integrity through observance of certain consistency rules. 

*Example*:

```python
deid_masked_entity = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("masked_with_entity")\
    .setMode("mask")\
    .setLanguage('ar')\
    .setMaskingPolicy("entity_labels")

deid_masked_char = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("masked_with_chars")\
    .setMode("mask")\
    .setLanguage('ar')\
    .setMaskingPolicy("same_length_chars")

deid_masked_fixed_char = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("masked_fixed_length_chars")\
    .setMode("mask")\
    .setLanguage('ar')\
    .setMaskingPolicy("fixed_length_chars")\
    .setFixedMaskLength(4)

obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("obfuscated") \
    .setMode("obfuscate")\
    .setLanguage('ar')\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker") \
    .setRegexOverride(True)

text = '''
الملاحظات السريرية - مريض السكري
التاريخ: 11 مايو 1999
اسم المريض: فاطمة علي
العنوان: شارع الحرية ، حي السلام ، القاهرة
دولة: مصر
اسم المستشفى: مستشفى الشفاء
اسم الطبيب: د.محمد صلاح
'''
```


*Result*:

|    | original sentence                          | Masked                                        | Masked with Chars                          | Masked with Fixed Chars               | Obfuscated                                                 |
|---:|:-------------------------------------------|:----------------------------------------------|:-------------------------------------------|:--------------------------------------|:-----------------------------------------------------------|
|  0 | الملاحظات السريرية - مريض السكري           | الملاحظات السريرية - مريض السكري              | الملاحظات السريرية - مريض السكري           | الملاحظات السريرية - مريض السكري      | الملاحظات السريرية - مريض السكري                           |
|  1 | التاريخ: 11 مايو 1999                      | التاريخ: [تاريخ]                              | التاريخ: [٭٭٭٭٭٭٭٭٭٭]                      | التاريخ: ٭٭٭٭                         | التاريخ: 11 يوليو 1999                                     |
|  2 | اسم المريض: فاطمة علي                      | اسم المريض: [الاسم]                           | اسم المريض: [٭٭٭٭٭٭٭]                      | اسم المريض: ٭٭٭٭                      | اسم المريض: رياض محروق                                     |
|  3 | العنوان: شارع الحرية ، حي السلام ، القاهرة | العنوان: شارع الحرية ، حي [الموقع] ، [الموقع] | العنوان: شارع الحرية ، حي [٭٭٭٭] ، [٭٭٭٭٭] | العنوان: شارع الحرية ، حي ٭٭٭٭ ، ٭٭٭٭ | العنوان: شارع الحرية ، حي شارع الجنوب أفريقي ، شارع التقدم |
|  4 | دولة: مصر                                  | دولة: [الموقع]                                | دولة: [٭]                                  | دولة: ٭٭٭٭                            | دولة: الشارع الأسفلتي                                      |
|  5 | اسم المستشفى: مستشفى الشفاء                | اسم المستشفى: مستشفى الشفاء                   | اسم المستشفى: مستشفى الشفاء                | اسم المستشفى: مستشفى الشفاء           | اسم المستشفى: مستشفى الشفاء                                |
|  6 | اسم الطبيب: د.محمد صلاح                    | اسم الطبيب: [الاسم]                           | اسم الطبيب: [٭٭٭٭٭٭٭٭٭]                    | اسم الطبيب: ٭٭٭٭                      | اسم الطبيب: ليث مصري                                       |


See [Clinincal Multi Language Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.1.Clinical_Multi_Language_Deidentification.ipynb) for examples.





</div><div class="h3-box" markdown="1">

#### New Arabic Clinical Deidentification Pipeline

This pipeline can be used to deidentify Arabic PHI information from medical texts in one one liner to ease the process of building the entire pipeline one by one. The PHI information will be masked and obfuscated in the resulting text. The pipeline can mask and obfuscate `CONTACT`, `NAME`, `DATE`, `ID`, `LOCATION`, `AGE`, `PATIENT`, `HOSPITAL`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `SSN`, `ACCOUNT`, `LICENSE`, `DLN` and `VIN`.

*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline
deid_pipeline_ar = PretrainedPipeline("clinical_deidentification", "ar", "clinical/models")

text = """
ملاحظات سريرية - مريض الربو:
التاريخ: 30 مايو 2023
اسم المريضة: ليلى حسن
تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012.
العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة
الرمز البريدي: 54321
البلد: المملكة العربية السعودية
اسم المستشفى: مستشفى النور
اسم الطبيب: د. أميرة أحمد
"""
```



*Result*:

|   |                                                              Sentence |                                                  masked_with_entity |                                                     Masked with Chars |                                       Masked with Fixed Chars |                                                            Obfuscated |
|--:|----------------------------------------------------------------------:|--------------------------------------------------------------------:|----------------------------------------------------------------------:|--------------------------------------------------------------:|----------------------------------------------------------------------:|
| 0 |                   ملاحظات سريرية - مريض الربو:\nالتاريخ: 30 مايو 2023 |              ملاحظات سريرية - مريض الربو:\nالتاريخ: [تاريخ] [تاريخ] |                   ملاحظات سريرية - مريض الربو:\nالتاريخ: [٭٭٭٭٭] [٭٭] |              ملاحظات سريرية - مريض الربو:\nالتاريخ: ٭٭٭٭ ٭٭٭٭ |                  ملاحظات سريرية - مريض الربو:\nالتاريخ: 30 يونيو 2024 |
| 1 |                                                 اسم المريضة: ليلى حسن |                                               اسم المريضة: [المريض] |                                                 اسم المريضة: [٭٭٭٭٭٭] |                                             اسم المريضة: ٭٭٭٭ |                                               اسم المريضة: أدهم جبالي |
| 2 | تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 123456789012. |     تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [هاتف]. | تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي [٭٭٭٭٭٭٭٭٭٭]. | تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي ٭٭٭٭. | تم تسجيل المريض في النظام باستخدام رقم الضمان الاجتماعي 963525347201. |
| 3 |                  العنوان: شارع المعرفة، مبنى رقم 789، حي الأمانة، جدة | العنوان: شارع المعرفة، مبنى رقم [الرمز البريدي] [المدينة] [المدينة] |                  العنوان: شارع المعرفة، مبنى رقم [٭٭] [٭٭٭٭٭٭٭٭٭] [٭] |                العنوان: شارع المعرفة، مبنى رقم ٭٭٭٭ ٭٭٭٭ ٭٭٭٭ |                العنوان: شارع المعرفة، مبنى رقم 160، كلميم سانت كاترين |
| 4 |                                                  الرمز البريدي: 54321 |                                      الرمز البريدي: [الرمز البريدي] |                                                  الرمز البريدي: [٭٭٭] |                                           الرمز البريدي: ٭٭٭٭ |                                                  الرمز البريدي: 79915 |
| 5 |                                       البلد: المملكة العربية السعودية |                                            البلد: [المدينة] [البلد] |                                       البلد: [٭٭٭٭٭٭٭٭٭٭٭٭٭] [٭٭٭٭٭٭] |                                              البلد: ٭٭٭٭ ٭٭٭٭ |                                        البلد: زغوان الغربية أوزبكستان |
| 6 |                                            اسم المستشفى: مستشفى النور |                                              اسم المستشفى: [الموقع] |                                            اسم المستشفى: [٭٭٭٭٭٭٭٭٭٭] |                                            اسم المستشفى: ٭٭٭٭ |                                            اسم المستشفى: شارع المدارس |
| 7 |                                             اسم الطبيب: د. أميرة أحمد |                                              اسم الطبيب: د. [دكتور] |                                             اسم الطبيب: د. [٭٭٭٭٭٭٭٭] |                                           اسم الطبيب: د. ٭٭٭٭ |                                           اسم الطبيب: د. هندية قبلاوي |


See [Clinincal Multi Language Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.1.Clinical_Multi_Language_Deidentification.ipynb) for examples.





</div><div class="h3-box" markdown="1">

#### 36 New Voice Of Patient (VOP) NER Models And Pipelines For Entity Extraction From Patient's Own Words

We are excited to introduce our new NER models which extract clinical entities from the documents that are shared by patients in their own words.

| model_name      | description   | predicted_entity   |
|-----------------|---------------|--------------------|
| [ner_vop_anatomy_emb](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_clinical_dept_en.md.html) <br /> [ner_vop_anatomy_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/07/ner_vop_anatomy_emb_clinical_medium_en.html)  <br /> [ner_vop_anatomy_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_anatomy_emb_clinical_large_en.html)   <br /> [ner_vop_anatomy_pipeline](https://nlp.johnsnowlabs.com/2023/06/09/ner_vop_anatomy_pipeline_en.html)                            | Extracts anatomical terms from the documents transferred from the patient’s own sentences.                                                                 | `BodyPart`, `Laterality`     |
| [ner_vop_clinical_dept](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_clinical_dept_en.html) <br />  [ner_vop_clinical_dept_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_clinical_dept_emb_clinical_medium_en.html) <br />  [ner_vop_clinical_dept_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_clinical_dept_emb_clinical_large_en.html) <br /> [ner_vop_clinical_dept_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_clinical_dept_pipeline_en.html)          | Extracts medical devices and clinical department mentions terms from the documents transferred from the patient’s own sentences.                           | `AdmissionDischarge`, `ClinicalDept`, `MedicalDevice`  |
| [ner_vop_demographic](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_demographic_en.html) <br /> [ner_vop_demographic_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_demographic_emb_clinical_medium_en.html) <br /> [ner_vop_demographic_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_demographic_emb_clinical_large_en.html) <br /> [ner_vop_demographic_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_demographic_pipeline_en.html)                    | Extracts demographic terms from the documents transferred from the patient’s own sentences.                                                                | `Gender`, `Employment`, `RaceEthnicity`, `Age`, `Substance`, `RelationshipStatus`, `SubstanceQuantity`     |
| [ner_vop_problem](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_problem_en.html) <br /> [ner_vop_problem_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_problem_emb_clinical_medium_en.html) <br /> [ner_vop_problem_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_problem_emb_clinical_large_en.html)  <br /> [ner_vop_problem_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_problem_pipeline_en.html)                                   | Extracts clinical problems from the documents transferred from the patient’s own sentences using a granular taxonomy.                                      | `PsychologicalCondition`, `Disease`, `Symptom`, `HealthStatus`, `Modifier`, `InjuryOrPoisoning`  |
| [ner_vop_test](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_test_en.html) <br />  [ner_vop_test_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_test_emb_clinical_medium_en.html) <br />  [ner_vop_test_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_test_emb_clinical_large_en.html) <br /> [ner_vop_test_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_test_pipeline_en.html)                                              | Extracts test mentions from the documents transferred from the patient’s own sentences.                                                                    | `VitalTest`, `Test`, `Measurements`, `TestResult`  |
| [ner_vop_temporal](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_temporal_en.html) <br />  [ner_vop_temporal_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_temporal_en.html) <br />  [ner_vop_temporal_emb_clinical_large_final](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_temporal_en.html) <br /> [ner_vop_temporal_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_temporal_pipeline_en.html)                        | Extracts temporal references from the documents transferred from the patient’s own sentences.                                                              | `DateTime`, `Frequency`, `Duration`  |
| [ner_vop_treatment](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_treatment_en.html)  <br />  [ner_vop_treatment_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_treatment_emb_clinical_medium_en.html)  <br />  [ner_vop_treatment_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_treatment_emb_clinical_large_en.html)  <br /> [ner_vop_treatment_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_treatment_pipeline_en.html)                          | Extracts treatments mentioned in documents transferred from the patient’s own sentences.                                                                   | `Drug`, `Form`, `Dosage`, `Frequency`, `Route`, `Duration`, `Procedure`, `Treatment`   |
| [ner_vop](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_en.html) <br />  [ner_vop_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_emb_clinical_medium_en.html) <br />  [ner_vop_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/06/ner_vop_emb_clinical_large_en.html) <br /> [ner_vop_pipeline](https://nlp.johnsnowlabs.com/2023/06/09/ner_vop_pipeline_en.html)                                                                  | Extracts healthcare-related terms from the documents transferred from the patient’s own sentences.                                                         | `Gender`, `Employment`, `Age`, `BodyPart`, `Substance`, `Form`, `PsychologicalCondition`, `Vaccine`, `Drug`, `DateTime`, `ClinicalDept`, `Laterality`, `Test`, `AdmissionDischarge`, `Disease`, `VitalTest`, `Dosage`, `Duration`, `RelationshipStatus`, `Route`, `Allergen`, `Frequency`, `Symptom`, `Procedure`, `HealthStatus`, `InjuryOrPoisoning`, `Modifier`, `Treatment`, `SubstanceQuantity`, `MedicalDevice`, `TestResult` |
| [ner_vop_problem_reduced](https://nlp.johnsnowlabs.com/2023/06/07/ner_vop_problem_reduced_en.html) <br />  [ner_vop_problem_reduced_emb_clinical_medium](https://nlp.johnsnowlabs.com/2023/06/07/ner_vop_problem_reduced_emb_clinical_medium_en.html) <br />  [ner_vop_problem_reduced_emb_clinical_large](https://nlp.johnsnowlabs.com/2023/06/07/ner_vop_problem_reduced_emb_clinical_large_en.html) <br /> [ner_vop_problem_reduced_pipeline](https://nlp.johnsnowlabs.com/2023/06/10/ner_vop_problem_reduced_pipeline_en.html) | Extracts clinical problems from the documents transferred from the patient’s own sentences. The taxonomy is reduced (one label for all clinical problems). | `Problem`, `HealthStatus`, `Modifier`  |                                                                                                                                                                                                                                                                                                              

*Example*:

```    
ner = MedicalNerModel.pretrained("ner_vop", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")
                             
sample_text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital."""

```


*Result*:

| chunk                | ner_label              |
|:---------------------|:-----------------------|
| 20 year old          | Age                    |
| girl                 | Gender                 |
| hyperthyroid         | Disease                |
| 1 month ago          | DateTime               |
| weak                 | Symptom                |
| light                | Symptom                |
| panic attacks        | PsychologicalCondition |
| depression           | PsychologicalCondition |
| left                 | Laterality             |
| chest                | BodyPart               |
| pain                 | Symptom                |
| increased            | TestResult             |
| heart rate           | VitalTest              |
| rapidly              | Modifier               |
| weight loss          | Symptom                |
| 4 months             | Duration               |
| hospital             | ClinicalDept           |
| discharged           | AdmissionDischarge     |


For all Voice of Patient models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?q=vop)


</div><div class="h3-box" markdown="1">

#### New BioBERT-Based VOP Classification Models for Biomedical Text Analysis

We are excited to introduce a new Bert-based Voice of Patient classifier models which are a collection of BioBERT-based classifiers designed for various text classification tasks in the biomedical domain. These models leverage the power of BERT, a transformer-based language model, to analyze and classify different types of textual data. They are trained to understand the nuances of medical language and concepts to make accurate predictions.

| modelname                                     | description                                                                                                                                                                                      | pred_entity                 |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| [bert_sequence_classifier_vop_drug_side_effect](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_drug_side_effect_en.html) <br /> [bert_sequence_classifier_vop_drug_side_effect_pipeline](https://nlp.johnsnowlabs.com/2023/06/14/bert_sequence_classifier_vop_drug_side_effect_pipeline_en.html)| Classify informal texts (such as tweets or forum posts) according to the presence of drug side effects. | `Drug_AE`, `Other`          |
| [bert_sequence_classifier_vop_hcp_consult](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_hcp_consult_en.html)   <br />  [bert_sequence_classifier_vop_hcp_consult_pipeline](https://nlp.johnsnowlabs.com/2023/06/14/bert_sequence_classifier_vop_hcp_consult_pipeline_en.html) | Identify texts that mention a HCP consult.                                                              | `Consulted_By_HCP`, `Other` |
| [bert_sequence_classifier_vop_self_report](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_self_report_en.html)  <br />  [bert_sequence_classifier_vop_self_report_pipeline](https://nlp.johnsnowlabs.com/2023/06/14/bert_sequence_classifier_vop_self_report_pipeline_en.html)  | Classify texts depending on if they are self-reported or if they refer to another person.               | `1st_Person`, `3rd_Person`  |
| [bert_sequence_classifier_vop_sound_medical](https://nlp.johnsnowlabs.com/2023/06/13/bert_sequence_classifier_vop_sound_medical_en.html)  <br /> [bert_sequence_classifier_vop_sound_medical_pipeline](https://nlp.johnsnowlabs.com/2023/06/14/bert_sequence_classifier_vop_sound_medical_pipeline_en.html)  | Identify whether the suggestion that is mentioned in the text is medically sound.                    | `True`, `False`             |

*Example*:


```python
sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_vop_sound_medical", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

sample_texts = ["I had a lung surgery for emphyema and after surgery my xray showing some recovery.",
                "I was advised to put honey on a burned skin."]

```

*Result*:



|text                                                                                                               |result      |
|-------------------------------------------------------------------------------------------------------------------|------------|
|My friend was treated for her skin cancer two years ago.                                                           |3rd_Person|
|I started with dysphagia in 2021, then, a few weeks later, felt weakness in my legs, followed by a severe diarrhea.|1st_Person|



</div><div class="h3-box" markdown="1">

#### Enhanced Entity Detection Accuracy With The Official Version Of Social Determinants Of Health (SDOH) Model

We are excited to introduce a new model that specializes in identifying social determinants of health (SDOH) mentions. This model accurately recognizes instances where SDOH characteristics, including `Access_To_Care`, `Community_Safety`, `Education`,  `Food_Insecurity`, `Insurance_Status`, and more entities are referenced. Its advanced capabilities provide valuable insights for SDOH-related analyses and applications.

*Example*:


```python
ner_model = MedicalNerModel.pretrained("ner_sdoh", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = """Smith is living in New York, a divorced Mexcian American woman. She has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. Pt with likely long-standing depression.She has a long history of etoh abuse, beginning in her teens. She has been a daily drinker for 30 years. She had DUI in April and was due to court this week.""" 

```

*Result*:


|    | chunks             |   begin |   end | entities            |
|---:|:-------------------|--------:|------:|:--------------------|
|  0 | New York           |      20 |    27 | Geographic_Entity   |
|  1 | divorced           |      32 |    39 | Marital_Status      |
|  2 | Mexcian American   |      41 |    56 | Race_Ethnicity      |
|  3 | woman              |      58 |    62 | Gender              |
|  4 | She                |      65 |    67 | Gender              |
|  5 | hospitalizations   |     109 |   124 | Other_SDoH_Keywords |
|  6 | cleaning assistant |     183 |   200 | Employment          |
|  7 | health insurance   |     220 |   235 | Insurance_Status    |
|  8 | depression         |     286 |   295 | Mental_Health       |
|  9 | She                |     297 |   299 | Gender              |
| 10 | etoh abuse         |     323 |   332 | Alcohol             |
| 11 | her                |     348 |   350 | Gender              |
| 12 | teens              |     352 |   356 | Age                 |
| 13 | She                |     359 |   361 | Gender              |
| 14 | daily              |     374 |   378 | Substance_Frequency |
| 15 | drinker            |     380 |   386 | Alcohol             |
| 16 | 30 years           |     392 |   399 | Substance_Duration  |
| 17 | She                |     402 |   404 | Gender              |
| 18 | DUI                |     410 |   412 | Legal_Issues        |


See [Models Hub Page](https://nlp.johnsnowlabs.com/2023/06/13/ner_sdoh_en.html) for more details.




</div><div class="h3-box" markdown="1">

#### New NER Model For Precise Detection Of Demographic Characteristics In Clinical Notes

This new model identifies healthcare mentions that refer to a situation where a patient's demographic characteristics, such as `race`, `ethnicity`, `gender`, `age`, `socioeconomic` `status`, or `geographic location`.



*Example*:

```python
ner = MedicalNerModel.pretrained("ner_demographic_extended_healthcare","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")


sample_text = """Patient Information:
Gender: Non-binary
Age: 68 years old
Race: Black
Employment status: Retired
Marital Status: Divorced
Sexual Orientation: Asexual
Religion: Judaism
Body Mass Index: 29.1
Unhealthy Habits: Substance use
Socioeconomic Status: Low Income
Area of Residence: Rural setting
Disability Status: Blindness
Chief Complaint:
The patient presented to the emergency department with complaint of severe chest pain that started suddenly while asleep.
"""

```

*Result*:

|chunk        |ner_label         |confidence|
|-------------|------------------|----------|
|Non-binary   |Gender            |0.9987    |
|68 years old |Age               |0.6892667 |
|Black        |Race_ethnicity    |0.9226    |
|Retired      |Employment_status |0.9426    |
|Divorced     |Marital_Status    |0.9996    |
|Asexual      |Sexual_orientation|1.0       |
|Judaism      |Religion          |0.986     |
|Substance use|Unhealthy_habits  |0.48755002|


See [Models Hub Page](https://nlp.johnsnowlabs.com/2023/06/08/ner_demographic_extended_healthcare_en.html) for more details.




</div><div class="h3-box" markdown="1">

#### Updated Medicare Risk Adjustment Score Calculation Module Incorporating CMS's Latest Proposed Updates Including The Version 28 Support

We are excited to introduce significant updates to the Medical Risk Adjustment module of Spark-NLP for Healthcare! <br/>

CMS (Centers for Medicare & Medicaid Services) releases updated versions of risk adjustment models periodically to account for changes in healthcare data, policy requirements, and advancements in statistical modeling techniques.

With this release, Spark-NLP for Healthcare incorporates the proposed updates by CMS for the risk adjustment module, featuring a major update represented as **Version 28**.

Each version of the risk adjustment module is associated with a specific year, indicating the time period for which the model is designed.
For example, `ESRDV21Y19` (ESRD version 21 year 19) refers to the 21st version of the risk adjustment model for End-Stage Renal Disease (ESRD) and is designed for the year 2019.


**Updates on Risk Adjustment Module**:

- New modules added to Spark-NLP for Healthcare:

| Version    | Year     | Module Name        |
|------------|----------|--------------------|
| 28         | Combined | `profileV28`       |
| 28         | 2024     | `profileV28Y24`    |
| 24         | Combined | `profileV24`       |
| ESRDV21    | 2019     | `profileESRDV21Y19`|



- A new feature has been introduced in this release that enhances the risk score calculation process. With this update, the risk score calculation now incorporates the coding pattern (intensity) adjustment and normalization factor for all versions and years.

- The default parameters for the `profile()` method have been modified in this release. <br/>
Previous Default: Version 24, Year 19 <br/>
Updated Default: Version 28, Year Combined <br/>

- We have included the `risk_score_adj` and `risk_score_age_adj` information in the outputs of the profile methods. <br/>


*Example*:

Risk Adjustment Module should be used with the following information in order:

1- A list of ICD10 codes for the measurement year. <br/>
2- The age of the patient. <br/>
3- The gender of the patient; {"M", "F"} <br/>
4- The eligibility segment of the patient. Allowed values are as follows:
>
    - "CFA": Community Full Benefit Dual Aged
    - "CFD": Community Full Benefit Dual Disabled
    - "CNA": Community NonDual Aged
    - "CND": Community NonDual Disabled
    - "CPA": Community Partial Benefit Dual Aged
    - "CPD": Community Partial Benefit Dual Disabled
    - "INS": Long Term Institutional
    - "NE": New Enrollee
    - "SNPNE": SNP NE

5- Original reason for entitlement code (orec).
>
    - "0": Old age and survivor's insurance
    - "1": Disability insurance benefits
    - "2": End-stage renal disease
    - "3": Both DIB and ESRD

6- If the patient is in Medicaid or not.

```python
#sample pyspark dataframe called df:
df.show(5)

>>>

```

|      ICD10CM_CODES|GENDER|OREC|AGE|MEDICAID|ELIGIBILITY|
|-------------------|------|----|---|--------|-----------|
|M86622, M0549, I...|     M|   0| 32|    true|        CFD|
|E133311, E200, T...|     M|   0| 32|    true|        CFD|
|C179, I70348, C8...|     M|   0| 32|    true|        CFD|
|S72463A, C37, E1...|     M|   0| 32|    true|        CFD|
|S1224XB, S72115B...|     M|   0| 32|    true|        CFD|




Applying `profileV28Y24` module over the sample data:

```python
df = df.withColumn("hcc_profile", profileV28Y24(df.ICD10CM_CODES, df.AGE, df.GENDER, df.ELIGIBILITY, df.OREC, df.MEDICAID))


```

*Result*:


|      ICD10CM_CODES|GENDER|OREC|AGE|MEDICAID|ELIGIBILITY|       hcc_profile|risk_score|            hcc_lst|risk_score_adj|risk_score_age_adj|           hcc_map|         parameters|            details|
|-------------------|------|----|---|--------|-----------|------------------|----------|-------------------|--------------|------------------|------------------|-------------------|-------------------|
|M86622, M0549, I...|     M|   0| 32|    true|        CFD|10.022, "HCC401...|    10.022|"HCC401","HCC21"...|        9.2913|            0.1771|"L97214":"HCC38...|"elig":"CFD","ag...|"CFD_HCC267":0.5...|
|E133311, E200, T...|     M|   0| 32|    true|        CFD|9.374, "HCC280"...|     9.374|"HCC280","CHR_LU...|        8.6906|            0.1771|"G308":"HCC127"...|"elig":"CFD","ag...|"CFD_HCC202":0.2...|
|C179, I70348, C8...|     M|   0| 32|    true|        CFD|12.988, "HCC17"...|    12.988|"HCC17","HCC401"...|       12.0411|            0.1771|"C4A20":"HCC21"...|"elig":"CFD","ag...|"CFD_HCC280":0.2...|
|S72463A, C37, E1...|     M|   0| 32|    true|        CFD|17.034, "HF_CHR...|    17.034|"HF_CHR_LUNG","H...|       15.7921|            0.1771|"C8296":"HCC21"...|"elig":"CFD","ag...|"CFD_HCC267":0.5...|
|S1224XB, S72115B...|     M|   0| 32|    true|        CFD|7.99, "HCC401",...|      7.99|"HCC401","HCC51"...|        7.4075|            0.1771|"D57818":"HCC10...|"elig":"CFD","ag...|"CFD_HCC267":0.5...|



For the detailed usage of the module, please visit [Calculate Medicare Risk Adjustment Score notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.1.Calculate_Medicare_Risk_Adjustment_Score.ipynb).


</div><div class="h3-box" markdown="1">

#### New Resources Downloader Notebook That Includes Comprehensive Guideline For Model Downloading

[Model Download Helpers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/34.Model_Download_Helpers.ipynb) includes a comprehensive guide to the various parameters and functionalities of the ResourceDownloader annotator, which facilitates the downloading and management of resources such as pretrained models and pipelines. This annotator is designed to efficiently download and manage various resources, including pretrained models and pipelines without using your sensitive AWS keys in any script/ environment with no addional library (e.g. boto3, aws cli) needed.

*Examples*:

- with S3 URI


```python
s3_uri = "s3://auxdata.johnsnowlabs.com/public/models/nerdl_conll_elmo_en_4.0.0_3.0_1654103884644.zip"

ResourceDownloader.downloadModelDirectly(s3_uri,  "public/models", unzip=True)

```

- with model name
```python
model_name = "public/models/nerdl_restaurant_100d_en_3.3.4_3.0_1640949258750.zip"

ResourceDownloader.downloadModelDirectly(model_name,  "public/models", unzip=True)

```
- updateCacheModels
```python
from sparknlp_jsl.updateModels import UpdateModels
UpdateModels.updateCacheModels()

ls ~/cache_pretrained

# embeddings_clinical_en_2.0.2_2.4_1558454742956/
# ner_clinical_large_en_2.5.0_2.4_1590021302624/ 

```



#### Pretrained Pipelines Now Compatible With All PySpark Versions

We are thrilled to announce the release of our new PretrainedPipeline, specifically designed to be compatible with all versions of PySpark. This groundbreaking update ensures seamless integration and effortless deployment of Spark NLP's powerful pretrained models across different PySpark environments.




</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- The `save()` method on `MedicalSummarization` has been fixed, ensuring proper functionality.
- The bug in the `Chunk2Token` Python class has been resolved, eliminating any issues related to it.
- The Fine-tune issue in `SentenceEntityResolver` has been fixed, enhancing its performance and accuracy.
- The `sparknlp_jsl.start()`function now works correctly with the `apple_silicon` and `aarch64` parameters.
- The default `scopeWindow` parameter on `AssertionDLApproach` has been updated to (9,15), enhancing its effectiveness in processing textual assertions.
- Compilation issues related to SparkNLP v443 have been resolved, resulting in smoother operation.
- We have improved the documentation, providing clearer instructions and explanations for easier usage.



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For Making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Extractive Summarization Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.2.ExtractiveSummarization.ipynb) 
- New [Model Download Helpers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/34.Model_Download_Helpers.ipynb)
- Updated [Biogpt_Chat_JSL Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Biogpt_Chat_JSL.ipynb) for latest models
- Updated [Clinical MultiLanguage Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.1.Clinical_Multi_Language_Deidentification.ipynb) for latest models
- New [All in One Voice Of Patient](https://demo.johnsnowlabs.com/healthcare/VOP/)
- New [Voice Of Patient CLASSIFICATION_SIDE_EFFECT Demo](https://demo.johnsnowlabs.com/healthcare/VOP_CLASSIFICATION_SIDE_EFFECT)
- Updated [SOCIAL DETERMINANT CLASSIFICATION GENERIC Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/) 
- Updated [CLINICAL DEIDENTIFICATION MULTI-LANGUAGE Demo](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/)  


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `clinical_deidentification` -> `ar`
+ `summarizer_clinical_laymen_pipeline`
+ `ner_demographic_extended_healthcare`
+ `ner_sdoh`
+ `ner_vop_anatomy`
+ `ner_vop_anatomy_emb_clinical_medium`
+ `ner_vop_anatomy_emb_clinical_large`
+ `ner_vop_anatomy_pipeline`
+ `ner_vop_clinical_dept`
+ `ner_vop_clinical_dept_emb_clinical_medium`
+ `ner_vop_clinical_dept_emb_clinical_large`
+ `ner_vop_clinical_dept_pipeline`
+ `ner_vop_demographic`
+ `ner_vop_demographic_emb_clinical_medium`
+ `ner_vop_demographic_emb_clinical_large`
+ `ner_vop_demographic_pipeline`
+ `ner_vop_problem`
+ `ner_vop_problem_emb_clinical_medium`
+ `ner_vop_problem_emb_clinical_large`
+ `ner_vop_problem_pipeline`
+ `ner_vop_test`
+ `ner_vop_test_emb_clinical_medium`
+ `ner_vop_test_emb_clinical_large`
+ `ner_vop_test_pipeline`
+ `ner_vop_temporal`
+ `ner_vop_temporal_emb_clinical_medium`
+ `ner_vop_temporal_emb_clinical_large_final`
+ `ner_vop_temporal_pipeline`
+ `ner_vop_treatment`
+ `ner_vop_treatment_emb_clinical_medium`
+ `ner_vop_treatment_emb_clinical_large`
+ `ner_vop_treatment_pipeline`
+ `ner_vop`
+ `ner_vop_emb_clinical_medium`
+ `ner_vop_emb_clinical_large`
+ `ner_vop_pipeline`
+ `ner_vop_problem_reduced`
+ `ner_vop_problem_reduced_emb_clinical_medium`
+ `ner_vop_problem_reduced_emb_clinical_large`
+ `ner_vop_problem_reduced_pipeline`
+ `bert_sequence_classifier_vop_drug_side_effect`
+ `bert_sequence_classifier_vop_drug_side_effect_pipeline`
+ `bert_sequence_classifier_vop_hcp_consult`
+ `bert_sequence_classifier_vop_hcp_consult_pipeline`
+ `bert_sequence_classifier_vop_self_report`
+ `bert_sequence_classifier_vop_self_report_pipeline`
+ `bert_sequence_classifier_vop_sound_medical`
+ `bert_sequence_classifier_vop_sound_medical_pipeline`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)



</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
