---
layout: model
title: Detect Assertion Status from General Symptoms Entities
author: John Snow Labs
name: assertion_opioid_general_symptoms_status_wip
date: 2024-02-28
tags: [licensed, en, clinical, assertion, opioid]
task: Assertion Status
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model detects the assertion status of  general symptoms entity related to opioid.

## Predicted Entities

`underlying_pain`, `withdrawal_symptom`, `overdose_symptom`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_general_symptoms_status_wip_en_5.2.1_3.0_1709119096996.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_general_symptoms_status_wip_en_5.2.1_3.0_1709119096996.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("ner_chunk")\
    .setWhiteList(["general_symptoms"])

assertion = AssertionDLModel.pretrained("assertion_opioid_general_symptoms_status_wip", "en", "clinical/models") \
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

sample_texts = ["""The patient presented with symptoms consistent with opioid withdrawal, including feelings of anxiety, tremors, and diarrhea. Vital signs were within normal limits, and supportive measures were initiated. The patient was closely monitored for potential complications and provided with appropriate pharmacological interventions to manage their symptoms.""",
               """The patient presented to the hospital for a neurological evaluation, with a documented prescription for Percocet to manage chronic back pain.""",
               """The patient presented to the clinic following a suicide attempt by heroin overdose. Upon assessment, the patient exhibited altered mental status, shallow breathing, and pinpoint pupils, indicative of opioid toxicity. Immediate resuscitative measures were initiated, including airway management, administration of naloxone, and close monitoring of vital signs. The patient was stabilized and admitted for further psychiatric evaluation and management.""",
               """The patient with a history of substance abuse presented with clinical signs indicative of opioid overdose, including constricted pupils, cyanotic lips, drowsiness, and confusion. Immediate assessment and intervention were initiated to address the patient's symptoms and stabilize their condition. Close monitoring for potential complications, such as respiratory depression, was maintained throughout the course of treatment.""",
               """The patient, known for a history of substance abuse, was brought to the hospital in a highly agitated and aggressive state, consistent with potential cocaine use. Initial assessment revealed signs of sympathetic overstimulation, including tachycardia, hypertension, and profuse sweating."""]

data = spark.createDataFrame(sample_texts, StringType()).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")                

val ner_model = MedicalNerModel.pretrained("ner_opioid", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("general_symptoms")

val assertion = AssertionDLModel.pretrained("assertion_opioid_general_symptoms_status_wip" "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")
    
val pipeline = new Pipeline().setStages(Array(document_assembler,
                                              sentence_detector,
                                              tokenizer,
                                              word_embeddings,
                                              ner_model,
                                              ner_converter,
                                              assertion))

val data = Seq("""The patient presented with symptoms consistent with opioid withdrawal, including feelings of anxiety, tremors, and diarrhea. Vital signs were within normal limits, and supportive measures were initiated. The patient was closely monitored for potential complications and provided with appropriate pharmacological interventions to manage their symptoms.""",
               """The patient presented to the hospital for a neurological evaluation, with a documented prescription for Percocet to manage chronic back pain.""",
               """The patient presented to the clinic following a suicide attempt by heroin overdose. Upon assessment, the patient exhibited altered mental status, shallow breathing, and pinpoint pupils, indicative of opioid toxicity. Immediate resuscitative measures were initiated, including airway management, administration of naloxone, and close monitoring of vital signs. The patient was stabilized and admitted for further psychiatric evaluation and management.""",
               """The patient with a history of substance abuse presented with clinical signs indicative of opioid overdose, including constricted pupils, cyanotic lips, drowsiness, and confusion. Immediate assessment and intervention were initiated to address the patient's symptoms and stabilize their condition. Close monitoring for potential complications, such as respiratory depression, was maintained throughout the course of treatment.""",
               """The patient, known for a history of substance abuse, was brought to the hospital in a highly agitated and aggressive state, consistent with potential cocaine use. Initial assessment revealed signs of sympathetic overstimulation, including tachycardia, hypertension, and profuse sweating.""").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------+-----+---+----------------+------------------+----------+
|chunk                      |begin|end|ner_label       |assertion         |confidence|
+---------------------------+-----+---+----------------+------------------+----------+
|withdrawal                 |59   |68 |general_symptoms|withdrawal_symptom|1.0       |
|tremors                    |102  |108|general_symptoms|withdrawal_symptom|1.0       |
|diarrhea                   |115  |122|general_symptoms|withdrawal_symptom|1.0       |
|chronic back pain          |123  |139|general_symptoms|underlying_pain   |1.0       |
|altered mental status      |123  |143|general_symptoms|overdose_symptom  |1.0       |
|shallow breathing          |146  |162|general_symptoms|overdose_symptom  |1.0       |
|pinpoint pupils            |169  |183|general_symptoms|overdose_symptom  |1.0       |
|constricted pupils         |117  |134|general_symptoms|overdose_symptom  |1.0       |
|cyanotic lips              |137  |149|general_symptoms|overdose_symptom  |1.0       |
|drowsiness                 |152  |161|general_symptoms|overdose_symptom  |1.0       |
|confusion                  |168  |176|general_symptoms|overdose_symptom  |1.0       |
|agitated                   |93   |100|general_symptoms|withdrawal_symptom|0.9999    |
|aggressive state           |106  |121|general_symptoms|withdrawal_symptom|0.9996    |
|sympathetic overstimulation|200  |226|general_symptoms|withdrawal_symptom|1.0       |
|tachycardia                |239  |249|general_symptoms|withdrawal_symptom|1.0       |
|profuse sweating           |270  |285|general_symptoms|withdrawal_symptom|0.9999    |
+---------------------------+-----+---+----------------+------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_opioid_general_symptoms_status_wip|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|952.9 KB|

## Benchmarking

```bash
             label  precision    recall  f1-score   support
  overdose_symptom       0.86      0.73      0.79        33
   underlying_pain       0.94      0.98      0.96       121
withdrawal_symptom       0.92      0.92      0.92        72
          accuracy         -         -       0.92       226
         macro avg       0.91      0.88      0.89       226
      weighted avg       0.92      0.92      0.92       226
```