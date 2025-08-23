---
layout: model
title: Detect Assertion Status (assertion_bert_classification_clinical_onnx)
author: John Snow Labs
name: assertion_bert_classification_clinical_onnx
date: 2025-07-15
tags: [licensed, clinical, en, assertion, classification, onnx]
task: Assertion Status
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
engine: onnx
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
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/02.0.Clinical_Assertion_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_clinical_onnx_en_6.0.2_3.0_1752593721962.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_clinical_onnx_en_6.0.2_3.0_1752593721962.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical_onnx", "en", "clinical/models")\
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
text = """
Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""
data = spark.createDataFrame([[text]]).toDF("text")
                              
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
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_clinical_onnx", "en", "clinical/models")\
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
text = """
Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""
data = spark.createDataFrame([[text]]).toDF("text")
                              
result = pipeline.fit(data).transform(data)

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
    .setCaseSensitive(false)

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_clinical_onnx", "en", "clinical/models")
    .setInputCols(Array("document", "ner_chunk"))
    .setOutputCol("assertion_class")
    .setCaseSensitive(false)

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

val text = """
Patient with severe fever and sore throat.
He shows no stomach pain and he maintained on an epidural and PCA for pain control.
He also became short of breath with climbing a flight of stairs.
After CT, lung tumor located at the right lower lobe. Father with Alzheimer.
"""


val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|    | chunks                                                         |   begin |   end | entities   | assertion   |   confidence |
|---:|:---------------------------------------------------------------|--------:|------:|:-----------|:------------|-------------:|
|  0 | acute distress                                                 |      43 |    56 | PROBLEM    | Absent      |     0.992191 |
|  1 | mild arcus senilis in the right                                |     191 |   221 | PROBLEM    | Present     |     0.99537  |
|  2 | jugular venous pressure distention                             |     380 |   413 | PROBLEM    | Absent      |     0.997313 |
|  3 | adenopathy in the cervical, supraclavicular, or axillary areas |     428 |   489 | PROBLEM    | Absent      |     0.996413 |
|  4 | tender                                                         |     514 |   519 | PROBLEM    | Absent      |     0.995015 |
|  5 | some fullness in the left upper quadrant                       |     535 |   574 | PROBLEM    | Possible    |     0.524748 |
|  6 | some edema                                                     |     660 |   669 | PROBLEM    | Present     |     0.987595 |
|  7 | cyanosis                                                       |     679 |   686 | PROBLEM    | Absent      |     0.996593 |
|  8 | clubbing                                                       |     692 |   699 | PROBLEM    | Absent      |     0.996629 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_clinical_onnx|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk]|
|Output Labels:|[assertion_onnx]|
|Language:|en|
|Size:|405.6 MB|
|Case sensitive:|true|