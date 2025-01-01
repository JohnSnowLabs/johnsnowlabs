---
layout: model
title: Pretrained Zero-Shot Named Entity Recognition (zeroshot_ner_jsl_large)
author: John Snow Labs
name: zeroshot_ner_jsl_large
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

Zero-shot Named Entity Recognition (NER) enables the identification of entities in text with minimal effort. By leveraging pre-trained language models and contextual understanding, zero-shot NER extends entity recognition capabilities to new domains and languages.
While the model card includes default labels as examples, it is important to highlight that users are not limited to these labels.
**The model is designed to support any set of entity labels, allowing users to adapt it to their specific use cases. For best results, it is recommended to use labels that are conceptually similar to the provided defaults.**

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_large_en_5.5.1_3.0_1735751702763.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zeroshot_ner_jsl_large_en_5.5.1_3.0_1735751702763.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_large", "en", "clinical/models")\
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

pretrained_zero_shot_ner = medical.PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_large", "en", "clinical/models")\
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

val pretrained_zero_shot_ner = PretrainedZeroShotNER().pretrained("zeroshot_ner_jsl_large", "en", "clinical/models")
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
|21-day-old            |18   |27 |Age           |0.99855894|
|Caucasian             |29   |37 |Race_Ethnicity|0.9965018 |
|male                  |39   |42 |Gender        |0.9979837 |
|for 2 days            |49   |58 |Frequency     |0.9547805 |
|congestion            |63   |72 |Symptom       |0.9777157 |
|mom                   |76   |78 |Gender        |0.99721634|
|nares                 |136  |140|Body_Part     |0.8162966 |
|she                   |148  |150|Gender        |0.99808997|
|mild                  |169  |172|Modifier      |0.9933716 |
|his                   |188  |190|Gender        |0.9682989 |
|retractions           |259  |269|Symptom       |0.93004584|
|Influenza vaccine     |326  |342|Vaccine       |0.9917237 |
|mom                   |358  |360|Gender        |0.99286497|
|Tylenol               |418  |424|Drug          |0.7294259 |
|Baby                  |427  |430|Age           |0.95155627|
|His                   |473  |475|Gender        |0.99755836|
|5 to 10 minutes       |532  |546|Frequency     |0.5138932 |
|his                   |561  |563|Gender        |0.99703395|
|respiratory congestion|565  |586|Symptom       |0.78011936|
|He                    |589  |590|Gender        |0.997498  |
|tired                 |623  |627|Symptom       |0.8767565 |
|fussy                 |642  |646|Symptom       |0.95738137|
|albuterol treatments  |710  |729|Treatment     |0.53156906|
|ER                    |744  |745|Clinical_Dept |0.9652154 |
|His                   |748  |750|Gender        |0.9987986 |
|urine output          |752  |763|Symptom       |0.5371252 |
|he                    |794  |795|Gender        |0.99845266|
|per 24 hours          |833  |844|Frequency     |0.8483188 |
|he                    |851  |852|Gender        |0.99878913|
|per 24 hours          |880  |891|Frequency     |0.7822129 |
|Mom                   |894  |896|Gender        |0.98790914|
|diarrhea              |909  |916|Symptom       |0.96422964|
|His                   |919  |921|Gender        |0.9979843 |
+----------------------+-----+---+--------------+----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zeroshot_ner_jsl_large|
|Compatibility:|Healthcare NLP 5.5.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.6 GB|

## Benchmarking

```bash

                    label  precision    recall  f1-score   support
      Admission_Discharge     0.6976    0.9814    0.8155       322
                      Age     0.8040    0.9495    0.8707       812
                  Alcohol     0.7731    0.9684    0.8598        95
                Body_Part     0.7486    0.8022    0.7744     10493
            Clinical_Dept     0.7665    0.9536    0.8499      1704
                Direction     0.7585    0.9451    0.8416      4316
Disease_Syndrome_Disorder     0.8701    0.6791    0.7628      5267
          Dosage_Strength     0.7500    0.8009    0.7746      1266
                     Drug     0.8876    0.8645    0.8759      2723
                 Duration     0.4256    0.9129    0.5805       918
               Employment     0.6494    0.8693    0.7434       375
                     Form     0.4963    0.7683    0.6030       259
                Frequency     0.5561    0.7341    0.6328      1019
                   Gender     0.9779    0.9920    0.9849      5612
      Injury_or_Poisoning     0.5710    0.7056    0.6312       992
           Medical_Device     0.8075    0.9034    0.8528      5610
                 Modifier     0.4157    0.9181    0.5723      2929
              Oncological     0.7931    0.8135    0.8032       740
                Procedure     0.7274    0.7884    0.7567      6509
           Race_Ethnicity     0.9916    1.0000    0.9958       118
      Relationship_Status     0.4623    0.9608    0.6242        51
                    Route     0.7375    0.7963    0.7658       967
           Section_Header     0.9047    0.9774    0.9396     10262
                  Smoking     0.9720    0.9630    0.9674       108
                  Symptom     0.7663    0.7455    0.7557     11590
                     Test     0.7322    0.6542    0.6910      6117
              Test_Result     0.3766    0.7947    0.5110      1398
                Treatment     0.3548    0.6404    0.4566       456
                  Vaccine     0.6522    0.7143    0.6818        21
                 accuracy          -         -    0.8770    242063
                macro avg     0.7129    0.8499    0.7635    242063
             weighted avg     0.8955    0.8770    0.8826    242063                    

```