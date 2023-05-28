---
layout: model
title: Detect Clinical Entities (BertForTokenClassifier)
author: John Snow Labs
name: bert_token_classifier_ner_jsl
date: 2023-05-01
tags: [berfortokenclassification, ner_jsl, ner, en, licensed, tensorflow]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
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

## Predicted Entities

`Injury_or_Poisoning`, `Direction`, `Test`, `Admission_Discharge`, `Death_Entity`, `Relationship_Status`, `Duration`, `Respiration`, `Hyperlipidemia`, `Birth_Entity`, `Age`, `Labour_Delivery`, `Family_History_Header`, `BMI`, `Temperature`, `Alcohol`, `Kidney_Disease`, `Oncological`, `Medical_History_Header`, `Cerebrovascular_Disease`, `Oxygen_Therapy`, `O2_Saturation`, `Psychological_Condition`, `Heart_Disease`, `Employment`, `Obesity`, `Disease_Syndrome_Disorder`, `Pregnancy`, `ImagingFindings`, `Procedure`, `Medical_Device`, `Race_Ethnicity`, `Section_Header`, `Symptom`, `Treatment`, `Substance`, `Route`, `Drug_Ingredient`, `Blood_Pressure`, `Diet`, `External_body_part_or_region`, `LDL`, `VS_Finding`, `Allergen`, `EKG_Findings`, `Imaging_Technique`, `Triglycerides`, `RelativeTime`, `Gender`, `Pulse`, `Social_History_Header`, `Substance_Quantity`, `Diabetes`, `Modifier`, `Internal_organ_or_component`, `Clinical_Dept`, `Form`, `Drug_BrandName`, `Strength`, `Fetus_NewBorn`, `RelativeDate`, `Height`, `Test_Result`, `Sexually_Active_or_Sexual_Orientation`, `Frequency`, `Time`, `Weight`, `Vaccine`, `Vaccine_Name`, `Vital_Signs_Header`, `Communicable_Disease`, `Dosage`, `Overweight`, `Hypertension`, `HDL`, `Total_Cholesterol`, `Smoking`, `Date`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_JSL/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_4.3.2_3.0_1682934532927.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_en_4.3.2_3.0_1682934532927.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_converter = NerConverter()\
  .setInputCols(["sentence","token","ner"])\
  .setOutputCol("ner_chunk")

pipeline =  Pipeline(stages=[
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter])
						       

sample_text = """The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""

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

val ner_converter = new NerConverter()
	.setInputCols(Array("sentence","token","ner"))
	.setOutputCol("ner_chunk")

val pipeline =  new Pipeline().setStages(Array(
		documentAssembler,
		sentenceDetector,
		tokenizer,
		tokenClassifier,
		ner_converter))
												
val sample_text = Seq("""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.""").toDS.toDF("text")

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
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|444.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|