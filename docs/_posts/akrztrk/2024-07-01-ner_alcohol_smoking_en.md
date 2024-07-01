---
layout: model
title: Detect Alcohol Smoking Specific Entities
author: John Snow Labs
name: ner_alcohol_smoking
date: 2024-07-01
tags: [licensed, en, clinical, ner, alcohol, smoking]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to detect and label alcohol and smoking-related entities within text data. Alcohol refers to beverages containing ethanol, a psychoactive substance that is widely consumed for its pleasurable effects. Smoking typically involves inhaling smoke from burning tobacco, a highly addictive substance. The model has been trained using advanced deep learning techniques on a diverse range of text sources and can accurately recognize and classify a wide range of entities related to alcohol and smoking. The model’s accuracy and precision have been carefully validated against expert-labeled data to ensure reliable and consistent results.

Here are the labels of the ALCOHOL_SMOKING model with their descriptions:

- `Alcohol_Type`:  Refers to the classification of alcoholic beverages based on their production process, ingredients, and alcohol content, commonly categorized into beer, wine, and spirits.

- `Cardiovascular_Issues`:  Encompass a range of conditions that impair the heart and vascular system's function, directly influenced by the consumption of alcohol and tobacco.

- `Cessation_Treatment`:  Encompasses the comprehensive strategies and interventions used to assist individuals in ending their use of alcohol.

- `Drinking_Status`:  Refers to the categorization of individuals based on their current and past alcohol consumption behavior.

- `GUT_Issues`:  Refers to digestive distress from smoking and drinking, including nausea, heartburn, ulcers, and liver diseases like cirrhosis and fatty liver.

- `Other_Health_Issues`:  All other signs or symptoms cannot be classified under specific categories. They may relate to skin, urinary system, reproductive system and any other system/organ of the body. 

- `Psychoneurologic_Issue`: Encompass a range of disorders affecting both the nervous and mental health systems, exacerbated or caused by alcohol or tobacco use, including conditions such as stroke, Alzheimer's disease, peripheral neuropathy, increased risk of dementia, alcohol use disorder, nicotine addiction, depression, and anxiety. Encompass a range of disorders affecting both the nervous and mental health systems, exacerbated or caused by alcohol or tobacco use, including conditions such as stroke, Alzheimer's disease, peripheral neuropathy, increased risk of dementia, alcohol use disorder, nicotine addiction, depression, and anxiety.  

- `Smoking_Status`:  Refers to the categorization of individuals based on their current and past smoking behavior.  

- `Smoking_Type`:  Refers to the classification of the substance’s individuals smoke and the methods they use, distinguishing among categories such as "Cigarettes," "Cigars," "Pipe," "Vaping/e-cigarettes," and "Other tobacco products.

- `Substance_Duration`:  The length of time a person has been engaged in these habits, namely smoking and alcohol, impacting their cumulative exposure to harmful substances and associated health risks.

- `Substance_Frequency`:  Refers to the rate or pattern at which these substances are consumed over a given period like every day, weekends, once in a month, weekly, monthly, daily etc.

- `Substance_Quantity`:  Measurable intake of tobacco or alcohol, respectively, often quantified as the number/pack or puffs of cigarettes or e-cigarettes smoked; or the volume, shot, glass, cup or similar measurements and concentration of alcohol consumed. 

- `Withdrawal_Treatment`:  Refers to pharmaceuticals prescribed to manage and alleviate the symptoms experienced during the cessation of alcohol use, specifically aimed at reducing the physical and psychological discomfort of withdrawal.

## Predicted Entities

`Drinking_Status`, `Alcohol_Type`, `Smoking_Status`, `Smoking_Type`, `Substance_Duration`, `Substance_Frequency`, `Substance_Quantity`, `Cardiovascular_Issues`, `Respiratory_Issues`, `GUT_Issues`, `Neurologic_Issues`, `Psychiatric_Issues`, `Other_Health_Issues`, `Drinking_Environment`, `Cessation_Treatment`, `Withdrawal_Treatment`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_alcohol_smoking_en_5.3.3_3.0_1719840489497.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_alcohol_smoking_en_5.3.3_3.0_1719840489497.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_alcohol_smoking", "en", "clinical/models")\
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

