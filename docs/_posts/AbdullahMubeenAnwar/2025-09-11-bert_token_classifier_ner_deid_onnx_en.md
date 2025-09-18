---
layout: model
title: Detect PHI for Deidentification (BertForTokenClassification - ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_deid_onnx
date: 2025-09-11
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Deidentification NER is a Named Entity Recognition model that annotates text to find protected health information that may need to be de-identified. It detects 23 entities. This ner model is trained with a combination of the i2b2 train set and a re-augmented version of i2b2 train set using `BertForTokenClassification`


We sticked to official annotation guideline (AG) for 2014 i2b2 Deid challenge while annotating new datasets for this model. All the details regarding the nuances and explanations for AG can be found here [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4978170/)

## Predicted Entities

`I-DATE`, `I-CITY`, `B-EMAIL`, `I-HOSPITAL`, `B-STATE`, `B-PHONE`, `B-MEDICALRECORD`, `B-HOSPITAL`, `B-USERNAME`, `I-ZIP`, `I-COUNTRY`, `B-ZIP`, `O`, `B-PROFESSION`, `I-URL`, `B-STREET`, `B-BIOID`, `B-URL`, `I-FAX`, `I-LOCATION-OTHER`, `I-AGE`, `I-DOCTOR`, `I-MEDICALRECORD`, `I-STATE`, `B-CITY`, `I-ORGANIZATION`, `B-DEVICE`, `I-STREET`, `B-COUNTRY`, `B-HEALTHPLAN`, `I-PATIENT`, `B-DOCTOR`, `B-AGE`, `I-PHONE`, `B-ORGANIZATION`, `I-IDNUM`, `I-DEVICE`, `B-FAX`, `B-LOCATION-OTHER`, `B-PATIENT`, `B-IDNUM`, `I-PROFESSION`, `B-DATE`, `I-HEALTHPLAN`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_deid_onnx_en_6.1.1_3.0_1757555160962.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_deid_onnx_en_6.1.1_3.0_1757555160962.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["document"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_deid_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverterInternal()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "A. Record date : 2093-01-13, David Hale, M.D. Name : Hendrickson, Ora MR. # 7194334. PCP : Oliveira, non-smoking. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_deid_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "document"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = nlp.Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "A. Record date : 2093-01-13, David Hale, M.D. Name : Hendrickson, Ora MR. # 7194334. PCP : Oliveira, non-smoking. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```

```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_ner_deid_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "A. Record date : 2093-01-13, David Hale, M.D. Name : Hendrickson, Ora MR. # 7194334. PCP : Oliveira, non-smoking. Cocke County Baptist Hospital. 0295 Keats Street. Phone +1 (302) 786-5227. Patient's complaints first surfaced when he started working for Brothers Coal-Mine."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------------+------------+
|text                         |entity      |
+-----------------------------+------------+
|2093-01-13                   |DATE        |
|David Hale                   |DOCTOR      |
|Hendrickson, Ora             |CITY        |
|7194334                      |IDNUM       |
|Oliveira                     |PATIENT     |
|Cocke County Baptist Hospital|HOSPITAL    |
|0295 Keats Street            |PHONE       |
|302) 786-5227                |PHONE       |
|Brothers Coal-Mine           |ORGANIZATION|
+-----------------------------+------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_deid_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.8 MB|
|Case sensitive:|true|
|Max sentence length:|128|