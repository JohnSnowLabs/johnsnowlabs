---
layout: model
title: Legal NER on Subpoenas (Small)
author: John Snow Labs
name: legner_bert_subpoenas_sm
date: 2023-08-07
tags: [en, licensed, tensorflow]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: LegalBertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a financial NER model aimed to extract 19 entities from subpoenas. This is called a small version because it has been trained on more generic labels. The larger versions of this model will be available on models hub.

## Predicted Entities

`COURT`, `APPOINTMENT_DATE`, `DEADLINE_DATE`, `DOCUMENT_DATE_FROM`, `ADDRESS`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_bert_subpoenas_sm_en_1.0.0_3.0_1691423741988.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_bert_subpoenas_sm_en_1.0.0_3.0_1691423741988.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from pyspark.sql import functions as F

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")\

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")\

tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

ner_model = legal.BertForTokenClassification.pretrained("legner_bert_subpoenas_sm", "en", "legal/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)\
    .setMaxSentenceLength(512)

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline =  nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    ner_model,
    ner_converter
])


empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

text = """In addition , in an earlier motion for summary disposition in which all Respondents joined , and which this Court denied in its Order of April30 , 2013 , Respondent Deloitte Touche Tohmatsu Certified Public Accountants Ltd ."""
data = spark.createDataFrame([[text]]).toDF("text")

result = model.transform(data)

result.select(F.explode(F.arrays_zip('ner_chunk.result', 'ner_chunk.metadata')).alias("cols")) \
          .select(F.expr("cols['0']").alias("chunk"),
                       F.expr("cols['1']['entity']").alias("label")).show(50, truncate = False)
```

</div>

## Results

```bash
+------------------------+---------------+
|chunk                   |label          |
+------------------------+---------------+
|summary disposition     |DOCUMENT_TYPE  |
|Deloitte Touche Tohmatsu|DOCUMENT_PERSON|
+------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_bert_subpoenas_sm|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|401.1 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## References

In House annotated dataset

## Benchmarking

```bash
label                      precision    recall  f1-score   support
             B-COURT       1.00      0.60      0.75        30
  I-APPOINTMENT_DATE       0.57      0.65      0.60        20
             I-COURT       0.93      0.89      0.91       166
  B-APPOINTMENT_DATE       0.67      0.44      0.53         9
     I-DEADLINE_DATE       0.83      0.26      0.40        19
B-DOCUMENT_DATE_FROM       0.80      1.00      0.89        16
           I-ADDRESS       0.87      0.94      0.90      1046
  B-APPOINTMENT_HOUR       0.43      0.92      0.59        13
  B-DOCUMENT_DATE_TO       0.88      1.00      0.93         7
  I-APPOINTMENT_HOUR       1.00      0.15      0.26        20
   B-DOCUMENT_PERSON       0.79      0.84      0.82      2919
B-DOCUMENT_DATE_YEAR       0.00      0.00      0.00         5
             B-STATE       0.59      0.79      0.68        24
         I-MATTER_VS       0.65      0.79      0.71       150
              I-CASE       0.00      0.00      0.00        11
            I-COUNTY       0.00      0.00      0.00         0
    B-DOCUMENT_TOPIC       0.64      0.77      0.70       208
            B-COUNTY       0.00      0.00      0.00         0
            B-MATTER       0.85      0.86      0.86       328
I-DOCUMENT_DATE_FROM       0.87      1.00      0.93        48
     I-SUBPOENA_DATE       0.56      0.28      0.38        53
            I-SIGNER       0.56      0.46      0.50        59
  I-DOCUMENT_DATE_TO       0.83      1.00      0.91        25
          I-RECEIVER       0.71      0.52      0.60        98
            B-SIGNER       0.76      0.49      0.59        39
    I-DOCUMENT_TOPIC       0.83      0.80      0.81       725
             I-STATE       0.67      0.29      0.40        14
         B-MATTER_VS       0.78      0.82      0.80       136
     I-DOCUMENT_TYPE       0.83      0.87      0.85       621
     B-DEADLINE_DATE       0.00      0.00      0.00         6
            I-MATTER       0.88      0.82      0.85       479
     B-DOCUMENT_TYPE       0.87      0.90      0.88      1714
           B-ADDRESS       0.81      0.83      0.82       101
     B-SUBPOENA_DATE       0.42      0.28      0.33        18
              B-CASE       0.91      0.97      0.94       312
   I-DOCUMENT_PERSON       0.80      0.83      0.81      3672
          B-RECEIVER       0.76      0.63      0.69        46
           micro-avg       0.82      0.84      0.83     13157
           macro-avg       0.66      0.61      0.61     13157
        weighted-avg       0.82      0.84      0.83     13157
```