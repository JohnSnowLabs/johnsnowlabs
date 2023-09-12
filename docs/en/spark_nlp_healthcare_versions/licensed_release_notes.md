---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-09-04
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.1.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first clinical NER models in 5 new languages as well as 22 new clinical pretrained models and pipelines**. 

+ 5 new clinical NER models for extracting clinical entities in the French, Italian, Polish, Spanish, and Turkish languages
+ Introducing the pretrained `ContextualParserModel` to allow saving & loading rule based NER models and releasing the first date-of-birth NER model
+ 3 new text classification models for classifying complaints and positive emotions in clinical texts
+ 6 new augmented NER models by leveraging the capabilities of the **LangTest** library to significantly boost their robustness
+ Improved the `RelationExtractionModel` annotator by enabling the selection of single or multiple labels in outputs and providing customizable feature scaling techniques
+ Improved consistency of names during the deidentification process, regardless of variations in casing or altered token sequences
+ Enhancing `Text2SQL` with custom schemas and releasing the first pretrained zero-shot Text2SQL Model for single tables.
+ Enhancements in Text2SQL: `tableLimit` and `postProcessingSubstitutions` parameters, and expanded variable support
+ Revamped the method names within the `ocr_nlp_processor` module and incorporated functionality to create colorful overlay bands using RGB codes over identified entities
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - The option to remove scope window constraints in the `AssertionDLModel` is now accessible by setting it to `[-1, -1]`, default is `[9, 15]`
+ Updated notebooks
  - Updated [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) with new CP model example
  - Updated [Spark OCR Utility Module Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb) with the new updates in `ocr_nlp_processor` module
  - Updated [Text To SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) with new single tables model
