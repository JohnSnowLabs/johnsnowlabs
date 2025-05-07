---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2025-05-02
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 6.0.0

#### Highlights

We’re excited to introduce significant advancements in the latest release of Spark NLP for Healthcare. This update features a new **FHIR Dedidentification module, a new Medical LLM finetuned for SOAP note generation to support advanced clinical documentation, the Assertion classification based on Bert architecture along with new contextual assertion models to enhance assertion status detection. Additionally, we are releasing new models and utility tools for Human Phenotype term extraction and mapping using official terminology vocabularies. This release includes 29 new clinical pretrained models and pipelines to expand coverage across a range of healthcare tasks.**

+ Introducing a new Assertion classification architectures based on Bert for sequence classification to improve assertion status detection contextually. 
+ Scalable and flexible FHIR deidentification module deidentify FHIR records across various resource types.
+ Small size Medical LLM for generating clinical SOAP (Subjective, Objective, Assessment, Plan) note
+ Human Phenotype term extraction and mapping using official terminology vocabularies
+ Inferring missing PHI entities via previously detected NER outputs within Deidentification
+ Improved Name Consistency Handling in Deidentification
+ Clinical document analysis with one-liner pretrained-pipelines for specific clinical tasks and concepts
+ Cloud Provider & LLM Benchmarks for Information Extraction tasks
+ Enabling flexible annotation transformations with `AnnotationConverter`
+ Introducing 2 new contextual assertion models to detect assertion status given a larger context and scenarious. 
+ New German Oncology named entity recognition model and ICD10 entity resolver model
+ Enabling exception handling within the pipelines for specified or all eligible stages
+ Interactive chat support for Healthcare NLP documentation
+ New peer-reviewed papers and blog posts on various topics
+ Various core improvements, bug fixes, enhanced overall robustness, and reliability of Spark NLP for Healthcare
    - Resolved log file creation on Databricks for training
    - Added `consistentAcrossNameParts` param to `LightDeIdentification` and `StructuredDeIdentification`
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Spanish Healthcare Models](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/48.Spanish_Healthcare_Models.ipynb) Notebook
    - New [PRR ROR EBGM for Signal Processing of Drug Events](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/medical_use_cases/Signal_Processing_Drug_ADE/PRR_ROR_EBGM_for_Signal_Processing_of_Drug_Events.ipynb) Notebook
    - New [BertForAssertionClassification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.4.BertForAssertionClassification.ipynb) Notebook
    - New [NER Performance Comparison Of Healthcare NLP VS Cloud Solutions](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/academic/NER_Benchmarks/NER_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions.ipynb) Notebook
    - New [Fhir DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.10.Fhir_DeIdentification.ipynb) Notebook
    - New [Human Phenotype Extraction And HPO Code Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/49.Human_Phenotype_Extraction_And_HPO_Code_Mapping.ipynb) Notebook
    - Updated [German Clinical Deidentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.9.German_Clinical_Deidentification) Notebook
    - Updated [German Healthcare Models](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/14.German_Healthcare_Models.ipynb) Notebook
    - Updated [Deidentification Custom Pretrained Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.7.Deidentification_Custom_Pretrained_Pipelines.ipynb) Notebook
    - Updated [Clinical_DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) Notebook
    - Updated [Analyse Veterinary Documents with Healthcare NLP](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/44.Analyse_Veterinary_Documents_with_Healthcare_NLP.ipynb) Notebook
    - Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.




</div><div class="h3-box" markdown="1">

#### Introducing a New Assertion Classification Architectures Based On Bert for Sequence Classification to Improve Assertion Status Detection Contextually

`BertForAssertionClassification` extracts the assertion status from text by analyzing both the extracted entities and their surrounding context. This classifier leverages pre-trained BERT models fine-tuned on biomedical text (e.g., BioBERT) and applies a sequence classification/regression head (a linear layer on the pooled output) to support multi-class document classification.

