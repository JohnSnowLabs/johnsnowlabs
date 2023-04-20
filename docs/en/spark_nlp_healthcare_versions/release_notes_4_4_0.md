---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 4.4.0
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_4_4_0
key: docs-licensed-release-notes
modify_date: 2023-04-12
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">


## 4.4.0

#### Highlights


+ Introducing `biogpt_chat_jsl`, the first ever closed-book medical question answering LLM based on BioGPT, that is finetuned on medical conversations, and scale over Spark clusters.
+ New `MedicalSummarizer` annotator and 5 new medical summarizer models for accurate and specialized results in medical text analysis, performning 30-35% (Blue) better than non-clinical summarizer models, with half of the parameters.
+ New `MedicalTextGenerator` annotator and 4 new medical text generator models for effortless creation of tailored medical documents
+ New Voice of Patients (VOP) NER model for detection of clinical terms in patient's own sentences
+ New Social Determinants of Health (SDOH) classification models
+ 2 brand new Clinical Embeddings Models, delivering unparalleled accuracy and insights for your medical data analysis
+ New annotator for windowed sentence splitting for enhanced context analysis
+ Gender-based name obfuscation in `Deidentification` for more accurate anonymization
+ `Deidentification` now supports unnormalized date shifting and format consistency
+ Setting entity pairs for each relation labels feature in `RelationExtractionModel` to reduce false positives
+ Core improvements and bug fixes
    - Format consistency for formatted entity obfuscation is set as default now
+ New and updated notebooks
+ New and updated demos
+ 30 new clinical models and pipelines added & updated in total




</div><div class="h3-box" markdown="1">

#### Introducing `biogpt_chat_jsl`, The First Ever Closed-Book Medical Question Answering LLM Based On `BioGPT`

