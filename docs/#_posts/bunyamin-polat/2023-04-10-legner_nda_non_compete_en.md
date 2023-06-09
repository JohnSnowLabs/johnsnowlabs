---
layout: model
title: Legal NER for NDA (Non-compete Clause)
author: John Snow Labs
name: legner_nda_non_compete
date: 2023-04-10
tags: [en, legal, licensed, ner, nda, non_compete]
task: Named Entity Recognition
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: FinanceNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a NER model, aimed to be run **only** after detecting the `NON_COMP` clause with a proper classifier (use `legmulticlf_mnda_sections_paragraph_other` model for that purpose). It will extract the following entities: `NON_COMPETE_COUNTRY`, and `NON_COMPETE_TERM`.

## Predicted Entities

`NON_COMPETE_COUNTRY`, `NON_COMPETE_TERM`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_nda_non_compete_en_1.0.0_3.0_1681096039352.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_nda_non_compete_en_1.0.0_3.0_1681096039352.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = legal.NerModel.pretrained("legner_nda_non_compete", "en", "legal/models")\
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

text = ["""The employee shall not engage in any business activities that compete with the company in France for a period of two years after leaving the company."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+---------+-------------------+
|chunk    |ner_label          |
+---------+-------------------+
|France   |NON_COMPETE_COUNTRY|
|two years|NON_COMPETE_TERM   |
+---------+-------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_nda_non_compete|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|16.2 MB|

## References

In-house annotations on the Non-disclosure Agreements

## Benchmarking

```bash
label                precision  recall  f1-score  support 
NON_COMPETE_COUNTRY  1.00       1.00    1.00      8       
NON_COMPETE_TERM     1.00       1.00    1.00      15      
micro-avg            1.00       1.00    1.00      23      
macro-avg            1.00       1.00    1.00      23      
weighted-avg         1.00       1.00    1.00      23 
```