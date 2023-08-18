---
layout: model
title: Assertion Status for Voice of the Patients (embeddings_clinical_large)
author: John Snow Labs
name: assertion_vop_clinical_large
date: 2023-08-17
tags: [clinical, licensed, en, assertion, vop]
task: Assertion Status
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: AssertionDLModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assertion status model used to predict if an NER chunk refers to a positive finding from the patient (Present_Or_Past), or if it refers to a family member or another person (SomeoneElse) or if it is mentioned but not as something present (Hypothetical_Or_Absent).

This model is the final version of the [WIP assertion model](https://nlp.johnsnowlabs.com/2023/06/17/assertion_vop_3cl_emb_clinical_large_wip_en.html).

## Predicted Entities

`Hypothetical_Or_Absent`, `Present_Or_Past`, `SomeoneElse`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_vop_clinical_large_en_5.0.1_3.0_1692307735425.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_vop_clinical_large_en_5.0.1_3.0_1692307735425.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")\
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("embeddings")

ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models") \
    .setInputCols(["sentence", "token", "embeddings"]) \
    .setOutputCol("ner")

ner_converter = NerConverterInternal() \
    .setInputCols(["sentence", "token", "ner"]) \
    .setOutputCol("ner_chunk")

assertion = AssertionDLModel.pretrained("assertion_vop_clinical_large", "en", "clinical/models") \
    .setInputCols(["sentence", "ner_chunk", "embeddings"]) \
    .setOutputCol("assertion")

pipeline = Pipeline(stages=[document_assembler,
                            sentence_detector,
                            tokenizer,
                            word_embeddings,
                            ner,
                            ner_converter,
                            assertion])

data = spark.createDataFrame([["I was feeling a lot of anxiety honestly. It was right after my mother was diagnosed with diabetes."]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel().pretrained("embeddings_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_vop_emb_clinical_large", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val assertion = AssertionDLModel.pretrained("assertion_vop_clinical_large", "en", "clinical/models")
    .setInputCols("sentence","ner_chunk","embeddings")
    .setOutputCol("assertion")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                                              sentence_detector,
                                              tokenizer,
                                              word_embeddings,
                                              ner,
                                              ner_converter,
                                              assertion))

val data = Seq("I was feeling a lot of anxiety honestly. It was right after my mother was diagnosed with diabetes.").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+--------+-----+---+----------------------+-------+---------------+----------+
|chunk   |begin|end|ner_label             |sent_id|assertion      |confidence|
+--------+-----+---+----------------------+-------+---------------+----------+
|anxiety |23   |29 |PsychologicalCondition|0      |Present_Or_Past|0.9971    |
|mother  |63   |68 |Gender                |1      |SomeoneElse    |0.9975    |
|diabetes|89   |96 |Disease               |1      |SomeoneElse    |0.9969    |
+--------+-----+---+----------------------+-------+---------------+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_vop_clinical_large|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, chunk, embeddings]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|940.7 KB|

## Benchmarking

```bash
                 label  precision    recall  f1-score   support
Hypothetical_Or_Absent       0.77      0.78      0.78      1265
       Present_Or_Past       0.88      0.89      0.89      2873
           SomeoneElse       0.92      0.87      0.90      1084
              accuracy       -         -         0.86      5222
             macro_avg       0.86      0.85      0.85      5222
          weighted_avg       0.86      0.86      0.86      5222
```
