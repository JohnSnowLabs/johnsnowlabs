---
layout: model
title: Financial Assertion of Sentiment (sm, Small)
author: John Snow Labs
name: finassertion_absa_sm
date: 2023-10-06
tags: [finance, assertion, en, sentiment_analysis, licensed]
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

This assertion model classifies financial entities into a sentiment. It is designed to be used together with the associated NER model.

## Predicted Entities

`POSITIVE`, `NEGATIVE`, `NEUTRAL`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finassertion_absa_sm_en_1.0.0_3.0_1696606845902.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finassertion_absa_sm_en_1.0.0_3.0_1696606845902.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = (
    nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")
)

# Sentence Detector annotator, processes various sentences per line
sentenceDetector = (
    nlp.SentenceDetector()
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

# Tokenizer splits words in a relevant format for NLP
tokenizer = (
    nlp.Tokenizer().setInputCols(["sentence"]).setOutputCol("token")
)

bert_embeddings = (
    nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base", "en")
    .setInputCols("document", "token")
    .setOutputCol("embeddings")
    .setMaxSentenceLength(512)
)

clinical_ner = (
    finance.NerModel.pretrained("finner_absa_sm", "en", "finance/models")
    .setInputCols(["sentence", "token", "embeddings"])
    .setOutputCol("ner")
)

ner_converter = (
    finance.NerConverterInternal()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

assertion_model = (
    finance.AssertionDLModel.pretrained("finassertion_absa_sm", "en", "finance/models")
    .setInputCols(["sentence", "ner_chunk", "embeddings"])
    .setOutputCol("assertion")
)

nlpPipeline = nlp.Pipeline(
    stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        bert_embeddings,
        clinical_ner,
        ner_converter,
        assertion_model,
    ]
)


text = "Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."

spark_df = spark.createDataFrame([[text]]).toDF("text")

result = model.fit(spark_df ).transform(spark_df)

result.select(
    F.explode(
        F.arrays_zip("ner_chunk.result", "ner_chunk.metadata")
    ).alias("cols")
).select(
    F.expr("cols['0']").alias("entity"),
    F.expr("cols['1']['entity']").alias("label"),
).show(
    50, truncate=False
)
```

</div>

## Results

```bash
+--------+---------+
|entity  |label    |
+--------+---------+
|Equity  |LIABILITY|
|earnings|PROFIT   |
+--------+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finassertion_absa_sm|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|2.7 MB|

## References

In-house annotations of earning call transcripts.

## Benchmarking

```bash
     label    precision    recall  f1-score   support

    NEGATIVE       0.57      0.42      0.48        74
     NEUTRAL       0.51      0.70      0.59       184
    POSITIVE       0.75      0.64      0.69       324
```