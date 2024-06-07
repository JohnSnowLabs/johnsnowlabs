---
layout: model
title: Financial NER (xlg, XLarge)
author: John Snow Labs
name: finner_financial_xlarge_fe
date: 2024-06-07
tags: [broker_reports, earning_calls, sec10k, tensorflow, finance, en, licensed]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This financial model is an xlg (Xlarge) version, which has been trained with more general labels than other versions such (`md`, `lg`, ...) that are available in the Models Hub. The training corpus used for this model is a combination of Broker Reports, Earning Calls, and 10K filings,was trained using custom finance word embeddings.

## Predicted Entities

`INCOME`, `KPI_INCREASE`, `CF`, `CFO`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_financial_xlarge_fe_en_1.0.0_3.0_1717749730843.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_financial_xlarge_fe_en_1.0.0_3.0_1717749730843.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("finance_word_embeddings", "en", "finance/models")\
            .setInputCols(["sentence","token"])\
            .setOutputCol("embeddings")

ner_model =finance.NerModel.pretrained("finner_financial_xlarge_fe", "en", "finance/models")\
      .setInputCols(["sentence", "token", "embeddings"])\
      .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence","token","ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ['''We expect Revenue / PAT CAGR of ~ 19 %/~ 22 % over FY2022-FY2024E EPS . Hence , we retain our Buy recommendation on VGIL with an unchanged price target ( PT ) of . This includes $ 1 billion in cash and cash equivalents , $ 2 billion in property and equipment , and $ 2 billion in intangible assets .''']

res = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-------------------------+---------------+
|chunk                    |label          |
+-------------------------+---------------+
|PAT CAGR                 |EXPENSE        |
|19                       |PERCENTAGE     |
|22                       |PERCENTAGE     |
|EPS                      |PROFIT_INCREASE|
|$                        |CURRENCY       |
|1 billion                |AMOUNT         |
|cash and cash equivalents|CF             |
|$                        |CURRENCY       |
|2 billion                |AMOUNT         |
|$                        |CURRENCY       |
|2 billion                |AMOUNT         |
+-------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_financial_xlarge_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.8 MB|

## References

In-house dataset

## Benchmarking

```bash
                     precision    recall  f1-score   support
AMOUNT                   0.87      0.93      0.90      3206
ASSET                    0.00      0.00      0.00        24
CF                       0.67      0.56      0.61       476
CF_DECREASE              0.64      0.30      0.41        23
CF_INCREASE              0.61      0.83      0.71        59
COUNT                    0.33      0.36      0.35        11
CURRENCY                 0.89      0.98      0.93      2130
DATE                     0.90      0.93      0.91      1196
EXPENSE                  0.59      0.59      0.59       367
EXPENSE_DECREASE         0.59      0.63      0.61        73
EXPENSE_INCREASE         0.83      0.80      0.82       135
FCF                      0.68      0.94      0.79        16
FISCAL_YEAR              0.88      0.90      0.89       435
KPI                      0.33      0.08      0.12        13
KPI_DECREASE             0.33      0.25      0.29         4
KPI_INCREASE             0.00      0.00      0.00         8
LIABILITY                0.50      0.42      0.46       227
LIABILITY_DECREASE       1.00      0.20      0.33         5
LIABILITY_INCREASE       1.00      1.00      1.00         1
ORG                      0.94      0.89      0.91        18
PERCENTAGE               0.99      0.96      0.97       774
PROFIT                   0.70      0.62      0.66       377
PROFIT_DECLINE           0.54      0.41      0.47        63
PROFIT_INCREASE          0.70      0.57      0.62       201
TICKER                   1.00      0.94      0.97        17
micro-avg                0.85      0.87      0.86      9859
macro-avg                0.66      0.60      0.61      9859
weighted-avg             0.84      0.87      0.85      9859
```