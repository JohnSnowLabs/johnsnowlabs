---
layout: model
title: Detect Past Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_past
date: 2024-07-04
tags: [assertion, past, clinical, en, contextual, licensed]
task: Assertion Status
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: ContextualAssertion
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model identifies contextual cues within text data to detect past assertions. It annotates text chunks with assertions using configurable rules, prefix and suffix patterns, and exception patterns.

## Predicted Entities

`past`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_past_en_5.4.0_3.0_1720051604670.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_past_en_5.4.0_3.0_1720051604670.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel \
    .pretrained("embeddings_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel \
    .pretrained("ner_jsl", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

contextual_assertion_past = ContextualAssertion.pretrained("contextual_assertion_past","en","clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setOutputCol("assertionPast") \
  

flattener = Flattener() \
    .setInputCols("assertionPast") \
    .setExplodeSelectedFields({"assertionPast":["metadata.ner_chunk as ner_chunk",
                                            "begin as begin",
                                            "end as end",
                                            "metadata.ner_label as ner_label",
                                            "result as result"]})

pipeline = Pipeline(
    stages=[
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      contextual_assertion_past,
      flattener

])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)
text = """The patient had no history of smoking or alcohol consumption and there was no family history of any types of tumor. """

data = spark.createDataFrame([[text]]).toDF('text')

result = model.transform(data)
result.show(truncate=False)
```
```scala
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols(Array("document"))
  .setOutputCol("sentences")

val tokenizer = new Tokenizer()
  .setInputCols(Array("sentences"))
  .setOutputCol("tokens")

val embedder = WordEmbeddingsModel
  .pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens"))
  .setOutputCol("embeddings")

val nerTagger = MedicalNerModel
  .pretrained("ner_clinical", "en", "clinical/models")
  .setInputCols(Array("sentences", "tokens", "embeddings"))
  .setOutputCol("nerTags")

val nerConverter = new NerConverterInternal()
  .setInputCols(Array("sentences", "tokens", "nerTags"))
  .setOutputCol("nerChunks")

val contextualAssertionAbsent = ContextualAssertion.pretrained("contextual_assertion_past","en" ,"clinical/models")
  .setInputCols("sentences", "tokens", "nerChunks")
  .setOutputCol("assertionPast")


val flattener = new Flattener()
  .setInputCols("assertionPast")
  .setExplodeSelectedFields(Map("assertionPast" -> Array("metadata.ner_chunk as ner_chunk",
                                                          "metadata.entity",
                                                          "begin as begin",
                                                          "end as end",
                                                          "metadata.ner_label as ner_label",
                                                          "result as result")
                            ))
  
val emptyDataSet = Seq("").toDS().toDF("text")

val pipeline = new Pipeline()
  .setStages(
      Array(documentAssembler,
            sentenceDetector,
            tokenizer,
            embedder,
            nerTagger,
            nerConverter,
            contextualAssertionAbsent,
            flattener
  )).fit(emptyDataSet)

val text = Seq("The patient had no history of smoking or alcohol consumption and there was no family history of any types of tumor.").toDS.toDF("text")

val dataSetResult = pipeline.transform(text)
dataSetResult.show(100)
```
</div>

## Results

```bash
+---------+-----+---+-----------+------+
|ner_chunk|begin|end|ner_label  |result|
+---------+-----+---+-----------+------+
|smoking  |30   |36 |Smoking    |past  |
|alcohol  |41   |47 |Alcohol    |past  |
|tumor    |109  |113|Oncological|past  |
+---------+-----+---+-----------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_past|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, chunk]|
|Output Labels:|[assertionPast]|
|Language:|en|
|Size:|1.5 KB|
|Case sensitive:|false|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
        Past       1.00      0.92      0.96        92
    accuracy        -          -       0.92        92
   macro_avg       0.50      0.46      0.48        92
weighted_avg       1.00      0.92      0.96        92
```