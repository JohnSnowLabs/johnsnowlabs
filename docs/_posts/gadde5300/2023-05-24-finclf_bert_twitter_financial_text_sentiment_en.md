---
layout: model
title: Financial Twitter Texts Sentiment Analysis
author: John Snow Labs
name: finclf_bert_twitter_financial_text_sentiment
date: 2023-05-24
tags: [en, finance, sentiment, bert, licensed, tensorflow]
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

This model is designed to perform sentiment analysis on Twitter data, extracting three primary sentiments: `Positive`, `Negative`, and `Neutral`.

## Predicted Entities

`Positive`, `Negative`, `Neutral`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_text_sentiment_en_1.0.0_3.0_1684941800385.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finclf_bert_twitter_financial_text_sentiment_en_1.0.0_3.0_1684941800385.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sequenceClassifier = finance.BertForSequenceClassification.pretrained("finclf_bert_twitter_financial_text_sentiment", "en", "finance/models")\
  .setInputCols(["document",'token'])\
  .setOutputCol("class")
  
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    tokenizer,
    sequenceClassifier  
])


empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

data = [["""Early Crater Lake Drill Results Return Better Than Expected Grades and Intersection Lengths â€“ 79.7 meters at 311 g/t Scandium Oxide, 0.326% Rare Earths Oxides and Yttrium --  Imperial Mining Group Ltd. ("Imperial") (TSX VENTURE: IPG; OTCQB: IMPNF) is pleased to announce that it has completed its Summer 2022 exploration and definition diamond drill program on the Ta-Nb Target and the TG Zone. Early results are encouraging and give inference to grade and tonnage increases to the TG North Lobe Deposit resource (see Imperial Press release - SEP 23, 2021)."""],["""Noranda Income Fund Provides an Update on Operational and Production Challenges and Announces a Cellhouse Maintenance Shutdown --  Noranda Income Fund (TSX:NIF.UN) (the â€œFundâ€) today provided an update regarding its previously disclosed challenges with cellhouse operating conditions and equipment fragility, which have been adversely affecting zinc production volumes and output quality."""]]

# couple of simple examples
example = model.transform(spark.createDataFrame(data).toDF("text"))

example.select("text", "class.result").show(truncate=False)
```

</div>

## Results

```bash
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |result    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|Early Crater Lake Drill Results Return Better Than Expected Grades and Intersection Lengths â€“ 79.7 meters at 311 g/t Scandium Oxide, 0.326% Rare Earths Oxides and Yttrium --  Imperial Mining Group Ltd. ("Imperial") (TSX VENTURE: IPG; OTCQB: IMPNF) is pleased to announce that it has completed its Summer 2022 exploration and definition diamond drill program on the Ta-Nb Target and the TG Zone. Early results are encouraging and give inference to grade and tonnage increases to the TG North Lobe Deposit resource (see Imperial Press release - SEP 23, 2021).|[Positive]|
|Noranda Income Fund Provides an Update on Operational and Production Challenges and Announces a Cellhouse Maintenance Shutdown --  Noranda Income Fund (TSX:NIF.UN) (the â€œFundâ€) today provided an update regarding its previously disclosed challenges with cellhouse operating conditions and equipment fragility, which have been adversely affecting zinc production volumes and output quality.                                                                                                                                                                       |[Negative]|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finclf_bert_twitter_financial_text_sentiment|
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
    Negative       0.75      0.60      0.67        15
     Neutral       0.89      0.87      0.88       207
    Positive       0.83      0.87      0.85       134
    accuracy         -             -     0.86       356
   macro-avg       0.82      0.78      0.80       356
weighted-avg       0.86      0.86      0.86       356

```