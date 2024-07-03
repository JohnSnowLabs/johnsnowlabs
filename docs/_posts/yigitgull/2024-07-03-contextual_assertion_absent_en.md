---
layout: model
title: Detect Absent Assertion Status with Contextual Assertion
author: John Snow Labs
name: contextual_assertion_absent
date: 2024-07-03
tags: [absent, en, assertion, contextual, licensed, clinical]
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

This model identifies contextual cues within text data to detect absent assertions. It annotates text chunks with assertions using configurable rules, prefix and suffix patterns, and exception patterns.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_absent_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/contextual_assertion_absent_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

#Absent
contextual_assertion_absent = ContextualAssertion\
    .pretrained("contextual_assertion_absent" ,"en" ,"clinical/models")\
    .setInputCols("sentence", "token", "ner_chunk") \
    .setAssertion("absent")\
    .setOutputCol("assertionAbsent") \
 


flattener = Flattener() \
    .setInputCols("assertionAbsent") \
    .setExplodeSelectedFields({"assertionAbsent":["metadata.ner_chunk as ner_chunk",
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
    contextual_assertion_absent,
    flattener

])

empty_data = spark.createDataFrame([[""]]).toDF("text")

model = pipeline.fit(empty_data)

text = """Patient resting in bed. Patient given azithromycin without any difficulty. Patient has audible wheezing, states chest tightness.
     No evidence of hypertension. Patient denies nausea at this time. zofran declined. Patient is also having intermittent sweating
     associated with pneumonia."""

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

    val contextualAssertionAbsent = ContextualAssertion.pretrained("contextual_assertion_absent", "en", "clinical/models")
      .setInputCols("sentences", "tokens", "nerChunks")
      .setOutputCol("assertionAbsent")

    val flattener = new Flattener()
      .setInputCols("assertionAbsent")
      .setExplodeSelectedFields(Map("assertionAbsent" -> Array("metadata.ner_chunk as ner_chunk",
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

    val text = Seq("Patient resting in bed. Patient given azithromycin without any difficulty." +
      " Patient has audible wheezing, states chest tightness.No evidence of hypertension. Patient denies" +
      " nausea at this time. zofran declined. Patient is also having intermittent sweating associated " +
      "with pneumonia. Patient refused pain but tylenol still given. Neither substance abuse nor alcohol" +
      " use however cocaine once used in the last year."
    ).toDS.toDF("text")

    val dataSetResult = pipeline.transform(text)
    dataSetResult.show(false)
```
</div>

## Results

```bash
+--------------+-----+---+---------+----------------------+
|ner_chunk     |begin|end|ner_label|assertionAbsent_result|
+--------------+-----+---+---------+----------------------+
|any difficulty|59   |72 |PROBLEM  |absent                |
|hypertension  |149  |160|PROBLEM  |absent                |
|nausea        |178  |183|PROBLEM  |absent                |
|zofran        |199  |204|TREATMENT|absent                |
|pain          |309  |312|PROBLEM  |absent                |
|tylenol       |318  |324|TREATMENT|absent                |
+--------------+-----+---+---------+----------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|contextual_assertion_absent|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, ner_chunk]|
|Output Labels:|[assertionAbsent]|
|Language:|en|
|Size:|1.3 KB|
|Case sensitive:|false|

## Benchmarking

```bash
       label  precision    recall  f1-score   support
      absent       1.00      0.97      0.98      2594
    accuracy        -         -        0.97      2594
   macro_avg       0.50      0.48      0.49      2594
weighted_avg       1.00      0.97      0.98      2594
```