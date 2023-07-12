---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 5.0.0
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_5_5_5
key: docs-licensed-release-notes
modify_date: 2023-07-12
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">

## 5.0.0

#### Highlights

We are delighted to announce a suite of remarkable enhancements and updates in our latest release of Spark NLP for Healthcare. **This release comes with the first Few Shot Text Classifier module and ONNX-optimized sBioBert sentence embeddings as well as 21 new clinical pretrained models and pipelines**. It is a testament to our commitment to continuously innovate and improve, furnishing you with a more sophisticated and powerful toolkit for healthcare natural language processing.

+ Introducing the very first Few Shot Classifier model to our toolkit to train classifier models with limited labeled data.
+ New ONNX Sentence BioBERT Embeddings model, designed to enhance performance and accuracy
+ 2 New Medical Question Answering models based on SOTA LLMs, designed to provide accurate answers to your inquiries against clinical notes
+ 7 new NER models for Social Determinants of Health(SDOH), broadening our ability to identify and analyze crucial factors that impact health outcomes.
+ New profiling pipelines for Social Determinants Of Health (SDOH), Voice Of The Patient (VOP), and Oncology to run multiple models at once in a single line
+ New clinical multi-class classifier models for classification of articles based on cancer hallmarks and Covid-19 topics   
+ New Patient Urgency Text Classifier model, designed to analyze the level of emergency in medical situations requiring immediate assistance
+ Brand-new Dutch clinical NER models, empowering accurate recognition and extraction of clinical entities in Dutch language
+ New German sentence entity resolver model exclusively tailored for ICD-10-GM codes
+ New feature to `InternalResourceDownloader` for point cache folder
+ `UpdateModels` is now more flexible and can be used to update existing models in the cache folder
+ New feature for `ChunkFilterer` to enable filtering chunks according to confidence thresholds
+ New feature for `StructuredDeidentification` to make it flexible for different languages
+ Enhanced ALAB module with Relation Extraction model training data preparation ability using document-level annotations
+ Various core improvements; bug fixes, enhanced overall robustness and reliability of Spark NLP for Healthcare
  - Improved Deidentification performance with refactoring
  - Updated `clinical_deidentification` pipeline by enhancing the `AGE` entity extraction capability
  - Minor corrections have been made to the calculation formulas in the Medicare Risk Adjustment Module
+ Updated notebooks and demonstrations for making Spark NLP for Healthcare easier to navigate and understand
+ The addition and update of numerous new clinical models and pipelines continue to reinforce our offering in the healthcare domain

We believe that these enhancements will elevate your experience with Spark NLP for Healthcare, enabling more efficient, accurate, and streamlined analysis of healthcare-related natural language data.


</div><div class="h3-box" markdown="1">

#### Introducing The Very First Few Shot Classifier Model To Our Toolkit To Train Classifier Models With Limited Labeled Data

The `FewShotClassifierApproach` and `FewShotClassifierModel` annotators are new additions to the set of annotators available in the Spark NLP for Healthcare library. These annotators specifically target few-shot classification tasks, which involve training a model to make accurate predictions with limited labeled data.

These new annotators provide a valuable capability for handling scenarios where labeled data is scarce or expensive to obtain. By effectively utilizing limited labeled examples, the few-shot classification approach enables the creation of models that can generalize and classify new instances accurately, even with minimal training data.

In our experiment, we compared the Few-Shot Classifier trained on partial data, equivalent to 40% of our entire dataset, against the ClassifierDL trained on both full (80% of the dataset) and partial data. To maintain fairness, the test set was constant at 20% of the entire dataset for all cases, and the same sentence embeddings were employed across the board. The Few-Shot Classifier achieved a macro F1 score of 0.867, outperforming outperform that of the ClassifierDL using the full dataset, which scored a macro F1 score of 0.847. The ClassifierDL using partial data also showed comparable results to its full data counterpart, demonstrating its robustness with less training data, but it was still surpassed by the Few-Shot Classifier. This superior performance from the Few-Shot Classifier with less data signifies that it is highly efficient and effective, making it an excellent choice for scenarios where data scarcity is a concern. We're excited to see how this innovative feature will enhance the future of text classification tasks in our library. Stay tuned for more updates as we continue to optimize and improve our offerings.

