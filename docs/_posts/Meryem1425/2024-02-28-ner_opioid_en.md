---
layout: model
title: Detect Opioid Specific Entities
author: John Snow Labs
name: ner_opioid
date: 2024-02-28
tags: [licensed, en, ner, opioid, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.2.1
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
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_OPIOID/){:.button.button-orange}
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_opioid_en_5.2.1_3.0_1709109768256.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_opioid_en_5.2.1_3.0_1709109768256.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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


sample_texts = ["""The patient, unmarried and with a significant history of substance abuse involving the illicit consumption of various opioids such as heroin, fentanyl, and oxycodone, presented with a headache and was diagnosed PTSD. Despite denying the use of alcohol, smoking, or marijuana, the patient, who has been unemployed for several months, required administration of Narcan for suspected opioid overdose. A recent toxicology screen confirmed the presence of opioids, and showed negative results for benzodiazepines, cocaine, amphetamines, barbiturates, and tricyclic substances."""]


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

val sample_texts = Seq("""The patient presented with symptoms consistent with opioid withdrawal, including feelings of anxiety, tremors, and diarrhea. Vital signs were within normal limits, and supportive measures were initiated. The patient was closely monitored for potential complications and provided with appropriate pharmacological interventions to manage their symptoms.""",
               """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency, including agitation, diaphoresis, and myalgias.""",
               """The patient presented to the emergency department following an overdose on cocaine. On examination, the patient displayed signs of sympathetic nervous system stimulation, including tachycardia, hypertension, dilated pupils, and agitation.""",
               """The patient, known for a history of substance abuse, was brought to the hospital in a highly agitated and aggressive state, consistent with potential cocaine use. Initial assessment revealed signs of sympathetic overstimulation, including tachycardia, hypertension, and profuse sweating.""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+--------------------+-----+---+----------------------+
|chunk               |begin|end|ner_label             |
+--------------------+-----+---+----------------------+
|unmarried           |13   |21 |marital_status        |
|substance abuse     |57   |71 |substance_use_disorder|
|opioids             |118  |124|opioid_drug           |
|heroin              |134  |139|opioid_drug           |
|fentanyl            |142  |149|opioid_drug           |
|oxycodone           |156  |164|opioid_drug           |
|headache            |184  |191|general_symptoms      |
|PTSD                |211  |214|psychiatric_issue     |
|alcohol             |244  |250|alcohol_use           |
|marijuana           |265  |273|other_drug            |
|unemployed          |302  |311|employment            |
|Narcan              |360  |365|antidote              |
|opioid              |381  |386|opioid_drug           |
|overdose            |388  |395|other_disease         |
|toxicology screen   |407  |423|test                  |
|opioids             |451  |457|test                  |
|negative            |471  |478|test_result           |
|benzodiazepines     |492  |506|test                  |
|cocaine             |509  |515|test                  |
|amphetamines        |518  |529|test                  |
|barbiturates        |532  |543|test                  |
|tricyclic substances|550  |569|test                  |
+--------------------+-----+---+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_opioid|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
           alcohol_use       0.94      0.91      0.92       248
              antidote       1.00      0.97      0.98        88
  communicable_disease       0.91      0.93      0.92       153
         drug_duration       0.87      0.88      0.87        91
             drug_form       0.98      0.98      0.98       695
        drug_frequency       0.99      0.97      0.98      1560
         drug_quantity       0.97      0.96      0.96      1757
            drug_route       0.98      0.99      0.99       774
         drug_strength       0.92      0.95      0.93       571
            employment       0.86      0.64      0.74       182
      general_symptoms       0.90      0.77      0.83      1428
           legal_issue       0.88      0.74      0.80        47
        marital_status       0.89      0.97      0.93        35
           opioid_drug       0.99      0.97      0.98       468
         other_disease       0.92      0.88      0.90      2030
            other_drug       0.92      0.95      0.94      1701
     psychiatric_issue       0.92      0.75      0.83       750
    sexual_orientation       1.00      1.00      1.00        10
substance_use_disorder       0.85      0.94      0.89       187
                  test       0.94      0.92      0.93        73
           test_result       1.00      0.95      0.98        21
              violence       0.85      0.66      0.74       251
             micro-avg       0.94      0.91      0.92     13120
             macro-avg       0.93      0.90      0.91     13120
          weighted-avg       0.94      0.91      0.92     13120
```
