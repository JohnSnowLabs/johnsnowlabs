---
layout: model
title: Detect Someone Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_someone_else
date: 2024-06-26
tags: [licensed, clinical, en, contextual, assertion, someoneelse]
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

This model identifies contextual cues within text data, such as negation, uncertainty, and assertion. It is used clinical assertion detection, etc. It annotates text chunks with assertions based on configurable rules, prefix and suffix patterns, and exception patterns.

## Predicted Entities

`someoneelse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_someone_else_en_5.4.0_3.0_1719410290867.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_someone_else_en_5.4.0_3.0_1719410290867.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

contextual_assertion_someoneElse = ContextualAssertion\
     .pretrained("contextual_assertion_someone_else" ,"en" ,"clinical/models")\
     .setInputCols("sentence", "token", "ner_chunk")\
     .setOutputCol("assertionSomeoneElse") 
           
flattener =Flattener()\
      .setInputCols("assertionSomeoneElse")\
      .setExplodeSelectedFields({"assertionSomeoneElse": ["result as result",
                                                          "begin as begin ",
                                                          "end as end",
                                                          "metadata.ner_chunk as ner_chunk",
                                                          "metadata.ner_label as ner_label"]                       
                               })            

pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    clinical_ner,
    ner_converter,
    contextual_assertion_someoneElse,
    flattener

])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)
text = """Patient has a family history of diabetes. Father diagnosed with heart failure last year. Sister and brother both have asthma.
          Grandfather had cancer in his late 70s. No known family history of substance abuse. Family history of autoimmune diseases is also noted."""

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

    val contextualAssertionSomeoneElse = ContextualAssertion.pretrained("contextual_assertion_someone_else" ,"en" ,"clinical/models")
      .setInputCols("sentences", "tokens", "nerChunks")
      .setOutputCol("assertionSomeoneElse")

    
    val flattener = new Flattener()
      .setInputCols("assertionSomeoneElse")

    val pipeline = new Pipeline()
      .setStages(Array(documentAssembler,
        sentenceDetector,
        tokenizer,
        embedder,
        nerTagger,
        nerConverter,
        contextualAssertionSomeoneElse,
        flattener
      )).fit(testDataSet)

    val dataSetResult = pipeline.transform(text)
    dataSetResult.show(false)
```
</div>

## Results

```bash
+-------------------+-----+---+---------+------------+
|ner_chunk          |begin|end|ner_label|result      |
+-------------------+-----+---+---------+------------+
|diabetes           |32   |39 |PROBLEM  |someone_else|
|heart failure      |64   |76 |PROBLEM  |someone_else|
|asthma             |118  |123|PROBLEM  |someone_else|
|cancer             |152  |157|PROBLEM  |someone_else|
|substance abuse    |203  |217|PROBLEM  |someone_else|
|autoimmune diseases|238  |256|PROBLEM  |someone_else|
+-------------------+-----+---+---------+------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_someone_else|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[assertionSomeoneElse]|
|Language:|en|
|Size:|1.5 KB|
|Case sensitive:|false|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
someone_else       1.00      0.81      0.89       131
    accuracy         -         -       0.81       131
   macro_avg       0.50      0.40      0.45       131
weighted_avg       1.00      0.81      0.89       131
```