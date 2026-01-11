---
layout: model
title: Detect Possible Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_possible
date: 2026-01-11
tags: [possible, en, assertion, contextual, licensed, clinical]
task: Assertion Status
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: ContextualAssertion
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Identifies medical conditions that are possible or suspected but not confirmed.

## Predicted Entities

`possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_possible_en_6.2.2_3.4_1768168751297.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_possible_en_6.2.2_3.4_1768168751297.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = MedicalNerModel\
    .pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

contextual_assertion = ContextualAssertion\
    .pretrained("contextual_assertion_possible", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_possible")

flattener = Flattener()\
    .setInputCols("assertion_possible")\
    .setExplodeSelectedFields({"assertion_possible": ["metadata.ner_chunk as ner_chunk",
                                                      "begin as begin",
                                                      "end as end",
                                                      "metadata.ner_label as ner_label",
                                                      "result"]})

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    contextual_assertion,
    flattener
])

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = pipeline.fit(empty_data)

text = """Possible pneumonia based on chest X-ray. Patient may have early arthritis. Suspected urinary tract infection."""
data = spark.createDataFrame([[text]]).toDF('text')
result = model.transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel\
    .pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

clinical_ner = medical.NerModel\
    .pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

contextual_assertion = medical.ContextualAssertion\
    .pretrained("contextual_assertion_possible", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_possible")

flattener = medical.Flattener()\
    .setInputCols("assertion_possible")\
    .setExplodeSelectedFields({"assertion_possible": ["metadata.ner_chunk as ner_chunk",
                                                      "begin as begin",
                                                      "end as end",
                                                      "metadata.ner_label as ner_label",
                                                      "result"]})

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    contextual_assertion,
    flattener
])

empty_data = spark.createDataFrame([[""]]).toDF("text")
model = pipeline.fit(empty_data)

text = """Possible pneumonia based on chest X-ray. Patient may have early arthritis. Suspected urinary tract infection."""
data = spark.createDataFrame([[text]]).toDF('text')
result = model.transform(data)

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

val contextualAssertion = ContextualAssertion
    .pretrained("contextual_assertion_possible", "en", "clinical/models")
    .setInputCols("sentences", "tokens", "nerChunks")
    .setOutputCol("assertion_possible")

val flattener = new Flattener()
    .setInputCols("assertion_possible")
    .setExplodeSelectedFields(Map("assertion_possible" -> Array(
        "metadata.ner_chunk as ner_chunk",
        "begin as begin",
        "end as end",
        "metadata.ner_label as ner_label",
        "result as result"
    )))

val emptyDataSet = Seq("").toDS().toDF("text")

val pipeline = new Pipeline()
    .setStages(Array(
        documentAssembler,
        sentenceDetector,
        tokenizer,
        embedder,
        nerTagger,
        nerConverter,
        contextualAssertion,
        flattener
    )).fit(emptyDataSet)

val text = Seq("""Possible pneumonia based on chest X-ray. Patient may have early arthritis. Suspected urinary tract infection.""").toDS.toDF("text")
val dataSetResult = pipeline.transform(text)

```
</div>

## Results

```bash

+-------------------------+-------+-----+-----------+-----------+
|ner_chunk                |begin  |end  |ner_label  |result     |
+-------------------------+-------+-----+-----------+-----------+
|pneumonia                |9      |17   |PROBLEM    |possible   |
|chest X-ray              |28     |38   |TEST       |possible   |
|early arthritis          |58     |72   |PROBLEM    |possible   |
|urinary tract infection  |85     |107  |PROBLEM    |possible   |
+-------------------------+-------+-----+-----------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_possible|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[custom_possible]|
|Language:|en|
|Size:|2.2 KB|
|Case sensitive:|false|
