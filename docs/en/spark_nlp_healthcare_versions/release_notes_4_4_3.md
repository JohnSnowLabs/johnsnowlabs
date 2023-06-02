---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 4.4.3
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_4_4_3
key: docs-licensed-release-notes
modify_date: 2023-06-01
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 4.4.3

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. This release comes with 30+ new clinical pretrained models and pipelines, and is a testament to our commitment to continuously innovate and improve, furnishing you with a more sophisticated and powerful toolkit for healthcare natural language processing.

+ Newly introduced Arabic De-Identification NER models and pretrained pipelines

+ New medical summarizer model fine-tuned with a custom dataset to minimize clinical jargon in laymen terms

+ New Medical Summarizer Pretrained Pipelines that can be used in one line

+ Updated ICD-10-CM resolver and chunk mapper models aligning with the latest updates in the ICD-10-CM terminology to ensure unparalleled accuracy in clinical coding.

+ A new Voice of Patient (VOP) medical classifier model focusing on the side effect classification of treatments and procedures in patients' own words.

+ Enhanced Social Determinants of Health (SDOH) classifier models for detecting patients' situation according to certain conditions (under treatment or not, suffering from housing insecurity)

+ Introducing the innovative `NerTemplateRender` annotator to generate customized prompts for zero shot models.

+ Sentence-wise token indexes now available in MedicalNerModel annotator

+ We have also made fine-tuned improvements to core functionalities and corrected various bugs, enhancing the overall robustness and reliability of Spark NLP for Healthcare.

    - Enhanced Gender Awareness feature: Our improved Gender Awareness feature now comes with an extended faker list, ensuring more comprehensive and accurate gender identification.

    - Expanded English Faker Name List: We've broadened the range of our English Faker Name list, allowing for more diverse and inclusive data generation.

+ Updated notebooks and demonstrations: We're improving user experience with our updated notebooks and demonstrations, making Spark NLP for Healthcare easier to navigate and understand.

+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain.

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling a more efficient, accurate, and streamlined analysis of healthcare-related natural language data.

</div><div class="h3-box" markdown="1">

#### Newly Introduced Arabic De-Identification NER Models And Pretrained Pipelines

We're thrilled to present our newly-integrated Arabic deidentification Named Entity Recognition (NER) models, featuring two diverse approaches. The first model provides granular entity recognition with 17 entities, while the other offers a more generic approach, identifying 8 entities. These models are accompanied by corresponding pretrained pipelines that can be deployed in a streamlined one-liner format.

Designed explicitly for deidentification tasks in Arabic language, these models and pipelines leverage our proprietary dataset curation and specialized augmentation methods. This expansion broadens the linguistic scope of our toolset, underscoring our commitment to providing comprehensive solutions for global healthcare NLP needs.

