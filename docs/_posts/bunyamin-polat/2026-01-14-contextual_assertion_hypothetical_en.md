---
layout: model
title: Detect Hypothetical Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_hypothetical
date: 2026-01-14
tags: [hypothetical, en, assertion, contextual_assertion, licensed, clinical]
task: Assertion Status
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: ContextualAssertion
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Identifies medical conditions mentioned in hypothetical or uncertain contexts.

## Predicted Entities

`hypothetical`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_hypothetical_en_6.2.0_3.4_1768420448298.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_hypothetical_en_6.2.0_3.4_1768420448298.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("contextual_assertion_hypothetical", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_hypothetical")

flattener = Flattener()\
    .setInputCols("assertion_hypothetical")\
    .setExplodeSelectedFields({"assertion_hypothetical": ["metadata.ner_chunk as ner_chunk",
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

text = """Patient should watch for signs of infection. Would recommend monitoring for potential allergic reactions."""
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

clinical_ner = medical.MedicalNerModel\
    .pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

contextual_assertion = medical.ContextualAssertion\
    .pretrained("contextual_assertion_hypothetical", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_hypothetical")

flattener = medical.Flattener()\
    .setInputCols("assertion_hypothetical")\
    .setExplodeSelectedFields({"assertion_hypothetical": ["metadata.ner_chunk as ner_chunk",
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

text = """Patient should watch for signs of infection. Would recommend monitoring for potential allergic reactions."""
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
    .pretrained("contextual_assertion_hypothetical", "en", "clinical/models")
    .setInputCols("sentences", "tokens", "nerChunks")
    .setOutputCol("assertion_hypothetical")

val flattener = new Flattener()
    .setInputCols("assertion_hypothetical")
    .setExplodeSelectedFields(Map("assertion_hypothetical" -> Array(
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

val text = Seq("""Patient should watch for signs of infection. Would recommend monitoring for potential allergic reactions.""").toDS.toDF("text")
val dataSetResult = pipeline.transform(text)

```
</div>

## Results

```bash

+--------------------+-------+-----+-----------+--------------+
|ner_chunk           |begin  |end  |ner_label  |result        |
+--------------------+-------+-----+-----------+--------------+
|infection           |34     |42   |PROBLEM    |hypothetical  |
|monitoring          |61     |70   |TEST       |hypothetical  |
|allergic reactions  |86     |103  |PROBLEM    |hypothetical  |
+--------------------+-------+-----+-----------+--------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_hypothetical|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[custom_hypothetical]|
|Language:|en|
|Size:|1.8 KB|
|Case sensitive:|false|