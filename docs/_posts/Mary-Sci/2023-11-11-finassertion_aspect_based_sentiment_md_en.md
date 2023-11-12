---
layout: model
title: Financial Assertion of Aspect-Based Sentiment (md, Medium)
author: John Snow Labs
name: finassertion_aspect_based_sentiment_md
date: 2023-11-11
tags: [assertion, licensed, en, finance]
task: Assertion Status
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This assertion model classifies financial entities into an aspect-based sentiment. It is designed to be used together with the associated NER model.

## Predicted Entities

`POSITIVE`, `NEGATIVE`, `NEUTRAL`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finassertion_aspect_based_sentiment_md_en_1.0.0_3.0_1699705705778.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finassertion_aspect_based_sentiment_md_en_1.0.0_3.0_1699705705778.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setInputCols("sentence", "token")\
    .setOutputCol("embeddings")\
    .setMaxSentenceLength(512)

finance_ner = finance.NerModel.pretrained("finner_aspect_based_sentiment_md", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

assertion_model = finance.AssertionDLModel.pretrained("finassertion_aspect_based_sentiment_md", "en", "finance/models")\
    .setInputCols(["sentence", "ner_chunk", "embeddings"])\
    .setOutputCol("assertion")


nlpPipeline = nlp.Pipeline(
    stages=[documentAssembler,
            sentenceDetector,
            tokenizer,
            bert_embeddings,
            finance_ner,
            ner_converter,
            assertion_model])

text = "Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."

spark_df = spark.createDataFrame([[text]]).toDF("text")

result = nlpPipeline.fit(spark_df ).transform(spark_df)

result.select(F.explode(F.arrays_zip("ner_chunk.result", "ner_chunk.metadata", "assertion.result", "assertion.metadata")).alias("cols"))\
      .select(F.expr("cols['0']").alias("entity"),
              F.expr("cols['1']['entity']").alias("label"),
              F.expr("cols['2']").alias("assertion"),
              F.expr("cols['3']['confidence']").alias("confidence")).show(50, truncate=False)
```

</div>

## Results

```bash
+--------+---------+---------+----------+
|entity  |label    |assertion|confidence|
+--------+---------+---------+----------+
|Equity  |LIABILITY|POSITIVE |0.9895    |
|earnings|PROFIT   |POSITIVE |0.995     |
+--------+---------+---------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finassertion_aspect_based_sentiment_md|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|2.7 MB|

## Benchmarking

```bash
 label         precision  recall  f1-score  support 
 NEGATIVE      0.68       0.43    0.53      232     
 NEUTRAL       0.44       0.65    0.53      441     
 POSITIVE      0.79       0.69    0.74      947     
 accuracy      -          -       0.64      1620    
 macro-avg     0.64       0.59    0.60      1620    
 weighted-avg  0.68       0.64    0.65      1620    
```
