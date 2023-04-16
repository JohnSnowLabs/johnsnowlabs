---
layout: model
title: Legal NER for NDA (Remedies Clauses)
author: John Snow Labs
name: legner_nda_remedies
date: 2023-04-16
tags: [en, licensed, ner, legal, nda, remedies]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a NER model, aimed to be run **only** after detecting the `REMEDIES` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` for that purpose). It will extract the following entities: `CURRENCY`, `NUMERIC_REMEDY`, and `REMEDY_TYPE`.

## Predicted Entities

`CURRENCY`, `NUMERIC_REMEDY`, `REMEDY_TYPE`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_remedies_en_1.0.0_3.0_1681687124993.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_remedies_en_1.0.0_3.0_1681687124993.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")
        
sentence_detector = nlp.SentenceDetector()\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_embeddings_legal_roberta_base","en") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_nda_remedies", "en", "legal/models")\
        .setInputCols(["sentence", "token", "embeddings"])\
        .setOutputCol("ner")

ner_converter = nlp.NerConverter()\
        .setInputCols(["sentence", "token", "ner"])\
        .setOutputCol("ner_chunk")

nlpPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        embeddings,
        ner_model,
        ner_converter])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ["""The breaching party shall pay the non-breaching party liquidated damages of $ 1,000 per day for each day that the breach of this NDA continues."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+------------------+--------------+
|chunk             |ner_label     |
+------------------+--------------+
|liquidated damages|REMEDY_TYPE   |
|$                 |CURRENCY      |
|1,000             |NUMERIC_REMEDY|
+------------------+--------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_remedies|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.3 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label           precision  recall  f1-score  support 
CURRENCY        1.00       1.00    1.00      11      
NUMERIC_REMEDY  1.00       1.00    1.00      11      
REMEDY_TYPE     0.86       0.94    0.90      32      
micro-avg       0.91       0.96    0.94      54      
macro-avg       0.95       0.98    0.97      54      
weighted-avg    0.92       0.96    0.94      54 
```