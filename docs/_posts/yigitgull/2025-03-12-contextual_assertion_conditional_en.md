---
layout: model
title: Detect Conditional Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_conditional
date: 2025-03-12
tags: [en, licensed, contextual, conditional, assertion, clinical]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.4
supported: true
annotator: ContextualAssertion
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model identifies contextual cues within text data to detect conditional assertions. It annotates text chunks with assertions using configurable rules, prefix and suffix patterns, and exception patterns.

## Predicted Entities

`conditional`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/02.3.Contextual_Assertion.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_conditional_en_5.5.3_3.4_1741811904923.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_conditional_en_5.5.3_3.4_1741811904923.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

contextual_assertion_conditional = ContextualAssertion.pretrained("contextual_assertion_conditional","en","clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setOutputCol("assertion_conditional") \


pipeline = Pipeline(
    stages=[
      document_assembler,
      sentence_detector,
      tokenizer,
      word_embeddings,
      clinical_ner,
      ner_converter,
      contextual_assertion_conditional
])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)
text = """The patient reports intermittent chest pain when engaging in physical activity, particularly on exertion. Symptoms appear to be contingent upon increased stress levels and heavy meals."""

data = spark.createDataFrame([[text]]).toDF('text')

result = model.transform(data)
result.selectExpr("explode(assertion_conditional) as result").show(truncate=False) 
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

val contextualAssertionConditional = ContextualAssertion.pretrained("contextual_assertion_conditional","en" ,"clinical/models")
  .setInputCols("sentences", "tokens", "nerChunks")
  .setOutputCol("assertion_conditional")


val emptyDataSet = Seq("").toDS().toDF("text")

val pipeline = new Pipeline()
  .setStages(
      Array(documentAssembler,
            sentenceDetector,
            tokenizer,
            embedder,
            nerTagger,
            nerConverter,
            contextualAssertionConditional
  )).fit(emptyDataSet)

val text = Seq("The patient reports intermittent chest pain when engaging in physical activity, particularly on exertion. Symptoms appear to be contingent upon increased stress levels and heavy meals.").toDS.toDF("text")

val dataSetResult = pipeline.transform(text)
dataSetResult.show(100)
```
</div>

## Results

```bash
+-----------------------+-----+---+-----------+
|ner_chunk              |begin|end|result     |
+-----------------------+-----+---+-----------+
|intermittent chest pain|21   |43 |conditional|
|Symptoms               |107  |114|conditional|
+-----------------------+-----+---+-----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_conditional|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[assertion_conditional]|
|Language:|en|
|Size:|1.4 KB|
|Case sensitive:|false|