+ New demos
  - New [Multi-Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/)
  - New [ASSERTION_SDOH Demo](https://demo.johnsnowlabs.com/healthcare/ASSERTION_SDOH/)
  - New [ASSERTION_VOP Demo](https://demo.johnsnowlabs.com/healthcare/ASSERTION_VOP/)
  - New [TEXT2SQL Demo](https://demo.johnsnowlabs.com/healthcare/TEXT2SQL/)
  - New [CLASSIFICATION LITCOVID Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_LITCOVID/)
  - New [PATIENT COMPLAINT CLASSIFICATION Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_PATIENT_COMPLAINT/)
  - Updated [Age Group Classification Demo](https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_AGE/) 
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.

</div><div class="h3-box" markdown="1">

#### 5 New Clinical NER Models for Extracting Clinical Entities in the French, Italian, Polish, Spanish, and Turkish languages

5 new Clinical NER models provide valuable tools for processing and analyzing multi-language clinical texts. They assist in automating the extraction of important clinical information, facilitating research, medical documentation, and other applications within the multi-language healthcare domain.

| Model Name   Lang | Predicted Entities     | Language |
|--------------------|------------------------|---|
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/30/ner_clinical_es.html)   | `PROBLEM` `TEST` `TREATMENT` | es |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/30/ner_clinical_fr.html)   | `PROBLEM` `TEST` `TREATMENT` | fr |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/30/ner_clinical_it.html)   | `PROBLEM` `TEST` `TREATMENT` | it |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_pl.html)   | `PROBLEM` `TEST` `TREATMENT` | pl |
| [ner_clinical](https://nlp.johnsnowlabs.com/2023/08/29/ner_clinical_tr.html)   | `PROBLEM` `TEST` `TREATMENT` | tr |


*Example*:

```python

ner_model = MedicalNerModel.pretrained("ner_clinical", "tr", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_text = """Hasta sıcak ve soğuk yiyecekler yerken diş hassasiyetinden şikayetçiydi. Olası çürük veya diş kökü problemlerini değerlendirmek için klinik ve radyografik muayene yapıldı ve diş köküne yakın bir boşluk tespit edildi. Sorunu gidermek için restoratif tedavi uygulandı."""
```

*Result*:

|chunk                                  |begin|end|ner_label|
|---------------------------------------|-----|---|---------|
|soğuk yiyecekler yerken diş hassasiyeti|18   |56 |PROBLEM  |
|radyografik muayene                    |144  |162|TEST     |
|restoratif tedavi                      |234  |250|TREATMENT|


Please check: [Multi-Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/)

</div><div class="h3-box" markdown="1">

#### Introducing the Pretrained `ContextualParserModel` to Allow Saving & Loading Rule Based NER Models and Releasing the First Date-of-Birth NER Model 

Now you can save your  `ContextualParserModel` models without exposing & sharing the rule sets and load back later on. We also release the first pretrained `ContextualParserModel` that can extract date-of-birth (DOB) entities in clinical texts.

*Example*:

```python
dob_contextual_parser = ContextualParserModel.pretrained("date_of_birth_parser", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_dob") 

text = """
Record date : 2081-01-04 
DB : 11.04.1962
DT : 12-03-1978 
DOD : 10.25.23 

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988. 

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""
```

*Result*:

|sentence_id|chunk           |begin|end|ner_label|
|-----------|----------------|-----|---|---------|
|1          |11.04.1962      |32   |41 |DOB      |
|3          |Nov 04, 1962    |109  |120|DOB      |
|4          |November 4, 1962|241  |256|DOB      |
|5          |11-04-1962      |297  |306|DOB      |


please check: [Model Card](https://nlp.johnsnowlabs.com/2023/08/22/date_of_birth_parser_en.html) and [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) for more information




</div><div class="h3-box" markdown="1">

#### 3 New Text Classification Models for Classifying Complaints and Positive Emotions in Clinical Texts

Introducing three novel text classification models tailored for healthcare contexts, specifically designed to differentiate between expressions of `Complaint` – characterized by negative or critical language reflecting dissatisfaction with healthcare experiences – and `No_Complaint` – denoting positive or neutral sentiments without any critical elements. These models offer enhanced insights into patient feedback and emotions within the healthcare domain.

| Model Name  | Predicted Entities     | Annotator
|--------------------|------------------------|---|
| [few_shot_classifier_patient_complaint_sbiobert_cased_mli](https://nlp.johnsnowlabs.com/2023/08/30/few_shot_classifier_patient_complaint_sbiobert_cased_mli_en.html)   | `Complaint` `No_Complaint` | FewShotClassifierModel |
| [bert_sequence_classifier_patient_complaint](https://nlp.johnsnowlabs.com/2023/08/31/bert_sequence_classifier_patient_complaint_en.html)   | `Complaint`, `No_Complaint` | MedicalBertForSequenceClassification |
| [genericclassifier_patient_complaint_sbiobert_cased_mli](https://nlp.johnsnowlabs.com/2023/08/31/patient_complaint_classifier_generic_bert_M1_en.html)   | `Complaint` `No_Complaint` | GenericClassifierModel |


*Example*:

```python

sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained("bert_sequence_classifier_patient_complaint", "en", "clinical/models")\
    .setInputCols(["document",'token'])\
    .setOutputCol("prediction")

sample_text = [
    ["""The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, knowledgeable and friendly.  This hospital site has plenty of parking"""],
    ["""My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad couldn’t breath good while the staff seem not to care and when they got to us they said they we’re gonna a take some blood samples and they made us wait again and to see the staff workers talking to each other and laughing taking there time and not seeming to care about there patience, while we were in the lobby there was another guy who told us they also made him wait while he can hardly breath and they left him there to wait my girl dad is coughing and not doing better and when the lady came in my girl dad didn’t have his shirt because he was hot and the lady came in said put on his shirt on and then left still waiting to get help rn"""]
    ]
```

*Result*:

|                text|        result|
|--------------------|--------------|
|The Medical Center is a large state of the art hospital facility with great doctors, nurses, technicians and receptionists.  Service is top notch, ...| No_Complaint |
|My gf dad wasn’t feeling well so we decided to take him to this place cus it’s his insurance and we waited for a while and mind that my girl dad co...|    Complaint |



</div><div class="h3-box" markdown="1">



#### 6 New Augmented NER Models by Leveraging the Capabilities of the LangTest Library to Significantly Boost Their Robustness

Newly introduced augmented NER models namely [ner_events_clinical_langtest](https://nlp.johnsnowlabs.com/2023/08/31/ner_events_clinical_langtest_en.html), [ner_oncology_anatomy_general_langtest](https://nlp.johnsnowlabs.com/2023/09/03/ner_oncology_anatomy_general_langtest_en.html), [ner_oncology_anatomy_granular_langtest](https://nlp.johnsnowlabs.com/2023/09/03/ner_oncology_anatomy_granular_langtest_en.html),  [ner_oncology_demographics_langtest](https://nlp.johnsnowlabs.com/2023/09/03/ner_oncology_demographics_langtest_en.html), [ner_oncology_posology_langtest](https://nlp.johnsnowlabs.com/2023/09/04/ner_oncology_posology_langtest_en.html), and [ner_oncology_response_to_treatment_langtest](https://nlp.johnsnowlabs.com/2023/09/04/ner_oncology_response_to_treatment_langtest_en.html) are powered by the innovative LangTest library. This cutting-edge NLP toolkit is at the forefront of language processing advancements, incorporating state-of-the-art techniques and algorithms to enhance the capabilities of our models significantly.

- These models are strengthened against various perturbations (lowercase, uppercase, titlecase, punctuation removal, etc.), and the previous and new robustness scores are presented below
  
| model names          | original robustness  | new robustness |
|---------------------------------------------|--------|-------|
| ner_oncology_anatomy_granular_langtest      | 0.79   | 0.89  |
| ner_oncology_response_to_treatment_langtest | 0.76   | 0.90  |
| ner_oncology_demographics_langtest          | 0.81   | 0.95  |
| ner_oncology_anatomy_general_langtest       | 0.79   | 0.81  |
| ner_oncology_posology_langtest              | 0.74   | 0.85  |
| ner_events_clinical_langtest                | 0.71   | 0.80  |

*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_events_clinical_langtest", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

text = "The patient presented to the emergency room last evening"
```


*Result*:

|chunk             |ner_label    |
|------------------|-------------|
|presented         |EVIDENTIAL   |
|the emergency room|CLINICAL_DEPT|
|last evening      |DATE         |



</div><div class="h3-box" markdown="1">


#### Improved the `RelationExtractionModel` Annotator by Enabling the Selection of Single or Multiple Labels in Outputs and Providing Customizable Feature Scaling Techniques

The `RelationExtractionModel` annotator is now equipped with the `setMultiClass()` method, which provides the option to specify whether the model should return only the label with the highest confidence score or include all labels in its output. Furthermore, the model offers the `setFeatureScaling()` method, granting the ability to apply different feature scaling techniques such as `zscore`, `minmax` or `empty` (no scaling).

*setFeatureScaling Example*:

```python
reModel = RelationExtractionModel.pretrained("re_ade_clinical", "en", 'clinical/models')\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(10)\
    .setRelationPairs(["drug-ade, ade-drug"])\
    .setFeatureScaling("zscore") # or minmax

text = "I experienced fatigue, aggression, and sadness after taking Lipitor but no more adverse after passing Zocor."
```


*Result*:

| index | chunk1     | entity1 | chunk2   | entity2 | relation | zscore | minmax |
|-------|------------|---------|----------|---------|----------|--------|--------|
| 0     | fatigue    | ADE     | Lipitor  | DRUG    | 0        | 0.9964 | 0.9983 |
| 1     | Zocor      | DRUG    | fatigue  | ADE     | 0        | 0.9884 | 0.9341 |
| 2     | aggression | ADE     | Lipitor  | DRUG    | 1        | 0.6123 | 0.9999 |
| 3     | Zocor      | DRUG    | aggression | ADE   | 0        | 0.9972 | 0.9833 |
| 4     | sadness    | ADE     | Lipitor  | DRUG    | 1        | 0.9999 | 0.9644 |
| 5     | Zocor      | DRUG    | sadness  | ADE     | 1        | 0.9080 | 0.9644 |


*setFeatureScaling Example*:

```python
reModel = RelationExtractionModel.pretrained("re_clinical", "en", "clinical/models")\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setMaxSyntacticDistance(10)\
    .setRelationPairs(["problem-test", "problem-treatment"])\
    .setMultiClass(True) # or Default value is False

text = """
A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation, associated with obesity with a body mass index ( BMI ) of 33.5 kg/m2 .
"""
```


*setMultiClass(False) Result*:

| chunk1                        | entity1 | chunk2 | entity2 | relation | confidence |
|-------------------------------|---------|--------|---------|----------|------------|
| gestational diabetes mellitus | PROBLEM | BMI    | TEST    | TeRP     | 1.0        |


*setMultiClass(True) Result*:
| chunk1                        | entity1 | chunk2 | entity2 | relation | confidence |
|-------------------------------|---------|--------|---------|----------|------------|
| gestational diabetes mellitus | PROBLEM | BMI    | TEST    | TeRP     | TeRP_confidence: 1.0 <br> TrCP_confidence: 0.0, <br>   TeCP_confidence: 2.36E-35 <br> TrAP_confidence: 8.85E-32 <br> TrWP_confidence: 1.16E-34 <br> TrNAP_confidence: 0.0 <br>   TrIP_confidence: 0.0 <br> PIP_confidence: 1.87E-28 <br> O_confidence: 9.56E-13 <br>      |


</div><div class="h3-box" markdown="1">

####  Improved Consistency of Names During the Deidentification Process, Regardless of Variations in Casing or Altered Token Sequences

The `Deidentification` annotator maintains consistent name handling in its `obfuscation` mode, even when the same name appears in different formats, such as varying casing or altered token orders. This ensures that names remain consistently protected regardless of their presentation within the text.

*Example*:

```python
deidentification = DeIdentification() \
      .setInputCols(["sentence", "token", "ner_chunk"]) \
      .setOutputCol("deidentified") \
      .setMode("obfuscate")

sample_text = """Patient Name: SULLAVAN, John K, MRN: 123456
SULLAVAN, JOHN K, Male, 05/09/1985
John K Sullavan is 25 years old patient has heavy back pain started from last week.
"""
```

*Results*:

|sentence|masked|deidentified|
|--------|------|------------|
|Patient Name: SULLAVAN, John K, MRN: 123456|Patient Name: \<PATIENT\> MRN: \<MEDICALRECORD\>|Patient Name: Viviann Spare MRN: 376947|
|SULLAVAN, JOHN K, Male, 05/09/1985|\<PATIENT\>, Male, \<DATE\>|Viviann Spare, Male, \<DATE\>|
|John K Sullavan is 25 years old patient has heavy back pain started from last week\.|\<PATIENT\> is \<AGE\> years old patient has heavy back pain started from last week\.|Viviann Spare is 20 years old patient has heavy back pain started from last week\.|

</div><div class="h3-box" markdown="1">


####  Enhancing `Text2SQL` with Custom Schemas and Releasing the First Pretrained Zero-Shot Text2SQL Model for Single Tables.

Utilizing [text2sql_with_schema_single_table](https://nlp.johnsnowlabs.com/2023/09/02/text2sql_with_schema_single_table_en.html) to generate SQL queries from natural language queries and custom database schemas featuring single tables. Powered by a large-scale finetuned language model developed by John Snow Labs on single-table schema data

*Example*:

```python

query_schema = {"patient": ["ID","Name","Age","Gender","BloodType","Weight","Height","Address","Email","Phone"] }

text2sql_with_schema_single_table = Text2SQL.pretrained("text2sql_with_schema_single_table", "en", "clinical/models")\
    .setMaxNewTokens(200)\
    .setSchema(query_schema)\
    .setInputCols(["document"])\
    .setOutputCol("sql_query")

sample_text = """ Calculate the average age of patients with blood type 'A-' """
```

*Results*:
```bash
SELECT AVG(Age)
FROM patient
WHERE BloodType = "A-"
```

please check: [Model Card](https://nlp.johnsnowlabs.com/2023/09/02/text2sql_with_schema_single_table_en.html) and [Text To SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) for more information


</div><div class="h3-box" markdown="1">


#### Enhancements in Text2SQL: `tableLimit` and `postProcessingSubstitutions` Parameters, and Expanded Variable Support

You can use the following code to replace particular strings with other strings in the generated sequence:

```python
text2sql_with_schema_single_table.setPostProcessingSubstitutions({
    'greater than': '>', 
    'not equal to': '<>', 
    'less than or equal to': '<=', 
    'superior': '>', 
    'inferior': '<', 
    'greater than or equal to': '>=', 
    'inferior or equal': '<=', 
    'superior or equal': '>=', 
    'equal to': '=', 
    'less than': '<'
})
```

Variables which can be used in the prompt template:
 
```bash
  "{tables_list}": comma separated list of tables

  "{tables}": comma separated list of tables with column names

  "{table1_name}", "{table2_name}", ... names of particular tables.

  "{table1_columns}", "{table2_columns}", ... comma separated lists of columns in particular tables.
```

see [Text To SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) for more information        


</div><div class="h3-box" markdown="1">

#### Revamped the Method Names Within the `ocr_nlp_processor` Module and Incorporated Functionality to Create Colorful Overlay Bands Using RGB Codes Over Identified Entities

We've modified the method names in the `ocr_nlp_processor` module and introduced the capability to specify RGB codes for overlaying colorful bands on entities. This allows improved readability for color-blind individuals when viewing deidentified PDF files if you set it `box_color = (115, 203, 235)` (“115” Red, “203” Green, “235” Blue). 

`ocr_nlp_processor` Methods:

|Previous|Now|
|-|-|
|black_band|colored_box|
|colored_box|bounding_box|
|highlight|highlight|

*Example*:

```python
from sparknlp_jsl.utils.ocr_nlp_processor import ocr_entity_processor

ocr_entity_processor(spark=spark,
                    file_path = path,
                    ner_pipeline = nlp_model,
                    chunk_col = "merged_chunk",
                    style = box,
                    save_dir = "deidentified_pdfs",
                    box_color= (115, 235, 255),
                    label= True,
                    label_color = "red",
                    resolution=100,
                    display_result = True)
```

#### Various Core Improvements; Bug Fixes, Enhanced Overall Robustness and Reliability of Spark NLP for Healthcare

- The option to remove scope window constraints in the `AssertionDLModel` is now accessible by setting it to `[-1, -1]`, default is `[9, 15]`



#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- Updated [Contextual Parser Rule Based NER Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb) with new CP model example
- Updated [Spark OCR Utility Module Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/5.3.Spark_OCR_Utility_Module.ipynb) with the new updates in `ocr_nlp_processor` module
- Updated [Text To SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) with new single tables model
- New [Multi-Language Clinical NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/)
- New [Social Determinants of Health Assertion  Demo](https://demo.johnsnowlabs.com/healthcare/ASSERTION_SDOH/)
- New [Voice of Patients Assertion Demo](https://demo.johnsnowlabs.com/healthcare/ASSERTION_VOP/)
- New [TEXT2SQL Demo](https://demo.johnsnowlabs.com/healthcare/TEXT2SQL/)
- New [CLASSIFICATION LITCOVID Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_LITCOVID/)
- New [PATIENT COMPLAINT CLASSIFICATION Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_PATIENT_COMPLAINT/)
- Updated [Age Group Classification Demo](https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_AGE/) 



</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `date_of_birth_parser`
+ `ner_clinical` -> `es`
+ `ner_clinical` -> `fr`
+ `ner_clinical` -> `it`
+ `ner_clinical` -> `pl`
+ `ner_clinical` -> `tr`
+ `bert_sequence_classifier_patient_complaint`
+ `genericclassifier_patient_complaint_sbiobert_cased_mli`
+ `few_shot_classifier_patient_complaint_sbiobert_cased_mli`
+ `ner_events_clinical_langtest`
+ `ner_oncology_anatomy_general_langtest`
+ `ner_oncology_anatomy_granular_langtest`
+ `ner_oncology_demographics_langtest`
+ `ner_oncology_posology_langtest`
+ `ner_oncology_response_to_treatment_langtest`
+ `ner_clinical_pipeline` -> `es`
+ `ner_clinical_pipeline` -> `fr`
+ `ner_clinical_pipeline` -> `it`
+ `ner_clinical_pipeline` -> `nl`
+ `ner_clinical_pipeline` -> `pl`
+ `ner_clinical_pipeline` -> `pt`
+ `ner_clinical_pipeline` -> `tr`
    



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
