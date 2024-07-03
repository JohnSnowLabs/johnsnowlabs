---
layout: model
title: Detect Assertion Status from Alcohol-Smoking Entities
author: John Snow Labs
name: assertion_alcohol_smoking_wip
date: 2024-07-03
tags: [en, licensed, clinical, assertion, alcohol, smoking, alcohol_smoking]
task: Assertion Status
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects the assertion status of entities related to alcohol-smoking.

## Predicted Entities

`Absent`, `Hypothetical_Possible`, `Past_History`, `Present_Planned`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_alcohol_smoking_wip_en_5.3.3_3.0_1720018706157.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_alcohol_smoking_wip_en_5.3.3_3.0_1720018706157.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
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

assertion = AssertionDLModel.pretrained("assertion_alcohol_smoking_wip", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
    ])

sample_texts = ["""Per the patient, the last drink was on ___, prior to admission. The patient admits to having experienced tremors, palpitations, and diaphoresis during the past alcohol withdrawals, but he denies ever having experienced seizures. Mr. ___ did not report experiencing any symptoms of withdrawal throughout his hospital stay, and an examination revealed no evidence of withdrawal.""",
               """SUBSTANCE ABUSE: The patient admitted to occasional binge drinking, but admitted to normally consuming one pint of liquor a day in the week before her admission. Before she attempted suicide, she was heavily intoxicated and had a high blood alcohol level (BAL). Attending the AA meetings and expressing a desire to keep going to AA to support sobriety were two ways the patient showed motivation to stop drinking. The patient was put on the CIWA protocol upon admission, but no PRN Valium was needed for alcohol withdrawal."""]


data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
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

val assertion = AssertionDLModel.pretrained("assertion_alcohol_smoking_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    clinical_embeddings,
    ner_model,
    ner_converter,
    assertion
))

val sample_texts = Seq("""Per the patient, the last drink was on ___, prior to admission. The patient admits to having experienced tremors, palpitations, and diaphoresis during the past alcohol withdrawals, but he denies ever having experienced seizures. Mr. ___ did not report experiencing any symptoms of withdrawal throughout his hospital stay, and an examination revealed no evidence of withdrawal.""",
               """SUBSTANCE ABUSE: The patient admitted to occasional binge drinking, but admitted to normally consuming one pint of liquor a day in the week before her admission. Before she attempted suicide, she was heavily intoxicated and had a high blood alcohol level (BAL). Attending the AA meetings and expressing a desire to keep going to AA to support sobriety were two ways the patient showed motivation to stop drinking. The patient was put on the CIWA protocol upon admission, but no PRN Valium was needed for alcohol withdrawal.""").toDF("text")


val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+------------+-----+---+----------------------+---------------+----------+
|chunk       |begin|end|ner_label             |assertion      |confidence|
+------------+-----+---+----------------------+---------------+----------+
|drink       |26   |30 |Drinking_Status       |Past_History   |0.8507    |
|tremors     |105  |111|Psychoneurologic_Issue|Past_History   |0.9315    |
|palpitations|114  |125|Cardiovascular_Issues |Past_History   |0.9251    |
|diaphoresis |132  |142|Other_Health_Issues   |Past_History   |0.9181    |
|alcohol     |160  |166|Drinking_Status       |Past_History   |0.9109    |
|seizures    |219  |226|Psychoneurologic_Issue|Absent         |0.5359    |
|binge       |52   |56 |Substance_Quantity    |Present_Planned|0.5528    |
|drinking    |58   |65 |Drinking_Status       |Present_Planned|0.5704    |
|one pint    |103  |110|Substance_Quantity    |Present_Planned|0.6838    |
|liquor      |115  |120|Alcohol_Type          |Present_Planned|0.6879    |
|a day       |122  |126|Substance_Frequency   |Present_Planned|0.8029    |
|suicide     |183  |189|Psychoneurologic_Issue|Past_History   |0.731     |
|intoxicated |208  |218|Psychoneurologic_Issue|Past_History   |0.7832    |
|alcohol     |241  |247|Drinking_Status       |Past_History   |0.507     |
|AA          |276  |277|Cessation_Treatment   |Present_Planned|0.4559    |
|AA          |329  |330|Cessation_Treatment   |Present_Planned|0.5112    |
|drinking    |404  |411|Drinking_Status       |Present_Planned|0.5385    |
|CIWA        |441  |444|Withdrawal_Treatment  |Present_Planned|0.5693    |
|Valium      |482  |487|Withdrawal_Treatment  |Absent         |0.553     |
|alcohol     |504  |510|Drinking_Status       |Present_Planned|0.5135    |
+------------+-----+---+----------------------+---------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_alcohol_smoking_wip|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|2.5 MB|

## Benchmarking

```bash
                label  precision    recall  f1-score   support
               Absent       0.84      0.74      0.79       213
Hypothetical_Possible       0.67      0.81      0.74       115
         Past_History       0.77      0.72      0.75       221
      Present_Planned       0.74      0.78      0.76       327
             accuracy        -         -        0.76       876
            macro-avg       0.76      0.76      0.76       876
         weighted-avg       0.76      0.76      0.76       876
```
