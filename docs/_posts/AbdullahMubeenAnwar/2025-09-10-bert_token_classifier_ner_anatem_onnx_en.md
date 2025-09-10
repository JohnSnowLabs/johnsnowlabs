---
layout: model
title: Detect Anatomical Structures in Medical Text (ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_anatem_onnx
date: 2025-09-10
tags: [medical, clinical, ner, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.0
supported: true
engine: onnx
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Anatomical entities ranging from subcellular structures to organ systems are central to biomedical science, and mentions of these entities are essential to understanding the scientific literature.

This model is trained with the BertForTokenClassification method from the transformers library and imported into Spark NLP. The model detects anatomical structures from a medical text.

## Predicted Entities

`O`, `B-Anatomy`, `I-Anatomy`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_anatem_onnx_en_6.1.0_3.0_1757520931204.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_anatem_onnx_en_6.1.0_3.0_1757520931204.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_anatem_onnx",
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

test_sentence = "Malignant cells often display defects in autophagy, an evolutionarily conserved pathway for degrading long-lived proteins and cytoplasmic organelles. However, as yet, there is no genetic evidence for a role of autophagy genes in tumor suppression. The beclin 1 autophagy gene is monoallelically deleted in 40 - 75 % of cases of human sporadic breast, ovarian, and prostate cancer."
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
  .pretrained("bert_token_classifier_ner_anatem_onnx", "en", "clinical/models")
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

val testSentence = "Malignant cells often display defects in autophagy, an evolutionarily conserved pathway for degrading long-lived proteins and cytoplasmic organelles. However, as yet, there is no genetic evidence for a role of autophagy genes in tumor suppression. The beclin 1 autophagy gene is monoallelically deleted in 40 - 75 % of cases of human sporadic breast, ovarian, and prostate cancer."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------------+-------+
|text                  |entity |
+----------------------+-------+
|Malignant cells       |Anatomy|
|cytoplasmic organelles|Anatomy|
|tumor                 |Anatomy|
|breast                |Anatomy|
|ovarian               |Anatomy|
|prostate cancer       |Anatomy|
+----------------------+-------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_anatem_onnx|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|