---
layout: docs
header: true
seotitle: Spark NLP for Healthcare | John Snow Labs
title: Spark NLP for Healthcare Release Notes 4.4.2
permalink: /docs/en/spark_nlp_healthcare_versions/release_notes_4_4_2
key: docs-licensed-release-notes
modify_date: 2023-05-18
show_nav: true
sidebar:
    nav: sparknlp-healthcare
---

<div class="h3-box" markdown="1">


## 4.4.2

#### Highlights


We are thrilled to unveil the latest set of upgrades and advancements for Spark NLP for Healthcare. This edition brings to the fore a host of remarkable enhancements and updates, which are as follows:

+ The medical QA models now incorporates Flan-T5 models, significantly expanding its capacity.
+ We introduce a newly finetuned biogpt-chat-jsl model, fine-tuned with clinical conditions to produce more precise descriptions when prompted.
+ The brand-new medical summarizer model is designed to provide summarizations of clinical guidelines under predefined categories such as causes, symptoms, and more. 
+ Text summarization method utilizing a map-reduce approach for section-wise summarization.
+ New chunk mapper model to map ICD10CM codes with corresponding causes and claim analysis codes according to CDC guidelines.
+ The PHI obfuscation (De-identification module) now offers the ability to customize the casings of fake entities for each entity type.
+ Users now have the option to enable or disable the 'gender awareness' feature in the De-identification module.
+ A set of four new classifier models has been introduced, further broadening the scope of our toolkit.
+ We now offer new clinical NER models specifically designed for extracting clinical terms in the German language.
+ Core functionalities have been fine-tuned with numerous improvements and bug fixes.
+ We are introducing new and updated notebooks, and demonstrations, providing a more user-friendly experience.
+ We have added and updated a substantial number of new clinical models and pipelines, further solidifying our offering in the healthcare domain.

We are confident that these enhancements will elevate your Spark NLP for Healthcare experience, enabling more accurate and streamlined processing of healthcare-related natural language data.



</div><div class="h3-box" markdown="1">


#### The Medical QA Models Now Incorporates Flan-T5 Models, Significantly Expanding Its Capacity

The newly incorporated `flan_t5_base_jsl_qa` model is meticulously designed to function seamlessly with the MedicalQuestionAnswering annotator. This innovative model is engineered to offer an efficacious solution for providing accurate answers and insightful information across a broad spectrum of domains. It is important to note that this is a general model and has not yet been fine-tuned for clinical texts. However, we are planning to carry out this specialized fine-tuning in our upcoming releases, further enhancing its applicability and precision in the clinical context.

*Example*:

```python
med_qa = MedicalQuestionAnswering.pretrained("flan_t5_base_jsl_qa", "en", "clinical/models")\
    .setInputCols(["document_question", "document_context"])\
    .setOutputCol("answer")\
    .setCustomPrompt("Question: {QUESTION}. Context: {DOCUMENT}")\
    .setMaxNewTokens(70)\
    .setTopK(1)
    

paper_abstract = "We have previously reported the feasibility of diagnostic and therapeutic peritoneoscopy including liver biopsy, gastrojejunostomy, and tubal ligation by an oral transgastric approach. We present results of per-oral transgastric splenectomy in a porcine model. The goal of this study was to determine the technical feasibility of per-oral transgastric splenectomy using a flexible endoscope. We performed acute experiments on 50-kg pigs. All animals were fed liquids for 3 days prior to procedure. The procedures were performed under general anesthesia with endotracheal intubation. The flexible endoscope was passed per orally into the stomach and puncture of the gastric wall was performed with a needle knife. The puncture was extended to create a 1.5-cm incision using a pull-type sphincterotome, and a double-channel endoscope was advanced into the peritoneal cavity. The peritoneal cavity was insufflated with air through the endoscope. The spleen was visualized. The splenic vessels were ligated with endoscopic loops and clips, and then mesentery was dissected using electrocautery. Endoscopic splenectomy was performed on six pigs. There were no complications during gastric incision and entrance into the peritoneal cavity. Visualization of the spleen and other intraperitoneal organs was very good. Ligation of the splenic vessels and mobilization of the spleen were achieved using commercially available devices and endoscopic accessories."

question = "How is transgastric endoscopic performed?"
```

