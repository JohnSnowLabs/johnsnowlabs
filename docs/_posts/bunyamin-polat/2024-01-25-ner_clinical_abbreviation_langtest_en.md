---
layout: model
title: Extraction of Clinical Abbreviations and Acronyms (LangTest)
author: John Snow Labs
name: ner_clinical_abbreviation_langtest
date: 2024-01-25
tags: [en, clinical, ner, licensed, abbreviation, langtest]
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

This model is trained to extract clinical acronyms and acronyms from text. It is the version of [ner_abbreviation_clinical](https://nlp.johnsnowlabs.com/2021/12/30/ner_abbreviation_clinical_en.html) model augmented with `langtest` library.

| **test_type**        | **before fail_count** | **after fail_count** | **before pass_count** | **after pass_count** | **minimum pass_rate** | **before pass_rate** | **after pass_rate** |
|----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|----------------------|---------------------|
| **lowercase**        | 351                   | 78                   | 223                   | 496                  | 90%                   | 39%                  | 86%                 |
| **titlecase**        | 325                   | 73                   | 248                   | 500                  | 85%                   | 43%                  | 87%                 |
| **uppercase**        | 117                   | 47                   | 382                   | 452                  | 90%                   | 77%                  | 91%                 |
| **weighted average** | **793**               | **198**              | **853**               | **1448**             | **88.33%**            | **51.82%**           | **87.97%**          |

## Predicted Entities

`ABBR`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_abbreviation_langtest_en_5.2.1_3.0_1706208855884.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_abbreviation_langtest_en_5.2.1_3.0_1706208855884.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")\

embeddings = WordEmbeddingsModel.pretrained('embeddings_clinical', 'en', 'clinical/models') \
    .setInputCols(['sentence', 'token']) \
    .setOutputCol('embeddings')

ner_model = MedicalNerModel.pretrained('ner_clinical_abbreviation_langtest', 'en', 'clinical/models') \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "abbr_ner"]) \
    .setOutputCol("ner_chunk")\


ner_pipeline = Pipeline(
        stages = [
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter
])

text = """Gravid with an Estimated Fetal Weight of 6-6/12 Pounds. Lower Extremities: There are no signs of edema in the lower extremities. Laboratory Data: Laboratory tests revealed a normal cbc. Blood Type: The patient's blood type has been identified as AB Positive. Rubella Status: The patient has confirmed immunity to rub. VDRL Test: The vdrl test for syphilis is nonreactive. Hepatitis C Screening (anti-hcv): The screening for Hepatitis C surface antigen returned a negative result. Testing for hiv showed a negative outcome."""

data = spark.createDataFrame([[text]]).toDF("text")

result = ner_pipeline.fit(data).transform(data)
```
```scala
val document_assembler = DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical_abbreviation_langtest", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = NerConverter() 
    .setInputCols(Array("sentence", "token", "ner")) 
    .setOutputCol("ner_chunk")


val ner_pipeline = new Pipeline().setStages(Array(document_assembler, sentence_aetector, tokenizer, embeddings, ner_model, ner_converter))

val data = Seq("Gravid with an Estimated Fetal Weight of 6-6/12 Pounds. Lower Extremities: There are no signs of edema in the lower extremities. Laboratory Data: Laboratory tests revealed a normal cbc. Blood Type: The patient's blood type has been identified as AB Positive. Rubella Status: The patient has confirmed immunity to rub. VDRL Test: The vdrl test for syphilis is nonreactive. Hepatitis C Screening (anti-hcv): The screening for Hepatitis C surface antigen returned a negative result. Testing for hiv showed a negative outcome.").toDF("text")

val result = ner_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------+---------+
|chunk   |ner_label|
+--------+---------+
|cbc     |ABBR     |
|VDRL    |ABBR     |
|vdrl    |ABBR     |
|anti-hcv|ABBR     |
|hiv     |ABBR     |
+--------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical_abbreviation_langtest|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.7 MB|

## Sample text from the training dataset

Trained on the in-house dataset.

## Benchmarking

```bash
label         precision  recall  f1-score  support 
ABBR          0.90       0.94    0.92      683     
micro-avg     0.90       0.94    0.92      683     
macro-avg     0.90       0.94    0.92      683     
weighted-avg  0.90       0.94    0.92      683     
```
