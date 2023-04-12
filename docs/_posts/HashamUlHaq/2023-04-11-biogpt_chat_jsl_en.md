---
layout: model
title: Clinical QA BioGPT (JSL)
author: John Snow Labs
name: biogpt_chat_jsl
date: 2023-04-11
tags: [licensed, en, clinical, tensorflow]
task: Text Generation
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is based on BioGPT finetuned with medical conversations happening in a clinical settings and can answer clinical questions related to symptoms, drugs, tests, and diseases.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_en_4.3.2_3.0_1681237323443.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_en_4.3.2_3.0_1681237323443.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")

gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl", "en", "clinical/models")\
    .setInputCols('documents')\
    .setOutputCol('answer')

pipeline = Pipeline().setStages([document_assembler, gpt_qa])

data = spark.createDataFrame([["question: what is metformin used for? answer:"]]).toDF("text")

pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")

val gpt_qa = new MedicalTextGenerator.pretrained("biogpt_chat_jsl", "en", "clinical/models")\
    .setInputCols("documents")
    .setOutputCol("answer")

val pipeline = new Pipeline().setStages(Array(document_assembler, gpt_qa))

val data = Seq(Array("question: what is metformin used for? answer:")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
question: what is metformin used for ? answer: Metformin is the most commonly prescribed oral hypoglycemics, and it is used to treat type 2 diabetes.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biogpt_chat_jsl|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|true|

## References

Trained on in-house curated dataset