*Result*:

```bash
['Transgastric endoscopic surgery is a type of surgery that involves removing the obstructions from the heart and lungs. It involves removing the trachea, a small artery, and a small sphincter. The trachea is then removed and the sphincter is removed.']
```


</div><div class="h3-box" markdown="1">


#### Introducing a Newly Finetuned biogpt-chat-jsl Model, based on Clinical Conditions.

We are excited to present our newly fine-tuned biogpt-chat-jsl model. This model, known as `biogpt_chat_jsl_conditions`, is based on the robust BioGPT architecture and has been meticulously fine-tuned with questions pertaining to a wide array of medical conditions.

Our team has concentrated on emphasizing the Q&A aspect, making it less conversational but highly focused on delivering accurate and insightful answers. This enhanced focus on question answering ensures that users can extract critical and relevant information quickly and accurately. This strategic fine-tuning with clinical guidelines strengthens the model's ability to provide superior results in the realm of medical NLP. 

*Example*:

```python
gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conditions", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("answer")\
    .setMaxNewTokens(199)

text = "What are the potential causes and risk factors for developing cardiovascular disease?"
```

*Result*:

```bash
[Cardiovascular disease ( CVD ) is a general term for conditions affecting the heart or blood vessels. It can be caused
by a variety of factors, including smoking, high blood pressure, diabetes, high cholesterol, and obesity. Certain
medical conditions, such as chronic kidney disease, can also increase the risk of developing CVD.]
```


</div><div class="h3-box" markdown="1">


#### The Brand-New Medical Summarizer Model Designed To Provide Summarizations Of Clinical Guidelines Under Predefined Categories Such As Causes, Symptoms, And More.

We are pleased to introduce the summarizer_clinical_guidelines_large model as part of our latest enhancements. This innovative Medical Summarizer Model is adept at providing succinct summarizations of clinical guidelines. At present, the model is equipped to handle guidelines for Asthma and Breast Cancer, though we plan to expand this repertoire in future iterations.

One of the notable features of this model is its ability to neatly categorize summarizations into four distinct sections: Overview, Causes, Symptoms, and Treatments. This systematic segregation facilitates ease of understanding and aids in extracting specific information more efficiently.

An additional technical specification to note is the model's context length, which stands at 768 tokens. This parameter ensures an optimal balance between detail and brevity, allowing for comprehensive yet concise summarizations.


*Example*:

```python
summarizer = MedicalSummarizer.pretrained("summarizer_clinical_guidelines_large", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(768)\
    .setMaxNewTokens(512)


text = """Clinical Guidelines for Breast Cancer:
Breast cancer is the most common type of cancer among women. It occurs when the cells in the breast start growing abnormally, forming a lump or mass. This can result in the spread of cancerous cells to other parts of the body. Breast cancer may occur in both men and women but is more prevalent in women.
The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy
Breast cancer may not present symptoms during its early stages. Symptoms typically manifest as the disease progresses. Some notable symptoms include:
- A lump or thickening in the breast or underarm area
- Changes in the size or shape of the breast
- Nipple discharge
- Nipple changes in appearance, such as inversion or flattening
- Redness or swelling in the breast
Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include:
- Surgery (such as lumpectomy or mastectomy)
- Radiation therapy
- Chemotherapy
- Hormone therapy
- Targeted therapy
Early detection is crucial for the successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40. If you notice any changes in your breast tissue, consult with your healthcare provider immediately.""" 
```


*Result*:

```bash
Overview of the disease: Breast cancer is the most common type of cancer among women, occurring when the cells in the breast start growing abnormally, forming a lump or mass. It can result in the spread of cancerous cells to other parts of the body. 

Causes: The exact cause of breast cancer is unknown, but several risk factors can increase the likelihood of developing it, such as a personal or family history, a genetic mutation, exposure to radiation, age, early onset of menstruation or late menopause, obesity, and hormonal factors. 

Symptoms: Symptoms of breast cancer typically manifest as the disease progresses, including a lump or thickening in the breast or underarm area, changes in the size or shape of the breast, nipple discharge, nipple changes in appearance, and redness or swelling in the breast. 

Treatment recommendations: Treatment for breast cancer depends on several factors, including the stage of the cancer, the location of the tumor, and the individual's overall health. Common treatment options include surgery, radiation therapy, chemotherapy, hormone therapy, and targeted therapy. Early detection is crucial for successful treatment of breast cancer. Women are advised to routinely perform self-examinations and undergo regular mammogram testing starting at age 40.
```


