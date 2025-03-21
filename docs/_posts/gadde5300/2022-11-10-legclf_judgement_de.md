---
layout: model
title: German Legal Judgement Classifier (Small)
author: John Snow Labs
name: legclf_judgement
date: 2022-11-10
tags: [de, legal, licensed, classification, judgement, german]
task: Text Classification
language: de
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalClassifierDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a `sm` version of German Legal Judgement Text Classifier written in German legal writing style "Urteilsstil" (judgement style), which will retrieve if a text is either conclusion, definition, other or subsumption .

## Predicted Entities

`conclusion`, `definition`, `subsumption`, `other`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legclf_judgement_de_1.0.0_3.0_1668064625045.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legclf_judgement_de_1.0.0_3.0_1668064625045.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
 
document_assembler = nlp.DocumentAssembler() \
                .setInputCol("text") \
                .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
                .setInputCols(["document"]) \
                .setOutputCol("token")
      
embeddings = nlp.BertEmbeddings.pretrained("bert_sentence_embeddings_financial","de") \
                .setInputCols(["document", "token"]) \
                .setOutputCol("embeddings")

sembeddings = nlp.SentenceEmbeddings()\
    .setInputCols(["document", "embeddings"]) \
    .setOutputCol("sentence_embeddings") \
    .setPoolingStrategy("AVERAGE")

classifierdl = legal.ClassifierDLModel.pretrained("legclf_judgement", "de", "legal/models")\
                .setInputCols(["sentence_embeddings"])\
                .setOutputCol("label")

bert_clf_pipeline = nlp.Pipeline(stages=[document_assembler,
                                     tokenizer,
                                     embeddings,
                                     sembeddings,
                                     classifierdl])

text = ["Insoweit ergibt sich tatsächlich im Ergebnis ein Verzicht der Arbeitnehmer in Höhe der RoSi-Zulage ."]
empty_df = spark.createDataFrame([[""]]).toDF("text")
model = bert_clf_pipeline.fit(empty_df)
res = model.transform(spark.createDataFrame([text]).toDF("text"))

```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+-------------+
|text                                                                                                |result       |
+----------------------------------------------------------------------------------------------------+-------------+
|Insoweit ergibt sich tatsächlich im Ergebnis ein Verzicht der Arbeitnehmer in Höhe der RoSi-Zulage .|[subsumption]|
+----------------------------------------------------------------------------------------------------+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legclf_judgement|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[label]|
|Language:|de|
|Size:|23.8 MB|

## References

An in-house augmented version of [this dataset](https://zenodo.org/record/3936490#.Y2ybxctBxD-)

## Benchmarking

```bash
       label  precision    recall  f1-score   support
  conclusion       0.47      0.69      0.55       156
  definition       0.72      0.90      0.80       286
       other       0.95      0.70      0.81       786
 subsumption       0.70      0.77      0.73       523
    accuracy          -         -      0.75      1751
   macro-avg       0.71      0.77      0.72      1751
weighted-avg       0.79      0.75      0.76      1751
```
