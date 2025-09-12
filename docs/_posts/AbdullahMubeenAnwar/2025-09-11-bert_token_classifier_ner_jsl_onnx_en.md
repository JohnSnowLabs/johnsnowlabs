---
layout: model
title: Detect Clinical Entities (BertForTokenClassifier - ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_jsl_onnx
date: 2025-09-11
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained **Named Entity Recognition (NER)** model identifies a wide range of clinical concepts from unstructured text.  

Predicted Entities and Definitions:

- **Injury_or_Poisoning** — Mentions of physical harm, accidents, falls, or poisoning (patient or others).  
- **Direction** — Laterality of internal and external organs (e.g., left, right, bilateral).  
- **Test** — Laboratory, pathology, or radiological tests.  
- **Admission_Discharge** — Terms indicating patient admission or discharge.  
- **Death_Entity** — Mentions related to patient death.  
- **Relationship_Status** — Social or marital status (e.g., single, married, divorced).  
- **Duration** — Duration of treatments or medication use.  
- **Respiration** — Mentions of respiratory rate (breaths per minute).  
- **Hyperlipidemia** — Mentions of hyperlipidemia, including subtypes and synonyms.  
- **Birth_Entity** — Mentions of childbirth.  
- **Age** — Mentions of age (past or present, patient or others).  
- **Labour_Delivery** — Stages of labor and delivery.  
- **Family_History_Header** — Section headers for family history.  
- **BMI** — Mentions of Body Mass Index values or related text.  
- **Temperature** — Mentions of body temperature.  
- **Alcohol** — Mentions of alcohol use, abuse, or related issues.  
- **Kidney_Disease** — Mentions of kidney diseases (acute, chronic, etc.).  
- **Oncological** — Mentions of cancer, tumors, or metastasis.  
- **Medical_History_Header** — Section headers for past medical history.  
- **Cerebrovascular_Disease** — Mentions of cerebrovascular disease or events.  
- **Oxygen_Therapy** — Mentions of breathing support (ventilator, CPAP, BPAP).  
- **O2_Saturation** — Mentions of oxygen saturation levels.  
- **Psychological_Condition** — Mentions of mental health conditions, disorders, or syndromes.  
- **Heart_Disease** — Mentions of acquired, congenital, or degenerative heart disease.  
- **Employment** — Mentions of occupations or employment status.  
- **Obesity** — Mentions of obesity (distinct from overweight/BMI).  
- **Disease_Syndrome_Disorder** — General disease mentions (excluding those with specific labels like Heart_Disease).  
- **Pregnancy** — Pregnancy-related terms (excluding specific labels like Labour_Delivery).  
- **ImagingFindings** — Radiographic or imaging findings.  
- **Procedure** — Mentions of invasive medical or surgical procedures.  
- **Medical_Device** — Mentions of medical devices and supplies.  
- **Race_Ethnicity** — Mentions of racial, ethnic, or sociocultural groups.  
- **Section_Header** — Generic section headers (excluding specific ones with their own labels).  
- **Symptom** — Mentions of symptoms (patient or others).  
- **Treatment** — Mentions of therapeutic or minimally invasive treatments (excludes invasive “Procedure”).  
- **Substance** — Mentions of recreational/illicit drug use.  
- **Route** — Medication administration routes. ([FDA reference](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm))  
- **Drug_Ingredient** — Active ingredients in drug products.  
- **Blood_Pressure** — Mentions of blood pressure (systolic, diastolic, MAP).  
- **Diet** — Mentions of dietary habits.  
- **External_body_part_or_region** — Mentions of external body parts/organs (visible).  
- **LDL** — Mentions of LDL lab tests/results.  
- **VS_Finding** — Vital sign–related qualitative findings (e.g., fever, cyanosis, tachycardia).  
- **Allergen** — Mentions of allergens.  
- **EKG_Findings** — Mentions of EKG readings.  
- **Imaging_Technique** — Mentions of radiographic views or imaging techniques.  
- **Triglycerides** — Mentions of triglyceride lab tests.  
- **RelativeTime** — Relative time references (e.g., “in the morning,” “approximately”).  
- **Gender** — Gender-specific nouns and pronouns.  
- **Pulse** — Mentions of heart rate (without detailed context).  
- **Social_History_Header** — Section headers for social history.  
- **Substance_Quantity** — Quantitative mentions of substance (illicit/recreational drugs).  
- **Diabetes** — Mentions of diabetes mellitus.  
- **Modifier** — Modifiers of symptoms/diseases (unless part of ICD-10 disease name).  
- **Internal_organ_or_component** — Mentions of internal organs (not visible externally).  
- **Clinical_Dept** — Mentions of medical/surgical departments.  
- **Form** — Drug/medication forms. ([FDA reference](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm))  
- **Drug_BrandName** — Commercial brand names of drugs.  
- **Strength** — Drug strength/potency. ([FDA reference](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm))  
- **Fetus_NewBorn** — Mentions of fetus, infant, newborn (excluding labels like Pregnancy).  
- **RelativeDate** — Date references relative to another event (e.g., “two years ago”).  
- **Height** — Mentions of patient height.  
- **Test_Result** — Mentions of clinical test results.  
- **Sexually_Active_or_Sexual_Orientation** — Mentions of sexual activity or orientation.  
- **Frequency** — Frequency of prescribed doses.  
- **Time** — Specific time mentions (hours, minutes).  
- **Weight** — Mentions of patient weight.  
- **Vaccine** — Mentions of vaccines or vaccination procedures.  
- **Vital_Signs_Header** — Section headers for vital signs.  
- **Communicable_Disease** — Mentions of communicable diseases.  
- **Dosage** — Prescribed drug dosage. ([FDA reference](https://wayback.archive-it.org/7993/20171115111313/https:/www.fda.gov/Drugs/DevelopmentApprovalProcess/FormsSubmissionRequirements/ElectronicSubmissions/DataStandardsManualmonographs/ucm071667.htm))  
- **Overweight** — Mentions of overweight (distinct from BMI/obesity).  
- **Hypertension** — Mentions of hypertension (quantitative values extracted separately as Blood_Pressure).  
- **HDL** — Mentions of HDL lab test results.  
- **Total_Cholesterol** — Mentions of cholesterol lab tests/results.  
- **Smoking** — Mentions of smoking status.  
- **Date** — Explicit dates (any format).

## Predicted Entities

`I-Symptom`, `B-Diabetes`, `B-Fetus_NewBorn`, `I-Modifier`, `B-Symptom`, `I-Internal_organ_or_component`, `I-Injury_or_Poisoning`, `B-Total_Cholesterol`, `I-ImagingFindings`, `B-Hypertension`, `B-Allergen`, `I-Height`, `B-Blood_Pressure`, `I-Route`, `I-O2_Saturation`, `I-Race_Ethnicity`, `I-Allergen`, `B-Substance`, `I-Overweight`, `I-Test_Result`, `I-Labour_Delivery`, `B-Dosage`, `B-Social_History_Header`, `B-Cerebrovascular_Disease`, `B-RelativeDate`, `I-Respiration`, `O`, `I-Form`, `B-Race_Ethnicity`, `B-Drug_Ingredient`, `B-Route`, `B-Sexually_Active_or_Sexual_Orientation`, `I-Blood_Pressure`, `I-Social_History_Header`, `I-Vaccine_Name`, `B-Time`, `B-BMI`, `I-Communicable_Disease`, `B-Triglycerides`, `I-Treatment`, `B-Test_Result`, `B-O2_Saturation`, `B-Height`, `I-Oxygen_Therapy`, `I-External_body_part_or_region`, `I-Strength`, `B-Psychological_Condition`, `B-Death_Entity`, `I-RelativeDate`, `I-Frequency`, `I-Hypertension`, `B-Oxygen_Therapy`, `B-Form`, `I-LDL`, `I-Diabetes`, `I-Drug_Ingredient`, `I-Smoking`, `I-Vital_Signs_Header`, `I-HDL`, `B-Medical_Device`, `B-Overweight`, `B-RelativeTime`, `I-Temperature`, `B-Internal_organ_or_component`, `I-Pregnancy`, `B-EKG_Findings`, `I-Fetus_NewBorn`, `B-Vital_Signs_Header`, `B-Pregnancy`, `B-Smoking`, `I-Age`, `B-Communicable_Disease`, `B-Test`, `B-Family_History_Header`, `I-Clinical_Dept`, `I-VS_Finding`, `B-Diet`, `B-Drug_BrandName`, `I-Medical_Device`, `I-Imaging_Technique`, `B-Oncological`, `B-Date`, `I-Disease_Syndrome_Disorder`, `I-Substance_Quantity`, `B-VS_Finding`, `I-Admission_Discharge`, `B-Modifier`, `B-Age`, `B-Vaccine`, `B-Disease_Syndrome_Disorder`, `B-External_body_part_or_region`, `B-Birth_Entity`, `I-Drug_BrandName`, `B-Employment`, `I-Dosage`, `I-Section_Header`, `B-Labour_Delivery`, `B-Kidney_Disease`, `I-Heart_Disease`, `I-Direction`, `I-Sexually_Active_or_Sexual_Orientation`, `B-Section_Header`, `B-Procedure`, `I-Gender`, `I-Employment`, `I-Weight`, `B-Strength`, `I-Diet`, `B-Imaging_Technique`, `B-HDL`, `I-Date`, `I-Duration`, `B-Admission_Discharge`, `B-Obesity`, `B-Gender`, `B-Alcohol`, `I-Substance`, `I-Medical_History_Header`, `B-Duration`, `I-Psychological_Condition`, `I-Family_History_Header`, `I-Total_Cholesterol`, `B-Frequency`, `I-Test`, `I-Procedure`, `B-Weight`, `I-Oncological`, `B-Temperature`, `B-Respiration`, `I-Triglycerides`, `I-Alcohol`, `B-Vaccine_Name`, `B-Pulse`, `B-Direction`, `B-Relationship_Status`, `B-Treatment`, `I-Obesity`, `I-Cerebrovascular_Disease`, `I-Hyperlipidemia`, `I-Time`, `B-Clinical_Dept`, `I-Kidney_Disease`, `B-Heart_Disease`, `I-BMI`, `B-Injury_or_Poisoning`, `B-Hyperlipidemia`, `I-EKG_Findings`, `B-Substance_Quantity`, `I-Relationship_Status`, `I-Vaccine`, `I-Death_Entity`, `I-Pulse`, `B-ImagingFindings`, `B-Medical_History_Header`, `B-LDL`, `I-RelativeTime`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_onnx_en_6.1.1_3.0_1757557797951.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_jsl_onnx_en_6.1.1_3.0_1757557797951.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_jsl_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import com.johnsnowlabs.nlp.annotators.sentence_detector_dl.SentenceDetectorDLApproach
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols(["document"])
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_jsl_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby-girl also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------------------------+----------------------------+
|text                                     |entity                      |
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
|decreased                                |Symptom                     |
|intake                                   |Symptom                     |
+-----------------------------------------+----------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_jsl_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|404.1 MB|
|Case sensitive:|true|
|Max sentence length:|128|