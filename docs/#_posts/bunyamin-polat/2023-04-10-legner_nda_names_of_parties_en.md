---
layout: model
title: Legal NER for NDA (Names of the Parties Clauses)
author: John Snow Labs
name: legner_nda_names_of_parties
date: 2023-04-10
tags: [en, legal, licensed, ner, nda, names_of_parties]
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

This is a NER model, aimed to be run **only** after detecting the `NAMES_OF_PARTIES` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `ALIAS`, `EFFDATE_NUMERIC`, `LOCATION`, and `PARTY`.

## Predicted Entities

`ALIAS`, `EFFDATE_NUMERIC`, `LOCATION`, `PARTY`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_names_of_parties_en_1.0.0_3.0_1681153822264.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_names_of_parties_en_1.0.0_3.0_1681153822264.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_names_of_parties", "en", "legal/models")\
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
        ner_converter
])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = nlpPipeline.fit(empty_data)

text = ["""This Confidentiality Agreement (this "Agreement") is dated effective as of the 4th day of June 2001, between Amerada Hess Corporation, a Delaware corporation ("AHC"), and Triton Energy Limited, a Cayman Islands company (the "Company")."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+------------------------+---------------+
|chunk                   |ner_label      |
+------------------------+---------------+
|4th day of June 2001    |EFFDATE_NUMERIC|
|Amerada Hess Corporation|PARTY          |
|Delaware                |LOCATION       |
|AHC                     |ALIAS          |
|Triton Energy Limited   |PARTY          |
|Cayman Islands          |LOCATION       |
|Company                 |ALIAS          |
+------------------------+---------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_names_of_parties|
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
label            precision  recall  f1-score  support 
ALIAS            0.92       0.96    0.94      25      
EFFDATE_NUMERIC  0.90       0.96    0.93      27      
LOCATION         1.00       0.93    0.96      14      
PARTY            0.77       0.88    0.82      26      
micro-avg        0.88       0.93    0.91      92      
macro-avg        0.90       0.93    0.91      92      
weighted-avg     0.88       0.93    0.91      92 
```
