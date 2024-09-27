---
layout: model
title: Generic Classifier for for Metastasis (SVM)
author: John Snow Labs
name: generic_svm_classifier_metastasis
date: 2024-08-09
tags: [licensed, en, generic_svm_classifier, svm, metastasis, classification, oncology]
task: Text Classification
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: GenericSVMClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained with the Generic Classifier annotator and the Support Vector Machine (SVM) algorithm and classifies text/sentence into two categories.
- `True`: Contains metastasis related terms.
- `False`: Doesn't contain metastasis related terms.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_svm_classifier_metastasis_en_5.4.0_3.0_1723203897310.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_svm_classifier_metastasis_en_5.4.0_3.0_1723203897310.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

generic_classifier = GenericSVMClassifierModel.pretrained("generic_svm_classifier_metastasis","en","clinical/models")\
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

data = spark.createDataFrame([['A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.'],
 ['The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci.'],
 ['After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.'],
 ['The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.']]).toDF("text")

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

val generic_classifier = GenericSVMClassifierModel.pretrained("generic_svm_classifier_metastasis","en","clinical/models")
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


val data = Seq([['A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.'],
 ['The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci.'],
 ['After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.'],
 ['The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.']]).toDF("text")

val result = clf_Pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|text                                                                                                                                                                                                                 |result |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.                                                                                                                          | False |
|The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci.| True  |
|After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.                                                                                       | False |
|The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.                                                                                                                       | True  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_svm_classifier_metastasis|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[feature_vector]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|14.0 KB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       False       0.96      0.99      0.97      4365
        True       0.94      0.84      0.89      1094
    accuracy          -         -      0.96      5459
   macro-avg       0.95      0.91      0.93      5459
weighted-avg       0.96      0.96      0.96      5459
```
