---
layout: model
title: Financial Twitter Texts Sentiment Analysis (Large)
author: John Snow Labs
name: finclf_bert_twitter_financial_text_sentiment_lg
date: 2023-05-25
tags: [en, finance, bert, sentiment, licensed, tensorflow]
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

This model is designed to perform sentiment analysis on Twitter data, extracting three primary sentiments: `Bullish`, `Bearish`, and `Neutral`.  This model is the large version of `finclf_bert_twitter_financial_news_sentiment` as it is trained on a much larger dataset.

## Predicted Entities

`Bullish`, `Bearish`, `Neutral`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_text_sentiment_lg_en_1.0.0_3.0_1684995427342.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_text_sentiment_lg_en_1.0.0_3.0_1684995427342.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = finance.BertForSequenceClassification.pretrained("finclf_bert_twitter_financial_text_sentiment_lg", "en", "finance/models")\
  .setInputCols(["document",'token'])\
  .setOutputCol("class")
  
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier  
])

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = pipeline.fit(empty_data)

data = [["""$GM: Deutsche Bank cuts to Hold """],["""HELSINKI (Thomson Financial)- Kemira GrowHow swung into profit in its first quarter earnings on improved sales , especially in its fertilizer business in Europe , which is normally stronger during the first quarter ."""],["""Vianor sells tires for cars and trucks as well as a range of other car parts and provides maintenance services ."""],["""Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing ."""]]

# couple of simple examples
example = model.transform(spark.createDataFrame(data).toDF("text"))

example.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
|text                                                                                                                                                                                                                    |result   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
|$GM: Deutsche Bank cuts to Hold                                                                                                                                                                                         |[Bearish]|
|HELSINKI (Thomson Financial)- Kemira GrowHow swung into profit in its first quarter earnings on improved sales , especially in its fertilizer business in Europe , which is normally stronger during the first quarter .|[Bullish]|
|Vianor sells tires for cars and trucks as well as a range of other car parts and provides maintenance services .                                                                                                        |[Neutral]|
|Pharmaceuticals group Orion Corp reported a fall in its third-quarter earnings that were hit by larger expenditures on R&D and marketing .                                                                              |[Bearish]|
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finclf_bert_twitter_financial_text_sentiment_lg|
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
label             precision    recall  f1-score   support
      Bearish       0.84      0.85      0.84       624
      Bullish       0.90      0.88      0.89      1064
      Neutral       0.94      0.94      0.94      2679
    accuracy          -         -       0.91      4367
    macro-avg       0.89      0.89      0.89      4367
weighted-avg        0.91      0.91      0.91      4367
```