</div><div class="h3-box" markdown="1">





#### Text Summarization Method Utilizing A Map-Reduce Approach For Section-Wise Summarization.

We are pleased to announce the augmentation of our `MedicalSummarizer` annotator with the integration of advanced parameters. This enhancement broadens the scope of your medical summarization activities, granting you increased flexibility and helping to navigate the constraints of token limitations.

These newly introduced parameters notably amplify the functionality of the annotator, equipping users with the ability to generate detailed and accurate summaries of medical documents. The MedicalSummarizer now utilizes a map-reduce approach, a method that progressively condenses separate text sections until the summary achieves the desired length.

We are introducing the following parameters:

`setRefineSummary`: Activate this for a more refined summarization, albeit at a slightly increased computational cost.
`setRefineSummaryTargetLength`: Set your desired summary length in tokens (separated by whitespace). This feature is only operative when setRefineSummary is activated.
`setRefineChunkSize`: Define the size of refined chunks according to your preference. This size should match the LLM context window size in tokens. This feature is only operative when `setRefineSummary` is enabled.
`setRefineMaxAttempts`: Set the maximum number of attempts for re-summarizing chunks that exceed the `setRefineSummaryTargetLength` before discontinuation. This feature is only operative when setRefineSummary is enabled.

These advancements in the MedicalSummarizer annotator underline our unwavering commitment to delivering cutting-edge tools that enable healthcare professionals and researchers to conduct more efficient and precise medical text analysis.

*Example*:

```python
MedicalSummarizer.pretrained()\
    .setInputCols(["document"])\
    .setOutputCol("summary")\
    .setMaxTextLength(512)\
    .setMaxNewTokens(512)\
    .setDoSample(True)\
    .setRefineSummary(True)\
    .setRefineSummaryTargetLength(100)\
    .setRefineMaxAttempts(3)\
    .setRefineChunkSize(512)\
            

text = """The patient is a pleasant 17-year-old gentleman who was playing basketball today in gym. Two hours prior to presentation, he started to fall and someone stepped on his ankle and kind of twisted his right ankle and he cannot bear weight on it now. It hurts to move or bear weight. No other injuries noted. He does not think he has had injuries to his ankle in the past.
SOCIAL HISTORY: He does not drink or smoke.
MEDICAL DECISION MAKING:
He had an x-ray of his ankle that showed a small ossicle versus avulsion fracture of the talonavicular joint on the lateral view. He has had no pain over the metatarsals themselves. This may be a fracture based upon his exam. He does want to have me to put him in a splint. He was given Motrin here. He will be discharged home to follow up with Dr. X from Orthopedics.
DISPOSITION: Crutches and splint were administered here. I gave him a prescription for Motrin and some Darvocet if he needs to length his sleep and if he has continued pain to follow up with Dr. X. Return if any worsening problems."""

```

*Result*:

```bash
['An ankle exam revealed an osteocorotony in an injured man, who had pain on both Metatatsals. The physician prescribed sprained knee walker, thigh splinting for pain and crutches, but a calconavenous joint had a fracture. A physician will consult an orthopedic specialist for relief, follow up by the doctor, follow-down based on pain.']
```


</div><div class="h3-box" markdown="1">






#### New Chunk Mapper Model To Map ICD10CM Codes With Corresponding Causes and Claim Analysis Codes According To CDC Guidelines.

This model is designed to map ICD-10-CM codes and deliver corresponding causes and generate claim analysis codes for each respective ICD-10-CM code, adhering to the guidelines provided by the Centers for Disease Control and Prevention (CDC).

This model efficiently interfaces with the complex structure of ICD-10-CM coding, facilitating the extraction of meaningful and contextually relevant information. In instances where an equivalent claim analysis code is not available, the model will return a None result.


*Example*:

