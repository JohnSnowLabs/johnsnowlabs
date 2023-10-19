---
layout: model
title: Detect Problems, Tests, and Treatments (Bulgarian)
author: John Snow Labs
name: ner_clinical
date: 2023-10-13
tags: [licensed, ner, bg, clinical]
task: Named Entity Recognition
language: bg
edition: Healthcare NLP 5.1.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Bulgarian. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state-of-the-art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/NER_CLINICAL_MULTI/){:.button.button-orange}
[Open in Colab](https://github.com/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/streamlit_notebooks/healthcare/NER_CLINICAL_MULTI.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_bg_5.1.1_3.0_1697219921664.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_bg_5.1.1_3.0_1697219921664.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\ 
    .setInputCol("text")\ 
    .setOutputCol("document")

tokenizer = Tokenizer()
    .setInputCols(["document"])
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","bg")
    .setInputCols(["document", "token"])
    .setOutputCol("embeddings")

ner_model = MedicalNerModel().pretrained("ner_clinical", "bg", "clinical/models")
    .setInputCols(["document", "token", "embeddings"])
    .setOutputCol("ner")

ner_converter = NerConverterInternal()
    .setInputCols(["document","token","ner"])
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[ documentAssembler, tokenizer, embeddings, ner_model, ner_converter])

sample_text = """Пациентът беше изключен от възможността за миокарден инфаркт, като се има предвид падането му в летището и бигеминията, забелязана по електрокардиограмата, която се разви по време на съзнателна седация по време на намаляването на фрактурата."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","bg")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "bg", "clinical/models")
    .setInputCols(Array("document", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("document", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ))

val sample_data = Seq("""Пациентът беше изключен от възможността за миокарден инфаркт, като се има предвид падането му в летището и бигеминията, забелязана по електрокардиограмата, която се разви по време на съзнателна седация по време на намаляването на фрактурата.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+--------------------------+-----+---+---------+
|chunk                     |begin|end|ner_label|
+--------------------------+-----+---+---------+
|миокарден инфаркт         |44   |60 |PROBLEM  |
|падането му               |83   |93 |PROBLEM  |
|бигеминията               |108  |118|PROBLEM  |
|електрокардиограмата      |135  |154|TEST     |
|съзнателна седация        |184  |201|TREATMENT|
|намаляването на фрактурата|215  |240|TREATMENT|
+--------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token, embeddings]|
|Output Labels:|[ner]|
|Language:|bg|
|Size:|920.1 KB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
     PROBLEM       0.70      0.70      0.70       216
        TEST       0.81      0.81      0.81       176
   TREATMENT       0.68      0.60      0.64       161
   micro-avg       0.73      0.71      0.72       553
   macro-avg       0.73      0.71      0.72       553
weighted-avg       0.73      0.71      0.72       553
```