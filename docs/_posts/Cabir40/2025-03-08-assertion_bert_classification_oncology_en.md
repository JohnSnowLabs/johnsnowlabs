---
layout: model
title: Detect Assertion Status (assertion_bert_classification_oncology)
author: John Snow Labs
name: assertion_bert_classification_oncology
date: 2025-03-08
tags: [licensed, clinical, en, assertion, classification, oncology, tensorflow]
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

`Present`, `Past`, `Family`, `Absent`, `Hypothetical`, `Possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_oncology_en_5.5.3_3.0_1741452459296.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_oncology_en_5.5.3_3.0_1741452459296.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
# Test classifier in Spark NLP pipeline
document_assembler = DocumentAssembler()\
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols("document")    .setOutputCol("sentence")

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
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")\
    .setCaseSensitive(False)
    
pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])

# Generating example
data = spark.createDataFrame(["he was begun on physical therapy but remained agitated .",
                              "there were no meatal blood ."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)

# Checking results
result.select("text", "assertion_class.result").show(truncate=False)
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
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "ner_chunk"])\
    .setOutputCol("assertion_class")\
    .setCaseSensitive(False)
    
pipeline = nlp.Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner,
    ner_converter,
    assertion_classifier
])
# Generating example
data = spark.createDataFrame(["he was begun on physical therapy but remained agitated .",
                              "there were no meatal blood ."], StringType()).toDF("text")
                              
result = pipeline.fit(data).transform(data)
```
```scala

val documenter = new DocumentAssembler() 
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
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_oncology", "en", "clinical/models")
    .setInputCols(Array("document", "ner_chunk"))
    .setOutputCol("assertion_class")
    .setCaseSensitive(False)

val pipeline = new Pipeline().setStages(
    Array(
        documenter, 
        sentence_detector,
        tokenizer, 
        embeddings,
        ner,
        ner_converter,
        assertion_classifier
))

val data = Seq(Array("he was begun on physical therapy but remained agitated .",
                    "there were no meatal blood .")).toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------+-------+
|text                                                            |result |
+----------------------------------------------------------------+-------+
|he was begun on physical therapy but remained agitated  .       |present|
|there were no meatal blood .                                    |absent |
+----------------------------------------------------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_oncology|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[assertion_class]|
|Language:|en|
|Size:|406.3 MB|
|Case sensitive:|true|
