---
layout: model
title: Detect Family Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_family
date: 2024-11-10
tags: [licensed, clinical, assertion, family, en, contextual]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: ContextualAssertion
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model identifies contextual cues within text data to detect family assertions. It annotates text chunks with assertions using configurable rules, prefix and suffix patterns, and exception patterns.

## Predicted Entities

`family`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_family_en_5.5.0_3.4_1731268220170.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_family_en_5.5.0_3.4_1731268220170.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .pretrained("ner_clinical", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverter() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

contextual_assertion_family = ContextualAssertion.pretrained("contextual_assertion_family","en","clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setOutputCol("assertion_family") \


pipeline = Pipeline(
    stages=[
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      contextual_assertion_family
])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)
text = """Schizophrenia has affected multiple generations in his family. The family has a high prevalence of asthma and allergies."""

data = spark.createDataFrame([[text]]).toDF('text')

result = model.transform(data)
result.select("assertion_family").show(truncate=False)
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

val contextualAssertion = ContextualAssertion.pretrained("contextual_assertion_family","en" ,"clinical/models")
  .setInputCols("sentences", "tokens", "nerChunks")
  .setOutputCol("assertion_family")


val emptyDataSet = Seq("").toDS().toDF("text")

val pipeline = new Pipeline()
  .setStages(
      Array(documentAssembler,
            sentenceDetector,
            tokenizer,
            embedder,
            nerTagger,
            nerConverter,
            contextualAssertion,
            flattener
  )).fit(emptyDataSet)

val text = Seq("Diabetes runs in her family, affecting both her parents and grandparents.").toDS.toDF("text")

val dataSetResult = pipeline.transform(text)
dataSetResult.show(truncate=false)
```
</div>

## Results

```bash
+-------------+-----+---+---------+------+
|ner_chunk    |begin|end|ner_label|result|
+-------------+-----+---+---------+------+
|Schizophrenia|0    |12 |PROBLEM  |family|
|asthma       |99   |104|PROBLEM  |family|
+-------------+-----+---+---------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_family|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[assertion_family]|
|Language:|en|
|Size:|1.5 KB|
|Case sensitive:|false|