```python
chunkerMapper = ChunkMapperModel.pretrained("icd10cm_cause_claim_mapper", "en", "clinical/models")\
      .setInputCols(["icd_chunk"])\
      .setOutputCol("mappings")\
      .setRels(["icd10cm_cause", "icd10cm_claim_analysis_code"])

text = ["D69.51", "G43.83", "A18.03"]

```

*Result*:

|icd10cm_code|cause                               |icd10cm_claim_analysis_code|
|------------|------------------------------------|---------------------------|
|D69.51      |Unintentional injuries              |D69.51                     |
|D69.51      |Adverse effects of medical treatment|D69.51                     |
|G43.83      |Headache disorders                  |G43.83                     |
|G43.83      |Tension-type headache               |G43.83                     |
|G43.83      |Migraine                            |G43.83                     |
|A18.03      |Whooping cough                      |A18.03                     | 


</div><div class="h3-box" markdown="1">






#### The PHI Obfuscation (De-Identification Module) Now Offers The Ability To Customize The Casings Of Fake Entities For Each Entity Type.

This update introduces the `entityCasingModes` parameter in the `Deidentification` classes, a feature that enables you to define a Json path containing a dictionary of modes for casing selections.

This powerful capability lets you dictate how the casing of entities or data elements should be altered during the deidentification process, providing you with greater control and flexibility over your data.

The `entityCasingModes` parameter offers the following casing modes:

- `lowercase`: Transforms all characters to lowercase following the rules of the default locale.
- `uppercase`: Changes all characters to uppercase based on the default locale's rules.
- `capitalize`: Adjusts the first character to uppercase and alters the remaining characters to lowercase.
- `titlecase`: Modifies the first character in every token (word) to uppercase and changes the remaining characters to lowercase.

With the ability to set the `entityCasingModes` parameter with the appropriate casing mode for each entity type, you now have enhanced control over the deidentification process and how it manages the casing of those elements. This update underlines our commitment to providing advanced and user-centric tools that cater to your specific needs in healthcare data processing.

*Example*:

```python
casing_dict= {
    "lowercase": ["IDNUM","MEDICALRECORD"] ,
    "uppercase": ["city","street"],
    "capitalize": [ "AGE"],
    "titlecase":["DOCTOR", "PATIENT", "HOSPITAL"],
}

import json
with open('entity_casing.json', 'w', encoding='utf-8') as f:
    json.dump(casing_dict, f, ensure_ascii=False, indent=4)

obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_subentity_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setEntityCasingModes("./entity_casing.json")

text ='''
Record date: 08-24-2007. SSN : S5067003218XYZ. Adress: Keats Street, San Francisco .
Victoria Davis is a 61-year-old , born in Los Angeles, white female.
Her surgery took place at Emory University Hospital on August 21, 2007.
The right total knee replacement performed by Dr. Anderson Johnson and Dr. Amelia Martinez. 
Davis was transfused with 2 units of autologous blood postoperatively.
'''
```

*Result*:

|    | sentence                                                                                    | mask                                                                          | deidentified                                                                                    |
|---:|:--------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
|  0 | Record date: 08-24-2007.                                                                    | Record date: \<DATE>.                                                         | Record date: 09-01-2007.                                                                        |
|  1 | SSN : S5067003218XYZ.                                                                       | SSN : \<MEDICALRECORD>.                                                       | SSN : r7150154340vuf.                                                                           |
|  2 | Adress: Keats Street, San Francisco .                                                       | Adress: \<CITY>, \<STATE> .                                                   | Adress: HAROLD, COLORADO .                                                                      |
|  3 | Victoria Davis is a 61-year-old , born in Los Angeles, white female.                        | \<PATIENT> is a \<AGE> , born in \<CITY>, white female.                       | Marivic Friend is a 62-year-old , born in AUSTIN, white female.                                 |
|  4 | Her surgery took place at Emory University Hospital on August 21, 2007.                     | Her surgery took place at \<HOSPITAL> on \<DATE>.                             | Her surgery took place at Healthsouth Rehabilitation Hospital The Woodlands on August 29, 2007. |
|  5 | The right total knee replacement performed by Dr. Anderson Johnson and Dr. Amelia Martinez. | The right total knee replacement performed by Dr. \<DOCTOR> and Dr. \<DOCTOR>.| The right total knee replacement performed by Dr. Marland Sensor and Dr. Freada Gin.            |
|  6 | Davis was transfused with 2 units of autologous blood postoperatively.                      | \<PATIENT> was transfused with 2 units of autologous blood postoperatively.   | Zadok Phlegm was transfused with 2 units of autologous blood postoperatively.                   |



