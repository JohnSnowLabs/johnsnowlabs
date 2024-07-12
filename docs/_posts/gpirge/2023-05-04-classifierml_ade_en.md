---
layout: model
title: Adverse Drug Events Classifier
author: John Snow Labs
name: classifierml_ade
date: 2023-05-04
tags: [ade, clinical, licensed, en, text_classification]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.1
spark_version: 3.0
supported: true
annotator: DocumentMLClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained with the `DocumentMLClassifierApproach` annotator and classifies a text/sentence into two categories:

True : The sentence is talking about a possible ADE

False : The sentence doesn’t have any information about an ADE.

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/classifierml_ade_en_4.4.1_3.0_1683229229936.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/classifierml_ade_en_4.4.1_3.0_1683229229936.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

classifier_ml = DocumentMLClassifierModel.pretrained("classifierml_ade", "en", "clinical/models")\
    .setInputCols("token")\
    .setOutputCol("prediction")

clf_Pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    classifier_ml])

data = spark.createDataFrame([["""I feel great after taking tylenol."""], ["""Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient."""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler =new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val classifier_ml = new DocumentMLClassifierModel.pretrained("classifierml_ade", "en", "clinical/models")
    .setInputCols("token")
    .setOutputCol("prediction")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, classifier_ml))

val data = Seq(Array("I feel great after taking tylenol", "Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------+-------+
|text                                                                                    |result |
+----------------------------------------------------------------------------------------+-------+
|I feel great after taking tylenol                                                       |[False]|
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[True] |
+----------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|classifierml_ade|
|Compatibility:|Healthcare NLP 4.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|2.7 MB|

## References

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

Reference: Gurulingappa et al., Benchmark Corpus to Support Information Extraction for Adverse Drug Effects, JBI, 2012. [https://www.sciencedirect.com/science/article/pii/S1532046412000615](https://www.sciencedirect.com/science/article/pii/S1532046412000615)

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       False       0.90      0.94      0.92      3359
        True       0.85      0.75      0.79      1364
    accuracy       -         -         0.89      4723
   macro avg       0.87      0.85      0.86      4723
weighted avg       0.89      0.89      0.89      4723
```
