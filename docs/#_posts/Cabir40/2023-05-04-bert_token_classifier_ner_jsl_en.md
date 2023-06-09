---
layout: model
title: Detect Clinical Entities (BertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_jsl
date: 2023-05-04
tags: [licensed, en, clinical, jsl, ner, berfortokenclassification, tensorflow]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 3.4.0
spark_version: 3.0
supported: true
recommended: true
engine: tensorflow
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terminology. This model is trained with BertForTokenClassification method from transformers library and imported into Spark NLP. 

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

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_3.4.0_3.0_1683228461283.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_3.4.0_3.0_1683228461283.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
documentAssembler = DocumentAssembler()\
	.setInputCol("text")\
	.setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
  .setInputCols(["document"])\
  .setOutputCol("sentence")

tokenizer = Tokenizer()\
  .setInputCols("sentence")\
  .setOutputCol("token")

tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_jsl", "en", "clinical/models")\
  .setInputCols(["token", "sentence"])\
  .setOutputCol("ner")\
  .setCaseSensitive(True)

ner_converter = NerConverterInternal()\
  .setInputCols(["sentence","token","ner"])\
  .setOutputCol("ner_chunk")

pipeline =  Pipeline(stages=[
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter])
						       

sample_text = "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."

df = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(df).transform(df)

```
```scala

val documentAssembler = new DocumentAssembler()
	.setInputCol("text")
	.setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val tokenizer = new Tokenizer()
	.setInputCols("sentence")
	.setOutputCol("token")
		
val tokenClassifier = MedicalBertForTokenClassifier.pretrained("bert_token_classifier_ner_jsl", "en", "clinical/models")
  .setInputCols(Array("token", "sentence"))
  .setOutputCol("ner")
  .setCaseSensitive(True)

val ner_converter = new NerConverterInternal()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")

val pipeline =  new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter))
												
val sample_text = Seq("The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.").toDS.toDF("text")

val result = pipeline.fit(sample_text).transform(sample_text)

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
|yellow                                   |Symptom                     |
|discharge                                |Symptom                     |
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
|Baby-girl                                |Age                         |
|decreased                                |Symptom                     |
+-----------------------------------------+----------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jsl|
|Compatibility:|Healthcare NLP 3.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|408.3 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## Benchmarking

