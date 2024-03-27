---
layout: model
title: Detect Opioid Specific Entities
author: John Snow Labs
name: ner_opioid
date: 2024-03-27
tags: [licensed, en, clinical, ner, opioid]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to detect and label opioid related entities within text data. Opioids are a class of drugs that include the illegal drug heroin, synthetic opioids such as fentanyl, and pain relievers available legally by prescription. The model has been trained using advanced deep learning techniques on a diverse range of text sources and can accurately recognize and classify a wide range of opioid-related entities. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results.

Here are the labels of the OPIOID model with their descriptions:

- `communicable_disease`: Communicable disease is a disease that people spread to one another through contact with contaminated surfaces, bodily fluids, blood products, insect bites, or through the air.
- `general_symptoms`: Include all the symptoms,vital findings and signs mentioned in the document, of the patient or someone else.
- `substance_use_disorder` : Mentions of substance use that include unspecific illicit drug abuse.
- `drug_duration`: The duration for which the drug was taken or prescribed.
- `psychiatric_issue`: Psychiatric disorders may also be referred to as mental health conditions is a behavioral or mental pattern that causes significant distress or impairment of personal functioning. A mental disorder is also characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behavior. It is usually associated with distress or impairment in important areas of functioning.
- `drug_strength`: The potency of one unit of drug (or a combination of drugs, generally speaking); the measurement units available are described by FDA.
- `drug_quantity`: The quantity associated with drug dosage.
- `other_drug`: Any generic or trade name of the drugs in the text other than the opioids.
- `drug_form`: The dosage forms available are described by FDA.
- `drug_frequency`: The frequency at which the drug doses are given or being used.
- `opioid_drug`: Any drug mentioned in the text that belongs to the opioid family either legally by prescription as pain relievers like fentanyl, oxycodone, hydrocodone, codeine, morphine, Oxymorphone, Hydromorphone, Methadone, Tramadol, Buprenorphine or illegal street drug like “heroin”.
- `drug_route`: The administration routes available are described by FDA.
- `employment`: Patient occupational titles. Includes "unemployed" and "retired".
- `violence`: Refers to any violent behavior towards self or others.
- `legal_issue`: Any problem, mention, act, or matter that related to crime and/or requires resolution within the legal framework.
- `other_disease`: Include all the diseases mentioned in the document, of the patient or someone else. 
- `alcohol_use`:  Mentions of alcohol drinking habit. 
- `test`: This label is assigned to entities representing tests conducted to detect the presence of drugs or substances in urine, blood, or saliva of the patient. 
- `marital_status`: Marital status examples like: Married, single, widowed, divorced, separated and registered partnership.
- `test_result`: This label is assigned to entities representing the outcome of a drug screening test, indicating whether specific drugs or substances were detected (positive) or not detected (negative) in an individual's system.
- `antidote`: Antidote is a medicine that rapidly reverses an opioid overdose like Naloxone, Kloxxado, Narcan, Evzio, Zimhi and it is not a treatment for opioid use disorder.
- `sexual_orientation`:  Sexual orientations include gay, lesbian, straight, bisexual, and asexual.

## Predicted Entities

`communicable_disease`, `general_symptoms`, `substance_use_disorder`, `drug_duration`, `psychiatric_issue`, `drug_strength`, `drug_quantity`, `other_drug`, `drug_form`, `drug_frequency`, `opioid_drug`, `drug_route`, `employment`, `violence`, `legal_issue`, `other_disease`, `alcohol_use`, `test`, `marital_status`, `test_result`, `antidote`, `sexual_orientation`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/OPIOID/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/OPIOID.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_opioid_en_5.3.0_3.0_1711516211243.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_opioid_en_5.3.0_3.0_1711516211243.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_opioid", "en", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
    ])


sample_texts = ["""History of Present Illness: A 20-year-old male was transferred from an outside hospital for evaluation for liver transplant following a Percocet overdose. On Sunday, March 27th, he experienced a stressful day and consumed approximately 20 Percocet (5/325) tablets throughout the day following a series of family arguments. He denies any intent to harm himself, although his parents confirm past suicidal attempts. On Monday, he felt he was experiencing a Percocet withdrawal "hangover" and took an additional 5 Percocet. He was admitted to the Surgical Intensive Care Unit (SICU) and received care from Liver, Transplant, Toxicology. Treatment included Naloxone every 4 hours, resulting in a gradual improvement in liver function tests (LFTs) and INR. During recovery, he developed hypertension and was initiated on clonidine.
Past Medical History: The patient has a history of Bipolar Disorder (with previous suicide attempts), ADHD, and a prior head injury resulting from an assault. He also has a history of a motor vehicle accident (MVA) resulting in a large L3 transverse process fracture and a small right frontal epidural hemorrhage.
Social History: The patient is single with no children, and works at a bar. He spent three years living in a group home during his teenage years. He consumes alcohol once a week but denies any illicit drug use. The patient's HIV and Hepatitis C status is negative. He is currently being evaluated neurologically
Latest toxicology results: BLOOD ASA - negative, Ethanol - negative,  Acetaminophen - negative, Benzodiazepines - negative, Barbiturates - negative."""]


data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val clinical_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_opioid", "en", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentenceDetector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter   
))

