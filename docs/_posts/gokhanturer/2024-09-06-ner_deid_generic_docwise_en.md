---
layout: model
title: Detect PHI for Deidentification (Generic - Docwise)
author: John Snow Labs
name: ner_deid_generic_docwise
date: 2024-09-06
tags: [en, clinical, licensed, ner, deid]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Named Entity Recognition (NER) annotator works at the document level, allowing it to identify and annotate entities throughout an entire document. It leverages a deep learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired by the former state-of-the-art model for NER developed by Chiu & Nichols: "Named Entity Recognition with Bidirectional LSTM-CNN". This NER model is particularly useful for detecting protected health information (PHI) that may need to be de-identified. It can recognize and annotate 7 specific entities: `DATE`, `NAME`, `LOCATION`, `PROFESSION`, `CONTACT`, `AGE`, and `ID`.

## Predicted Entities

`DATE`, `NAME`, `LOCATION`, `PROFESSION`, `CONTACT`, `AGE`, `ID`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_docwise_en_5.4.1_3.0_1725651582098.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_docwise_en_5.4.1_3.0_1725651582098.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
documentAssembler = DocumentAssembler()\
      .setInputCol("text")\
      .setOutputCol("document")

tokenizer = Tokenizer()\
      .setInputCols(["document"])\
      .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
      .setInputCols(["document", "token"])\
      .setOutputCol("embeddings")

ner_deid_generic = MedicalNerModel.pretrained("ner_deid_generic_docwise", "en", "clinical/models")  \
      .setInputCols(["document", "token", "embeddings"]) \
      .setOutputCol("ner_deid_generic_docwise")

ner_deid_generic_converter = NerConverterInternal()\
      .setInputCols(["document", "token", "ner_deid_generic_docwise"])\
      .setOutputCol("ner_chunk_generic_docwise")

nlpPipeline = Pipeline(stages=[
      documentAssembler,
      tokenizer,
      word_embeddings,
      ner_deid_generic,
      ner_deid_generic_converter,
      ])

text = '''Dr. John Taylor, ID 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old male patient.'''

deid_model = nlpPipeline.fit(empty_data)

result = deid_model.transform(spark.createDataFrame([[text]]).toDF("text"))
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val nerDeidGeneric = MedicalNerModel.pretrained("ner_deid_generic_docwise", "en", "clinical/models")
    .setInputCols(Array("document", "token", "embeddings"))
    .setOutputCol("ner_deid_generic_docwise")

val nerDeidGenericConverter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner_deid_generic_docwise"))
    .setOutputCol("ner_chunk_generic_docwise")

val nlpPipeline = new Pipeline().setStages(Array(
    documentAssembler,
    tokenizer,
    wordEmbeddings,
    nerDeidGeneric,
    nerDeidGenericConverter
))

val text = Seq("""Dr. John Taylor, ID 982345, a cardiologist at St. Mary's Hospital in Boston, was contacted on 05/10/2023 regarding a 45-year-old male patient.""").toDF("text")

val model = nlpPipeline.fit(spark.emptyDataFrame)
val result = model.transform(text)
```
</div>

## Results

```bash
+-------------------+-----+---+----------+
|chunk              |begin|end|ner_label |
+-------------------+-----+---+----------+
|John Taylor        |5    |15 |NAME      |
|982345             |21   |26 |CONTACT   |
|cardiologist       |31   |42 |PROFESSION|
|St. Mary's Hospital|47   |65 |LOCATION  |
|Boston             |70   |75 |LOCATION  |
|05/10/2023         |95   |104|DATE      |
|45-year-old        |118  |128|AGE       |
+-------------------+-----+---+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_docwise|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|9.3 MB|

## Benchmarking

```bash
     label     tp     fp     fn   total  precision  recall      f1
   CONTACT  254.0    7.0   13.0   267.0     0.9732  0.9513  0.9621
      NAME 3616.0   92.0  200.0  3816.0     0.9752  0.9476  0.9612
      DATE 3844.0   55.0   93.0  3937.0     0.9859  0.9764  0.9811
        ID  521.0   67.0  328.0   849.0     0.8861  0.6137  0.7251
  LOCATION 1918.0  126.0  224.0  2142.0     0.9384  0.8954  0.9164
PROFESSION  272.0   21.0  241.0   513.0     0.9283  0.5302  0.6749
       AGE  470.0   25.0   29.0   499.0     0.9495  0.9419  0.9457
     MACRO    -       -     -       -        -        -     0.8809
     MICRO    -       -     -       -        -        -     0.9302
```
