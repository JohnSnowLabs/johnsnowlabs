---
layout: model
title: Detect Clinical Entities (clinical_medium)
author: John Snow Labs
name: ner_jsl_emb_clinical_medium
date: 2023-04-12
tags: [ner, licensed, clinical, en, clinical_medium]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terminology. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN. This model is the official version of jsl_ner_wip_clinical model.

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
- `Route`: Drug and medication administration routes available described by [FDA](http://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
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
- `Form`: Drug and medication forms available described by [FDA](http://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Drug_BrandName`: Commercial labeling name chosen by the labeler or the drug manufacturer for a drug containing a single or multiple drug active ingredients. 
- `Strength`: Potency of one unit of drug (or a combination of drugs) the measurement units available are described by [FDA](http://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
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
- `Dosage`: Quantity prescribed by the physician for an active ingredient; measurement units are available described by [FDA](http://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm). 
- `Overweight`: Terms related to the patient being overweight (BMI and Obesity is extracted separately). 
- `Hypertension`: All terms related to Hypertension (quantitative data such as 150/100 is extracted as Blood_Pressure). 
- `HDL`: Terms related to the lab test for HDL (High Density Lipoprotein). 
- `Total_Cholesterol`: Terms related to the lab test and results for cholesterol. 
- `Smoking`: All mentions of smoking status of a patient. 
- `Date`: Mentions of an exact date, in any format, including day number, month and/or year.

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Admission_Discharge`, `Death_Entity`, `Relationship_Status`, `Duration`, `Respiration`, `Hyperlipidemia`, `Birth_Entity`, `Age`, `Labour_Delivery`, `Family_History_Header`, `BMI`, `Temperature`, `Alcohol`, `Kidney_Disease`, `Oncological`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Oxygen_Therapy`, `O2_Saturation`, `Psychological_Condition`, `Heart_Disease`, `Employment`, `Obesity`, `Disease_Syndrome_Disorder`, `Pregnancy`, `ImagingFindings`, `Procedure`, `Medical_Device`, `Race_Ethnicity`, `Section_Header`, `Symptom`, `Treatment`, `Substance`, `Route`, `Drug_Ingredient`, `Blood_Pressure`, `Diet`, `External_body_part_or_region`, `LDL`, `VS_Finding`, `Allergen`, `EKG_Findings`, `Imaging_Technique`, `Triglycerides`, `RelativeTime`, `Gender`, `Pulse`, `Social_History_Header`, `Substance_Quantity`, `Diabetes`, `Modifier`, `Internal_organ_or_component`, `Clinical_Dept`, `Form`, `Drug_BrandName`, `Strength`, `Fetus_NewBorn`, `RelativeDate`, `Height`, `Test_Result`, `Sexually_Active_or_Sexual_Orientation`, `Frequency`, `Time`, `Weight`, `Vaccine`, `Vaccine_Name`, `Vital_Signs_Header`, `Communicable_Disease`, `Dosage`, `Overweight`, `Hypertension`, `HDL`, `Total_Cholesterol`, `Smoking`, `Date`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_JSL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_jsl_emb_clinical_medium_en_4.3.2_3.0_1681306334405.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_jsl_emb_clinical_medium_en_4.3.2_3.0_1681306334405.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"])\
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_jsl_emb_clinical_medium", "en", "clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")
    
ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter])


data = spark.createDataFrame([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.
"""]]).toDF("text")

result = ner_pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
        .setInputCol("text")
        .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
        .setInputCols("document") 
        .setOutputCol("sentence")

val tokenizer = new Tokenizer()
        .setInputCols("sentence")
        .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical_medium", "en", "clinical/models")
        .setInputCols(Array("sentence", "token"))
        .setOutputCol("embeddings")

val jsl_ner = MedicalNerModel.pretrained("ner_jsl_emb_clinical_medium", "en", "clinical/models")
        .setInputCols(Array("sentence", "token", "embeddings"))
        .setOutputCol("ner")

val jsl_ner_converter = new NerConverter()
        .setInputCols(Array("sentence", "token", "ner"))
        .setOutputCol("ner_chunk")

val jsl_ner_pipeline = new Pipeline().setStages(Array(
            documentAssembler, 
            sentenceDetector, 
            tokenizer, 
            embeddings, 
            jsl_ner, 
            jsl_ner_converter))


val data = Seq("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""").toDS.toDF("text")

val result = jsl_ner_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------------------------------+-----+---+----------------------------+
|chunk                                    |begin|end|ner_label                   |
+-----------------------------------------+-----+---+----------------------------+
|21-day-old                               |17   |26 |Age                         |
|Caucasian                                |28   |36 |Race_Ethnicity              |
|male                                     |38   |41 |Gender                      |
|2 days                                   |52   |57 |Duration                    |
|congestion                               |62   |71 |Symptom                     |
|mom                                      |75   |77 |Gender                      |
|suctioning yellow discharge              |88   |114|Symptom                     |
|nares                                    |135  |139|External_body_part_or_region|
|she                                      |147  |149|Gender                      |
|mild                                     |168  |171|Modifier                    |
|problems with his breathing while feeding|173  |213|Symptom                     |
|perioral cyanosis                        |237  |253|Symptom                     |
|retractions                              |258  |268|Symptom                     |
|Influenza vaccine                        |325  |341|Vaccine_Name                |
|One day ago                              |344  |354|RelativeDate                |
|mom                                      |357  |359|Gender                      |
|tactile temperature                      |376  |394|Symptom                     |
|Tylenol                                  |417  |423|Drug_BrandName              |
|Baby                                     |426  |429|Age                         |
|decreased p.o                            |449  |461|Symptom                     |
+-----------------------------------------+-----+---+----------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_jsl_emb_clinical_medium|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|15.2 MB|

## Benchmarking

```bash
                                label  precision    recall  f1-score   support
                      Drug_Ingredient       0.91      0.94      0.93      1905
            Disease_Syndrome_Disorder       0.85      0.89      0.87      4949
                       Drug_BrandName       0.94      0.92      0.93       963
                             Strength       0.95      0.93      0.94       759
                                Route       0.90      0.94      0.92       943
          Internal_organ_or_component       0.89      0.90      0.89     10310
                               Dosage       0.95      0.78      0.86       478
                            Frequency       0.90      0.87      0.88      1016
                            Treatment       0.90      0.70      0.78       332
                            Procedure       0.85      0.91      0.88      6433
                               Gender       0.98      0.99      0.99      5586
                         RelativeTime       0.79      0.70      0.74       306
                            Direction       0.91      0.90      0.91      4344
                             Modifier       0.84      0.82      0.83      2863
                              Symptom       0.84      0.83      0.84     11599
                                 Date       0.94      0.98      0.96       546
         External_body_part_or_region       0.89      0.85      0.87      3270
                       Section_Header       0.98      0.97      0.98      9320
                                  Age       0.85      0.92      0.88       757
                            Substance       0.91      0.85      0.88       113
                           VS_Finding       0.86      0.60      0.70       304
                       Medical_Device       0.87      0.93      0.90      5475
                       Oxygen_Therapy       0.89      0.85      0.87       117
                                 Test       0.87      0.87      0.87      4491
                             Diabetes       0.95      0.97      0.96       149
                             Duration       0.86      0.86      0.86      1009
                      ImagingFindings       0.83      0.50      0.63       353
                       Hyperlipidemia       0.80      0.87      0.84        47
                         Hypertension       0.97      0.94      0.96       152
                         RelativeDate       0.90      0.89      0.89      1338
                        Clinical_Dept       0.92      0.94      0.93      1771
                       Kidney_Disease       0.90      0.96      0.93       228
                        Heart_Disease       0.93      0.85      0.89       967
                                 Diet       0.67      0.62      0.65       106
                               Weight       0.93      0.93      0.93       254
                          Test_Result       0.79      0.81      0.80      1470
                                 Form       0.85      0.85      0.85       254
                                 Time       0.80      0.72      0.76        76
              Psychological_Condition       0.81      0.76      0.79       187
                  Injury_or_Poisoning       0.84      0.80      0.82       889
                  Admission_Discharge       0.91      0.97      0.94       301
                      Labour_Delivery       0.74      0.73      0.73       110
                           Employment       0.90      0.73      0.81       389
                              Vaccine       0.83      0.33      0.48        15
                              Obesity       0.92      0.91      0.92        54
                          Oncological       0.92      0.93      0.93       784
                              Smoking       0.96      0.94      0.95       106
                    Imaging_Technique       0.70      0.53      0.60        98
                       Blood_Pressure       0.86      0.87      0.86       314
                                Pulse       0.87      0.92      0.89       278
                          Respiration       0.96      0.94      0.95       180
                        O2_Saturation       0.86      0.77      0.81        96
               Medical_History_Header       0.93      0.99      0.96       396
                    Total_Cholesterol       0.88      0.37      0.52        19
              Cerebrovascular_Disease       0.75      0.78      0.76       108
                            Pregnancy       0.90      0.71      0.79       201
                         Death_Entity       0.85      0.76      0.80        46
                         EKG_Findings       0.78      0.43      0.56       186
                       Race_Ethnicity       0.97      0.99      0.98       118
                Family_History_Header       0.97      0.99      0.98       273
                              Alcohol       0.84      0.95      0.89        84
                        Fetus_NewBorn       0.75      0.54      0.63       235
                   Vital_Signs_Header       0.96      0.94      0.95       710
                  Relationship_Status       0.93      0.95      0.94        41
                               Height       0.98      0.85      0.91        68
                          Temperature       0.91      0.96      0.94       141
                        Triglycerides       0.40      0.40      0.40        10
                                  LDL       0.94      0.68      0.79        22
                Social_History_Header       0.98      0.97      0.98       259
                 Communicable_Disease       0.79      0.62      0.70        50
                           Overweight       0.86      0.86      0.86         7
                             Allergen       0.00      0.00      0.00        23
                   Substance_Quantity       0.33      1.00      0.50         2
                         Vaccine_Name       0.68      1.00      0.81        15
                         Birth_Entity       0.00      0.00      0.00         3
                                  BMI       1.00      0.67      0.80        15
Sexually_Active_or_Sexual_Orientation       1.00      0.80      0.89         5
                                  HDL       1.00      1.00      1.00         2
                            micro-avg       0.89      0.89      0.89     92193
                            macro-avg       0.85      0.81      0.82     92193
                         weighted-avg       0.89      0.89      0.89     92193
```