```bash
                                  label  precision    recall  f1-score   support
                  B-Admission_Discharge       0.87      0.98      0.92       421
                                  B-Age       0.97      0.97      0.97      2143
                              B-Alcohol       0.90      0.85      0.87       101
                             B-Allergen       0.29      0.32      0.30        31
                                  B-BMI       0.77      0.77      0.77        13
                         B-Birth_Entity       0.30      0.60      0.40         5
                       B-Blood_Pressure       0.84      0.86      0.85       193
              B-Cerebrovascular_Disease       0.63      0.81      0.71       176
                        B-Clinical_Dept       0.88      0.91      0.90      1459
                 B-Communicable_Disease       0.78      0.84      0.81        50
                                 B-Date       0.97      0.99      0.98      1393
                         B-Death_Entity       0.71      0.82      0.76        44
                             B-Diabetes       0.95      0.97      0.96       145
                                 B-Diet       0.67      0.51      0.58       112
                            B-Direction       0.90      0.93      0.91      5617
            B-Disease_Syndrome_Disorder       0.89      0.89      0.89      7569
                               B-Dosage       0.75      0.79      0.77       333
                       B-Drug_BrandName       0.95      0.93      0.94      3165
                      B-Drug_Ingredient       0.92      0.94      0.93      5134
                             B-Duration       0.81      0.84      0.82       389
                         B-EKG_Findings       0.63      0.46      0.53       145
                           B-Employment       0.87      0.91      0.89       406
         B-External_body_part_or_region       0.83      0.85      0.84      3647
                B-Family_History_Header       1.00      1.00      1.00       333
                        B-Fetus_NewBorn       0.64      0.70      0.67       166
                                 B-Form       0.81      0.79      0.80       334
                            B-Frequency       0.93      0.95      0.94      1343
                               B-Gender       0.99      0.99      0.99      5644
                                  B-HDL       0.55      1.00      0.71         6
                        B-Heart_Disease       0.88      0.89      0.89      1052
                               B-Height       1.00      0.73      0.84        26
                       B-Hyperlipidemia       0.97      0.99      0.98       236
                         B-Hypertension       0.97      0.98      0.97       506
                      B-ImagingFindings       0.50      0.46      0.48       187
                    B-Imaging_Technique       0.90      0.78      0.84        95
                  B-Injury_or_Poisoning       0.87      0.84      0.86       793
          B-Internal_organ_or_component       0.89      0.90      0.89     14484
                       B-Kidney_Disease       0.83      0.79      0.81       201
                                  B-LDL       1.00      1.00      1.00        12
                      B-Labour_Delivery       0.67      0.72      0.69       129
                       B-Medical_Device       0.88      0.91      0.89      7574
               B-Medical_History_Header       0.97      0.98      0.98       218
                             B-Modifier       0.83      0.83      0.83      4226
                        B-O2_Saturation       0.74      0.68      0.71        59
                              B-Obesity       0.81      0.81      0.81       108
                          B-Oncological       0.94      0.93      0.94       917
                           B-Overweight       1.00      0.80      0.89        10
                       B-Oxygen_Therapy       0.74      0.84      0.79       148
                            B-Pregnancy       0.82      0.80      0.81       279
                            B-Procedure       0.90      0.91      0.91      8012
              B-Psychological_Condition       0.78      0.87      0.82       245
                                B-Pulse       0.88      0.93      0.90       152
                       B-Race_Ethnicity       0.99      1.00      0.99       157
                  B-Relationship_Status       0.89      0.93      0.91        44
                         B-RelativeDate       0.81      0.83      0.82       630
                         B-RelativeTime       0.66      0.62      0.64       167
                          B-Respiration       0.93      0.97      0.95       131
                                B-Route       0.85      0.90      0.87      1430
                       B-Section_Header       0.98      0.98      0.98     15527
B-Sexually_Active_or_Sexual_Orientation       0.83      0.56      0.67         9
                              B-Smoking       0.94      0.92      0.93       186
                B-Social_History_Header       0.90      1.00      0.95       401
                             B-Strength       0.91      0.94      0.93       721
                            B-Substance       0.98      0.88      0.93       160
                              B-Symptom       0.88      0.88      0.88     13889
                          B-Temperature       0.92      0.94      0.93       161
                                 B-Test       0.86      0.90      0.88      5336
                          B-Test_Result       0.86      0.87      0.87      2240
                                 B-Time       0.74      0.87      0.80        68
                    B-Total_Cholesterol       0.66      0.72      0.69        29
                            B-Treatment       0.79      0.75      0.77       391
                        B-Triglycerides       1.00      1.00      1.00        22
                           B-VS_Finding       0.80      0.86      0.83       555
                              B-Vaccine       0.62      0.71      0.67        35
                         B-Vaccine_Name       0.65      0.75      0.70        20
                   B-Vital_Signs_Header       0.92      0.96      0.94      1131
                               B-Weight       0.70      0.76      0.73        90
                                  I-Age       0.83      0.79      0.81       202
                              I-Alcohol       0.50      0.25      0.33         8
                             I-Allergen       0.25      0.50      0.33         2
                                  I-BMI       0.71      0.74      0.73        27
                       I-Blood_Pressure       0.91      0.92      0.91       476
              I-Cerebrovascular_Disease       0.48      0.79      0.59        66
                        I-Clinical_Dept       0.93      0.94      0.94       878
                 I-Communicable_Disease       0.29      0.71      0.42         7
                                 I-Date       0.91      0.95      0.93       136
                         I-Death_Entity       0.33      0.50      0.40         2
                             I-Diabetes       0.97      0.95      0.96        81
                                 I-Diet       0.65      0.54      0.59        80
                            I-Direction       0.81      0.80      0.80       353
            I-Disease_Syndrome_Disorder       0.88      0.86      0.87      4633
                               I-Dosage       0.85      0.80      0.82       266
                       I-Drug_BrandName       0.78      0.64      0.70        67
                      I-Drug_Ingredient       0.80      0.85      0.82       437
                             I-Duration       0.87      0.92      0.89       802
                         I-EKG_Findings       0.68      0.50      0.58       209
                           I-Employment       0.77      0.77      0.77       141
         I-External_body_part_or_region       0.79      0.81      0.80      1063
                I-Family_History_Header       0.99      1.00      0.99       424
                        I-Fetus_NewBorn       0.63      0.55      0.59       154
                            I-Frequency       0.84      0.79      0.82       510
                               I-Gender       0.43      0.30      0.35        10
                                  I-HDL       0.50      1.00      0.67         3
                        I-Heart_Disease       0.89      0.88      0.88      1120
                               I-Height       0.95      0.94      0.95        66
                         I-Hypertension       0.33      0.32      0.33        22
                      I-ImagingFindings       0.61      0.59      0.60       256
                    I-Imaging_Technique       0.86      0.83      0.84        59
                  I-Injury_or_Poisoning       0.78      0.76      0.77       616
          I-Internal_organ_or_component       0.89      0.89      0.89      6723
                       I-Kidney_Disease       0.88      0.92      0.90       223
                                  I-LDL       1.00      1.00      1.00         8
                      I-Labour_Delivery       0.65      0.77      0.70       124
                       I-Medical_Device       0.88      0.92      0.90      4220
               I-Medical_History_Header       1.00      0.99      0.99       939
                             I-Modifier       0.63      0.59      0.61       305
                        I-O2_Saturation       0.88      0.80      0.84       110
                              I-Obesity       0.68      0.65      0.67        20
                          I-Oncological       0.94      0.92      0.93       692
                       I-Oxygen_Therapy       0.77      0.75      0.76        61
                            I-Pregnancy       0.59      0.68      0.63       143
                            I-Procedure       0.91      0.90      0.90      7483
              I-Psychological_Condition       0.76      0.82      0.79        77
                                I-Pulse       0.92      0.90      0.91       226
                       I-Race_Ethnicity       1.00      1.00      1.00         1
                         I-RelativeDate       0.83      0.90      0.86       890
                         I-RelativeTime       0.73      0.68      0.71       233
                          I-Respiration       0.98      0.93      0.96       117
                                I-Route       0.90      0.90      0.90       375
                       I-Section_Header       0.97      0.98      0.98     12864
I-Sexually_Active_or_Sexual_Orientation       0.57      1.00      0.73         4
                              I-Smoking       0.40      0.33      0.36         6
                I-Social_History_Header       0.92      0.99      0.95       478
                             I-Strength       0.86      0.94      0.90       502
                            I-Substance       0.84      0.76      0.80        50
                              I-Symptom       0.78      0.75      0.77      7167
                          I-Temperature       0.97      0.99      0.98       233
                                 I-Test       0.81      0.85      0.83      3038
                          I-Test_Result       0.59      0.63      0.61       413
                                 I-Time       0.80      0.80      0.80        71
                    I-Total_Cholesterol       0.82      0.86      0.84        43
                            I-Treatment       0.72      0.73      0.73       187
                        I-Triglycerides       0.87      1.00      0.93        20
                           I-VS_Finding       0.55      0.59      0.57        86
                              I-Vaccine       1.00      0.67      0.80         6
                         I-Vaccine_Name       0.86      1.00      0.92        18
                   I-Vital_Signs_Header       0.94      0.97      0.96      1063
                               I-Weight       0.93      0.88      0.90       237
                                      O       0.97      0.96      0.97    200407
                               accuracy        -         -        0.93    386755
                              macro-avg       0.77      0.79      0.77    386755
                           weighted-avg       0.93      0.93      0.93    386755
```
