---
layout: model
title: Legal NER for MAPA(Multilingual Anonymisation for Public Administrations)
author: John Snow Labs
name: legner_mapa
date: 2023-04-26
tags: [bg, licensed, ner, legal, mapa]
task: Named Entity Recognition
language: bg
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

This model extracts `ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, and `PERSON` entities from `Bulgarian` documents.

## Predicted Entities

`ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, `PERSON`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_mapa_bg_1.0.0_3.0_1682548782666.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_mapa_bg_1.0.0_3.0_1682548782666.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_base_bg_cased", "bg")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_mapa", "bg", "legal/models")\
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

text = ["""7 В окончателно решение № 1072 на Curtea de Apel București ( Апелативен съд Букурещ, Румъния ), 3-то гражданско отделение за малолетни и непълнолетни лица и семейноправни въпроси, от 12 юни 2013г., което е приложено към акта за преюдициално запитване и представено от г‑н Liberato, се уточнява, че„ [с] ъдът приема, че страните са сключили брак в Италия през октомври 2005 г. и до октомври 2006 г. са живели ту в Румъния, ту в Италия."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))

```

</div>

## Results

```bash
+----------------+---------+
|chunk           |ner_label|
+----------------+---------+
|Букурещ, Румъния|ADDRESS  |
|12 юни 2013г.,  |DATE     |
|г‑н Liberato    |PERSON   |
|Италия          |ADDRESS  |
|октомври 2005 г.|DATE     |
|октомври 2006 г.|DATE     |
|Румъния         |ADDRESS  |
|Италия          |ADDRESS  |
+----------------+---------+
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
|Language:|bg|
|Size:|1.4 MB|

## References

The dataset is available [here](https://huggingface.co/datasets/joelito/mapa).

## Benchmarking

```bash
label	precision	recall	f1-score	support
ADDRESS	0.86	0.75	0.8	8
AMOUNT	1.0	0.64	0.78	11
DATE	0.97	0.97	0.97	65
ORGANISATION	0.81	0.86	0.83	35
PERSON	0.87	0.84	0.85	56
macro-avg	0.9	0.87	0.89	175
macro-avg	0.9	0.81	0.85	175
weighted-avg	0.9	0.87	0.89	175
```