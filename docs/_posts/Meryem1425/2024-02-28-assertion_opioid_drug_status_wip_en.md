---
layout: model
title: Detect Assertion Status from Drug Entities
author: John Snow Labs
name: assertion_opioid_drug_status_wip
date: 2024-02-28
tags: [en, licensed, clinical, assertion, opioid]
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

This model detects the assertion status of  drug entities related to opioid (including opioid_drug and other_drug).

## Predicted Entities

`opioid_medical_use`, `opioid_abuse`, `opioid_overdose`, `drug_medical_use`, `drug_abuse`, `drug_overdose`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_drug_status_wip_en_5.2.1_3.0_1709113624863.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_drug_status_wip_en_5.2.1_3.0_1709113624863.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["opioid_drug", "other_drug"])

assertion = AssertionDLModel.pretrained("assertion_opioid_drug_status_wip", "en", "clinical/models") \
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

sample_texts = ["""The patient presented to the hospital for a neurological evaluation, with a documented prescription for Percocet to manage chronic back pain. Assessment revealed ongoing discomfort localized to the lumbar region, with associated numbness and tingling in the lower extremities.""",
               """The patient, with a known history of hypertension managed with atenolol 50mg and verapamil 40mg, presented after a fall resulting in an ankle injury. Examination revealed swelling and tenderness, indicative of a twisted ankle. Considering the patient's medical history and pain management needs, a prescription for tramadol was provided to alleviate discomfort while ensuring minimal impact on blood pressure control.""",
               """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency, including agitation, diaphoresis, and myalgias.""",
               """The patient presented to the emergency department following an overdose on cocaine. On examination, the patient displayed signs of sympathetic nervous system stimulation, including tachycardia, hypertension, dilated pupils, and agitation.""",
               """The patient, with a documented history of chronic pain syndrome, was admitted following an accidental overdose of prescribed OxyContin. Upon assessment, the patient displayed symptoms indicative of opioid toxicity, including respiratory depression, altered mental status, and pinpoint pupils. Immediate resuscitative measures were undertaken, including airway management, administration of naloxone, and close monitoring of vital signs."""]

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
    .setWhiteList(Array("opioid_drug", "other_drug"))


val assertion = AssertionDLModel.pretrained("assertion_opioid_drug_status_wip", "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")
    
val pipeline = new Pipeline().setStages(Array(document_assembler,
                                              sentence_detector,
                                              tokenizer,
                                              word_embeddings,
                                              ner_model,
                                              ner_converter,
                                              assertion))

val data = Seq("""The patient presented to the hospital for a neurological evaluation, with a documented prescription for Percocet to manage chronic back pain. Assessment revealed ongoing discomfort localized to the lumbar region, with associated numbness and tingling in the lower extremities.""",
               """The patient, with a known history of hypertension managed with atenolol 50mg and verapamil 40mg, presented after a fall resulting in an ankle injury. Examination revealed swelling and tenderness, indicative of a twisted ankle. Considering the patient's medical history and pain management needs, a prescription for tramadol was provided to alleviate discomfort while ensuring minimal impact on blood pressure control.""",
               """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency, including agitation, diaphoresis, and myalgias.""",
               """The patient presented to the emergency department following an overdose on cocaine. On examination, the patient displayed signs of sympathetic nervous system stimulation, including tachycardia, hypertension, dilated pupils, and agitation.""",
               """The patient, with a documented history of chronic pain syndrome, was admitted following an accidental overdose of prescribed OxyContin. Upon assessment, the patient displayed symptoms indicative of opioid toxicity, including respiratory depression, altered mental status, and pinpoint pupils. Immediate resuscitative measures were undertaken, including airway management, administration of naloxone, and close monitoring of vital signs.""").toDF("text")


val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------+-----+---+-----------+------------------+----------+
|chunk    |begin|end|ner_label  |assertion         |confidence|
+---------+-----+---+-----------+------------------+----------+
|Percocet |104  |111|opioid_drug|opioid_medical_use|0.9976    |
|atenolol |63   |70 |other_drug |drug_medical_use  |1.0       |
|verapamil|81   |89 |other_drug |drug_medical_use  |1.0       |
|tramadol |315  |322|opioid_drug|opioid_medical_use|0.9986    |
|opioid   |82   |87 |opioid_drug|opioid_abuse      |0.6656    |
|percocet |143  |150|opioid_drug|opioid_abuse      |0.828     |
|opioid   |256  |261|opioid_drug|opioid_abuse      |0.9498    |
|cocaine  |75   |81 |other_drug |drug_overdose     |0.9093    |
|OxyContin|125  |133|opioid_drug|opioid_overdose   |0.9986    |
|opioid   |198  |203|opioid_drug|opioid_overdose   |0.9995    |
+---------+-----+---+-----------+------------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_opioid_drug_status_wip|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|942.3 KB|

## Benchmarking

```bash
             label  precision    recall  f1-score   support
        drug_abuse       0.91      0.74      0.82        39
  drug_medical_use       0.97      0.99      0.98      1181
     drug_overdose       0.85      0.57      0.68        30
      opioid_abuse       0.75      0.86      0.80        59
opioid_medical_use       0.91      0.91      0.91       284
   opioid_overdose       0.77      0.64      0.70        42
          accuracy        -         -        0.95      1635
         macro avg       0.86      0.79      0.82      1635
      weighted avg       0.95      0.95      0.94      1635
```