val sample_texts = Seq("""History of Present Illness: A 20-year-old male was transferred from an outside hospital for evaluation for liver transplant following a Percocet overdose. On Sunday, March 27th, he experienced a stressful day and consumed approximately 20 Percocet (5/325) tablets throughout the day following a series of family arguments. He denies any intent to harm himself, although his parents confirm past suicidal attempts. On Monday, he felt he was experiencing a Percocet withdrawal "hangover" and took an additional 5 Percocet. He was admitted to the Surgical Intensive Care Unit (SICU) and received care from Liver, Transplant, Toxicology. Treatment included Naloxone every 4 hours, resulting in a gradual improvement in liver function tests (LFTs) and INR. During recovery, he developed hypertension and was initiated on clonidine.
Past Medical History: The patient has a history of Bipolar Disorder (with previous suicide attempts), ADHD, and a prior head injury resulting from an assault. He also has a history of a motor vehicle accident (MVA) resulting in a large L3 transverse process fracture and a small right frontal epidural hemorrhage.
Social History: The patient is single with no children, and works at a bar. He spent three years living in a group home during his teenage years. He consumes alcohol once a week but denies any illicit drug use. The patient's HIV and Hepatitis C status is negative. He is currently being evaluated neurologically
Latest toxicology results: BLOOD ASA - negative, Ethanol - negative,  Acetaminophen - negative, Benzodiazepines - negative, Barbiturates - negative.""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+---------------------------+-----+----+----------------------+
|chunk                      |begin|end |ner_label             |
+---------------------------+-----+----+----------------------+
|Percocet                   |136  |143 |opioid_drug           |
|overdose                   |145  |152 |other_disease         |
|20                         |236  |237 |drug_quantity         |
|Percocet                   |239  |246 |opioid_drug           |
|tablets                    |256  |262 |drug_form             |
|harm himself               |347  |358 |violence              |
|suicidal attempts          |395  |411 |psychiatric_issue     |
|Percocet                   |455  |462 |opioid_drug           |
|withdrawal                 |464  |473 |general_symptoms      |
|hangover                   |476  |483 |general_symptoms      |
|5                          |509  |509 |drug_quantity         |
|Percocet                   |511  |518 |opioid_drug           |
|Naloxone                   |653  |660 |antidote              |
|every 4 hours              |662  |674 |drug_frequency        |
|hypertension               |782  |793 |other_disease         |
|clonidine                  |816  |824 |other_drug            |
|Bipolar Disorder           |878  |893 |psychiatric_issue     |
|suicide attempts           |910  |925 |psychiatric_issue     |
|ADHD                       |929  |932 |psychiatric_issue     |
|head injury                |947  |957 |other_disease         |
|assault                    |977  |983 |violence              |
|transverse process fracture|1066 |1092|other_disease         |
|epidural hemorrhage        |1120 |1138|general_symptoms      |
|single                     |1172 |1177|marital_status        |
|works at a bar             |1201 |1214|employment            |
|alcohol                    |1299 |1305|alcohol_use           |
|illicit drug use           |1334 |1349|substance_use_disorder|
|HIV                        |1366 |1368|communicable_disease  |
|Hepatitis C                |1374 |1384|communicable_disease  |
|toxicology                 |1460 |1469|test                  |
|BLOOD ASA                  |1480 |1488|test                  |
|negative                   |1492 |1499|test_result           |
|Ethanol                    |1502 |1508|test                  |
|negative                   |1512 |1519|test_result           |
|Acetaminophen              |1523 |1535|test                  |
|negative                   |1539 |1546|test_result           |
|Benzodiazepines            |1549 |1563|test                  |
|negative                   |1567 |1574|test_result           |
|Barbiturates               |1577 |1588|test                  |
|negative                   |1592 |1599|test_result           |
+---------------------------+-----+----+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_opioid|
|Compatibility:|Healthcare NLP 5.3.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
           alcohol_use       0.92      0.95      0.94       353
              antidote       1.00      0.99      0.99       141
  communicable_disease       0.76      0.88      0.82       224
         drug_duration       0.81      0.71      0.75       238
             drug_form       0.97      0.95      0.96       614
        drug_frequency       0.94      0.97      0.96      1527
         drug_quantity       0.96      0.94      0.95      2169
            drug_route       0.95      0.98      0.97       903
         drug_strength       0.84      0.95      0.89       388
            employment       0.79      0.63      0.70       306
      general_symptoms       0.90      0.84      0.87      4483
           legal_issue       0.73      0.52      0.61        84
        marital_status       0.95      0.95      0.95        57
           opioid_drug       0.98      0.96      0.97       725
         other_disease       0.91      0.90      0.90      4145
            other_drug       0.94      0.93      0.94      2617
     psychiatric_issue       0.88      0.85      0.86      1356
    sexual_orientation       1.00      0.78      0.88        23
substance_use_disorder       0.91      0.88      0.90       276
                  test       0.97      0.93      0.95       102
           test_result       1.00      0.93      0.97        30
              violence       0.81      0.71      0.76       542
             micro-avg       0.92      0.89      0.90     21303
             macro-avg       0.91      0.87      0.89     21303
          weighted-avg       0.91      0.89      0.90     21303
```
