---
layout: model
title: Disease Named Entity Recognition (Base, ONNX)
author: John Snow Labs
name: roberta_disease_ner_onnx
date: 2025-12-26
tags: [roberta, ner, medical, clinical, en, licensed, onnx]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
engine: onnx
annotator: RoBertaForTokenClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

RoBERTa-based token classification model for identifying disease mentions in text using the BIO tagging scheme (B-DISEASE, I-DISEASE, O). Designed for dense disease extraction in clinical and biomedical narratives.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/roberta_disease_ner_onnx_en_6.2.0_3.4_1766781701381.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/roberta_disease_ner_onnx_en_6.2.0_3.4_1766781701381.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.ml import Pipeline

documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = RoBertaForTokenClassification \
    .pretrained("roberta_disease_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient presented with type 2 diabetes, hypertension, chronic kidney disease, congestive heart failure, chronic obstructive pulmonary disease, and atrial fibrillation, later complicated by diabetic retinopathy, peripheral neuropathy, gastroesophageal reflux disease, and osteoarthritis, requiring management of hyperlipidemia, hypothyroidism, and anemia."],
    ["During hospitalization, the patient was diagnosed with pneumonia, sepsis, acute respiratory distress syndrome, acute kidney injury, liver cirrhosis, and deep vein thrombosis, with coexisting conditions of ulcerative colitis, Crohn's disease, systemic lupus erythematosus, and rheumatoid arthritis, necessitating interventions for heart failure exacerbation, arrhythmia, and electrolyte imbalance."],
    ["In the oncology unit, the patient was treated for breast cancer, ovarian cancer, pancreatic cancer, and leukemia, with comorbidities including anemia, neutropenia, thrombocytopenia, febrile neutropenia, and cachexia, complicated by infections such as cytomegalovirus, herpes zoster, and candidiasis, alongside chronic conditions like osteoporosis, hypertension, diabetes mellitus, and chronic pain syndrome."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

tokenClassifier = medical.RoBertaForTokenClassification \
    .pretrained("roberta_disease_ner_onnx", "en", "clinical/models") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("ner")

converter = nlp.NerConverter() \
    .setInputCols(["document", "token", "ner"]) \
    .setOutputCol("ner_chunk")

pipeline = nlp.Pipeline(stages=[
    documentAssembler,
    tokenizer,
    tokenClassifier,
    converter
])

data = spark.createDataFrame([
    ["Patient presented with type 2 diabetes, hypertension, chronic kidney disease, congestive heart failure, chronic obstructive pulmonary disease, and atrial fibrillation, later complicated by diabetic retinopathy, peripheral neuropathy, gastroesophageal reflux disease, and osteoarthritis, requiring management of hyperlipidemia, hypothyroidism, and anemia."],
    ["During hospitalization, the patient was diagnosed with pneumonia, sepsis, acute respiratory distress syndrome, acute kidney injury, liver cirrhosis, and deep vein thrombosis, with coexisting conditions of ulcerative colitis, Crohn's disease, systemic lupus erythematosus, and rheumatoid arthritis, necessitating interventions for heart failure exacerbation, arrhythmia, and electrolyte imbalance."],
    ["In the oncology unit, the patient was treated for breast cancer, ovarian cancer, pancreatic cancer, and leukemia, with comorbidities including anemia, neutropenia, thrombocytopenia, febrile neutropenia, and cachexia, complicated by infections such as cytomegalovirus, herpes zoster, and candidiasis, alongside chronic conditions like osteoporosis, hypertension, diabetes mellitus, and chronic pain syndrome."]
]).toDF("text")

result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk").selectExpr(
    "chunk.result as text",
    "chunk.metadata['entity'] as entity"
).show(truncate=False)

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotators._
import org.apache.spark.sql.functions._
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols(Array("document"))
  .setOutputCol("token")

val tokenClassifier = RoBertaForTokenClassification
  .pretrained("roberta_disease_ner_onnx", "en", "clinical/models")
  .setInputCols(Array("document", "token"))
  .setOutputCol("ner")

val converter = new NerConverter()
  .setInputCols(Array("document", "token", "ner"))
  .setOutputCol("ner_chunk")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  tokenClassifier,
  converter
))

val data = Seq(
  "Patient presented with type 2 diabetes, hypertension, chronic kidney disease, congestive heart failure, chronic obstructive pulmonary disease, and atrial fibrillation, later complicated by diabetic retinopathy, peripheral neuropathy, gastroesophageal reflux disease, and osteoarthritis, requiring management of hyperlipidemia, hypothyroidism, and anemia.",
  "During hospitalization, the patient was diagnosed with pneumonia, sepsis, acute respiratory distress syndrome, acute kidney injury, liver cirrhosis, and deep vein thrombosis, with coexisting conditions of ulcerative colitis, Crohn's disease, systemic lupus erythematosus, and rheumatoid arthritis, necessitating interventions for heart failure exacerbation, arrhythmia, and electrolyte imbalance.",
  "In the oncology unit, the patient was treated for breast cancer, ovarian cancer, pancreatic cancer, and leukemia, with comorbidities including anemia, neutropenia, thrombocytopenia, febrile neutropenia, and cachexia, complicated by infections such as cytomegalovirus, herpes zoster, and candidiasis, alongside chronic conditions like osteoporosis, hypertension, diabetes mellitus, and chronic pain syndrome."
).toDF("text")

val result = pipeline.fit(data).transform(data)

result.selectExpr("explode(ner_chunk) as chunk")
  .selectExpr("chunk.result as text", "chunk.metadata['entity'] as entity")
  .show(false)
```
</div>

## Results

```bash

+--------------------+-------+
|text                |entity |
+--------------------+-------+
|hypertension        |DISEASE|
|atrial fibrillation |DISEASE|
|diabetic retinopathy|DISEASE|
|peripheral          |DISEASE|
|gastroesophageal    |DISEASE|
|osteoarthritis      |DISEASE|
|hyperlipidemia      |DISEASE|
|hypothyroidism      |DISEASE|
|anemia              |DISEASE|
|pneumonia           |DISEASE|
|sepsis              |DISEASE|
|cirrhosis           |DISEASE|
|thrombosis          |DISEASE|
|ulcerative          |DISEASE|
|colitis             |DISEASE|
+--------------------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_disease_ner_onnx|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token, sentence]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|466.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|