---
layout: model
title: Legal NER for MAPA(Multilingual Anonymisation for Public Administrations)
author: John Snow Labs
name: legner_mapa
date: 2023-04-27
tags: [pt, licensed, ner, legal, mapa]
task: Named Entity Recognition
language: pt
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

This model extracts `ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, and `PERSON` entities from `Portuguese` documents.

## Predicted Entities

`ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, `PERSON`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_mapa_pt_1.0.0_3.0_1682608680085.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_mapa_pt_1.0.0_3.0_1682608680085.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_base_pt_cased", "pt")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_mapa", "pt", "legal/models")\
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

text = ["""Nos termos dos Decretos da Garda Síochána (6), só pode ser admitido como estagiário para integrar a força policial nacional quem tiver pelo menos 18 anos, mas menos de 35 anos de idade, no primeiro dia do mês em que tenha sido publicado pela primeira vez, num jornal nacional, o anúncio da vaga a que o recrutamento respeita."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-----------------------+------------+
|chunk                  |ner_label   |
+-----------------------+------------+
|Garda Síochána         |ORGANISATION|
|força policial nacional|ORGANISATION|
|18 anos                |AMOUNT      |
|35 anos                |AMOUNT      |
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
|Language:|pt|
|Size:|1.4 MB|

## References

The dataset is available [here](https://huggingface.co/datasets/joelito/mapa).

## Benchmarking

```bash
label         precision  recall  f1-score  support 
ADDRESS       0.91       0.91    0.91      23      
AMOUNT        1.00       0.83    0.91      6       
DATE          1.00       0.95    0.97      61      
ORGANISATION  0.85       0.77    0.81      30      
PERSON        0.88       0.91    0.89      65      
macro-avg     0.92       0.90    0.91      185     
macro-avg     0.93       0.87    0.90      185     
weighted-avg  0.92       0.90    0.91      185               
```
