---
layout: model
title: Clinical QA BioGPT (JSL - conversational)
author: John Snow Labs
name: biogpt_chat_jsl_conversational
date: 2023-04-18
tags: [clinical, licensed, en, tensorflow]
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

This model is based on BioGPT finetuned with medical conversations happening in a clinical settings and can answer clinical questions related to symptoms, drugs, tests, and diseases. The difference between this model and `biogpt_chat_jsl` is that this model produces more concise/smaller response.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_conversational_en_4.4.0_3.0_1681853305199.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_conversational_en_4.4.0_3.0_1681853305199.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")
    
gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conversational", "en", "clinical/models")\
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

val summarizer  = MedicalTextGenerator.pretrained("biogpt_chat_jsl_conversational", "en", "clinical/models")
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
question: How to treat asthma ? answer: You have to take montelukast + albuterol tablet once or twice in day according to severity of symptoms. Montelukast is used as a maintenance therapy to relieve symptoms of asthma. Albuterol is used as a rescue therapy when symptoms are severe. You can also use inhaled corticosteroids ( ICS ) like budesonide or fluticasone for long term treatment.
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biogpt_chat_jsl_conversational|
|Compatibility:|Healthcare NLP 4.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|true|