|                           | macro-f1-score | weighted-f1-score | accuracy  |
|---------------------------|----------------|-------------------|-----------|
| ClassifierDL_full_Data    | 0.85       | 0.84        | 0.84  |
| ClassifierDL_partial_Data | 0.84       | 0.84        | 0.84  |
| FewShot_partial_Data      | 0.87       | 0.87        | 0.87  |

The `FewShotClassifier` is designed to process sentence embeddings as input. It generates category annotations, providing labels along with confidence scores that range from 0 to 1. Input annotation types supported by this model include `SENTENCE_EMBEDDINGS`, while the output annotation type is `CATEGORY`.


*Example*:

```python

few_shot_approach = FewShotClassifierApproach()\
    .setLabelColumn("label")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("prediction")\
    .setModelFile(f"/tmp/log_reg_graph.pb")\
    .setEpochsNumber(10)\
    .setBatchSize(1)\
    .setLearningRate(0.001)

pipeline = Pipeline(
    stages=[
        document_asm,
        sentence_embeddings,
        graph_builder,
        few_shot_approach
    ])


data = [
    ["ADE_positive", 'Both PAN and methotrexate have been independently demonstrated to cause sensorineural hearing loss.'],
    ["ADE_positive", 'Adrenal suppression in a fetus due to administration of methylprednisolone has hitherto been rarely published.'],
    ["ADE_negative", 'Pathogenic mechanisms for the development of pseudomembranous colitis and the epidemiology of this condition in patients with AIDS are discussed.'],
    ["ADE_negative", 'I report a patient who developed the syndrome during treatment for schizophrenia with the antipsychotic agent molindone hydrochloride.']
]

model = pipeline.fit(train_data)

tests = [
    'Bleomycin pneumonitis potentiated by oxygen administration.',
    'Enzymes derived from two different bacterial sources (Escherichia coli and Erwinia carotovora) are in common use.',
]
```


*Result*:

text          |prediction category      
--------------|--------------------
Bleomycin pneumonitis potentiated by oxygen administration.    | ADE_positive
Enzymes derived from two different bacterial sources (Escherichia coli and Erwinia carotovora) are in common use. | ADE_negative


please check: [Text Classification with FewShotClassifier Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.3.Text_Classification_with_FewShotClassifier.ipynb) for more information


</div><div class="h3-box" markdown="1">

#### New ONNX Sentence BioBERT Embeddings Model, Designed To Enhance Performance And Accuracy

Spark NLP 5.0.0 introduced support for ONNX Runtime that can handle machine learning models in the ONNX format and has been proven to significantly boost inference performance across a multitude of models. This integration leads to substantial improvements when serving our LLM models, including BERT. We now introduce the first medical sentence embeddings, that is called  `sbiobert_base_cased_mli_onnx` and optimized with ONNX, generating two times faster inference.

*Example*:

```python
sbiobert_embeddings = BertSentenceEmbeddings\
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")
```

*Result*:

```bash
Gives a 768 dimensional vector representation of the sentence.
```
Please see the [model card](https://nlp.johnsnowlabs.com/2023/07/11/sbiobert_base_cased_mli_onnx_en.html)



</div><div class="h3-box" markdown="1">

#### 2 New Medical Question Answering Models Based On SOTA LLMs, Designed To Provide Accurate Answers To Your Inquiries Against Clinical Notes
Now we have [`clinical_notes_qa_base`](https://nlp.johnsnowlabs.com/2023/07/06/clinical_notes_qa_base_en.html) and [`clinical_notes_qa_large`](https://nlp.johnsnowlabs.com/2023/07/06/clinical_notes_qa_large_en.html) models that are capable of open-book question answering on Medical Notes.

These new medical question answering models empower users to extract valuable information and insights from medical notes effectively. Whether you are a healthcare professional, researcher, or enthusiast, the `clinical_notes_qa_base` and `clinical_notes_qa_large` models offer advanced tools for retrieving targeted information from medical documents and enhancing your understanding of the medical domain.

*Example*:

```python
med_qa  = sparknlp_jsl.annotators.MedicalQuestionAnswering()\
    .pretrained("clinical_notes_qa_base", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setCustomPrompt("Context: {context} \n Question: {question} \n Answer: ")\
    .setOutputCol("answer")\

note_text = """Patient with a past medical history of hypertension for 15 years.\n(Medical Transcription Sample Report)\nHISTORY OF PRESENT ILLNESS:\nThe patient is a 74-year-old white woman who has a past medical history of hypertension for 15 years, history of CVA with no residual hemiparesis and uterine cancer with pulmonary metastases, who presented for evaluation of recent worsening of the hypertension. According to the patient, she had stable blood pressure for the past 12-15 years on 10 mg of lisinopril."""

question = "What is the primary issue reported by patient?"

```

*Result*:

```
"The primary issue reported by the patient is hypertension."
```
please check: [MEDICAL LLM Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/) 


</div><div class="h3-box" markdown="1">

#### 7 New NER Models For Social Determinants Of Health (SDOH), Broadening Our Ability To Identify And Analyze Crucial Factors That Impact Health Outcomes

Introducing our new set of SDOH NER models that are specifically designed to identify and extract entities related to various social determinants of health. Here is a brief overview of each model and the entities it predicts:

**model name** | **description** | **predicted entities**   
---------------------------------|-----------------|-----------------------
[ner_sdoh_access_to_healthcare](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_access_to_healthcare_en.html)| extract entities related to access to healthcare | `Access_To_Care`, `Healthcare_Institution`, `Insurance_Status`                                                 
[ner_sdoh_community_condition](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_community_condition_en.html) | identify and extract entities associated with different community conditions | `Community_Safety`, `Environmental_Condition`, `Food_Insecurity`, `Housing`, `Transportation`                 
[ner_sdoh_demographics](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_demographics_en.html)       | extract entities associated with different demographic factors | `Age`, `Family_Member`, `Gender`, `Geographic_Entity`, `Language`, `Race_Ethnicity`, `Spiritual_Beliefs`
[ner_sdoh_health_behaviours_problems](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_health_behaviours_problems_en.html) | extract entities associated with health behaviors and problems | `Communicable_Disease`, `Diet`, `Disability`, `Eating_Disorder`, `Exercise`, `Hyperlipidemia`, `Hypertension`, `Mental_Health`, `Obesity`, `Other_Disease`, `Quality_Of_Life`, `Sexual_Activity`
[ner_sdoh_income_social_status](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_income_social_status_en.html) | extract entities associated with income and social status | `Education`, `Employment`, `Financial_Status`, `Income`, `Marital_Status`, `Population_Group`
[ner_sdoh_social_environment](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_social_environment_en.html) | extract entities associated with different aspects of the social environment | `Chidhood_Event`, `Legal_Issues`, `Social_Exclusion`, `Social_Support`, `Violence_Or_Abuse`
[ner_sdoh_substance_usage](https://nlp.johnsnowlabs.com/2023/07/02/ner_sdoh_substance_usage_en.html) |  extract entities associated with substance usage | `Alcohol`, `Smoking`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Substance_Use`


*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_sdoh_health_behaviours_problems", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

sample_text = """The patient is a 54-year-old female with a complex medical history, including anxiety, depression, bulimia nervosa, elevated cholesterol, substance abuse, hypertension, and hyperlipidemia. Her partner has been diagnosed with hepatitis C.  She reports a lack of regular exercise and a departure from a healthy diet for approximately two years due to chronic sciatic pain. Her sedentary lifestyle and poor diet have contributed to obesity, leading to a negative impact on her self-esteem.  The patient is motivated to make lifestyle improvements, including weight loss, addressing her mental well-being, and enhancing her sexual satisfaction."""
```

*Result*:

|chunk                 |begin|end|ner_label           |
|----------------------|-----|---|--------------------|
|anxiety               |78   |84 |Mental_Health       |
|depression            |87   |96 |Mental_Health       |
|bulimia nervosa       |99   |113|Eating_Disorder     |
|elevated cholesterol  |116  |135|Hyperlipidemia      |
|hypertension          |155  |166|Hypertension        |
|hyperlipidemia        |173  |186|Hyperlipidemia      |
|hepatitis C           |225  |235|Communicable_Disease|
|regular exercise      |261  |276|Exercise            |
|healthy diet          |301  |312|Diet                |
|chronic sciatic pain  |349  |368|Other_Disease       |
|sedentary lifestyle   |375  |393|Exercise            |
|poor diet             |399  |407|Diet                |
|obesity               |429  |435|Obesity             |
|self-esteem           |474  |484|Quality_Of_Life     |
|lifestyle improvements|521  |542|Quality_Of_Life     |
|mental well-being     |583  |599|Mental_Health       |
|sexual satisfaction   |620  |638|Sexual_Activity     |


please check [Social Determinant of Health Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Model.ipynb)  for more information


</div><div class="h3-box" markdown="1">

#### New Profiling Pipelines For Social Determinants Of Health (SDOH), Voice Of The Patient (VOP), and Oncology To Run Multiple Models At Once In A Single Line


We are excited to introduce our new profiling pipelines that focus on Social Determinants of Health (SDOH), Voice of Patient (VOP), and Oncology domains. We can use pretrained NER profiling pipelines for exploring all the available pretrained NER models at once. These profiling pipelines offer powerful tools for extracting meaningful information from medical text data in the respective domains. They assist in uncovering patterns, trends, and insights that are crucial for research, analysis, and decision-making in healthcare and related fields. Here's a brief overview of each pipeline and the included NER  models:

**Pipeline Name**      |  **included NER Models**
-----------------------|--------------------
[ner_profiling_oncology](https://nlp.johnsnowlabs.com/2023/07/03/ner_profiling_oncology_en.html) |  `ner_oncology_unspecific_posology`, `ner_oncology_tnm`, `ner_oncology_therapy`, `ner_oncology_test`, `ner_oncology_response_to_treatment`, `ner_oncology_posology`, `ner_oncology`, `ner_oncology_limited_80p_for_benchmarks`, `ner_oncology_diagnosis`, `ner_oncology_demographics`, `ner_oncology_biomarker`, `ner_oncology_anatomy_granular`, `ner_oncology_anatomy_general`
[ner_profiling_sdoh](https://nlp.johnsnowlabs.com/2023/07/11/ner_profiling_sdoh_en.html)     | `ner_sdoh`, `ner_sdoh_social_environment_wip`, `ner_sdoh_mentions`, `ner_sdoh_demographics`, `ner_sdoh_community_condition`, `ner_sdoh_substance_usage`, `ner_sdoh_access_to_healthcare`, `ner_sdoh_health_behaviours_problems`, `ner_sdoh_income_social_status`
[ner_profiling_vop](https://nlp.johnsnowlabs.com/2023/07/03/ner_profiling_vop_en.html)      | `ner_vop_clinical_dept`, `ner_vop_temporal`, `ner_vop_test`, `ner_vop`, `ner_vop_problem`, `ner_vop_problem_reduced`, `ner_vop_treatment`, `ner_vop_demographic`, `ner_vop_anatomy`



*Example*:

```python
from sparknlp.pretrained import PretrainedPipeline

ner_profiling_pipeline = PretrainedPipeline("ner_profiling_oncology", 'en', 'clinical/models')

```

For results and different examples, please see 
-   [Voice of Patient Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/35.Voice_of_Patient_Model.ipynb)
-   [Social Determinant of Health Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Model.ipynb)  
-   [Oncology Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb)



</div><div class="h3-box" markdown="1">

#### New Clinical Multi-Class Classifier Models for Classification Of Articles Based On Cancer Hallmarks And Covid-19 Topics

We are pleased to introduce our two new multi-classifier models. Here's a brief overview of each model and the entities they predict:

**model name**  | **description**    | **predicted entities**
----------------|--------------------|-----------------------
[multiclassifierdl_hoc](https://nlp.johnsnowlabs.com/2023/07/04/multiclassifierdl_hoc_en.html)    | This model makes a semantic classification of the article according to the hallmarks of cancer based on its abstract | `Activating_Invasion_And_Metastasis`, `Avoiding_Immune_Destruction`, `Cellular_Energetics`, `Enabling_Replicative_Immortality`, `Evading_Growth_Suppressors`, `Genomic_Instability_And_Mutation`, `Inducing_Angiogenesis`, `Resisting_Cell_Death`, `Sustaining_Proliferative_Signaling`, `Tumor_Promoting_Inflammation`
[multiclassifierdl_litcovid](https://nlp.johnsnowlabs.com/2023/07/04/multiclassifierdl_litcovid_en.html) | This model determines the relevant COVID-19 topics of the article based on its abstract.   | `Mechanism`, `Transmission`, `Diagnosis`, `Treatment`, `Prevention`, `Case_Report`, `Epidemic_Forecasting`

These multi-classifier models enhance the classification and analysis of articles by providing predictions related to specific domains. They facilitate efficient information retrieval and assist researchers and practitioners in quickly identifying articles relevant to cancer hallmarks or specific COVID-19 topics based on abstract content

*Example*:

```python
multi_classifier_dl = MultiClassifierDLModel.pretrained("multiclassifierdl_litcovid", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("category")

text = """Low level of plasminogen increases risk for mortality in COVID-19 patients. The pathophysiology of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), and especially of its complications is still not fully understood. In fact, a very high number of patients with COVID-19 die because of thromboembolic causes. A role of plasminogen, as precursor of fibrinolysis, has been hypothesized. In this study, we aimed to investigate the association between plasminogen levels and COVID-19-related outcomes in a population of 55 infected Caucasian patients (mean age: 69.8 +/- 14.3, 41.8% female). Low levels of plasminogen were significantly associated with inflammatory markers (CRP, PCT, and IL-6), markers of coagulation (D-dimer, INR, and APTT), and markers of organ dysfunctions (high fasting blood glucose and decrease in the glomerular filtration rate). A multidimensional analysis model, including the correlation of the expression of coagulation with inflammatory parameters, indicated that plasminogen tended to cluster together with IL-6, hence suggesting a common pathway of activation during disease's complication. Moreover, low levels of plasminogen strongly correlated with mortality in COVID-19 patients even after multiple adjustments for presence of confounding. These data suggest that plasminogen may play a pivotal role in controlling the complex mechanisms beyond the COVID-19 complications, and may be useful both as biomarker for prognosis and for therapeutic target against this extremely aggressive infection."""
```

*Result*:

|  text|   result|
|------|---------|
|Low level of plasminogen increases risk for mortality in COVID-19 patients. The pathophysiology of coronavirus diseas...|[Mechanism, Treatment, Diagnosis]|




</div><div class="h3-box" markdown="1">

#### New Patient Urgency Text Classifier Model, Designed To Analyze The Level Of Emergency In Medical Situations Requiring Immediate Assistance

The Patient Urgency Text Classifier model is designed to analyze the level of emergency in medical situations that demand immediate assistance from medical organizations.

[`bert_sequence_classifier_patient_urgency`](https://nlp.johnsnowlabs.com/2023/07/09/bert_sequence_classifier_patient_urgency_en.html): This model has undergone training using a dataset of emergency calls, which have been labeled with three distinct classes (`High`, `Medium`, `Low`).

*Example*:

```python
sequenceClassifier = MedicalBertForSequenceClassification.pretrained("bert_sequence_classifier_patient_urgency", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("prediction")

sample_text_list = [
    "I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s slurring his speech. He is breathing, but it’s really ragged. And, he is not responding when I talk to him…he seems out of it.",
    "My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and cannot move.",
    "My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke up in pain and is having a hard time moving around. The pain is around the surgery area. It is not severe, but it’s making her uncomfortable. She does not have fever, nausea or vomiting. There’s some slight feeling of being bloated."
]
```

*Result*:

|text|  result|
|--------|--------|
|I think my father is having a stroke. His face is drooping, he can’t move his right side and he’s...|   High |
|My old neighbor has fallen and cannot get up. She is conscious, but she is in a lot of pain and c...| Medium |
|My wife has been in pain all morning. She had an operation a few days ago. This morning, she woke...|  Low |


</div><div class="h3-box" markdown="1">

#### Brand-new Dutch Clinical NER Models, Empowering Accurate Recognition And Extraction Of Clinical Entities In Dutch Language

[`ner_clinical`](https://nlp.johnsnowlabs.com/2023/07/05/ner_clinical_nl.html) and [`bert_token_classifier_ner_clinical`](https://nlp.johnsnowlabs.com/2023/07/05/bert_token_classifier_ner_clinical_nl.html): These two Dutch clinical NER models provide valuable tools for processing and analyzing Dutch clinical texts. They assist in automating the extraction of important clinical information, facilitating research, medical documentation, and other applications within the Dutch healthcare domain.


*Example*:

```python
ner_model = MedicalNerModel.pretrained("ner_clinical", "nl", "clinical/models")\
  .setInputCols(["sentence", "token", "embeddings"])\
  .setOutputCol("ner")

text = """Dhr. Van Dijk, 58 jaar oud, kwam naar de kliniek met klachten van aanhoudende hoest, koorts en kortademigheid. We hebben besloten om een röntgenfoto van de borst, bloedonderzoek en een CT-scan te laten uitvoeren. De resultaten wezen op een ernstige longontsteking, een verhoogd aantal witte bloedcellen en mogelijk COPD. Hem is een antibiotica kuur en een sterke hoestsiroop voorgeschreven. Daarnaast adviseren we hem een voedzaam dieet te volgen."""
```

*Result*:

|chunk                                |begin|end|ner_label|confidence|
|-------------------------------------|-----|---|---------|----------|
|aanhoudende hoest                    |66   |82 |PROBLEM  |0.82    |
|koorts                               |85   |90 |PROBLEM  |0.99    |
|kortademigheid                       |95   |108|PROBLEM  |0.99    |
|röntgenfoto van de borst             |137  |160|TEST     |0.61    |
|bloedonderzoek                       |163  |176|TEST     |0.92    |
|een CT-scan                          |181  |191|TEST     |0.73    |
|ernstige longontsteking              |240  |262|PROBLEM  |0.78    |
|een verhoogd aantal witte bloedcellen|265  |301|PROBLEM  |0.45    |
|COPD                                 |315  |318|PROBLEM  |0.98    |
|antibiotica kuur                     |332  |347|TREATMENT|0.63    |
|een sterke hoestsiroop               |352  |373|TREATMENT|0.47    |
|een voedzaam dieet                   |418  |435|TREATMENT|0.69    |



</div><div class="h3-box" markdown="1">

#### New German Sentence Entity Resolver Model Exclusively Tailored For ICD-10-GM Codes


[`robertaresolve_icd10gm`](https://nlp.johnsnowlabs.com/2023/06/30/robertaresolve_icd10gm_de.html): This model maps extracted medical entities to ICD10-GM codes for the German language using `xlmroberta_embeddings_paraphrase_mpnet_base_v2` embeddings.

With this German Sentence Entity Resolver, you can efficiently analyze German medical texts and obtain the relevant ICD-10-GM codes associated with the extracted medical entities. This enables precise categorization and classification of medical data, enhancing medical research, coding, and analysis in the German healthcare domain.

*Example*:

```python
icd10gm_resolver = SentenceEntityResolverModel.pretrained("robertaresolve_icd10gm", "de", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("icd10gm_code")

text = ["Dyspnoe", "Lymphknoten"]
```

*Result*:

| chunks  | code    | resolutions   | all_codes     | all_distances   |
|:--------|:--------|:-------------:|--------------:|:----------------|
| Dyspnoe | R06.0   |Dyspnoe:::Dysphagie:::Dysurie...| R06.0:::R13:::R30.0... | 0.00:::1.09:::1.17... |
| Lymphknoten|D36.0 |Lymphknoten:::Lymphknotenvergrößerung...| D36.0:::R59:::Q82.0... | 0.00:::0.04:::0.12... |




</div><div class="h3-box" markdown="1">

#### New Feature To `InternalResourceDownloader` To Point Cache Folder

By setting the `cache_folder_path`, you can control where the downloaded resources are stored, enabling easy access and reuse of the downloaded models in subsequent operations or workflows.

*Example*:

```python
from sparknlp_jsl.pretrained import InternalResourceDownloader

#The first argument is the path to the zip file and the second one is the folder.
InternalResourceDownloader.downloadModelDirectly("clinical/models/ner_clinical_large_en_2.5.0_2.4_1590021302624.zip",
                                                 "clinical/models",
                                                 unzip=False,
                                                 cache_folder_path="/content")
```


</div><div class="h3-box" markdown="1">

#### `UpdateModels` Is Now More Flexible And Can Be Used To Update Existing Models In The Cache Folder

`UpdateModels` is a helper class that provides functionality to update existing pretrained models located in the cache folder. It offers two main methods: `updateCacheModels` and `updateModels`.

`UpdateModels.updateCacheModels(cache_folder='')`: This method refreshes all the pretrained models located in the cache pretrained folder.

`UpdateModels.updateModels()`: This method downloads all the new pretrained models that have been released since the specified date interval.

- `model_names`: A list of names of the models to be downloaded.
- `language`: The language of the models, with a default value of "en".
- `start_date`: The starting date used to filter the models, in the format "yyyy-MM-dd".
- `end_date`: The ending date used to filter the models, in the format "yyyy-MM-dd".
- `cache_folder`: The path indicating where the models will be downloaded and stored.

*Example*:

```python
from sparknlp_jsl.updateModels import UpdateModels

UpdateModels.updateModels(start_date = "2021-01-01",
                          end_date = "2023-07-07",
                          model_names=["ner_clinical","ner_jsl"],
                          language="en",
                          remote_loc="clinical/models",
                          cache_folder="/content/jsl_models"
                          )

ls /content/jsl_models/
```

*Result*:

```
ner_clinical_en_3.0.0_3.0_1617208419368/  
ner_jsl_en_4.2.0_3.0_1666181370373/
```



</div><div class="h3-box" markdown="1">

#### New Feature For `ChunkFilterer` To Enable Filtering Chunks According To Confidence Thresholds

We have added a new `setEntitiesConfidence` parameter to `ChunkFilterer` annotator that enables filtering the chunks according to the confidence thresholds. The only thing you need to do is provide a dictionary that has the NER labels as keys and the confidence thresholds as values.

*Example*:

```python
posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("posology_ner_chunk")

chunk_filterer = ChunkFilterer()\
    .setInputCols("sentence","posology_ner_chunk")\
    .setOutputCol("chunk_filtered")\
    .setFilterEntity("entity")\
    .setEntitiesConfidence({"DRUG":0.9,
                            "FREQUENCY":0.9,
                            "DOSAGE":0.9,
                            "DURATION":0.9,
                            "STRENGTH":0.9})


sample_text = 'The patient was prescribed 1 capsule of Advil for 5 days. He was seen by the endocrinology service and she was discharged on 40 units of insulin glargine at night.'  
```

*Detected chunks*:

|sentence_id |chunks	       |entities  |confidence |
|------------|-----------------|----------|-----------|
|0     	     |1                |DOSAGE    |0.99 |
|0	         |capsule          |FORM      |0.99 |
|0	         |Advil	           |DRUG      |0.99 |
|0	         |for 5 days       |DURATION  |0.71 |
|1    	     |40 units	       |DOSAGE	  |0.85 |
|1           |insulin glargine |DRUG      |0.83 |
|1	         |at night         |FREQUENCY |0.81  |

*Filtered by confidence scores*:

|sentence_id |chunks    |entitie  |confidence |
|------------|----------|---------|-----------|
|0     	     |1         |DOSAGE   |0.99 |
|0	         |capsule   |FORM     |0.99 |
|0	         |Advil	    |DRUG     |0.99 |



</div><div class="h3-box" markdown="1">

####  New Feature For `StructuredDeidentification` To Make It Flexible For Different Languages

The new language feature added to `StructuredDeidentification` enhances its flexibility by supporting different languages for deidentification tasks.

*Example*:

```python
from sparknlp_jsl.structured_deidentification import StructuredDeidentification

obfuscator = StructuredDeidentification(spark,
                                        {"NAME":"PATIENT",
                                         "AGE":"AGE",
                                         "ADDRESS":"LOCATION",
                                         "DOB":"DATE"},
                                        obfuscateRefSource = "faker",
                                        language="de")

obfuscator_df = obfuscator.obfuscateColumns(df)
```

*Original Dataframe*:

|NAME           |DOB       |AGE|ADDRESS                                |
|---------------|----------|---|---------------------------------------|
|Cecilia Chapman|04/02/1935|83 |711-2880 Nulla St. Mankato Mississippi |
|Iris Watson    |03/10/2009|9  |283 8562 Fusce Rd. Frederick Nebraska  |
|Bryar Pitts    |11/01/1921|98 |5543 Aliquet St. Fort Dodge GA         |
|Theodore Lowe  |13/02/2002|16 |Ap #867-859 Sit Rd. Azusa New York     |
|Calista Wise   |20/08/1942|76 |7292 Dictum Av. San Antonio MI         |


*Obfuscated Result*:

|NAME                 |DOB         |AGE  |ADDRESS                       |
|---------------------|------------|-----|------------------------------|
| Giesela Janzen      | 19/03/1935 | 86  | Annie-Lübs-Platz 8/0         |
| Folker Sonntag      | 30/10/2009 | 5   | Georg-Albers-Platz 8/7       |
| Matthäus Koch       | 13/02/1921 | 99  | Annelore-Schmidt-Straße 6/2  |
| Elly Metz           | 23/03/2002 | 17  | Klemens-Thanel-Straße 4      |
| Friederike Heinrich | 30/09/1942 | 75  | Rita-Süßebier-Weg 550        |



</div><div class="h3-box" markdown="1">

#### Enhanced ALAB Module With Relation Extraction Model Training Data Preparation Ability Using Document-Level Annotations

In order to facilitate the preparation of document-level annotated data for training Relation Extraction models, we have introduced a new parameter called `doc_wise_annot` to the `get_relation_extraction_data` method in the ALAB module. By setting the `doc_wise_annot` parameter to `True`, the method will return the dataframe with sentence-cross annotations, if they exist. The default value is `False`.

*Example*:

```python
alab.get_relation_extraction_data(
    spark=spark,
    input_json_path='alab_demo.json',
    ground_truth=True,
    ...
    doc_wise_annot=True
)
```

</div><div class="h3-box" markdown="1">

#### Various Core Improvements: Bug Fixes, Enhanced Overall Robustness, And Reliability Of Spark NLP For Healthcare

- Improved Deidentification performance with refactoring
- Updated `clinical_deidentification` pipeline by enhancing the `AGE` entity extraction capability
- Minor corrections have been made to the calculation formulas in the Medicare Risk Adjustment Module


</div><div class="h3-box" markdown="1">

#### Updated Notebooks And Demonstrations For making Spark NLP For Healthcare Easier To Navigate And Understand

- New [Text Classification with Few Shot Classifier Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/30.3.Text_Classification_with_FewShotClassifier.ipynb)
- New [Voice of Patient Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/35.Voice_of_Patient_Model.ipynb)
- New [Social Determinant of Health Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/36.Social_Determinant_of_Health_Model.ipynb)
- Updated [Oncology Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/27.Oncology_Model.ipynb) for latest models
- New All-In-One [Social Determinant of Health Demo](https://demo.johnsnowlabs.com/healthcare/SDOH/)
- Updated [Medical LLM Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_LLM/)
- Updated [German ICD10GM Resolver Demo](https://demo.johnsnowlabs.com/healthcare/ER_ICD10_GM_DE/)


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `clinical_notes_qa_base`
+ `clinical_notes_qa_large`
+ `ner_profiling_vop`
+ `ner_profiling_sdoh`
+ `ner_profiling_oncology`
+ `ner_sdoh_access_to_healthcare`
+ `ner_sdoh_community_condition`
+ `ner_sdoh_demographics`
+ `ner_sdoh_health_behaviours_problems`
+ `ner_sdoh_income_social_status`
+ `ner_sdoh_social_environment`
+ `ner_sdoh_substance_usage`
+ `multiclassifierdl_hoc`
+ `multiclassifierdl_litcovid`
+ `bert_sequence_classifier_patient_urgency`
+ `ner_clinical` -> `nl`
+ `bert_token_classifier_ner_clinical` -> `nl`
+ `robertaresolve_icd10gm` -> `de`
+ `icd10gm_resolver_pipeline` -> `de`
+ `clinical_deidentification`
+ `sbiobert_base_cased_mli_onnx`





</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
