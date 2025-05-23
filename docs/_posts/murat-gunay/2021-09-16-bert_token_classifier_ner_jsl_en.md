---
layout: model
title: Detect Clinical Entities (BertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_jsl
date: 2021-09-16
tags: [ner, ner_jsl, en, licensed]
task: Named Entity Recognition
language: en
nav_key: models
edition: Healthcare NLP 3.2.0
spark_version: 2.4
supported: true
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---


## Description


Pretrained named entity recognition deep learning model for clinical terminology.  This model is trained with `BertForTokenClassification` method from `transformers` library and imported into Spark NLP. It detects 77 entities.

Definitions of Predicted Entities: 

- `Injury_or_Poisoning`: Physical harm or injury caused to the body, including those caused by accidents, falls, or poisoning of a patient or someone else. 
- `Direction`: All the information relating to the laterality of the internal and external organs. 
- `Test`: Mentions of laboratory, pathology, and radiological tests. 
- `Admission_Discharge`: Terms that indicate the admission and/or the discharge of a patient. 
- `Death_Entity`: Mentions that indicate the death of a patient. 
- `Relationship_Status`: State of patients romantic or social relationships (e.g. single, married, divorced). 
- `Duration`: The duration of a medical treatment or medication use. 
- `Respiration`: Number of breaths per minute. 
- `Hyperlipidemia`: Terms that indicate hyperlipidemia with relevant subtypes and synonims.  
- `Birth_Entity`: Mentions that indicate giving birth. 
- `Age`: All mention of ages, past or present, related to the patient or with anybody else. 
- `Labour_Delivery`: Extractions include stages of labor and delivery. 
- `Family_History_Header`: identifies section headers that correspond to Family History of the patient. 
- `BMI`: Numeric values and other text information related to Body Mass Index. 
- `Temperature`: All mentions that refer to body temperature. 
- `Alcohol`: Terms that indicate alcohol use, abuse or drinking issues of a patient or someone else. 
- `Kidney_Disease`: Terms that refer to any kidney diseases (includes mentions of modifiers such as "Acute" or "Chronic"). 
- `Oncological`: All the cancer, tumor or metastasis related extractions mentioned in the document, of the patient or someone else. 
- `Medical_History_Header`: Identifies section headers that correspond to Past Medical History of a patient. 
- `Cerebrovascular_Disease`: All terms that refer to cerebrovascular diseases and events.  
- `Oxygen_Therapy`: Breathing support triggered by patient or entirely or partially by machine (e.g. ventilator, BPAP, CPAP). 
- `O2_Saturation`: Systemic arterial, venous or peripheral oxygen saturation measurements. 
- `Psychological_Condition`: All the Mental health diagnosis, disorders, conditions or syndromes of a patient or someone else. 
- `Heart_Disease`: All mentions of acquired, congenital or degenerative heart diseases. 
- `Employment`: All mentions of patient or provider occupational titles and employment status . 
- `Obesity`: Terms related to a patient being obese (overweight and BMI are extracted as different labels). 
- `Disease_Syndrome_Disorder`: All the diseases mentioned in the document, of the patient or someone else (excluding diseases that are extracted with their specific labels, such as "Heart_Disease" etc.). 
- `Pregnancy`: All terms related to Pregnancy (excluding terms that are extracted with their specific labels, such as "Labour_Delivery" etc.). 
- `ImagingFindings`: All mentions of radiographic and imagistic findings. 
- `Procedure`: All mentions of invasive medical or surgical procedures or treatments. 
- `Medical_Device`: All mentions related to medical devices and supplies. 
- `Race_Ethnicity`: All terms that refer to racial and national origin of sociocultural groups. 
- `Section_Header`: All the section headers present in the text  (Medical History, Family History, Social History, Physical Examination and Vital signs Headers are extracted separately with their specific labels). 
- `Symptom`: All the symptoms mentioned in the document, of a patient or someone else. 
- `Treatment`: Includes therapeutic and minimally invasive treatment and procedures (invasive treatments or procedures are extracted as "Procedure"). 
- `Substance`: All mentions of substance use related to the patient or someone else (recreational drugs, illicit drugs). 
- `Route`: Drug and medication administration routes available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Drug_Ingredient`: Active ingredient/s found in drug products. 
- `Blood_Pressure`: Systemic blood pressure, mean arterial pressure, systolic and/or diastolic are extracted. 
- `Diet`: All mentions and information regarding patients dietary habits. 
- `External_body_part_or_region`: All mentions related to external body parts or organs that can be examined by naked eye. 
- `LDL`: All mentions related to the lab test and results for LDL (Low Density Lipoprotein). 
- `VS_Finding`: Qualitative data (e.g. Fever, Cyanosis, Tachycardia) and any other symptoms that refers to vital signs. 
- `Allergen`: Allergen related extractions mentioned in the document. 
- `EKG_Findings`: All mentions of EKG readings. 
- `Imaging_Technique`: All mentions of special radiographic views or special imaging techniques used in radiology. 
- `Triglycerides`: All mentions terms related to specific lab test for Triglycerides. 
- `RelativeTime`: Time references that are relative to different times or events (e.g. words such as "approximately", "in the morning"). 
- `Gender`: Gender-specific nouns and pronouns. 
- `Pulse`: Peripheral heart rate, without advanced information like measurement location. 
- `Social_History_Header`: Identifies section headers that correspond to Social History of a patient. 
- `Substance_Quantity`: All mentions of substance quantity (quantitative information related to illicit/recreational drugs). 
- `Diabetes`: All terms related to diabetes mellitus. 
- `Modifier`: Terms that modify the symptoms, diseases or risk factors. If a modifier is included in ICD-10 name of a specific disease, the respective modifier is not extracted separately. 
- `Internal_organ_or_component`: All mentions related to internal body parts or organs that can not be examined by naked eye. 
- `Clinical_Dept`: Terms that indicate the medical and/or surgical departments. 
- `Form`: Drug and medication forms available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Drug_BrandName`: Commercial labeling name chosen by the labeler or the drug manufacturer for a drug containing a single or multiple drug active ingredients. 
- `Strength`: Potency of one unit of drug (or a combination of drugs) the measurement units available are described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Fetus_NewBorn`: All terms related to fetus, infant, new born (excluding terms that are extracted with their specific labels, such as "Labour_Delivery", "Pregnancy" etc.). 
- `RelativeDate`: Temporal references that are relative to the date of the text or to any other specific date (e.g. "approximately two years ago", "about two days ago"). 
- `Height`: All mentions related to a patients height. 
- `Test_Result`: Terms related to all the test results present in the document (clinical tests results are included). 
- `Sexually_Active_or_Sexual_Orientation`: All terms that are related to sexuality, sexual orientations and sexual activity. 
- `Frequency`: Frequency of administration for a dose prescribed. 
- `Time`: Specific time references (hour and/or minutes). 
- `Weight`: All mentions related to a patients weight. 
- `Vaccine`: Generic and brand name of vaccines or vaccination procedure. 
- `Vital_Signs_Header`: Identifies section headers that correspond to Vital Signs of a patient. 
- `Communicable_Disease`: Includes all mentions of communicable diseases. 
- `Dosage`: Quantity prescribed by the physician for an active ingredient; measurement units are available described by [FDA](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Overweight`: Terms related to the patient being overweight (BMI and Obesity is extracted separately). 
- `Hypertension`: All terms related to Hypertension (quantitative data such as 150/100 is extracted as Blood_Pressure). 
- `HDL`: Terms related to the lab test for HDL (High Density Lipoprotein). 
- `Total_Cholesterol`: Terms related to the lab test and results for cholesterol. 
- `Smoking`: All mentions of smoking status of a patient. 
- `Date`: Mentions of an exact date, in any format, including day number, month and/or year. 



## Predicted Entities


`Injury_or_Poisoning`, `Direction`, `Test`, `Admission_Discharge`, `Death_Entity`, `Relationship_Status`, `Duration`, `Respiration`, `Hyperlipidemia`, `Birth_Entity`, `Age`, `Labour_Delivery`, `Family_History_Header`, `BMI`, `Temperature`, `Alcohol`, `Kidney_Disease`, `Oncological`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Oxygen_Therapy`, `O2_Saturation`, `Psychological_Condition`, `Heart_Disease`, `Employment`, `Obesity`, `Disease_Syndrome_Disorder`, `Pregnancy`, `ImagingFindings`, `Procedure`, `Medical_Device`, `Race_Ethnicity`, `Section_Header`, `Symptom`, `Treatment`, `Substance`, `Route`, `Drug_Ingredient`, `Blood_Pressure`, `Diet`, `External_body_part_or_region`, `LDL`, `VS_Finding`, `Allergen`, `EKG_Findings`, `Imaging_Technique`, `Triglycerides`, `RelativeTime`, `Gender`, `Pulse`, `Social_History_Header`, `Substance_Quantity`, `Diabetes`, `Modifier`, `Internal_organ_or_component`, `Clinical_Dept`, `Form`, `Drug_BrandName`, `Strength`, `Fetus_NewBorn`, `RelativeDate`, `Height`, `Test_Result`, `Sexually_Active_or_Sexual_Orientation`, `Frequency`, `Time`, `Weight`, `Vaccine`, `Vital_Signs_Header`, `Communicable_Disease`, `Dosage`, `Overweight`, `Hypertension`, `HDL`, `Total_Cholesterol`, `Smoking`, `Date`


{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_BERT_TOKEN_CLASSIFIER/){:.button.button-orange}{:target="_blank"}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_BERT_TOKEN_CLASSIFIER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_3.2.0_2.4_1631824058676.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_3.2.0_2.4_1631824058676.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}


## How to use

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

tokenClassifier = BertForTokenClassification.pretrained("bert_token_classifier_ner_jsl", "en", "clinical/models")\
    .setInputCols("token", "document")\
    .setOutputCol("ner")\
    .setCaseSensitive(True)

ner_converter = NerConverter()\
    .setInputCols(["document","token","ner"])\
    .setOutputCol("ner_chunk")

pipeline =  Pipeline(stages=[documentAssembler, tokenizer, tokenClassifier, ner_converter])

p_model = pipeline.fit(spark.createDataFrame(pd.DataFrame({'text': ['']})))

test_sentence = """The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

result = p_model.transform(spark.createDataFrame(pd.DataFrame({'text': [test_sentence]})))
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val tokenClassifier = BertForTokenClassification.pretrained("bert_token_classifier_ner_jsl", "en", "clinical/models")
    .setInputCols(Array("token", "document"))
    .setOutputCol("ner")
    .setCaseSensitive(True)

val ner_converter = new NerConverter()
    .setInputCols(Array("document","token","ner"))
    .setOutputCol("ner_chunk")

val pipeline =  new Pipeline().setStages(Array(documentAssembler, tokenizer, tokenClassifier, ner_converter))

val data = Seq("""he patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```


{:.nlu-block}
```python
import nlu
nlu.load("en.classify.token_bert.ner_jsl").predict("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""")
```

</div>


## Results


```bash
+-----------------------------------------+----------------------------+
|chunk                                    |ner_label                   |
+-----------------------------------------+----------------------------+
|21-day-old                               |Age                         |
|Caucasian                                |Race_Ethnicity              |
|male                                     |Gender                      |
|2 days                                   |Duration                    |
|congestion                               |Symptom                     |
|mom                                      |Gender                      |
|yellow discharge                         |Symptom                     |
|nares                                    |External_body_part_or_region|
|she                                      |Gender                      |
|mild                                     |Modifier                    |
|problems with his breathing while feeding|Symptom                     |
|perioral cyanosis                        |Symptom                     |
|retractions                              |Symptom                     |
|One day ago                              |RelativeDate                |
|mom                                      |Gender                      |
|tactile temperature                      |Symptom                     |
|Tylenol                                  |Drug_BrandName              |
|Baby-girl                                |Gender                      |
|decreased p.o. intake                    |Symptom                     |
|His                                      |Gender                      |
|breast-feeding                           |External_body_part_or_region|
|20 minutes                               |Duration                    |
|q.2h. to 5 to 10 minutes                 |Frequency                   |
|his                                      |Gender                      |
|respiratory congestion                   |Symptom                     |
|He                                       |Gender                      |
|tired                                    |Symptom                     |
|fussy                                    |Symptom                     |
|over the past 2 days                     |RelativeDate                |
|albuterol                                |Drug_Ingredient             |
|ER                                       |Clinical_Dept               |
|His                                      |Gender                      |
|urine output has                         |Symptom                     |
|decreased                                |Symptom                     |
|he                                       |Gender                      |
|per 24 hours                             |Frequency                   |
|he                                       |Gender                      |
|per 24 hours                             |Frequency                   |
|Mom                                      |Gender                      |
|diarrhea                                 |Symptom                     |
|His                                      |Gender                      |
|bowel                                    |Internal_organ_or_component |
+-----------------------------------------+----------------------------+
```


{:.model-param}
## Model Information


{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jsl|
|Compatibility:|Healthcare NLP 3.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|en|
|Case sensitive:|true|
|Max sentense length:|256|


## Data Source


Trained on data gathered and manually annotated by John Snow Labs. https://www.johnsnowlabs.com/data/


## Benchmarking


```bash
Label  precision    recall  f1-score   support
B-Admission_Discharge       0.96      0.97      0.96       298
B-Age       0.96      0.97      0.97      1545
B-Alcohol       0.89      0.86      0.87       117
B-BMI       1.00      0.67      0.80         9
B-Birth_Entity       0.50      0.60      0.55         5
B-Blood_Pressure       0.78      0.73      0.76       232
B-Cancer_Modifier       0.82      0.90      0.86        10
B-Cerebrovascular_Disease       0.68      0.75      0.71       163
B-Clinical_Dept       0.88      0.88      0.88      1510
B-Communicable_Disease       0.88      0.94      0.91        47
B-Date       0.96      0.97      0.96       960
B-Death_Entity       0.84      0.79      0.82        39
B-Diabetes       0.94      0.93      0.93       129
B-Diet       0.64      0.55      0.59       166
B-Direction       0.92      0.94      0.93      4605
B-Disease_Syndrome_Disorder       0.90      0.87      0.88      6729
B-Dosage       0.73      0.74      0.73       611
B-Drug_BrandName       0.89      0.90      0.89      2919
B-Drug_Ingredient       0.90      0.92      0.91      6243
B-Duration       0.76      0.80      0.78       296
B-EKG_Findings       0.75      0.76      0.76       114
B-Employment       0.86      0.84      0.85       315
B-External_body_part_or_region       0.86      0.87      0.86      3050
B-Family_History_Header       0.99      0.99      0.99       268
B-Fetus_NewBorn       0.71      0.67      0.69        97
B-Form       0.75      0.75      0.75       351
B-Frequency       0.88      0.93      0.90      1238
B-Gender       0.98      0.98      0.98      4409
B-HDL       1.00      0.50      0.67         8
B-Heart_Disease       0.83      0.86      0.85       728
B-Height       0.93      0.87      0.90        31
B-Hyperlipidemia       0.97      1.00      0.99       229
B-Hypertension       0.98      0.99      0.98       423
B-ImagingFindings       0.53      0.59      0.56       218
B-Imaging_Technique       0.49      0.57      0.53        60
B-Injury_or_Poisoning       0.84      0.80      0.82       721
B-Internal_organ_or_component       0.89      0.91      0.90     11514
B-Kidney_Disease       0.78      0.79      0.78       164
B-LDL       0.62      0.67      0.64        12
B-Labour_Delivery       0.75      0.64      0.69        84
B-Medical_Device       0.87      0.90      0.88      6762
B-Medical_History_Header       0.92      0.94      0.93       163
B-Modifier       0.82      0.86      0.84      3491
B-O2_Saturation       0.51      0.73      0.60       154
B-Obesity       0.92      0.97      0.95       120
B-Oncological       0.87      0.89      0.88       925
B-Oncology_Therapy       0.91      0.45      0.61        22
B-Overweight       0.75      0.60      0.67        10
B-Oxygen_Therapy       0.68      0.71      0.70       313
B-Pregnancy       0.75      0.85      0.79       237
B-Procedure       0.89      0.89      0.89      6219
B-Psychological_Condition       0.74      0.76      0.75       209
B-Pulse       0.80      0.74      0.77       178
B-Race_Ethnicity       0.93      0.99      0.96       111
B-Relationship_Status       1.00      0.76      0.87        34
B-RelativeDate       0.86      0.84      0.85       569
B-RelativeTime       0.65      0.68      0.67       250
B-Respiration       0.87      0.72      0.79       161
B-Route       0.85      0.86      0.85      1361
B-Section_Header       0.96      0.97      0.97     12925
B-Sexually_Active_or_Sexual_Orientation       1.00      1.00      1.00         1
B-Smoking       0.95      0.84      0.89       145
B-Social_History_Header       0.93      0.95      0.94       338
B-Staging       1.00      1.00      1.00         4
B-Strength       0.88      0.88      0.88       794
B-Substance       0.73      0.94      0.82        87
B-Symptom       0.87      0.86      0.87     11526
B-Temperature       0.81      0.84      0.83       198
B-Test       0.87      0.88      0.88      5850
B-Test_Result       0.84      0.85      0.84      2096
B-Time       0.92      0.98      0.95      1119
B-Total_Cholesterol       0.95      0.75      0.84        28
B-Treatment       0.62      0.65      0.64       354
B-Triglycerides       0.59      0.94      0.73        17
B-VS_Finding       0.77      0.86      0.81       592
B-Vaccine       0.90      0.84      0.87        77
B-Vital_Signs_Header       0.94      0.99      0.96       958
B-Weight       0.75      0.86      0.80       109
I-Age       0.92      0.96      0.94       283
I-Alcohol       0.83      0.62      0.71         8
I-Allergen       0.00      0.00      0.00        15
I-BMI       1.00      0.88      0.93        24
I-Blood_Pressure       0.82      0.84      0.83       456
I-Cerebrovascular_Disease       0.48      0.82      0.61        66
I-Clinical_Dept       0.92      0.91      0.91       717
I-Communicable_Disease       0.81      1.00      0.89        25
I-Date       0.94      0.99      0.96       152
I-Death_Entity       0.67      0.40      0.50         5
I-Diabetes       0.99      0.92      0.95        85
I-Diet       0.70      0.72      0.71        83
I-Direction       0.86      0.84      0.85       235
I-Disease_Syndrome_Disorder       0.88      0.86      0.87      3878
I-Dosage       0.78      0.69      0.73       540
I-Drug_BrandName       0.68      0.55      0.61        89
I-Drug_Ingredient       0.83      0.87      0.85       720
I-Duration       0.83      0.86      0.85       567
I-EKG_Findings       0.81      0.69      0.75       175
I-Employment       0.66      0.71      0.69       118
I-External_body_part_or_region       0.85      0.89      0.87       873
I-Family_History_Header       0.97      1.00      0.98       280
I-Fetus_NewBorn       0.55      0.58      0.56        88
I-Frequency       0.86      0.89      0.87       638
I-HDL       1.00      0.75      0.86         4
I-Heart_Disease       0.86      0.86      0.86       732
I-Height       0.97      0.95      0.96        82
I-Hypertension       0.82      0.75      0.78        12
I-ImagingFindings       0.64      0.60      0.62       257
I-Injury_or_Poisoning       0.78      0.79      0.79       589
I-Internal_organ_or_component       0.90      0.91      0.90      5278
I-Kidney_Disease       0.94      0.91      0.93       186
I-LDL       0.43      0.60      0.50         5
I-Labour_Delivery       0.84      0.77      0.80        69
I-Medical_Device       0.88      0.91      0.89      3590
I-Medical_History_Header       1.00      0.96      0.98       433
I-Metastasis       0.92      0.65      0.76        17
I-Modifier       0.62      0.58      0.60       322
I-O2_Saturation       0.65      0.87      0.75       217
I-Obesity       0.78      1.00      0.88         7
I-Oncological       0.85      0.91      0.88       741
I-Oxygen_Therapy       0.67      0.72      0.70       224
I-Pregnancy       0.57      0.62      0.59       115
I-Procedure       0.91      0.88      0.89      6231
I-Psychological_Condition       0.76      0.88      0.82        69
I-Pulse       0.82      0.82      0.82       278
I-RelativeDate       0.89      0.88      0.89       757
I-RelativeTime       0.70      0.80      0.74       227
I-Respiration       0.90      0.68      0.77       173
I-Route       0.98      0.92      0.95       359
I-Section_Header       0.96      0.98      0.97      7817
I-Sexually_Active_or_Sexual_Orientation       1.00      1.00      1.00         1
I-Smoking       0.67      0.50      0.57         4
I-Social_History_Header       0.91      1.00      0.95       200
I-Strength       0.85      0.89      0.87       761
I-Substance       0.70      0.90      0.79        21
I-Symptom       0.76      0.72      0.74      6496
I-Temperature       0.92      0.87      0.89       301
I-Test       0.84      0.86      0.85      3126
I-Test_Result       0.89      0.82      0.85      1676
I-Time       0.91      0.95      0.93       424
I-Total_Cholesterol       0.67      1.00      0.81        29
I-Treatment       0.68      0.62      0.65       196
I-Vaccine       0.89      0.96      0.92        25
I-Vital_Signs_Header       0.96      0.99      0.97       633
I-Weight       0.82      0.93      0.87       200
O       0.96      0.96      0.96    175897
accuracy        -         -        0.92    338378
macro-avg       0.76      0.74      0.74    338378
weighted-avg       0.92      0.92      0.92    338378
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk4MDQwOTY4XX0=
-->