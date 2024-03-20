---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.3.0
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_3_0
key: docs-licensed-release-notes
modify_date: 2024-02-29
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.3.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. This release comes with **the new 3 rule-based entity recognition/matcher modules to extract named entities with rules and a Flattener module to flatten the pipeline outputs effortlessly, as well as `41` new clinical pretrained models and pipelines including new De-Identification pipelines at various sizes**. 

+ 4 new `Opioid` NER models to extract opioid-related entities from 22 classes and 3 assertion models to detect the status of opioid drug usage and underlying symptoms.
+ `Multi-Lingual` NER model for `Deidentification` to detect sensitive entities (`name`, `date`, `location` etc.) from multiple languages.
+ New `Age` classification model to detect age groups from clinical texts without any mention of age.
+ `Biomarker` text classification model to detect sentences/ phrases that may contain biomarker-related terms.
+ New NER model for `SNOMED` term extraction regardless of its type.
+ New 6 `ChunkMapper` models for medical code mapping to map various medical terminologies across each other.
+ Curated pretrained pipelines to analyze clinical documents for specific clinical tasks and concepts at once.
+ Enhanced data exploration with the new `Flattener` annotator to prettify the pipeline outputs in a tabulated format.
+ Rule-based entity recognition/matcher modules (`TextMatcher`, `RegexMatcher` and `EntityRuler`)  to extract named entities with rules and dictionaries
+ Deidentification now supports masking and obfuscation at the same time without an additional stage
+ `ChunkMerger` now supports dictionary format for the selective merging
+ `MedicalQuestionAnswering` returns Score in metadata
+ New speed benchmarks for various pipelines across different platforms under various settings (EMR, Databricks, etc.)
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Consistent obfuscation is supported in `StructuredDeidentification` too 
    - Added `deid_source` field to the metadata to infer the source of entity chunks coming from internal or external NER models and stages
    - Refactoring the Deidentification module for improved functionality 
    - Flushing the temporary files dumped by the `SentenceEntityResolver` 
    - Fixed `IOBTagger` was returning zero instead of 'O'
    - Lighter jars for Spark NLP leading optimized Spark's sessions 
    - `Resolution2Chunk` documentation updated
    - Updated the default value of the `customBoundsStrategy` parameter in the `InternalDocumentSplitter`
    - Enhanced `InternalDocumentSplitter` with UUID Metadata Field
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [Flattener Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/41.Flattener.ipynb)
    - New [Rule Based Entity Matchers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb)
    - New [Opioid Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/42.Opioid_Models.ipynb)
    - Updated [Clinical Deidentification Improvement Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.4.Clinical_Deidentification_Improvement.ipynb)
    - New [OPIOID Demo](https://demo.johnsnowlabs.com/healthcare/OPIOID/)
    - New [Biomarker Classification Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_BIOMARKER/)
    - New [SNOMED Term NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_SNOMED_TERM/)
    - New [Multi Language NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEID_MULTI/)
    - Updated [Age Classification Demo](https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_AGE/)
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.



</div><div class="h3-box" markdown="1">

#### 4 New `Opioid` NER Model to Extract Opioid-Related Entities from 22 Classes and 3 Assertion Models to Detect the Status of Opioid Drug Usage and Underlying Symptoms.


- NER Model

|Model Name         | Predicted Entities | Description      |
|-------------------|--------------------|------------------|
| [ner_opioid](https://nlp.johnsnowlabs.com/2024/02/28/ner_opioid_en.html) | `communicable_disease`, `general_symptoms`, `substance_use_disorder`, `drug_duration`, `psychiatric_issue`, `drug_strength`, `drug_quantity`, `other_drug`, `drug_form`, `drug_frequency`, `opioid_drug`, `drug_route`, `employment`, `violence`, `legal_issue`, `other_disease`, `alcohol_use`, `test`, `marital_status`, `test_result`, `antidote`, `sexual_orientation` | Detects opioid-related entities within text data |

This `ner_opioid` model is designed to detect and label opioid-related entities within text data. Opioids are a class of drugs that include the illegal drug heroin, synthetic opioids such as fentanyl, and pain relievers available legally by prescription. The model has been trained using advanced deep-learning techniques on a diverse range of text sources and can accurately recognize and classify a wide range of opioid-related entities. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results.

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_opioid", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")


sample_texts = ["""The patient, unmarried and with a significant history of substance abuse involving the illicit consumption of various opioids such as heroin, fentanyl, and oxycodone, presented with a headache and was diagnosed PTSD. Despite denying the use of alcohol, smoking, or marijuana, the patient, who has been unemployed for several months, required administration of Narcan for suspected opioid overdose. A recent toxicology screen confirmed the presence of opioids, and showed negative results for benzodiazepines, cocaine, amphetamines, barbiturates, and tricyclic substances."""]

```

*Result*:

|chunk               |begin|end|ner_label             |
|--------------------|-----|---|----------------------|
|unmarried           |13   |21 |marital_status        |
|substance abuse     |57   |71 |substance_use_disorder|
|opioids             |118  |124|opioid_drug           |
|heroin              |134  |139|opioid_drug           |
|fentanyl            |142  |149|opioid_drug           |
|oxycodone           |156  |164|opioid_drug           |
|headache            |184  |191|general_symptoms      |
|PTSD                |211  |214|psychiatric_issue     |
|alcohol             |244  |250|alcohol_use           |
|marijuana           |265  |273|other_drug            |
|unemployed          |302  |311|employment            |
|Narcan              |360  |365|antidote              |
|opioid              |381  |386|opioid_drug           |
|overdose            |388  |395|other_disease         |
|toxicology screen   |407  |423|test                  |
|opioids             |451  |457|test                  |
|negative            |471  |478|test_result           |
|benzodiazepines     |492  |506|test                  |
|cocaine             |509  |515|test                  |
|amphetamines        |518  |529|test                  |
|barbiturates        |532  |543|test                  |
|tricyclic substances|550  |569|test                  |


- Assertion Models

|Model Name         | Assertion Status | Description      |
|-------------------|-------------------|------------------|
| [assertion_opioid_wip](https://nlp.johnsnowlabs.com/2024/02/28/assertion_opioid_wip_en.html) | `present`, `history`, `absent`, `hypothetical`, `past`, `family_or_someoneelse` | Detects the assertion status of entities related to opioid |
| [assertion_opioid_drug_status_wip](https://nlp.johnsnowlabs.com/2024/02/28/assertion_opioid_drug_status_wip_en.html) | `opioid_medical_use`, `opioid_abuse`, `opioid_overdose`, `drug_medical_use`, `drug_abuse`, `drug_overdose` | Detects the assertion status of drug entities related to opioid (including opioid_drug and other_drug) |
| [assertion_opioid_general_symptoms_status_wip](https://nlp.johnsnowlabs.com/2024/02/28/assertion_opioid_general_symptoms_status_wip_en.html) | `underlying_pain`, `withdrawal_symptom`, `overdose_symptom` | Detects the assertion status of general symptoms entity related to opioid. |


*Example*:

```python
assertion = AssertionDLModel.pretrained("assertion_opioid_wip" "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

sample_texts = [
    """The patient with a history of substance abuse presented with clinical signs indicative of opioid overdose, including constricted pupils, cyanotic lips, drowsiness, and confusion. Immediate assessment and intervention were initiated to address the patient's symptoms and stabilize their condition. Close monitoring for potential complications, such as respiratory depression, was maintained throughout the course of treatment.""",
    """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency."""]

```

*Result*:

|chunk                 |begin|end|ner_label             |assertion   |confidence|
|----------------------|-----|---|----------------------|------------|----------|
|substance abuse       |30   |44 |substance_use_disorder|history     |0.9644    |
|opioid                |90   |95 |opioid_drug           |hypothetical|0.7974    |
|overdose              |97   |104|other_disease         |hypothetical|0.9961    |
|constricted pupils    |117  |134|general_symptoms      |past        |0.732     |
|cyanotic lips         |137  |149|general_symptoms      |past        |0.8501    |
|drowsiness            |152  |161|general_symptoms      |past        |0.9469    |
|confusion             |168  |176|general_symptoms      |past        |0.9686    |
|respiratory depression|351  |372|other_disease         |hypothetical|0.5921    |
|opioid                |82   |87 |opioid_drug           |history     |0.735     |
|percocet              |143  |150|opioid_drug           |present     |0.905     |
|pills                 |152  |156|drug_form             |present     |0.9363    |
|withdrawal            |220  |229|general_symptoms      |present     |0.9929    |
|opioid                |256  |261|opioid_drug           |present     |0.9348    |


Please check [Opioid Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/42.Opioid_Models.ipynb) for more information


</div><div class="h3-box" markdown="1">

#### `Multi-Lingual` NER Model for `Deidentification` to Detect Sensitive Entities (`name`, `date`, `location` etc.) from Multiple Languages.

Introducing our latest innovation: a Multilingual Named Entity Recognition (NER) model designed for deidentification purposes. This new model is capable of annotating text in English, German, French, Italian, Spanish, Portuguese, and Romanian. It excels at detecting sensitive entities such as AGE, CONTACT, DATE, ID, LOCATION, NAME, and PROFESSION. Using this model, data protection can be achieved in multiple languages and domains. 

*Example*:

```python
embeddings = XlmRoBertaEmbeddings.pretrained("xlm_roberta_base", "xx") \
    .setInputCols("sentence", "token") \
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)

ner = MedicalNerModel.pretrained("ner_deid_multilingual", "xx", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

text_list = [
"""Record date : 2093-01-13, David Hale, M.D., Name : Hendrickson, Ora MR. # 7194334 Date : 01/13/93 .""",
"""J'ai vu en consultation Michel Martinez (49 ans) adressé au Centre Hospitalier De Plaisir pour un diabète mal contrôlé avec des symptômes datant de Mars 2015.""",
"""Michael Berger wird ins St. Elisabeth-Krankenhaus in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""",
"""Ho visto Gastone Montanariello (49 anni) riferito all' Ospedale San Camillo per diabete mal controllato con sintomi risalenti a marzo 2015.""",
"""Antonio Miguel Martínez, un varón de 35 años de edad, de profesión auxiliar de enfermería y nacido en Cadiz, España.""",
"""Detalhes do paciente. Nome do paciente:  Pedro Gonçalves. Endereço: Rua Das Flores 23. Cidade/ Província: Porto.""",
"""Spitalul Pentru Ochi de Deal, Drumul Oprea Nr. 972 Vaslui, 737405 România"""
]
```

*Result*:

|doc_id|begin|end|chunk                        |ner_label |
|------|-----|---|-----------------------------|----------|
|1     |14   |23 |2093-01-13                   |DATE      |
|1     |26   |35 |David Hale                   |NAME      |
|1     |51   |61 |Hendrickson                  |NAME      |
|1     |74   |80 |7194334                      |ID        |
|1     |89   |96 |01/13/93                     |DATE      |
|2     |24   |38 |Michel Martinez              |NAME      |
|2     |41   |46 |49 ans                       |AGE       |
|2     |60   |88 |Centre Hospitalier De Plaisir|LOCATION  |
|2     |148  |156|Mars 2015                    |DATE      |
|3     |0    |13 |Michael Berger               |NAME      |
|3     |53   |65 |Bad Kissingen                |LOCATION  |
|3     |86   |91 |Berger                       |NAME      |
|3     |128  |129|76                           |AGE       |
|4     |9    |29 |Gastone Montanariello        |NAME      |
|4     |32   |33 |49                           |AGE       |
|4     |55   |74 |Ospedale San Camillo         |LOCATION  |
|4     |128  |137|marzo 2015                   |DATE      |
|5     |0    |22 |Antonio Miguel Martínez      |NAME      |
|5     |37   |38 |35                           |AGE       |
|5     |67   |88 |auxiliar de enfermería       |PROFESSION|
|5     |102  |106|Cadiz                        |LOCATION  |
|5     |109  |114|España                       |LOCATION  |
|6     |41   |55 |Pedro Gonçalves              |NAME      |
|6     |68   |71 |Rua Das Flores               |NAME      |
|6     |106  |110|Porto                        |LOCATION  |
|7     |0    |27 |Spitalul Pentru Ochi de Deal |LOCATION  |
|7     |30   |44 |Drumul Oprea Nr              |LOCATION  |
|7     |47   |49 |972                          |LOCATION  |
|7     |51   |56 |Vaslui                       |LOCATION  |
|7     |59   |64 |737405                       |LOCATION  |
|7     |66   |72 |România                      |LOCATION  |


Please see the model card [ner_deid_multilingual](https://nlp.johnsnowlabs.com/2024/02/12/ner_deid_multilingual_xx.html) for more information about the model 



</div><div class="h3-box" markdown="1">

#### New `Age` Classification Model to Detect Age Groups from Clinical Texts without any Mention of Age

Introducing a new age classification model is a sophisticated text classification tool tailored to identify and categorize text according to different age groups. This model distinguishes among `Old Adult`, `Adult`, `Child and Teen`, and `Other/Unknown` contexts, providing valuable insights into textual data that references age-specific scenarios or concerns.

*Example*:

```python

generic_classifier = GenericClassifierModel.pretrained("genericclassifier_age_e5", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

sample_texts = [
"""The patient presents with conditions often associated with the stresses and lifestyle of early career and possibly higher education stages, including sleep irregularities and repetitive stress injuries. There's a notable emphasis on preventative care, with discussions around lifestyle choices that can impact long-term health, such as smoking cessation, regular exercise, and balanced nutrition. The patient is also counseled on mental health, particularly in managing stress and anxiety that may arise from personal and professional responsibilities and ambitions at this stage of life.""",
"""The senior patient presents with age-related issues such as reduced hearing and vision, arthritis, and memory lapses. Emphasis is on managing chronic conditions, maintaining social engagement, and adapting lifestyle to changing physical abilities. Discussions include medication management, dietary adjustments to suit older digestion, and the importance of regular, low-impact exercise.""",
"""The late teenage patient is dealing with final growth spurts, the stress of impending adulthood, and decisions about higher education or career paths. Health discussions include maintaining a balanced diet, the importance of regular sleep patterns, and managing academic and social pressures. Mental health support is considered crucial at this stage, with a focus on building resilience and coping mechanisms.""",
"""The patient, faces adjustments to a new lifestyle with changes in daily routines and social interactions. Health concerns include managing the transition from an active work life to more leisure time, which may impact physical and mental health. Preventative health measures are emphasized, along with the importance of staying mentally and physically active and engaged in the community."""
]
```

*Result*:

|                                                                                                text|         result|
|----------------------------------------------------------------------------------------------------|---------------|
|The patient presents with conditions often associated with the stresses and lifestyle of early ca...|          Adult|
|The senior patient presents with age-related issues such as reduced hearing and vision, arthritis...|      Old Adult|
|The late teenage patient is dealing with final growth spurts, the stress of impending adulthood, ...| Child and Teen|
|The patient, faces adjustments to a new lifestyle with changes in daily routines and social inter...|  Other/Unknown|


Please check: [genericclassifier_age_e5](https://nlp.johnsnowlabs.com/2024/02/12/genericclassifier_age_e5_en.html)



</div><div class="h3-box" markdown="1">

#### `Biomarker` Text Classification Model to Detect Sentences/Phrases that may Contain Biomarker-related Terms

We are thrilled to introduce our latest advancement: a cutting-edge text classification model specifically tailored for biomarkers. This state-of-the-art model is designed to analyze clinical sentences and accurately determine whether they contain terms associated with biomarkers. 

- `1`: Contains biomarker related terms.
- `0`: Doesn't contain biomarker related terms.

*Example*:

```python

sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_biomarker", "en", "clinical/models")\
    .setInputCols(["sentence",'token'])\
    .setOutputCol("prediction")

sample_texts = [
"""In the realm of cancer research, several biomarkers have emerged as crucial indicators of disease progression and treatment response. For instance, the expression levels of HER2/neu, a protein receptor, have been linked to aggressive forms of breast cancer. Additionally, the presence of prostate-specific antigen (PSA) is often monitored to track the progression of prostate cancer. Moreover, in cardiovascular health, high-sensitivity C-reactive protein (hs-CRP) serves as a biomarker for inflammation and potential risk of heart disease. Meanwhile, elevated levels of troponin T are indicative of myocardial damage, commonly observed in acute coronary syndrome. In the field of diabetes management, glycated hemoglobin is a widely used to assess long-term blood sugar control. Its levels reflect the average blood glucose concentration over the past two to three months, offering valuable insights into disease management strategies."""
]
```

*Result*:

|sentence                                                                                                                                                    |prediction|
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|In the realm of cancer research, several biomarkers have emerged as crucial indicators of disease progression and treatment response.                       |0         |
|For instance, the expression levels of HER2/neu, a protein receptor, have been linked to aggressive forms of breast cancer.                                 |1         |
|Additionally, the presence of prostate-specific antigen (PSA) is often monitored to track the progression of prostate cancer.                               |1         |
|Moreover, in cardiovascular health, high-sensitivity C-reactive protein (hs-CRP) serves as a biomarker for inflammation and potential risk of heart disease.|1         |
|Meanwhile, elevated levels of troponin T are indicative of myocardial damage, commonly observed in acute coronary syndrome.                                 |0         |
|In the field of diabetes management, glycated hemoglobin is a widely used to assess long-term blood sugar control.                                          |0         |
|Its levels reflect the average blood glucose concentration over the past two to three months, offering valuable insights into disease management strategies.|0         |


Please check: [bert_sequence_classifier_biomarker](https://nlp.johnsnowlabs.com/2024/02/13/bert_sequence_classifier_biomarker_en.html)


</div><div class="h3-box" markdown="1">

#### New NER Model for SNOMED Term Extraction Regardless of its Type

We are excited to introduce our latest Name Entity Recognition (NER) model, designed specifically to extract SNOMED terms from clinical text. This cutting-edge model offers enhanced accuracy and efficiency in identifying and categorizing SNOMED concepts within medical documents, aiding in comprehensive data analysis and clinical decision-making processes. With its advanced capabilities, this NER model promises to revolutionize the way healthcare professionals extract valuable insights from clinical narratives.

*Example*:

```python

embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_snomed_term", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

text_list = ["""The patient was diagnosed with acute appendicitis and scheduled for immediate surgery.""",
"""Due to experiencing chronic pain, the patient was referred to a fibromyalgia specialist for further evaluation.""",
"""His hypertension is currently managed with a combination of lifestyle modifications and medication.""",
"""The child was brought in with symptoms of acute otitis, including ear pain and fever.""",
"""Laboratory tests indicate the individual has hyperthyroidism, requiring further endocrinological assessment.""",
"""The radiograph showed evidence of a distal radius fracture from a recent fall."""]

```

*Result*:

|doc_id|begin|end|chunk             |ner_label  |
|------|-----|---|------------------|-----------|
|1     |31   |48 |acute appendicitis|snomed_term|
|2     |20   |31 |chronic pain      |snomed_term|
|2     |63   |74 |fibromyalgia      |snomed_term|
|3     |4    |15 |hypertension      |snomed_term|
|4     |48   |53 |otitis            |snomed_term|
|4     |65   |72 |ear pain          |snomed_term|
|5     |45   |59 |hyperthyroidism   |snomed_term|
|6     |4    |13 |radiograph        |snomed_term|
|6     |43   |57 |radius fracture   |snomed_term|


Please check: [ner_snomed_term](https://nlp.johnsnowlabs.com/2024/02/13/ner_snomed_term_en.html)


</div><div class="h3-box" markdown="1">

#### New 6 ChunkMapper Models for Medical Code Mapping to Map Various Medical Terminologies Across Each Other

Introducing a suite of new ChunkMapper models designed to streamline medical code mapping tasks. These models include mappings between UMLS, LOINC, CPT, and SNOMED codes, offering a comprehensive solution for interoperability within medical systems.

| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
|[`umls_loinc_mapper`](https://nlp.johnsnowlabs.com/2024/02/15/umls_loinc_mapper_en.html)  | Maps UMLS codes to corresponding LOINC codes. |
|[`umls_cpt_mapper`](https://nlp.johnsnowlabs.com/2024/02/27/umls_cpt_mapper_en.html)    | Maps UMLS codes to corresponding CPT codes.   |
|[`umls_snomed_mapper`](https://nlp.johnsnowlabs.com/2024/02/26/umls_snomed_mapper_en.html) | Maps UMLS codes to corresponding SNOMED codes.|
|[`snomed_umls_mapper`](https://nlp.johnsnowlabs.com/2024/02/26/snomed_umls_mapper_en.html) | Maps SNOMED codes to corresponding UMLS codes.|
|[`cpt_umls_mapper`](https://nlp.johnsnowlabs.com/2024/02/27/cpt_umls_mapper_en.html)    | Maps CPT codes to corresponding UMLS codes.   |
|[`loinc_umls_mapper`](https://nlp.johnsnowlabs.com/2024/02/19/loinc_umls_mapper_en.html)  | Maps LOINC codes to corresponding UMLS codes. |


*Example*:

```python
chunkerMapper = ChunkMapperModel.pretrained("umls_loinc_mapper", "en", "clinical/models")\
    .setInputCols(["umls_code"])\
    .setOutputCol("mappings")\
    .setRels(["loinc_code"])

text = "acebutolol"
```

*Result*:

|      chunk |     UMLS |     LOINC |   relation |
|-----------:|---------:|----------:|-----------:|
| acebutolol | C0000946 | LP16015-7 | loinc_code |



</div><div class="h3-box" markdown="1">

#### Curated Pretrained Pipelines to Analyse Clinical Documents for Specific Clinical Tasks and Concepts at Once

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the process of analyzing clinical documents. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for extracting vital information with unprecedented ease.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.


| Pipeline Name                                                            |      Description            |
|--------------------------------------------------------------------------|-------------------------------------------|
| [`hcpcs_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/30/hcpcs_resolver_pipeline_en.html) | This pipeline extracts `PROCEDURE` entities and maps them to their corresponding [Healthcare Common Procedure Coding System (HCPCS)](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HCPCS/index.html) codes. |
| [`hgnc_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/30/hgnc_resolver_pipeline_en.html) | This pipeline extracts `GENE` entities and maps them to their corresponding [HUGO Gene Nomenclature Committee (HGNC)](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/HGNC/index.html) codes. |
| [`icd10cm_generalised_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/30/icd10cm_generalised_resolver_pipeline_en.html) | This pipeline extracts the following entities and maps them to their ICD-10-CM codes. It predicts ICD-10-CM codes up to 3 characters (according to ICD-10-CM code structure the first three characters represent the general type of injury or disease). |
| [`loinc_numeric_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/30/loinc_numeric_resolver_pipeline_en.html) | This pipeline extracts `TEST` entities and maps them to their corresponding Logical Observation Identifiers Names and Codes(LOINC) codes. It is trained with the numeric LOINC codes, without the inclusion of LOINC “Document Ontology” codes starting with the letter “L”. It also provides the official resolution of the codes within the brackets.  |
| [`snomed_procedures_measurements_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/01/31/snomed_procedures_measurements_resolver_pipeline_en.html) | This pipeline extracts `Procedure` and measurement (`Test`) entities and maps them to their corresponding SNOMED codes. |
| [`ncit_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/02/01/ncit_resolver_pipeline_en.html) | This advanced pipeline extracts oncological entities from clinical texts to map these entities to their corresponding National Cancer Institute Thesaurus (NCIt) codes. |
| [`rxcui_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/02/01/rxcui_resolver_pipeline_en.html) | This advanced pipeline extracts medication entities from clinical texts to map these entities to their corresponding RxNorm Concept Unique Identifier (RxCUI) codes. |
| [`icd10pcs_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/02/02/icd10pcs_resolver_pipeline_en.html) | This pipeline extracts `Procedure` entities from clinical texts and map them to their corresponding ICD-10-PCS codes. |
| [`icdo_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/02/02/icdo_resolver_pipeline_en.html) | This pipeline extracts oncological entities from clinical texts and maps them to their corresponding ICD-O codes. |
| [`loinc_resolver_pipeline`](https://nlp.johnsnowlabs.com/2024/02/02/loinc_resolver_pipeline_en.html) | This pipeline extracts `Test` entities from clinical texts and maps them to their corresponding Logical Observation Identifiers Names and Codes (LOINC) codes. |
| [`clinical_deidentification_obfuscation_medium`](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_medium_en.html) | This pipeline can be used to detect the PHI information from medical texts and obfuscate (replace them with fake ones) in the resulting text. |
| [`clinical_deidentification_obfuscation_small`](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_small_en.html) |  This pipeline can be used to detect the PHI information from medical texts and obfuscate (replace them with fake ones) in the resulting text. |



</div><div class="h3-box" markdown="1">

#### Enhanced Data Exploration with the New Flattener Annotator to Prettify the Pipeline Outputs in a Tabulated Format

Introducing the latest addition to our annotation toolkit: the Flattener Annotator. This powerful tool facilitates data exploration by returning exploded columns for each specified field containing annotation data. With customizable settings, users can select fields of interest and effortlessly explode their content for deeper analysis. 

*Example*:

```python
ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk") \
    .setWhiteList(["SYMPTOM","VS_FINDING","DISEASE_SYNDROME_DISORDER","ADMISSION_DISCHARGE","PROCEDURE"])
    
clinical_assertion = AssertionDLModel.pretrained("assertion_jsl_augmented", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion") \

# returns exploded columns for each specified field containing annotation data.
flattener = Flattener()\
    .setInputCols("ner_chunk", "assertion") \
    .setExplodeSelectedFields({"ner_chunk": ["result as ner_chunks",
                                             "begin as begins",
                                             "end as ends",
                                             "metadata.entity as entity"],
                               "assertion":["result as assertions",
                                            "metadata.confidence as confidence"]
                               })

text = """
GENERAL: He is an elderly gentleman in no acute distress. He is sitting up in bed eating his breakfast. He is alert and oriented and answering questions appropriately.
HEENT: Sclerae showed mild arcus senilis in the right. Left was clear. Pupils are equally round and reactive to light. Extraocular movements are intact. Oropharynx is clear.
NECK: Supple. Trachea is midline. No jugular venous pressure distention is noted. No adenopathy in the cervical, supraclavicular, or axillary areas.
ABDOMEN: Soft and not tender. There may be some fullness in the left upper quadrant, although I do not appreciate a true spleen with inspiration.
EXTREMITIES: There is some edema, but no cyanosis and clubbing .
"""
```

*Result*:

|ner_chunks                        |begins|ends|entity                   |assertions|confidence|
|----------------------------------|------|----|-------------------------|----------|----------|
|distress                          |49    |56  |SYMPTOM                  |Absent    |0.9999    |
|arcus senilis                     |196   |208 |DISEASE_SYNDROME_DISORDER|Past      |1.0       |
|jugular venous pressure distention|380   |413 |SYMPTOM                  |Absent    |1.0       |
|adenopathy                        |428   |437 |SYMPTOM                  |Absent    |1.0       |
|tender                            |514   |519 |SYMPTOM                  |Absent    |1.0       |
|fullness                          |540   |547 |SYMPTOM                  |Possible  |1.0       |
|edema                             |665   |669 |SYMPTOM                  |Present   |1.0       |
|cyanosis                          |679   |686 |VS_FINDING               |Absent    |1.0       |
|clubbing                          |692   |699 |SYMPTOM                  |Absent    |1.0       |


Please check [Flattener Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/41.Flattener.ipynb) for more information.


</div><div class="h3-box" markdown="1">

#### Rule-based Entity Recognition/matcher Modules (`TextMatcher`, `RegexMatcher` and `EntityRuler`)  to Extract Mamed Entities with Rules and Dictionaries

- Efficient Regex Matching with the new `RegexMatcherInternal` annotator
  
The **`RegexMatcherInternal`** class implements an internal annotator approach to match a set of regular expressions with a provided entity. This approach is utilized for associating specific patterns within text data with predetermined entities, such as dates, mentioned within the text.

The class allows users to define rules using regular expressions paired with entities, offering flexibility in customization. These rules can either be directly set using the `setRules` method, with a specified delimiter, or loaded from an external file using the `setExternalRules` method. 


*Example*:

```python
rules = '''
(\d{1,3}\.){3}\d{1,3}~IPADDR
\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{2}|\d{2}/\d{2}/\d{2}~DATE
'''

with open('./rules/regex_rules.txt', 'w') as f:
    f.write(rules)

regex_matcher_internal = RegexMatcherInternal()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='./rules/regex_rules.txt',
                      delimiter='~')

text = """Name : Hendrickson, Ora, Record date: 2093-01-13, MR #719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no: A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com."""
```

*Result*:

|  regex_result|begin|end|ner_label|
|--------------|-----|---|---------|
|    2093-01-13|   38| 47|     DATE|
|203.120.223.13|   97|110|   IPADDR|
|      01/13/93|  188|195|     DATE|

Please check [Rule Based Entity Matchers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more information.


</div><div class="h3-box" markdown="1">
  
- Efficient Text Matching with the new `TextMatcherInternal` annotator

The `TextMatcherInternal` annotator provides a robust solution for matching exact phrases against a given document. Users can specify phrases of interest in a source file, where each phrase is paired with its corresponding label or entity, separated by a `delimiter`. The annotator allows for fine-tuned control over the matching process through various parameters. Users can choose to enable case sensitivity, merge overlapping matched chunks, and customize entity metadata fields. Additionally, options like setting the delimiter and specifying whether the matcher should operate on chunks or tokens offer further flexibility.

*Text Matcher Pretrained Models*:

|model|entities|
|:----|-------|
| [drug_matcher](https://nlp.johnsnowlabs.com/2024/03/06/drug_matcher_en.html)  |`DRUG` |
| [biomarker_matcher](https://nlp.johnsnowlabs.com/2024/03/06/biomarker_matcher_en.html)  |`Biomarker` |

*Example*:

```python
matcher_drug = """
Aspirin 100mg#Drug
aspirin#Drug
paracetamol#Drug
amoxicillin#Drug
ibuprofen#Drug
lansoprazole#Drug
"""

with open ('matcher_drug.csv', 'w') as f:
  f.write(matcher_drug)

entityExtractor = TextMatcherInternal()\
    .setInputCols(["document", "token"])\
    .setEntities("matcher_drug.csv")\
    .setOutputCol("matched_text")\
    .setCaseSensitive(False)\
    .setDelimiter("#")\
    .setMergeOverlapping(False)

text = """John's doctor prescribed aspirin 100mg for his heart condition, along with paracetamol for his fever, amoxicillin for his tonsilitis, ibuprofen for his inflammation, and lansoprazole for his GORD."""
```

*Result*:

|        chunk|begin|end|label|
|-------------|-----|---|-----|
|      aspirin|   25| 31| Drug|
|aspirin 100mg|   25| 37| Drug|
|  paracetamol|   75| 85| Drug|
|  amoxicillin|  102|112| Drug|
|    ibuprofen|  134|142| Drug|
| lansoprazole|  170|181| Drug|


Please check [Rule Based Entity Matchers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more information.


</div><div class="h3-box" markdown="1">
  
- Efficient Text Matching with the new `EntityRulerInternal` annotator

The `EntityRulerInternal` is a versatile annotator designed to match exact strings or regex patterns against a given document, assigning them named entities as specified. This powerful tool allows users to define custom rules in a file, accommodating any number of named entities. By leveraging this annotator, users can efficiently identify and classify specific text patterns within documents, enhancing the accuracy and efficiency of named entity recognition tasks. 


*Example*:

```python
data = [
    {
        "id": "drug-words",
        "label": "Drug",
        "patterns": ["paracetamol", "aspirin", "ibuprofen", "lansoprazol"]
    },
    {
        "id": "disease-words",
        "label": "Disease",
        "patterns": ["heart condition","tonsilitis","GORD"]
    },
        {
        "id": "symptom-words",
        "label": "Symptom",
        "patterns": ["fever","headache"]
    },
]

with open("entities.json", "w") as f:
    json.dump(data, f)

entityRuler = EntityRulerInternalApproach()\
    .setInputCols(["document", "token"])\
    .setOutputCol("entities")\
    .setPatternsResource("entities.json")\
    .setCaseSensitive(False)\

text = """John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis, ibuprofen for his inflammation, and lansoprazole for his GORD on 2023-12-01."""
```

*Result*:

|          chunk|begin|end|  label|
|---------------|-----|---|-------|
|        aspirin|   25| 31|   Drug|
|heart condition|   41| 55|Disease|
|    paracetamol|   69| 79|   Drug|
|          fever|   89| 93|Symptom|
|       headache|   99|106|Symptom|
|     tonsilitis|  129|138|Disease|
|      ibuprofen|  141|149|   Drug|
|    lansoprazol|  177|187|   Drug|
|           GORD|  198|201|Disease|


Please check [Rule Based Entity Matchers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb) for more information.


</div><div class="h3-box" markdown="1">

#### Deidentification now Supports Masking and Obfuscation at the Same Time without an Additional Stage

Explore how metadata masking is implemented in deidentification processes through the setMetadataMaskingPolicy function. This feature enables users to add a mask option to DEID within the metadata, providing enhanced data privacy measures. Options such as `entity_labels`, `same_length_chars`, and `fixed_length_chars` offer flexibility in choosing the desired masking policy. 

*Example*:

```python
deidentification = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deid") \
    .setMode("obfuscate") \
    .setObfuscateDate(True) \
    .setObfuscateRefSource('faker') \
    .setMetadataMaskingPolicy("entity_labels") # Options : 'entity_labels', 'same_length_chars', 'fixed_length_chars'

text = """Record date : 2093-01-13 , David Hale , M.D . , Name : Hendrickson Ora , MR # 7194334 Date : 01/13/93 . PCP : Oliveira , 25 years-old , Record date : 2079-11-09 . Cocke County Baptist Hospital , 0295 Keats Street , Phone 55-555-5555 ."""
```

*Result*:

|    | sentence  | deidentified    | masked  |
|---:|:----------|:----------------|:--------------|
|  0 | Record date : 2093-01-13 , David Hale , M.D . | Record date : 2093-02-12 , Docia Chuck , M.D . |  Record date : \<DATE> , \<DOCTOR> , M.D .  |
|  1 | , Name : Hendrickson , Ora MR # 7194334 Date : 01/13/93 . | , Name : Marisue Humble MR # 7185162 Date : 02/12/93 . | , Name : \<PATIENT> MR # \<MEDICALRECORD> Date : \<DATE> . |
|  2 | Patient : Oliveira, 25 years-old , Record date : 2079-11-09 . | Patient : Consuella Lose, 35 years-old , Record date : 2079-12-09 . | Patient : \<PATIENT>, \<AGE> years-old , Record date : \<DATE> . |
|  3 | Cocke County Baptist Hospital .                               | SHELBY REGIONAL MEDICAL CENTER .     | \<HOSPITAL> .  |
|  4 | 0295 Keats Street                                             | 600 North Sioux Point Road           | \<STREET>  |


Please check [Clinical DeIdentification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.Clinical_DeIdentification.ipynb) for more information.


</div><div class="h3-box" markdown="1">

#### `ChunkMerger` now Supports Dictionary Format for the Selective Merging

ChunkMergeModel and ChunkMergeApproach now offer support for the Dictionary format, enhancing its selectiveness and flexibility in chunk merging operations. 
The `ChunkMergeModel` includes `setReplaceDict` for replacing entity labels and `setFalsePositives` for enabling precise control over chunk merging outcomes. 
Additionally, the `ChunkMergeApproach` has `setEntitiesConfidence`, allowing users to adjust entity confidence levels for further customization. 
These enhancements empower users to optimize their data processing pipelines, improving accuracy and efficiency in chunk merging tasks.

*Example*:

```python

chunk_merge_model = ChunkMergeModel() \
    .setInputCols("clinical_ner_chunk","deid_ner_chunk") \
    .setOutputCol("merged_chunk") \
    .setReplaceDict({"DOCTOR": "NAME",
                     "PATIENT": "NAME"}) \
    .setFalsePositives([["metformin", "TREATMENT", "DRUG"],
                        ["glipizide","TREATMENT",""]])

text ='''
Jennifer is 58 years old. She was  seen by Dr. John Green and discharged on metformin, glipizide for T2DM and atorvastatin and gemfibrozil for HTG.
'''
```

*Result for without rules*:

|       chunk|begin|end|   entity|confidence|
|------------|-----|---|---------|----------|
|    Jennifer|    1|  8|  PATIENT|    0.9993|
|          58|   13| 14|      AGE|       1.0|
|  John Green|   48| 57|   DOCTOR|    0.7381|
|   metformin|   77| 85|TREATMENT|    0.9999|
|   glipizide|   88| 96|TREATMENT|       1.0|
|        T2DM|  102|105|  PROBLEM|    0.9988|
|atorvastatin|  111|122|TREATMENT|    0.9999|
| gemfibrozil|  128|138|TREATMENT|       1.0|
|         HTG|  144|146|  PROBLEM|    0.9991|

*Result for with rules*:

In the example, "metformin" has been classified as a DRUG entity, while "glipizide" has been removed due to the setFalsePositives rules.
Additionally, "Jennifer" and "John Green" chunks have been labeled as NAME according to the setReplaceDict rules.


|       chunk|begin|end|   entity|confidence|
|------------|-----|---|---------|----------|
|    Jennifer|    1|  8|     NAME|    0.9993|
|          58|   13| 14|      AGE|       1.0|
|  John Green|   48| 57|     NAME|    0.7381|
|   metformin|   77| 85|     DRUG|    0.9999|
|        T2DM|  102|105|  PROBLEM|    0.9988|
|atorvastatin|  111|122|TREATMENT|    0.9999|
| gemfibrozil|  128|138|TREATMENT|       1.0|
|         HTG|  144|146|  PROBLEM|    0.9991|


</div><div class="h3-box" markdown="1">

#### `MedicalQuestionAnswering` Returns Score in Metadata

Our Medical Question Answering system now includes a significant enhancement: the ability to return a score in metadata. This update provides users with valuable additional information, allowing them to gauge the relevance of the provided answers. 

*Example*:

```python
med_qa  = MedicalQuestionAnswering().pretrained("clinical_notes_qa_base_onnx", "en", "clinical/models")\
              .setInputCols(["document_question", "document_context"])\
              .setCustomPrompt("Context: {context} \n Question: {question} \n Answer: ")\
              .setOutputCol("answer")\

context = '''
Patient with a past medical history of hypertension for 15 years.
(Medical Transcription Sample Report)\nHISTORY OF PRESENT ILLNESS:
The patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril.
'''

question = "What is the primary issue reported by patient?"   
```

*Result*:


|Question           |Answer                         |metadata               |
|-------------------|-------------------------------|-----------------------|
|What is the primary issue reported by patient?|The primary issue reported by the patient is hypertension.|{score -> 0.97722054}|



</div><div class="h3-box" markdown="1">

#### New Speed Benchmarks for Various Pipelines Across Different Platforms Under Various Settings (EMR, Databricks etc.)


- Performance Evaluation of AWS EMR Cluster for Clinical Text Analysis

This study presents a benchmark assessment of an AWS EMR (Elastic MapReduce) cluster for analyzing clinical texts. 
The evaluation aims to assess the performance and scalability of the AWS EMR cluster configuration for clinical text analysis tasks.

**Dataset:** 340 Custom Clinical Texts, approx. 235 tokens per text
**Versions:**
    - **EMR Version:** ERM.6.15.0
    - **spark-nlp Version:** v5.2.2
    - **spark-nlp-jsl Version :** v5.2.1
    - **Spark Version :** v3.4.1
**Instance Type:** 
    -  **Primary**: m4.4xlarge, 16 vCore, 64 GiB memory
    - **Worker :**  m4.4xlarge, 16 vCore, 64 GiB memory


```python
ner_pipeline = Pipeline(stages = [
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_jsl,
        ner_jsl_converter])


resolver_pipeline = Pipeline(stages = [
        document_assembler,
        sentence_detector,
        tokenizer,
        word_embeddings,
        ner_jsl,
        ner_jsl_converter,
        chunk2doc,
        sbert_embeddings,
        snomed_resolver]) 
```

***Results Table***

| partition | NER Timing     |NER and Resolver Timing| 
| ---------:|:-------------- |:----------------------| 
|4          |  24.7 seconds  |1 minutes 8.5  seconds|
|8          |  23.6 seconds  |1 minutes 7.4  seconds|
|16         |  22.6 seconds  |1 minutes 6.9  seconds|
|32         |  23.2 seconds  |1 minutes 5.7  seconds|
|64         |  22.8 seconds  |1 minutes 6.7  seconds|
|128        |  23.7 seconds  |1 minutes 7.4  seconds|
|256        |  23.9 seconds  |1 minutes 6.1  seconds|
|512        |  23.8 seconds  |1 minutes 8.4  seconds|
|1024       |  25.9 seconds  |1 minutes 10.2 seconds|



- Performance Evaluation of ONNX and Base Embeddings in Resolver Benchmark

This study presents a benchmark evaluation of resolver performance using ONNX and base embeddings on clinical text datasets.
The evaluation aims to assess the performance and efficiency of the resolver component under these different embedding configurations.

**Dataset:** 100 Custom Clinical Texts, approx. 595 tokens per text
**Versions:**
    - **spark-nlp Version:** v5.2.2
    - **spark-nlp-jsl Version :** v5.2.1
    - **Spark Version :** v3.2.1
**Instance Type:** 
    -  8 CPU Cores 52GiB RAM (Colab Pro - High RAM)


```python
nlp_pipeline = Pipeline(
    stages = [
        document_assembler,
        sentenceDetectorDL,
        tokenizer,
        word_embeddings,
        clinical_ner,
        ner_converter,
  ])

embedding_pipeline = PipelineModel(
    stages = [
        c2doc,
        sbiobert_embeddings # base or onnx version
  ])

resolver_pipeline = PipelineModel(
    stages = [
        rxnorm_resolver
  ])
```

***Results Table***

|partition|preprocessing|embeddings| resolver    |onnx_embeddings|resolver_with_onnx_embeddings|
|--------:|------------:|---------:|------------:|--------------:|------------:|
| 4       |      25 sec | 25 sec   |7 min 46 sec |   9 sec       |8 min 29 sec |
| 8       |      21 sec | 25 sec   |5 min 12 sec |   9 sec       |4 min 53 sec |
| 16      |      21 sec | 25 sec   |4 min 41 sec |   9 sec       |4 min 30 sec |
| 32      |      20 sec | 24 sec   |5 min 4 sec  |   9 sec       |4 min 34 sec |
| 64      |      21 sec | 24 sec   |4 min 44 sec |   9 sec       |5 min 2 sec  |
| 128     |      20 sec | 25 sec   |5 min 4 sec  |   10 sec      |4 min 51 sec |
| 256     |      22 sec | 26 sec   |4 min 34 sec |   10 sec      |5 min 13 sec |
| 512     |      24 sec | 27 sec   |4 min 46 sec |   12 sec      |4 min 22 sec |
| 1024    |      29 sec | 30 sec   |4 min 24 sec |   14 sec      |4 min 29 sec |


Please check [Speed Benchmarks](https://nlp.johnsnowlabs.com/docs/en/benchmark) for more information.

</div><div class="h3-box" markdown="1">




#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Consistent obfuscation is supported in `StructuredDeidentification` too 
- Added `deid_source` field to the metadata to infer the source of entity chunks coming from internal or external NER models and stages
- Refactoring the Deidentification module for improved functionality 
- Flushing the temporary files dumped by the `SentenceEntityResolver` 
- Fixed `IOBTagger` was returning zero instead of 'O'
- Lighter jars for Spark NLP leading optimized Spark's sessions 
- `Resolution2Chunk` documentation updated
- Updated the default value of the `customBoundsStrategy` parameter in the `InternalDocumentSplitter`
- Enhanced `InternalDocumentSplitter` with UUID Metadata Field


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Flattener Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/41.Flattener.ipynb)
- New [Rule Based Entity Matchers Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/40.Rule_Based_Entity_Matchers.ipynb)
- New [Opioid Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/42.Opioid_Models.ipynb)
- Updated [Clinical Deidentification Improvement Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/4.4.Clinical_Deidentification_Improvement.ipynb) for latest models
- New [Opioid Demo](https://demo.johnsnowlabs.com/healthcare/OPIOID/)
- New [Biomarker Classification Demo](https://demo.johnsnowlabs.com/healthcare/CLASSIFICATION_BIOMARKER/)
- New [SNOMED Term NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_SNOMED_TERM/) 
- New [Multi Language NER Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEID_MULTI/)
- Updated [Age Classification Demo](https://demo.johnsnowlabs.com/healthcare/PUBLIC_HEALTH_AGE/) with new `genericclassifier_age_e5` model


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `drug_matcher`
+ `biomarker_matcher`
+ `umls_loinc_mapper`
+ `umls_cpt_mapper`
+ `umls_snomed_mapper`
+ `snomed_umls_mapper`
+ `cpt_umls_mapper`
+ `loinc_umls_mapper`
+ `ner_opioid`
+ `ner_snomed_term`
+ `ner_deid_multilingual`
+ `ner_deid_name_multilingual_clinical`
+ `assertion_opioid_wip`
+ `assertion_opioid_drug_status_wip`
+ `assertion_opioid_general_symptoms_status_wip`
+ `genericclassifier_age_e5`
+ `bert_sequence_classifier_biomarker`
+ `ncit_resolver_pipeline`
+ `rxcui_resolver_pipeline`
+ `hgnc_resolver_pipeline`
+ `hcpcs_resolver_pipeline`
+ `snomed_procedures_measurements_resolver_pipeline`
+ `icdo_resolver_pipeline`
+ `icd10pcs_resolver_pipeline`
+ `icd10cm_generalised_resolver_pipeline`
+ `loinc_resolver_pipeline`
+ `loinc_numeric_resolver_pipeline`
+ `medication_resolver_pipeline`
+ `medication_resolver_transform_pipeline`
+ `clinical_deidentification_obfuscation_medium`
+ `clinical_deidentification_obfuscation_small`
+ `clinical_deidentification`
+ `clinical_deidentification_generic`
+ `clinical_deidentification_subentity`
+ `sbiobertresolve_snomed_bodyStructure`
+ `sbiobertresolve_snomed_drug`
+ `sbiobertresolve_snomed_conditions`
+ `sbiobertresolve_snomed_auxConcepts`
+ `sbiobertresolve_snomed_findings`
+ `sbiobertresolve_snomed_findings_aux_concepts`
+ `sbiobertresolve_snomed_procedures_measurements`





</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
