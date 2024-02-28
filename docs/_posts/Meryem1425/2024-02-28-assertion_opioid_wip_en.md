---
layout: model
title: Detect Assertion Status from Opioid Entities
author: John Snow Labs
name: assertion_opioid_wip
date: 2024-02-28
tags: [en, clinical, licensed, assertion, opioid]
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

This model detects the assertion status of entities related to opioid.

## Predicted Entities

`present`, `history`, `absent`, `hypothetical`, `past`, `family_or_someoneelse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_wip_en_5.2.1_3.0_1709111823206.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_opioid_wip_en_5.2.1_3.0_1709111823206.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

assertion = AssertionDLModel.pretrained("assertion_opioid_wip" "en", "clinical/models") \
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

sample_texts = [ """The patient with a history of substance abuse presented with clinical signs indicative of opioid overdose, including constricted pupils, cyanotic lips, drowsiness, and confusion. Immediate assessment and intervention were initiated to address the patient's symptoms and stabilize their condition. Close monitoring for potential complications, such as respiratory depression, was maintained throughout the course of treatment.""",
                """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency.""",
               """The patient was brought to the clinic exhibiting symptoms consistent with opioid withdrawal, despite denying any illicit drug use. Upon further questioning, the patient revealed using tramadol for chronic pain management."""]
               
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

val assertion = AssertionDLModel.pretrained("assertion_opioid_wip" "en", "clinical/models")
    .setInputCols(Array("sentence", "ner_chunk", "embeddings"))
    .setOutputCol("assertion")
        
val pipeline = new Pipeline().setStages(Array(document_assembler,
                                              sentence_detector,
                                              tokenizer,
                                              word_embeddings,
                                              ner_model,
                                              ner_converter,
                                              assertion))

val data = Seq("""The patient with a history of substance abuse presented with clinical signs indicative of opioid overdose, including constricted pupils, cyanotic lips, drowsiness, and confusion. Immediate assessment and intervention were initiated to address the patient's symptoms and stabilize their condition. Close monitoring for potential complications, such as respiratory depression, was maintained throughout the course of treatment.""",
                """The patient presented to the rehabilitation facility with a documented history of opioid abuse, primarily stemming from misuse of prescription percocet pills intended for their partner's use. Initial assessment revealed withdrawal symptoms consistent with opioid dependency.""",
               """The patient was brought to the clinic exhibiting symptoms consistent with opioid withdrawal, despite denying any illicit drug use. Upon further questioning, the patient revealed using tramadol for chronic pain management.""").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------+-----+---+----------------------+------------+----------+
|chunk                 |begin|end|ner_label             |assertion   |confidence|
+----------------------+-----+---+----------------------+------------+----------+
|substance abuse       |30   |44 |substance_use_disorder|history     |0.9644    |
|opioid                |90   |95 |opioid_drug           |hypothetical|0.7974    |
|overdose              |97   |104|other_disease         |hypothetical|0.9961    |
|constricted pupils    |117  |134|general_symptoms      |past        |0.732     |
|cyanotic lips         |137  |149|general_symptoms      |past        |0.8501    |
|drowsiness            |152  |161|general_symptoms      |past        |0.9469    |
|confusion             |168  |176|general_symptoms      |past        |0.9686    |
|respiratory depression|351  |372|other_disease         |hypothetical|0.5921    |
|opioid                |82   |87 |opioid_drug           |history     |0.735     |
|percocet              |143  |150|opioid_drug           |present     |0.905     |
|pills                 |152  |156|drug_form             |present     |0.9363    |
|withdrawal            |220  |229|general_symptoms      |present     |0.9929    |
|opioid                |256  |261|opioid_drug           |present     |0.9348    |
|opioid                |74   |79 |opioid_drug           |present     |0.8874    |
|withdrawal            |81   |90 |general_symptoms      |present     |0.8789    |
|illicit drug use      |113  |128|substance_use_disorder|absent      |0.9919    |
|tramadol              |184  |191|opioid_drug           |present     |0.9836    |
|chronic pain          |197  |208|general_symptoms      |present     |0.9993    |
+----------------------+-----+---+----------------------+------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_opioid_wip|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk, embeddings]|
|Output Labels:|[assertion_pred]|
|Language:|en|
|Size:|942.4 KB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
      absent       0.80      0.86      0.83       507
      family       0.73      0.71      0.72       136
     history       0.75      0.62      0.68       770
hypothetical       0.64      0.69      0.66       352
        past       0.59      0.32      0.42       214
     present       0.72      0.80      0.76      1571
 someoneelse       0.18      0.11      0.13        28
    accuracy         -        -        0.72      3578
   macro-avg       0.63      0.59      0.60      3578
weighted-avg       0.72      0.72      0.71      3578
```
