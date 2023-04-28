---
layout: model
title: Legal NER for MAPA(Multilingual Anonymisation for Public Administrations)
author: John Snow Labs
name: legner_mapa
date: 2023-04-28
tags: [ga, licensed, ner, legal, mapa]
task: Named Entity Recognition
language: ga
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

This model extracts `ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, and `PERSON` entities from `Irish` documents.

## Predicted Entities

`ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, `PERSON`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_mapa_ga_1.0.0_3.0_1682670223837.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_mapa_ga_1.0.0_3.0_1682670223837.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.RoBertaEmbeddings.pretrained("roberta_base_czech_legal","gle")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_mapa", "ga", "legal/models")\
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

text = ["""Dhiúltaigh Tribunale di Teramo ( An Chúirt Dúiche, Teramo ) an t-iarratas a rinne Bn.Grigorescu, ar bhonn teagmhasach, chun aitheantas a thabhairt san Iodáil do bhreithiúnas colscartha Tribunalul București ( An Chúirt Réigiúnach, Búcairist ) an 3 Nollaig 2012, de bhun Rialachán Uimh."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+--------------+---------+
|chunk         |ner_label|
+--------------+---------+
|Teramo        |ADDRESS  |
|Bn.Grigorescu |PERSON   |
|Búcairist     |ADDRESS  |
|3 Nollaig 2012|DATE     |
+--------------+---------+
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
|Language:|ga|
|Size:|16.3 MB|

## References

The dataset is available [here](https://huggingface.co/datasets/joelito/mapa).

## Benchmarking

```bash
label         precision  recall  f1-score  support 
ADDRESS       0.82       0.74    0.78      19      
AMOUNT        1.00       1.00    1.00      7       
DATE          0.91       0.92    0.91      75      
ORGANISATION  0.65       0.67    0.66      48      
PERSON        0.71       0.82    0.76      56      
micro-avg     0.79       0.82    0.80      205     
macro-avg     0.82       0.83    0.82      205     
weighted-avg  0.79       0.82    0.80      205
```
