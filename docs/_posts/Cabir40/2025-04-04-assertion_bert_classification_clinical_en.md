---
layout: model
title: Detect Assertion Status (assertion_bert_classification_clinical)
author: John Snow Labs
name: assertion_bert_classification_clinical
date: 2025-04-04
tags: [licensed, clinical, en, assertion, classification, tensorflow]
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

`absent`, `present`, `conditional`, `associated_with_someone_else`, `hypothetical`, `possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_clinical_en_5.5.3_3.0_1743785655582.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_clinical_en_5.5.3_3.0_1743785655582.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")\
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
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")\
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
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical", "en", "clinical/models")
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
| ner_chunk       |   begin |   end | ner_chunk   | assertion                    |
|:----------------|--------:|------:|:------------|:-----------------------------|
| severe fever    |      13 |    13 | PROBLEM     | present                      |
| sore throat     |      30 |    30 | PROBLEM     | present                      |
| stomach pain    |      55 |    55 | PROBLEM     | absent                       |
| pain control    |     113 |   113 | PROBLEM     | hypothetical                 |
| short of breath |     142 |   142 | PROBLEM     | conditional                  |
| lung tumor      |     202 |   202 | PROBLEM     | present                      |
| Alzheimer       |     258 |   258 | PROBLEM     | associated_with_someone_else |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_clinical|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[assertion_class]|
|Language:|en|
|Size:|406.2 MB|
|Case sensitive:|true|


## Benchmarking

```bash
                       label  precision    recall  f1-score   support
                      absent      0.964     0.976     0.970      2594
associated_with_someone_else      0.932     0.840     0.884       131
                 conditional      0.691     0.514     0.589       148
                hypothetical      0.931     0.912     0.922       445
                    possible      0.814     0.699     0.752       652
                     present      0.963     0.976     0.969      8622
                    accuracy      -         -         0.953     12592
                   macro-avg      0.883     0.820     0.848     12592
                weighted-avg      0.951     0.953     0.951     12592
```
