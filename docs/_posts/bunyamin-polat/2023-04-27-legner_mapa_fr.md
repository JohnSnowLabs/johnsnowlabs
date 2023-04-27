---
layout: model
title: Legal NER for MAPA(Multilingual Anonymisation for Public Administrations)
author: John Snow Labs
name: legner_mapa
date: 2023-04-27
tags: [fr, ner, licensed, legal, mapa]
task: Named Entity Recognition
language: fr
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
annotator: LegalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The dataset consists of 12 documents taken from EUR-Lex, a multilingual corpus of court decisions and legal dispositions in the 24 official languages of the European Union.

This model extracts `ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, and `PERSON` entities from `French` documents.

## Predicted Entities

`ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, `PERSON`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_mapa_fr_1.0.0_3.0_1682596162755.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_mapa_fr_1.0.0_3.0_1682596162755.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = nlp.DocumentAssembler()\
        .setInputCol("text")\
        .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")\
        .setInputCols(["document"])\
        .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
        .setInputCols(["sentence"])\
        .setOutputCol("token")

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_base_fr_cased", "fr")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_mapa", "fr", "legal/models")\
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

text = ["""Heeren, administrateur, vu la phase écrite de la procédure et à la suite de l’audience du 28 novembre 2017, rend le présent Arrêt Antécédents du litige 1 La requérante, Foshan Lihua Ceramic Co."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-----------------------+------------+
|chunk                  |ner_label   |
+-----------------------+------------+
|Heeren                 |PERSON      |
|28 novembre 2017       |DATE        |
|Foshan Lihua Ceramic Co|ORGANISATION|
+-----------------------+------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legner_mapa|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|fr|
|Size:|1.4 MB|

## References

The dataset is available [here](https://huggingface.co/datasets/joelito/mapa).

## Benchmarking

```bash
label         precision  recall  f1-score  support 
ADDRESS       1.00       1.00    1.00      11      
AMOUNT        1.00       1.00    1.00      4       
DATE          1.00       0.96    0.98      28      
ORGANISATION  1.00       0.95    0.98      22      
PERSON        0.94       0.94    0.94      31      
macro-avg     0.98       0.96    0.97      96      
macro-avg     0.99       0.97    0.98      96      
weighted-avg  0.98       0.96    0.97      96  
```