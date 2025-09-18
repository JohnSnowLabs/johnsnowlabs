---
layout: model
title: Extract entities in clinical trial abstracts (BertForTokenClassification - ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_clinical_trials_abstracts_onnx
date: 2025-09-11
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

This Named Entity Recognition model is trained with the BertForTokenClassification method from transformers library and imported into Spark NLP.

It extracts relevant entities from clinical trial abstracts. It uses a simplified version of the ontology specified by [Sanchez Graillet, O., et al.](https://pub.uni-bielefeld.de/record/2939477) in order to extract concepts related to trial design, diseases, drugs, population, statistics and publication.

## Predicted Entities

`I-CTDesign`, `I-Journal`, `B-Drug`, `I-Author`, `I-Age`, `B-Confidence`, `O`, `B-Value`, `B-PublicationYear`, `B-PercentagePatients`, `B-PMID`, `I-Country`, `B-Duration`, `B-DisorderOrSyndrome`, `I-DisorderOrSyndrome`, `B-AllocationRatio`, `B-CTAnalysisApproach`, `B-PValue`, `I-Value`, `B-DoseValue`, `B-Country`, `I-Duration`, `I-NumberPatients`, `B-TimePoint`, `B-CTDesign`, `I-BioAndMedicalUnit`, `B-NumberPatients`, `I-PercentagePatients`, `I-CTAnalysisApproach`, `B-BioAndMedicalUnit`, `I-DrugTime`, `B-Author`, `B-Journal`, `I-PValue`, `I-DoseValue`, `I-TimePoint`, `I-AllocationRatio`, `I-Confidence`, `B-Age`, `I-Drug`, `B-DrugTime`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_clinical_trials_abstracts_onnx_en_6.1.1_3.0_1757551012509.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_clinical_trials_abstracts_onnx_en_6.1.1_3.0_1757551012509.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_clinical_trials_abstracts_onnx",
        "en",
        "clinical/models"
    )
    .setInputCols(["token", "document"])
    .setOutputCol("ner")
    .setCaseSensitive(True)
)

ner_converter = (
     NerConverterInternal()
    .setInputCols(["document", "token", "ner"])
    .setOutputCol("ner_chunk")
)

pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "This open-label, parallel-group, two-arm, pilot study compared the beta-cell protective effect of adding insulin glargine (GLA) vs. NPH insulin to ongoing metformin. Overall, 28 insulin-naive type 2 diabetes subjects (mean +/- SD age, 61.5 +/- 6.7 years; BMI, 30.7 +/- 4.3 kg/m(2)) treated with metformin and sulfonylurea were randomized to add once-daily GLA or NPH at bedtime."
data = spark.createDataFrame([[test_sentence]]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
```
{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")


tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")


token_classifier = medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_clinical_trials_abstracts_onnx",
        "en",
        "clinical/models"
    )\
    .setInputCols(["token", "document"])\
    .setOutputCol("ner")\
    .setCaseSensitive(True)


ner_converter = medical.NerConverterInternal()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_chunk")


pipeline = Pipeline(stages=[
    document_assembler,
    tokenizer,
    token_classifier,
    ner_converter
])

test_sentence = "This open-label, parallel-group, two-arm, pilot study compared the beta-cell protective effect of adding insulin glargine (GLA) vs. NPH insulin to ongoing metformin. Overall, 28 insulin-naive type 2 diabetes subjects (mean +/- SD age, 61.5 +/- 6.7 years; BMI, 30.7 +/- 4.3 kg/m(2)) treated with metformin and sulfonylurea were randomized to add once-daily GLA or NPH at bedtime."
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
  .pretrained("bert_token_classifier_ner_clinical_trials_abstracts_onnx", "en", "clinical/models")
  .setInputCols(Array("token", "document"))
  .setOutputCol("ner")
  .setCaseSensitive(true)

val nerConverter = new  NerConverterInternal()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline()
  .setStages(Array(
    documentAssembler,
    tokenizer,
    tokenClassifier,
    nerConverter
  ))

val testSentence = "This open-label, parallel-group, two-arm, pilot study compared the beta-cell protective effect of adding insulin glargine (GLA) vs. NPH insulin to ongoing metformin. Overall, 28 insulin-naive type 2 diabetes subjects (mean +/- SD age, 61.5 +/- 6.7 years; BMI, 30.7 +/- 4.3 kg/m(2)) treated with metformin and sulfonylurea were randomized to add once-daily GLA or NPH at bedtime."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+----------------+------------------+
|text            |entity            |
+----------------+------------------+
|open-label      |CTDesign          |
|parallel-group  |CTDesign          |
|two-arm         |CTDesign          |
|insulin glargine|Drug              |
|GLA             |Drug              |
|NPH             |Drug              |
|insulin         |Drug              |
|metformin       |Drug              |
|28              |NumberPatients    |
|insulin-naive   |Drug              |
|type 2 diabetes |DisorderOrSyndrome|
|61.5            |Age               |
|6.7             |Confidence        |
|30.7            |Value             |
|4.3             |Confidence        |
|kg/m(2))        |BioAndMedicalUnit |
|metformin       |Drug              |
|sulfonylurea    |Drug              |
|randomized      |CTDesign          |
|once-daily      |DrugTime          |
+----------------+------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_clinical_trials_abstracts_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.8 MB|
|Case sensitive:|true|
|Max sentence length:|128|