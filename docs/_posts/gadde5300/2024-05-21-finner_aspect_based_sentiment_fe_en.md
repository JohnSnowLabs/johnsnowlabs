---
layout: model
title: Financial NER on Aspect-Based Sentiment Analysis
author: John Snow Labs
name: finner_aspect_based_sentiment_fe
date: 2024-05-21
tags: [ner, finance, licensed, en]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
recommended: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This NER model identifies entities that can be associated with a financial sentiment. The model is trained using custom finance embeddings and is designed to be used with the associated Assertion Status model that classifies the entities into a sentiment category.

## Predicted Entities

`ASSET`, `CASHFLOW`, `EXPENSE`, `FREE_CASH_FLOW`, `GAINS`, `KPI`, `LIABILITY`, `LOSSES`, `PROFIT`, `REVENUE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_aspect_based_sentiment_fe_en_1.0.0_3.0_1716293156004.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_aspect_based_sentiment_fe_en_1.0.0_3.0_1716293156004.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model =finance.NerModel.pretrained("finner_aspect_based_sentiment_fe", "en", "finance/models")\
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

text = ["""Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."""]

res = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+--------+------+
|chunk   |label |
+--------+------+
|Equity  |GAINS |
|earnings|PROFIT|
+--------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_aspect_based_sentiment_fe|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|14.6 MB|

## Benchmarking

```bash
label              precision    recall  f1-score   support
ASSET                0.72      0.63      0.67       132
CASHFLOW             0.81      0.73      0.77        64
EXPENSE              0.76      0.85      0.81       315
FREE_CASH_FLOW       0.93      0.93      0.93        43
GAINS                0.78      0.81      0.80       161
KPI                  0.73      0.68      0.70       253
LIABILITY            0.73      0.67      0.70        93
LOSSES               0.79      0.80      0.80        56
PROFIT               0.80      0.91      0.85       223
REVENUE              0.81      0.80      0.80       492
micro-avg            0.78      0.79      0.78      1832
macro-avg            0.79      0.78      0.78      1832
weighted-avg         0.78      0.79      0.78      1832
```