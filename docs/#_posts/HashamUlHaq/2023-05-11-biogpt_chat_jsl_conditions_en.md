---
layout: model
title: Clinical QA BioGPT (JSL - conditions)
author: John Snow Labs
name: biogpt_chat_jsl_conditions
date: 2023-05-11
tags: [en, licensed, clinical, tensorflow]
task: Text Generation
language: en
edition: Healthcare NLP 4.4.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is based on BioGPT finetuned with questions related to various medical conditions. It's less conversational, and more Q&A focused.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_conditions_en_4.4.0_3.0_1683778577103.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_conditions_en_4.4.0_3.0_1683778577103.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")
    
gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conditions", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("answer").setMaxNewTokens(100)
    
pipeline = Pipeline().setStages([document_assembler, gpt_qa])

data = spark.createDataFrame([["How to treat asthma ?"]]).toDF("text")

pipeline.fit(data).transform(data)
```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer  = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conditions", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("answer").setMaxNewTokens(100)

val pipeline = new Pipeline().setStages(Array(document_assembler, summarizer))

val text = "How to treat asthma ?"

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
question: How to treat asthma?. answer: The main treatments for asthma are reliever inhalers, which are small handheld devices that you put into your mouth or nose to help you breathe quickly, and preventer inhaler, a soft mist inhaler that lets you use your inhaler as often as you like. If you have severe asthma, your doctor may prescribe a long-acting bronchodilator, such as salmeterol or vilanterol, or a steroid inhaler. You'll usually need to take both types of inhaler at the same time.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biogpt_chat_jsl_conditions|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|true|