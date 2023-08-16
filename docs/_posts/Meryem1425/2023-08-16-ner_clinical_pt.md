---
layout: model
title: Detect Problems, Tests and Treatments ( Portuguese)
author: John Snow Labs
name: ner_clinical
date: 2023-08-16
tags: [licensed, clinical, ner, pt]
task: Named Entity Recognition
language: pt
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained named entity recognition deep learning model for clinical terms in Portuguese. The SparkNLP deep learning model (MedicalNerModel) is inspired by a former state of the art model for NER: Chiu & Nicols, Named Entity Recognition with Bidirectional LSTM-CNN.

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pt_5.0.1_3.0_1692216634922.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ner_clinical_pt_5.0.1_3.0_1692216634922.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","pt") \
.setInputCols(["document", "token"]) \
.setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical", "pt", "clinical/models")\
    .setInputCols(["sentence", "token","embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

sample_text = """A paciente apresenta sensibilidade dentária ao consumir alimentos quentes e frios.
Realizou-se um exame clínico e radiográfico para avaliar possíveis cáries ou problemas na raiz do dente.
Identificou-se uma cárie próxima à raiz do dente. Foi realizado um tratamento de restauração para resolver o problema."""

data = spark.createDataFrame([[sample_text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "en")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val embeddings = WordEmbeddingsModel.pretrained("w2v_cc_300d","pt")
    .setInputCols(Array("document", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel.pretrained("ner_clinical", "pt", "clinical/models")
    .setInputCols(Array("sentence", "token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
    document_assembler, 
    sentence_detector,
    tokenizer,
    embeddings,
    ner_model,
    ner_converter   
    ])

val sample_data = Seq("""A paciente apresenta sensibilidade dentária ao consumir alimentos quentes e frios.
Realizou-se um exame clínico e radiográfico para avaliar possíveis cáries ou problemas na raiz do dente.
Identificou-se uma cárie próxima à raiz do dente. Foi realizado um tratamento de restauração para resolver o problema.""").toDS.toDF("text")

val result = pipeline.fit(sample_data).transform(sample_data)
```
</div>

## Results

```bash
+--------------------------+-----+---+---------+
|chunk                     |begin|end|ner_label|
+--------------------------+-----+---+---------+
|sensibilidade dentária    |21   |42 |PROBLEM  |
|alimentos                 |56   |64 |TREATMENT|
|exame clínico             |98   |110|TEST     |
|cáries                    |150  |155|PROBLEM  |
|problemas na raiz do dente|160  |185|PROBLEM  |
|uma cárie                 |203  |211|PROBLEM  |
|tratamento de restauração |255  |279|TREATMENT|
|problema                  |297  |304|PROBLEM  |
+--------------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ner_clinical|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|pt|
|Size:|2.9 MB|

## Benchmarking

```bash
       label  precision    recall  f1-score   support

   TREATMENT       0.83      0.66      0.73       480
        TEST       0.93      0.79      0.85       500
     PROBLEM       0.83      0.83      0.83      1037

   micro-avg       0.85      0.78      0.81      2017
   macro-avg       0.86      0.76      0.81      2017
weighted-avg       0.85      0.78      0.81      2017
```