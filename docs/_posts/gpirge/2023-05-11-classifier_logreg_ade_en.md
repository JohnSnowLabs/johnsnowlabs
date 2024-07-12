---
layout: model
title: Adverse Drug Events Classifier (LogReg)
author: John Snow Labs
name: classifier_logreg_ade
date: 2023-05-11
tags: [text_classification, ade, clinical, licensed, logreg, en]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.1
spark_version: 3.0
supported: true
annotator: DocumentLogRegClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained with the Logistic Regression algorithm and classifies text/sentence into two categories:

True : The sentence is talking about a possible ADE

False : The sentence doesn’t have any information about an ADE.

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/classifier_logreg_ade_en_4.4.1_3.0_1683817451286.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/classifier_logreg_ade_en_4.4.1_3.0_1683817451286.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

logreg = DocumentLogRegClassifierModel.pretrained("classifier_logreg_ade", "en", "clinical/models")\
    .setInputCols("token")\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    logreg])

data = spark.createDataFrame([["""None of the patients required treatment for the overdose."""], ["""Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient."""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler =new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val logreg = new DocumentLogRegClassifierModel.pretrained("classifier_logreg_ade", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, logreg))

val data = Seq(Array("None of the patients required treatment for the overdose.", "Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------+-------+
|text                                                                                    |result |
+----------------------------------------------------------------------------------------+-------+
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[True] |
|None of the patients required treatment for the overdose.                               |[False]|
+----------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|classifier_logreg_ade|
|Compatibility:|Healthcare NLP 4.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|595.7 KB|

## References

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

Reference: Gurulingappa et al., Benchmark Corpus to Support Information Extraction for Adverse Drug Effects, JBI, 2012. [https://www.sciencedirect.com/science/article/pii/S1532046412000615](https://www.sciencedirect.com/science/article/pii/S1532046412000615)

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       False       0.91      0.92      0.92      3362
        True       0.79      0.79      0.79      1361
    accuracy       -         -         0.88      4723
   macro_avg       0.85      0.85      0.85      4723
weighted_avg       0.88      0.88      0.88      4723
```