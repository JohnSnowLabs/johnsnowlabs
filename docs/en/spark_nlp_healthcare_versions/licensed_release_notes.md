---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes
permalink: /docs/en/spark_nlp_healthcare_versions/licensed_release_notes
key: docs-licensed-release-notes
modify_date: 2023-12-25
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.2.0

#### Highlights

We are delighted to announce remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first DocumentFiltererByClassifier annotator, RAG with SparkNLP tutorials and well as 5 new clinical pretrained models and pipelines**. Here are the newies in this release:

+ A tutorial to build a Retrieval Augmented Generation (RAG) based clinical chatbot using LLMs with John Snow Labs in Databricks.
+ Clinical document section classifier models to classify the sections within clinical documents.
+ Introducing `DocumentFiltererByClassifier` to filter the documents or document sections using classifier outcomes.
+ New Social Determinants of Health (SDOH) models that are categorizing text, identifying health risks, and recognizing mental health concerns in clinical documents.
+ Robust exception handling to allow skipping the corrupted records processed via `NERConverter`, `ChunkMapperModel`, `DocMapperModel`, `SentenceEntityResolverModel`, `RelationExtractonModel`, `RelationExtractonDLModel` and `AssertionDLModel` annotators.
+ Exploring generative AI applications: RAG-based medical chatbot notebooks in Spark NLP workshop repository.
+ Introducing the `enableSentenceIncrement` parameter in `InternalDocumentSplitter`, offering precise sentence indexing control for streamlined text processing with annotators like sentenceDetector.
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare:
    - `enableSentenceIncrement` parameter in `InternalDocumentSplitter`, offering precise sentence indexing control for streamlined text processing with annotators like SentenceDetector.
    - Enabling `targetEntities` and `entityWeights` parameters in `ChunkEntityEmbeddings`.
    - Refactored `ContextualParserApproach` rules instances for proper integration into LightPipelines.
    - Fixed assertion pre-annotations issue in the NLP Lab module.
    - Deprecated messages deleted: Removed deprecation warning for `confidenceValue` metadata in `ContextualParserApproach` and "deprecation_notice" message in `ChunkMapperModel`.  
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The additions and updates of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

These enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### A tutorial to Build a Retrieval Augmented Generation (RAG) Based Clinical Catbot Using LLMs with John Snow Labs in Databricks

In an era witnessing rapid advancements in Large Language Models (LLMs) and chatbot technologies, this informative session emphasizes the benefits of employing LLM systems based on RAG (Retrieval Augmented Generation). Particularly valuable in scenarios where precision in responses holds significance—such as addressing queries concerning medical patients or clinical protocols—RAG LLMs excel by providing accurate answers while minimizing imaginative outputs. They achieve this by explaining the source of each fact, mitigating errors, and utilizing private documents for information retrieval. Additionally, these systems facilitate near-real-time data updates without necessitating LLM reconfiguration.

This tutorial guides participants through the creation of a RAG Large Language Model (LLM) clinical chatbot system. Leveraging John Snow Labs’ specialized healthcare-oriented LLM and NLP models integrated into the Databricks platform, the system employs LLMs to query a knowledge base via a vector database populated by Healthcare NLP at scale within a Databricks notebook. Utilizing a user-friendly graphical interface, users can engage in productive conversations with the system, thereby enhancing the efficiency and efficacy of healthcare workflows.

Of paramount importance, the system is developed with a focus on data privacy, security, and compliance. It operates entirely within customers’ cloud infrastructure, ensuring zero data sharing and eliminating external API calls, thereby safeguarding sensitive healthcare information.