We developed a new LLM called [`biogpt_chat_jsl`](https://nlp.johnsnowlabs.com/2023/04/12/biogpt_chat_jsl_en.html), the first ever closed-book medical question answering LLM based on `BioGPT`, that is finetuned on medical conversations happening in a clinical settings and can answer clinical questions related to symptoms, drugs, tests, and diseases. Due to the generative nature of the conversations returned by the model, we wrap this model around our brand new `MedicalTextGenerator` annotator that can scale over Spark clusters and fully compatible with the rest of the NLP models within the same pipeline as a downstream task (i.e. the generated text can be fed to NER or any other model in Spark NLP within the same pipeline). 


*Example*:

```python
    
gpt_jsl_qa  = MedicalTextGenerator.pretrained("biogpt_chat_jsl", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)

sample_text = "How to treat asthma ?"
```

*Result*:

```bash
['Asthma is itself an allergic disease due to cold or dust or pollen or grass etc. irrespective of the triggering factor. You can go for pulmonary function tests if not done. Treatment is mainly symptomatic which might require inhalation steroids, beta agonists, anticholinergics as MDI or rota haler as a regular treatment. To decrease the inflammation of bronchi and bronchioles, you might be given oral antihistamines with mast cell stabilizers (montelukast) and steroids (prednisolone) with nebulization and frequently steam inhalation. To decrease the bronchoconstriction caused by allergens, you might be given oral antihistamines with mast cell stabilizers (montelukast) and steroids (prednisolone) with nebulization and frequently steam inhalation. The best way to cure any allergy is a complete avoidance of allergen or triggering factor. Consult your pulmonologist for further advise.']
```


</div><div class="h3-box" markdown="1">

#### New `MedicalSummarizer` Annotator And 5 New Medical Summarizer Models For Accurate And Specialized Results In Medical Text Analysis

We have a new `MedicalSummarizer` annotator that uses a generative deep learning model to create summaries of medical texts given clinical contexts. This annotator helps to quickly summarize complex medical information.

Also we are releasing 5 new medical summarizer models.

| name                                       | description                              |
|--------------------------------------------|------------------------------------------|
| [`summarizer_clinical_jsl`](https://nlp.johnsnowlabs.com/2023/03/25/summarizer_clinical_jsl_en.html) | This model is a modified version of Flan-T5 (LLM) based summarization model that is finetuned with clinical notes, encounters, critical care notes, discharge notes, reports, curated  by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. It can generate summaries from clinical notes up to 512 tokens given the input text (max 1024 tokens).|
| [`summarizer_clinical_jsl_augmented`](https://nlp.johnsnowlabs.com/2023/03/30/summarizer_clinical_jsl_augmented_en.html) | This model is a modified version of Flan-T5 (LLM) based summarization model that is at first finetuned with natural instructions and then finetuned with clinical notes, encounters, critical care notes, discharge notes, reports, curated  by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. It can generate summaries from clinical notes up to 512 tokens given the input text (max 1024 tokens).|
| [`summarizer_clinical_questions`](https://nlp.johnsnowlabs.com/2023/04/03/summarizer_clinical_questions_en.html)     | This model is a modified version of Flan-T5 (LLM) based summarization model that is finetuned with medical questions exchanged in clinical mediums (clinic, email, call center etc.) by John Snow Labs.  It can generate summaries up to 512 tokens given an input text (max 1024 tokens).|
| [`summarizer_biomedical_pubmed`](https://nlp.johnsnowlabs.com/2023/04/03/summarizer_biomedical_pubmed_en.html)      | This model is a modified version of Flan-T5 (LLM) based summarization model that is finetuned with biomedical datasets (Pubmed abstracts) by John Snow Labs.  It can generate summaries up to 512 tokens given an input text (max 1024 tokens).|
| [`summarizer_generic_jsl`](https://nlp.johnsnowlabs.com/2023/03/30/summarizer_generic_jsl_en.html)            | This model is a modified version of Flan-T5 (LLM) based summarization model that is finetuned with additional data curated by John Snow Labs. This model is further optimized by augmenting the training methodology, and dataset. It can generate summaries from clinical notes up to 512 tokens given the input text (max 1024 tokens) |


Our clinical summarizer models with only 250M parameters perform 30-35% better than non-clinical SOTA text summarizers with 500M parameters, in terms of Bleu and Rouge benchmarks. That is, **we achieve 30% better with half of the parameters that other LLMs have**. See the details below.

</div><div class="h3-box" markdown="1">

🔎 Benchmark on MtSamples Summarization Dataset

| model_name | model_size | Rouge | Bleu | bertscore_precision | bertscore_recall: | bertscore_f1 |
|--|--|--|--|--|--|--|
philschmid/flan-t5-base-samsum | 250M | 0.1919 | 0.1124 | 0.8409 | 0.8964 | 0.8678 |
linydub/bart-large-samsum | 500M | 0.1586 | 0.0732 | 0.8747 | 0.8184 | 0.8456 |
philschmid/bart-large-cnn-samsum |  500M | 0.2170 | 0.1299 | 0.8846 | 0.8436 | 0.8636 |
transformersbook/pegasus-samsum | 500M | 0.1924 | 0.0965 | 0.8920 | 0.8149 | 0.8517 |
**summarizer_clinical_jsl** | **250M** | **0.4836** | **0.4188** | **0.9041** | **0.9374** | **0.9204** |
**summarizer_clinical_jsl_augmented** | **250M** | **0.5119** | **0.4545** | **0.9282** | **0.9526** | **0.9402** |

🔎 Benchmark on MIMIC Summarization Dataset

| model_name | model_size | Rouge | Bleu | bertscore_precision | bertscore_recall: | bertscore_f1 |
|--|--|--|--|--|--|--|
philschmid/flan-t5-base-samsum | 250M | 0.1910 | 0.1037 | 0.8708 | 0.9056 | 0.8879 |
linydub/bart-large-samsum | 500M | 0.1252 | 0.0382 | 0.8933 | 0.8440 | 0.8679 |
philschmid/bart-large-cnn-samsum | 500M | 0.1795 | 0.0889 | 0.9172 | 0.8978 | 0.9074 |
transformersbook/pegasus-samsum | 570M | 0.1425 | 0.0582 | 0.9171 | 0.8682 | 0.8920 |
**summarizer_clinical_jsl** | **250M** | **0.395** | **0.2962** | **0.895** | **0.9316** | **0.913** |
**summarizer_clinical_jsl_augmented** | **250M** | **0.3964** | **0.307** | **0.9109** | **0.9452** | **0.9227** |

![image](https://user-images.githubusercontent.com/64752006/230899745-3a67d142-1bdf-4f4b-83cb-d012953b1e09.png)

</div><div class="h3-box" markdown="1">

*Example*:

```python
summarizer = MedicalSummarizer.pretrained("summarizer_clinical_jsl", "en", "clinical/models")\
            .setInputCols(['document'])\
            .setOutputCol('summary')\
            .setMaxTextLength(512)\
            .setMaxNewTokens(512)

sample_text = """Patient with hypertension, syncope, and spinal stenosis - for recheck.
 (Medical Transcription Sample Report)
 SUBJECTIVE:  The patient is a 78-year-old female who returns for recheck. She has hypertension. She denies difficulty with chest pain, palpations, orthopnea, nocturnal dyspnea, or edema.
 PAST MEDICAL HISTORY / SURGERY / HOSPITALIZATIONS:  Reviewed and unchanged from the dictation on 12/03/2003.
 MEDICATIONS:  Atenolol 50 mg daily, Premarin 0.625 mg daily, calcium with vitamin D two to three pills daily, multivitamin daily, aspirin as needed, and TriViFlor 25 mg two pills daily. She also has Elocon cream 0.1% and Synalar cream 0.01% that she uses as needed for rash.
 """
```

*Result*:

```bash
["A 78-year-old female with hypertension, syncope, and spinal stenosis returns for recheck. She denies chest pain, palpations, orthopnea, nocturnal dyspnea, or edema. She is on multiple medications and has Elocon cream and Synalar cream for rash."]
```

*Example*:

```python
summarizer = MedicalSummarizer.pretrained("summarizer_clinical_questions", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)

sample_text = """Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed,poor digestion, panic attacks, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months. Because of this, I stayed in the hospital and just discharged from hospital. I had many other blood tests, brain mri, ultrasound scan, endoscopy because of some dumb doctors bcs they were not able to diagnose actual problem. Finally I got an appointment with a homeopathy doctor finally he find that i was suffering from hyperthyroid and my TSH was 0.15 T3 and T4 is normal . Also i have b12 deficiency and vitamin D deficiency so I'm taking weekly supplement of vitamin D and 1000 mcg b12 daily. I'm taking homeopathy medicine for 40 days and took 2nd test after 30 days. My TSH is 0.5 now. I feel a little bit relief from weakness and depression but I'm facing with 2 new problem from last week that is breathtaking problem and very rapid heartrate. I just want to know if i should start allopathy medicine or homeopathy is okay? Bcs i heard that thyroid take time to start recover. So please let me know if both of medicines take same time. Because some of my friends advising me to start allopathy and never take a chance as i can develop some serious problems.Sorry for my poor english😐Thank you."""
```

*Result*:

```bash
['What are the treatments for hyperthyroidism?']
```


You can check the [Medical Summarization Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb) for more examples and see the [Medical Summarization](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_SUMMARIZATION/) demo.



</div><div class="h3-box" markdown="1">

#### New `MedicalTextGenerator` Annotator And 4 New Medical Text Generator Models For Effortless Creation Of Tailored Medical Documents

We are releasing 4 new medical text generator models with a new `MedicalTextGenerator` annotator that uses the basic BioGPT model to perform various tasks related to medical text abstraction. With this annotator, a user can provide a prompt and context and instruct the system to perform a specific task, such as explaining why a patient may have a particular disease or paraphrasing the context more directly. In addition, this annotator can create a clinical note for a cancer patient using the given keywords or write medical texts based on introductory sentences. The BioGPT model is trained on large volumes of medical data allowing it to identify and extract the most relevant information from the text provided.

| name                                       | description                              |
|--------------------------------------------|------------------------------------------|
| [`text_generator_biomedical_biogpt_base`](https://nlp.johnsnowlabs.com/2023/04/03/text_generator_biomedical_biogpt_base_en.html)| This model is a BioGPT (LLM) based text generation model that is finetuned with biomedical datasets (Pubmed abstracts) by John Snow Labs.  Given a few tokens as an intro, it can generate human-like, conceptually meaningful texts  up to 1024 tokens given an input text (max 1024 tokens). |
| [`text_generator_generic_flan_base`](https://nlp.johnsnowlabs.com/2023/04/03/text_generator_generic_flan_base_en.html)     | This model is a modified version of Flan-T5 (LLM) based text generation model, which is basically the same as official [Flan-T5-base model](https://huggingface.co/google/flan-t5-base) released by Google.  Given a few tokens as an intro, it can generate human-like, conceptually meaningful texts  up to 512 tokens given an input text (max 1024 tokens).|
| [`text_generator_generic_jsl_base`](https://nlp.johnsnowlabs.com/2023/04/03/text_generator_generic_jsl_base_en.html)      | This model is a modified version of Flan-T5 (LLM) based text generation model that is finetuned with natural instruction datasets by John Snow Labs.  Given a few tokens as an intro, it can generate human-like, conceptually meaningful texts  up to 512 tokens given an input text (max 1024 tokens).|
| [`text_generator_generic_flan_t5_large`](https://nlp.johnsnowlabs.com/2023/04/04/text_generator_generic_flan_t5_large_en.html)      | This model is based on google's Flan-T5 Large, and can generate conditional text. Sequence length is 512 tokens.|


*Example*:

```python
med_text_generator  = MedicalTextGenerator.pretrained("text_generator_generic_jsl_base", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)

sample_text = "the patient is admitted to the clinic with a severe back pain and "
```

*Result*:

```bash
['the patient is admitted to the clinic with a severe back pain and a severe left - sided leg pain. The patient was diagnosed with a lumbar disc herniation and underwent a discectomy. The patient was discharged on the third postoperative day. The patient was followed up for a period of 6 months and was found to be asymptomatic. A rare case of a giant cell tumor of the sacrum. Giant cell tumors ( GCTs ) are benign, locally aggressive tumors that are most commonly found in the long bones of the extremities. They are rarely found in the spine. We report a case of a GCT of the sacrum in a young female patient. The patient presented with a history of progressive lower back pain and a palpable mass in the left buttock. The patient underwent a left hemilaminectomy and biopsy. The histopathological examination revealed a GCT. The patient was treated with a combination of surgery and radiation therapy. The patient was followed up for 2 years and no recurrence was observed. A rare case of a giant cell tumor of the sacrum. Giant cell tumors ( GCTs ) are benign, locally aggressive tumors that are most commonly found in the long bones of the extremities.']
```

You can check the [Medical Text Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Medical_Text_Generation.ipynb) for more examples and see the [Medical Text Generation](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_GENERATION/) demo.



</div><div class="h3-box" markdown="1">

#### New Voice of Patients (VOP) NER Model For Detection of Clinical Terms In Patient's Own Sentences

Announcing a new `ner_vop_wip` model that can detect `SubstanceQuantity`, `Measurements`, `Treatment`, `Modifier`, `RaceEthnicity`, `Allergen`, `TestResult`, `InjuryOrPoisoning`, `Frequency`, `MedicalDevice`, `Procedure`, `Duration`, `DateTime`, `HealthStatus`, `Route`, `Vaccine`, `Disease`, `Symptom`, `RelationshipStatus`, `Dosage`, `Substance`, `VitalTest`, `AdmissionDischarge`, `Test`, `Laterality`, `ClinicalDept`, `PsychologicalCondition`, `Age`, `BodyPart`, `Drug`, `Employment`, `Form` entities in patient's own sentences.  

For more details, please check the [model card](https://nlp.johnsnowlabs.com/2023/03/30/ner_vop_wip_en.html).

*Example*:

```python
...
ner = MedicalNerModel.pretrained("ner_vop_wip", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

sample_text = "Hello,I'm 20 year old girl. I'm diagnosed with hyperthyroid 1 month ago. I was feeling weak, light headed, depression, left chest pain, increased heart rate, rapidly weight loss, from 4 months."
```

*Results*:

| chunk        | ner_label              |
|--------------|------------------------|
| 20 year old  | Age                    |
| girl         | Gender                 |
| hyperthyroid | Disease                |
| 1 month ago  | DateTime               |
| weak         | Symptom                |
| light headed | Symptom                |
| depression   | PsychologicalCondition |
| left         | Laterality             |
| chest        | BodyPart               |
| pain         | Symptom                |
| increased    | TestResult             |
| heart rate   | VitalTest              |
| rapidly      | Modifier               |
| weight loss  | Symptom                |
| 4 months     | Duration               |



</div><div class="h3-box" markdown="1">

#### New Social Determinants of Health (SDOH) Classification Models

Announcing new classification models that can be used for SDOH tasks.

| name                                       | description                              | labels              |  
|--------------------------------------------|------------------------------------------|---------------------|
| [`genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/04/10/genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli_en.html)           | This Generic Classifier model is intended for detecting whether the patient has housing insecurity. If the clinical note includes patient housing problems, the model identifies it. If there is no housing issue or it is not mentioned in the text, it is regarded as "no housing insecurity". The model is trained by using GenericClassifierApproach annotator. | `Housing_Insecurity`: The patient has housing problems.<br>`No_Housing_Insecurity`: The patient has no housing problems or it is not mentioned in the clinical notes.|
| [`genericclassifier_sdoh_mental_health_clinical`](https://nlp.johnsnowlabs.com/2023/04/10/genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli_en.html)            | This Generic Classifier model is intended for detecting if the patient has mental health problems in clinical notes. This model is trained by using GenericClassifierApproach annotator. |`Mental_Disorder`: The patient has mental health problems. <br>`No_Or_Not_Mentioned`: The patient doesn't have mental health problems or it is not mentioned in the clinical notes.|
| [`genericclassifier_sdoh_under_treatment_sbiobert_cased_mli`](https://nlp.johnsnowlabs.com/2023/04/10/genericclassifier_sdoh_under_treatment_sbiobert_cased_mli_en.html)            | This Generic Classifier model is intended for detecting if the patient is under treatment or not. If under treatment is not mentioned in the text, it is regarded as "not under treatment". The model is trained by using GenericClassifierApproach annotator. |`Under_Treatment`: The patient is under treatment. <br>`Not_Under_Treatment_Or_Not_Mentioned`: The patient is not under treatment or it is not mentioned in the clinical notes.|

*Example*:

```python
generic_classifier = GenericClassifierModel.pretrained("genericclassifier_sdoh_mental_health_clinical", 'en', 'clinical/models')\
    .setInputCols(["features"])\
    .setOutputCol("class")

sample_text = ["James is a 28-year-old man who has been struggling with schizophrenia for the past five years. He was diagnosed with the condition after experiencing a psychotic episode in his early 20s.",
"Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. He reports feeling generally healthy, with no significant medical concerns."]
```

*Results*:

|                                                                 text|               result|
|---------------------------------------------------------------------|---------------------|
|James is a 28-year-old man who has been struggling with schizophrenia for the past five years. He...|    [Mental_Disorder]|
|Patient John is a 60-year-old man who presents to a primary care clinic for a routine check-up. H...|[No_Or_Not_Mentioned]|


</div><div class="h3-box" markdown="1">

#### 2 Brand New Clinical Embeddings Models, Delivering Unparalleled Accuracy And Insights For Your Medical Data Analysis

We are releasing two new clinical embeddings models, which were trained using the word2vec algorithm on clinical and biomedical datasets. The models are expected to be more effective in generalizing recent content, and the dataset curation cut-off date was March 2023. The models come in two sizes: the `large` model is around 2 GB, while the `medium` model is around 1 GB, and both have 200 dimensions. Benchmark tests indicate that the new embeddings models can replace the previous clinical embeddings while training other models (e.g. NER, assertion, RE etc.).


| name                                       | description                              |
|--------------------------------------------|------------------------------------------|
| [`embeddings_clinical_medium`](https://nlp.johnsnowlabs.com/2023/04/07/embeddings_clinical_medium_en.html)           | This model is trained on a list of clinical and biomedical datasets curated in-house. The size of the model is around 1 GB and has 200 dimensions. |
| [`embeddings_clinical_large`](https://nlp.johnsnowlabs.com/2023/04/07/embeddings_clinical_large_en.html)            | This model is trained on a list of clinical and biomedical datasets curated in-house. The size of the model is around 2 GB and has 200 dimensions. |


*Example*:

```python
embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")
```

We are releasing 12 new NER models, trained with the new embeddings.


</div><div class="h3-box" markdown="1">

#### Windowed Sentence Splitting For Enhanced Context Analysis

We have a new `WindowedSentenceModel` annotator that helps you to merge the previous and following sentences of a given piece of text, so that you add the context surrounding them. This is super useful for especially context-rich analyses that require a deeper understanding of the language being used.

Inferring the class from `sentence X` may be a much harder task sometime, due to the lack of context, than to infer the class of `sentence X-1 + sentence X + sentence X+1`. In this example, the window is `1`, that's why we augment sentence with **1 neighbour from behind and another from ahead**. Window size can be configured so that each piece of text/sentence get a number of previous and posterior sentences as context, equal to the windows size.



*Example*:

```python
windowedSentence1 =  WindowedSentenceModel()\
    .setWindowSize(1)\
    .setInputCols("sentence")\
    .setOutputCol("window_1")

sample_text = """The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions."""
```

*Results* :

result                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis.                                                |
|The patient was admitted on Monday. She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold.               |
|She has a right-sided pleural effusion for thoracentesis. Her Coumadin was placed on hold. A repeat echocardiogram was checked.              |
|Her Coumadin was placed on hold. A repeat echocardiogram was checked. She was started on prophylaxis for DVT.                                |
|A repeat echocardiogram was checked. She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy.        |
|She was started on prophylaxis for DVT. Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.|
|Her CT scan from March 2006 prior to her pericardectomy. It already shows bilateral plural effusions.                            |            




</div><div class="h3-box" markdown="1">

#### Gender-Based Name Obfuscation in `Deidentification` For More Accurate Anonymization

We have enhanced the `Deidentification` capabilities by introducing **gender-based name obfuscation**, which enables more accurate anonymization of personal information. This feature checks the gender categories of names and replaces them with fake names from the same gender category. For example, if a name belongs to a male person, it will be replaced with a fake name of a male person. Similarly, female names will be replaced with fake female names, while unisex names will be replaced with fake unisex names. This ensures that the anonymized data remains consistent and maintains its accuracy, without compromising on privacy.  

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")

```

*Results*:

| sentence                                      | obfuscated                                     |
|:----------------------------------------------|:-----------------------------------------------|
| William Walker is a 62 y.o. patient admitted  | Jamire Allen is a 64 y.o. patient admitted     |
| Jack Davies was seen by attending his Doctor. | Decarlos Ran was seen by attending his Doctor. |
| Cecilia Reyes was scheduled for assessment.   | Ressie Moellers was scheduled for assessment.  |
| Jessica Smith was discharged on 10/02/2022    | Leocadia Quin was discharged on 04/04/2022     |
| Evelyn White was seen by physician            | Tritia Santiago was seen by physician          |
| Riley John was started on prophylaxis         | Nayel Dodrill was started on prophylaxis       |




</div><div class="h3-box" markdown="1">

#### `Deidentification` Now Maintains Unnormalized Date Shifting And Format Consistency

The `DATE` entity obfuscation now maintains the same format as the original date, ensuring that the anonymized data remains consistent and easy to work with. This improvement in format consistency is designed to enhance the clarity and usability of `Deidentification` annotator, making it easier to extract meaningful insights from text data while still protecting individual privacy.

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setDays(10)\
```

*Results*:

| dates     | obfuscated   |
|:-------------|:-------------|
| 08/02/2018   | 18/02/2018   |
| 8/2/2018     | 18/2/2018    |
| 08/02/18     | 18/02/18     |
| 8/2/18       | 18/2/18      |
| 11/2018      | 12/2018      |
| 01/05        | 11/05        |
| 12 Mar 2021  | 22 Mar 2021  |
| Mar 2021     | Apr 2021     |
| Jan 30, 2018 | Feb 9, 2018  |
| Jan 3, 2018  | Jan 13, 2018 |
| Jan 05       | Jan 15       |
| Jan 5        | Jan 15       |
| 2022         | 2023         |


</div><div class="h3-box" markdown="1">



#### Setting Entity Pairs For Each Relation Labels Feature In `RelationExtractionModel` to reduce false positives

`RelationExtractionModel` now includes the ability to set entity pairs for each relation label, giving you more control over your results and even greater accuracy.

In the following example, we utilize entity pair restrictions to limit the results of Relation Extraction labels solely to relations that exist between specified entities, thus improving the accuracy and relevance of the extracted data. If we don't set `setRelationTypePerPair` parameter here, RE model may return different RE labels for these specified entities.

*Example*:

```python
re_model = RelationExtractionModel.pretrained("re_test_result_date", "en", "clinical/models")\
    .setInputCols(["embeddings", "pos_tags", "ner_chunks", "dependencies"])\
    .setOutputCol("relations")\
    .setRelationPairsCaseSensitive(False)\
    .setRelationTypePerPair({
            "is_result_of": ["Test_Result-Test"],
            "is_date_of": ["Date-Test"],
            "is_finding_of": ["Test-EKG_Findings", "Test-ImagingFindings"]
        })\
    .setPredictionThreshold(0)
```



</div><div class="h3-box" markdown="1">

#### Core Improvements and Bug Fixes


- We set format consistency for formatted entity obfuscation of `PHONE`, `FAX`, `ID`, `IDNUM`, `BIOID`, `MEDICALRECORD`, `ZIP`, `VIN`, `SSN`, `DLN`, `LICENSE` and `PLATE` entities as default to make it easy-to-use.




</div><div class="h3-box" markdown="1">

#### New and Updated Notebooks

- New [Medical Summarization Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb) for summarization of clinical context can be used with new `MedicalSummarizer` annotator.
- New [Medical Text Generation Notebook](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Medical_Text_Generation.ipynb) for test generation of clinical context can be used with new `MedicalTextGenerator` annotator.




</div><div class="h3-box" markdown="1">

#### New and Updated Demos

+ [Medical Summarization](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_SUMMARIZATION/) demo
+ [Medical Text Generation](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_GENERATION/) demo



</div><div class="h3-box" markdown="1">

#### 30 New Clinical Models and Pipelines Added & Updated in Total


+ `ner_vop_wip`
+ `biogpt_chat_jsl`
+ `summarizer_generic_jsl`
+ `summarizer_clinical_jsl`
+ `summarizer_biomedical_pubmed`
+ `summarizer_clinical_questions`
+ `summarizer_clinical_jsl_augmented`
+ `text_generator_biomedical_biogpt_base`
+ `text_generator_generic_flan_base`
+ `text_generator_generic_flan_t5_large`
+ `text_generator_generic_jsl_base`
+ `genericclassifier_sdoh_housing_insecurity_sbiobert_cased_mli`
+ `genericclassifier_sdoh_mental_health_clinical`
+ `genericclassifier_sdoh_under_treatment_sbiobert_cased_mli`
+ `embeddings_clinical_medium`
+ `embeddings_clinical_large`
+ `ner_jsl_limited_80p_for_benchmarks`
+ `ner_oncology_limited_80p_for_benchmarks`
+ `ner_jsl_emb_clinical_large`
+ `ner_jsl_emb_clinical_medium`
+ `ner_oncology_emb_clinical_medium`
+ `ner_oncology_emb_clinical_large`
+ `ner_vop_emb_clinical_medium_wip`
+ `ner_vop_emb_clinical_large_wip`
+ `ner_sdoh_emb_clinical_large_wip`
+ `ner_sdoh_emb_clinical_medium_wip`
+ `ner_posology_emb_clinical_large`
+ `ner_posology_emb_clinical_medium`
+ `ner_deid_large_emb_clinical_large`
+ `ner_deid_large_emb_clinical_medium`

</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="prev_ver h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
