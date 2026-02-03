---
layout: model
title: Detect Anatomical Regions (MedicalBertForTokenClassifier - ONNX)
author: John Snow Labs
name: bert_token_classifier_ner_anatomy_onnx
date: 2025-09-10
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

Pretrained named entity recognition deep learning model for anatomy terms. This model is trained with the BertForTokenClassification method from the transformers library and imported into Spark NLP.

## Predicted Entities

`I-Multi-tissue_structure`, `B-Tissue`, `B-Anatomical_system`, `I-Organism_subdivision`, `B-Cell`, `B-Cellular_component`, `I-Pathological_formation`, `I-Anatomical_system`, `B-Pathological_formation`, `B-Developing_anatomical_structure`, `B-Immaterial_anatomical_entity`, `I-Immaterial_anatomical_entity`, `I-Cellular_component`, `I-Cell`, `B-Organ`, `B-Organism_substance`, `I-Organ`, `I-Developing_anatomical_structure`, `B-Organism_subdivision`, `B-Multi-tissue_structure`, `I-Organism_substance`, `O`, `I-Tissue`, `PAD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_anatomy_onnx_en_6.1.1_3.0_1757521819217.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_anatomy_onnx_en_6.1.1_3.0_1757521819217.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
        "bert_token_classifier_ner_anatomy_onnx",
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

test_sentence = "The heart is an organ composed of cardiac muscle tissue and supported by connective tissue, making it a complex multi-tissue structure within the circulatory system, an anatomical system. It develops from the embryonic heart tube, a developing anatomical structure, and is connected to the left atrium, an organism subdivision. Surrounding it is the pericardial sac, an immaterial anatomical entity, which encloses the pericardial cavity, another immaterial anatomical entity. Within the myocardium, cardiac cells function together, and inside them, mitochondria act as vital cellular components. The blood circulating through the heart is an organism substance, while pus may accumulate in case of infection, representing a pathological formation. Sometimes, tumors can also arise in the lung, another organ, showing abnormal pathological formations."
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


token_classifier =  medical.BertForTokenClassifier.pretrained(
        "bert_token_classifier_ner_anatomy_onnx",
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

test_sentence = "The heart is an organ composed of cardiac muscle tissue and supported by connective tissue, making it a complex multi-tissue structure within the circulatory system, an anatomical system. It develops from the embryonic heart tube, a developing anatomical structure, and is connected to the left atrium, an organism subdivision. Surrounding it is the pericardial sac, an immaterial anatomical entity, which encloses the pericardial cavity, another immaterial anatomical entity. Within the myocardium, cardiac cells function together, and inside them, mitochondria act as vital cellular components. The blood circulating through the heart is an organism substance, while pus may accumulate in case of infection, representing a pathological formation. Sometimes, tumors can also arise in the lung, another organ, showing abnormal pathological formations."
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
  .pretrained("bert_token_classifier_ner_anatomy_onnx", "en", "clinical/models")
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

val testSentence = "The heart is an organ composed of cardiac muscle tissue and supported by connective tissue, making it a complex multi-tissue structure within the circulatory system, an anatomical system. It develops from the embryonic heart tube, a developing anatomical structure, and is connected to the left atrium, an organism subdivision. Surrounding it is the pericardial sac, an immaterial anatomical entity, which encloses the pericardial cavity, another immaterial anatomical entity. Within the myocardium, cardiac cells function together, and inside them, mitochondria act as vital cellular components. The blood circulating through the heart is an organism substance, while pus may accumulate in case of infection, representing a pathological formation. Sometimes, tumors can also arise in the lung, another organ, showing abnormal pathological formations."
val data = Seq(testSentence).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)
```
</div>

## Results

```bash

+---------------------+-------------------------------+
|text                 |entity                         |
+---------------------+-------------------------------+
|heart                |Organ                          |
|organ                |Organ                          |
|cardiac muscle tissue|Tissue                         |
|connective tissue    |Tissue                         |
|circulatory system   |Multi-tissue_structure         |
|embryonic heart tube |Developing_anatomical_structure|
|left                 |Multi-tissue_structure         |
|atrium               |Multi-tissue_structure         |
|pericardial sac      |Tissue                         |
|pericardial cavity   |Tissue                         |
|myocardium           |Organ                          |
|cardiac cells        |Cell                           |
+---------------------+-------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_anatomy_onnx|
|Compatibility:|Healthcare NLP 6.1.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|403.7 MB|
|Case sensitive:|true|
|Max sentence length:|128|
