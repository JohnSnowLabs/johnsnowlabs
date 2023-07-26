---
layout: model
title: Financial Twitter News Sentiment Analysis
author: John Snow Labs
name: finclf_bert_twitter_financial_news_sentiment
date: 2023-05-24
tags: [en, finance, twitter, news, sentiment, licensed, tensorflow]
task: Sentiment Analysis
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: FinanceBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to perform sentiment analysis on Twitter data, extracting three primary sentiments: `Bullish`, `Bearish`, and `Neutral`.

## Predicted Entities

`Bearish`, `Bullish`, `Neutral`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_news_sentiment_en_1.0.0_3.0_1684923548358.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_news_sentiment_en_1.0.0_3.0_1684923548358.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')

tokenizer = nlp.Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier = finance.BertForSequenceClassification.pretrained("finclf_bert_twitter_financial_news_sentiment", "en", "finance/models")\
  .setInputCols(["document",'token'])\
  .setOutputCol("class")
  
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier  
])

data = [["""$MPLX $MPC - MPLX cut at Credit Suisse on potential dilution from Marathon strategic review https://t.co/0BFQy4ZU6W"""],["""Biogen stock price target raised to $392 from $320 at Instinet"""],["""Luckin Coffee shares halted in premarket; news pending https://t.co/6Kz4NwnNFN"""]]

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

example = model.transform(spark.createDataFrame(data).toDF("text"))

example.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+-------------------------------------------------------------------------------------------------------------------+---------+
|text                                                                                                               |result   |
+-------------------------------------------------------------------------------------------------------------------+---------+
|$MPLX $MPC - MPLX cut at Credit Suisse on potential dilution from Marathon strategic review https://t.co/0BFQy4ZU6W|[Bearish]|
|Biogen stock price target raised to $392 from $320 at Instinet                                                     |[Bullish]|
|Luckin Coffee shares halted in premarket; news pending https://t.co/6Kz4NwnNFN                                     |[Neutral]|
+-------------------------------------------------------------------------------------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finclf_bert_twitter_financial_news_sentiment|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|406.4 MB|
|Case sensitive:|true|
|Max sentence length:|512|

## References

In-house annotations on financial reports

## Benchmarking

```bash
label              precision    recall  f1-score   support
     Bearish       0.80      0.72      0.76       379
     Bullish       0.82      0.78      0.80       468
     Neutral       0.90      0.94      0.92      1540
    accuracy                           0.87      2387
   macro-avg       0.84      0.81      0.83      2387
weighted-avg       0.87      0.87      0.87      2387

```