| Model Name                                                            |      Predicted Entities            |
|-----------------------------------------------------------------------|-----------------------------|
| [`assertion_bert_classification_radiology`](https://nlp.johnsnowlabs.com/2025/04/28/assertion_bert_classification_radiology_en.html) |  `Confirmed`, `Suspected`, `Negative` |
| [`assertion_bert_classification_jsl`](https://nlp.johnsnowlabs.com/2025/04/28/assertion_bert_classification_jsl_en.html) |  `Present`, `Planned`, `SomeoneElse`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible` |
| [`assertion_bert_classification_clinical`](https://nlp.johnsnowlabs.com/2025/04/04/assertion_bert_classification_clinical_en.html) |  `absent`, `present`, `conditional`, `associated_with_someone_else`, `hypothetical`, `possible` |


*Example*:

```python
...
ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")

text = """Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""

data = spark.createDataFrame([[text]]).toDF("text")                         
result = pipeline.fit(data).transform(data)

# show results
result.selectExpr("explode(assertion_class) as result")\
      .selectExpr("result.metadata['ner_chunk'] as ner_chunk",
                  "result.begin as begin",
                  "result.begin as end",
                  "result.metadata['ner_label'] as ner_chunk",
                  "result.result as assertion").show(truncate=False)
```

*Result*:

{:.table-model-big}
| ner_chunk       |   begin |   end | ner_chunk   | assertion                    |
|:----------------|--------:|------:|:------------|:-----------------------------|
| severe fever    |      13 |    13 | PROBLEM     | present                      |
| sore throat     |      30 |    30 | PROBLEM     | present                      |
| stomach pain    |      55 |    55 | PROBLEM     | absent                       |
| pain control    |     113 |   113 | PROBLEM     | hypothetical                 |
| short of breath |     142 |   142 | PROBLEM     | conditional                  |
| lung tumor      |     202 |   202 | PROBLEM     | present                      |
| Alzheimer       |     258 |   258 | PROBLEM     | associated_with_someone_else |

Please check the [BertForAssertionClassification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.4.BertForAssertionClassification.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

#### Scalable and Flexible FHIR De-identification Module Deidentify FHIR Records Across Various Resource Types

We’re excited to introduce a major upgrade to **FHIR deidentification** in Spark NLP for Healthcare. This new feature brings generic, path-based de-identification, eliminating the need for resource-specific configurations and enabling seamless processing across various FHIR document types. With full support for FHIR R4, basic support for R5, and legacy compatibility with STU3, it offers broad coverage for modern healthcare systems. The de-identification tool works with both JSON and XML formats, and is compatible with both Spark pipelines and direct usage—making it more powerful and flexible than ever for protecting patient data at scale.
 To use **FHIR deidentification** module, please set `fhir_deid=True` in the start() function.

*Example*:

```python

rules = {
  "Patient.birthDate" : "DATE",
  "Patient.name.given" : "FIRST_NAME",
  "Patient.name.family" : "LAST_NAME",
  "Patient.telecom.value" : "EMAIL",
  "Patient.gender" : "GENDER"
}

fhir = (
    FhirDeIdentification()
      .setInputCol("text")
      .setOutputCol("deid")
      .setMode("obfuscate")
      .setMappingRules(rules)
      .setFhirVersion("R4")
      .setParserType("JSON")
      .setDays(20)
      .setSeed(88)
      .setCustomFakers(
          {
              "GENDER": ["female", "other"]
          }
      )
      .setObfuscateRefSource("both")
)


john_doe = """{
  "resourceType": "Patient",
  "id": "example",
  "name": [
    {
      "use": "official",
      "family": "Doe",
      "given": [
        "John",
        "Michael"
      ]
    }
  ],
  "telecom": [
    {
      "system": "email",
      "value": "john.doe@example.com"
    },
    {
      "system": "url",
      "value": "http://johndoe.com"
    }
  ],
  "birthDate": "1970-01-01",
  "gender": "male"
}"""
```

*Result*:
```bash
{
    'resourceType': 'Patient',
    'id': 'example',
    'name': [
        {
            'use': 'official',
            'family': 'Cease',
            'given': [
                'Mylene',
                'Anola'
            ]
        }
    ],
    'telecom': [
        {
            'system': 'email',
            'value': 'Bryton@yahoo.com'
        },
        {
            'system': 'url',
            'value': 'https://aurora.com'
        }
    ],
    'birthDate': '1970-01-21',
    'gender': 'other'
}
```


</div><div class="h3-box" markdown="1">

#### Small Size Medical LLM for Generating Clinical SOAP (Subjective, Objective, Assessment, Plan) Note

This large language model is used by a medical expert to generate structured SOAP (Subjective, objective, assessment, plan) summaries from patient-provider dialogues.It ensures medically accurate documentation using standardized terminology and professional clinical formatting suitable for real-world healthcare communication. The model strictly follows SOAP conventions without using special formatting or markdown.

*Example*:

```python
medical_llm = medical.AutoGGUFModel.pretrained("jsl_meds_text2soap_v1", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)

pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

prompt = """
...
A 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years prior to presentation and subsequent type two diabetes mellitus ( T2DM ), one prior episode of HTG-induced pancreatitis three years prior to presentation , and associated with an acute hepatitis , presented with a one-week history of polyuria , poor appetite , and vomiting .
She was on metformin , glipizide , and dapagliflozin for T2DM and atorvastatin and gemfibrozil for HTG . She had been on dapagliflozin for six months at the time of presentation .
Physical examination on presentation was significant for dry oral mucosa ; significantly , her abdominal examination was benign with no tenderness , guarding , or rigidity . Pertinent laboratory findings on admission were : serum glucose 111 mg/dl ,  creatinine 0.4 mg/dL , triglycerides 508 mg/dL , total cholesterol 122 mg/dL , and venous pH 7.27 .
"""
```

*Result*:

```bash
S: The patient is a 28-year-old female with a history of gestational diabetes mellitus diagnosed eight years ago and type two diabetes mellitus (T2DM), with a prior episode of HTG-induced pancreatitis three years ago. She presented with a one-week history of polyuria, poor appetite, and vomiting. She was on metformin, glipizide, dapagliflozin, atorvastatin, and gemfibrozil for her conditions.
O: Physical examination showed dry oral mucosa but was otherwise benign with no tenderness, guarding, or rigidity. Laboratory findings included serum glucose 111 mg/dL, creatinine 0.4 mg/dL, triglycerides 508 mg/dL, total cholesterol 122 mg/dL, and venous pH 7.27. She was on dapagliflozin for six months prior to presentation.
A: The primary diagnosis is diabetic ketoacidosis (DKA) based on the patient's symptoms of polyuria, poor appetite, vomiting, and elevated triglycerides and total cholesterol. Differential diagnoses could include other causes of polyuria such as diabetes insipidus or a complication from her underlying diabetes. The patient's history of HTG and recent use of dapagliflozin are also relevant.
P: The management plan includes close monitoring of her glucose levels and electrolyte balance. She will be started on intravenous insulin and hydration to treat DKA. Dietary adjustments will be made to manage her diabetes and HTG. Regular follow-up appointments will be scheduled to monitor her glucose levels and adjust her medications as necessary. Education on the importance of adherence to the treatment plan and monitoring for signs of complications such as worsening of symptoms or new symptoms will be provided.
```

Please check the [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### Human Phenotype Term Extraction and Mapping Using Official Terminology Vocabularies

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`hpo_mapper`](https://nlp.johnsnowlabs.com/2025/05/01/hpo_mapper_en.html) | This model is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes. It ensures that observed symptoms, signs, and clinical abnormalities are standardized using HPO terminology. |
| [`hpo_matcher`](https://nlp.johnsnowlabs.com/2025/05/01/hpo_matcher_en.html) | This model is a text matcher designed to automatically extract mentions of phenotypic abnormalities associated with human diseases from clinical or biomedical text. |
| [`stopwords_removal_hpo`](https://nlp.johnsnowlabs.com/2025/05/02/stopwords_removal_hpo_en.html) | This model is designed to remove stop words from clinical phenotype descriptions, particularly in the context of Human Phenotype Ontology (HPO). |
| [`hpo_mapper_pipeline`](https://nlp.johnsnowlabs.com/2025/05/02/hpo_mapper_pipeline_en.html) | This pipeline is designed to map extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes. It ensures that observed symptoms, signs, and clinical abnormalities are standardized using HPO terminology. |


- **Example of Models**:

```python
entityExtractor = TextMatcherInternalModel().pretrained("hpo_matcher","en", "clinical/models")\
    .setInputCols(["sentence", "clean_tokens"])\
    .setOutputCol("hpo_term")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

mapper = ChunkMapperModel().pretrained("hpo_mapper","en", "clinical/models")\
    .setInputCols(["hpo_term"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(True)


text =  '''Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity. 
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation. '''

data = spark.createDataFrame([[text]]).toDF("text")
```

*Result*:

{:.table-model-big}
|chunk             |begin|end|label|hpo_code  |
|------------------|-----|---|-----|----------|
|apnea             |9    |13 |HPO  |HP:0002104|
|HYPERBILIRUBINEMIA|59   |76 |HPO  |HP:0002904|
|hyperbilirubinemia|84   |101|HPO  |HP:0002904|
|sepsis            |160  |165|HPO  |HP:0100806|



- **Example of Pipeline**:

```python
pipeline = PretrainedPipeline("hpo_mapper_pipeline", "en", "clinical/models")

result = pipeline.fullAnnotate("""Presumed apnea of prematurity since < 34 wks gestation at birth.
HYPERBILIRUBINEMIA: At risk for hyperbilirubinemia d/t prematurity.
1/25-1/30: Received Amp/Gent while undergoing sepsis evaluation.""")
```

*Result*:

{:.table-model-big}
|chunk             |begin|end|label|hpo_code  |
|------------------|-----|---|-----|----------|
|apnea             |9    |13 |HPO  |HP:0002104|
|HYPERBILIRUBINEMIA|59   |76 |HPO  |HP:0002904|
|hyperbilirubinemia|84   |101|HPO  |HP:0002904|
|sepsis            |160  |165|HPO  |HP:0100806|

Please check the [Human Phenotype Extraction And HPO Code Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/49.Human_Phenotype_Extraction_And_HPO_Code_Mapping.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

#### Inferring Missing PHI Entities via Previously Detected NER Outputs Within Deidentification

**`setChunkMatching`**

This feature allows chunks like "NAME" and "DATE" to be inferred in contexts where they are not directly detected by NER, by referencing previously identified chunks within the same group. For example, if "NAME" was identified earlier in the document, similar text later in the group can be tagged accordingly—even if the NER model missed it due to lack of context.

- **`setChunkMatching({entity: threshold})`** enables chunk-level entity inference across multiple rows.
- Especially useful when entity annotations (e.g., `"NAME"`, `"DATE"`) are partially missing but present in other rows of the same group.
- Requires `setGroupByCol("your_grouping_column")` for context-based propagation.


*Example*:

```python
text = """
Created On : 10/22/2024 1:21PM Electronically Reviewed by: Kelly Goetz, M.A. on DOB 10/22/2024.Performed on Oct 22, 2024 12:48.
"""

deidentification = DeIdentification() \
    .setInputCols(["ner_chunk", "token", "sentence"]) \
    .setOutputCol("deidentified") \
    .setMode("masked") 

```

*Before Chunk Matching*:

{:.table-model-big}
|    | chunk        |   begin |   end | masked |
|---:|:-------------|--------:|------:|:----------|
|  0 | 10/22/2024   |      13 |    18 | DATE      |
|  1 | Kelly Goetz  |      55 |    62 | DOCTOR    |
|  2 | Oct 22, 2024 |     101 |   106 | DATE      |


```python
deidentification = DeIdentification() \
    .setInputCols(["ner_chunk", "token", "sentence"]) \
    .setOutputCol("deidentified") \
    .setMode("masked") \
    .setGroupByCol("filename") \
    .setChunkMatching({"NAME": 0.50, "DATE": 0.50})
```

*Results with Chunk Matching*:

{:.table-model-big}
|    | chunk        |   begin |   end | masked |
|---:|:-------------|--------:|------:|:----------|
|  0 | 10/22/2024   |      13 |    18 | DATE      |
|  1 | Kelly Goetz  |      55 |    62 | DOCTOR    |
|  2 | 10/22/2024   |      77 |    82 | DATE     |
|  3 | Oct 22, 2024 |      97 |   102 | DATE     |


**`groupByCol`**

A new capability has been added to support consistent obfuscation within groups using the `groupByCol` parameter in conjunction with `consistentObfuscation` and `ConsistentAcrossNameParts`.

- The `groupByCol` parameter allows partitioning the dataset into groups based on the values of a specified column.
- When used with `consistentObfuscation=True`, it ensures consistent entity replacements within each group (e.g., per document or per patient).
- **Default:** `""` (empty string) — grouping is disabled.
- **Type:** Must be a valid column of type `StringType` in the input DataFrame.
- The specified column must exist in the input data and must be of type `StringType`.
- Using this parameter may affect the row order of the dataset.
- This feature is **not supported** in `LightPipeline`.

*Example*:

```python
data = [
    ("file_1", "Patient John Doe visited on 2024-09-12 with complaints of chest pain. John Doe "),
    ("file_1", "Johm Doe was seen at St. Mary's Hospital in Boston. John Doe "),
    ("file_2", "Johm Doe has blood test results on 2025-01-05 were abnormal."),
    ("file_2", "Patient ID 8843921 experienced nausea and dizziness. John Doe "),
    ("file_3", "Michael Johnson was diagnosed with hypertension in New York."),
    ("file_4", "Maria Garcia came to the clinic on 2023-12-20 for a routine checkup."),
    ("file_4", "Contact number listed as (555) 123-4567."),
    ("file_4", "A follow-up was scheduled using the email maria.garcia@example.com, with a call planned for 2023-12-20."),
]

schema = StructType([
    StructField("id", StringType(), True),
    StructField("text", StringType(), True),
])

df = spark.createDataFrame(data, schema=schema)

obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setConsistentObfuscation(True)\
    .setGroupByCol("id")
``` 

**`ConsistentAcrossNameParts`**

The ConsistentAcrossNameParts parameter controls whether name obfuscation is applied consistently across different parts of a name entity, even when they appear separately in the text.

- **`ConsistentAcrossNameParts` (default: `True`)** ensures that all parts of a name entity (e.g., first name, last name) are consistently obfuscated, even when they appear separately in the text.

Behavior

- **When set to `True`**:
  - Full names and their individual components are mapped consistently.
  - Example:
    - "John Smith" → "Liam Brown"
    - "John" → "Liam"
    - "Smith" → "Brown"


</div><div class="h3-box" markdown="1">

#### Improved Name Consistency Handling in De-Identification

In this release, we have improved the way fake names are generated and assigned during the de-identification (De-ID) process. Previously, name tokens (e.g., first name and last name) were treated as a single chunk when generating a fake name. Now, each component of a name (first name, middle name, last name, etc.) is processed individually and then recombined into a full fake name.
This enhancement allows for more consistent obfuscation within documents, even when only partial name mentions appear (e.g., "John Smith" vs. "Mr. Smith"). As a result, the same fake name components will be used throughout a document for the same real-world identity, improving coherence and readability while preserving privacy.

**Note:** This change may lead to different fake name outputs compared to previous versions, especially for historical data. If users would like to retain the previous behavior (treating the full name as a single chunk and relying on previously generated fake names from earlier versions), they can set the corresponding configuration parameter to False.


</div><div class="h3-box" markdown="1">

#### Clinical Document Analysis with One-Liner Pretrained Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the clinical document analysis process. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for quickly extracting vital information.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_deid_nameAugmented_docwise_pipeline`](https://nlp.johnsnowlabs.com/2025/03/25/ner_deid_nameAugmented_docwise_pipeline_en.html) | This pipeline can be used to extract PHI information such as `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `VIN`, `ZIP` entities. |
| [`ner_deid_nameAugmented_pipeline_v3`](https://nlp.johnsnowlabs.com/2025/03/25/ner_deid_nameAugmented_pipeline_v3_en.html) | This pipeline can be used to extract PHI information such as `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `VIN`, `ZIP` entities. |
| [`ner_deid_subentity_docwise_augmented_pipeline_v2`](https://nlp.johnsnowlabs.com/2025/03/24/ner_deid_subentity_docwise_augmented_pipeline_v2_en.html) | This pipeline can be used to extract PHI information such as `LOCATION`, `CONTACT`, `PROFESSION`, `NAME`, `DATE`, `AGE`, `MEDICALRECORD`, `ORGANIZATION`, `HEALTHPLAN`, `DOCTOR`, `USERNAME`, `LOCATION-OTHER`, `URL`, `DEVICE`, `CITY`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `BIOID`, `FAX`, `LOCATION_OTHER`, `DLN`, `SSN`, `ACCOUNT`, `PLATE`, `VIN`, `LICENSE`, `IP` entities. |
| [`clinical_deidentification_nameAugmented_v3`](https://nlp.johnsnowlabs.com/2025/03/13/clinical_deidentification_nameAugmented_v3_en.html) | This pipeline can be used to extract PHI information such as `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `ORGANIZATION`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `VIN`, `ZIP` entities. |
| [`clinical_deidentification_subentity_enriched_ar`](https://nlp.johnsnowlabs.com/2025/03/13/clinical_deidentification_subentity_enriched_ar.html) | This pipeline can be used to extract PHI information such as `MEDICALRECORD`, `ORGANIZATION`, `PROFESSION`, `DOCTOR`, `USERNAME`, `URL`, `DEVICE`, `CITY`, `DATE`, `ZIP`, `STATE`, `PATIENT`, `COUNTRY`, `STREET`, `PHONE`, `HOSPITAL`, `EMAIL`, `IDNUM`, `AGE`, `LOCATION`, `DLN`, `SSN`, `PLATE`, `VIN`, `LICENSE`, `IP`, `ACCOUNT`, `DOB` entities. |
| [`clinical_deidentification_nameAugmented_docwise`](https://nlp.johnsnowlabs.com/2025/03/14/clinical_deidentification_nameAugmented_docwise_en.html) | This pipeline can be used to extract PHI information such as `ACCOUNT`, `AGE`, `BIOID`, `CITY`, `CONTACT`, `COUNTRY`, `DATE`, `DEVICE`, `DLN`, `EMAIL`, `FAX`, `HEALTHPLAN`, `IDNUM`, `IP`, `LICENSE`, `LOCATION`, `MEDICALRECORD`, `NAME`, `PHONE`, `PLATE`, `PROFESSION`, `SSN`, `STATE`, `STREET`, `URL`, `VIN`, `ZIP` entities. |

*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

deid_pipeline = PretrainedPipeline("ner_deid_nameAugmented_docwise_pipeline", "en", "clinical/models")

text = """Record date : 2093-01-13, Name : Hendrickson ORA. 25 years-old, MRN #719435.
IP: 203.120.223.13, the driver's license no:A334455B. The SSN: 324598674 and e-mail: hale@gmail.com.
Patient's VIN : 1HGBH41JXMN109286. Date : 01/13/93, PCP : David Hale."""
```

*Result*:

{:.table-model-big}
|result           |begin|end|entity       |
|-----------------|-----|---|-------------|
|2093-01-13       |14   |23 |DATE         |
|Hendrickson ORA  |33   |47 |NAME         |
|25               |50   |51 |AGE          |
|#719435          |68   |74 |MEDICALRECORD|
|203.120.223.13   |81   |94 |IP           |
|no:A334455B      |118  |128|DLN          |
|324598674        |140  |148|SSN          |
|hale@gmail.com   |162  |175|EMAIL        |
|1HGBH41JXMN109286|194  |210|VIN          |
|01/13/93         |220  |227|DATE         |
|David Hale       |236  |245|NAME         |



Please check the [Pretrained Clinical Pipelines](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.Pretrained_Clinical_Pipelines.ipynb) model for more information



</div><div class="h3-box" markdown="1">

####  Cloud Provider & LLM Benchmarks for Information Extraction Tasks

We conducted an extensive benchmark comparing **Spark NLP for Healthcare** against leading cloud-based NLP services and popular Large Language Models (LLMs). The evaluation covered a range of NLP tasks, including **Entity Recognition (NER), Assertion Detection, Medical Terminology Mapping**, and more.

The benchmark focused on assessing performance across several key clinical entity types. For each task, we measured critical metrics like **accuracy, coverage, precision, recall,** and **F1-score,** ensuring a comprehensive understanding of each system's strengths and weaknesses.

**Key Achievements:**

- Superior Accuracy & Coverage: Spark NLP consistently outperformed cloud providers such as **AWS Comprehend Medical, Google Cloud Healthcare API, Azure Text Analytics for Health,** and large language models like **Anthropic Claude - Sonnet 3.7 and OpenAI GPT-4.5.**
- Assertion Detection Excellence: Spark NLP demonstrated a clear edge in detecting contextual assertions (e.g., negation, uncertainty) in medical texts.
- Medical Terminology Mapping: Our solution excelled in mapping complex medical terminology, ensuring that nuanced healthcare concepts were accurately identified.
- NER Performance: Spark NLP achieved the highest accuracy in recognizing clinical entities like **diseases, procedures, and medications**, surpassing other services in precision and recall.
- Clinical Relevance: The benchmark highlighted Spark NLP’s ability to extract medically relevant entities with better context understanding, making it a reliable choice for healthcare NLP needs.

These findings were presented at the **NLP Summit**, reinforcing Spark NLP’s position as a highly reliable and effective solution for extracting complex medical entities from clinical documents, and making it the preferred choice for healthcare organizations looking for top-tier NLP performance.

![JSL vs Cloud Providers on NER](/assets/images/JSLvsCloudProviders.webp)

You can reproduce the results using the [NER Performance Comparison Of Healthcare NLP VS Cloud Solutions](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/academic/NER_Benchmarks/NER_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions.ipynb) notebook. 

For a detailed presentation of the benchmark results, you can watch the NLP Summit session here: [Benchmarks That Matter: Evaluating Medical Language Models for Real-World Applications](https://www.youtube.com/watch?v=uAoOaA_G2W4)

We prepared **9 distinct pretrained pipelines** using Spark NLP for Healthcare’s customization capabilities, all of which were utilized in this benchmark to ensure optimized performance across a range of clinical entity types.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`ner_admission_discharge_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_admission_discharge_benchmark_pipeline_en.html) | This pipeline can be used to detect clinical `Admission Discharge` in medical text, with a focus on admission entities. |
| [`ner_body_part_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_body_part_benchmark_pipeline_en.html) | This pipeline can be used to extract all types of anatomical references in medical text. It is a single-entity pipeline and generalizes all anatomical references to a single entity. |
| [`ner_drug_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_drug_benchmark_pipeline_en.html) | This pipeline can be used to extract posology information in medical text. |
| [`ner_procedure_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_procedure_benchmark_pipeline_en.html) | This pipeline can be used to extract `procedure` mentions in medical text. |
| [`ner_test_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_test_benchmark_pipeline_en.html) | This pipeline can be used to extract `test` mentions in medical text. |
| [`ner_treatment_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/27/ner_treatment_benchmark_pipeline_en.html) | This pipeline can be used to extract treatments mentioned in medical text. |
| [`ner_consumption_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/28/ner_consumption_benchmark_pipeline_en.html) | This pipeline can be used to extract `Consumption` (Alcohol, Smoking/Tobacco, and Substance Usage) related information in medical text. |
| [`ner_grade_stage_severity_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/28/ner_grade_stage_severity_benchmark_pipeline_en.html) | This pipeline can be used to extract biomarker, grade stage, and severity-related information in medical text. `GRADE_STAGE_SEVERITY`:  Mentions of pathological grading, staging, severity, and modifier of the diseases/cancers. |
| [`ner_problem_benchmark_pipeline`](https://nlp.johnsnowlabs.com/2025/03/28/ner_problem_benchmark_pipeline_en.html) | This pipeline can be used to extract `problem` (diseases, disorders, injuries, symptoms, signs .etc) information in medical text. |



</div><div class="h3-box" markdown="1">

#### Enabling flexible annotation transformations with `AnnotationConverter`

A versatile converter that transforms DataFrame annotations through custom logic. By defining conversion functions (`f`), users can modify annotations to perform transformations such as:

- Assertion outputs → Chunk outputs  
- LLM outputs → Document outputs
- rule-based outputs → Updated outputs

The converter integrates with PySpark NLP-style pipelines (e.g., DocumentAssembler, Tokenizer) but operates purely in Python.

*Example*:

```python
test_data = spark.createDataFrame([
    (1, """I like SparkNLP annotators such as MedicalBertForSequenceClassification and BertForAssertionClassification."""),
]).toDF("id", "text")
document_assembler = DocumentAssembler().setInputCol('text').setOutputCol('document')
tokenizer = Tokenizer().setInputCols('document').setOutputCol('token')

def myFunction(annotations):
    new_annotations = []
    pattern = r"(?<=[a-z])(?=[A-Z])"

    for annotation in annotations:
        text = annotation.result
        import re
        parts = re.split(pattern, text)
        begin = annotation.begin
        for part in parts:
            end = begin + len(part) - 1
            new_annotations.append(
                Annotation(
                    annotatorType="token",
                    begin=begin,
                    end=end,
                    result=part,
                    metadata=annotation.metadata,
                    embeddings=annotation.embeddings,
                )
            )
            begin = end + 1

    return new_annotations

camel_case_tokenizer = AnnotationConverter(f=myFunction)\
    .setInputCol("token")\
    .setOutputCol("camel_case_token")\
    .setOutputAnnotatorType("token")

pipeline = Pipeline(stages=[document_assembler, tokenizer, camel_case_tokenizer])
model = pipeline.fit(test_data)
df = model.transform(test_data)
df.selectExpr("explode(camel_case_token) as tokens").show(truncate=False)
```


*Result*:

df.selectExpr("explode(camel_case_token) as tokens").show(truncate=False)

{:.table-model-big}
|tokens                                               |
|-----------------------------------------------------|
|{token, 0, 0, I, {sentence -> 0}, []}                |
|{token, 2, 5, like, {sentence -> 0}, []}             |
|{token, 7, 11, Spark, {sentence -> 0}, []}           |
|{token, 12, 14, NLP, {sentence -> 0}, []}            |
|{token, 16, 25, annotators, {sentence -> 0}, []}     |
|{token, 27, 30, such, {sentence -> 0}, []}           |
|{token, 32, 33, as, {sentence -> 0}, []}             |
|{token, 35, 41, Medical, {sentence -> 0}, []}        |
|{token, 42, 45, Bert, {sentence -> 0}, []}           |
|{token, 46, 48, For, {sentence -> 0}, []}            |
|{token, 49, 56, Sequence, {sentence -> 0}, []}       |
|{token, 57, 70, Classification, {sentence -> 0}, []} |
|{token, 72, 74, and, {sentence -> 0}, []}            |
|{token, 76, 79, Bert, {sentence -> 0}, []}           |
|{token, 80, 82, For, {sentence -> 0}, []}            |
|{token, 83, 91, Assertion, {sentence -> 0}, []}      |
|{token, 92, 105, Classification, {sentence -> 0}, []}|
|{token, 106, 106, ., {sentence -> 0}, []}            |





</div><div class="h3-box" markdown="1">

####  Introducing 2 New Contextual Assertion Models to Detect Assertion Status Given a Larger Context and Scenarious

These models identify contextual cues within text data, such as negation, uncertainty, etc. They are used for clinical assertion detection and annotate text chunks with assertions.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`contextual_assertion_conditional`](https://nlp.johnsnowlabs.com/2025/03/12/contextual_assertion_conditional_en.html) | This model identifies contextual cues within text data to detect conditional assertions. |
| [`contextual_assertion_possible`](https://nlp.johnsnowlabs.com/2025/03/12/contextual_assertion_possible_en.html) | This model identifies contextual cues within text data to detect possible assertions. |

*Example*:

```python
clinical_ner = MedicalNerModel \
    .pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

contextual_assertion_conditional = ContextualAssertion.pretrained("contextual_assertion_conditional","en","clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setOutputCol("assertion_conditional")

contextual_assertion_possible = ContextualAssertion.pretrained("contextual_assertion_possible","en","clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setOutputCol("assertion_possible")

assertion_merger = AssertionMerger() \
    .setInputCols("assertion_conditional", "assertion_possible") \
    .setOutputCol("assertion_merger")


text = """The patient presents with symptoms suggestive of pneumonia, including fever, productive cough, and mild dyspnea.
Chest X-ray findings are compatible with a possible early-stage infection, though bacterial pneumonia cannot be entirely excluded.
The patient reports intermittent chest pain when engaging in physical activity, particularly on exertion. Symptoms appear to be contingent upon increased stress levels and heavy meals."""
```

*Result*:

{:.table-model-big}
|chunk           |begin|end|ner_label|assertion  |
|----------------|-----|---|---------|-----------|
|symptoms        |26   |33 |PROBLEM  |possible   |
|pneumonia       |49   |57 |PROBLEM  |possible   |
|fever           |70   |74 |PROBLEM  |possible   |
|productive cough|77   |92 |PROBLEM  |possible   |
|mild dyspnea    |99   |110|PROBLEM  |conditional|
|Chest X-ray     |113  |123|TEST     |conditional|


Please check the [Contextual Assertion](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.3.Contextual_Assertion.ipynb) model for more information


</div><div class="h3-box" markdown="1">

####  New German Medical Named Entity Recognition Model and Medical Entity Resolver Model

**NER Model**

This model extracts more than 40 oncology-related entities, including therapies, tests and staging in German.


*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_oncology_wip", "de", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

text = """Patientin: 67 Jahre, weiblich

Diagnose: Invasives duktales Mammakarzinom links (G3)

Befunde:

Schmerzloser, tastbarer Knoten im oberen äußeren Quadranten links
Hautrötung, eingezogene Mamille, tastbare axilläre Lymphknoten
Histologie:

ER + , PR + , HER2-negativ, Ki-67 bei 35 %
Bildgebung:

Mammographie: Tumor 2,8 cm, Mikroverkalkungen
MRT: Tumorgröße 3,1 cm mit Drüseninfiltration
PET-CT: Keine Fernmetastasen
Therapie:

Neoadjuvante Chemotherapie
Brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol (5 Jahre)
Beurteilung:
Fortgeschrittenes lokal begrenztes Mammakarzinom, günstiger Hormonrezeptorstatus. Therapie gemäß Tumorkonferenz empfohlen."""
```

*Result*:

{:.table-model-big}
|chunk                          |begin|end|ner_label           |
|-------------------------------|-----|---|--------------------|
|67 Jahre                       |11   |18 |Age                 |
|weiblich                       |21   |28 |Gender              |
|Invasives                      |41   |49 |Histological_Type   |
|duktales                       |51   |58 |Histological_Type   |
|Mammakarzinom links            |60   |78 |Cancer_Dx           |
|Knoten                         |120  |125|Tumor_Finding       |
|oberen äußeren Quadranten links|130  |160|Direction           |
|Mamille                        |186  |192|Site_Other_Body_Part|
|axilläre Lymphknoten           |204  |223|Site_Lymph_Node     |
|Histologie                     |225  |234|Pathology_Test      |
|ER                             |238  |239|Biomarker           |
|+                              |241  |241|Biomarker_Result    |
|PR                             |245  |246|Biomarker           |
|+                              |248  |248|Biomarker_Result    |
|HER2-negativ                   |252  |263|Biomarker           |
|Ki-67                          |266  |270|Biomarker           |
|35 %                           |276  |279|Biomarker_Result    |
|Bildgebung                     |281  |290|Imaging_Test        |
|Mammographie                   |294  |305|Imaging_Test        |
|Tumor                          |308  |312|Tumor_Finding       |
|2,8 cm                         |314  |319|Tumor_Size          |
|MRT                            |340  |342|Imaging_Test        |
|Tumorgröße                     |345  |354|Tumor_Finding       |
|3,1 cm                         |356  |361|Tumor_Size          |
|Drüseninfiltration             |367  |384|Histological_Type   |
|PET-CT                         |386  |391|Imaging_Test        |
|Neoadjuvante Chemotherapie     |426  |451|Chemotherapy        |
|Brusterhaltende Operation      |453  |477|Cancer_Surgery      |
|Sentinel-Lymphknotenbiopsie    |483  |509|Pathology_Test      |
|Adjuvante Strahlentherapie     |511  |536|Radiotherapy        |
|Hormontherapie                 |538  |551|Hormonal_Therapy    |
|Letrozol                       |557  |564|Hormonal_Therapy    |
|Fortgeschrittenes lokal        |589  |611|Staging             |
|Mammakarzinom                  |624  |636|Cancer_Dx           |



**Resolver Model**

This model maps German medical entities and concepts to ICD-10-GM codes using the sent_xlm_roberta_biolord_2023_m Sentence Embeddings. It also returns the official resolution text within the brackets inside the metadata.

*Example*:

```python
icd_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icd10gm_augmented", "de", "clinical/models") \
    .setInputCols(["biolord_embeddings"]) \
    .setOutputCol("icd_code")\
    .setDistanceFunction("EUCLIDEAN")

text = """Patientin: 67 Jahre, weiblich

Diagnose: Invasives duktales Mammakarzinom links (G3)

Histologie:

ER + , PR + , HER2-negativ, Ki-67 bei 35 %
Bildgebung:

Mammographie: Tumor 2,8 cm, Mikroverkalkungen
PET-CT: Keine Fernmetastasen
Therapie:

Neoadjuvante Chemotherapie
Brusterhaltende Operation mit Sentinel-Lymphknotenbiopsie
Adjuvante Strahlentherapie
Hormontherapie mit Letrozol (5 Jahre)
Beurteilung:
Fortgeschrittenes lokal begrenztes Mammakarzinom, günstiger Hormonrezeptorstatus. Therapie gemäß Tumorkonferenz empfohlen."""
```

*Result*:

{:.table-model-big}
| chunk | begin | end | ner_label | icd | resolution | all_resolution | all_result |
|-------|-------|-----|-----------|-----|------------|----------------|------------|
|Mammakarzinom links       |60   |78 |Cancer_Dx    |C50  |Brustdrüsenkarzinom [Bösartige Neubildung der Brustdrüse [Mamma]]                                       |Brustdrüsenkarzinom [Bösartige Neubildung der Brustdrüse [Mamma]]:::Krebs in der Brustdrüse, nicht näher klassifiziert [Brustdrüse, nicht näher bezeichnet]:::Mammakarzinom [Brustdrüse [Mamma]]:::Neoplasma malignum: UQ der Brustdrüse [Unterer äußerer Quadrant der Brustdrüse]:::Bösartige Mammaerkrankung [Bösartige Neubildung der Brustdrüse [Mamma] in der Familienanamnese]:::Bösartige Tumoren der Brustregion [Thorax]      |C50:::C50.9:::D48.6:::C50.5:::Z80.3:::C76.1            |
|Tumor                     |169  |173|Tumor_Finding|D36.9|Neubildung ohne spezifische Lokalisation [Gutartige Neubildung an nicht näher bezeichneter Lokalisation]|Neubildung ohne spezifische Lokalisation [Gutartige Neubildung an nicht näher bezeichneter Lokalisation]:::Neubildung ohne spezifische Angaben zu Lokalisationen [Neubildung unsicheren oder unbekannten Verhaltens an sonstigen und nicht näher bezeichneten Lokalisationen]:::Neubildung unspezifischen Verhaltens, ohne weitere Angaben [Neubildung unsicheren oder unbekannten Verhaltens, nicht näher bezeichnet]:::Neubildung... |D36.9:::D48:::D48.9:::D48.7:::D36.7:::C80:::C80.9:::D36|
|Adjuvante Strahlentherapie|326  |351|Radiotherapy |Z51.0|Radiotherapie-Sitzung [Strahlentherapie-Sitzung]                                                        |Radiotherapie-Sitzung [Strahlentherapie-Sitzung]:::Nachsorge nach Radiotherapie [Nachuntersuchung nach Strahlentherapie wegen anderer Krankheitszustände]:::Nachsorge nach Strahlentherapie bei malignen Tumoren [Nachuntersuchung nach Strahlentherapie wegen bösartiger Neubildung]:::Rehabilitation nach Strahlentherapie [Rekonvaleszenz nach Strahlentherapie]:::Strahlen- und Chemotherapie bei bösartigen Tumoren...            |Z51.0:::Z09.1:::Z08.1:::Z54.1:::Z51.82                 |
|Mammakarzinom             |439  |451|Cancer_Dx    |D48.6|Mammakarzinom [Brustdrüse [Mamma]]                                                                      |Mammakarzinom [Brustdrüse [Mamma]]:::Mamma-Karzinom [Bösartige Neubildung der Brustdrüse [Mamma]]:::Bösartige Mammaerkrankung [Bösartige Neubildung der Brustdrüse [Mamma] in der Familienanamnese]:::Krebs in der Brustdrüse, nicht näher klassifiziert [Brustdrüse, nicht näher bezeichnet]:::Bösartige Tumoren der Brustregion [Thorax]:::Neoplasma malignum: UQ der Brustdrüse [Unterer äußerer Quadrant der Brustdrüse]           |D48.6:::C50:::Z80.3:::C50.9:::C76.1:::C50.5            |


Please check the [German Healthcare Models](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/14.German_Healthcare_Models.ipynb) model for more information




</div><div class="h3-box" markdown="1">

#### Enabling Exception Handling within the Pipelines for Specified or All Eligible Stages

This utility module allows automated exception handling in pipelines by enabling `setDoExceptionHandling` on specific stages or all stages that support it. Users can choose stages manually or apply it globally, with an option to save the updated pipeline to a custom path.

*Example*:

```python
from sparknlp_jsl.utils import apply_exception_handling
from sparknlp.pretrained import PretrainedPipeline

oncology_pipeline = PretrainedPipeline("oncology_biomarker_pipeline", "en", "clinical/models")

handled_pipeline =  apply_exception_handling(oncology_pipeline)
```


*Result*:

```bash

📢 Summary Report:
✅ Total modified stages: 15
  - Stage 4: MedicalNerModel
  - Stage 5: NerConverterInternalModel
  - Stage 6: MedicalNerModel
  - Stage 7: NerConverterInternalModel
  - Stage 8: MedicalNerModel
  - Stage 9: NerConverterInternalModel
  - Stage 10: MedicalNerModel
  - Stage 11: NerConverterInternalModel
  - Stage 13: ChunkMergeModel
  - Stage 14: ChunkMergeModel
  - Stage 15: AssertionDLModel
  - Stage 16: ChunkFilterer
  - Stage 17: AssertionDLModel
  - Stage 21: RelationExtractionModel
  - Stage 22: RelationExtractionModel
⚠️ Total skipped stages: 9
  - Stage 0: DocumentAssembler (No exception handling support)
  - Stage 1: SentenceDetectorDLModel (No exception handling support)
  - Stage 2: TokenizerModel (No exception handling support)
  - Stage 3: WordEmbeddingsModel (No exception handling support)
  - Stage 12: TextMatcherInternalModel (No exception handling support)
  - Stage 18: AssertionMerger (No exception handling support)
  - Stage 19: PerceptronModel (No exception handling support)
  - Stage 20: DependencyParserModel (No exception handling support)
  - Stage 23: AnnotationMerger (No exception handling support)
```

</div><div class="h3-box" markdown="1">

#### Interactive Chat Support for Healthcare NLP Documentation
 
We’re introducing a conversational assistant powered by Healthcare NLP documentation and repositories. This new tool enables users to easily explore which components to use when solving specific problems, understand the functionalities of different modules, and get explanations for code found across our repositories — all through a simple chat interface.
 
Just type your question into the chatbox and get instant guidance on how to leverage Healthcare NLP more effectively. Whether you're debugging, exploring features, or looking for best practices, this assistant helps you find the right answers faster.
 
You can check the [chat support page](https://deepwiki.com/JohnSnowLabs/spark-nlp-workshop/1-overview) for spark-nlp-workshop repository.


</div><div class="h3-box" markdown="1">

#### New Peer-Reviewed Papers and Blog Posts On Various Topics

- Peer-Reviewed Papers:
    - [Can Zero-Shot Commercial API’s Deliver Regulatory-Grade Clinical Text De-Identification?](https://arxiv.org/pdf/2503.20794) We evaluate the performance of four leading solutions for de-identification of unstructured medical text - Azure Health Data Services, AWS Comprehend Medical, OpenAI GPT-4o, and John Snow Labs - on a ground truth dataset of 48 clinical documents annotated by medical experts. The analysis, conducted at both entity-level and token-level, suggests that John Snow Labs’ Medical Language Models solution achieves the highest accuracy, with a 96% F1-score in protected health information (PHI) detection, outperforming Azure (91%), AWS (83%), and GPT-4o (79%). John Snow Labs is not only the only solution which achieves regulatory-grade accuracy (surpassing that of human experts) but is also the most cost-effective solution: It is over 80% cheaper compared to Azure and GPT-4o, and is the only solution not priced by token. Its fixed-cost local deployment model avoids the escalating per-request fees of cloud-based services, making it a scalable and economical choice.
    - [Beyond Negation Detection: Comprehensive Assertion Detection Models for Clinical NLP](https://arxiv.org/pdf/2503.17425) Assertion status detection is a critical yet often overlooked component of clinical NLP, essential for accurately attributing extracted medical facts. Past studies narrowly focused on negation detection, resulting in underperforming commercial solutions such as AWS Medical Comprehend, Azure AI Text Analytics, and GPT-4o due to their limited domain adaptation. To address this gap, we developed state-of-the-art assertion detection models, including fine-tuned LLMs, transformer-based classifiers, few-shot classifiers, and deep learning (DL) approaches and evaluated our models against cloud-based commercial API solutions and legacy rule-based NegEx approach as well as GPT-4o. Our fine-tuned LLM achieves the highest overall accuracy (0.962), outperforming GPT-4o (0.901) and commercial APIs by a notable margin, particularly excelling in Present (+4.2%), Absent (+8.4%), and Hypothetical (+23.4%) assertions. Our DL-based models surpass commercial solutions in Conditional (+5.3%) and Associated with Someone Else (+10.1%), while few-shot classifier offers a lightweight yet highly competitive alternative (0.929), making it ideal for resource-constrained environments. Integrated within Spark NLP, our models consistently outperform black-box commercial solutions while enabling scalable inference and seamless integration with medical NER, Relation Extraction, and Terminology Resolution. These results reinforce the importance of domain-adapted, transparent, and customizable clinical NLP solutions over generalpurpose LLMs and proprietary APIs.


- Blog Posts:
    - [Contextual Entity Ruler: Enhance Named Entity Recognition with Contextual Rules](https://medium.com/john-snow-labs/contextual-entity-ruler-enhance-named-entity-recognition-with-contextual-rules-6123eec0cfc7) This blog post mention that Contextual Entity Ruler in Spark NLP refines entity recognition by applying context-aware rules to detected entities. It updates entities using customizable patterns, regex, and scope windows. It boosts accuracy by reducing false positives and adapting to niche contexts. Key features include token/character-based windows, prefix/suffix rules, and modes. Integrate it post-NER to enhance precision without retraining models
    - [Pretrained Zero-Shot Models for Clinical Entity Recognition: A Game Changer in Healthcare NLP](https://medium.com/john-snow-labs/pretrained-zero-shot-models-for-clinical-entity-recognition-a-game-changer-in-healthcare-nlp-cc634a287ac3) This blog post discover how Pretrained Zero-Shot Named Entity Recognition (NER) models simplify the recognition of entities in multiple domains with minimal configuration. Recent advancements in pretrained zero-shot NER models and their ease in being applied across different datasets and applications are described in the article.
    - [Task-Based Clinical NLP: Unlocking Insights with One-Liner Pipelines](https://medium.com/john-snow-labs/task-based-clinical-nlp-unlocking-insights-with-one-liner-pipelines-bda40c7df4bc) This blog post explores Healthcare NLP’s Task-Based Clinical Pretrained Pipelines, showcasing how they streamline clinical text analysis with just one-liner codes. By demonstrating the explain_clinical_doc_granular pipeline in a real-world scenario, we illustrate its capabilities in Named Entity Recognition (NER), Assertion Status, and Relation Extraction. These pipelines provide an efficient way to extract medical insights from unstructured clinical text, offering valuable tools for healthcare professionals and researchers.
    - [How Good Are Open-Source LLM-Based De-identification Tools in a Medical Context?](https://medium.com/john-snow-labs/how-good-are-open-source-llm-based-de-identification-tools-in-a-medical-context-6600ddac6a0f) It’s often assumed that all PII and PHI entities are the same, meaning de-identification tools should work equally well across all unstructured text. While this seems logical in theory, each domain-specific dataset has distinct characteristics, requiring customized approaches for effective PII detection. In this blog post, we highlight how LLM-based de-identification models, such as GLiNER PII and OpenPipe’s PII-Redact, excel in general text — achieving macro-average F1 scores of 0.62 for GLiNER and 0.98 for OpenPipe — but face significant performance drops on clinical datasets, where their scores fall to 0.41 and 0.42 respectively.
    - [Beyond Negation Detection: Comprehensive Assertion Detection Models for Clinical NLP](https://medium.com/john-snow-labs/beyond-negation-detection-comprehensive-assertion-detection-models-for-clinical-nlp-d90659a14408) Assertion status detection is critical in clinical NLP but often overlooked, leading to underperformance in commercial solutions like AWS Medical Comprehend, Azure AI Text Analytics, and GPT-4o. We developed advanced assertion detection models, including fine-tuned LLMs, transformers, few-shot classifiers, deep learning (DL) and rule -based approaches. Our fine-tuned LLM achieves 0.962 accuracy, outperforming GPT-4o (0.901) and commercial APIs, with notable improvements in Present (+4.2%), Absent (+8.4%), and Hypothetical (+23.4%) assertions. Our DL models also excel in Conditional (+5.3%) and Associated with Someone Else (+10.1%) categories. The few-shot classifier (0.929 accuracy) provides a lightweight alternative for resource-limited environments. Integrated with Spark NLP, our models offer scalable, transparent, and domain-adapted solutions that surpass black-box commercial APIs in medical NLP tasks.




</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Resolved log file creation on Databricks for training
- Added `consistentAcrossNameParts` param to `LightDeIdentification` and `StructuredDeIdentification`


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For Making Spark NLP For Healthcare Easier To Navigate And Understand

  - New [Spanish Healthcare Models](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/48.Spanish_Healthcare_Models.ipynb) Notebook
  - New [PRR ROR EBGM for Signal Processing of Drug Events](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/medical_use_cases/Signal_Processing_Drug_ADE/PRR_ROR_EBGM_for_Signal_Processing_of_Drug_Events.ipynb) Notebook
  - New [BertForAssertionClassification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/2.4.BertForAssertionClassification.ipynb) Notebook
  - New [NER Performance Comparison Of Healthcare NLP VS Cloud Solutions](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/academic/NER_Benchmarks/NER_Performance_Comparison_Of_Healthcare_NLP_VS_Cloud_Solutions.ipynb) Notebook
  - New [Fhir DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.10.Fhir_DeIdentification.ipynb) Notebook
  - New [Human Phenotype Extraction And HPO Code Mapping](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/49.Human_Phenotype_Extraction_And_HPO_Code_Mapping.ipynb) Notebook
  - Updated [German Clinical Deidentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.9.German_Clinical_Deidentification) Notebook
  - Updated [German Healthcare Models](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/14.German_Healthcare_Models.ipynb) Notebook
  - Updated [Deidentification Custom Pretrained Pipelines](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.7.Deidentification_Custom_Pretrained_Pipelines.ipynb) Notebook
  - Updated [Clinical_DeIdentification](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) Notebook
  - Updated [Analyse Veterinary Documents with Healthcare NLP](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/44.Analyse_Veterinary_Documents_with_Healthcare_NLP.ipynb) Notebook
  - Updated [Loading Medical and Open Souce LLMs](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `jsl_meds_text2soap_v1`
+ `assertion_bert_classification_radiology`
+ `assertion_bert_classification_jsl`
+ `assertion_bert_classification_clinical`
+ `ner_deid_nameAugmented_docwise_pipeline`
+ `ner_deid_nameAugmented_pipeline_v3`
+ `ner_deid_subentity_docwise_augmented_pipeline_v2`
+ `clinical_deidentification_docwise_wip`
+ `clinical_deidentification_nameAugmented_v3`
+ `clinical_deidentification_subentity_enriched_ar`
+ `clinical_deidentification_nameAugmented_docwise`
+ `clinical_deidentification_docwise_benchmark`
+ `ner_admission_discharge_benchmark_pipeline`
+ `ner_body_part_benchmark_pipeline`
+ `ner_drug_benchmark_pipeline`
+ `ner_procedure_benchmark_pipeline`
+ `ner_test_benchmark_pipeline`
+ `ner_treatment_benchmark_pipeline`
+ `ner_consumption_benchmark_pipeline`
+ `ner_grade_stage_severity_benchmark_pipeline`
+ `ner_problem_benchmark_pipeline`
+ `contextual_assertion_conditional`
+ `contextual_assertion_possible`
+ `ner_oncology_wip` -> de         
+ `biolordresolve_icd10gm_augmented` -> de
+ `hpo_matcher`
+ `hpo_mapper`
+ `stopwords_removal_hpo`
+ `hpo_mapper_pipeline`


</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
