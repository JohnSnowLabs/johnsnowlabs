---
layout: model
title: Detect concepts in drug development trials (BertForTokenClassification - ONNX)
author: John Snow Labs
name: bert_token_classifier_drug_development_trials_onnx
date: 2025-09-09
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.1
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

A BERT-based NER model for extracting key concepts from clinical trial texts, including trial groups, clinical end points, efficacy and safety measures, patient information, and statistical metrics.

## Predicted Entities

`B-Patient_Group`, `B-Confidence_Range`, `B-Trial_Group`, `B-Confidence_Interval`, `O`, `B-DATE`, `I-Confidence_level`, `I-P_Value`, `I-Patient_Group`, `I-Follow_Up`, `B-End_Point`, `B-Duration`, `B-Value`, `B-Follow_Up`, `B-Patient_Count`, `I-DATE`, `I-Value`, `I-ADE`, `I-Trial_Group`, `B-Confidence_level`, `B-Hazard_Ratio`, `I-Patient_Count`, `I-End_Point`, `B-P_Value`, `I-Confidence_Interval`, `I-Confidence_Range`, `B-ADE`, `I-Duration`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_drug_development_trials_onnx_en_6.1.1_3.0_1757422232534.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_drug_development_trials_onnx_en_6.1.1_3.0_1757422232534.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import DocumentAssembler
from sparknlp_jsl.annotator import MedicalBertForTokenClassifier
from sparknlp.annotator import Tokenizer, NerConverter
from pyspark.ml import Pipeline

document_assembler = (
    DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")
)

tokenizer = (
    Tokenizer()
    .setInputCols(["document"])
    .setOutputCol("token")
)

token_classifier = (
    MedicalBertForTokenClassifier.pretrained(
        "bert_token_classifier_drug_development_trials_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
    NerConverter()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = (
    "In June 2003, the median overall survival with and without topotecan "
    "were 4.0 and 3.6 months, respectively. The best complete response (CR), "
    "partial response (PR), stable disease, and progressive disease were "
    "observed in 23, 63, 55, and 33 patients with topotecan, and 11, 61, 66, "
    "and 32 patients without topotecan."
)

data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
```scala
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotators.Tokenizer
import com.johnsnowlabs.nlp.annotators.ner.NerConverter
import com.johnsnowlabs.nlp.annotators.classifier.dl.MedicalBertForTokenClassifier
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val tokenClassifier = MedicalBertForTokenClassifier
  .pretrained("bert_token_classifier_drug_development_trials_onnx", "en", "clinical/models")
  .setInputCols("token", "document")
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new NerConverter()
  .setInputCols("document", "token", "ner")
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = 
  "In June 2003, the median overall survival with and without topotecan " +
  "were 4.0 and 3.6 months, respectively. The best complete response (CR), " +
  "partial response (PR), stable disease, and progressive disease were " +
  "observed in 23, 63, 55, and 33 patients with topotecan, and 11, 61, 66, " +
  "and 32 patients without topotecan."

val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+-----------------------+-------------+
|text                   |entity       |
+-----------------------+-------------+
|June 2003              |DATE         |
|median                 |Duration     |
|overall survival       |End_Point    |
|without topotecan      |Trial_Group  |
|4.0                    |Value        |
|3.6 months             |Value        |
|complete response (CR) |End_Point    |
|partial response (PR)  |End_Point    |
|stable disease         |End_Point    |
|progressive disease    |End_Point    |
|23                     |Patient_Count|
|63                     |Patient_Count|
|55                     |Patient_Count|
|33 patients            |Patient_Count|
|topotecan              |Trial_Group  |
|11                     |Patient_Count|
|61                     |Patient_Count|
|66                     |Patient_Count|
|32 patients            |Patient_Count|
|without topotecan      |Trial_Group  |
+-----------------------+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_drug_development_trials_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|
