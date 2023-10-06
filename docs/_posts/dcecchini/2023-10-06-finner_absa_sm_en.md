---
layout: model
title: Financial NER for Aspect-based Sentiment Analysis (sm, Small)
author: John Snow Labs
name: finner_absa_sm
date: 2023-10-06
tags: [finance, en, ner, licensed]
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

This NER model identifies entities that can be associated with a financial sentiment. The model is designed to be used with the associated Assertion Status model that classifies the entities into a sentiment category.

## Predicted Entities

`REVENUE`, `EXPENSE`, `PROFIT`, `KPI`, `GAINS`, `ASSET`, `LIABILITY`, `CASHFLOW`, `LOSSES`, `FREE_CASH_FLOW`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finner_absa_sm_en_1.0.0_3.0_1696605316183.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finner_absa_sm_en_1.0.0_3.0_1696605316183.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence") \
    .setCustomBounds(["\n\n"])

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_sec_bert_base","en")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(True)\
    .setMaxSentenceLength(512)

ner_model = finance.NerModel.pretrained("finner_absa_sm", "en", "finance/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")\

ner_converter = finance.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

model = pipeline.fit(spark.createDataFrame([[""]]).toDF("text"))


text = "Equity and earnings of affiliates in Latin America increased to $4.8 million in the quarter from $2.2 million in the prior year as the commodity markets in Latin America remain strong through the end of the quarter."

spark_df = spark.createDataFrame([[text]]).toDF("text")

result = model. Transform(spark_df)
result. Select(F.explode(F.arrays_zip('ner_chunk.result', 'ner_chunk.metadata')).alias("cols")) \
               .select(F.expr("cols['0']").alias("entity"),
                       F.expr("cols['1']['entity']").alias("label")).show(50, truncate = False)

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
|Model Name:|finner_absa_sm|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.3 MB|

## References

In-house annotations of earning call transcripts.

## Benchmarking

```bash
         label    precision    recall  f1-score   support

         B-ASSET     0.6000    0.2400    0.3429        25
      B-CASHFLOW     0.7000    0.5833    0.6364        12
       B-EXPENSE     0.7222    0.6500    0.6842        60
B-FREE_CASH_FLOW     1.0000    1.0000    1.0000         8
         B-GAINS     0.7333    0.5946    0.6567        37
           B-KPI     0.7143    0.5556    0.6250        36
     B-LIABILITY     0.5000    0.2778    0.3571        18
        B-LOSSES     0.7143    0.7143    0.7143         7
        B-PROFIT     0.8462    0.8919    0.8684        37
       B-REVENUE     0.7385    0.8000    0.7680        60
         I-ASSET     0.8000    0.3636    0.5000        11
      I-CASHFLOW     0.9091    0.9091    0.9091        11
       I-EXPENSE     0.7451    0.6230    0.6786        61
I-FREE_CASH_FLOW     1.0000    1.0000    1.0000        17
         I-GAINS     0.8333    0.6667    0.7407        30
           I-KPI     0.8500    0.5000    0.6296        34
     I-LIABILITY     0.5000    0.5000    0.5000         6
        I-LOSSES     0.7143    0.6250    0.6667         8
        I-PROFIT     0.8621    0.9615    0.9091        26
       I-REVENUE     0.7600    0.7308    0.7451        26
               O     0.9839    0.9923    0.9880      8660
```