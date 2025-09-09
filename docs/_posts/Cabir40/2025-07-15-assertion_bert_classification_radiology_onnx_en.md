---
layout: model
title: Detect Assertion Status (assertion_bert_classification_radiology_onnx)
author: John Snow Labs
name: assertion_bert_classification_radiology_onnx
date: 2025-07-15
tags: [licensed, clinical, en, assertion, classification, radiology, onnx]
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

`Confirmed`, `Suspected`, `Negative`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/02.0.Clinical_Assertion_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_radiology_onnx_en_6.0.2_3.0_1752595964071.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classification_radiology_onnx_en_6.0.2_3.0_1752595964071.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["ImagingFindings"])
    
assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_radiology_onnx", "en", "clinical/models")\
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
INTERPRETATION: There has been interval development of a moderate left-sided pneumothorax with near complete collapse of the left upper lobe. 
The lower lobe appears aerated. There is stable, diffuse, bilateral interstitial thickening with no definite acute air space consolidation. 
The heart and pulmonary vascularity are within normal limits. Left-sided port is seen with Groshong tip at the SVC/RA junction. 
No evidence for acute fracture, malalignment, or dislocation.
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

ner = medical.NerModel.pretrained("ner_radiology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["ImagingFindings"])
    
assertion_classifier = medical.BertForAssertionClassification.pretrained("assertion_bert_classification_radiology_onnx", "en", "clinical/models")\
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
INTERPRETATION: There has been interval development of a moderate left-sided pneumothorax with near complete collapse of the left upper lobe. 
The lower lobe appears aerated. There is stable, diffuse, bilateral interstitial thickening with no definite acute air space consolidation. 
The heart and pulmonary vascularity are within normal limits. Left-sided port is seen with Groshong tip at the SVC/RA junction. 
No evidence for acute fracture, malalignment, or dislocation.
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

val ner = MedicalNerModel.pretrained("ner_radiology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("ImagingFindings"))
        
val assertion_classifier = BertForAssertionClassification.pretrained("assertion_bert_classification_radiology_onnx", "en", "clinical/models")
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
INTERPRETATION: There has been interval development of a moderate left-sided pneumothorax with near complete collapse of the left upper lobe. 
The lower lobe appears aerated. There is stable, diffuse, bilateral interstitial thickening with no definite acute air space consolidation. 
The heart and pulmonary vascularity are within normal limits. Left-sided port is seen with Groshong tip at the SVC/RA junction. 
No evidence for acute fracture, malalignment, or dislocation.
"""


val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|    | chunks                        |   begin |   end | entities        | assertion   |   confidence |
|---:|:------------------------------|--------:|------:|:----------------|:------------|-------------:|
|  0 | pneumothorax                  |      78 |    89 | ImagingFindings | Confirmed   |     0.999775 |
|  1 | complete collapse             |     101 |   117 | ImagingFindings | Confirmed   |     0.999778 |
|  2 | aerated                       |     167 |   173 | ImagingFindings | Confirmed   |     0.999811 |
|  3 | thickening                    |     225 |   234 | ImagingFindings | Confirmed   |     0.999158 |
|  4 | acute air space consolidation |     253 |   281 | ImagingFindings | Negative    |     0.999907 |
|  5 | within normal limits          |     325 |   344 | ImagingFindings | Confirmed   |     0.999777 |
|  6 | acute fracture                |     430 |   443 | ImagingFindings | Negative    |     0.999927 |
|  7 | malalignment                  |     446 |   457 | ImagingFindings | Negative    |     0.999929 |
|  8 | dislocation                   |     463 |   473 | ImagingFindings | Negative    |     0.999925 |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classification_radiology_onnx|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk]|
|Output Labels:|[assertion_onnx]|
|Language:|en|
|Size:|405.6 MB|
|Case sensitive:|true|