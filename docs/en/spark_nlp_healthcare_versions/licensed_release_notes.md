---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-08-18
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">


## 5.0.2

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first Text2SQL module and ONNX-optimized medical text summarization models as well as 20 new clinical pretrained models and pipelines**. It is a testament to our commitment to continuously innovate and improve, furnishing you with a more sophisticated and powerful toolkit for healthcare natural language processing.

+ `Text2SQL` module to translate text prompts into accurate SQL queries
+ Support for ONNX integration of Seq2Seq models such as `MedicalTextGenerator`, `MedicalSummarizer`, and `MedicalQuestionAnswering`
+ 2 new medical QA models and 1 new summarization model optimized with ONNX.
+ Brand new clinical NER model for extracting clinical entities in the **Portuguese** language
+ 3 novel assertion status (negativity scope) detection models tailored for entities extracted from Voice of Patient (VoP) notes
+ Detecting assertion statuses of entities related to Social Determinants of Health (SDOH) identified within clinical notes
+ Classifying **transportation insecurity** within the context of Social Determinants of Health (SDOH)
+ Text Classifier models to infer **Age Groups** from health records, even in the absence of explicit age indications or mentions.
+ Mapping **ICD-10-CM codes to Medicare Severity-Diagnosis Related Group (MS-DRG)**
+ Five new sentence entity resolver (terminology mapping) pretrained pipelines, designed to streamline solutions with a single line of code
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - Improvement of the deidentification faker list (city, street, hospital, profession) for various language
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### `Text2SQL` module to translate text prompts into accurate SQL queries

We are excited to introduce our latest innovation, the `Text2SQL` annotator. This powerful tool revolutionizes the way you interact with databases by effortlessly translating natural language text prompts into accurate and effective SQL queries. With the integration of a state-of-the-art LLM, this annotator opens new possibilities for enhanced data retrieval and manipulation, streamlining your workflow and boosting efficiency. 

