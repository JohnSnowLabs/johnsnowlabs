---
layout: model
title: Detect Assertion Status (assertion_bert_classification_jsl_onnx)
author: John Snow Labs
name: assertion_bert_classification_jsl_onnx
date: 2025-07-15
tags: [licensed, clinical, en, assertion, classification, jsl, onnx]
task: Assertion Status
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
engine: onnx
annotator: BertForAssertionClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities.

## Predicted Entities

`Present`, `Planned`, `SomeoneElse`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_jsl_onnx_en_6.0.2_3.0_1752596719405.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_jsl_onnx_en_6.0.2_3.0_1752596719405.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")
    
embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_jsl_onnx", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")\
    .setCaseSensitive(False)
    
pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])


text = """
The patient is a 21-day-old Caucasian male here for 2 days of congestion -
mom has been suctioning yellow discharge from the patient's nares,
plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions).
One day ago, mom also noticed a tactile temperature and gave the patient Tylenol.
Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion.
He sleeps well, but has been more tired and has been fussy over the past 2 days.
The parents noticed no improvement with albuterol treatments given in the ER.
His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours.
Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.

Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""
data = spark.createDataFrame([[text]]).toDF("text")
                              
result = pipeline.fit(data).transform(data)

# Checking results
result.select("text", "assertion_class.result").show(truncate=False)

```

{:.jsl-block}
```python
# Test classifier in Spark NLP pipeline
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")
    
tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_jsl_onnx", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")\
    .setCaseSensitive(False)
    
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])

text = """
The patient is a 21-day-old Caucasian male here for 2 days of congestion -
mom has been suctioning yellow discharge from the patient's nares,
plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions).
One day ago, mom also noticed a tactile temperature and gave the patient Tylenol.
Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion.
He sleeps well, but has been more tired and has been fussy over the past 2 days.
The parents noticed no improvement with albuterol treatments given in the ER.
His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours.
Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.

Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""
data = spark.createDataFrame([[text]]).toDF("text")
                              
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
    .setInputCols("sentences")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_jsl_onnx", "en", "clinical/models")
    .setInputCols(Array("document", "ner_chunk"))
    .setOutputCol("assertion_class")
    .setCaseSensitive(false)

val pipeline = new Pipeline().setStages(
    Array(
        document_assembler, 
        sentence_detector,
        tokenizer, 
        embeddings,
        ner,
        ner_converter,
        assertion_classifier
))

val text = """
The patient is a 21-day-old Caucasian male here for 2 days of congestion -
mom has been suctioning yellow discharge from the patient's nares,
plus she has noticed some mild problems with his breathing while feeding (but negative for any perioral cyanosis or retractions).
One day ago, mom also noticed a tactile temperature and gave the patient Tylenol.
Baby also has had some decreased p.o. intake. His normal breast-feeding is down from 20 minutes q.2h. to 5 to 10 minutes secondary to his respiratory congestion.
He sleeps well, but has been more tired and has been fussy over the past 2 days.
The parents noticed no improvement with albuterol treatments given in the ER.
His urine output has also decreased; normally he has 8 to 10 wet and 5 dirty diapers per 24 hours, now he has down to 4 wet diapers per 24 hours.
Mom denies any diarrhea. His bowel movements are yellow colored and soft in nature.

Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""


val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|    | chunks                                |   begin |   end | entities   | assertion    |   confidence |
|---:|:--------------------------------------|--------:|------:|:-----------|:-------------|-------------:|
|  0 | congestion                            |      63 |    72 | PROBLEM    | Present      |     0.981844 |
|  1 | some mild problems with his breathing |     164 |   200 | PROBLEM    | Present      |     0.996332 |
|  2 | any perioral cyanosis                 |     234 |   254 | PROBLEM    | Absent       |     0.998711 |
|  3 | retractions                           |     259 |   269 | PROBLEM    | Absent       |     0.998287 |
|  4 | a tactile temperature                 |     303 |   323 | PROBLEM    | Present      |     0.995938 |
|  5 | his respiratory congestion            |     489 |   514 | PROBLEM    | Present      |     0.999145 |
|  6 | more tired                            |     546 |   555 | PROBLEM    | Present      |     0.999283 |
|  7 | any diarrhea                          |     833 |   844 | PROBLEM    | Absent       |     0.998015 |
|  8 | yellow colored                        |     871 |   884 | PROBLEM    | Present      |     0.997913 |
|  9 | severe fever                          |     920 |   931 | PROBLEM    | Present      |     0.99936  |
| 10 | sore throat                           |     937 |   947 | PROBLEM    | Present      |     0.999398 |
| 11 | stomach pain                          |     962 |   973 | PROBLEM    | Absent       |     0.99866  |
| 12 | pain control                          |    1020 |  1031 | PROBLEM    | Hypothetical |     0.945752 |
| 13 | short of breath                       |    1049 |  1063 | PROBLEM    | Present      |     0.998179 |
| 14 | lung tumor                            |    1109 |  1118 | PROBLEM    | Present      |     0.998691 |
| 15 | Alzheimer                             |    1165 |  1173 | PROBLEM    | SomeoneElse  |     0.996398 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_jsl_onnx|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk]|
|Output Labels:|[assertion_onnx]|
|Language:|en|
|Size:|405.6 MB|
|Case sensitive:|true|