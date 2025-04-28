---
layout: model
title: Detect Assertion Status (assertion_bert_classification_jsl)
author: John Snow Labs
name: assertion_bert_classification_jsl
date: 2025-04-28
tags: [licensed, jsl, en, assertion, classification, tensorflow]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.0
supported: true
engine: tensorflow
annotator: BertForAssertionClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities.

## Predicted Entities

`Present`, `Planned`, `SomeoneElse`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_jsl_en_5.5.3_3.0_1745864492083.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_jsl_en_5.5.3_3.0_1745864492083.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")
    
embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")
    
pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])

text = """Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""

data = spark.createDataFrame([[text]]).toDF("text")                         
result = pipeline.fit(data).transform(data)

# show results
result.selectExpr("explode(assertion_class) as result")\
      .selectExpr("result.metadata['ner_chunk'] as ner_chunk",
                  "result.begin as begin",
                  "result.begin as end",
                  "result.metadata['ner_label'] as ner_chunk",
                  "result.result as assertion").show(truncate=False)

```

{:.jsl-block}
```python
# Test classifier in Spark NLP pipeline
document_assembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols("document")\
    .setOutputCol("sentence")
    
tokenizer = nlp.Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")
    
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])

text = """Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""

data = spark.createDataFrame([[text]]).toDF("text")                         
result = pipeline.fit(data).transform(data)

# show results
result.selectExpr("explode(assertion_class) as result")\
      .selectExpr("result.metadata['ner_chunk'] as ner_chunk",
                  "result.begin as begin",
                  "result.begin as end",
                  "result.metadata['ner_label'] as ner_chunk",
                  "result.result as assertion").show(truncate=False)

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val sentence_detector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentences")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")
    .setCaseSensitive(False)

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_jsl", "en", "clinical/models")
    .setInputCols(Array("document", "ner_chunk"))
    .setOutputCol("assertion_class")

val pipeline = new Pipeline().setStages(
    Array(
        document_assembler, 
        sentence_detector,
        tokenizer, 
        embeddings,
        ner,
        ner_converter,
        assertion_classifier
))

val text = """Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""
val data = Seq(Array(text)).toDF("text")                         
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
|    | ner_chunk       |   begin |   end | ner_chunk   | assertion    |
|---:|:----------------|--------:|------:|:------------|:-------------|
|  0 | severe fever    |      13 |    13 | PROBLEM     | Present      |
|  1 | sore throat     |      30 |    30 | PROBLEM     | Present      |
|  2 | stomach pain    |      55 |    55 | PROBLEM     | Absent       |
|  3 | pain control    |     113 |   113 | PROBLEM     | Hypothetical |
|  4 | short of breath |     142 |   142 | PROBLEM     | Present      |
|  5 | lung tumor      |     202 |   202 | PROBLEM     | Present      |
|  6 | Alzheimer       |     258 |   258 | PROBLEM     | SomeoneElse  |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_jsl|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[assertion_class]|
|Language:|en|
|Size:|406.3 MB|
|Case sensitive:|true|
