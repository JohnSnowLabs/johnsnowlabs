---
layout: model
title: Generic Classifier for Adverse Drug Events
author: John Snow Labs
name: generic_logreg_classifier_ade
date: 2023-05-09
tags: [generic_classifier, logreg, clinical, licensed, en, text_classification, ade]
task: Text Classification
language: en
edition: Healthcare NLP 4.4.1
spark_version: 3.0
supported: true
annotator: GenericLogRegClassifierModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained with the Generic Classifier annotator and the Logistic Regression algorithm and classifies text/sentence into two categories:

True : The sentence is talking about a possible ADE

False : The sentence doesn’t have any information about an ADE.

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/generic_logreg_classifier_ade_en_4.4.1_3.0_1683641152188.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/generic_logreg_classifier_ade_en_4.4.1_3.0_1683641152188.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sentence_embeddings = SentenceEmbeddings() \
        .setInputCols(["document", "word_embeddings"]) \
        .setOutputCol("sentence_embeddings") \
        .setPoolingStrategy("AVERAGE")

features_asm = FeaturesAssembler()\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("features")

generic_classifier = GenericClassifierModel.pretrained("generic_logreg_classifier_ade", "en", "clinical/models")\
    .setInputCols(["features"])\
    .setOutputCol("class")

clf_Pipeline = Pipeline(stages=[
    document_assembler, 
    tokenizer,
    word_embeddings,
    sentence_embeddings,
    features_asm,
    generic_classifier])

data = spark.createDataFrame([["""None of the patients required treatment for the overdose."""], ["""Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient."""]]).toDF("text")

result = clf_Pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val word_embeddings = new WordEmbeddingsModel().pretrained("embeddings_clinical","en","clinical/models")
    .setInputCols(Array("document", "token"))
    .setOutputCol("word_embeddings")

val sentence_embeddings = new SentenceEmbeddings()
    .setInputCols(Array("document", "word_embeddings"))
    .setOutputCol("sentence_embeddings") 
    .setPoolingStrategy("AVERAGE")

val features_asm = new FeaturesAssembler()
    .setInputCols("sentence_embeddings")
    .setOutputCol("features")

val generic_classifier = new GenericClassifierModel.pretrained("generic_logreg_classifier_ade", "en", "clinical/models")
    .setInputCols("features")
    .setOutputCol("class")

val clf_Pipeline = new Pipeline().setStages(Array(document_assembler, tokenizer, word_embeddings, sentence_embeddings, features_asm, generic_classifier))

val data = Seq(Array("None of the patients required treatment for the overdose.", "Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.")).toDS().toDF("text")

val result = clf_Pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------------------------------------------+-------+
|text                                                                                    |result |
+----------------------------------------------------------------------------------------+-------+
|None of the patients required treatment for the overdose.                               |[False]|
|Detection of activated eosinophils in nasal polyps of an aspirin-induced asthma patient.|[True] |
+----------------------------------------------------------------------------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|generic_logreg_classifier_ade|
|Compatibility:|Healthcare NLP 4.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[feature_vector]|
|Output Labels:|[prediction]|
|Language:|en|
|Size:|17.0 KB|

## References

The corpus used for model training is ADE-Corpus-V2 Dataset: Adverse Drug Reaction Data. This is a dataset for classification of a sentence if it is ADE-related (True) or not (False).

Reference: Gurulingappa et al., Benchmark Corpus to Support Information Extraction for Adverse Drug Effects, JBI, 2012. http://www.sciencedirect.com/science/article/pii/S1532046412000615

## Benchmarking

```bash
       label  precision    recall  f1-score   support
       False       0.84      0.92      0.88      3362
        True       0.74      0.57      0.64      1361
    accuracy       -         -         0.82      4723
   macro avg       0.79      0.74      0.76      4723
weighted avg       0.81      0.82      0.81      4723
```