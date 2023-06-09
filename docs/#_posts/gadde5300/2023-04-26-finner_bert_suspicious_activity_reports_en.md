---
layout: model
title: Financial Suspicious Activity Reports NER
author: John Snow Labs
name: finner_bert_suspicious_activity_reports
date: 2023-04-26
tags: [finance, suspicious_activity_reports, en, bert, licensed, tensorflow]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceBertForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Financial BertForTokenClassification NER model aimed to extract entities from suspicious activity reports that are filed by financial institutions, and those associated with their business, with the Financial Crimes Enforcement Network.

## Predicted Entities

`SUSPICIOUS_ITEMS`, `PERSON_NAME`, `SUSPICIOUS_ACTION`, `SUSPICIOUS_KEYWORD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_bert_suspicious_activity_reports_en_1.0.0_3.0_1682502028225.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_bert_suspicious_activity_reports_en_1.0.0_3.0_1682502028225.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
  .setInputCol("text")\
  .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
  .setInputCols("document")\
  .setOutputCol("token")

tokenClassifier = finance.BertForTokenClassification.pretrained("finner_bert_suspicious_activity_reports", "en", "finance/models")\
  .setInputCols("token", "document")\
  .setOutputCol("label")\
  .setCaseSensitive(True)

ner_converter = nlp.NerConverter()\
        .setInputCols(["document","token","label"])\
        .setOutputCol("ner_chunk")

pipeline =  nlp.Pipeline(stages=[
  documentAssembler,
  tokenizer,
  tokenClassifier,
    ner_converter
    ]
)

import pandas as pd

p_model = pipeline.fit(spark.createDataFrame(pd.DataFrame({'text': ['']})))


text = """SUSPICIOUS ACTIVITY REPORT

Date: [Today's Date]

To: [Financial Institution's Compliance Department]

Subject: Suspicious Activity Related to Business Loan

Account Holder Information:
Name: [Name of Business]
Address: [Business Address]
Account Number: [Business Account Number]

Description of Activity:
On [Date], [Name of Business] submitted a loan application for a substantial amount of money. The loan officer reviewing the application noticed several indications of possible suspicious activity."""

res = p_model.transform(spark.createDataFrame([[text]]).toDF("text"))

result_df = res.select(F.explode(F.arrays_zip(res.token.result,res.label.result, res.label.metadata)).alias("cols"))\
                  .select(F.expr("cols['0']").alias("token"),
                          F.expr("cols['1']").alias("label"),
                          F.expr("cols['2']['confidence']").alias("confidence"))

result_df.show(100, truncate=100)
```

</div>

## Results

```bash
+-------------+--------------------+
|chunk        |entity              |
+-------------+--------------------+
|SUSPICIOUS   |B-SUSPICIOUS_KEYWORD|
|ACTIVITY     |O                   |
|REPORT       |O                   |
|Date         |O                   |
|:            |O                   |
|[Today's     |O                   |
|Date]        |O                   |
|To           |O                   |
|:            |O                   |
|[Financial   |O                   |
|Institution's|O                   |
|Compliance   |O                   |
|Department]  |O                   |
|Subject      |O                   |
|:            |O                   |
|Suspicious   |B-SUSPICIOUS_KEYWORD|
|Activity     |O                   |
|Related      |O                   |
|to           |O                   |
|Business     |B-SUSPICIOUS_ACTION |
|Loan         |I-SUSPICIOUS_ACTION |
|Account      |O                   |
|Holder       |O                   |
|Information  |O                   |
|:            |O                   |
|Name         |O                   |
|:            |O                   |
|[Name        |O                   |
|of           |O                   |
|Business]    |O                   |
|Address      |O                   |
|:            |O                   |
|[Business    |O                   |
|Address]     |O                   |
|Account      |O                   |
|Number       |O                   |
|:            |O                   |
|[Business    |O                   |
|Account      |O                   |
|Number]      |O                   |
|Description  |O                   |
|of           |O                   |
|Activity     |O                   |
|:            |O                   |
|On           |O                   |
|[Date]       |O                   |
|,            |O                   |
|[Name        |O                   |
|of           |O                   |
|Business]    |O                   |
|submitted    |O                   |
|a            |O                   |
|loan         |B-SUSPICIOUS_ACTION |
|application  |I-SUSPICIOUS_ACTION |
|for          |O                   |
|a            |O                   |
|substantial  |O                   |
|amount       |O                   |
|of           |O                   |
|money        |O                   |
|.            |O                   |
|The          |O                   |
|loan         |O                   |
|officer      |O                   |
|reviewing    |O                   |
|the          |O                   |
|application  |O                   |
|noticed      |O                   |
|several      |O                   |
|indications  |O                   |
|of           |O                   |
|possible     |O                   |
|suspicious   |B-SUSPICIOUS_KEYWORD|
|activity     |O                   |
|.            |O                   |
+-------------+--------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_bert_suspicious_activity_reports|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|404.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|

## References

In house annotated data

## Benchmarking

```bash

label                      precision    recall  f1-score   support

  B-SUSPICIOUS_ITEMS       0.75      0.84      0.79      1079
       B-PERSON_NAME       0.97      0.97      0.97        88
       I-PERSON_NAME       0.98      0.99      0.98       171
 B-SUSPICIOUS_ACTION       0.91      0.87      0.89       752
 I-SUSPICIOUS_ACTION       0.93      0.91      0.92       814
B-SUSPICIOUS_KEYWORD       0.91      0.97      0.94      1528
  I-SUSPICIOUS_ITEMS       0.77      0.84      0.81       659
           micro-avg       0.86      0.90      0.88      5091
           macro-avg       0.89      0.91      0.90      5091
        weighted-avg       0.86      0.90      0.88      5091

```