</div><div class="h3-box" markdown="1">

#### Users Now Have The Option To Enable Or Disable The 'Gender Awareness' Feature In The De-Identification Module.

Users now have the ability to enable or disable the 'Gender Awareness' feature, providing greater control over the deidentification process. This feature is operated via the `setGenderAwareness` parameter in the Deidentification class. By setting this parameter to `True`, the deidentification algorithm will consider the gender information associated with names. This additional layer of awareness allows for a more precise and accurate process of anonymization.

The option to activate or deactivate 'Gender Awareness' provides you with increased flexibility to adapt the deidentification process to your specific needs, further enhancing the accuracy and utility of the De-Identification module. 

*Example*:

```python
obfuscation = DeIdentification()\
    .setInputCols(["sentence", "token", "ner_chunk"]) \
    .setOutputCol("deidentified") \
    .setMode("obfuscate")\
    .setObfuscateDate(True)\
    .setGenderAwareness(True)

data = [
'William Walker is a 62 y.o. patient admitted',
'Jack Davies was seen by attending his Doctor.',
'Cecilia Reyes was scheduled for assessment.',
'Jessica Smith was discharged on 10/02/2022', 
'Evelyn White was seen by physician', 
'Riley John MD. was started on prophylaxis',   
]
```

*Result*:

|    | sentence                                      | deid_entity_label                            | obfuscated                                          |
|---:|:----------------------------------------------|:---------------------------------------------|:----------------------------------------------------|
|  0 | William Walker is a 62 y.o. patient admitted  | \<PATIENT> is a \<AGE> y.o. patient admitted | Emillio Epps is a 77 y.o. patient admitted          |
|  1 | Jack Davies was seen by attending his Doctor. | \<PATIENT> was seen by attending his Doctor. | Mitsuru Hitchcock was seen by attending his Doctor. |
|  2 | Cecilia Reyes was scheduled for assessment.   | \<PATIENT> was scheduled for assessment.     | Celeste Pies was scheduled for assessment.          |
|  3 | Jessica Smith was discharged on 10/02/2022    | \<PATIENT> was discharged on \<DATE>         | Chancey Banner was discharged on 12/03/2022         |
|  4 | Evelyn White was seen by physician            | \<PATIENT> was seen by physician             | Mistee Pipe was seen by physician                   |
|  5 | Riley John MD. was started on prophylaxis     | \<DOCTOR> MD. was started on prophylaxis     | Yandel Alvine MD. was started on prophylaxis        |


</div><div class="h3-box" markdown="1">


#### A Set Of Four New Classifier Models Has Been Introduced, Further Broadening The Scope Of Our Toolkit.

We are excited to announce 4 new classification models.

| model name                          | annotator                       | predicted entities |
|-------------------------------------|---------------------------------|-----------------|
| [`classifierml_ade`]()              | DocumentMLClassifierApproach    | `True`, `False` |
| [`classifier_logreg_ade`]()         | DocumentLogRegClassifierModel   | `True`, `False` |
| [`generic_svm_classifier_ade`]()    | GenericSVMClassifierModel       | `True`, `False` |
| [`generic_logreg_classifier_ade`]() | GenericLogRegClassifierModel    | `True`, `False` |


*Example*:

```python
logreg = DocumentLogRegClassifierModel.pretrained("classifier_logreg_ade", "en", "clinical/models")\
    .setInputCols("token")\
    .setOutputCol("prediction")

    ["""I feel great after taking tylenol."""], 
    ["""Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient."""]
```

*Result*:

|text                                                                                    |result |
|----------------------------------------------------------------------------------------|-------|
|I feel great after taking tylenol                                                       |[False]|
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[True] |



</div><div class="h3-box" markdown="1">




