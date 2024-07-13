---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.3.3
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_3_3
key: docs-licensed-release-notes
modify_date: 2024-05-21
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.3.3

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with a brand new PipelineTracer module to return structured jsons from pretrained pipelines, brand new hyperparameters to customize relation extraction models and Deidentification process, and 22 new clinical pretrained models and pipelines**. 

+ Introducing 7 new Sentence Entity Resolver Models for entity mapping to medical terminologies, using SOTA `BioLord` sentence embeddings
+ Clinical document analysis with one-liner pretrained pipelines for specific clinical tasks and concepts
+ Introducing 2 new Chunk Mapper models designed for medical code mapping between `SNOMED` and `MedDRA` terminologies
+ Improved version of Social Determinants of Health (SDoH) named entity recognition model with reduced set of core entities
+ Automating pipeline tracing and analysis with `PipelineTracer`  to help return structured jsons from pretrained pipelines via the `OuputParser` module
+ Configuring age-based obfuscation with the `setAgeGroups` parameter
+ Enhancing date obfuscation control with the `setKeepYear` parameter in the `Deidentification` annotator to allow `year` info intact
+ Broadening relation extraction with extended scope windows, `directionSensitive` and `filterByTokenDistance` parameters to allow further customization and reduce FPs
+ Enhancing rule-based annotators with the `ner_source` field for improved chunk tracking and prioritization
+ Introduction of a new parameter `dataSetInfo` to store dataset details for `AssertionDL` and `GenericClassifier` for traceability
+ Converting visual NER annotations to CoNLL format for training text-based NER models with visual annotations
+ Performance analysis of deidentification pipelines on clinical texts in a cluster environment
+ New blogposts on relation extraction, MedDRA response to treatment, and pretrained pipelines.
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Added training params to trainable annotators within the metadata of the trained models
    - Updated Risk Adjustment module with V28Y24
    - Resolved index issue in `AssertionChunkConverter` annotator and `AnnotationLab.get_assertion_data` modules
    - Resolved saving issue in `Flattener` annotator
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [PipelineTracer and PipelineOutputParser Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb)
    - Updated [Task Based Clinical Pretrained Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb)
    - Updated [Pretrained Clinical Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.Pretrained_Clinical_Pipelines.ipynb)
    - Updated [ADE Demo](https://demo.johnsnowlabs.com/healthcare/ADE/)
    - Updated [NER_POSOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/NER_POSOLOGY/)
    - Updated [NER_RADIOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/NER_RADIOLOGY/)
    - Updated [VOP Demo](https://demo.johnsnowlabs.com/healthcare/VOP/)
    - Updated [SDOH Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/)
    - Updated [ONCOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/)
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.

</div><div class="h3-box" markdown="1">


####  Introducing 7 New Sentence Entity Resolver Models for Entity Mapping to Medical Terminologies, Using SOTA `BioLord` Sentence Embeddings

The latest lineup of 7 cutting-edge resolver models are designed to enhance clinical entity mapping and coding accuracy. These models leverage advanced natural language processing to seamlessly map medical entities and concepts to standardized codes, facilitating streamlined data analysis and healthcare decision-making. Each model specializes in precise code assignment within specific medical domains, from drug ingredients to veterinary-related entities. Dive into our resolver models and empower your applications with state-of-the-art clinical entity resolution.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`sbiobertresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2024/05/06/biolordresolve_umls_general_concepts_en.html) | This model maps clinical entities and concepts to the following 4 UMLS CUI code categories |
| [`biolordresolve_umls_general_concepts`](https://nlp.johnsnowlabs.com/2024/05/06/biolordresolve_umls_general_concepts_en.html) | This model maps clinical entities and concepts to the following 4 UMLS CUI code categories |
| [`biolordresolve_icd10cm_augmented_billable_hcc`](https://nlp.johnsnowlabs.com/2024/05/06/biolordresolve_icd10cm_augmented_billable_hcc_en.html) | This model maps extracted medical entities to ICD-10-CM codes |
| [`biolordresolve_avg_rxnorm_augmented`](https://nlp.johnsnowlabs.com/2024/05/07/biolordresolve_avg_rxnorm_augmented_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes |
| [`biolordresolve_snomed_findings_aux_concepts`](https://nlp.johnsnowlabs.com/2024/05/07/biolordresolve_snomed_findings_aux_concepts_en.html) | This model maps clinical entities and concepts to SNOMED codes |
| [`biolordresolve_cpt_procedures_measurements_augmented`](https://nlp.johnsnowlabs.com/2024/05/08/biolordresolve_cpt_procedures_measurements_augmented_en.html) | This model maps medical entities to CPT codes |
| [`sbiobertresolve_snomed_veterinary_wip`](https://nlp.johnsnowlabs.com/2024/05/06/sbiobertresolve_snomed_veterinary_wip_en.html) | TThis model maps veterinary-related entities and concepts to SNOMED codes |


*Example*:

```python
icd10cm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_icd10cm_augmented_billable_hcc", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("icd10_code")\
    .setDistanceFunction("EUCLIDEAN")

text = "John Doe, a 49-year-old male with CMT2P, AIDS-causing virus infection, and PKD2, presents for a follow-up visit to manage his chronic conditions."
```

*Result*:

{:.table-model-big}
|chunk|sbiobert icd10cm code|sbiobert icd10cm resolution|biolord icd10cm code|biolord icd10cm resolution|
|-|-|-|-|-|
|CMT2P|G12.1|sma2 [other inherited spinal muscular atrophy]|G60.0|cmt2p - charcot-marie-tooth disease type 2p [hereditary motor and sensory neuropathy]|
|AIDS-causing virus infection|B34.9|disease caused by virus [viral infection, unspecified]|B20|hiv - human immunodeficiency virus infection [human immunodeficiency virus [hiv] disease]|
|PKD2|C77.9|pn2 category [secondary and unspecified malignant neoplasm of lymph node, unspecified]|Q61.2|pkd2 - polycystic kidney disease 2 [polycystic kidney, adult type]|



</div><div class="h3-box" markdown="1">

####  Clinical Document Analysis with One-Liner Pretrained Pipelines for Specific Clinical Tasks and Concepts

We introduce a suite of advanced, hybrid pretrained pipelines, specifically designed to streamline the clinical document analysis process. These pipelines are built upon multiple state-of-the-art (SOTA) pretrained models, delivering a comprehensive solution for quickly extracting vital information.

What sets this release apart is the elimination of complexities typically involved in building and chaining models. Users no longer need to navigate the intricacies of constructing intricate pipelines from scratch or the uncertainty of selecting the most effective model combinations. Our new pretrained pipelines simplify these processes, offering a seamless, user-friendly experience.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`explain_clinical_doc_sdoh`](https://nlp.johnsnowlabs.com/2024/05/01/explain_clinical_doc_sdoh_en.html) | This pipeline is designed to extract all clinical/medical entities, assertion status, and relation informations which may be considered as Social Determinants of Health (SDOH) entities from text. |
| [`explain_clinical_doc_mental_health`](https://nlp.johnsnowlabs.com/2024/05/06/explain_clinical_doc_mental_health_en.html) | This pipeline is designed to extract all mental health-related entities, assertion status, and relation information from text. |
| [`ner_medication_generic_pipeline`](https://nlp.johnsnowlabs.com/2024/04/25/ner_medication_generic_pipeline_en.html) | This pre-trained pipeline is designed to identify generic `DRUG` entities in clinical texts. It was built on top of the `ner_posology_greedy`, `ner_jsl_greedy`, `ner_drugs_large`, and `drug_matcher` models to detect the entities `DRUG`, `DOSAGE`, `ROUTE`, and `STRENGTH` chunking them into a larger entity as `DRUG` when they appear together. |
| [`ner_deid_generic_context_augmented_pipeline`](https://nlp.johnsnowlabs.com/2024/05/20/ner_deid_generic_context_augmented_pipeline_en.html) | This pipeline can be used to extract PHI information such as `AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`,  `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PHONE`, `EMAIL`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities. |
| [`ner_deid_subentity_context_augmented_pipeline`](https://nlp.johnsnowlabs.com/2024/05/20/ner_deid_subentity_context_augmented_pipeline_en.html) | This pipeline can be used to extract PHI information such as `AGE`, `CONTACT`, `DATE`, `LOCATION-OTHE`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `EMAIL`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities. |
| [`ner_deid_context_augmented_pipeline`](https://nlp.johnsnowlabs.com/2024/05/20/ner_deid_subentity_context_augmented_pipeline_en.html) | This pipeline can be used to extract PHI information such as `AGE`, `CONTACT`, `DATE`, `LOCATION`, `NAME`, `PROFESSION`, `CITY`, `COUNTRY`, `DOCTOR`, `HOSPITAL`, `IDNUM`, `MEDICALRECORD`, `ORGANIZATION`, `PATIENT`, `PHONE`, `EMAIL`, `STREET`, `USERNAME`, `ZIP`, `ACCOUNT`, `LICENSE`, `VIN`, `SSN`, `DLN`, `PLATE`, `IPADDR` entities. |


*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

pipeline_sdoh = PretrainedPipeline("explain_clinical_doc_sdoh", "en", "clinical/models")

text = """The patient reported experiencing symptoms of anxiety and depression, which have been affecting his quality of life. 
He reported a history of childhood trauma related to violence and abuse in his household, which has contributed to his smoking, alcohol use and current mental health struggles."""

```

*NER and Assertion Result*:

{:.table-model-big}
| chunks          |begin |end | entities         | assertion|
|:----------------|-----:|---:|:-----------------|:---------|
| anxiety         |   46 | 52 | Mental_Health    | Present  |
| depression      |   58 | 67 | Mental_Health    | Present  |
| childhood trauma|  143 |158 | Childhood_Event  | Past     |
| violence        |  171 |178 | Violence_Or_Abuse| Past     |
| abuse           |  184 |188 | Violence_Or_Abuse| Past     |
| smoking         |  237 |243 | Smoking          | Present  |
| alcohol         |  246 |252 | Alcohol          | Present  |


*Relation Extraction Result*:

{:.table-model-big}
| relation type                     | entity1           | chunk1           | entity2           | chunk2          | confidence|
|:----------------------------------|:------------------|:-----------------|:------------------|:----------------|:----------|
| Mental_Health-Quality_Of_Life     | Mental_Health     | anxiety          | Quality_Of_Life   | quality of life |      0.98 |
| Mental_Health-Quality_Of_Life     | Mental_Health     | depression       | Quality_Of_Life   | quality of life |      0.95 |
| Childhood_Event-Violence_Or_Abuse | Childhood_Event   | childhood trauma | Violence_Or_Abuse | violence        |      0.96 |
| Childhood_Event-Violence_Or_Abuse | Childhood_Event   | childhood trauma | Violence_Or_Abuse | abuse           |      0.97 |
| Childhood_Event-Alcohol           | Childhood_Event   | childhood trauma | Alcohol           | alcohol         |      1.00 |
| Violence_Or_Abuse-Alcohol         | Violence_Or_Abuse | violence         | Alcohol           | alcohol         |      0.99 |
| Violence_Or_Abuse-Alcohol         | Violence_Or_Abuse | abuse            | Alcohol           | alcohol         |      0.93 |


Please check the [Task Based Clinical Pretrained Pipelines](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb) model for more information

</div><div class="h3-box" markdown="1">
    
#### Introducing 2 new Chunk Mapper models designed for medical code mapping between `SNOMED` and `MedDRA` terminologies.

Introducing a suite of new ChunkMapper models designed to streamline medical code mapping tasks. These models include mappings between MedDRA and SNOMED codes, offering a comprehensive solution for interoperability within medical systems.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
|[`meddra_llt_snomed_mapper`](https://nlp.johnsnowlabs.com/2024/05/14/meddra_llt_snomed_mapper_en.html)  | This pretrained model maps MedDRA LLT (Lowest Level Term) codes to corresponding SNOMED codes. |
|[`snomed_meddra_llt_mapper`](https://nlp.johnsnowlabs.com/2024/05/14/snomed_meddra_llt_mapper_en.html)  | This pretrained model maps SNOMED codes to corresponding MedDRA LLT (Lowest Level Term) codes. |

*Example*:

```python
chunkMapper = ChunkMapperModel.load('meddra_llt_snomed_mapper')\
    .setInputCols(["meddra_llt_code2chunk"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

text = ["Chronic renal insufficiency", "Gastritis", "Transient ischemic attack"]
```

*Result*:

{:.table-model-big}
|                      chunk|meddra_code|                                     snomed_code|
|---------------------------|-----------|------------------------------------------------|
|Chronic renal insufficiency|   10050441|723190009:Chronic renal insufficiency (disorder)|
|                  Gastritis|   10017853|                    4556007:Gastritis (disorder)|
|  Transient ischemic attack|   10072760|  266257000:Transient ischemic attack (disorder)|


</div><div class="h3-box" markdown="1">


####  Improved Version of Social Determinants of Health (SDoH) Named Entity Recognition Model with Reduced Set of Core Entities


We are introducing our new Social Determinants of Health (SDoH) Named Entity Recognition model that has been specifically designed to identify and extract entities related to various social determinants of health. This new model is an improvement over our previous version, aimed at better understanding and tracking the impacts of social factors on health.

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_sdoh_core", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = [["""Smith is 55 years old, living in New York, a divorced Mexcian American woman with financial problems. She speaks Spanish and Portuguese. She lives in an apartment. She has been struggling with diabetes for the past 10 years and has recently been experiencing frequent hospitalizations due to uncontrolled blood sugar levels. Smith works as a cleaning assistant and cannot access health insurance or paid sick leave. She has a son, a student at college. Pt with likely long-standing depression. She is aware she needs rehab. Pt reports having her catholic faith as a means of support as well.  She has a long history of etoh abuse, beginning in her teens. She reports she has been a daily drinker for 30 years, most recently drinking beer daily. She smokes a pack of cigarettes a day. She had DUI in April and was due to court this week."""]]
```

*Result*:

{:.table-model-big}
|chunk                  |begin|end|label              |
|-----------------------|-----|---|-------------------|
|New York               |33   |40 |Geographic_Entity  |
|financial problems     |82   |99 |Financial_Status   |
|apartment              |153  |161|Housing            |
|hospitalizations       |268  |283|Other_SDoH_Keywords|
|access health insurance|372  |394|Insurance_Status   |
|son                    |426  |428|Family_Member      |
|student                |433  |439|Education          |
|college                |444  |450|Education          |
|depression             |482  |491|Mental_Health      |
|rehab                  |517  |521|Access_To_Care     |
|catholic faith         |546  |559|Spiritual_Beliefs  |
|support                |575  |581|Social_Support     |
|daily                  |682  |686|Substance_Frequency|
|30 years               |700  |707|Substance_Duration |
|daily                  |738  |742|Substance_Frequency|
|a pack                 |756  |761|Substance_Quantity |
|a day                  |777  |781|Substance_Frequency|
|DUI                    |792  |794|Legal_Issues       |

Please check the [model card](https://nlp.johnsnowlabs.com/2024/04/08/ner_sdoh_core_en.html) and [SDOH Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/)


####  Automating Pipeline Tracing and Analysis with `PipelineTracer` to Help Return Structured JSONs from Pretrained Pipelines Via the `PipelineOuputParser` module

`PipelineTracer` is a versatile class designed to trace and analyze the stages of a pipeline, offering in-depth insights into entities, assertions, deidentification, classification, and relationships. It also facilitates the creation of parser dictionaries for building a `PipelineOutputParser`. Key functions include printing the pipeline schema, creating parser dictionaries, and retrieving possible assertions, relations, and entities. Also, provide direct access to parser dictionaries and available pipeline schemas

Please check the [PipelineTracer and PipelineOutputParser](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb) notebook for more information


*PipelineTracer Example*:

```python
from sparknlp.pretrained import PretrainedPipeline
from sparknlp_jsl.pipeline_tracer import PipelineTracer

oncology_pipeline = PretrainedPipeline("explain_clinical_doc_oncology", "en", "clinical/models")

pipeline_tracer = PipelineTracer(oncology_pipeline)

column_maps = pipeline_tracer.createParserDictionary()
column_maps.update({"document_identifier": "explain_clinical_doc_oncology"})
print(column_maps)
```

*column_maps Result*:

```python
{
    'document_identifier': 'explain_clinical_doc_oncology',
    'document_text': 'document',
    'entities': [
        {
            'ner_chunk_column_name': 'merged_chunk',
            'assertion_column_name': '',
            'resolver_column_name': ''
        },
        {
            'ner_chunk_column_name': 'merged_chunk_for_assertion',
            'assertion_column_name': 'assertion',
            'resolver_column_name': ''
        }
    ],
    'relations': ['all_relations'],
    'summaries': [],
    'deidentifications': [],
    'classifications': []
 }
```

*PipelineOutputParser Example*:

```python
text = """The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, which showed a complex ovarian mass. A Pap smear performed one month later was positive for atypical glandular cells suspicious for adenocarcinoma. The pathologic specimen showed extension of the tumor throughout the fallopian tubes, appendix, omentum, and 5 out of 5 enlarged lymph nodes. The final pathologic diagnosis of the tumor was stage IIIC papillary serous ovarian adenocarcinoma. Two months later, the patient was diagnosed with lung metastases.Neoadjuvant chemotherapy with the regimens of Cyclophosphamide (500 mg/m2) is being given for 6 cycles with poor response"""

results = oncology_pipeline.fullAnnotate()

from sparknlp_jsl.pipeline_output_parser import PipelineOutputParser

pipeline_parser = PipelineOutputParser(column_maps)
result = pipeline_parser.run(results)
```

*PipelineOutputParser Result*:

```python
{
    'result': [
        {
            'document_identifier': 'explain_clinical_doc_oncology',
            'document_text': ['The Patient underwent a computed tomography (CT) scan of the abdomen and pelvis, ....'],
            'entities': [
                [{'chunk_id': '0',
                'begin': 24,
                'end': 42,
                'chunk': 'computed tomography',
                'label': 'Imaging_Test',
                'assertion': None,
                'term_code': None},
                {'chunk_id': '1',
                'begin': 45,
                'end': 46,
                'chunk': 'CT',
                'label': 'Imaging_Test',
                'assertion': None,
                'term_code': None},
                ...
                ],
                [{'chunk_id': '0',
                'begin': 24,
                'end': 42,
                'chunk': 'computed tomography',
                'label': 'Imaging_Test',
                'assertion': 'Past',
                'term_code': None},
                {'chunk_id': '1',
                'begin': 45,
                'end': 46,
                'chunk': 'CT',
                'label': 'Imaging_Test',
                'assertion': 'Past',
                'term_code': None}]
            ],
            'relations': [
                [{'relation': 'is_location_of',
                'entity1': 'Site_Other_Body_Part',
                'entity1_begin': '104',
                'entity1_end': '110',
                'chunk1': 'ovarian',
                'entity2': 'Tumor_Finding',
                'entity2_begin': '112',
                'entity2_end': '115',
                'chunk2': 'mass',
                'confidence': '0.922661'},
                {'relation': 'is_finding_of',
                'entity1': 'Pathology_Test',
                'entity1_begin': '120',
                'entity1_end': '128',
                'chunk1': 'Pap smear',
                'entity2': 'Cancer_Dx',
                'entity2_begin': '213',
                'entity2_end': '226',
                'chunk2': 'adenocarcinoma',
                'confidence': '0.52542114'},
                ...]
            ],
            'summaries': [],
            'deidentifications': [],
            'classifications': []
        }
    ]
}
```

*getParserDictDirectly Example*:

```python
from sparknlp_jsl.pipeline_tracer import PipelineTracer

columns_directly = PipelineTracer.getParserDictDirectly("clinical_deidentification", "en", "clinical/models")

print(columns_directly)
```

*getParserDictDirectly Result*:

```python
{
    'document_identifier': 'clinical_deidentification',
    'document_text': 'sentence',
    'entities': [{
        'ner_chunk_column_name': 'ner_chunk',
        'assertion_column_name': '',
        'resolver_column_name': ''}],
    'relations': [],
    'summaries': [],
    'deidentifications': [{
        'original': 'sentence',
        'obfuscated': 'obfuscated',
        'masked': ''}],
    'classifications': []}

```

</div><div class="h3-box" markdown="1">

####  Configuring Age-based Obfuscation with the `setAgeGroups` Parameter

This method, setAgeGroups, is used in conjunction with the `obfuscateByAgeGroups` parameter to specify age ranges for obfuscation. If the specified `ageGroups` dictionary does not cover all ages, the obfuscation defaults to the `ageRanges` parameter. Each entry in the dictionary includes an age group name paired with a range of two integers: the lower and upper bounds of the age group. By default, the method includes a standard dictionary of age groups in English, but users can customize this dictionary to suit specific age classifications and obfuscation requirements. This method takes a value parameter containing a dictionary mapping age group names to corresponding age ranges for obfuscation.


*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_subentity_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateByAgeGroups(True)\
    .setAgeGroups({"baby": [0, 1],
                   "toddler": [1, 4],
                   "child": [4, 13],
                   "teenager": [13, 20],
                   "adult": [20, 65],
                   "senior": [65, 100] })

text ='''
Name: Joseph Brown, Age: 17, Phone: (9) 7765-5632.
This 17 yrs old male, presented with chest heaviness that started during a pick-up basketball game. 
Mark Smith, aged 55, and his daughter (7) Mary were involved in an accident during their travel.
'''
```

*Result*:

{:.table-model-big}
|sentence|deidentified|
|--------|------------|
|Name: Joseph Brown, Age: 17, Phone: (9) 7765-5632.                                                 |Name: Burnadette Carrion, Age: teenager, Phone: (6) 9846-1747.                                     |
|This 17 yrs old male, presented with chest heaviness that started during a pick-up basketball game.|This teenager male, presented with chest heaviness that started during a pick-up basketball game. |
|Mark Smith, aged 55, and his daughter (7) Mary were involved in an accident during their travel.   |Cleve Dale, adult, and his daughter (child) Mary were involved in an accident during their travel.|


</div><div class="h3-box" markdown="1">


#### Enhancing Date Obfuscation Control with the `setKeepYear` Parameter in `Deidentification` Annotator to Allow `year` Info Intact

The `setKeepYear` parameter to improve date obfuscation controls. This feature allows users to decide whether to retain the year in date entities while obfuscating the month and day. The default setting is False.

- `True`, the year remains unchanged, ensuring consistency in data that relies on year-specific information.
- `False`, the entire date, including the year, will be modified. 

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_subentity_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setObfuscateRefSource("faker") \
    .setKeepYear(True)
```

*.setKeepYear(False) Result*:

{:.table-model-big}
|sentence                                                 |deidentified                                             |
|---------------------------------------------------------|---------------------------------------------------------|
|Hendrickson, Ora, Record date: 2023-01-01, Age: 25 .     |Delle Ferdinand, Record date: 2023-02-10, Age: 35 .      |
|He was admitted to hospital for cystectomy on 12/31/2022.|He was admitted to hospital for cystectomy on 02/09/2023.|

*.setKeepYear(True) Result*:

{:.table-model-big}
|sentence                                                 |deidentified                                             |
|---------------------------------------------------------|---------------------------------------------------------|
|Hendrickson, Ora, Record date: 2023-01-01, Age: 25 .     |Lenord Radon, Record date: 2023-02-07, Age: 31 .         |
|He was admitted to hospital for cystectomy on 12/31/2022.|He was admitted to hospital for cystectomy on 02/06/2022.|

As you can see, `2022` has not been changed.


####  Broadening Relation Extraction with Extended Scope-Windows, `directionSensitive` and `filterByTokenDistance` Parameters to Allow Further Customization and Reduce FPs

-  In RelationRxtraction, scopeWindow expands beyond the immediate tokens of target chunks. By applying a `scopeWindow [X, Y]`, additional `X` tokens to the left and `Y` tokens to the right become crucial for feature generation, enriching contextual information essential for precise embeddings-based feature extraction.

*Example*:

```python
re_model = RelationExtractionModel.pretrained("re_oncology_wip", "en", "clinical/models") \
    .setInputCols(["embeddings", "pos_tags", "ner_chunk", "dependencies"]) \
    .setOutputCol("re_oncology_results") \
    .setScopeWindow([5,5])
```

- The features `directionSensitive` and `filterByTokenDistance` have been implemented. The `directionSensitive` setting determines how entity relations are considered. If set to true, only relations in the form of ENTITY1-ENTITY2 are considered. If set to false, both ENTITY1-ENTITY2 and ENTITY2-ENTITY1 relations are considered. The `filterByTokenDistance` setting is a criterion for filtering based on the number of tokens between entities. The model only identifies relations where the entities are separated by fewer than the specified number of tokens.

*directionSensitive Example*:

```python
re_ner_chunk_filter = RENerChunksFilter() \
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setMaxSyntacticDistance(10)\
    .setDirectionSensitive(True)\
    .setRelationPairs(["test-problem", #"problem-test"
                       "treatment-problem", #"problem-treatment"
                       ])\

redl_model = RelationExtractionDLModel.pretrained("redl_clinical_biobert", "en", "clinical/models")\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations")\
    .setPredictionThreshold(0.5)\
    .setRelationPairsCaseSensitive(False)\


text = ''' She was treated with a five-day course of amoxicillin for a respiratory tract infection.
She was on metformin, glipizide, and dapagliflozin for T2DM and additionally atorvastatin and gemfibrozil for HTG.
However, serum chemistry obtained six hours after presentation revealed the anion gap was still elevated at 21, serum bicarbonate was 16 mmol/L, and lipase was 52 U/L.
The β-hydroxybutyrate level was found to be elevated at 5.29 mmol/L - the original sample was centrifuged and the chylomicron layer was removed before analysis due to interference from turbidity caused by lipemia again.
'''
```

*directionSensitive Result*:

{:.table-model-big.db}
|sentence |entity1_begin|entity1_end| chunk1                      | entity1   |entity2_begin |entity2_end | chunk2                        | entity2| relation|confidence |
|--------:|-------------|-----------|:----------------------------|:----------|-------------:|-----------:|:------------------------------|:-------|:--------|----------:|
|       0 |           43|         53| amoxicillin                 | TREATMENT |           59 |         87 | a respiratory tract infection | PROBLEM| Treatment_Administered_Problem |  0.998835 |
|       1 |          101|        109| metformin                   | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem |  0.995263 |
|       1 |          101|        109| metformin                   | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem |  0.749655 |
|       1 |          112|        120| glipizide                   | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem |  0.993901 |
|       1 |          112|        120| glipizide                   | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem |  0.839519 |
|       1 |          127|        139| dapagliflozin               | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem |  0.99619  |
|       1 |          127|        139| dapagliflozin               | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem |  0.984917 |
|       1 |          167|        178| atorvastatin                | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem |  0.935767 |
|       1 |          184|        194| gemfibrozil                 | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem |  0.983878 |
|       2 |          214|        228| serum chemistry             | TEST      |          295 |        308 | still elevated                | PROBLEM| Test_Revealed_Problem      |  0.997158 |
|       2 |          277|        289| the anion gap               | TEST      |          295 |        308 | still elevated                | PROBLEM| Test_Revealed_Problem      |  0.989831 |
|       3 |          373|        399| The β-hydroxybutyrate level | TEST      |          417 |        424 | elevated                      | PROBLEM| Test_Revealed_Problem      |  0.996874 |
|       3 |          373|        399| The β-hydroxybutyrate level | TEST      |          540 |        551 | interference                  | PROBLEM| Test_Revealed_Problem      |  0.964988 |
|       3 |          373|        399| The β-hydroxybutyrate level | TEST      |          558 |        566 | turbidity                     | PROBLEM| Test_Revealed_Problem      |  0.972585 |
|       3 |          373|        399| The β-hydroxybutyrate level | TEST      |          578 |        584 | lipemia                       | PROBLEM| Test_Revealed_Problem      |  0.976935 |
|       3 |          524|        531| analysis                    | TEST      |          558 |        566 | turbidity                     | PROBLEM| Test_Performed_Problem     |  0.537359 |
|       3 |          524|        531| analysis                    | TEST      |          578 |        584 | lipemia                       | PROBLEM| Test_Performed_Problem     |  0.850083 |



*filterByTokenDistance Example*:

```python
re_ner_chunk_filter = RENerChunksFilter() \
    .setInputCols(["ner_chunk", "dependencies"])\
    .setOutputCol("re_ner_chunk")\
    .setMaxSyntacticDistance(10)\
    .setDirectionSensitive(True)\
    .setRelationPairs(["test-problem", #"problem-test"
                       "treatment-problem", #"problem-treatment"
                       ])\
    .setFilterByTokenDistance(4)

redl_model = RelationExtractionDLModel.pretrained("redl_clinical_biobert", "en", "clinical/models")\
    .setInputCols(["re_ner_chunk", "sentence"])\
    .setOutputCol("relations")\
    .setPredictionThreshold(0.5)\
    .setRelationPairsCaseSensitive(False)\

text = ''' She was treated with a five-day course of amoxicillin for a respiratory tract infection.
She was on metformin, glipizide, and dapagliflozin for T2DM and additionally atorvastatin and gemfibrozil for HTG.
However, serum chemistry obtained six hours after presentation revealed the anion gap was still elevated at 21, serum bicarbonate was 16 mmol/L, and lipase was 52 U/L.
The β-hydroxybutyrate level was found to be elevated at 5.29 mmol/L - the original sample was centrifuged and the chylomicron layer was removed before analysis due to interference from turbidity caused by lipemia again.
'''

```

*filterByTokenDistance Result*:

{:.table-model-big.db}
|sentence|entity1_begin |entity1_end | chunk1                      | entity1   |entity2_begin |entity2_end | chunk2                        | entity2| relation|confidence|
|-------:|-------------:|-----------:|:----------------------------|:----------|-------------:|-----------:|:------------------------------|:-------|:--------|------:|
|       0|           43 |         53 | amoxicillin                 | TREATMENT |           59 |         87 | a respiratory tract infection | PROBLEM| Treatment_Administered_Problem    |  0.99 |
|       1|          101 |        109 | metformin                   | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem    |  0.99 |
|       1|          112 |        120 | glipizide                   | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem    |  0.99 |
|       1|          127 |        139 | dapagliflozin               | TREATMENT |          145 |        148 | T2DM                          | PROBLEM| Treatment_Administered_Problem    |  0.99 |
|       1|          167 |        178 | atorvastatin                | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem    |  0.94 |
|       1|          184 |        194 | gemfibrozil                 | TREATMENT |          200 |        202 | HTG                           | PROBLEM| Treatment_Administered_Problem    |  0.98 |
|       2|          277 |        289 | the anion gap               | TEST      |          295 |        308 | still elevated                | PROBLEM| Test_Revealed_Problem    |  0.98 |
|       3|          373 |        399 | The β-hydroxybutyrate level | TEST      |          417 |        424 | elevated                      | PROBLEM| Test_Revealed_Problem    |  0.99 |
|       3|          524 |        531 | analysis                    | TEST      |          558 |        566 | turbidity                     | PROBLEM| Test_Performed_Problem   |  0.54 |
|       3|          524 |        531 | analysis                    | TEST      |          578 |        584 | lipemia                       | PROBLEM| Test_Performed_Problem   |  0.85 |


please see the blogpost [Next-Level Relation Extraction in Healthcare NLP: Introducing New Directional and Contextual Features](https://medium.com/john-snow-labs/next-level-relation-extraction-in-healthcare-nlp-introducing-new-directional-and-contextual-cc54eb68a699)


</div><div class="h3-box" markdown="1">

#### Enhancing Rule-Based Annotators with the `ner_source` Field for Improved Chunk Tracking and Prioritization

Enhancing rule-based annotators such as `ContextualParser`, `TextMatcherInternal`, `RegexMatcherInternal`, and `EntityRulerInternal` with `ner_source` field for improved chunk tracking and prioritization

We have enhanced rule-based annotators, including `ContextualParser`, `TextMatcherInternal`, `RegexMatcherInternal`, and `EntityRulerInternal`, by adding the `ner_source` field. This improvement allows for better chunk tracking and prioritization, enabling clients to trace the origin of chunks effectively. Additionally, with the `ner_source` field, `NerConverterInternal` and `ChunkMergerApproach` can now prioritize chunks using the `.setChunkPrecedence("ner_source")` method, leading to more accurate and efficient entity recognition and handling.

*Example*:

```python
regex_matcher_internal = RegexMatcherInternal()\
    .setInputCols('document')\
    .setStrategy("MATCH_ALL")\
    .setOutputCol("regex_matches")\
    .setExternalRules(path='./rules/regex_rules.txt', delimiter='~')

entityExtractor = TextMatcherInternal()\
    .setInputCols(["document", "token"])\
    .setEntities("matcher_drug.csv")\
    .setOutputCol("matched_text")\
    .setCaseSensitive(False)\
    .setDelimiter("#")\
    .setMergeOverlapping(False)

entityRuler = EntityRulerInternalApproach()\
    .setInputCols(["document", "token"])\
    .setOutputCol("entities")\
    .setPatternsResource("entities.json")\
    .setCaseSensitive(False)\

text = """ Name: John Smith, Record date: 2093-01-13, MR #719435, John's doctor prescribed aspirin for his heart condition, along with paracetamol for his fever and headache, amoxicillin for his tonsilitis."""

```

*Result*:

{:.table-model-big}
| chunk           |   begin |   end | entity   | ner_source    |
|:----------------|--------:|------:|:---------|:--------------|
| 2093-01-13      |      32 |    41 | DATE     | regex_matches |
| aspirin         |      81 |    87 | Drug     | matched_text  |
| heart condition |      97 |   111 | Disease  | entities      |
| paracetamol     |     125 |   135 | Drug     | matched_text  |
| fever           |     145 |   149 | Symptom  | entities      |
| headache        |     155 |   162 | Symptom  | entities      |
| amoxicillin     |     165 |   175 | Drug     | matched_text  |
| tonsilitis      |     185 |   194 | Disease  | entities      |



</div><div class="h3-box" markdown="1">

#### Introduction of a new parameter `dataSetInfo` to store dataset details for `AssertionDL` and `GenericClassifier` for Traceability

The parameters from the `Approach` class, utilized during model training, have been added into the `Model` class. These values are now directly stored within the model itself. Additionally, a new parameter named "dataSetInfo"(details regarding the dataset) has been added for `AssertionDL` and `GenericClassifier`.

*Example*:

```python
scope_window = [10,10]

assertionStatus = AssertionDLApproach()\
    .setLabelCol("label")\
    .setInputCols("document", "chunk", "embeddings")\
    .setOutputCol("assertion")\
    .setBatchSize(64)\
    .setDropout(0.1)\
    .setLearningRate(0.001)\
    .setEpochs(5)\
    .setValidationSplit(0.2)\
    .setMaxSentLen(250)\
    ...
    .setDatasetInfo("i2b2_assertion_sample_short_dataset")

# save trained model and load 
clinical_assertion = AssertionDLModel.load("./assertion_custom_model") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

!cat ./assertion_custom_model/metadata/part-00000
```


*Result*:

```python
{
    "paramMap": {
        "startCol": "start",
        "inputCols": ["document","chunk","embeddings"],
        "learningRate": 0.0010000000474974513,
        "outputLogsPath": "training_logs/",
        "storageRef": "clinical",
        "maxSentLen": 250,
        "scopeWindow": [10,10],
        "endCol": "end",
        "label": "label",
        "enableOutputLogs": true,
        "batchSize": 64,
        "includeConfidence": true,
        "graphFile": "./tf_graphs/assertion_graph.pb",
        "epochs": 5,
        "dropout": 0.10000000149011612,
        "graphFolder": "./tf_graphs",
        "outputCol": "assertion",
        "validationSplit": 0.20000000298023224,
        "datasetInfo": "i2b2_assertion_sample_short_dataset"
    }
}
```



</div><div class="h3-box" markdown="1">

#### Converting Visual NER Annotations to CoNLL Format for Training Text-Based NER Models with Visual Annotations

This module converts Visual NER annotations into the CoNLL format using the JohnSnowLabs NLP Lab. By processing an NLP Lab-exported JSON file containing Visual NER results, it generates a CoNLL file that is suitable for training Named Entity Recognition (NER) models.


*Example*:

```python
# Import the module
from sparknlp_jsl.alab import AnnotationLab
alab = AnnotationLab()

# Download sample Visual NER result JSON file
!wget -q https://raw.githubusercontent.com/JohnSnowLabs/spark-nlp-workshop/master/tutorials/Annotation_Lab/data/alab_visualner_result.json 

# Convert Visual NER annotations to CoNLL format
df = alab.get_conll_data_from_visualner(
    input_json_path = "alab_visualner_result.json",
    output_name = "visual_ner.conll",
    save_dir  = "exported_conll"
)
```


</div><div class="h3-box" markdown="1">

####  Performance Analysis of Deidentification Pipelines on Clinical Texts in a Cluster Environment


- Deidentification Pipelines Benchmarks

    This benchmark provides valuable insights into the efficiency and scalability of deidentification pipelines in different computational environments.

    - **Dataset:** 100000 Clinical Texts from MTSamples, approx. 508 tokens and 26.44 chunks per text.
    - **Versions:[May-2024]**
        - **spark-nlp Version:** v5.3.2
        - **spark-nlp-jsl Version:** v5.3.2
        - **Spark Version:** v3.4.0
    - **Instance Type:**
        - DataBricks Config: 
            - 32 CPU Core, 128GiB RAM (8 worker) (2.7 $/hr)\

            {:.table-model-big}
            |data_count |partition |Databricks |
            |----------:|---------:|----------:|
            |    100000 |      512 | 1h 42m 55s|
    
        - AWS EC2 instance Config:
                - 8 CPU cores, 58GiB RAM (r6a.2xlarge $0.4536/h)
            
            {:.table-model-big}
            |data_count |partition |   AWS   |
            |----------:|---------:|--------:|
            |    100000 |      512 | 3h 3m 40|


- Deidentification Pipelines Speed Comparison

    This benchmark presents a detailed comparison of various deidentification pipelines applied to a dataset of 10,000 custom clinical texts, aiming to anonymize sensitive information for research and analysis. The comparison evaluates the elapsed time and processing stages of different deidentification pipelines. Each pipeline is characterized by its unique combination of Named Entity Recognition (NER), deidentification methods, rule-based NER, clinical embeddings, and chunk merging processes.
    
    - **Dataset:** 10K Custom Clinical Texts with 1024 partitions, approx. 500 tokens and 14 chunks per text. 
    - **Versions:**
        - **spark-nlp Version:** v5.3.1
        - **spark-nlp-jsl Version:** v5.3.1
        - **Spark Version:** v3.4.0
    - **Instance Type:** 
        -  8 CPU Cores 52GiB RAM (Colab Pro - High RAM)


{:.table-model-big}
|Deidentification Pipeline Name                   | Elapsed Time     | Stages           |
|:------------------------------------------------|-----------------:|:-----------------| 
|[clinical_deidentification_subentity_optimized](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_optimized_en.html)| 67 min 44 seconds| 1 NER, 1 Deidentification, 13 Rule-based NER, 1 clinical embedding, 2 chunk merger  |
|[clinical_deidentification_generic_optimized](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_generic_optimized_en.html)    | 68 min 31 seconds| 1 NER, 1 Deidentification, 13 Rule-based NER, 1 clinical embedding, 2 chunk merger  |
|[clinical_deidentification_generic](https://nlp.johnsnowlabs.com/2024/02/21/clinical_deidentification_generic_en.html)                        | 86 min 24 seconds| 1 NER, 4 Deidentification, 13 Rule-based NER, 1 clinical embedding, 2 chunk merger  |
|[clinical_deidentification_subentity](https://nlp.johnsnowlabs.com/2024/02/21/clinical_deidentification_subentity_en.html)                    | 99 min 41 seconds| 1 NER, 4 Deidentification, 13 Rule-based NER, 1 clinical embedding, 2 chunk merger  |
|[clinical_deidentification](https://nlp.johnsnowlabs.com/2024/03/27/clinical_deidentification_en.html)                                        |117 min 44 seconds| 2 NER, 1 Deidentification, 13 Rule-based NER, 1 clinical embedding, 3 chunk merger  |
|[clinical_deidentification_nameAugmented](https://nlp.johnsnowlabs.com/2024/03/14/clinical_deidentification_subentity_nameAugmented_en.html)  |134 min 27 seconds| 2 NER, 4 Deidentification, 13 Rule-based NER, 1 clinical embedding, 3 chunk merger  |
|[clinical_deidentification_glove](https://nlp.johnsnowlabs.com/2023/06/17/clinical_deidentification_glove_en.html)                            |146 min 51 seconds| 2 NER, 4 Deidentification,  8 Rule-based NER, 1 clinical embedding, 3 chunk merger  |
|[clinical_deidentification_obfuscation_small](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_small_en.html)    |147 min 06 seconds| 1 NER, 1 Deidentification,  2 Rule-based NER, 1 clinical embedding, 1 chunk merger  |
|[clinical_deidentification_slim](https://nlp.johnsnowlabs.com/2023/06/17/clinical_deidentification_slim_en.html)                              |154 min 37 seconds| 2 NER, 4 Deidentification, 15 Rule-based NER, 1 glove embedding,    3 chunk merger  |
|[clinical_deidentification_multi_mode_output](https://nlp.johnsnowlabs.com/2024/03/27/clinical_deidentification_multi_mode_output_en.html)    |154 min 50 seconds| 2 NER, 4 Deidentification, 13 Rule-based NER, 1 clinical embedding, 3 chunk merger  |
|[clinical_deidentification_obfuscation_medium](https://nlp.johnsnowlabs.com/2024/02/09/clinical_deidentification_obfuscation_medium_en.html)  |205 min 40 seconds| 2 NER, 1 Deidentification,  2 Rule-based NER, 1 clinical embedding, 1 chunk merger  |

PS: The reasons pipelines with the same stages have different costs are due to the layers of the NER model and the hardcoded regexes in Deidentification.

Please check [Deidentification Benchmarks](https://nlp.johnsnowlabs.com/docs/en/benchmark#deidentification-benchmarks) for more detail

</div><div class="h3-box" markdown="1">


#### New Blogposts on Relation Extraction, MedDRA, Response to Treatment, and Pretrained Pipelines.

- [Next-Level Relation Extraction in Healthcare NLP: Introducing New Directional and Contextual Features](https://medium.com/john-snow-labs/next-level-relation-extraction-in-healthcare-nlp-introducing-new-directional-and-contextual-cc54eb68a699)
- [Clinical Document Analysis with One-Liner Pretrained Pipelines in Healthcare NLP](https://medium.com/john-snow-labs/clinical-document-analysis-with-one-liner-pretrained-pipelines-in-healthcare-nlp-4d468150bd53)
- [Mapping Medical Terms to MedDRA Ontology Using Healthcare NLP](https://medium.com/john-snow-labs/mapping-medical-terms-to-meddra-ontology-using-healthcare-nlp-f75ea44bdaff)
- [Response to Cancer Treatment](https://medium.com/john-snow-labs/response-to-cancer-treatment-d7d3b6f40aa3)


#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Added training params to trainable annotators within the metadata of the trained models
- Updated Risk Adjustment module with V28Y24
- Resolved index issue in `AssertionChunkConverter` annotator and `AnnotationLab.get_assertion_data` modules
- Resolved saving issue in `Flattener` annotator

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [PipelineTracer and PipelineOutputParser Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.4.PipelineTracer_and_PipelineOutputParser.ipynb)
- Updated [Task Based Clinical Pretrained Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.3.Task_Based_Clinical_Pretrained_Pipelines.ipynb)
- Updated [Pretrained Clinical Pipelines Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/11.Pretrained_Clinical_Pipelines.ipynb)
- Updated [ADE Demo](https://demo.johnsnowlabs.com/healthcare/ADE/)
- Updated [NER_POSOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/NER_POSOLOGY/)
- Updated [NER_RADIOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/NER_RADIOLOGY/)
- Updated [VOP Demo](https://demo.johnsnowlabs.com/healthcare/VOP/)
- Updated [SDOH Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/)
- Updated [ONCOLOGY Demo](https://demo.johnsnowlabs.com/healthcare/ONCOLOGY/)

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.


+ `meddra_llt_snomed_mapper`            
+ `snomed_meddra_llt_mapper`             
+ `explain_clinical_doc_sdoh`
+ `explain_clinical_doc_oncology`
+ `explain_clinical_doc_granular`            
+ `explain_clinical_doc_mental_health`   
+ `ner_medication_generic_pipeline`      
+ `ner_deid_context_augmented_pipeline`  
+ `ner_deid_generic_context_augmented_pipeline` 
+ `ner_deid_subentity_context_augmented_pipeline` 
+ `biolordresolve_rxnorm_augmented`      
+ `biolordresolve_umls_general_concepts`  
+ `biolordresolve_icd10cm_augmented_billable_hcc` 
+ `sbiobertresolve_snomed_veterinary_wip` 
+ `sbiobertresolve_umls_general_concepts` 
+ `biolordresolve_avg_rxnorm_augmented` 
+ `biolordresolve_snomed_findings_aux_concepts` 
+ `biolordresolve_cpt_procedures_measurements_augmented` 
+ `sbiobertresolve_umls_disease_syndrome` 
+ `sbiobertresolve_umls_findings`
+ `sbiobertresolve_umls_major_concepts` 
+ `sbiobertresolve_umls_clinical_drugs` 
+ `sbiobertresolve_umls_drug_substance` 
+ `sbiobertresolve_icd9` 



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Versions

</div>
{%- include docs-healthcare-pagination.html -%}