sample_texts = ["""The outpatient clinic addressed a complaint from the patient regarding severe anxiety and withdrawal symptoms. 
He disclosed a history of alcohol addiction, with weekly episodes of intense binge drinking over the past decade. 
However, due to recent challenges in his personal and professional life, he decided to quit drinking cold turkey a week ago. 
Since then, he has been experiencing escalating symptoms including tremors, sweating, nausea, and severe anxiety. 
The patient denies recent use drugs or smoking, focusing her struggles solely on alcohol.
He was placed on CIWA protocol w/ lorazepam for management. Scheduled for cognitive-behavioral therapy (CBT)."""]

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

val ner_model = MedicalNerModel.pretrained("ner_alcohol_smoking", "en", "clinical/models")
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

val sample_texts = Seq("""The outpatient clinic addressed a complaint from the patient regarding severe anxiety and withdrawal symptoms. 
He disclosed a history of alcohol addiction, with weekly episodes of intense binge drinking over the past decade. 
However, due to recent challenges in his personal and professional life, he decided to quit drinking cold turkey a week ago. 
Since then, he has been experiencing escalating symptoms including tremors, sweating, nausea, and severe anxiety. 
The patient denies recent use drugs or smoking, focusing her struggles solely on alcohol.
He was placed on CIWA protocol w/ lorazepam for management. Scheduled for cognitive-behavioral therapy (CBT).""").toDF("text")

val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+----------------------------+-----+---+----------------------+
|chunk                       |begin|end|ner_label             |
+----------------------------+-----+---+----------------------+
|anxiety                     |78   |84 |Psychoneurologic_Issue|
|alcohol addiction           |138  |154|Drinking_Status       |
|weekly                      |162  |167|Substance_Frequency   |
|binge                       |189  |193|Substance_Quantity    |
|drinking                    |195  |202|Drinking_Status       |
|over the past decade        |204  |223|Substance_Duration    |
|drinking                    |319  |326|Drinking_Status       |
|tremors                     |420  |426|Psychoneurologic_Issue|
|sweating                    |429  |436|Other_Health_Issues   |
|nausea                      |439  |444|GUT_Issues            |
|anxiety                     |458  |464|Psychoneurologic_Issue|
|smoking                     |507  |513|Smoking_Status        |
|alcohol                     |549  |555|Drinking_Status       |
|CIWA                        |575  |578|Withdrawal_Treatment  |
|lorazepam                   |592  |600|Withdrawal_Treatment  |
|cognitive-behavioral therapy|632  |659|Cessation_Treatment   |
|CBT                         |662  |664|Cessation_Treatment   |
+----------------------------+-----+---+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_alcohol_smoking|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|4.9 MB|

## Benchmarking

```bash
                        precision    recall  f1-score   support
          Alcohol_Type       1.00      1.00      1.00        16
 Cardiovascular_Issues       0.94      0.94      0.94        93
   Cessation_Treatment       0.91      0.93      0.92        57
       Drinking_Status       0.98      0.98      0.98       127
            GUT_Issues       0.90      0.91      0.91       258
   Other_Health_Issues       0.87      0.84      0.86       183
Psychoneurologic_Issue       0.94      0.85      0.89       189
    Respiratory_Issues       0.93      0.90      0.91        41
        Smoking_Status       0.96      1.00      0.98        22
          Smoking_Type       1.00      1.00      1.00         3
    Substance_Duration       0.94      0.93      0.93        54
   Substance_Frequency       0.92      0.96      0.94        25
    Substance_Quantity       0.96      1.00      0.98        45
  Withdrawal_Treatment       0.92      0.71      0.80        17
             micro-avg       0.92      0.91      0.91      1130
             macro-avg       0.94      0.92      0.93      1130
          weighted-avg       0.92      0.91      0.91      1130
```
