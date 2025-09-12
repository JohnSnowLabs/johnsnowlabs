---
layout: model
title: Bert For Sequence Classification (Metastasis) ONNX
author: John Snow Labs
name: bert_sequence_classifier_metastasis_onnx
date: 2025-09-12
tags: [licensed, en, bfsc, metastasis, classification, oncology, onnx]
task: Text Classification
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a [BioBERT](https://nlp.johnsnowlabs.com/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) based metastasis classification model that can determine whether the clinical sentences include terms related to metastasis or not.
- `1`: Contains metastasis related terms.
- `0`: Doesn't contain metastasis related terms.

## Predicted Entities

`True`, `False`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_onnx_en_6.1.1_3.0_1757684174420.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_metastasis_onnx_en_6.1.1_3.0_1757684174420.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import SentenceDetectorDLModel, MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_metastasis_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])


sample_texts = [
                ["Contrast MRI confirmed the findings of meningeal carcinomatosis."],
                ["A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis."],
                ["The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci."] ,
                ["After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined."],
                ["The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer."],
                ["The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."],
                ]

sample_data = spark.createDataFrame(sample_texts).toDF("text")


model = pipeline.fit(data)
result = model.transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = (
    nlp.DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

sentenceDetector = (
    nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl","xx")
    .setInputCols(["document"])
    .setOutputCol("sentence")
)

tokenizer = (
    nlp.Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")
)

token_classifier = (
    medical.MedicalBertForTokenClassifier.pretrained(
        "bert_sequence_classifier_metastasis_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "sentence"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    nlp.NerConverter()
    .setInputCols(["sentence", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentenceDetector,
    tokenizer,
    token_classifier,
    ner_converter
])


sample_texts = [
                ["Contrast MRI confirmed the findings of meningeal carcinomatosis."],
                ["A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis."],
                ["The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci."] ,
                ["After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined."],
                ["The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer."],
                ["The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."],
                ]

sample_data = spark.createDataFrame(sample_texts).toDF("text")


model = pipeline.fit(data)
result = model.transform(data)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.ml.Pipeline
import spark.implicits._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetectorDLModel()
  .pretrained("sentence_detector_dl","xx")
  .setInputCols(["document"])
  .setOutputCol("sentence")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_sequence_classifier_metastasis_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val data = Seq(Array("Contrast MRI confirmed the findings of meningeal carcinomatosis.",
                     "A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.",
                     "The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci." ,
                     "After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.",
                     "The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.",
                     "The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease."
                    )).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|text                                                                                                                                                                                                                 |result|
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
|Contrast MRI confirmed the findings of meningeal carcinomatosis.                                                                                                                                                     |[1]   |
|A 62-year-old male presents with weight loss, persistent cough, and episodes of hemoptysis.                                                                                                                          |[0]   |
|The primary tumor (T) is staged as T3 due to its size and local invasion, there is no nodal involvement (N0), and due to multiple bone and liver lesions, it is classified as M1, reflecting distant metastatic foci.|[1]   |
|After all procedures done and reviewing the findings, biochemical results and screening, the TNM classification is determined.                                                                                       |[0]   |
|The oncologist noted that the tumor had spread to the liver, indicating advanced stage cancer.                                                                                                                       |[1]   |
|The patient's care plan is adjusted to focus on symptom management and slowing the progression of the disease.                                                                                                       |[0]   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_metastasis_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|