---
layout: model
title: Generic Classifier for Oncology
author: John Snow Labs
name: generic_classifier_oncology
date: 2024-08-13
tags: [licensed, en, genericclassifiermodel, classification, oncology]
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

This model is a oncology classification model that determines whether clinical sentences include terms related to oncology.
- `True`: Contains oncology related terms.
- `False`: Doesn't contain oncology related terms.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_classifier_oncology_en_5.4.0_3.0_1723533974344.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_classifier_oncology_en_5.4.0_3.0_1723533974344.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

generic_classifier = GenericClassifierModel.pretrained("generic_classifier_oncology","en","clinical/models")\
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
["The patient was diagnosed with a malignant tumor, and surgery was promptly scheduled to remove the mass."],
["Following this adjustment, the patient's ECG remained in sinus rhythm, with heart rates varying between 45 and 70 bpm and no significant QTc prolongation."],
["During the treatment review, the oncologist discussed the progression of metastases from the primary lesion to nearby lymph nodes."],
["Functional MRI (fMRI) showed increased activation in the motor cortex during the finger-tapping task."]
]).toDF("text")

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

val generic_classifier = GenericClassifierModel.pretrained("generic_classifier_oncology","en","clinical/models")
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
["The patient was diagnosed with a malignant tumor, and surgery was promptly scheduled to remove the mass."],
["Following this adjustment, the patient's ECG remained in sinus rhythm, with heart rates varying between 45 and 70 bpm and no significant QTc prolongation."],
["During the treatment review, the oncologist discussed the progression of metastases from the primary lesion to nearby lymph nodes."],
["Functional MRI (fMRI) showed increased activation in the motor cortex during the finger-tapping task."]
]).toDF("text")

val result = clf_Pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|text                                                                                                                                                      |result |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
|The patient was diagnosed with a malignant tumor, and surgery was promptly scheduled to remove the mass.                                                  | True  |
|Following this adjustment, the patient's ECG remained in sinus rhythm, with heart rates varying between 45 and 70 bpm and no significant QTc prolongation.| False |
|During the treatment review, the oncologist discussed the progression of metastases from the primary lesion to nearby lymph nodes.                        | True  |
|Functional MRI (fMRI) showed increased activation in the motor cortex during the finger-tapping task.                                                     | False |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_classifier_oncology|
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
       False       0.90      0.86      0.88      2093
        True       0.89      0.93      0.91      2714
    accuracy          -         -      0.90      4807
   macro-avg       0.90      0.89      0.89      4807
weighted-avg       0.90      0.90      0.90      4807
```
