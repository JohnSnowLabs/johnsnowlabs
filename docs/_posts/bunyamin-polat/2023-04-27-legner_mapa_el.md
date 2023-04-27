---
layout: model
title: Legal NER for MAPA(Multilingual Anonymisation for Public Administrations)
author: John Snow Labs
name: legner_mapa
date: 2023-04-27
tags: [el, ner, legal, mapa, licensed]
task: Named Entity Recognition
language: el
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

This model extracts `ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, and `PERSON` entities from `Greek` documents.

## Predicted Entities

`ADDRESS`, `AMOUNT`, `DATE`, `ORGANISATION`, `PERSON`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legner_mapa_el_1.0.0_3.0_1682590655353.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legner_mapa_el_1.0.0_3.0_1682590655353.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embeddings = nlp.BertEmbeddings.pretrained("bert_embeddings_base_el_cased", "el")\
        .setInputCols(["sentence", "token"])\
        .setOutputCol("embeddings")\
        .setMaxSentenceLength(512)\
        .setCaseSensitive(True)

ner_model = legal.NerModel.pretrained("legner_mapa", "el", "legal/models")\
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

text = ["""86 Στην υπόθεση της κύριας δίκης, προκύπτει ότι ορισμένοι εργαζόμενοι της Martin‑Meat αποσπάσθηκαν στην Αυστρία κατά την περίοδο μεταξύ του έτους 2007 και του έτους 2012, για την εκτέλεση εργασιών τεμαχισμού κρέατος σε εγκαταστάσεις της Alpenrind."""]

result = model.transform(spark.createDataFrame([text]).toDF("text"))
```

</div>

## Results

```bash
+-----------+------------+
|chunk      |ner_label   |
+-----------+------------+
|Martin‑Meat|ORGANISATION|
|Αυστρία    |ADDRESS     |
|2007       |DATE        |
|2012       |DATE        |
|Alpenrind  |ORGANISATION|
+-----------+------------+
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
|Language:|el|
|Size:|16.4 MB|

## References

The dataset is available [here](https://huggingface.co/datasets/joelito/mapa).

## Benchmarking

```bash
label         precision  recall  f1-score  support 
ADDRESS       0.89       1.0     0.94      16      
AMOUNT        0.82       0.75    0.78      12      
DATE          0.98       0.98    0.98      65      
ORGANISATION  0.85       0.85    0.85      40      
PERSON        0.9        0.95    0.92      38      
macro-avg     0.91       0.93    0.92      171     
macro-avg     0.89       0.91    0.9       171     
weighted-avg  0.91       0.93    0.92      171     
```