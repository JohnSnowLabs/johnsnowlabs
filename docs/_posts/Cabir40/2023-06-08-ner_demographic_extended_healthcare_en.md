---
layout: model
title: NER for Demographic Extended (healthcare)
author: John Snow Labs
name: ner_demographic_extended_healthcare
date: 2023-06-08
tags: [demographic, licensed, clinical, en, ner, extended]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 4.4.3
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model identifies healthcare mentions that refers to a situation where a patient's demographic characteristics, such as `race`, `ethnicity`, `gender`, `age`, `socioeconomic` `status`, or `geographic location`.

## Predicted Entities

`Gender`, `Age`, `Race_ethnicity`, `Employment_status`, `Job_title`, `Marital_status`, `Political_afiliation`, `Union_membership`, `Sexual_orientation`, `Religion`, `Height`, `Weight`, `Obesity`, `Unhealthy_habits`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_demographic_extended_healthcare_en_4.4.3_3.0_1686217338322.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_demographic_extended_healthcare_en_4.4.3_3.0_1686217338322.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models") \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") 

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_healthcare_100d", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_demographic_extended_healthcare","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner")\
    .setLabelCasing("upper")
    
ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

ner_pipeline = Pipeline(stages=[
    documentAssembler, 
    sentenceDetector,
    tokenizer,
    word_embeddings,
    ner,
    ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

ner_model = ner_pipeline.fit(empty_data)

data = spark.createDataFrame([["""Patient Information:
Gender: Non-binary
Age: 68 years old
Race: Black
Employment status: Retired
Marital Status: Divorced
Sexual Orientation: Asexual
Religion: Judaism
Body Mass Index: 29.1
Unhealthy Habits: Substance use
Socioeconomic Status: Low Income
Area of Residence: Rural setting
Disability Status: Blindness
Chief Complaint:
The patient presented to the emergency department with complaint of severe chest pain that started suddenly while asleep.
"""]]).toDF("text")


result = ner_model.transform(data)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
  .setInputCols(Array("document"))
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentence"))
  .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_healthcare_100d", "en", "clinical/models")
  .setInputCols(Array("sentence", "token"))
  .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_demographic_extended_healthcare","en", "clinical/models")
  .setInputCols(Array("sentence", "token", "embeddings"))
  .setOutputCol("ner")
  .setLabelCasing("upper")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentence", "token", "ner"))
  .setOutputCol("ner_chunk")

val nerPipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  tokenizer,
  wordEmbeddings,
  ner,
  nerConverter
))
```
</div>

## Results

```bash
+-------------+------------------+----------+
|chunk        |ner_label         |confidence|
+-------------+------------------+----------+
|Non-binary   |GENDER            |0.9987    |
|68 years old |AGE               |0.6892667 |
|Black        |RACE_ETHNICITY    |0.9226    |
|Retired      |EMPLOYMENT_STATUS |0.9426    |
|Divorced     |MARITAL_STATUS    |0.9996    |
|Asexual      |SEXUAL_ORIENTATION|1.0       |
|Judaism      |RELIGION          |0.986     |
|Substance use|UNHEALTHY_HABITS  |0.48755002|
+-------------+------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_demographic_extended_healthcare|
|Compatibility:|Healthcare NLP 4.4.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|3.1 MB|

## References

trained by in-house dataset

## Benchmarking

```bash
label                     TP      FP      FN    Total  Precision  Recall     F1      
B-Age                     115     2.0     6     121    0.982906   0.950413   0.966387
I-Age                     107     4.0     2     109    0.963964   0.981651   0.972727
B-Employment_status       82      3.0     5     87     0.964706   0.942529   0.953488
I-Employment_status       0       1.0     2     2      0.000000   0.000000   0.000000
B-Gender                  110     1.0     21    131    0.990991   0.839695   0.909091
I-Gender                  0       0.0     1     1      0.000000   0.000000   0.000000
B-Height                  22      1.0     2     24     0.956522   0.916667   0.936170
I-Height                  39      1.0     1     40     0.975000   0.975000   0.975000
B-Job_title               34      3.0     16    50     0.918919   0.680000   0.781609
I-Job_title               19      2.0     9     28     0.904762   0.678571   0.775510
B-Marital_Status          80      5.0     6     86     0.941176   0.930233   0.935673
I-Marital_Status          9       1.0     1     10     0.900000   0.900000   0.900000
B-Obesity                 56      2.0     2     58     0.965517   0.965517   0.965517
I-Obesity                 2       0.0     2     4      1.000000   0.500000   0.666667
B-Political_affiliation   19      0.0     0     19     1.000000   1.000000   1.000000
B-Race_ethnicity          89      5.0     4     93     0.946809   0.956989   0.951872
I-Race_ethnicity          27      3.0     2     29     0.900000   0.931034   0.915254
B-Religion                70      3.0     4     74     0.958904   0.945946   0.952381
I-Religion                2       0.0     5     7      1.000000   0.285714   0.444444
B-Sexual_orientation      57      0.0     0     57     1.000000   1.000000   1.000000
B-Unhealthy_habits        254     27.0    82    336    0.903915   0.755952   0.823339
I-Unhealthy_habits        141     9.0     54    195    0.940000   0.723077   0.817391
B-Union_membership        9       1.0     4     13     0.900000   0.692308   0.782609
I-Union_membership        39      1.0     4     43     0.975000   0.906977   0.939759
B-Weight                  26      1.0     1     27     0.962963   0.962963   0.962963
I-Weight                  25      1.0     0     25     0.961538   1.000000   0.980392
Macro-average             1433    77.0    236  -       0.881291   0.785432   0.830605
Micro-average             1433    77.0    236   -      0.949006   0.858597   0.901541
```