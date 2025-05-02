---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v5.5.2 Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_5_2
key: docs-licensed-release-notes
modify_date: 2025-01-17
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.5.2

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of `Healthcare NLP`. **This release comes with brand new relational databases support for de-identification, improved context awareness for chunk embeddings, new customization parameters for flexible output modifications, and 59 new and updated clinical pretrained models and pipelines**.

+ Calculate the embeddings of the neighboring context of a named entity (not just the chunk) with the `BertSentenceChunkEmbeddings` annotator for improved context awareness
+ De-identifying sensitive data in relational databases with a few lines of codes
+ Reduce false positives returned by NER models via possible and impossible context using `ContextualEntityFilterer`. This also refines entity extraction by leveraging regex-based contextual filtering
+ Enhace named entities with specific keywords by allowing greater control over pattern matching via `ContextualEntityRuler`
+ 10 New `PretrainedZeroShotNER` named entity recognition models that are already finetuned on in-house annotations
+ Introducing clinical document analysis with one-liner pretrained pipelines for specific clinical tasks and concepts
+ Introducing 2 new named entity recognition and an assertion models for extracts gene and phenotype features
+ Introducing 2 new named entity recognition models for extracts mentions of cancer types and biomarker
+ Updated human phenotype ontology resolver model
+ Updated all unified medical language system® (UMLS) models.
+ New blog posts on various topics
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - New filtering parameters for `Assertion` annotators: `whiteList`, `blackList`, and `caseSensitive`
    - Bugfixes in `StructuredDeidentification` for improved fake chunk handling and formatting
    - Bug fix for save and load functionality in `DateNormalizer` annotator
    - `PipelineTracer` Improvements: Recursive support for `ChunkMerger` and `AssertionMerger`, and bug fix for `getReplaceDict` issue
    - Corrected begin index calculation in exclude mode for `ContextualEntityRulery`
    - Length-Controlled Fake Text Generation in Deidentification for a Better Consistency
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Oncology Use Cases](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.1.Oncology_Use_Cases.ipynb)  Notebook
    - New [Clinical Deidentification for Structured Data](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook
    - Updated [CLINICAL TEXT SUMMARIZATION](https://demo.johnsnowlabs.com/healthcare/CLINICAL_TEXT_SUMMARIZATION_ES/) Demo
    - Updated [DEID PHI TEXT MULTI](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/) Demo
    - Updated [NER GENE PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### Calculate the Embeddings of the Neighboring Context of a Named Entity (not just the chunk) with the `BertSentenceChunkEmbeddings` Annotator for Improved Context Awareness

The `BertSentenceChunkEmbeddings` annotator now includes advanced features and expanded support for ONNX models:
- `strategy`: Defines how embeddings are computed, with the following options:
	- "sentence_average": Average of sentence and chunk embeddings.
	- "scope_average": Average of scope (defined by scopeWindow) and chunk embeddings.
	- "chunk_only": Embeddings based solely on chunks.
	- "scope_only": Embeddings based solely on scope (requires scopeWindow).
- `scopeWindow`: Specifies the range of tokens used for scope embeddings, which are defined as two non-negative integers. The first integer indicates tokens before the chunk, and the second indicates tokens after. The default is (0, 0), meaning only chunk embeddings are used.
- ONNX Model Support: The annotator now supports ONNX models, enabling integration with models.

*Example*:

```python
chunk_only_embeddings = BertSentenceChunkEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)\
    .setChunkWeight(0.5)\
    .setStrategy("chunk_only")

scope_average_embeddings = BertSentenceChunkEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "ner_chunk"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)\
    .setChunkWeight(0.5)\
    .setStrategy("scope_average")\
    .setScopeWindow([5,5])

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd10cm_augmented_billable_hcc","en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("icd10cm_code")\
    .setDistanceFunction("EUCLIDEAN")

text = """he patient is a 42-year-old female and has diabetes mellitus with diabetic neuropathy since four years and she was treated by Center Hospital."""
```

*Results*:


{:.table-model-big}
| Parameter      | Chunk              | ICD-10-CM Code | Resolution                                                                                                        |
|----------------|--------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| chunk_only     | diabetes mellitus  | E10.9          | diabetes mellitus [type 1 diabetes mellitus without complications]                                                |
| scope_average  | diabetes mellitus  | E11.40         | nervous system disorder due to diabetes mellitus [type 2 diabetes mellitus with diabetic neuropathy, unspecified] |


</div><div class="h3-box" markdown="1">

#### De-identifying Sensitive Data in Relational Databases with a Few Lines of Codes

The RelationalDBDeidentification class provides a robust solution for de-identifying sensitive data in relational databases. It supports a variety of obfuscation techniques and integrates seamlessly with database systems. Key features include:

- End-to-End De-Identification:
	- deidentify(): Automates the de-identification process by:
        - Fetching tables.
        - Extracting schema information.
        - Detecting sensitive columns.
        - Applying obfuscation and masking techniques.
        - Exporting de-identified data as CSV files.
- Database Connectivity:
	- connect_to_db(): Establishes a connection to the MySQL database.
	- get_all_tables(): Retrieves all table names from the connected database.
- Schema and Data Processing:
	- get_schema_info(table_name): Extracts schema details, including date columns, primary keys, and foreign keys, for a specified table.
- Data Obfuscation:
	- obfuscate_dates(df, date_columns): Shifts dates by a specified number of days.
	- obfuscate_ages(df, age_columns, use_hipaa): Obfuscates age columns using HIPAA rules or predefined age groups.
	- mask_other_sensitive_columns(df, other_columns): Masks sensitive columns by replacing their values with asterisks.
 
This class provides a complete framework for protecting sensitive information while maintaining data integrity for relational databases.

*Example*:

```python
from sparknlp_jsl.utils.database_deidentification import RelationalDBDeidentification

config = {
    "db_config": {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "healthcare_db"
    },
    "deid_options": {
        "days_to_shift": 10,
        "age_groups": {
            "child": (0, 12),
            "teen": (13, 19),
            "adult": (20, 64),
            "senior": (65, 90)
        },
        "pk_fk_shift_value": 100,
        "use_hipaa": False,
        "output_path": "deidentified_output/"
    },
    "logging": {
        "level": "INFO",
        "file": "deidentification.log"
    }
}

deidentifier = RelationalDBDeidentification(spark, config)
deidentifier.deidentify()
```

*Example for appointments*:

{:.table-model-big}
|appointment_id|patient_id|doctor_name      |appointment_date|reason            |
|--------------|----------|-----------------|----------------|------------------|
|1             |1         |Dr. Emily Carter |2024-01-15      |Annual Checkup    |
|2             |2         |Dr. Sarah Johnson|2024-02-10      |Flu Symptoms      |
|3             |1         |Dr. Emily Carter |2024-02-15      |Follow-up Visit   |
|4             |1         |Dr. James Wilson |2024-03-20      |Routine Blood Test|

*Result for appointments (De-identified table)*:

{:.table-model-big}
|appointment_id|patient_id|doctor_name|appointment_date|reason            |
|--------------|----------|-----------|----------------|------------------|
|101           |101       |*****      |2024-01-25      |Annual Checkup    |
|102           |102       |*****      |2024-02-20      |Flu Symptoms      |
|103           |101       |*****      |2024-02-25      |Follow-up Visit   |
|104           |101       |*****      |2024-03-30      |Routine Blood Test|



*Example for patients*:

{:.table-model-big}
|patient_id|name      |address                 |ssn        |email                 |dob       |age|
|----------|----------|------------------------|-----------|----------------------|----------|---|
|1         |John Doe  |123 Main St, Springfield|123-45-6789|john.doe@example.com  |1985-04-15|38 |
|2         |Jane Smith|456 Elm St, Shelbyville |987-65-4321|jane.smith@example.com|1990-07-20|33 |

*Result for patients (De-identified table)*:

{:.table-model-big}
|patient_id|name |address|ssn  |email|dob       |age|
|----------|-----|-------|-----|-----|----------|---|
|101       |*****|*****  |*****|*****|1985-04-25|39 |
|102       |*****|*****  |*****|*****|1990-07-30|62 |


Please check the [4.8.Clinical_Deidentification_for_Structured_Data](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### Reduce False Positives Returned by NER Models via Possible and Impossible Context Using `ContextualEntityFilterer`. This also Refines Entity Extraction by Leveraging Regex-Based Contextual Filtering 

The `ContextualEntityFilterer` now includes two new parameters, `possibleRegexContext` and `impossibleRegexContext`, providing advanced filtering options for contextual entity recognition. These parameters offer granular control for refining entity extraction by leveraging regex-based contextual filtering.
- `possibleRegexContext`: The possible regex context to filter the chunks. If the regex is found in the context(chunk), the chunk is kept.
- `impossibleRegexContext`: The impossible regex context to filter the chunks. If the regex is found in the context(chunk), the chunk is removed.
Important Note: When defining regex patterns in code, use double escape characters (e.g., \\) to ensure proper handling of special characters.

*Example*:

```python
 contextual_entity_filterer = ContextualEntityFilterer() \
	.setInputCols("sentence", "token", "ner_chunks") \
	.setOutputCol("filtered_ner_chunks") \
	.setRules([{
		"entity": "AGE",
		"scopeWindow": [3, 3],                
		"scopeWindowLevel": "token",
		"impossibleRegexContext" : "\\b(1[2-9]\\d|[2-9]\\d{2,}|\\d{4,})\\b"
	}])\
	.setRuleScope("sentence")\
	.setCaseSensitive(False)

text = "California, known for its beautiful beaches,and he is 366 years old. " \
        "The Grand Canyon in Arizona,  where the age is 37, is a stunning natural landmark." \
        "It was founded on September 9, 1850, and Arizona on February 14, 1912."
```


*Result*:

```bash
# NER Result
|            chunk|begin|end|ner_label|
|-----------------|-----|---|---------|
|       California|    0|  9| LOCATION|
|              366|   54| 56|      AGE| # this is an imposible age 
|     Grand Canyon|   73| 84| LOCATION|
|          Arizona|   89| 95| LOCATION|
|               37|  116|117|      AGE|
|September 9, 1850|  169|185|     DATE|
|February 14, 1912|  203|219|     DATE|

# Filtered Result
|            chunk|begin|end|ner_label|
|-----------------|-----|---|---------|
|       California|    0|  9| LOCATION|
|     Grand Canyon|   73| 84| LOCATION|
|          Arizona|   89| 95| LOCATION|
|               37|  116|117|      AGE|
|September 9, 1850|  169|185|     DATE|
|February 14, 1912|  203|219|     DATE|
```

Please check the [ContextualEntityFilterer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualEntityFilterer.ipynb) Notebook for more information

</div><div class="h3-box" markdown="1">

#### Enhace Named Entities with Specific Keywords by Allowing Greater Control Over Pattern Matching via `ContextualEntityRuler`

The `ContextualEntityRuler` has been updated with a new parameter, `allowTokensInBetween`, to enhance matching flexibility and address a bug in `exclude` mode's begin indexes:
- `allowTokensInBetween`: When `True`: Allows tokens between prefix/suffix patterns and the entity, enabling extended matches. When `False`: Tokens between patterns and entities prevent a match. Default: False
- adding the "replace_label_only" option to the `mode` parameter
  
This update provides greater control over pattern matching while ensuring robust performance in entity recognition workflows.

*Example*:

```python
rules = [
	{
		"entity": "Age",
		"scopeWindow" : [15,15],
		"scopeWindowLevel" : "char",
		"suffixPatterns" : ["years old", "year old", "months"],
		"replaceEntity": "Modified_Age",
		"mode": "exclude"
	},
	{
		"entity": "Diabetes",
		"scopeWindow" : [3,3],
		"scopeWindowLevel"  : "token",
		"suffixPatterns" : ["complications"],
		"replaceEntity": "Modified_Diabetes",
		"mode": "include"
	},
	{
		"entity": "NAME",
		"scopeWindow" : [3,3],
		"scopeWindowLevel" : "token",
		"prefixPatterns" : ["MD", "M.D", "Dr"],
		"replaceEntity": "Doctor_Name",
		"mode": "replace_only_labels"
	}   
]

contextual_entity_ruler = ContextualEntityRuler() \
            .setInputCols("sentence", "token", "ner_chunk") \
            .setOutputCol("ruled_ner_chunk") \
            .setRules(rules) \
            .setCaseSensitive(False)\
            .setDropEmptyChunks(True)\
            .setAllowPunctuationInBetween(False)\
            .setAllowTokensInBetween(True)
text = """ Dr. John Snow assessed the 36 years old who has a history of the diabetes mellitus with complications in May, 2006"""

```

*NER Result*:

{:.table-model-big}
|            chunk|begin|end|ner_label|
|-----------------|-----|---|---------|
|        John Snow|    5| 13|     NAME|
|     36 years old|   28| 39|      Age|
|diabetes mellitus|   66| 82| Diabetes|


*Replaced Result*:

{:.table-model-big}
|                               chunk|begin|end|       ner_label |
|------------------------------------|-----|---|-----------------|
|                       Dr. John Snow|    1| 13|      Doctor_Name|
|                                  36|   28| 29|     Modified_Age|
|diabetes mellitus with complications|   66|101|Modified_Diabetes|



</div><div class="h3-box" markdown="1">

#### 10 New `PretrainedZeroShotNER` Named Entity Recognition Models that are Already Finetuned on In-house Annotations

Pretrained-Zero-Shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels. The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.

{:.table-model-big}
| Model Name                                                            |      Description            |      Predicted Entites      |
|-----------------------------------------------------------------------|-----------------------------|-----------------------------|
| [`zeroshot_ner_oncology_biomarker_large`](https://nlp.johnsnowlabs.com/2024/12/13/zeroshot_ner_oncology_biomarker_large_en.html) | This model extracts oncology biomarkers entities | `Biomarker`, `Biomarker_Result` |
| [`zeroshot_ner_oncology_biomarker_medium`](https://nlp.johnsnowlabs.com/2024/12/13/zeroshot_ner_oncology_biomarker_medium_en.html)|This model extracts oncology biomarkers entities | `Biomarker`, `Biomarker_Result` |
| [`zeroshot_ner_deid_generic_multi_large_xx`](https://nlp.johnsnowlabs.com/2024/12/21/zeroshot_ner_deid_generic_multi_large_xx.html) | This model extracts demographic entities | `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION` |
| [`zeroshot_ner_deid_generic_multi_medium_XX`](https://nlp.johnsnowlabs.com/2024/12/21/zeroshot_ner_deid_generic_multi_medium_xx.html)|This model extracts demographic entities | `AGE`, `CONTACT`, `DATE`, `ID`, `LOCATION`, `NAME`, `PROFESSION` |
| [`zeroshot_ner_deid_subentity_merged_large`](https://nlp.johnsnowlabs.com/2024/12/17/zeroshot_ner_deid_subentity_merged_large_en.html)|This model extracts demographic entities | `DOCTOR`, `PATIENT`, `AGE`, `DATE`, `HOSPITAL`, `CITY`, `STREET`, `STATE`, `COUNTRY`, `PHONE`, `IDNUM`, `EMAIL`, `ZIP`, `ORGANIZATION`, `PROFESSION`, `USERNAME` |
| [`zeroshot_ner_jsl_large`](https://nlp.johnsnowlabs.com/2025/01/01/zeroshot_ner_jsl_large_en.html)|This model extracts general entities | `Admission_Discharge`, `Alcohol`, `Body_Part`, `Disease_Syndrome_Disorder`, `Drug`, `Injury_or_Poisoning`, `Oncological`, `Procedure`, `Section_Header`, `Smoking`, `Symptom`, `Test`, `Test_Result`, `Treatment`, ...|
| [`zeroshot_ner_jsl_medium`](https://nlp.johnsnowlabs.com/2025/01/01/zeroshot_ner_jsl_medium_en.html)|This model extracts general entities |  `Admission_Discharge`, `Alcohol`, `Body_Part`, `Disease_Syndrome_Disorder`, `Drug`, `Injury_or_Poisoning`, `Oncological`, `Procedure`, `Section_Header`, `Smoking`, `Symptom`, `Test`, `Test_Result`, `Treatment`, ...|
| [`zeroshot_ner_ade_clinical_large`](https://nlp.johnsnowlabs.com/2024/12/02/zeroshot_ner_ade_clinical_large_en.html)|This model extracts general entities | `DRUG`, `ADE`, `PROBLEM` |
| [`zeroshot_ner_sdoh_medium`](https://nlp.johnsnowlabs.com/2025/01/06/zeroshot_ner_sdoh_medium_en.html)|This model extracts general entities | `Access_To_Care`,  `Alcohol`,  `Disability`, `Financial_Status`, `Insurance_Status`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Quality_Of_Life`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Violence_Or_Abuse`, ... |
| [`zeroshot_ner_sdoh_large`](https://nlp.johnsnowlabs.com/2025/01/07/zeroshot_ner_sdoh_large_en.html)|This model extracts general entities   | `Access_To_Care`,  `Alcohol`,  `Disability`, `Financial_Status`, `Insurance_Status`, `Legal_Issues`, `Marital_Status`, `Mental_Health`, `Quality_Of_Life`, `Smoking`, `Social_Exclusion`, `Social_Support`, `Violence_Or_Abuse`, ... |


*Example*:

```python
# You can change the labels
labels = ['Biomarker', 'Biomarker_Result']
pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_oncology_biomarker_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

text = """The results of immunohistochemical examination showed that she tested negative for CK7, synaptophysin (Syn), chromogranin A (CgA),
Muc5AC, human epidermal growth factor receptor-2 (HER2), and Muc6; positive for CK20, Muc1, Muc2, E-cadherin, and p53; the Ki-67 index was about 87% .
"""
```

*Result*:

{:.table-model-big}
|chunk                                   |begin|end|ner_label       |confidence|
|----------------------------------------|-----|---|----------------|----------|
|negative                                |71   |78 |Biomarker_Result|0.96627086|
|CK7                                     |84   |86 |Biomarker       |0.98598194|
|synaptophysin                           |89   |101|Biomarker       |0.97052944|
|Syn                                     |104  |106|Biomarker       |0.5375477 |
|chromogranin A                          |110  |123|Biomarker       |0.95293134|
|Muc5AC                                  |132  |137|Biomarker       |0.9601343 |
|human epidermal growth factor receptor-2|140  |179|Biomarker       |0.95500314|
|HER2                                    |182  |185|Biomarker       |0.87689865|
|Muc6                                    |193  |196|Biomarker       |0.9785201 |
|positive                                |199  |206|Biomarker_Result|0.99296826|
|CK20                                    |212  |215|Biomarker       |0.99122345|
|Muc1                                    |218  |221|Biomarker       |0.97516555|
|Muc2                                    |224  |227|Biomarker       |0.9656944 |
|E-cadherin                              |230  |239|Biomarker       |0.98840755|
|p53                                     |246  |248|Biomarker       |0.9895884 |
|Ki-67 index                             |255  |265|Biomarker       |0.90272933|
|87%                                     |277  |279|Biomarker_Result|0.84652114|


Please check the [ZeroShot Clinical NER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.6.ZeroShot_Clinical_NER.ipynb) Notebook for more information

</div><div class="h3-box" markdown="1">

####  Introducing Clinical Document Analysis with One-Liner Pretrained Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the clinical document analysis process. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for quickly extracting vital information.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`clinical_deidentification_zeroshot_large`](https://nlp.johnsnowlabs.com/2024/12/04/clinical_deidentification_zeroshot_large_en.html) | This pipeline is designed to extract all clinical/medical entities which may be considered as Deidentification entities from text. |
| [`clinical_deidentification_zeroshot_medium`](https://nlp.johnsnowlabs.com/2024/12/04/clinical_deidentification_zeroshot_medium_en.html) | his pipeline is designed to extract all clinical/medical entities which may be considered as Deidentification entities from text. |
| [`clinical_deidentification_docwise_large_wip`](https://nlp.johnsnowlabs.com/2024/12/03/clinical_deidentification_docwise_large_wip_en.html) | This pipeline is designed to extract all clinical/medical entities which may be considered as Deidentification entities from text. |
| [`clinical_deidentification_docwise_medium_wip`](https://nlp.johnsnowlabs.com/2024/12/03/clinical_deidentification_docwise_medium_wip_en.html) | This pipeline is designed to extract all clinical/medical entities which may be considered as Deidentification entities from text. |
| [`clinical_deidentification_light`](https://nlp.johnsnowlabs.com/2025/01/06/clinical_deidentification_light_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. |
| [`clinical_deidentification_docwise_benchmark`](https://nlp.johnsnowlabs.com/2025/01/16/clinical_deidentification_docwise_benchmark_en.html) | This pipeline can be used to deidentify PHI information from medical texts. The PHI information will be masked and obfuscated in the resulting text. This pipeline is prepared for benchmarking with cloud providers. |


*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline_sdoh = PretrainedPipeline("clinical_deidentification_zeroshot_medium", "en", "clinical/models")

text = """Dr. John Lee, from Royal Medical Clinic in Chicago,  attended to the patient on 11/05/2024.
The patient’s medical record number is 56467890.
The patient, Emma Wilson, is 50 years old,  her Contact number: 444-456-7890 ."
"""

```

*Result*:

```bash

Masked with entity labels
------------------------------
Dr. <DOCTOR>, from <HOSPITAL> in <CITY>,  attended to the patient on <DATE>.
The patient’s medical record number is <MEDICALRECORD>
patient, <PATIENT>, is <AGE> years old,  her Contact number: <PHONE> .

Obfuscated
------------------------------
Dr. Edwardo Graft, from MCBRIDE ORTHOPEDIC HOSPITAL in CLAMART,  attended to the patient on 14/06/2024.
The patient’s medical record number is 78295621.
The patient, Nathaneil Bakes, is 43 years old,  her Contact number: 308-657-8469 .

```

Please check the [Task Based Clinical Pretrained Pipelines](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb) model for more information

</div><div class="h3-box" markdown="1">

####  Introducing 2 New Named Entity Recognition and an Assertion Models for Gene and Phenotype Features

These Named Entity Recognition and Assertion models are specifically trained to extract critical information related to genetics, their phenotypes, and associated information contained within any medical document. 

- NER Models
  
{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_genes_phenotypes`](https://nlp.johnsnowlabs.com/2025/01/11/ner_genes_phenotypes_en.html) | This pipeline is designed to extract all clinical/medical entities that may be considered as related to genetics, their phenotypes entities from text. |
| [`ner_genes_phenotypes_wip`](https://nlp.johnsnowlabs.com/2024/12/04/ner_genes_phenotypes_wip_en.html) | This pipeline is designed to extract all clinical/medical entities which may be considered as related to genetics, their phenotypes entities from text. |

*Example*:

```python
ner_model = MedicalNerModel.pretrained('ner_genes_phenotypes', "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

text = """"The CFTR gene, situated on chromosome 7, encodes a chloride channel protein crucial for epithelial salt and water regulation. This gene is associated with cystic fibrosis, demonstrating autosomal recessive inheritance. Mutations like the classic ΔF508 (deletion of phenylalanine at position 508) significantly impair protein folding and cellular transport. The gene shows incomplete penetrance, with variable clinical manifestations ranging from mild respiratory complications to severe multi-organ dysfunction. Diagnostic approaches include genetic testing, sweat chloride analysis, and pulmonary function assessments. Treatment modalities have evolved, incorporating targeted therapies like CFTR modulators that address specific molecular defects. Gene interactions with environmental factors and modifier genes influence disease progression and severity. Prevalence is notably higher in populations of Northern European descent, with approximately 1 in 2,500-3,500 live births affected.
The FMR1 gene, located on the X chromosome, is critical in neurological development and synaptic function. This gene is associated with Fragile X syndrome, exhibiting X-linked dominant inheritance with variable penetrance. Molecular characterization reveals CGG trinucleotide repeat expansions causing potential intellectual disability and neurodevelopmental challenges. Penetrance is complex, with males typically more severely affected than females due to X-chromosome inactivation patterns. Clinical presentations include developmental delays, characteristic facial features, and potential autism spectrum disorder associations. Diagnostic strategies involve molecular genetic testing to quantify CGG repeat expansions. Treatment approaches are multidisciplinary, focusing on educational interventions, behavioral therapies, and management of associated neurological symptoms. Environmental interactions and epigenetic modifications significantly influence phenotypic expressions."""

```

*Result*:

{:.table-model-big}
|chunk                                         |begin|end |ner_label            |
|----------------------------------------------|-----|----|---------------------|
|CFTR gene                                     |5    |13  |MPG                  |
|chromosome 7                                  |28   |39  |Site                 |
|chloride channel protein                      |52   |75  |MPG                  |
|epithelial salt and water regulation          |89   |124 |Gene_Function        |
|cystic fibrosis                               |156  |170 |Phenotype_Disease    |
|autosomal recessive                           |187  |205 |Inheritance_Pattern  |
|ΔF508                                         |247  |251 |Gene                 |
|deletion                                      |254  |261 |Type_Of_Mutation     |
|phenylalanine                                 |266  |278 |MPG                  |
|incomplete penetrance                         |373  |393 |Gene_Penetrance      |
|multi-organ dysfunction                       |488  |510 |Other_Disease        |
|CFTR                                          |694  |697 |MPG                  |
|Northern European descent                     |906  |930 |Prevalence           |
|1 in 2,500-3,500                              |952  |967 |Incidence            |
|FMR1 gene                                     |996  |1004|MPG                  |
|X chromosome                                  |1022 |1033|Site                 |
|neurological development and synaptic function|1051 |1096|Gene_Function        |
|Fragile X syndrome                            |1128 |1145|Phenotype_Disease    |
|X-linked dominant                             |1159 |1175|Inheritance_Pattern  |
|variable penetrance                           |1194 |1212|Gene_Penetrance      |
|CGG                                           |1250 |1252|Gene                 |
|intellectual disability                       |1304 |1326|Clinical_Presentation|
|Penetrance is complex                         |1363 |1383|Gene_Penetrance      |
|males                                         |1391 |1395|Prevalence           |
|females                                       |1435 |1441|Prevalence           |
|X-chromosome                                  |1450 |1461|Site                 |
|developmental delays                          |1517 |1536|Clinical_Presentation|
|autism spectrum disorder                      |1585 |1608|Other_Disease        |
|CGG                                           |1692 |1694|Gene                 |


- Assertion Models

{:.table-model-big}
|Model Name         | Assertion Status | Description      |
|-------------------|-------------------|------------------|
| [assertion_genomic_abnormality_wip](https://nlp.johnsnowlabs.com/2025/01/16/assertion_genomic_abnormality_wip_en.html) | `Normal`, `Affected`, `Variant` | This assertion status detection model is trained to classify entities (Gene and MPG) extracted by the NER model `ner_genes_phenotypes` |

*Example*:

```python
assertion = AssertionDLModel.pretrained("assertion_genomic_abnormality_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

sample_texts = ["""
The ATP7B gene provides instructions for a copper-transporting ATPase essential for copper homeostasis. Mutations in the ATP7B gene cause Wilson disease, an autosomal recessive disorder of copper metabolism. 
Over 500 mutations have been identified, including missense, nonsense, and splice site mutations. The variant ATP7B protein leads to impaired copper excretion and accumulation in various organs, particularly the liver and brain. 
Clinical presentations of Wilson disease include hepatic dysfunction, neurological symptoms (e.g., tremors, dystonia), and psychiatric disturbances. 
Kayser-Fleischer rings, copper deposits in the cornea, are a characteristic sign. Gene-environment interactions are significant, with dietary copper intake and other environmental factors influencing disease progression. 
Diagnosis involves a combination of clinical symptoms, low serum ceruloplasmin, high urinary copper, and genetic testing. 
Treatment focuses on reducing copper accumulation through chelation therapy with drugs like penicillamine or trientine, and zinc supplementation to block copper absorption. 
Liver transplantation may be necessary in severe cases. The worldwide prevalence of Wilson disease is estimated at 1 in 30,000, with higher rates in certain isolated populations.
"""]
```

*Result*:

{:.table-model-big}
|chunk        |begin|end|ner_label|assertion|confidence|
|-------------|-----|---|---------|---------|----------|
|ATP7B gene   |5    |14 |MPG      |Normal   |0.9835    |
|ATPase       |64   |69 |MPG      |Normal   |0.9979    |
|ATP7B gene   |122  |131|MPG      |Affected |0.9974    |
|ATP7B protein|319  |331|MPG      |Affected |0.9713    |
|ceruloplasmin|873  |885|MPG      |Affected |0.9707    |



</div><div class="h3-box" markdown="1">

####  Introducing 2 New Named Entity Recognition Models for Extracts Mentions of Cancer Types and Biomarker

Explore two advanced NER models specifically trained to extract critical oncology-related information from clinical and biomedical texts. The ner_cancer_types model identifies mentions of six primary cancer types and Tumors. Meanwhile, the ner_oncology_biomarker_docwise model focuses on extracting biomarkers and biomarker results.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_cancer_types`](https://nlp.johnsnowlabs.com/2025/01/13/ner_cancer_types_en.html) | This model is designed to extract critical information from clinical and biomedical text related to oncology. The model recognizes 6 main cancer types (`CNS Tumor`, `Carcinoma`, `Leukemia`,  `Lymphoma`, `Melanoma`, `Sarcoma`, `Other_Tumors`) |
| [`ner_oncology_biomarker_docwise`](https://nlp.johnsnowlabs.com/2025/01/15/ner_oncology_biomarker_docwise_en.html) | This model is designed to extracts mentions of biomarkers and biomarker results from oncology texts. During training, a doc-wise method was used. |


*Example*:

```python
ner_model = MedicalNerModel.pretrained('ner_cancer_types', "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

text =  """
    We report a case of CD3 negative, CD20 positive T-cell prolymphocytic leukemia (T-PLL). The leukemic cells were negative for surface CD3, CD2, and CD7 and strongly positive for CD20. 
    T-cell lineage markers such as CD4, CD5, and cytoplasmic CD3 were also positive. A monoclonal rearrangement of the T-cell receptor (TCR) β chain gene was detected. 
    CD3 negative T-PLL has been reported often, but CD20 positive T-PLL has not. We reviewed seven cases of CD20 positive immature and mature T-cell leukemias, including the present case. 
    Three were immature T-cell leukemias (acute lymphoblastic leukemia), and four were mature T-cell leukemias (granular lymphocytic leukemia, small lymphocytic lymphoma/chronic lymphocytic leukemia, 
    adult T-cell leukemia, and the present case). 
"""

```

*Result*:

{:.table-model-big}
|chunk                                                  |begin|end|ner_label       |
|-------------------------------------------------------|-----|---|----------------|
|CD3                                                    |21   |23 |Biomarker       |
|negative                                               |25   |32 |Biomarker_Result|
|CD20                                                   |35   |38 |Biomarker       |
|positive                                               |40   |47 |Biomarker_Result|
|T-cell prolymphocytic leukemia                         |49   |78 |Leukemia_Type   |
|T-PLL                                                  |81   |85 |Leukemia_Type   |
|negative                                               |113  |120|Biomarker_Result|
|CD3                                                    |134  |136|Biomarker       |
|CD2                                                    |139  |141|Biomarker       |
|CD7                                                    |148  |150|Biomarker       |
|positive                                               |165  |172|Biomarker_Result|
|CD20                                                   |178  |181|Biomarker       |
|CD4                                                    |215  |217|Biomarker       |
|CD5                                                    |220  |222|Biomarker       |
|CD3                                                    |241  |243|Biomarker       |
|positive                                               |255  |262|Biomarker_Result|
|CD3                                                    |348  |350|Biomarker       |
|negative                                               |352  |359|Biomarker_Result|
|T-PLL                                                  |361  |365|Leukemia_Type   |
|CD20                                                   |396  |399|Biomarker       |
|positive                                               |401  |408|Biomarker_Result|
|T-PLL                                                  |410  |414|Leukemia_Type   |
|CD20                                                   |452  |455|Biomarker       |
|positive                                               |457  |464|Biomarker_Result|
|mature T-cell leukemias                                |479  |501|Leukemia_Type   |
|T-cell leukemias                                       |552  |567|Leukemia_Type   |
|acute lymphoblastic leukemia                           |570  |597|Leukemia_Type   |
|mature T-cell leukemias                                |615  |637|Leukemia_Type   |
|granular lymphocytic leukemia                          |640  |668|Leukemia_Type   |
|small lymphocytic lymphoma/chronic lymphocytic leukemia|671  |725|Leukemia_Type   |
|adult T-cell leukemia                                  |728  |748|Leukemia_Type   |


</div><div class="h3-box" markdown="1">


#### Updated Human Phenotype Ontology Resolver Model

This model maps phenotypic abnormalities, medical terms associated with hereditary diseases, encountered in Human Phenotype Ontology (HPO) codes using sbiobert_base_cased_mli Sentence Bert Embeddings, and has faster load time, with a speedup of about 6X when compared to previous versions. Also, the load process now is more memory friendly meaning that the maximum memory required during load time is smaller, reducing the chances of OOM exceptions, and thus relaxing hardware requirements

`This model returns Human Phenotype Ontology (HPO) codes for phenotypic abnormalities encountered in human diseases. It also returns associated codes from the following vocabularies for each HPO code: - SNOMEDCT_US - UMLS (Unified Medical Language System ) - ORPHA (international reference resource for information on rare diseases and orphan drugs) - EPCC (European Paediatric Cardiac Code - another region-specific or discipline-specific coding system related to healthcare or medical classification) - Fyler (unique identifier used within a specific coding system or database)`

*Example*:

```python

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_HPO", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("hpo")\
    .setDistanceFunction("EUCLIDEAN")

text =  """She is followed by Dr. X in our office and has a history of severe tricuspid regurgitation. On 05/12/08, preserved left and right ventricular systolic function, aortic sclerosis with apparent mild aortic stenosis. She has previously had a Persantine Myoview nuclear rest-stress test scan completed at ABCD Medical Center in 07/06 that was negative. She has had significant mitral valve regurgitation in the past being moderate, but on the most recent echocardiogram on 05/12/08, that was not felt to be significant. She does have a history of significant hypertension in the past. She has had dizzy spells and denies clearly any true syncope. She has had bradycardia in the past from beta-blocker therapy."""

```

*Result*:

{:.table-model-big}
|                     chunk|begin|end|ner_label|resolution|               description|                                                                       all_codes|
|--------------------------|-----|---|---------|----------|--------------------------|--------------------------------------------------------------------------------|
|   tricuspid regurgitation|   67| 89|       HP|HP:0005180|   tricuspid regurgitation|Fyler:1161||SNOMEDCT_US:111287006||UMLS:C0040961:::EPCC:06.01.92||ICD-10:Q22....|
|           aortic stenosis|  197|211|       HP|HP:0001650|           aortic stenosis|Fyler:1411||SNOMEDCT_US:60573004||UMLS:C0003507:::SNOMEDCT_US:204368006||UMLS...|
|mitral valve regurgitation|  373|398|       HP|HP:0001653|mitral valve regurgitation|Fyler:1151||SNOMEDCT_US:48724000||UMLS:C0026266||UMLS:C3551535:::EPCC:06.02.9...|
|              hypertension|  555|566|       HP|HP:0000822|              hypertension|SNOMEDCT_US:24184005||SNOMEDCT_US:38341003||UMLS:C0020538||UMLS:C0497247:::-:...|
|               bradycardia|  655|665|       HP|HP:0001662|               bradycardia|SNOMEDCT_US:48867003||UMLS:C0428977:::Fyler:7013||SNOMEDCT_US:49710005||UMLS:...|

Please check the [sbiobertresolve_HPO](https://nlp.johnsnowlabs.com/2025/01/14/sbiobertresolve_HPO_en.html) model for more information



</div><div class="h3-box" markdown="1">

#### Updated all Unified Medical Language System® (UMLS) Models.

The 2024AB release of the Unified Medical Language System® (UMLS) has updated all resolvers, mappers, and pretrained pipelines related to UMLS.


*Resolver Model*:

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`biolordresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2024/12/06/biolordresolve_umls_general_concepts_en.html) | This model maps clinical entities and concepts to 4 UMLS CUI code categories| 
| [`sbiobertresolve_umls_major_concepts`](https://nlp.johnsnowlabs.com/2024/12/02/sbiobertresolve_umls_major_concepts_en.html)|This model maps clinical entities and concepts to 4 major categories of UMLS CUI codes| 
| [`sbiobertresolve_umls_clinical_drugs`](https://nlp.johnsnowlabs.com/2024/12/05/sbiobertresolve_umls_clinical_drugs_en.html) |This model maps drug entities to UMLS CUI codes.| 
| [`sbiobertresolve_umls_disease_syndrome`](https://nlp.johnsnowlabs.com/2024/12/05/sbiobertresolve_umls_disease_syndrome_en.html)|This model maps clinical entities to UMLS CUI codes. | 
| [`sbiobertresolve_umls_drug_substance`](https://nlp.johnsnowlabs.com/2024/12/05/sbiobertresolve_umls_drug_substance_en.html)|This model maps clinical entities to UMLS CUI codes. | 
| [`sbiobertresolve_umls_findings`](https://nlp.johnsnowlabs.com/2024/12/05/sbiobertresolve_umls_findings_en.html)|This model maps clinical entities to UMLS CUI codes. | 
| [`sbiobertresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2024/12/05/sbiobertresolve_umls_general_concepts_en.html)|This model maps clinical entities to UMLS CUI codes. | 


*Mapper Model*:

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`umls_clinical_drugs_mapper`](https://nlp.johnsnowlabs.com/2024/12/06/umls_clinical_drugs_mapper_en.html) | This model maps entities (Clinical Drugs) with their corresponding UMLS CUI codes.| 
| [`umls_icd10cm_mapper`](https://nlp.johnsnowlabs.com/2024/12/09/umls_icd10cm_mapper_en.html)|This model maps UMLS codes to corresponding ICD10CM codes.| 
| [`cpt_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/10/cpt_umls_mapper_en.html) |This model maps CPT codes to corresponding UMLS codes.| 
| [`icd10cm_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/10/icd10cm_umls_mapper_en.html)|This model maps ICD10CM codes to corresponding UMLS codes under the Unified Medical Language System (UMLS).| 
| [`umls_cpt_mapper`](https://nlp.johnsnowlabs.com/2024/12/10/umls_cpt_mapper_en.html)|This model maps UMLS codes to corresponding CPT codes.| 
| [`rxnorm_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/11/rxnorm_umls_mapper_en.html)|This This pretrained model maps RxNorm codes to corresponding UMLS codes.| 
| [`snomed_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/11/snomed_umls_mapper_en.html)|This model maps SNOMED codes to corresponding UMLS codes.| 
| [`umls_rxnorm_mapper`](https://nlp.johnsnowlabs.com/2024/12/11/umls_rxnorm_mapper_en.html)|This model maps UMLS codes to corresponding RxNorm codes. | 
| [`umls_snomed_mapper`](https://nlp.johnsnowlabs.com/2024/12/11/umls_snomed_mapper_en.html)|This model maps UMLS codes to corresponding SNOMED codes.| 
| [`mesh_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/12/mesh_umls_mapper_en.html)|This model maps MESH codes to corresponding UMLS codes.| 
| [`umls_mesh_mapper`](https://nlp.johnsnowlabs.com/2024/12/12/umls_mesh_mapper_en.html)|This model maps UMLS codes to corresponding MESH codes.| 
| [`umls_disease_syndrome_mapper`](https://nlp.johnsnowlabs.com/2024/12/16/umls_disease_syndrome_mapper_en.html)|This model maps entities (Disease or Syndrome) with corresponding UMLS CUI codes.| 
| [`umls_clinical_findings_mapper`](https://nlp.johnsnowlabs.com/2024/12/18/umls_clinical_findings_mapper_en.html)|This model maps clinical entities and concepts to 4 major categories of UMLS CUI codes. | 
| [`umls_drug_substance_mapper`](https://nlp.johnsnowlabs.com/2024/12/18/umls_drug_substance_mapper_en.html)|This model maps entities (Drug Substances) with their corresponding UMLS CUI codes.| 
| [`umls_major_concepts_mapper`](https://nlp.johnsnowlabs.com/2024/12/18/umls_major_concepts_mapper_en.html)| This model maps entities (Major Clinical Concepts) with corresponding UMLS CUI codes.| 
| [`loinc_umls_mapper`](https://nlp.johnsnowlabs.com/2024/12/19/loinc_umls_mapper_en.html)|This model maps LOINC codes to corresponding UMLS codes.| 
| [`umls_loinc_mapper`](https://nlp.johnsnowlabs.com/2024/12/19/umls_loinc_mapper_en.html)|This model maps UMLS codes to corresponding LOINC codes.| 


*Pretrained Pipeline*:

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`medication_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/19/medication_resolver_pipeline_en.html)| This pipeline to extract medications and resolve their adverse reactions (ADE), RxNorm, UMLS, NDC, SNOMED CT codes, and action/treatments in clinical text.| 
| [`medication_resolver_transform_pipeline`](https://nlp.johnsnowlabs.com/2024/12/19/medication_resolver_transform_pipeline_en.html)|This pipeline to extract medications and resolve their adverse reactions (ADE), RxNorm, UMLS, NDC, SNOMED CT codes, and action/treatments in clinical text. | 
| [`snomed_multi_mapper_pipeline`](https://nlp.johnsnowlabs.com/2024/12/23/snomed_multi_mapper_pipeline_en.html)|This pipeline maps SNOMED codes to their corresponding ICD-10, ICD-O, and UMLS codes.| 
| [`umls_clinical_findings_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/23/umls_clinical_findings_resolver_pipeline_en.html)|This pipeline maps entities (Clinical Findings) with their corresponding UMLS CUI codes.| 
| [`umls_drug_substance_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/23/umls_drug_substance_resolver_pipeline_en.html)|This pipeline maps entities (Drug Substances) with their corresponding UMLS CUI codes. | 
| [`umls_disease_syndrome_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/24/umls_disease_syndrome_resolver_pipeline_en.html)|This pipeline maps entities (Diseases and Syndromes) with their corresponding UMLS CUI codes. | 
| [`umls_drug_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/24/umls_drug_resolver_pipeline_en.html)|This pipeline maps entities (Clinical Drugs) with their corresponding UMLS CUI codes. | 
| [`umls_major_concepts_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/12/24/umls_major_concepts_resolver_pipeline_en.html)|This pipeline maps entities (Clinical Major Concepts) with their corresponding UMLS CUI codes. | 


*Example*:

```python
resolver_pipeline = PretrainedPipeline("medication_resolver_pipeline", "en", "clinical/models")
text = """The patient was prescribed Amlodopine Vallarta 10-320mg, Eviplera. The other patient is given Lescol 40 MG and Everolimus 1.5 mg tablet"""
```

*Result*:

{:.table-model-big}
|chunk                       |ner_label|ADE                        |RxNorm |Action                    |Treatment                                 |UMLS    |SNOMED_CT       |NDC_Product|NDC_Package  |
|----------------------------|---------|---------------------------|-------|--------------------------|------------------------------------------|--------|----------------|-----------|-------------|
|Amlodopine Vallarta 10-320mg|DRUG     |Gynaecomastia              |722131 |NONE                      |NONE                                      |C1949334|1153435009      |00093-7693 |00093-7693-56|
|Eviplera                    |DRUG     |Anxiety                    |217010 |Inhibitory Bone Resorption|Osteoporosis                              |C0720318|NONE            |NONE       |NONE         |
|Lescol 40 MG                |DRUG     |NONE                       |103919 |Hypocholesterolemic       |Heterozygous Familial Hypercholesterolemia|C0353573|NONE            |00078-0234 |00078-0234-05|
|Everolimus 1.5 mg tablet    |DRUG     |Acute myocardial infarction|2056895|NONE                      |NONE                                      |C4723581|1029521000202102|00054-0604 |00054-0604-21|

Please check the [Task_Based_Clinical_Pretrained_Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">
	
#### New Blog Posts On Various Topics

Dive into our latest blog series exploring cutting-edge advancements in healthcare NLP. Discover how innovative technologies like LangTest are transforming the field by enhancing the robustness of AI models. From ensuring precision and stability in foundation models to leveraging Databricks for robust LLM evaluation, these posts offer valuable insights into creating resilient, reliable, and impactful AI applications in healthcare and beyond

- [For Foundation Models, Precision Matters — But Stability Matters More](https://medium.com/@chakravarthik27/562450175dd9): This blog post discusses the crucial role of robustness in AI models, particularly foundation models, which are essential for applications like healthcare, finance, and autonomous systems. It emphasizes that while accuracy is important, robustness—ensuring models perform well under various conditions and adversarial inputs—is paramount for safe and reliable AI deployment. The article introduces LangTest by John Snow Labs, a tool that helps test and enhance model robustness through simulations of real-world variations like typos and slang. By prioritizing robustness alongside accuracy, the article advocates for a more comprehensive approach to AI model evaluation to ensure they are not only intelligent but also resilient and trustworthy in real-world applications. 
- [Robustness Testing of LLM Models Using LangTest in Databricks](https://medium.com/@chakravarthik27/20aa680a625d): This blog posthighlights the significance of evaluating the robustness of large language models (LLMs) like GPT-4 in NLP applications. These models power various tools, from chatbots to advanced data analysis systems, and ensuring their reliability with diverse, unpredictable inputs is critical. LangTest, an open-source evaluation tool, is introduced as a solution for assessing and enhancing the robustness of these models. The post explains how to leverage LangTest within the Databricks environment to evaluate and improve the performance of foundation models effectively.


</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- New filtering parameters for `Assertion` annotators: `whiteList`, `blackList`, and `caseSensitive`
- Bugfixes in `StructuredDeidentification` for improved fake chunk handling and formatting
- Bug fix for save and load functionality in `DateNormalizer` annotator
- `PipelineTracer` Improvements: Recursive support for `ChunkMerger` and `AssertionMerger`, and bug fix for `getReplaceDict` issue
- Corrected begin index calculation in exclude mode for `ContextualEntityRulery`
- Length-Controlled Fake Text Generation in Deidentification for a Better Consistency


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Oncology Use Cases](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.1.Oncology_Use_Cases.ipynb)  Notebook
- New [Clinical Deidentification for Structured Data](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.8.Clinical_Deidentification_for_Structured_Data.ipynb) Notebook
- Updated [CLINICAL TEXT SUMMARIZATION](https://demo.johnsnowlabs.com/healthcare/CLINICAL_TEXT_SUMMARIZATION_ES/) Demo
- Updated [DEID PHI TEXT MULTI](https://demo.johnsnowlabs.com/healthcare/DEID_PHI_TEXT_MULTI/) Demo
- Updated [NER GENE PHENOTYPES](https://demo.johnsnowlabs.com/healthcare/NER_GENE_PHENOTYPES/) Demo




</div><div class="h3-box" markdown="1">

#### We have added and updated a substantial number of new clinical models and pipelines, further solidifying our offering in the healthcare domain.

+ `zeroshot_ner_oncology_biomarker_large`
+ `zeroshot_ner_oncology_biomarker_medium`
+ `clinical_deidentification_zeroshot_large`
+ `clinical_deidentification_zeroshot_medium`
+ `clinical_deidentification_docwise_wip`
+ `clinical_deidentification_v2_wip`
+ `clinical_deidentification_docwise_large_wip`
+ `clinical_deidentification_docwise_medium_wip`
+ `zeroshot_ner_deid_generic_multi_large`
+ `zeroshot_ner_deid_generic_multi_medium`
+ `zeroshot_ner_deid_generic_multi_large` -> `xx`
+ `zeroshot_ner_deid_generic_multi_medium` -> `xx`
+ `biolordresolve_umls_general_concepts`
+ `sbiobertresolve_umls_major_concepts`
+ `sbiobertresolve_umls_clinical_drugs`
+ `sbiobertresolve_umls_disease_syndrome`
+ `sbiobertresolve_umls_drug_substance`
+ `sbiobertresolve_umls_findings`
+ `sbiobertresolve_umls_general_concepts`
+ `umls_clinical_drugs_mapper`
+ `umls_icd10cm_mapper`
+ `cpt_umls_mapper`
+ `icd10cm_umls_mapper`
+ `umls_cpt_mapper`
+ `rxnorm_umls_mapper`
+ `snomed_umls_mapper`
+ `umls_rxnorm_mapper`
+ `umls_snomed_mapper`
+ `mesh_umls_mapper`
+ `umls_mesh_mapper`
+ `umls_disease_syndrome_mapper`
+ `umls_clinical_findings_mapper`
+ `umls_drug_substance_mapper`
+ `umls_major_concepts_mapper`
+ `loinc_umls_mapper`
+ `umls_loinc_mapper`
+ `medication_resolver_pipeline`
+ `medication_resolver_transform_pipeline`
+ `snomed_multi_mapper_pipeline`
+ `umls_clinical_findings_resolver_pipeline`
+ `umls_drug_substance_resolver_pipeline`
+ `umls_disease_syndrome_resolver_pipeline`
+ `umls_drug_resolver_pipeline`
+ `umls_major_concepts_resolver_pipeline`
+ `zeroshot_ner_jsl_large`
+ `zeroshot_ner_jsl_medium`
+ `ner_genes_phenotypes_wip`
+ `ner_genes_phenotypes`
+ `zeroshot_ner_ade_clinical_large`
+ `zeroshot_ner_deid_subentity_merged_large`
+ `clinical_deidentification_multi_mode_output`
+ `clinical_deidentification_light`
+ `zeroshot_ner_sdoh_medium`
+ `zeroshot_ner_sdoh_large`
+ `sbiobertresolve_HPO`
+ `ner_oncology_biomarker_docwise`
+ `ner_cancer_types`
+ `clinical_deidentification_docwise_benchmark`
+ `assertion_genomic_abnormality_wip`

</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">




## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
