---
layout: model
title: Oncological Response to Treatment Classifier ONNX
author: John Snow Labs
name: bert_sequence_classifier_response_to_treatment_onnx
date: 2025-09-12
tags: [licensed, en, clinical, public_health, response, treatment, classifier, onnx]
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

The Oncological Response to Treatment classifier employs [MedicalBertForSequenceClassification embeddings](https://sparknlp.org/2022/07/18/biobert_pubmed_base_cased_v1.2_en_3_0.html) within a robust classifier architecture. Trained on a diverse dataset, this model provides accurate label assignments and confidence scores for its predictions. The primary goal of this model is to categorize text into two key labels: `Yes` and `No`.

- `Yes`: The patient responded to treatment.

- `No`: The patient did not respond to treatment.

## Predicted Entities

`Yes`, `No`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_response_to_treatment_onnx_en_6.1.1_3.0_1757684851181.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_sequence_classifier_response_to_treatment_onnx_en_6.1.1_3.0_1757684851181.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_sequence_classifier_response_to_treatment_onnx",
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
    ["Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy."],
    ["The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. "],
    ["MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy."],
    ["A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum."],
    ["Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib."],
    ["Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention."],
    ["The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."]
]

data = spark.createDataFrame(sample_texts).toDF("text")


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
        "bert_sequence_classifier_response_to_treatment_onnx",
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
    ["Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy."],
    ["The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. "],
    ["MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy."],
    ["A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum."],
    ["Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib."],
    ["Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention."],
    ["The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."]
]

data = spark.createDataFrame(sample_texts).toDF("text")


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
  .pretrained("bert_sequence_classifier_response_to_treatment_onnx", "en", "clinical/models")
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

val data = Seq(Array(
    "Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting stable disease post-temozolomide therapy.",
    "The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion size from 3 cm to 1 cm, suggesting a favorable response to treatment. The skin infection is also well controlled with multi-antibiotic approach. ",
    "MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision and six months of hormonal suppression therapy.",
    "A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infection. Will discuss the PPI continuum.",
    "Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and number of hepatic metastases following six months of targeted therapy with sorafenib.",
    "Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation and new vascular abnormalities after endovascular coiling of a cerebral aneurysm, indicating a unsuccessful intervention.",
    "The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and FVC, suggesting ineffective control of asthma symptoms with even maximally optimized inhaler therapy. Continuum will discuss."
)).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------------------------------------------------------------------------------------+------+
|                                                                                                text|result|
+----------------------------------------------------------------------------------------------------+------+
|Contrast-enhanced MRI of the brain showed no change in the size of the glioblastoma, suggesting s...| [Yes]|
|The breast ultrasound after neoadjuvant chemotherapy displayed a decrease in the primary lesion s...| [Yes]|
|MRI of the pelvis indicated no further progression of endometriosis after laparoscopic excision a...| [Yes]|
|A repeat endoscopy revealed healing gastric ulcers with new signs of malignancy or H. pylori infe...|  [No]|
|Dynamic contrast-enhanced MRI of the liver revealed no significant reduction in the size and numb...|  [No]|
|Digital subtraction angiography of the cerebral vessels displayed  further aneurysmal dilation an...|  [No]|
|The patient's repeat spirometry tests demonstrated non-significant improvement in both FEV1 and F...|  [No]|
+----------------------------------------------------------------------------------------------------+------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_sequence_classifier_response_to_treatment_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[label]|
|Language:|en|
|Size:|437.7 MB|
|Case sensitive:|true|