| NER model                                  | pipeline | description                              |            predicted entities             |
|--------------------------------------------|----------|------------------------------------------|-------------------------------------------|
| [`ner_deid_subentity`](https://nlp.johnsnowlabs.com/2023/05/29/ner_deid_subentity_ar.html) | [`ner_deid_subentity_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/ner_deid_subentity_pipeline_ar.html) | This model/pipeline can detect protected health information (PHI) entities with 17 different labels.| `PATIENT`, `HOSPITAL`, `DATE`, `ORGANIZATION`, `CITY`, `STREET`, `USERNAME`, `SEX`, `IDNUM`, `EMAIL`, `ZIP`, `MEDICALRECORD`, `PROFESSION`, `PHONE`, `COUNTRY`, `DOCTOR`, `AGE` |
| [`ner_deid_generic`](https://nlp.johnsnowlabs.com/2023/05/30/ner_deid_generic_ar.html)     | [`ner_deid_generic_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/ner_deid_generic_pipeline_ar.html)  |  This model/pipeline can detect PHI entities with 8 different labels. | `CONTACT`, `NAME`, `DATE`, `ID`, `SEX`, `LOCATION`, `PROFESSION`, `AGE` |


*NER Model Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_deid_subentity", "ar", "clinical/models")\
        .setInputCols(["sentence","token","embeddings"])\
        .setOutputCol("ner")
```

*Pretrained Pipeline Examle*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("ner_deid_generic_pipeline", "ar", "clinical/models")

sample_text = '''
عالج الدكتور محمد المريض أحمد البالغ من العمر 55 سنة  في 15/05/2000  في مستشفى مدينة الرباط. رقم هاتفه هو  0610948235 وبريده الإلكتروني
mohamedmell@gmail.com.'''

```

*Result*:

|chunk                       |ner_label |
|---------------------------:|:---------|
|محمد                        |DOCTOR    |
|55 سنة                      |AGE       |
|15/05/2000                  |DATE      |
|الرباط                      |CITY      |
|0610948235                  |PHONE     |
|mohamedmell@gmail.com       |EMAIL     |

You can check the  [Multi Language Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb) for more examples and see the [NER DEMOGRAPHICS ARABIC](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/) demo.


</div><div class="h3-box" markdown="1">

#### New Medical Summarizer Model Fine-Tuned With A Custom Dataset To Minimize Clinical Jargon In Laymen Terms

We are delighted to announce the release of our [summarizer_clinical_laymen](https://nlp.johnsnowlabs.com/2023/05/29/summarizer_clinical_laymen_en.html) model, a refined variant of our Flan-T5 (LLM) based summarization model. This model has been carefully fine-tuned with a custom dataset curated by John Snow Labs, expressly designed to minimize the use of clinical terminology in the generated summaries. The summarizer_clinical_laymen model is capable of producing summaries of up to **512 tokens** from an input text of a maximum of 1024 tokens.

This innovation embodies our commitment to providing user-friendly and accessible NLP solutions, making it easier for non-clinical personnel and patients to comprehend medical summaries without losing critical information.

*Example*:

```python
summarizer = MedicalSummarizer.pretrained("summarizer_clinical_laymen", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxNewTokens(512)

text = """Jennifer was seen in my office for evaluation for elective surgical weight loss on October 6, 2008. ABC is a 34-year-old female with a BMI of 43. She is 5'6" tall and weighs 267 pounds. She is motivated to attempt surgical weight loss because she has been overweight for over 20 years and wants to have more energy and improve her self-image. She is not only affected physically, but also socially by her weight. When she loses weight she always regains it and she always gains back more weight than she has lost. At one time, she lost 100 pounds and gained the weight back within a year. She has tried numerous commercial weight loss programs including Weight Watcher's for four months in 1992 with 15-pound weight loss, RS for two months in 1990 with six-pound weight loss, Slim Fast for six weeks in 2004 with eight-pound weight loss, an exercise program for two months in 2007 with a five-pound weight loss, Atkin's Diet for three months in 2008 with a ten-pound weight loss, and Dexatrim for one month in 2005 with a five-pound weight loss. She has also tried numerous fat reduction or fad diets. She was on Redux for nine months with a 100-pound weight loss.\n\nPAST MEDICAL HISTORY: She has a history of hypertension and shortness of breath.\n\nPAST SURGICAL HISTORY: Pertinent for cholecystectomy.\n\nPSYCHOLOGICAL HISTORY: Negative.\n\nSOCIAL HISTORY: She is single. She drinks alcohol once a week. She does not smoke.\n\nFAMILY HISTORY: Pertinent for obesity and hypertension.\n\nMEDICATIONS: Include Topamax 100 mg twice daily, Zoloft 100 mg twice daily, Abilify 5 mg daily, Motrin 800 mg daily, and a multivitamin.\n\nALLERGIES: She has no known drug allergies.\n\nREVIEW OF SYSTEMS: Negative.\n\nPHYSICAL EXAM: This is a pleasant female in no acute distress. Alert and oriented x 3. HEENT: Normocephalic, atraumatic. Extraocular muscles intact, nonicteric sclerae. Chest is clear to auscultation bilaterally. Cardiovascular is normal sinus rhythm. Abdomen is obese, soft, nontender and nondistended. Extremities show no edema, clubbing or cyanosis.\n\nASSESSMENT/PLAN: This is a 34-year-old female with a BMI of 43 who is interested in surgical weight via the gastric bypass as opposed to Lap-Band. ABC will be asking for a letter of medical necessity from Dr. XYZ. She will also see my nutritionist and social worker and have an upper endoscopy. Once this is completed, we will submit her to her insurance company for approval."""
```

*Result*:

```This is a clinical note about a 34-year-old woman who is interested in having weight loss surgery. She has been overweight for over 20 years and wants to have more energy and improve her self-image. She has tried many diets and weight loss programs, but has not been successful in keeping the weight off. She has a history of hypertension and shortness of breath, but is not allergic to any medications. She will have an upper endoscopy and will be contacted by a nutritionist and social worker. The plan is to have her weight loss surgery through the gastric bypass rather than Lap-Band.```


</div><div class="h3-box" markdown="1">



#### New Medical Summarizer Pretrained Pipelines That Can Be Used In One Line

We are excited to announce the launch of seven new medical summarizer pretrained pipelines. These novel pipelines have been specifically developed to enable streamlined execution in a succinct one-liner format, eliminating the need to construct verbose pipelines.


| model name                                 | description                              |
|--------------------------------------------|------------------------------------------|
| [`summarizer_biomedical_pubmed_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_biomedical_pubmed_pipeline_en.html)           | Finetuned with biomedical datasets (Pubmed abstracts) by John Snow Labs  |
| [`summarizer_clinical_jsl_augmented_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_clinical_jsl_augmented_pipeline_en.html) | Finetuned with natural instructions and then finetuned with clinical notes, encounters, critical care notes, discharge notes, reports, curated  by John Snow Labs |
| [`summarizer_clinical_jsl_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_clinical_jsl_pipeline_en.html)                     | Summarize clinical notes, encounters, critical care notes, discharge notes, reports, etc.  |
| [`summarizer_clinical_questions_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_clinical_questions_pipeline_en.html)         | Finetuned with medical questions exchanged in clinical mediums (clinic, email, call center etc.) by John Snow Labs.  It generates question  |
| [`summarizer_generic_jsl_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_generic_jsl_pipeline_en.html)                       | Finetuned with additional data curated by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. |
| [`summarizer_radiology_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_radiology_pipeline_en.html)                           | Capable to summarizing radiology reports while preserving the important information such as imaging tests and findings.   |
| [`summarizer_clinical_guidelines_large_pipeline`](https://nlp.johnsnowlabs.com/2023/05/31/summarizer_clinical_guidelines_large_pipeline_en.html) | Finetuned to summarize clinical guidelines (only for Asthma and Breast Cancer as of now) into four different sections: Overview, Causes, Symptoms, Treatments. |



*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("summarizer_clinical_guidelines_large_pipeline", "en", "clinical/models")

text = """Clinical Guidelines for Breast Cancer:
Breast cancer is the most common type of cancer among women. It occurs when the cells in the breast start growing abnormally, forming a lump or mass. This can result in the spread of cancerous cells to other parts of the body. Breast cancer may occur in both men and women but is more prevalent in women.
The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy
Breast cancer may not present symptoms during its early stages. Symptoms typically manifest as the disease progresses. Some notable symptoms include:
- A lump or thickening in the breast or underarm area
- Changes in the size or shape of the breast
- Nipple discharge
- Nipple changes in appearance, such as inversion or flattening
- Redness or swelling in the breast
Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include:
- Surgery (such as lumpectomy or mastectomy)
- Radiation therapy
- Chemotherapy
- Hormone therapy
- Targeted therapy
Early detection is crucial for the successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40. If you notice any changes in your breast tissue, consult with your healthcare provider immediately.
"""
```

*Result*:

```
Overview of the disease: Breast cancer is the most common type of cancer among women, occurring when the cells in the breast start growing abnormally, forming a lump or mass. It can result in the spread of cancerous cells to other parts of the body.

Causes: The exact cause of breast cancer is unknown, but several risk factors can increase the likelihood of developing it, such as a personal or family history, a genetic mutation, exposure to radiation, age, early onset of menstruation or late menopause, obesity, and hormonal factors.

Symptoms: Symptoms of breast cancer typically manifest as the disease progresses, including a lump or thickening in the breast or underarm area, changes in the size or shape of the breast, nipple discharge, nipple changes in appearance, and redness or swelling in the breast.

Treatment recommendations: Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include surgery, radiation therapy, chemotherapy, hormone therapy, and targeted therapy. Early detection is crucial for successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40.

```


</div><div class="h3-box" markdown="1">


#### Updated ICD-10-CM Resolver And Chunk Mapper Models Aligning With The Latest Updates In The ICD-10-CM Terminology To Ensure Unparalleled Accuracy In Clinical Coding.

New and updated ICD-10-CM sentence entity resolver and chunk mapper models provide enhanced accuracy and comprehensive concept recognition for effective coding and medical condition classification. These models were trained based on the latest version of ICD-10-CM release (April 1, 2023).

Here are the updated ICD-10-CM sentence entity resolver and chunk mapper models.

| model name                                 |  type        | description                              |
|--------------------------------------------|--------------|------------------------------------------|
| [`icd10cm_mapper`](https://nlp.johnsnowlabs.com/2023/05/30/icd10cm_mapper_en.html)                       | chunk mapper | Maps medical entities with their corresponding ICD-10-CM codes.  |
| [`icd10cm_billable_hcc_mapper`](https://nlp.johnsnowlabs.com/2023/05/26/icd10cm_billable_hcc_mapper_en.html)                       | chunk mapper | Maps ICD-10-CM codes with their corresponding billable and HCC scores. If there is no HCC score for the corresponding ICD-10-CM code, result will be returned as 0.|
| [`sbiobertresolve_hcc_augmented`](https://nlp.johnsnowlabs.com/2023/05/31/sbiobertresolve_hcc_augmented_en.html)        |     resolver | Maps medical entities to Hierarchical Condition Categories (HCC) codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.  |
| [`sbiobertresolve_icd10cm_augmented`](https://nlp.johnsnowlabs.com/2023/05/31/sbiobertresolve_icd10cm_augmented_en.html)           |    resolver | Maps medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings.  |
| [`sbiobertresolve_icd10cm_augmented_billable_hcc`](https://nlp.johnsnowlabs.com/2023/05/31/sbiobertresolve_icd10cm_augmented_billable_hcc_en.html)           |    resolver | Maps medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings and it supports 7-digit codes with HCC status. |
| [`sbiobertresolve_icd10cm_generalised_augmented`](https://nlp.johnsnowlabs.com/2023/05/31/sbiobertresolve_icd10cm_generalised_augmented_en.html)           |    resolver | Maps medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It predicts ICD-10-CM codes up to 3 characters (according to ICD-10-CM code structure the first three characters represent general type of the injury or disease). |
| [`sbiobertresolve_icd10cm_slim_billable_hcc`](https://nlp.johnsnowlabs.com/2023/05/31/sbiobertresolve_icd10cm_slim_billable_hcc_en.html)           |    resolver | Maps medical entities to ICD-10-CM codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings and it supports 7-digit codes with HCC status. In this model, synonyms having low cosine similarity to unnormalized terms are dropped. |
| [`sbertresolve_icd10cm_slim_billable_hcc`](https://nlp.johnsnowlabs.com/2023/05/31/sbertresolve_icd10cm_slim_billable_hcc_en.html)           |    resolver | Maps medical entities to ICD-10-CM codes using `sbert_jsl_medium_uncased` Sentence Bert Embeddings and it supports 7-digit codes with HCC status. In this model, synonyms having low cosine similarity to unnormalized terms are dropped. |
| [`sbertresolve_icd10cm_augmented_billable_hcc`](https://nlp.johnsnowlabs.com/2023/05/31/sbertresolve_icd10cm_augmented_billable_hcc_en.html)           |    resolver | maps clinical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings and it supports 7-digit codes with HCC status. It also returns the official resolution text within the brackets inside the metadata. |
| [`sbertresolve_icd10cm_augmented`](https://nlp.johnsnowlabs.com/2023/05/31/sbertresolve_icd10cm_augmented_en.html)           |    resolver | Maps medical entities and concepts to ICD-10-CM codes using `sbert_jsl_medium_uncased` sentence bert embeddings. It also returns the official resolution text within the brackets inside the metadata.  |

*Mapper Example*:

```python
chunkMapper= ChunkMapperModel().pretrained("icd10cm_billable_hcc_mapper", "en", "clinical/models")\
     .setInputCols(["chunk"])\
     .setOutputCol("mappings")\
     .setRels(["billable", "hcc_score"]) \
     .setLowerCase(True) \
     .setMultivaluesRelations(True)

sample_icd_codes= ["D66", "S22.00", "Z3A.10"]
```

*Result*:



| icd10cm_code | billable | hcc_score |
|--------------|----------|-----------|
| D66          | 1        | 46        |
| S22.00       | 0        | 0         |
| Z3A.10       | 1        | 0         |


*Resolver Example*:

```python
icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

sample_text = "The patient has a gestational diabetes mellitus history and subsequent type two diabetes mellitus, associated with obesity, presented with a one-week history of poor appetite, and vomiting."
```

*Result*:

| ner_chunk                             | icd10cm_code | resolution                                                                    | billable_status | hcc_status | hcc_score |
|---------------------------------------|--------------|-------------------------------------------------------------------------------|-----------------|------------|-----------|
| gestational diabetes mellitus         | O24.4        | gestational diabetes mellitus [gestational diabetes mellitus]                 | 0               | 0          | 0         |
| subsequent type two diabetes mellitus | O24.11       | pre-existing type 2 diabetes mellitus [pre-existing type 2 diabetes mellitus] | 0               | 0          | 0         |
| obesity                               | E66.9        | obesity [obesity, unspecified]                                                | 1               | 0          | 0         |
| poor appetite                         | R63.0        | poor appetite [anorexia]                                                      | 1               | 0          | 0         |
| vomiting                              | R11.1        | vomiting [vomiting]                                                           | 0               | 0          | 0         |





</div><div class="h3-box" markdown="1">


#### A New Voice Of Patient (VOP) Medical Classifier Model Focusing On The Side Effect Classification Of Treatments And Procedures In Patients' Own Words

We have a new VOP classification model that classifies the patients' expressions in order to determine if they make any references to the side effects associated with medical treatments or procedures.

- [bert_sequence_classifier_vop_side_effect](https://nlp.johnsnowlabs.com/2023/05/24/bert_sequence_classifier_vop_side_effect_en.html): This model is a [BioBERT based](https://github.com/dmis-lab/biobert) classifier that classifies texts written by patients as True if side effects from treatments or procedures are mentioned.

*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained("bert_sequence_classifier_vop_side_effect", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")
```

*Result*:

|text                                                          |result |
|--------------------------------------------------------------|-------|
|I felt kind of dizzy after taking that medication for a month.| True  |
|I had a dental procedure last week and everything went well.  | False |


</div><div class="h3-box" markdown="1">




#### Enhanced Social Determinants Of Health (SDOH) Classifier Models For Detecting Patients' Situation According To Certain Conditions (Under Treatment Or Not, Suffering From Housing Insecurity)

We have updated SDOH classification models to offer improved accuracy.

- `genericclassifier_sdoh_under_treatment_sbiobert_cased_mli`: This Generic Classifier model is intended for detecting if the patient is under treatment or not. If under treatment is not mentioned in the text, it is regarded as “Not_Under_Treatment_Or_Not_Mentioned”. The model is trained by using GenericClassifierApproach annotator. `Under_Treatment`: The patient is under treatment. `Not_Under_Treatment_Or_Not_Mentioned`: The patient is not under treatment or it is not mentioned in the clinical notes


*Example*:

```python
generic_classifier = GenericClassifierModel\
    .pretrained("genericclassifier_sdoh_under_treatment_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

text_list = ["Patient is a 50-year-old male who was diagnosed with hepatitis C. He has received a treatment plan that includes medication and regular monitoring of his liver function.",
"Patient has been living with chronic migraines for several years. She has not pursued any specific treatment for her migraines and has been managing her condition through lifestyle modifications such as stress reduction techniques and avoiding triggers."]
```

*Result*:

|                                                                                                text  |                               result |
|------------------------------------------------------------------------------------------------------|--------------------------------------|
| Patient is a 50-year-old male who was diagnosed with hepatitis C. He has received a treatment pla... |                      Under_Treatment |
| Patient has been living with chronic migraines for several years. She has not pursued any specifi... | Not_Under_Treatment_Or_Not_Mentioned |


- `genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli`: This Generic Classifier model is intended for detecting whether the patient has housing insecurity. If the clinical note includes patient housing problems, the model identifies it. If there is no housing issue or it is not mentioned in the text, it is regarded as “no housing insecurity”. The model is trained by using GenericClassifierApproach annotator. `Housing_Insecurity`: The patient has housing problems. `No_Housing_Insecurity_Or_Not_Mentioned`: The patient has no housing problems or it is not mentioned in the clinical notes.

*Example*:

```python
generic_classifier = GenericClassifierModel\
    .pretrained("genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

text_list = [
"Patient is a 50-year-old male who no has stable housing. He recently underwent a hip replacement surgery and has made a full recovery. ",
"Patient is a 25-year-old female who has her private housing. She presented with symptoms of a urinary tract infection and was diagnosed with the condition. Her living situation has allowed her to receive prompt medical care and treatment, and she has made a full recovery. "]
```

*Result*:

|                                                                                               text   |                                 result |
|------------------------------------------------------------------------------------------------------|----------------------------------------|
| Patient is a 50-year-old male who no has stable housing. He recently underwent a hip replacement ... |                     Housing_Insecurity |
| Patient is a 25-year-old female who has her private housing. She presented with symptoms of a uri... | No_Housing_Insecurity_Or_Not_Mentioned |






</div><div class="h3-box" markdown="1">


#### Introducing The Innovative `Nertemplaterender` Annotator To Generate Customized Prompts For Zero Shot Models

The New Annotator `NerTemplateRender` function is designed to render templates by permuting chunks of text when there is an excess of text available to fill the template. This annotator provides flexibility in rendering templates by permuting, combining, and resampling chunks of text based on the specified options, ensuring efficient utilization of available text resources. It provides several options for customizing the rendering process, here are the parameters:

- `setTemplates`: Sets The list of scope fields to consider when making entity tuples to render the templates. " + "The scope fields are the metadata keys containing the scope index or name for each chunk. " + "i.e. `sentence`, `paragraph`, `section` ...
- `setPermuteEntities`: Sets True if you want to permute chunks when the text has more than enough to fill the template, generating even more outputs. Overrides `combineEntities`
- `setCombineEntities`: "Sets True if you want to combine chunks when the text has more than enough to fill the template, generating more outputs
- `setResampleEntities`: Sets True if you want to resample entities from texts that do not have enough chunks to fill a template


*Example*:

```python
NerTemplateRender = NerTemplateRenderModel()\
  .setInputCols("chunk_deid")\
  .setOutputCol("templates")\
  .setTemplates(["When {{PATIENT}} {{ADMISSION}} ?",
                "What medication did {{DOCTOR}} prescribe for {{PROBLEM}}?",
                "Which hospital was {{PATIENT}} admitted to for {{PROBLEM}}?",
                "Why were {{PATIENT}} admitted to {{CLINICAL_DEPT}} on {{DATE}} by {{DOCTOR}}?" ])\
    .setPermuteEntities(True)\
    .setResampleEntities(True)

data = spark.createDataFrame([
    ["John Smith was admitted Sep 3rd to Mayo Clinic"],
    ["Dr. David pescribed metformin 500mg for my severe headache."],
    ["Olivia was admitted to the Memorial Hospital for her colon cancer."],
    ["27 years old Anne was admitted to clinic on Sep 1st by Dr. Jennifer for a right-sided pleural effusion for thoracentesis."]].toDF("text")


```

*Result*:


|                                                                    result|template|
|--------------------------------------------------------------------------|--------|
|                                                When John Smith admitted ?|       1|
|               What medication did David prescribe for my severe headache?|       2|
|               Which hospital was Olivia admitted to for her colon cancer?|       3|
|                                                    When Olivia admitted ?|       1|
|   Which hospital was Anne admitted to for a right-sided pleural effusion?|       3|
|What medication did Jennifer prescribe for a right-sided pleural effusion?|       2|
|                  Why were Anne admitted to clinic on Sep 1st by Jennifer?|       4|
|                                                      When Anne admitted ?|       1|


</div><div class="h3-box" markdown="1">


#### Sentence-Wise Token Indexes Are Now Avaliable In `MedicalNerModel` Annotator


The `MedicalNerModel` now includes a new parameter called `setSentenceTokenIndex` which allows you to obtain the token index at the sentence level. This parameter provides a convenient way to retrieve the specific token index associated with each sentence in the medical text. By using this parameter, you can easily identify and locate tokens within a sentence, enabling more granular analysis and processing of medical text data.

*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\
    .setSentenceTokenIndex(True)

sample_text = """He had a nonproductive cough that started last week.
He had chest pain with a fever since yesterday."""
```

*Result*:

|        token|ner_label|confidence|sentence_token_index|sentence|
|-------------|---------|----------|--------------------|--------|
|           He|        O|    0.9999|                   0|       0|
|          had|        O|    0.9996|                   1|       0|
|            a|B-PROBLEM|    0.9406|                   2|       0|
|nonproductive|I-PROBLEM|    0.9605|                   3|       0|
|        cough|I-PROBLEM|    0.9872|                   4|       0|
|         that|        O|    0.9559|                   5|       0|
|      started|        O|    0.9945|                   6|       0|
|         last|        O|    0.9863|                   7|       0|
|         week|        O|    0.4276|                   8|       0|
|            .|        O|    0.9999|                   9|       0|
|           He|        O|    0.9998|                   0|       1|
|          had|        O|    0.9988|                   1|       1|
|        chest|B-PROBLEM|    0.9978|                   2|       1|
|         pain|I-PROBLEM|    0.9974|                   3|       1|
|         with|        O|    0.9998|                   4|       1|
|            a|B-PROBLEM|    0.9527|                   5|       1|
|        fever|I-PROBLEM|    0.9907|                   6|       1|
|        since|        O|    0.9999|                   7|       1|
|    yesterday|        O|    0.9176|                   8|       1|
|            .|        O|    0.9999|                   9|       1|


</div><div class="h3-box" markdown="1">

#### We Have Also Made Fine-Tuned Improvements To Core Functionalities And Corrected Various Bugs, Enhancing The Overall Robustness And Reliability Of Spark Nlp For Healthcare

- Enhanced Gender Awareness feature: Our improved Gender Awareness feature now comes with an extended faker list, ensuring more comprehensive and accurate gender identification.
- Expanded English Faker Name List: We've broadened the range of our English Faker Name list, allowing for more diverse and inclusive data generation.



</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations: We'Re Improving User Experience With Our Updated Notebooks And Demonstrations, Making Spark Nlp For Healthcare Easier To Navigate And Understand


- Updated [Multi Language Deidentification Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb) notebook for lastest models
- New [MEDICAL SUMMARIZATION GUIDELINES](https://demo.johnsnowlabs.com/healthcare/MEDICAL_SUMMARIZATION_GUIDELINES/) demo
- New [DEID CONSISTENCY](https://demo.johnsnowlabs.com/healthcare/DEIDENTIFICATION_CONSISTENCY/) demo
- New [NER DEMOGRAPHICS ARABIC](https://demo.johnsnowlabs.com/healthcare/NER_DEMOGRAPHICS_AR/) demo



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `summarizer_clinical_laymen`
+ `bert_sequence_classifier_vop_side_effect`
+ `ner_deid_subentity` -> `ar`
+ `ner_deid_generic` -> `ar`
+ `ner_deid_subentity_pipeline` -> `ar`
+ `ner_deid_generic_pipeline` -> `ar`
+ `summarizer_radiology_pipeline`
+ `summarizer_generic_jsl_pipeline`
+ `summarizer_clinical_jsl_pipeline`
+ `summarizer_biomedical_pubmed_pipeline`
+ `summarizer_clinical_questions_pipeline`
+ `summarizer_clinical_jsl_augmented_pipeline`
+ `summarizer_clinical_guidelines_large_pipeline`
+ `icd10cm_billable_hcc_mapper`
+ `icd10cm_mapper`
+ `sbiobertresolve_hcc_augmented`
+ `sbiobertresolve_icd10cm_augmented`
+ `sbiobertresolve_icd10cm_augmented_billable_hcc`
+ `sbiobertresolve_icd10cm_generalised_augmented`
+ `sbiobertresolve_icd10cm_slim_billable_hcc`
+ `sbertresolve_icd10cm_augmented`
+ `sbertresolve_icd10cm_augmented_billable_hcc`
+ `sbertresolve_icd10cm_slim_billable_hcc`
+ `genericclassifier_sdoh_under_treatment_sbiobert_cased_mli`
+ `genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli`
+ `ner_ade_emb_clinical_large`
+ `ner_ade_emb_clinical_medium`
+ `ner_cellular_emb_clinical_large`
+ `ner_cellular_emb_clinical_medium`
+ `ner_bacterial_species_emb_clinical_large`
+ `ner_bacterial_species_emb_clinical_medium`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)



</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
