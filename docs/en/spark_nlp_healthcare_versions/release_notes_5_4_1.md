---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Healthcare NLP v5.4.1 Release Notes 
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_4_1
key: docs-licensed-release-notes
modify_date: 2024-08-21
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.4.1

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with 9 new Large Language Models (LLMs), a brand new LargeFewShotClassifier annotator, and 31 new and updated clinical pretrained models and pipelines**.

+ Explore 9 new specialized LLMs at various sizes and quantization levels for healthcare applications (medical note summarization, Q&A, RAG, and Chat)
+ Introducing 7 new oncological text classification models to detect documents mentioning metastasis, therapy, and other oncology terms.
+ Introducing a new oncology NER model to detect 6 main cancer types and 5 crucial contexts for cancer diagnosis, treatment, and prognosis.
+ Introducing a new stigmatization NER model to identify and categorize stigmatizing language in medical records by extracting entities related to patient behavior, demeanor, and healthcare provider attitudes.
+ New rule-based entity matcher models to customize De-Identification pipelines.
+ 3 new Entity Resolver models for associate clinical entities with RxNorm codes.
+ Introducing the new `LargeFewShotClassifierModel` annotator and 2 new classification models (age group detection and drug adverse event classification) that are trained with small datasets while achieving comparable performance to the models trained with larger datasets.
+ Introducing the `DocumentFiltererByNER` annotator to filter out the documents and sentences having certain types of named entities within the same pipeline.
+ Introducing a brand new `Mapper2Chunk` annotator to create a new chunk type from any mapper.
+ Introducing new `setConfidenceCalculationDirection` parameter for `ContextualAssertion` (rule-based context aware assertion status detection) to allow direction-sensitive confidence score calculation 
+ Introducing a new `dict_to_annotation_converter` module for converting dictionary data to Spark NLP annotations (e.g. allowing deidentification and obfuscation over a list of entities within a JSON format such as GenAI annotations)
+ New blog posts on identifying named entities in medical text with Zero-Shot learning
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
    - Enhanced metadata information with the `setMetadataFields` field for `AssertionChunkConverter`
    - Added new date format for deidentification
    - Added new parameters for the `Replacer` annotator to allow replacing any type of entities in a text with any other phrase or placeholder (e.g. replace all the drug generic names with drug brand names, etc.)
    - Added `document_id` info and confidence scores for `resolutions` and `assertions` fields to the `PipelineOutputParser` module
    - Resolved Flattener NullPointerException; if the column is empty, the Flattener returns empty columns instead of throwing an exception.
    - Resolved the AssertionMerger loading issue; an exception was thrown when attempting to load the AssertionMerger model.
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
    - New [DocumentFiltererByNER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentFiltererByNER.ipynb) MOOC Notebook
    - New [LargeFewShotClassifier](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/LargeFewShotClassifierModel.ipynb) MOOC Notebook
    - New [Mapper2Chunk](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Mapper2Chunk.ipynb) MOOC Notebook
    - Updated [AssertionChunkConverter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionChunkConverter.ipynb) MOOC Notebook
    - Updated [ContextualAssertion](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualAssertion.ipynb) MOOC Notebook
    - Updated [Replacer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb) MOOC Notebook
    - Updated [Clinical Entity Resolver](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb) notebook
    - Updated [Improved Entity Resolution with SentenceChunkEmbeddings](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.1.Improved_Entity_Resolution_with_SentenceChunkEmbeddings.ipynb) notebook
    - Updated [Improved Entity Resolvers in SparkNLP with sBert](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb) notebook
    - Updated [Clinical Medication Use Case](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/43.Clinical_Medication_Use_Case.ipynb) notebook
    - Updated [Oncology_Model](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb) notebook
    - New [Text Classification with LargeFewShotClassifier](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.4.Text_Classification_with_LargeFewShotClassifier.ipynb) Notebook
    - New [NER_STIGMATIZATION](https://demo.johnsnowlabs.com/healthcare/NER_STIGMATIZATION/) demo
    - Updated [NER_ONCOLOGY_CLINICAL](https://demo.johnsnowlabs.com/healthcare/NER_ONCOLOGY_CLINICAL/) demo
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">
 
#### Explore 9 New Specialized LLMs at Various Sizes and Quantisation Levels for Healthcare Applications (Medical Note Summarization, Q&A, RAG, and Chat)

Discover nine newly released large language models designed to tackle various tasks in the healthcare domain. These models include capabilities for summarization, question answering, retrieval-augmented generation (RAG), chat functionalities, and medical named entity recognition (NER). Each model is optimized with different quantization levels (q16, q8, q4) to balance performance and efficiency, catering to specific needs in medical data processing and analysis. Whether you need detailed summaries, precise Q&A, or accurate entity extraction, these models offer advanced solutions for healthcare professionals and researchers.


{:.table-model-big}
| Model Name              | Description |
|-------------------------|-------------|
| [JSL_MedM_q16_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_medm_q16_v2_en.html)    | Summarization, Q&A, RAG, and Chat |
| [JSL_MedM_q8_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_medm_q8_v2_en.html)      | Summarization, Q&A, RAG, and Chat |
| [JSL_MedM_q4_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_medm_q4_v2_en.html)      | Summarization, Q&A, RAG, and Chat |
| [JSL_MedS_RAG_q16_v1](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_rag_q16_v1_en.html)| LLM component of Retrieval Augmented Generation (RAG)  |
| [JSL_MedS_RAG_q8_v1](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_rag_q8_v1_en.html)  | LLM component of Retrieval Augmented Generation (RAG)  |
| [JSL_MedS_RAG_q4_v1](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_rag_q4_v1_en.html)  | LLM component of Retrieval Augmented Generation (RAG)  |
| [JSL_MedS_NER_q16_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_ner_q16_v2_en.html)| Extract and link medical named entities |
| [JSL_MedS_NER_q8_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_ner_q8_v2_en.html)  | Extract and link medical named entities |
| [JSL_MedS_NER_q4_v2](https://nlp.johnsnowlabs.com/2024/08/21/jsl_meds_ner_q4_v2_en.html)  | Extract and link medical named entities |

**We recommend using 8b quantized versions of the models in a GPU-poor environment as the qualitative performance difference between q16 and q8 versions is very negligible.**

Note: Our current LLM loader implementation based on `llama.cpp` may lag behind when it comes to inference speed and output quality on certain use cases. We have other means of serving these models outside of the Healthcare NLP library and users are advised to get in touch with us if there is such a need. 

*Example*:

```python

from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_medm_q16_v2", "en", "clinical/models")

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin"""

llm_loader_pretrained.generate(prompt)
```

*Result*:

```bash
Answer: E. Nitrofurantoin. This is the best treatment for that patient.
```

Please check the [LLMLoader](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/46.Loading_Medical_and_Open-Souce_LLMs.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

####  Introducing 7 New Oncological Text Classification Models to Detect Documents Mentioning Metastasis, Therapy, and Other Oncology Terms

Explore 7 new state-of-the-art oncological text classification models designed to identify and categorize clinical sentences related to metastasis, oncology, and therapy. Each model is tailored for specific tasks, such as identifying metastasis-related terms or broader oncology and therapy concepts in clinical narratives.
 
Predicted Classes:
- `True`: Contains therapy-related terms.
- `False`: Doesn’t contain therapy-related terms.

{:.table-model-big}
| Model Name              | Description | Predicted Classes |
|-------------------------|-------------|-------------|
|[bert_sequence_classifier_metastasis](https://nlp.johnsnowlabs.com/2024/08/02/bert_sequence_classifier_metastasis_en.html)      | a metastasis classification model that can determine whether clinical sentences include terms related to metastasis or not. |  `0`, `1` |
|[classifierdl_metastasis](https://nlp.johnsnowlabs.com/2024/08/09/classifierdl_metastasis_en.html)      | a metastasis classification model that determines whether clinical sentences include terms related to metastasis. |  `True`, `False` |
|[generic_classifier_metastasis](https://nlp.johnsnowlabs.com/2024/08/09/generic_classifier_metastasis_en.html)      | a metastasis classification model that determines whether clinical sentences include terms related to metastasis. | `True`, `False` |
|[generic_logreg_classifier_metastasis](https://nlp.johnsnowlabs.com/2024/08/09/generic_logreg_classifier_metastasis_en.html)      | trained with the Generic Classifier annotator and the Logistic Regression algorithm and classifies text/sentence into two categories. | `True`, `False` |
|[generic_svm_classifier_metastasis](https://nlp.johnsnowlabs.com/2024/08/09/generic_svm_classifier_metastasis_en.html)      | trained with the Generic Classifier annotator and the Support Vector Machine (SVM) algorithm and classifies text/sentence into two categories.| `True`, `False` |
|[generic_classifier_oncology](https://nlp.johnsnowlabs.com/2024/08/13/generic_classifier_oncology_en.html)      |  an oncology classification model that determines whether clinical sentences include terms related to oncology.| `True`, `False` |
|[generic_classifier_therapy](https://nlp.johnsnowlabs.com/2024/08/16/generic_classifier_therapy_en.html)      | a therapy classification model that determines whether clinical sentences include terms related to therapy.| `True`, `False` |

*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained("bert_sequence_classifier_metastasis", "en", "clinical/models")\
    .setInputCols(["sentence", 'token'])\
    .setOutputCol("prediction")

sample_texts =[
    ["Contrast MRI confirmed the findings of meningeal carcinomatosis."],
    ["A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis."],
    ["The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci."] ,
    ["After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined."],
    ["The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer."],
    ["The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."]
]

# `1`: Contains metastasis-related terms.
# `0`: Doesn't contain metastasis-related terms.
```

*Result*:

{:.table-model-big}
|                                                                                                text|result|
|----------------------------------------------------------------------------------------------------|------|
|                                    Contrast MRI confirmed the findings of meningeal carcinomatosis.|   1  |
|         A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.|   0  |
|The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal invol...|   1  |
|After all procedures done and reviewing the findings, biochemical results and screening, the TNM ...|   0  |
|      The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.|   1  |
|The patient's care plan is adjusted to focus on symptom management and slowing the progression of...|   0  |

Please check the [Oncology_Model](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">

####  Introducing a New Oncology NER Model to Detect 6 Main Cancer Types and 5 Crucial Contexts for Cancer Diagnosis, Treatment, and Prognosis

his Named Entity Recognition (NER) model is specifically trained to extract critical information from clinical and biomedical text related to oncology. The model recognizes 6 main cancer types and 5 crucial contexts for cancer diagnosis, treatment, and prognosis.:

- `CNS Tumor Type`: Tumors originating in the central nervous system, including brain and spinal cord tumors.
- `Carcinoma Type`: Cancers arising from epithelial cells, which are the most common type of cancer, including breast, lung, and colorectal carcinomas.
- `Leukemia Type`: Cancers of the blood and bone marrow, characterized by the abnormal proliferation of white blood cells.
- `Lymphoma Type`: Cancers of the lymphatic system, affecting lymphocytes (a type of white blood cell), including Hodgkin and non-Hodgkin lymphomas.
- `Melanoma`: A type of skin cancer originating from melanocytes, the cells that produce pigment.
- `Sarcoma Type`: Cancers arising from connective tissues, such as bone, cartilage, fat, muscle, or vascular tissues.
- `Metastasis`: Recognizes terms related to the spread of cancer to different parts of the body, including mentions of metastatic sites and related clinical descriptions.
- `Biomarker`: Extracts entities related to cancer biomarkers, including genetic markers, protein levels, and other measurable indicators used for cancer diagnosis, prognosis, and treatment response.
- `Biomarker_Quant`: Extracts numerical measurements or values associated with the biomarker.
- `Biomarker_Result`: Extracts descriptive or categorical assessments of the biomarker status.
- `Body Site`: Knowing the primary site of the tumor is essential for diagnosis and treatment planning. The body site where the cancer originates often determines the type of cancer and influences therapeutic approaches.

{:.table-model-big}
| Model Name              | Description | Predicted Entities  |
|-------------------------|-------------|---------------------|
|[ner_cancer_types_wip](https://nlp.johnsnowlabs.com/2024/08/16/ner_cancer_types_wip_en.html) | This Named Entity Recognition (NER) model is specifically trained to recognize 6 main cancer types, body sites, biomarkers, and their results. | `CNS_Tumor_Type`, `Carcinoma_Type`, `Leukemia_Type`, `Lymphoma_Type`, `Melanoma`, `Sarcoma_Type`, `Metastasis`, `Body_Site`, `Biomarker`, `Biomarker_Quant`, `Biomarker_Result` |

This model achieves 0.92 accuracy and 0.91 macro F1 across 11 entities

*Example*:

```python
ner_model = MedicalNerModel.pretrained('ner_cancer_types_wip', "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = """
Patient A, a 55-year-old female, presented with carcinoma in the left breast. A biopsy revealed an elevated HER2. The patient also showed a slightly elevated CA 15-3 level at 45 U/mL. Follow-up imaging revealed metastasis to the axillary lymph nodes, and further scans indicated small metastatic lesions in the liver.
Additionally, imaging of the patient's lower back indicated a possible sarcoma. Subsequent tests identified elevated levels of lactate dehydrogenase (LDH), with a result of 580 IU/L (normal range: 140-280 IU/L), and a biopsy confirmed metastasis to the lungs.
Routine bloodwork revealed a mild increase in B2M (Beta-2 microglobulin), suggestive of possible lymphoma, and a normal range for hemoglobin and white blood cells, ruling out leukemia. CNS involvement was ruled out as imaging did not indicate any anomalies.
For melanoma screening, a suspicious mole on the patient's arm was biopsied, and tests confirmed a BRAF V600E mutation. Further imaging revealed metastatic spread to the lungs and liver.
"""
```

*Result*:

{:.table-model-big}
| ner_chunk          |begin|end | ner_label      | 
|--------------------|-----|----|----------------|
|carcinoma           |49   |57  |Carcinoma_Type  |
|breast              |71   |76  |Body_Site       |
|elevated            |100  |107 |Biomarker_Result|
|HER2                |109  |112 |Biomarker       |
|elevated            |150  |157 |Biomarker_Result|
|CA 15-3             |159  |165 |Biomarker       |
|45 U/mL             |176  |182 |Biomarker_Quant |
|metastasis          |212  |221 |Metastasis      |
|axillary lymph nodes|230  |249 |Body_Site       |
|metastatic          |286  |295 |Metastasis      |
|liver               |312  |316 |Body_Site       |
|sarcoma             |391  |397 |Sarcoma_Type    |
|elevated            |428  |435 |Biomarker_Result|
|LDH                 |470  |472 |Biomarker       |
|580 IU/L            |493  |500 |Biomarker_Quant |
|metastasis          |555  |564 |Metastasis      |
|lungs               |573  |577 |Body_Site       |
|B2M                 |627  |629 |Biomarker       |
|lymphoma            |678  |685 |Lymphoma_Type   |
|leukemia            |756  |763 |Leukemia_Type   |
|CNS                 |766  |768 |Body_Site       |
|melanoma            |844  |851 |Melanoma        |
|arm                 |899  |901 |Body_Site       |
|BRAF                |939  |942 |Biomarker       |
|mutation            |950  |957 |Biomarker_Result|
|metastatic          |985  |994 |Metastasis      |
|lungs               |1010 |1014|Body_Site       |
|liver               |1020 |1024|Body_Site       |


Please check the [Oncology_Model](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

####  Introducing a New Stigmatization NER Model to Identify and Categorize Stigmatizing Language in Medical Records by Extracting Entities Related to Patient Behavior, Demeanor, and Healthcare Provider Attitudes.

This NER model identifies and categorizes stigmatizing language in medical records by extracting entities related to patient behavior, demeanor, and healthcare provider attitudes, aiming to assess and mitigate the impact of such language on patient care.

{:.table-model-big}
| Model Name              | Description | Predicted Entities  |
|-------------------------|-------------|---------------------|
|[ner_stigmatization_wip](https://nlp.johnsnowlabs.com/2024/08/27/ner_stigmatization_wip_en.html)      | This Named Entity Recognition (NER) model is specifically trained to extract critical information from clinical text related to stigmatization. This model aims to systematically collect and analyze data on stigmatizing language found in patients' medical records. |`Aggressive`, `Argumentative`, `Calm`, `Resistant`, `Credibility_Doubts`, `Suspected_DSB`, `Compliant`, `Noncompliant`, `Collaborative_Decision_Making`, `Neglected_Appearance`, `Paternalistic_Tone`, `Poor_Reasoning`, `Poor_Decision_Making`, `Other_Discriminatory_Language`, `Positive_Descriptors`, `Positive_Assessment`, `Disoriented`, `Test`, `Treatment`, `Problem`|

This model achieves 0.91 accuracy and 0.89 macro F1 across 11 entities

*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_stigmatization_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_texts = """During his hospital stay, David Brown's reluctance to seek care and resistance to necessary treatments highlighted the significant impact of poor reasoning and judgment on his health outcomes. His confrontational attitude and frequent defensiveness during discussions about his treatment plan revealed the deep-seated anxieties he harbored about his health. Despite these challenges, the healthcare team made concerted efforts to educate him on the importance of adhering to his prescribed regimen and attending regular follow-up appointments. However, Mr. Brown often fixated on incorrect beliefs, insisting that his symptoms were solely due to stress, which further complicated his care."""

```

*Result*:

{:.table-model-big}
|chunk                      |begin|end|ner_label         |
|---------------------------|-----|---|------------------|
|reluctance                 |40   |49 |Resistant         |
|resistance                 |68   |77 |Resistant         |
|treatments                 |92   |101|TREATMENT         |
|poor reasoning and judgment|141  |167|Poor_Reasoning    |
|confrontational            |197  |211|Argumentative     |
|defensiveness              |235  |247|Argumentative     |
|the deep-seated anxieties  |302  |326|PROBLEM           |
|adhering                   |463  |470|Compliant         |
|his prescribed regimen     |475  |496|TREATMENT         |
|insisting                  |599  |607|Credibility_Doubts|
|his symptoms               |614  |625|PROBLEM           |
|stress                     |646  |651|PROBLEM           |



</div><div class="h3-box" markdown="1">

#### New Rule-Based Entity Matcher Models to Customize De-Identification Pipelines

We introduce a suite of text and regex matchers, specifically designed to enhance the deidentification and clinical document understanding process with rule-based methods.


{:.table-model-big}
| Model Name              | Description | Predicted Entities  |
|-------------------------|-------------|---------------------|
|[email_matcher](https://nlp.johnsnowlabs.com/2024/08/21/email_matcher_en.html)|This model extracts emails in clinical notes using rule-based RegexMatcherInternal annotator. | `EMAIL` |
|[url_matcher](https://nlp.johnsnowlabs.com/2024/08/21/url_matcher_en.html)     | This model extracts URLs in clinical notes using rule-based RegexMatcherInternal annotator. | `URL` |
|[ip_matcher](https://nlp.johnsnowlabs.com/2024/08/21/ip_matcher_en.html)       | This model extracts IP Addresses in clinical notes using rule-based RegexMatcherInternal annotator. | `IP` |

*Example*:

```python
email_regex_matcher = RegexMatcherInternalModel.pretrained("email_matcher", "en", "clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("email_chunk")

url_regex_matcher = RegexMatcherInternalModel.pretrained("url_matcher", "en", "clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("url_chunk") 

ip_regex_matcher = RegexMatcherInternalModel.pretrained("ip_matcher", "en", "clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("ip_chunk")  

text = """
Name: David Hale, ID: 1231511863, Driver's License No: A334455B, SSN: 324-59-8674. E-mail: hale@gmail.com.
Access the router at http://192.168.0.1 for configuration. Please connect to 10.0.0.1 to access the database.
For more details, visit our website at www.johnsnowlabs.com or check out http://www.johnsnowlabs.com/info for general info.
Visit http://198.51.100.42 for more information. File transfers can be done via ftp://files.example.com.
"""
```

*Result*:

{:.table-model-big}
| chunk                            |begin|end|ner_label|ner_source |
|----------------------------------|-----|---|---------|-----------|
| hale@gmail.com                   |92   |105|EMAIL    |email_chunk|
| 192.168.0.1                      |136  |146|IP       |ip_chunk   |
| 10.0.0.1                         |185  |192|IP       |ip_chunk   |
| www.johnsnowlabs.com             |257  |276|URL      |url_chunk  |
| http://www.johnsnowlabs.com/info |291  |322|URL      |url_chunk  |
| 198.51.100.42                    |355  |367|IP       |ip_chunk   |
| ftp://files.example.com          |422  |444|URL      |url_chunk  |



</div><div class="h3-box" markdown="1">
    
####  3 New Sentence Entity Resolver Models for Associate Clinical Entities with RxNorm Codes

Introducing 3 new Sentence Entity Resolver Models `sbiobertresolve_rxnorm_augmented_v2`, `biolordresolve_rxnorm_augmented_v2`, and `biolordresolve_avg_rxnorm_augmented_v2` help to map medical entities to RXNORM codes.

{:.table-model-big}
| Model Name                                                            |      Description            |
|-----------------------------------------------------------------------|-----------------------------|
| [`sbiobertresolve_rxnorm_augmented_v2`](https://nlp.johnsnowlabs.com/2024/08/14/sbiobertresolve_rxnorm_augmented_v2_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. |
| [`biolordresolve_rxnorm_augmented_v2`](https://nlp.johnsnowlabs.com/2024/08/19/biolordresolve_rxnorm_augmented_v2_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023_c` embeddings. |
| [`biolordresolve_avg_rxnorm_augmented_v2`](https://nlp.johnsnowlabs.com/2024/08/20/biolordresolve_avg_rxnorm_augmented_v2_en.html) | This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023` embeddings. |

*Example*:

```python
rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented_v2", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

text= "The patient was prescribed aspirin and an Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals and metformin 1000 mg two times a day and Lisinopril 10 mg daily"
```

*Result*:

{:.table-model-big}
|ner_chunk|entity|RxNormCode| resolutions|all_k_resolutions|all_k_results|all_k_distances|all_k_aux_labels|
|------|------|----------|-----------|-------|--------|------|------|
|          aspirin|  DRUG|      1191|                                              aspirin[aspirin]|aspirin[aspirin]:::aspirin Oral Powder Product:::YS...|1191:::1295740:::405403:::218266:...|0.0000:::4.1826:::5.7007:::6.0877:::6....|Ingredient:::Clinical Dose Group:::Brand Name...|
|Albuterol inhaler|  DRUG|    745678|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]|albuterol Metered Dose Inhaler[albuterol Metered Do...|745678:::2108226:::1154602:::2108...|4.9847:::5.1028:::5.4746:::5.7809:::6....|Clinical Drug Form:::Clinical Drug Form:::Cli...|
|    Coumadin 5 mg|  DRUG|    855333|                               warfarin sodium 5 MG [Coumadin]|warfarin sodium 5 MG [Coumadin]:::coumarin 5 MG[cou...|855333:::438740:::153692:::352120...|0.0000:::4.0885:::5.3065:::5.5132:::5....|Branded Drug Comp:::Clinical Drug Comp:::Bran...|
|metformin 1000 mg|  DRUG|    316255|                          metformin 1000 MG[metformin 1000 MG]|metformin 1000 MG[metformin 1000 MG]:::metformin hy...|316255:::860995:::860997:::861014...|0.0000:::5.2988:::5.9071:::6.3066:::6....|Clinical Drug Comp:::Clinical Drug Comp:::Bra...|
| Lisinopril 10 mg|  DRUG|    316151|                            lisinopril 10 MG[lisinopril 10 MG]|lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 ...|316151:::567576:::565846:::393444...|0.0000:::3.6543:::4.2783:::4.2805:::4....|Clinical Drug Comp:::Branded Drug Comp:::Bran...|



</div><div class="h3-box" markdown="1">
    
####  Introducing the New `LargeFewShotClassifierModel` Annotator and 2 New Classification Models (Age Group Detection and Drug Adverse Event Classification) That are Trained with Small Datasets While Achieving Comparable Performance to The Models Trained with Larger Datasets

The new LargeFewShotClassifierModel annotator  is designed to work effectively with minimal labeled data, offering flexibility and adaptability to new, unseen classes. Key parameters include batch size, case sensitivity, and maximum sentence length. The release includes two new classification models:

{:.table-model-big}
| Model Name              | Description | Predicted Entities  | Benchmarking  |
|-------------------------|-------------|---------------------|---------------------|
|[large_fewshot_classifier_age_group](https://nlp.johnsnowlabs.com/2024/08/15/large_fewshot_classifier_age_group_en.html)      | Identifies and classifies tweets reporting Adverse Drug Events (ADEs), learning effectively from minimal labeled examples and adapting to new, unseen classes. | `ADE`, `noADE` | Achieves 0.90 accuracy and 0.81 macro F1 across 3 entities |
|[large_fewshot_classifier_ade](https://nlp.johnsnowlabs.com/2024/08/12/large_fewshot_classifier_ade_en.html)      | Identifies and classifies the age group of a person mentioned in health documents, learning effectively from minimal labeled examples and adapting to new, unseen classes. |`Adult`, `Child`, `Unknown` | Achieves 0.89 accuracy and 0.81 macro F1 across 3 entities |


*Example*:

```python

large_few_shot_classifier = LargeFewShotClassifierModel()\
    .pretrained('large_fewshot_classifier_ade')\
    .setInputCols("document")\
    .setOutputCol("prediction")

text_list = [
    ["The patient developed severe liver toxicity after taking the medication for three weeks"],
    ["He experienced no complications during the treatment and reported feeling much better."],
    ["She experienced a sudden drop in blood pressure after the administration of the new drug."],
    ["The doctor recommended a daily dosage of the vitamin supplement to improve her health."]
]
```

*Result*:

{:.table-model-big}
|text                                                                                     |result|
|-----------------------------------------------------------------------------------------|------|
|The patient developed severe liver toxicity after taking the medication for three weeks  |ADE   |
|He experienced no complications during the treatment and reported feeling much better.   |noADE |
|She experienced a sudden drop in blood pressure after the administration of the new drug.|ADE   |
|The doctor recommended a daily dosage of the vitamin supplement to improve her health.   |noADE |


Please check the [LargeFewShotClassifier](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.4.Text_Classification_with_LargeFewShotClassifier.ipynb) Notebook for more information



</div><div class="h3-box" markdown="1">
    
#### Introducing `DocumentFiltererByNER` Annotator to Filter Out the Documents and Sentences Having Certain Types of Named Entities within the Same Pipeline

The `DocumentFiltererByNER` annotator returns sentences containing the entity chunks you have filtered, allowing you to see only the sentences with the entities you want. It is particularly useful for extracting and organizing the results obtained from Spark NLP Pipelines.

Key Parameters:

- `blackList`: If defined, list of entities to ignore. The rest will be processed.
- `whiteList`: If defined, list of entities to process. The rest will be ignored.
- `caseSensitive`: Determines whether the definitions of the white-listed and black-listed entities are case sensitive or not.
- `outputAsDocument`: Whether to return all sentences joined into a single document. (default: `False`).
- `joinString`: This parameter specifies the string that will be inserted between results of documents when combining them into a single result if outputAsDocument is set to `True` (default is: " ").


*Example*:

```python
filterer = medical.DocumentFiltererByNER() \
    .setInputCols(["sentence", "ner_chunk"]) \
    .setOutputCol("filterer") \
    .setWhiteList(["Disease_Syndrome_Disorder"])\
    .setOutputAsDocument(True)\
    .setJoinString(" ")

spark_df = spark.createDataFrame([
    [1,"Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cancer are more likely to develop serious illness."],
    [2,"Anyone can get sick with COVID-19 and become seriously ill or die at any age. The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads. Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing your hands or using an alcohol-based rub frequently."],
    [3, "Get vaccinated when it’s your turn and follow local guidance. Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention. The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols. It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate until you recover if you feel unwell."]
    ]).toDF("idx","text")
```

*Input DataFrame*:

{:.table-model-big}
|idx|sent_id| sentence                                                                                                                                 | ner_chunk                                                                          | ner_label                                                                                                       |
|---|-------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
|  1|      0| Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.                                                  | ['Coronavirus disease', 'infectious disease']                                      | ['Disease_Syndrome_Disorder', 'Disease_Syndrome_Disorder']                                                      |
|  1|      1| Most people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment.| ['infected', 'virus', 'mild', 'moderate', 'respiratory illness']                   | ['Disease_Syndrome_Disorder', 'Disease_Syndrome_Disorder', 'Modifier', 'Modifier', 'Disease_Syndrome_Disorder'] |
|  1|      2| However, some will become seriously ill and require medical attention.                                                                   | ['ill']                                                                            | ['Symptom']                                                                                                     |
|  1|      3| Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, or cance...| ['cardiovascular disease', 'diabetes', 'chronic', 'respiratory disease', 'cancer'] | ['Heart_Disease', 'Diabetes', 'Modifier', 'Disease_Syndrome_Disorder', 'Oncological']                           |
|  2|      0| Anyone can get sick with COVID-19 and become seriously ill or die at any age.                                                            | ['COVID-19', 'ill']                                                                | ['Drug_Ingredient', 'Symptom']                                                                                  |
|  2|      1| The best way to prevent and slow down transmission is to be well informed about the disease and how the virus spreads.                   | nan                                                                                | nan                                                                                                             |
|  2|      2| Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing ...| ['infection', 'hands', 'alcohol-based rub', 'frequently']                          | ['Disease_Syndrome_Disorder', 'External_body_part_or_region', 'Medical_Device', 'Modifier']                     |
|  3|      0| Get vaccinated when it’s your turn and follow local guidance.                                                                            | nan                                                                                | nan                                                                                                             |
|  3|      1| Stay home if you feel unwell.                                                                                                            | ['unwell']                                                                         | ['Symptom']                                                                                                     |
|  3|      2| If you have a fever, cough and difficulty breathing, seek medical attention.                                                             | ['fever', 'cough', 'difficulty breathing']                                         | ['VS_Finding', 'Symptom', 'Symptom']                                                                            |
|  3|      3| The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe.  | ['infected person’s mouth', 'nose', 'cough', 'sneeze', 'sing or breathe']          | ['Disease_Syndrome_Disorder', 'External_body_part_or_region', 'Symptom', 'Symptom', 'Symptom']                  |
|  3|      4| These particles range from larger respiratory droplets to smaller aerosols.                                                              | nan                                                                                | nan                                                                                                             |
|  3|      5| It is important to practice respiratory etiquette, for example by coughing into a flexed elbow, and to stay home and self-isolate unti...| ['coughing into a flexed elbow', 'unwell']                                         | ['Symptom', 'Symptom']                                                                                          |

*Result after filtering*:

{:.table-model-big}
|idx | metadata                                                  | result                                                                                                                                      |
|---:|:----------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [{'sentence': '0'}, {'sentence': '1'}, {'sentence': '3'}] | ['Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.', 'Most people infected with the virus will exp...|
|  2 | [{'sentence': '2'}]                                       | ['Protect yourself and others from infection by staying at least 1 metre apart from others, wearing a properly fitted mask, and washing y...|
|  3 | [{'sentence': '3'}]                                       | ['The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe.'] |

Please check the [DocumentFiltererByNER](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentFiltererByNER.ipynb) Notebook for more information


</div><div class="h3-box" markdown="1">

#### Introducing a Brand New `Mapper2Chunk` Annotator to Create a New Chunk Type from any Mapper

The `Mapper2Chunk` annotator converts 'LABELED_DEPENDENCY' type annotations coming from ChunkMapper into 'CHUNK' type to create a new chunk-type column, compatible with annotators that use chunk type as input.

Key Parameter:
- `FilterNoneValues`: Whether to filter 'NONE' values. The default is `false`.


*Example*:

```python
ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

chunkMapper = ChunkMapperModel.pretrained("drug_action_treatment_mapper", "en", "clinical/models") \
    .setInputCols(["ner_chunk"]) \
    .setOutputCol("relations") \
    .setRels(["action"])

mapper2chunk = Mapper2Chunk() \
    .setInputCols(["relations"]) \
    .setOutputCol("chunk") \
    .setFilterNoneValues(True)

text = """Patient resting in bed. Patient given azithromycin without any difficulty. Patient denies nausea at this time. Zofran declined. Patient is also having intermittent sweating"""
```


*Input DataFrame*:

{:.table-model-big}
|result       |annotatorType                |
|-------------|-----------------------------|
|[bactericidal, antiemetic, anti-abstinence, NONE, NONE]|[labeled_dependency, labeled_dependency, labeled_dependency, labeled_dependency, labeled_dependency]|


*Result after mapper2chunk*:

{:.table-model-big}
|result                                     |annotatorType        |
|-------------------------------------------|---------------------|
|[bactericidal, antiemetic, anti-abstinence]|[chunk, chunk, chunk]|



</div><div class="h3-box" markdown="1">

#### Introducing new `setConfidenceCalculationDirection` Parameter for `ContextualAssertion` (Rule Based Context-Aware Assertion Status Detection) to Allow Direction-Sensitive Confidence Score Calculation


The `setConfidenceCalculationDirection` parameter in the ContextualAssertion model allows users to specify the direction (left, right, or both) for calculating assertion confidence in clinical text analysis. By default, the direction is set to "left". This feature is easily configurable within the Spark NLP framework, providing more control over assertion confidence calculations.
 
*Example*:

```python
contextual_assertion = ContextualAssertion()\
            .setInputCols("sentence", "token", "ner_chunk") \
            .setOutputCol("assertion") \
            .setConfidenceCalculationDirection("both")

text = """Patient resting in bed. Patient given azithromycin without any difficulty. Patient has audible wheezing, states chest tightness.
No evidence of hypertension. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating
associated with pneumonia. Patient refused pain but tylenol still given. Neither substance abuse nor alcohol use however cocaine
once used in the last year. Alcoholism unlikely. Patient has headache and fever. Patient is not diabetic. Not clearly of diarrhea.
Lab reports confirm lymphocytopenia. Cardaic rhythm is Sinus bradycardia. Patient also has a history of cardiac injury.
No kidney injury reported. No abnormal rashes or ulcers. Patient might not have liver disease. Confirmed absence of hemoptysis.
Although patient has severe pneumonia and fever, test reports are negative for COVID-19 infection. COVID-19 viral infection absent.
"""
```
*Result*:

{:.table-model-big}
|ner_chunk         |begin|end|confidence|result|
|------------------|-----|---|----------|------|
|any difficulty    |59   |72 |0.9802    |absent|
|hypertension      |149  |160|0.7711    |absent|
|nausea            |178  |183|0.9802    |absent|
|zofran            |199  |204|0.9802    |absent|
|pain              |309  |312|0.9802    |absent|
|tylenol           |318  |324|0.8187    |absent|
|Alcoholism        |428  |437|0.9802    |absent|
|diabetic          |496  |503|0.9802    |absent|
|kidney injury     |664  |676|0.9802    |absent|
|abnormal rashes   |691  |705|0.9802    |absent|
|ulcers            |710  |715|0.6703    |absent|
|liver disease     |741  |753|0.8869    |absent|
|hemoptysis        |777  |786|0.9802    |absent|
|COVID-19 infection|873  |890|0.9802    |absent|
|viral infection   |902  |916|0.9802    |absent|

Please check the [ContextualAssertion](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualAssertion.ipynb) Notebook for more information




</div><div class="h3-box" markdown="1">

#### Introducing a New `dict_to_annotation_converter` Module for Converting Dictionary Data to Spark NLP Annotations (e.g. Allowing Deidentification and Obfuscation Over a List of Entities within a JSON Format such as GenAI Annotations)

This method converts a list of dictionaries into a Spark DataFrame with document and chunk columns compatible with Spark NLP for tasks like deidentification. The input data must include text and chunk information with specific attributes, such as start and end indices, entity types, and metadata. The method also allows customization of column names and an optional adjustment of chunk end indices.

*Example*:

```python
list_of_dict = [
    {
        "text": "My name is George, and I was born on 12/11/1995. I have the pleasure of working at John Snow Labs.",
        "chunks": [
            {
                "begin": 11,
                "end": 16,
                "result": "George",
                "entity": "PERSON",
                "metadata": {"confidence": "1", "ner_source": "ner_deid"}
            },
            {
                "begin": 37,
                "end": 46,
                "result": "12/11/1995",
                "entity": "DATE",
                "metadata": {"confidence": "0.9", "ner_source": "ner_deid"}
            },
            {
                "begin": 83,
                "end": 96,
                "result": "John Snow labs",
                "entity": "ORG",
                "metadata": {"confidence": "0.87", "ner_source": "ner_deid"}
            }
            ],
        "doc_id": "1",
        "file_path": "/path/to/file1"
    }
 ]
from sparknlp_jsl.annotator import LightDeIdentification
from sparknlp_jsl.utils import *

result_df = dict_to_annotation_converter(spark, list_of_dict)
result_df.select("doc_id", "text","chunk").show(truncate = 100)
```

*Result*:

{:.table-model-big}
|doc_id|       text|               chunk|
|------|-----------|--------------------|
|   1  |My name is George, and I was born on 12/11/1995. I have the pleasure of working at John Snow Labs.|[{chunk, 11, 16, George, {sentence -> 0, chunk -> 0, ner_source -> llm_output, entity -> PERSON, ...|


</div><div class="h3-box" markdown="1">

#### New Blogposts: Identifying Named Entities in Medical Text with Zero-Shot Learning

Explore the latest developments in healthcare NLP through our new blog posts, where we take a deep dive into the innovative technologies and methodologies transforming the medical field. These posts offer insights into how the latest tools are being used to analyze large amounts of unstructured data, identify critical medical assets, and extract meaningful patterns and correlations. Learn how these advances are not only improving our understanding of complex health issues but also contributing to more effective prevention, diagnosis, and treatment strategies.

- [Advanced NLP Techniques: Identifying Named Entities in Medical Text with Zero-Shot Learning](https://medium.com/john-snow-labs/advanced-nlp-techniques-identifying-named-entities-in-medical-text-with-zero-shot-learning-d511e0c3c28d) showcases how the RoBERTaForQuestionAnswering model enables versatile Named Entity Recognition (NER) without the need for extensive domain-specific training. This blog post provides an in-depth look at the ZeroShotNerModel, highlighting its ability to swiftly and efficiently adapt to diverse datasets.

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, and Reliability of Spark NLP for Healthcare

- Enhanced metadata information with the `setMetadataFields` field for `AssertionChunkConverter`
- Added new date format for deidentification
- Added new parameters for the `Replacer` annotator
- Added `document_id` info and confidence scores for `resolutions` and `assertions` fields to the `PipelineOutputParser` module
- Resolved Flattener NullPointerException; if the column is empty, the Flattener returns empty columns instead of throwing an exception.
- Resolved the AssertionMerger loading issue; an exception was thrown when attempting to load the AssertionMerger model.

</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [DocumentFiltererByNER](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/DocumentFiltererByNER.ipynb) MOOC Notebook
- New [LargeFewShotClassifier](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/LargeFewShotClassifierModel.ipynb) MOOC Notebook
- New [Mapper2Chunk](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Mapper2Chunk.ipynb) MOOC Notebook
- Updated [AssertionChunkConverter](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/AssertionChunkConverter.ipynb) MOOC Notebook
- Updated [ContextualAssertion](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/ContextualAssertion.ipynb) MOOC Notebook
- Updated [Replacer](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/Spark_NLP_Udemy_MOOC/Healthcare_NLP/Replacer.ipynb) MOOC Notebook
- Updated [Clinical Entity Resolver](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb) notebook
- Updated [Improved Entity Resolution with SentenceChunkEmbeddings](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.1.Improved_Entity_Resolution_with_SentenceChunkEmbeddings.ipynb) notebook
- Updated [Improved Entity Resolvers in SparkNLP with sBert](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb) notebook
- Updated [Clinical Medication Use Case](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/43.Clinical_Medication_Use_Case.ipynb) notebook
- Updated [Oncology_Model](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb) notebook
- New [Text Classification with LargeFewShotClassifier](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.4.Text_Classification_with_LargeFewShotClassifier.ipynb) Notebook
- New [NER_STIGMATIZATION](https://demo.johnsnowlabs.com/healthcare/NER_STIGMATIZATION/) demo
- Updated [NER_ONCOLOGY_CLINICAL](https://demo.johnsnowlabs.com/healthcare/NER_ONCOLOGY_CLINICAL/) demo

</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.




+ `jsl_meds_ner_q16_v2`
+ `jsl_meds_ner_q8_v2`
+ `jsl_meds_ner_q4_v2`
+ `jsl_meds_rag_q16_v1`
+ `jsl_meds_rag_q8_v1`
+ `jsl_meds_rag_q4_v1`
+ `jsl_medm_q16_v2`
+ `jsl_medm_q8_v2`
+ `jsl_medm_q4_v2`
+ `sbiobertresolve_rxnorm_augmented_v2`
+ `biolordresolve_rxnorm_augmented_v2`
+ `biolordresolve_avg_rxnorm_augmented_v2`
+ `bert_sequence_classifier_metastasis`     
+ `classifierdl_metastasis`
+ `generic_classifier_metastasis`
+ `generic_logreg_classifier_metastasis`
+ `generic_svm_classifier_metastasis`
+ `generic_classifier_oncology`
+ `generic_classifier_therapy`
+ `icd10cm_rxnorm_resolver_pipeline`
+ `icd10cm_resolver_pipeline`
+ `medication_resolver_transform_pipeline`
+ `medication_resolver_pipeline`
+ `rxnorm_resolver_pipeline`
+ `large_fewshot_classifier_ade`
+ `large_fewshot_classifier_age_group`
+ `ner_cancer_types_wip`
+ `ner_stigmatization_wip`
+ `email_matcher`
+ `url_matcher`
+ `ip_matcher`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Versions

</div>
{%- include docs-healthcare-pagination.html -%}