[Webinar Slides](https://d5ln38p3754yc.cloudfront.net/content_object_shared_files/79064165adfc3626e2872ebb19ab5ed32f1bce8e/Webinar-JSL-Databricks-LangChain_122023.pdf?1702403478)

[Medical Chatbot RAG JohnSnowLabs Databricks notebook link](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/databricks/python/tutorials/healthcare_case_studies/Medical_Chatbot_RAG_JohnSnowLabs_Databricks.ipynb)

[![Building a RAG LLM Clinical Chatbot with John Snow Labs in Databricks](https://i.ytimg.com/vi/Q35kk-9opcw/hqdefault.jpg?sqp=-oaymwE2CPYBEIoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhFIFQoZTAP&rs=AOn4CLAXb9RdAEEa-NJqEw2KeQiFHKngvQ)](https://www.youtube.com/watch?v=Q35kk-9opcw "Click and go to the video")


</div><div class="h3-box" markdown="1">


#### Clinical Document Section Classifier Models to Classify the Sections within Clinical Documents

The latest development introduces two new Section Header Classifier models aimed at leveraging Bert models for the classification of text within clinical documents, focusing on specific sections within the document structure. These models facilitate the categorization of text into distinct sections according to a defined taxonomy, including sections such as **Complications and Risk Factors, Consultation and Referral, Diagnostic and Laboratory Data, Discharge Information, Habits, History, Patient Information, Procedures, Impression, and Others**.

The classifier model has a `headless` version too to cover the use cases in which there is no specific section header included in the section text. This allows classifying the sections even without a major clue (e.g. header, title, etc.) to indicate the section by itself.

These models offer enhanced capabilities to precisely classify clinical document text content into specific sections, aiding in structured information extraction and facilitating streamlined analysis within healthcare and clinical research domains.

| Model Name           |            Predicted Classes              |
|----------------------|-------------------------------------------|
| [`bert_sequence_classifier_clinical_sections`](https://nlp.johnsnowlabs.com/2023/12/21/bert_sequence_classifier_clinical_sections_en.html) | `Complications and Risk Factors`, `Consultation and Referral`, `Diagnostic and Laboratory Data`, `Discharge Information`, `Habits`, `History`, `Patient Information`, `Procedures`, `Impression`, `Other` |
| [`bert_sequence_classifier_clinical_sections_headless`](https://nlp.johnsnowlabs.com/2023/12/21/bert_sequence_classifier_clinical_sections_headless_en.html)   | `Consultation and Referral`, `Habits`, `Complications and Risk Factors`, `Diagnostic and Laboratory Data`, `Discharge Information`, `History`, `Impression`, `Patient Information`, `Procedures`, `Other` |

*Example*:

```python
sequenceClassifier = medical.BertForSequenceClassification\
    .pretrained("bert_sequence_classifier_clinical_sections", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")\
    .setCaseSensitive(False)

text = """
Medical Specialty: Cardiovascular / Pulmonary Sample Name: Aortic Valve Replacement

Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery. (Medical Transcription Sample Report)

DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with congestive heart failure. The patient has diabetes and is morbidly obese.

PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
""""
```

*Result*:

|                                                                       text|                       Classes|
|:--------------------------------------------------------------------------|:-----------------------------|
|         Medical Specialty:\nCardiovascular / Pulmonary\n\nSample Name: Aortic Valve Replacement\n\n|                       History|
|Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery. (Medical Transcription Sample Report)|Complications and Risk Factors|
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with congestive heart failure. The patient has diabetes and is morbidly obese. |Diagnostic and Laboratory Data|
|PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.|                    Procedures|

Please check [Section Header Splitter Demo](https://demo.johnsnowlabs.com/healthcare/SECTION_HEADER/)  and [Section Header Splitting and Classification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/18.1.Section_Header_Splitting_and_Classification.ipynb)


</div><div class="h3-box" markdown="1">


#### Introducing `DocumentFiltererByClassifier` to Filter the Documents or Document Sections Using Classifier Outcomes

The `DocumentFiltererByClassifier` function is designed to filter documents based on the outcomes generated by classifier annotators. It operates using a white list and a black list. The white list comprises classifier results that meet the criteria to pass through the filter, while the black list includes results that are prohibited from passing through. This filtering process is sensitive to cases by default. However, by setting `caseSensitive` to `False`, the filter becomes case-insensitive, allowing for a broader range of matches based on the specified criteria. This function serves as an effective tool for systematically sorting and managing documents based on specific classifier outcomes, facilitating streamlined document handling and organization. Here is an example on how to use this module with `DocumentSplitter` to filter out a specific section/ split based on a classifier.


*Example*:

```python
document_splitter = InternalDocumentSplitter() \
    .setInputCols("document")\
    .setOutputCol("splits")\
    .setSplitMode("recursive")\
    .setChunkSize(100)\
    .setChunkOverlap(3)\
    .setExplodeSplits(True)\
    .setSplitPatterns(["\n\n", "\n"])\

sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained('bert_sequence_classifier_clinical_sections', 'en', 'clinical/models')\
    .setInputCols(["splits", "token"])\
    .setOutputCol("prediction")\
    .setCaseSensitive(False)

document_filterer = DocumentFiltererByClassifier()\
    .setInputCols(["splits", "prediction"])\
    .setOutputCol("filteredDocuments")\
    .setWhiteList(["Diagnostic and Laboratory Data"])\
    .setCaseSensitive(False)
```


*Results before filtering*:

|                                                                          splits|                       classes|
|--------------------------------------------------------------------------------|------------------------------|
|Medical Specialty:\nCardiovascular / Pulmonary\n\nSample Name: Aortic Valve R...|                       History|
|Description: Aortic valve replacement using a mechanical valve and two-vessel...|Complications and Risk Factors|
|                                           (Medical Transcription Sample Report)|Complications and Risk Factors|
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel ...|                    Procedures|
|                 ANESTHESIA: General endotracheal\n\nINCISION: Median sternotomy|                    Procedures|
|INDICATIONS: The patient presented with severe congestive heart failure assoc...|     Consultation and Referral|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|PROCEDURE: The patient was brought to the operating room and placed in supine...|                    Procedures|
|The patient went on cardiopulmonary bypass and the aortic cross-clamp was app...|                    Procedures|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|
|The patient came off cardiopulmonary bypass after aortic cross-clamp was rele...|                    Procedures|

*Results after filtering*:

|                                                                          splits|                       classes|
|--------------------------------------------------------------------------------|------------------------------|
|DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with...|Diagnostic and Laboratory Data|
|FINDINGS: The left ventricle is certainly hypertrophied· The aortic valve lea...|Diagnostic and Laboratory Data|
|The radial artery was used for the left anterior descending artery. Flow was ...|Diagnostic and Laboratory Data|
|The first obtuse marginal artery was a very large target and the vein graft t...|Diagnostic and Laboratory Data|


Please check: [Section_Header_Splitting_and_Classification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/18.1.Section_Header_Splitting_and_Classification.ipynb) for more information


</div><div class="h3-box" markdown="1">


#### New Social Determinants Of Health (SDOH) Models That Are Categorizing Text, Identifying Health Risks And Recognizing Mental Health Concerns In Clinical Documents

These new SDoH models bring in advanced categorization capabilities to assess critical factors affecting individual health.

The models adeptly categorize text, assisting in identifying susceptibility to health risks related to frailty and recognizing mental health concerns within analyzed text data. Consequently, they contribute significantly to a more intricate understanding of how violence and abuse factors influence healthcare outcomes.

These innovative models signify a substantial leap forward in identifying and addressing key social determinants impacting overall health and well-being.


| Model Name           |            Predicted Classes              |
|----------------------|-------------------------------------------|
| [`bert_sequence_classifier_sdoh_violence_abuse`](https://nlp.johnsnowlabs.com/2023/12/20/bert_sequence_classifier_sdoh_violence_abuse_en.html) | `Domestic_Violence_Abuse`, `Personal_Violence_Abuse`, `No_Violence_Abuse`, `Unknown` |
| [`bert_sequence_classifier_sdoh_mental_health`](https://nlp.johnsnowlabs.com/2023/12/20/bert_sequence_classifier_sdoh_mental_health_en.html)   | `Mental_Disorder`, `No_Or_Not_Mentioned` |
| [`bert_sequence_classifier_sdoh_frailty_vulnerability`](https://nlp.johnsnowlabs.com/2023/12/20/bert_sequence_classifier_sdoh_frailty_vulnerability_en.html) |  `Frailty_Vulnerability`, `No_Or_Unknown` |

*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification\
    .pretrained("bert_sequence_classifier_sdoh_violence_abuse", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

sample_texts = [
    ["Repeated visits for fractures, with vague explanations suggesting potential family-related trauma."],
    ["Patient presents with multiple bruises in various stages of healing, suggestive of repeated physical abuse."],
    ["There are no reported instances or documented episodes indicating the patient poses a risk of violence."] ,
    ["Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatment plan that includes surgery, chemotherapy, and radiation therapy."]
]
```


*Result*:

|   text                |      result|
|-----------------------|------------|
|Repeated visits for fractures, with vague explanations suggesting potential family-related trauma.  | Domestic_Violence_Abuse |
|Patient presents with multiple bruises in various stages of healing, suggestive of repeated physi...| Personal_Violence_Abuse |
|There are no reported instances or documented episodes indicating the patient poses a risk of vio...|       No_Violence_Abuse |
|Patient B is a 40-year-old female who was diagnosed with breast cancer. She has received a treatm...|                 Unknown |


Please check [SOCIAL DETERMINANT CLASSIFICATION Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/)


</div><div class="h3-box" markdown="1">

#### Robust Exception Handling To Allow Skipping The Corrupted Records Processed Via `NERConverter`, `ChunkMapperModel`, `DocMapperModel`, `SentenceEntityResolverModel`, `RelationExtractonModel`, `RelationExtractonDLModel` and `AssertionDLModel` Annotators

We added `doExceptionHandling` parameter into `NERConverterInternal`, `ChunkMapperModel`, `DocMapperModel`, `SentenceEntityResolverModel`, `RelationExtractonModel`, `RelationExtractonDLModel` and  `AssertionDLModel` annotators for a robust exception handling if the process is broken down due to corrupted inputs. If it is set as `True`, the annotator tries to process as usual and ff exception-causing data (e.g. corrupted record/ document) is passed to the annotator, an exception warning is emitted which has the exception message. **Processing continues with the next one** while the rest of the drecords within the same batch is parsed without interruption. The default behavious is `False` and will throw exception and break the process to inform users.

*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")\
    .setDoExceptionHandling(True)
```

</div><div class="h3-box" markdown="1">

#### Exploring Generative AI Applications: RAG-Based Medical Chatbot Notebooks in Spark NLP Workshop Repository

Within the workshop repository of Spark NLP, a new dedicated folder for generative AI notebook examples has been introduced at [generative-ai](https://github.com/JohnSnowLabs/spark-nlp-workshop/tree/master/generative-ai). This repository section hosts two notable notebooks:

- [Medical Chatbot RAG JohnSnowLabs LangChain Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/generative-ai/Medical_Chatbot_RAG_JohnSnowLabs_LangChain.ipynb): This notebook delves into the application of Retrieval Augmented Generation (RAG) in developing a medical chatbot. Leveraging John Snow Labs' LangChain, this notebook explores the implementation and functionalities of RAG technology in healthcare contexts.

- [Medical Chatbot RAG JohnSnowLabs Haystack Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/generative-ai/Medical_Chatbot_RAG_JohnSnowLabs_Haystack.ipynb): Another notebook dedicated to RAG-based medical chatbot development within the John Snow Labs ecosystem, this time utilizing Haystack. The notebook likely offers unique insights and approaches to creating medical chatbots using RAG within the John Snow Labs' framework.

These notebooks provide valuable resources for individuals interested in understanding and implementing RAG-based generative AI specifically tailored for medical chatbot applications.


</div><div class="h3-box" markdown="1">

#### Introducing The `enableSentenceIncrement` Parameter In `InternalDocumentSplitter`, Offering Precise Sentence Indexing Control For Streamlined Text Processing With Annotators Like `SentenceDetector`

The `enableSentenceIncrement` parameter holds significance as it directly influences the management of sentence indexing within the document splitting process. By regulating this feature, users gain more precise control over sentence index increments in metadata. This functionality is particularly valuable when employing split documents in subsequent annotators, such as the `SentenceDetector`, ensuring accurate and streamlined processing of text data.

*Example*:

```python
document_splitter = InternalDocumentSplitter() \
    .setInputCols(["document", "sentence"]) \
    .setOutputCol("splits") \
    .setSplitMode("sentence") \
    .setMaxLength(2)\
    .setExplodeSplits(True)\
    .setEnableSentenceIncrement(True)

sample_text = """Sample Name: Aortic Valve Replacement
Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
(Medical Transcription Sample Report)
DIAGNOSIS: Aortic valve stenosis with coronary artery disease associated with congestive heart failure. The patient has diabetes and is morbidly obese.
PROCEDURES: Aortic valve replacement using a mechanical valve and two-vessel coronary artery bypass grafting procedure using saphenous vein graft to the first obtuse marginal artery and left radial artery graft to the left anterior descending artery.
"""
```

*Result*:

|metadata                                 | result       |
|:----------------------------------------|:-------------|
| {id -> 0, sentence -> 0, document -> 0} |Description: Aortic valve replacement using a mechanical valve and two-vessel coronary artery byp...|
| {id -> 0, sentence -> 1, document -> 1} |The patient has diabetes and is morbidly obese.\nANESTHESIA: General endotracheal\nINCISION: Medi...|
| {id -> 0, sentence -> 2, document -> 2} |INDICATIONS: The patient presented with severe congestive heart failure associated with the patie...|
| {id -> 0, sentence -> 3, document -> 3} |In addition, The patient had significant coronary artery disease consisting of a chronically occl...|
| {id -> 0, sentence -> 4, document -> 4} |It was decided to perform a valve replacement as well as coronary artery bypass grafting procedur...|
| {id -> 0, sentence -> 5, document -> 5} |It is a tricuspid type of valve. The coronary artery consists of a large left anterior descending...|

Please check: [Internal Document Splitter Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/38.InternalDocumentSplitter.ipynb) for more information



</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

+ Enabling `targetEntities` and `entityWeights` parameters in `ChunkEntityEmbeddings`
+ Refactored `ContextualParserApproach` rules instances for proper integration into LightPipelines
+ Fixed assertion pre-annotations issue in the ALAB module
+ Deprecated Messages Deletion: Removed deprecation warning for confidenceValue metadata in `ContextualParserApproach` and "deprecation_notice" message in `ChunkMapperModel`  


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Medical Chatbot RAG JohnSnowLabs LangChain Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/generative-ai/Medical_Chatbot_RAG_JohnSnowLabs_LangChain.ipynb)
- New [Medical Chatbot RAG JohnSnowLabs Haystack Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/generative-ai/Medical_Chatbot_RAG_JohnSnowLabs_Haystack.ipynb)
- New [Section Header Splitting and Classification Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/18.1.Section_Header_Splitting_and_Classification.ipynb)
- Updated [Clinical Entity Resolvers Notebook](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb) with new examples
- New [Section Header Splitter Demo](https://demo.johnsnowlabs.com/healthcare/SECTION_HEADER/)
- Updated [Social Determinant Classification Demo](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_SEQUENCE_CLASSIFICATION/)


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `bert_sequence_classifier_sdoh_violence_abuse`
+ `bert_sequence_classifier_sdoh_mental_health`
+ `bert_sequence_classifier_sdoh_frailty_vulnerability`
+ `bert_sequence_classifier_clinical_sections`
+ `bert_sequence_classifier_clinical_sections_headless`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">



## Previous versions

</div>
{%- include docs-healthcare-pagination.html -%}
