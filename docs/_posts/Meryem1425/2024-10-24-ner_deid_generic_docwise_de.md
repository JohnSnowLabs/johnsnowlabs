---
layout: model
title: Detect PHI for Deidentification (Generic - Docwise)
author: John Snow Labs
name: ner_deid_generic_docwise
date: 2024-10-24
tags: [deid, ner, de, licensed, clinical]
task: De-identification
language: de
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Named Entity Recognition (NER) model works at the document level, allowing it to identify and annotate entities throughout the entire document. It leverages a deep learning architecture (Char CNNs - BiLSTM - CRF - word embeddings) inspired by the former state-of-the-art model for NER developed by Chiu & Nichols: “Named Entity Recognition with Bidirectional LSTM-CNN”. Deidentification NER is a Named Entity Recognition model that annotates German text to find protected health information (PHI) that may need to be deidentified. It was trained with in-house annotations and detects 7 entities.

## Predicted Entities

`DATE`, `NAME`, `LOCATION`, `PROFESSION`, `AGE`, `ID`, `CONTACT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_DEID_DE/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/04.1.Clinical_Multi_Language_Deidentification.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_docwise_de_5.5.0_3.0_1729796973620.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_deid_generic_docwise_de_5.5.0_3.0_1729796973620.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","de","clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("embeddings")

deid_ner = MedicalNerModel.pretrained("ner_deid_generic_docwise", "de", "clinical/models")\
    .setInputCols(["document", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_deid_generic_chunk")

nlpPipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer, 
    word_embeddings, 
    deid_ner, 
    ner_converter])

data = spark.createDataFrame([["""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhaus
in Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen."""]]).toDF("text")

result = nlpPipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d", "de", "clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val deid_ner = MedicalNerModel.pretrained("ner_deid_generic_docwise", "de", "clinical/models") 
    .setInputCols(Array("document", "token", "embeddings")) 
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner"))
    .setOutputCol("ner_deid_generic_chunk")

val nlpPipeline = new Pipeline().setStages(Array(
    document_assembler,
    tokenizer,
    word_embeddings, 
    deid_ner, 
    ner_converter))

val data = Seq("""Michael Berger wird am Morgen des 12 Dezember 2018 ins St. Elisabeth-Krankenhausin Bad Kissingen eingeliefert. Herr Berger ist 76 Jahre alt und hat zu viel Wasser in den Beinen.""").toDS.toDF("text")

val result = nlpPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-------------------------+-----+---+---------+
|chunk                    |begin|end|ner_label|
+-------------------------+-----+---+---------+
|Michael Berger           |0    |13 |NAME     |
|12 Dezember 2018         |34   |49 |DATE     |
|St. Elisabeth-Krankenhaus|55   |79 |LOCATION |
|Bad Kissingen            |84   |96 |LOCATION |
|Herr Berger              |112  |122|NAME     |
|76                       |128  |129|AGE      |
+-------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_deid_generic_docwise|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|de|
|Size:|3.0 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
         AGE       0.98      0.92      0.95       828
     CONTACT       0.73      0.88      0.80       147
        DATE       1.00      1.00      1.00      7044
          ID       0.93      0.95      0.94       387
    LOCATION       0.91      0.86      0.88     10593
        NAME       0.90      0.94      0.92      7404
  PROFESSION       0.91      0.65      0.76       459
   micro-avg       0.93      0.92      0.93     26862
   macro-avg       0.91      0.89      0.89     26862
weighted-avg       0.93      0.92      0.92     26862
```
