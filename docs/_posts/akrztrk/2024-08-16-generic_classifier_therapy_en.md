---
layout: model
title: Generic Classifier for Therapy
author: John Snow Labs
name: generic_classifier_therapy
date: 2024-08-16
tags: [licensed, en, genericclassifiermodel, classification, therapy, oncology]
task: Text Classification
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: GenericClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a therapy classification model that determines whether clinical sentences include terms related to therapy.
- `True`: Contains therapy related terms.
- `False`: Doesn't contain therapy related terms.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/08.2.Generic_Classifier.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_classifier_therapy_en_5.4.0_3.0_1723792286109.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_classifier_therapy_en_5.4.0_3.0_1723792286109.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("word_embeddings")

sentence_embeddings = SentenceEmbeddings()\
    .setInputCols(["document", "word_embeddings"])\
    .setOutputCol("sentence_embeddings")\
    .setPoolingStrategy("AVERAGE")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("generic_classifier_therapy","en","clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(
  stages=[
    document_assembler,
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier])

data = spark.createDataFrame([
['Patient was briefly started on Arimidex due to significant complaints of hot flashes and joint pain, for which these symptoms increased while on Arimidex.'],
['The patient continues to report pain more at the base of her skull radiating to the top of the head and into the jaws.'],
['Post-Surgical Finding: There are post-surgical findings from a previous lumpectomy with radiation seen in the left breast.'],
['Significant narrowing of the disc with tiny osteophyte and bulging disc producing mild ventral impress and minimal facet degenerative change.']]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
  .setInputCol(Array("text"))
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")
  .setInputCols(Array("document","token"))
  .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings()
  .setInputCols(Array("document", "word_embeddings"))
  .setOutputCol("sentence_embeddings")
  .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
  .setInputCols(Array("sentence_embeddings"))
  .setOutputCol("features")

val generic_classifier = GenericClassifierModel.pretrained("generic_classifier_therapy","en","clinical/models")
  .setInputCols(Array("features"))
  .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  word_embeddings,
  sentence_embeddings,
  features_asm,
  generic_classifier
))


val data = Seq([
["Patient was briefly started on Arimidex due to significant complaints of hot flashes and joint pain, for which these symptoms increased while on Arimidex."],
["The patient continues to report pain more at the base of her skull radiating to the top of the head and into the jaws."],
["Post-Surgical Finding: There are post-surgical findings from a previous lumpectomy with radiation seen in the left breast."],
["Significant narrowing of the disc with tiny osteophyte and bulging disc producing mild ventral impress and minimal facet degenerative change."]]).toDF("text")

val result = clf_Pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|text                                                                                                                                                      |result |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|Patient was briefly started on Arimidex due to significant complaints of hot flashes and joint pain, for which these symptoms increased while on Arimidex.| True  |
|The patient continues to report pain more at the base of her skull radiating to the top of the head and into the jaws.                                    | False |
|Post-Surgical Finding: There are post-surgical findings from a previous lumpectomy with radiation seen in the left breast.                                | True  |
|Significant narrowing of the disc with tiny osteophyte and bulging disc producing mild ventral impress and minimal facet degenerative change.             | False |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_classifier_therapy|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[features]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|1.5 MB|

## Benchmarking
```bash
       label  precision    recall  f1-score   support
       False       0.94      0.92      0.93      3044
        True       0.86      0.90      0.88      1607
    accuracy          -         -      0.92      4651
   macro-avg       0.90      0.91      0.91      4651
weighted-avg       0.92      0.92      0.92      4651
```
