---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_jsl_medium)
author: John Snow Labs
name: zeroshot_ner_jsl_medium
date: 2025-01-01
tags: [licensed, en, ner, jsl, zeroshot, clinical]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PretrainedZeroShotNER
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages. While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels.

**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_medium_en_5.5.1_3.0_1735738633274.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_medium_en_5.5.1_3.0_1735738633274.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = [ 'Admission_Discharge', 'Age', 'Alcohol', 'Body_Part', 'Clinical_Dept', 'Direction', 'Disease_Syndrome_Disorder', 'Dosage_Strength',
 'Drug', 'Duration', 'Employment', 'Form', 'Frequency', 'Gender', 'Injury_or_Poisoning', 'Medical_Device', 'Modifier', 'Oncological', 'Procedure',
 'Race_Ethnicity', 'Relationship_Status', 'Route', 'Section_Header', 'Smoking', 'Symptom', 'Test', 'Test_Result', 'Treatment', 'Vaccine']

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

labels = [ 'Admission_Discharge', 'Age', 'Alcohol', 'Body_Part', 'Clinical_Dept', 'Direction', 'Disease_Syndrome_Disorder', 'Dosage_Strength',
 'Drug', 'Duration', 'Employment', 'Form', 'Frequency', 'Gender', 'Injury_or_Poisoning', 'Medical_Device', 'Modifier', 'Oncological', 'Procedure',
 'Race_Ethnicity', 'Relationship_Status', 'Route', 'Section_Header', 'Smoking', 'Symptom', 'Test', 'Test_Result', 'Treatment', 'Vaccine']

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_medium", "en", "clinical/models")\
    .setInputCols("sentence", "token")\
    .setOutputCol("ner")\
    .setPredictionThreshold(0.5)\
    .setLabels(labels)

ner_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "ner")\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
])

data = spark.createDataFrame([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

labels = Array("Admission_Discharge", "Age", "Alcohol", "Body_Part", "Clinical_Dept", "Direction", "Disease_Syndrome_Disorder", "Dosage_Strength",
 "Drug", "Duration", "Employment", "Form", "Frequency", "Gender", "Injury_or_Poisoning", "Medical_Device", "Modifier", "Oncological", "Procedure",
 "Race_Ethnicity", "Relationship_Status", "Route", "Section_Header", "Smoking", "Symptom", "Test", "Test_Result", "Treatment", "Vaccine")

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_medium", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("ner")
    .setPredictionThreshold(0.5)
    .setLabels(labels)

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    sentence_detector,
    tokenizer,
    pretrained_zero_shot_ner,
    ner_converter
))

val data = Seq([["""The patient is a 21-day-old Caucasian male here for 2 days of congestion - mom has been suctioning yellow discharge from the patient's nares, plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions). Additionally, there is no side effect observed after Influenza vaccine. One day ago, mom also noticed a tactile temperature and gave the patient Tylenol. Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion. He sleeps well, but has been more tired and has been fussy over the past 2 days. The parents noticed no improvement with albuterol treatments given in the ER. His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours. Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature."""]]).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------------------+-----+---+--------------+----------+
|chunk                 |begin|end|ner_label     |confidence|
+----------------------+-----+---+--------------+----------+
|21-day-old            |18   |27 |Age           |0.99517584|
|Caucasian             |29   |37 |Race_Ethnicity|0.9966413 |
|male                  |39   |42 |Gender        |0.9939465 |
|for 2 days            |49   |58 |Duration      |0.97774404|
|congestion            |63   |72 |Symptom       |0.881555  |
|mom                   |76   |78 |Gender        |0.99762625|
|yellow discharge      |100  |115|Symptom       |0.76778966|
|nares                 |136  |140|Body_Part     |0.6822294 |
|she                   |148  |150|Gender        |0.990868  |
|mild                  |169  |172|Modifier      |0.95501876|
|his                   |188  |190|Gender        |0.8426027 |
|retractions           |259  |269|Symptom       |0.8958332 |
|Influenza vaccine     |326  |342|Vaccine       |0.95380205|
|mom                   |358  |360|Gender        |0.9972128 |
|Tylenol               |418  |424|Drug          |0.6613898 |
|Baby                  |427  |430|Age           |0.9905624 |
|decreased p.o. intake |450  |470|Symptom       |0.7145019 |
|His                   |473  |475|Gender        |0.9991347 |
|his                   |561  |563|Gender        |0.99727863|
|respiratory congestion|565  |586|Symptom       |0.6558582 |
|He                    |589  |590|Gender        |0.9948435 |
|tired                 |623  |627|Symptom       |0.8143402 |
|fussy                 |642  |646|Symptom       |0.9036174 |
|treatments            |720  |729|Treatment     |0.5731197 |
|ER                    |744  |745|Clinical_Dept |0.97431695|
|His                   |748  |750|Gender        |0.9941076 |
|urine output          |752  |763|Symptom       |0.670487  |
|he                    |794  |795|Gender        |0.99911016|
|dirty diapers         |819  |831|Symptom       |0.52134395|
|per 24 hours          |833  |844|Duration      |0.6613321 |
|he                    |851  |852|Gender        |0.998706  |
|per 24 hours          |880  |891|Duration      |0.6907453 |
|Mom                   |894  |896|Gender        |0.9977082 |
|diarrhea              |909  |916|Symptom       |0.8736686 |
|His                   |919  |921|Gender        |0.9904789 |
+----------------------+-----+---+--------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_jsl_medium|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|711.8 MB|

## Benchmarking

```bash
                    label  precision    recall  f1-score   support
      Admission_Discharge     0.7925    0.9845    0.8781       322
                      Age     0.7951    0.9273    0.8562       812
                  Alcohol     0.8058    0.8737    0.8384        95
                Body_Part     0.8432    0.6978    0.7636     10493
            Clinical_Dept     0.7952    0.9431    0.8628      1704
                Direction     0.7929    0.9279    0.8551      4316
Disease_Syndrome_Disorder     0.8196    0.5202    0.6365      5267
          Dosage_Strength     0.5673    0.8025    0.6647      1266
                     Drug     0.7994    0.7653    0.7820      2723
                 Duration     0.4339    0.9325    0.5922       918
               Employment     0.7213    0.8213    0.7681       375
                     Form     0.3865    0.8610    0.5335       259
                Frequency     0.6404    0.6712    0.6555      1019
                   Gender     0.9768    0.9891    0.9829      5612
      Injury_or_Poisoning     0.5355    0.7298    0.6177       992
           Medical_Device     0.8728    0.8439    0.8581      5610
                 Modifier     0.5662    0.8365    0.6753      2929
                        O     0.9364    0.9250    0.9307    159014
              Oncological     0.7531    0.8243    0.7871       740
                Procedure     0.7582    0.7840    0.7709      6509
           Race_Ethnicity     0.9752    1.0000    0.9874       118
      Relationship_Status     0.5625    0.8824    0.6870        51
                    Route     0.7211    0.7218    0.7214       967
           Section_Header     0.8873    0.9750    0.9291     10262
                  Smoking     0.9537    0.9537    0.9537       108
                  Symptom     0.7911    0.7154    0.7513     11590
                     Test     0.7530    0.6348    0.6888      6117
              Test_Result     0.3906    0.7561    0.5151      1398
                Treatment     0.3524    0.5811    0.4387       456
                  Vaccine     0.8182    0.4286    0.5625        21
                 accuracy          -         -    0.8788    242063
                macro avg     0.7266    0.8103    0.7515    242063
             weighted avg     0.8871    0.8788    0.8801    242063
```
