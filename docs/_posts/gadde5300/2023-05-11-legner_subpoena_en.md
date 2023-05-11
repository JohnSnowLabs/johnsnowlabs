---
layout: model
title: Legal Subpoenas NER (small)
author: John Snow Labs
name: legner_subpoena
date: 2023-05-11
tags: [legal, subpoena, en, licensed]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a legal NER mode trained on Subpoenas, which is aimed to extract the following entities from a Subpoena. `ADDRESS`, `MATTER_VS`, `APPOINTMENT_HOUR`, `DOCUMENT_TOPIC`, `DOCUMENT_PERSON`, `COURT_ADDRESS`, `APPOINTMENT_DATE`, `COUNTY`, `CASE`, `SIGNER`, `COURT`, `DOCUMENT_DATE_TO`, `DOCUMENT_TYPE`, `STATE`, `DOCUMENT_DATE_FROM`, `RECEIVER`, `MATTER`, `SUBPOENA_DATE`, `DOCUMENT_DATE_YEAR`

## Predicted Entities

`ADDRESS`, `MATTER_VS`, `APPOINTMENT_HOUR`, `DOCUMENT_TOPIC`, `DOCUMENT_PERSON`, `COURT_ADDRESS`, `APPOINTMENT_DATE`, `COUNTY`, `CASE`, `SIGNER`, `COURT`, `DOCUMENT_DATE_TO`, `DOCUMENT_TYPE`, `STATE`, `DOCUMENT_DATE_FROM`, `RECEIVER`, `MATTER`, `SUBPOENA_DATE`, `DOCUMENT_DATE_YEAR`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_subpoena_en_1.0.0_3.0_1683798607192.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_subpoena_en_1.0.0_3.0_1683798607192.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

textSplitter = legal.TextSplitter()\
    .setInputCols(['document'])\
    .setOutputCol('sentence')

token = nlp.Tokenizer()\
    .setInputCols(['sentence'])\
    .setOutputCol('token')

roberta_embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings") \
    .setMaxSentenceLength(512)
  
loaded_ner_model = legal.NerModel.pretrained('legner_subpoena','en','legal/models')\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

converter = nlp.NerConverter()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_span")

ner_prediction_pipeline = nlp.Pipeline(stages = [
                                            document,
                                            textSplitter,
                                            token,
                                            roberta_embeddings,
                                            loaded_ner_model,
                                            converter
                                            ])

empty_data = spark.createDataFrame([['']]).toDF("text")

prediction_model = ner_prediction_pipeline.fit(empty_data)

text = """ABC Corporation Case Number : 2023-0456-7890 To Whom It May Concern , Please be advised that on behalf of John Doe , we have issued a subpoena to ABC Corporation for the production of financial records . SUBPOENA REPORT STATE : New York COURT : Supreme Court of New York COUNTY : New York County CASE NO : 2023-456789 To : Jane Doe Address : 456 Park Avenue , New York , NY 10022 You are hereby commanded to appear before the Supreme Court of New York on the date and time specified below to give testimony in the above-mentioned case ."""

sample_data = spark.createDataFrame([[text]]).toDF("text")

preds = prediction_model.transform(sample_data)
```

</div>

## Results

```bash
+-------------------------------------+---------------+
|chunk                                |entity         |
+-------------------------------------+---------------+
|ABC Corporation                      |MATTER_VS      |
|2023-0456-7890                       |CASE           |
|John Doe                             |DOCUMENT_PERSON|
|ABC Corporation                      |DOCUMENT_PERSON|
|financial records                    |DOCUMENT_TYPE  |
|New York                             |STATE          |
|Supreme Court                        |COURT          |
|New York                             |STATE          |
|New York County                      |COUNTY         |
|2023-456789                          |CASE           |
|Jane Doe                             |RECEIVER       |
|456 Park Avenue , New York , NY 10022|ADDRESS        |
|Supreme Court                        |COURT          |
|New York                             |STATE          |
|testimony                            |DOCUMENT_TYPE  |
+-------------------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_subpoena|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.4 MB|

## References

In house annotated dataset

## Benchmarking

```bash
label                     precision    recall  f1-score   support
           B-ADDRESS       0.92      0.80      0.86        61
         B-MATTER_VS       0.84      0.84      0.84        49
           I-ADDRESS       0.90      0.77      0.83       430
  B-APPOINTMENT_HOUR       0.98      1.00      0.99        46
    I-DOCUMENT_TOPIC       0.67      0.56      0.61        68
   B-DOCUMENT_PERSON       0.86      0.92      0.89       374
     B-COURT_ADDRESS       0.63      0.71      0.67        24
  I-APPOINTMENT_DATE       1.00      0.90      0.95       149
            I-COUNTY       0.88      0.98      0.93       102
              B-CASE       0.85      1.00      0.92        41
            B-SIGNER       0.84      0.66      0.74        32
             I-COURT       0.97      0.91      0.94        85
  B-DOCUMENT_DATE_TO       1.00      1.00      1.00        52
     B-DOCUMENT_TYPE       0.95      0.93      0.94       699
             I-STATE       1.00      0.67      0.80        27
I-DOCUMENT_DATE_FROM       0.98      1.00      0.99       196
    B-DOCUMENT_TOPIC       0.83      0.84      0.84       230
          I-RECEIVER       0.79      0.93      0.85        82
B-DOCUMENT_DATE_FROM       0.99      1.00      0.99        66
  I-APPOINTMENT_HOUR       0.97      1.00      0.98        57
            I-SIGNER       0.90      0.65      0.75        40
            B-COUNTY       0.92      1.00      0.96        47
            B-MATTER       0.89      0.89      0.89        45
  I-DOCUMENT_DATE_TO       1.00      1.00      1.00       154
     I-SUBPOENA_DATE       0.81      0.91      0.86       148
  B-APPOINTMENT_DATE       0.94      0.92      0.93        51
             B-COURT       0.97      0.89      0.93        85
     I-DOCUMENT_TYPE       0.96      0.86      0.91       243
          B-RECEIVER       0.78      0.92      0.84        71
            I-MATTER       0.84      0.93      0.88        45
         I-MATTER_VS       0.87      0.67      0.75        30
B-DOCUMENT_DATE_YEAR       0.92      1.00      0.96        34
             B-STATE       0.91      0.86      0.88        83
     B-SUBPOENA_DATE       0.81      0.88      0.84        48
     I-COURT_ADDRESS       0.60      0.84      0.70       221
   I-DOCUMENT_PERSON       0.90      0.91      0.91       300
           micro-avg       0.89      0.89      0.89      4515
           macro-avg       0.89      0.88      0.88      4515
        weighted-avg       0.89      0.89      0.89      4515
```
