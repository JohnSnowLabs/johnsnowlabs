---
layout: model
title: Detect Family Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_family
date: 2026-01-11
tags: [family, en, assertion, contextual, licensed, clinical]
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

Identifies medical conditions that belong to family members rather than the patient.

## Predicted Entities

`family`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_family_en_6.2.2_3.4_1768168705702.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_family_en_6.2.2_3.4_1768168705702.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_converter = NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

contextual_assertion = ContextualAssertion\
    .pretrained("contextual_assertion_family", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_family")

flattener = Flattener()\
    .setInputCols("assertion_family")\
    .setExplodeSelectedFields({"assertion_family": ["metadata.ner_chunk as ner_chunk",
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

text = """Father has diabetes and mother had breast cancer. Sister suffers from migraines."""
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

ner_converter = nlp.NerConverter()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

contextual_assertion = medical.ContextualAssertion\
    .pretrained("contextual_assertion_family", "en", "clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk")\
    .setOutputCol("assertion_family")

flattener = medical.Flattener()\
    .setInputCols("assertion_family")\
    .setExplodeSelectedFields({"assertion_family": ["metadata.ner_chunk as ner_chunk",
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

text = """Father has diabetes and mother had breast cancer. Sister suffers from migraines."""
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
    .pretrained("contextual_assertion_family", "en", "clinical/models")
    .setInputCols("sentences", "tokens", "nerChunks")
    .setOutputCol("assertion_family")

val flattener = new Flattener()
    .setInputCols("assertion_family")
    .setExplodeSelectedFields(Map("assertion_family" -> Array(
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

val text = Seq("""Father has diabetes and mother had breast cancer. Sister suffers from migraines.""").toDS.toDF("text")
val dataSetResult = pipeline.transform(text)

```
</div>

## Results

```bash

+---------------+-------+-----+-----------+-----------+
|ner_chunk      |begin  |end  |ner_label  |result     |
+---------------+-------+-----+-----------+-----------+
|diabetes       |11     |18   |PROBLEM    |family     |
|breast cancer  |35     |47   |PROBLEM    |family     |
|migraines      |70     |78   |PROBLEM    |family     |
+---------------+-------+-----+-----------+-----------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_family|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[custom_family]|
|Language:|en|
|Size:|2.3 KB|
|Case sensitive:|false|