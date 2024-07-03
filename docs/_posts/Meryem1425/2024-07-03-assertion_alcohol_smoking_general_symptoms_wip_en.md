---
layout: model
title: Detect Assertion Status from General Symptoms Entities
author: John Snow Labs
name: assertion_alcohol_smoking_general_symptoms_wip
date: 2024-07-03
tags: [licensed, en, clinical, assertion, alcohol, smoking, alcohol_smoking, withdrawal_symptom, overdose_symptom]
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

This model detects the assertion status of general symptoms entity related to alcohol-smoking.

## Predicted Entities

`Overdose_Symptom`, `Withdrawal_Symptom`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_alcohol_smoking_general_symptoms_wip_en_5.3.3_3.0_1720021258349.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_alcohol_smoking_general_symptoms_wip_en_5.3.3_3.0_1720021258349.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Drinking_Status", "Cardiovascular_Issues", "Respiratory_Issues", "GUT_Issues", "Neurologic_Issues", "Psychiatric_Issues", "Other_Health_Issues"])

assertion = AssertionDLModel.pretrained("assertion_alcohol_smoking_general_symptoms_wip", "en", "clinical/models")\
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

sample_texts = ["""The initial technician's record indicated decreased oxygen saturation (55%) by pulse oximetry, tachycardia (heart rate 110 bpm), and hypotension (blood pressure 90/72 mmHg).He was admitted to the intensive care unit with a preliminary diagnosis of acute respiratory failure due to acute alcohol intoxication."""]

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
    .setWhiteList(Array("Drinking_Status", "Cardiovascular_Issues", "Respiratory_Issues", "GUT_Issues", "Neurologic_Issues", "Psychiatric_Issues", "Other_Health_Issues"))
    
val assertion = AssertionDLModel.pretrained("assertion_alcohol_smoking_general_symptoms_wip", "en", "clinical/models")
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

val sample_texts = Seq("""The initial technician's record indicated decreased oxygen saturation (55%) by pulse oximetry, tachycardia (heart rate 110 bpm), and hypotension (blood pressure 90/72 mmHg).He was admitted to the intensive care unit with a preliminary diagnosis of acute respiratory failure due to acute alcohol intoxication.""").toDF("text")


val result = pipeline.fit(sample_texts).transform(sample_texts)
```
</div>

## Results

```bash
+---------------------------+-----+---+---------------------+----------------+----------+
|chunk                      |begin|end|ner_label            |assertion       |confidence|
+---------------------------+-----+---+---------------------+----------------+----------+
|decreased oxygen saturation|42   |68 |Respiratory_Issues   |Overdose_Symptom|0.9947    |
|tachycardia                |95   |105|Cardiovascular_Issues|Overdose_Symptom|0.9941    |
|hypotension                |133  |143|Cardiovascular_Issues|Overdose_Symptom|0.9956    |
|respiratory failure        |254  |272|Respiratory_Issues   |Overdose_Symptom|0.9999    |
+---------------------------+-----+---+---------------------+----------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_alcohol_smoking_general_symptoms_wip|
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
  Overdose_Symptom       0.80      0.71      0.75        17
Withdrawal_Symptom       0.75      0.83      0.79        18
          accuracy        -          -       0.77        35
         macro-avg       0.78      0.77      0.77        35
      weighted-avg       0.77      0.77      0.77        35
```