#### We Now Offer New Clinical NER Models Specifically Designed For Extracting Clinical Terms In The German Language.

We are excited to announce the German `ner_clinical` models, that can detect `Problem`, `Test` and `Treatment` entities.


*Example*:

```python
clinical_ner = MedicalNerModel.pretrained("ner_clinical", "de", "clinical/models") \
        .setInputCols(["sentence", "token", "embeddings"]) \
        .setOutputCol("ner")

sample_text= """Verschlechterung von Schmerzen oder Schwäche in den Beinen , Verlust der Darm - oder Blasenfunktion oder andere besorgniserregende Symptome. 
Der Patient erhielt empirisch Ampicillin , Gentamycin und Flagyl sowie Narcan zur Umkehrung von Fentanyl .
ALT war 181 , AST war 156 , LDH war 336 , alkalische Phosphatase war 214 und Bilirubin war insgesamt 12,7 ."""
```


*Result*:

|chunk                 |ner_label|
|----------------------|---------|
|Schmerzen             |PROBLEM  |
|Schwäche in den Beinen|PROBLEM  |
|Verlust der Darm      |PROBLEM  |
|Blasenfunktion        |PROBLEM  |
|Symptome              |PROBLEM  |
|empirisch Ampicillin  |TREATMENT|
|Gentamycin            |TREATMENT|
|Flagyl                |TREATMENT|
|Narcan                |TREATMENT|
|Fentanyl              |TREATMENT|
|ALT                   |TEST     |
|AST                   |TEST     |
|LDH                   |TEST     |
|alkalische Phosphatase|TEST     |
|Bilirubin             |TEST     |



</div><div class="h3-box" markdown="1">





#### Core Functionalities Have Been Fine-Tuned With Numerous Improvements and Bug Fixes

- Updated default models and documentation for `pretrained()` functions in most annotators.
- Use custom signatures when saving a `MedicalBertForSequenceClassification` model



</div><div class="h3-box" markdown="1">

#### We Are Introducing New and Updated Notebooks And Demonstrations, Providing a More User-Friendly Experience.


- New [Porting_QA_Models_From_Text_Generator_Backbone](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/31.1.Porting_QA_Models_From_Text_Generator_Backbone.ipynb) notebook for porting QA models from Text_Generator Models.
- Updated [Biogpt_Chat_JSL](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.Biogpt_Chat_JSL.ipynb) notebook with latest model.
- Updated [Medical_Text_Summarization](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/32.Medical_Text_Summarization.ipynb) notebook with lastest improvement.
- Updated [Medical_Question_Answering](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/31.Medical_Question_Answering.ipynb) norebook with latest model.
- New [SOCIAL DETERMINANT CLASSIFICATION GENERIC](https://demo.johnsnowlabs.com/healthcare/SOCIAL_DETERMINANT_CLASSIFICATION_GENERIC/) demo
- New [SPANISH CLINICAL TEXT SUMMARIZATION](https://demo.johnsnowlabs.com/healthcare/CLINICAL_TEXT_SUMMARIZATION_ES/) demo


</div><div class="h3-box" markdown="1">

#### We Have Added And Updated A Substantial Number Of New Clinical Models And Pipelines, Further Solidifying Our Offering In The Healthcare Domain.

+ `flan_t5_base_jsl_qa`
+ `biogpt_chat_jsl_conditions`
+ `summarizer_clinical_guidelines_large`
+ `ner_clinical` -> `de`
+ `classifier_logreg_ade`
+ `classifierml_ade`
+ `generic_svm_classifier_ade`
+ `generic_logreg_classifier_ade`
+ `ner_anatomy_emb_clinical_large`
+ `ner_anatomy_emb_clinical_medium`
+ `ner_abbreviation_emb_clinical_large`
+ `ner_abbreviation_emb_clinical_medium`
+ `icd10cm_cause_claim_mapper`
+ `spellcheck_drug_norvig`



</div><div class="h3-box" markdown="1">

For all Spark NLP for Healthcare models, please check: [Models Hub Page](https://nlp.johnsnowlabs.com/models?edition=Healthcare+NLP)


</div><div class="h3-box" markdown="1">

## Versions

</div>
{%- include docs-healthcare-pagination.html -%}
