---
layout: model
title: Financial NER on Aspect-Based Sentiment Analysis
author: John Snow Labs
name: finner_aspect_based_sentiment_md
date: 2023-11-11
tags: [ner, licensed, finance, en]
task: Named Entity Recognition
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This Financial NER model can extract fine-grained information with respect to entities mentioned in user comments.

## Predicted Entities

`ASSET`, `CASHFLOW`, `EXPENSE`, `FREE_CASH_FLOW`, `GAINS`, `KPI`, `LIABILITY`, `LOSSES`, `PROFIT`, `REVENUE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_aspect_based_sentiment_md_en_1.0.0_3.0_1699704469251.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_aspect_based_sentiment_md_en_1.0.0_3.0_1699704469251.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

# Tokenizer splits words in a relevant format for NLP
tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

bert_embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")\
    .setInputCols("document", "token")\
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)


ner_model = finance.NerModel().pretrained("finner_aspect_based_sentiment_md", "en", "finance/models")\
    .setInputCols(["document", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        bert_embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = nlpPipeline.fit(empty_data)

text = ["""Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."""]
result = model.transform(spark.createDataFrame([text]).toDF("text"))

from pyspark.sql import functions as F

result.select(F.explode(F.arrays_zip(result.ner_chunk.result, result.ner_chunk.begin, result.ner_chunk.end, result.ner_chunk.metadata)).alias("cols")) \
               .select(F.expr("cols['0']").alias("chunk"),
                       F.expr("cols['1']").alias("begin"),
                       F.expr("cols['2']").alias("end"),
                       F.expr("cols['3']['entity']").alias("ner_label")
                       ).show(100, truncate=False)
```

</div>

## Results

```bash
+--------+-----+---+---------+
|chunk   |begin|end|ner_label|
+--------+-----+---+---------+
|Equity  |1    |6  |LIABILITY|
|earnings|12   |19 |PROFIT   |
+--------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finner_aspect_based_sentiment_md|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.5 MB|

## Benchmarking

```bash
 label           precision  recall  f1-score  support 
 ASSET           0.50       0.72    0.59      53      
 CASHFLOW        0.78       0.60    0.68      30      
 EXPENSE         0.71       0.68    0.70      151     
 FREE_CASH_FLOW  1.00       1.00    1.00      19      
 GAINS           0.80       0.78    0.79      55      
 KPI             0.72       0.58    0.64      106     
 LIABILITY       0.65       0.51    0.57      39      
 LOSSES          0.77       0.59    0.67      29      
 PROFIT          0.77       0.74    0.75      101     
 REVENUE         0.74       0.78    0.76      231     
 micro-avg       0.72       0.71    0.71      814     
 macro-avg       0.74       0.70    0.71      814     
 weighted-avg    0.73       0.71    0.71      814  
```