Also we have a new `text2sql_mimicsql` model that is specifically finetuned on MIMIC-III dataset schema for enhancing the precision of SQL queries derived from medical natural language queries on MIMIC dataset. Please check the [model card](https://nlp.johnsnowlabs.com/2023/08/14/text2sql_mimicsql_en.html) for more details.


*Example*:

```python
text2sql = Text2SQL.pretrained("text2sql_mimicsql", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sql")

sample_text = "Calulate the total number of patients who had icd9 code 5771"
```

*Results:*

|SQL Query|
|-|
|SELECT COUNT ( DISTINCT DEMOGRAPHIC."SUBJECT_ID" ) FROM DEMOGRAPHIC INNER JOIN PROCEDURES on DEMOGRAPHIC.HADM_ID = PROCEDURES.HADM_ID WHERE PROCEDURES."ICD9_CODE" = "5771"|

Please check: [Text to SQL Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) for more information


</div><div class="h3-box" markdown="1">

#### Support for ONNX integration of Medical Seq2Seq models

ONNX integration empowers our Seq2Seq models to perform their tasks more efficiently and effectively. By leveraging the optimized capabilities of these LLMs through ONNX, the processing speed and overall performance of these models are substantially improved.

</div><div class="h3-box" markdown="1">

#### 2 New Medical QA Models and 1 New Summarization Model Optimized with ONNX.

We're excited to introduce the ONNX-powered versions of `summarizer_clinical_laymen`, `clinical_notes_qa_base` and `clinical_notes_qa_large` models, representing a significant advancement in efficiency and versatility.

|Model|Description|
|-|-|
|[`summarizer_clinical_laymen_onnx`](https://nlp.johnsnowlabs.com/2023/08/16/summarizer_clinical_laymen_onnx_en.html)|The ONNX version of `summarizer_clinical_laymen` model that is finetuned with custom dataset by John Snow Labs to avoid using clinical jargon on the summaries.|
|[`clinical_notes_qa_base_onnx`](https://nlp.johnsnowlabs.com/2023/08/17/clinical_notes_qa_base_onnx_en.html)|The ONNX version of `clinical_notes_qa_base` model that is capable of open-book question answering on Medical Notes.|
|[`clinical_notes_qa_large_onnx`](https://nlp.johnsnowlabs.com/2023/08/17/clinical_notes_qa_large_onnx_en.html)|The ONNX version of `clinical_notes_qa_large` model that is capable of open-book question answering on Medical Notes.|

*Example*:

```python
med_qa = MedicalQuestionAnswering()\
    .pretrained("clinical_notes_qa_base_onnx", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("Context: {context} \n Question: {question} \n Answer: ")\
    .setOutputCol("answer")\

note_text = "Patient with a past medical history of hypertension for 15 years.\n(Medical Transcription Sample Report)\nHISTORY OF PRESENT ILLNESS:\nThe patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."

question = "What is the primary issue reported by patient?"
```

*Results*:

|answer|
|-|
|The primary issue reported by the patient is hypertension.|

</div><div class="h3-box" markdown="1">


#### Brand New Clinical NER Model For Extracting Clinical Entities In The Portuguese Language

Portuguese clinical NER models provide valuable tools for processing and analyzing Portuguese clinical texts. They assist in automating the extraction of important clinical information, facilitating research, medical documentation, and other applications within the Portuguese healthcare domain.

For more details, please check the [model card](https://nlp.johnsnowlabs.com/2023/08/16/ner_clinical_pt.html).

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_clinical", "pt", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_text = """A paciente apresenta sensibilidade dentária ao consumir alimentos quentes e frios.
Realizou-se um exame clínico e radiográfico para avaliar possíveis cáries ou problemas na raiz do dente."""
```

*Results*:

|chunk                     |begin|end|ner_label|
|--------------------------|-----|---|---------|
|sensibilidade dentária    |21   |42 |PROBLEM  |
|alimentos                 |56   |64 |TREATMENT|
|exame clínico             |98   |110|TEST     |
|cáries                    |150  |155|PROBLEM  |
|problemas na raiz do dente|160  |185|PROBLEM  |



</div><div class="h3-box" markdown="1">

#### 3 Novel Assertion Status (Negativity Scope) Detection Models Tailored for Entities Extracted from Voice of Patient (VoP) Notes

We are excited to announce 3 new assertion status detection models that can classify assertions for the detected entities in VoP notes with the `Hypothetical_Or_Absent`, `Present_Or_Past`, and `SomeoneElse` labels. 

|Model|Description|
|-|-|
|[`assertion_vop_clinical`](https://nlp.johnsnowlabs.com/2023/08/17/assertion_vop_clinical_en.html)|This model is trained with `embeddings_clinical` embeddings and predicts the assertion status of the detected chunks.|
|[`assertion_vop_clinical_medium`](https://nlp.johnsnowlabs.com/2023/08/17/assertion_vop_clinical_medium_en.html)|This model is trained with `embeddings_clinical_medium` embeddings and predicts the assertion status of the detected chunks.|
|[`assertion_vop_clinical_large`](https://nlp.johnsnowlabs.com/2023/08/17/assertion_vop_clinical_large_en.html)|This model is trained with `embeddings_clinical_large` embeddings and predicts the assertion status of the detected chunks.|


*Example*:

```python
assertion = AssertionDLModel.pretrained("assertion_vop_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"])\
    .setOutputCol("assertion")

sample_text = "I was feeling anxiety honestly. Can it bring on tremors? It was right after my friend was diagnosed with diabetes."
```

*Results*:

|chunk   |begin|end|ner_label             |sent_id|assertion             |confidence|
|--------|-----|---|----------------------|-------|----------------------|----------|
|anxiety |14   |20 |PsychologicalCondition|0      |Present_Or_Past       |0.98    |
|tremors |48   |54 |Symptom               |1      |Hypothetical_Or_Absent|0.99    |
|diabetes|105  |112|Disease               |2      |SomeoneElse           |0.99    |


</div><div class="h3-box" markdown="1">


#### Detecting Assertion Statuses (Negativity Scope) of Entities Related to Social Determinants of Health (SDOH) Identified within Clinical Notes

We are introducing a new `assertion_sdoh_wip` assertion status detection model that can classify assertions for the detected SDOH entities in text into six distinct labels: `Absent`, `Present`, `Someone_Else`, `Past`, `Hypothetical`, and `Possible`. 

For more details, please check the [model card](https://nlp.johnsnowlabs.com/2023/08/13/assertion_sdoh_wip_en.html).

*Example*:

```python
assertion = AssertionDLModel.pretrained("assertion_sdoh_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

sample_text = "Smith works as a cleaning assistant and does not have access to health insurance or paid sick leave. But she has generally housing problems. She lives in a apartment now.  She has long history of EtOH abuse, beginning in her teens. She is aware she needs to attend Rehab Programs."
```

*Results*:

|chunk             |begin|end|ner_label         |assertion   |
|------------------|-----|---|------------------|------------|
|cleaning assistant|17   |34 |Employment        |Present     |
|health insurance  |64   |79 |Insurance_Status  |Absent      |
|apartment         |156  |164|Housing           |Present     |
|EtOH abuse        |196  |205|Alcohol           |Past        |
|Rehab Programs    |265  |278|Access_To_Care    |Hypothetical|


</div><div class="h3-box" markdown="1">

#### Classifying `Transportation Insecurity` within the Context of Social Determinants of Health (SDOH)

Introducing two new **transportation insecurity classifier models for SDOH** that offer precise label assignments and confidence scores. With a strong ability to thoroughly analyze text, these models categorize content into `No_Transportation_Insecurity_Or_Unknown` and `Transportation_Insecurity`, providing valuable insights into transportation-related insecurity.

|Model|Description|
|-|-|
|[`genericclassifier_sdoh_transportation_insecurity_e5_large`](https://nlp.johnsnowlabs.com/2023/08/13/genericclassifier_sdoh_transportation_insecurity_e5_large_en.html)|This model is trained with E5 large embeddings within a generic classifier framework.|
|[`genericclassifier_sdoh_transportation_insecurity_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/08/13/genericclassifier_sdoh_transportation_insecurity_sbiobert_cased_mli_en.html)|This model is trained with BioBERT embeddings within a generic classifier framework|

*Example*:

```python
generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_transportation_insecurity_sbiobert_cased_mli", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

sample_text_list = ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy. She is alone and can not drive a car or can not use public bus. ", "Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disorder characterized by excessive worry and persistent anxiety."]
```

*Results*:

|Text|Transportation Insecurity Class|
|-|-|
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|              Transportation_Insecurity|
|Lisa, a 28-year-old woman, was diagnosed with generalized anxiety disorder (GAD), a mental disord...|No_Transportation_Insecurity_Or_Unknown|

</div><div class="h3-box" markdown="1">


#### Text Classifier Models to Infer `Age Groups` from Health Records, Even in the Absence of Explicit Age Indications or Mentions.

Now we have three new Age Group Text Classifier models that are designed to analyze the age group of individuals mentioned in health documents, whether or not the age is explicitly mentioned in the training data. These models are trained using in-house annotated health-related text, and categorized into three classes:

- **Adult**: Refers to individuals who are fully grown or developed, usually 18 years or older.
- **Child**: A young human who is not yet an adult. Typically refers to someone below the legal age of adulthood, which is often below 18 years old.
- **Unknown**: Represents situations where determining the age group from the given text is not possible.

|Model|Description|
|-|-|
|[`bert_sequence_classifier_age_group`](https://nlp.johnsnowlabs.com/2023/08/16/bert_sequence_classifier_age_group_en.html)|This model is a BioBERT-based Age Group Text Classifier and it is trained for analyzing the age group of a person mentioned in health documents.|
|[`genericclassifier_age_group_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/08/16/genericclassifier_age_group_sbiobert_cased_mli_en.html)|This Generic Classifier model is trained for analyzing the age group of a person mentioned in health documents.|
|[`few_shot_classifier_age_group_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/08/17/few_shot_classifier_age_group_sbiobert_cased_mli_en.html)|This Few Shot Classifier model is trained for analyzing the age group of a person mentioned in health documents.|

*Example*:

```python
few_shot_classifier = FewShotClassifierModel.pretrained("few_shot_classifier_age_group_sbiobert_cased_mli", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("prediction")

sample_text_list = [["A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30 years, and was diagnosed with hypertension two years ago. After a detailed physical examination, the doctor found a noticeable wheeze on lung auscultation and prescribed a spirometry test, which showed irreversible airway obstruction. The patient was diagnosed with Chronic obstructive pulmonary disease (COPD) caused by smoking."],
 ["Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, low iron.  5 months and still no answers from drs. "],
 ["Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux.Only dull ache above abdomen and left side of chest.I am on reberprozole and librax.My question is whether chronic gastritis is curable or is it a lifetime condition?I am loosing hope because this dull ache is not going away.Please please reply"]]
```

*Results*:

|Text|Age Group|
|-|-|
|A patient presented with complaints of chest pain and shortness of breath. The medical history revealed the patient had a smoking habit for over 30...|  Adult|
|Hi, wondering if anyone has had a similar situation. My 1 year old daughter has the following; loose stools/ pale stools, elevated liver enzymes, l...|  Child|
|Hi have chronic gastritis from 4 month(confirmed by endoscopy).I do not have acid reflux. Only dull ache above abdomen and left side of chest.I am o...|Unknown|


</div><div class="h3-box" markdown="1">

#### Mapping ICD-10-CM Codes to `Medicare Severity-Diagnosis Related Group (MS-DRG)`

We have a new `icd10cm_ms_drg_mapper` chunk mapper model that maps the ICD-10-CM codes with their corresponding Medicare Severity-Diagnosis Related Group (MS-DRG). 

*Example*:

```python
chunkMapper = DocMapperModel.pretrained("icd10cm_ms_drg_mapper", "en", "clinical/models")\
      .setInputCols(["icd_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["ms-drg"])

sample_codes = ["L08.1", "U07.1", "C10.0", "J351"]
```

*Results*:

|ICD10CM Code|MS-DRG                         |
|------------|-------------------------------|
|L08.1       |Erythrasma                     |
|U07.1       |COVID-19                       |
|C10.0       |Malignant neoplasm of vallecula|
|J351        |Hypertrophy of tonsils         |

For more details, please check the [model card](https://nlp.johnsnowlabs.com/2023/08/08/icd10cm_ms_drg_mapper_en.html).


</div><div class="h3-box" markdown="1">

#### Five New Sentence Entity Resolver (Terminology Mapping) Pretrained Pipelines, Designed to Streamline Solutions with a Single Line of Code

We have five new sentence entity resolver pipelines that are meticulously designed to enhance your solutions by efficiently identifying entities and their resolutions within the clinical note. You can easily integrate this advanced capability using just a single line of code.

|Pipeline|Description|
|-|-|
|[`abbreviation_pipeline`](https://nlp.johnsnowlabs.com/2023/08/16/abbreviation_pipeline_en.html)|Detects abbreviations and acronyms of medical regulatory activities as well as map them with their definitions and categories.|
|[`icd10cm_multi_mapper_pipeline`](https://nlp.johnsnowlabs.com/2023/08/16/icd10cm_multi_mapper_pipeline_en.html)|Maps ICD-10-CM codes to their corresponding billable mappings, hcc codes, cause mappings, claim mappings, SNOMED codes, UMLS codes and ICD-9 codes without using any text data. You’ll just feed white space-delimited ICD-10-CM codes and get the result.| 
|[`rxnorm_multi_mapper_pipeline`](https://nlp.johnsnowlabs.com/2023/08/16/rxnorm_multi_mapper_pipeline_en.html)|Maps RxNorm codes to their corresponding drug brand names, rxnorm extension brand names, action mappings, treatment mappings, UMLS codes, NDC product codes and NDC package codes. You’ll just feed white space-delimited RxNorm codes and get the result.|
|[`rxnorm_resolver_pipeline`](https://nlp.johnsnowlabs.com/2023/08/16/rxnorm_resolver_pipeline_en.html)|Maps medication entities with their corresponding RxNorm codes. You’ll just feed your text and it will return the corresponding RxNorm codes.|
|[`snomed_multi_mapper_pipeline`](https://nlp.johnsnowlabs.com/2023/08/16/snomed_multi_mapper_pipeline_en.html)|Maps SNOMED codes to their corresponding ICD-10, ICD-O, and UMLS codes. You’ll just feed white space-delimited SNOMED codes and get the result.|

```python
from sparknlp.pretrained import PretrainedPipeline

abbr_pipeline = PretrainedPipeline("abbreviation_pipeline", "en", "clinical/models")

result = abbr_pipeline.fullAnnotate("""Gravid with estimated fetal weight of 6-6/12 pounds.
LABORATORY DATA: Laboratory tests include a CBC which is normal. 
VDRL: Nonreactive""")
```
     
*Results*:

|chunk|entity|category_mappings|                     definition_mappings|
|-|-|-|-|
|  CBC|  ABBR|          general|complete blood count|
| VDRL|  ABBR|    clinical_dept|  Venereal Disease Research Laboratories|
|  HIV|  ABBR|medical_condition|            Human immunodeficiency virus|

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Improvement of the deidentification faker list (city, street, hospital, profession) for various language


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Extracting Public Health Related_Insights From Social Media Texts Using Healthcare NLP](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/medical_use_cases/Public_Health_Risk_Factors_Analysis/Extracting_Public_Health_related_Insights_from_Social_Media_Texts_Using_Healthcare_NLP.ipynb) Notebook for automated health information extraction and co-occurrence analysis with JohnSnowLabs models
- [Text to SQL Generation](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/37.Text2SQL_Generation.ipynb) Notebook for automatically converting natural language questions into corresponding SQL queries
- Updated [NORMALIZED SECTION HEADER MAPPER](https://demo.johnsnowlabs.com/healthcare/NORMALIZED_SECTION_HEADER_MAPPER/) Demo with `ner_section_header_diagnosis` model
- Updated [ENTITY RESOLVER LOINC](https://demo.johnsnowlabs.com/healthcare/ER_LOINC/) Demo with `sbiobertresolve_loinc_numeric` and `sbiobertresolve_loinc_augmented` models




</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `summarizer_clinical_laymen_onnx`
+ `clinical_notes_qa_large_onnx` 
+ `clinical_notes_qa_base_onnx` 
+ `ner_clinical` -> `pt`
+ `text2sql_mimicsql`
+ `assertion_sdoh_wip`
+ `genericclassifier_sdoh_transportation_insecurity_e5_large`
+ `genericclassifier_sdoh_transportation_insecurity_sbiobert_cased_mli`
+ `bert_sequence_classifier_age_group`
+ `genericclassifier_age_group_sbiobert_cased_mli`
+ `icd10cm_ms_drg_mapper`
+ `abbreviation_pipeline`
+ `rxnorm_resolver_pipeline`
+ `icd10cm_multi_mapper_pipeline`
+ `rxnorm_multi_mapper_pipeline`
+ `snomed_multi_mapper_pipeline`
+ `assertion_vop_clinical`
+ `assertion_vop_clinical_medium`
+ `assertion_vop_clinical_large`
+ `few_shot_classifier_age_group_sbiobert_cased_mli`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">


## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
