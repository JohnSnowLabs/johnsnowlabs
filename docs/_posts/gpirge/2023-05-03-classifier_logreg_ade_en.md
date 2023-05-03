---
layout: model
title: Adverse Drug Events Classifier (LogReg)
author: John Snow Labs
name: classifier_logreg_ade
date: 2023-05-03
tags: [clinical, licensed, en, text_classification, logreg]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.1
spark_version: 3.2
supported: true
annotator: DocumentLogRegClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model classifies text/sentence in two categories:

True : The sentence is talking about a possible ADE.

False : The sentence doesn’t have any information about an ADE.

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/classifier_logreg_ade_en_4.4.1_3.2_1683153314225.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/classifier_logreg_ade_en_4.4.1_3.2_1683153314225.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

normalizer = Normalizer()\
    .setInputCols("token")\
    .setOutputCol("normalized")

stopwords_cleaner = StopWordsCleaner()\
    .setInputCols("normalized")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)

stemmer = Stemmer()\
    .setInputCols("cleanTokens")\
    .setOutputCol("stem")

logreg = DocumentLogRegClassifierModel.pretrained("classifier_logreg_ade", "en", "clinical/models")\
    .setInputCols("stem")\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    normalizer,
    stopwords_cleaner, 
    stemmer, 
    logreg])

data = spark.createDataFrame([["""I feel great after taking tylenol."""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler =new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val normalizer = new Normalizer()
    .setInputCols("token")
    .setOutputCol("normalized")

val stopwords_cleaner = new StopWordsCleaner()
    .setInputCols("normalized")
    .setOutputCol("cleanTokens")
    .setCaseSensitive(False)

val stemmer = new Stemmer()
    .setInputCols("cleanTokens")
    .setOutputCol("stem")

val logreg = new DocumentLogRegClassifierModel.pretrained("classifier_logreg_ade", "en", "clinical/models")
    .setInputCols("stem")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, normalizer, stopwords_cleaner, stemmer, logreg))

val data = Seq(Array("""I feel great after taking tylenol""")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+---------------------------------+-------+
|text                             |result |
+---------------------------------+-------+
|I feel great after taking tylenol|[False]|
+---------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|classifier_logreg_ade|
|Compatibility:|Healthcare NLP 4.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[stem]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|402.9 KB|

## References

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

Reference: Gurulingappa et al., Benchmark Corpus to Support Information Extraction for Adverse Drug Effects, JBI, 2012. http://www.sciencedirect.com/science/article/pii/S1532046412000615

## Benchmarking

```bash
              precision    recall  f1-score   support

       False       0.92      0.90      0.91      3362
        True       0.77      0.82      0.79      1361

    accuracy                           0.88      4723
   macro avg       0.85      0.86      0.85      4723
weighted avg       0.88      0.88      0.88      4723
```