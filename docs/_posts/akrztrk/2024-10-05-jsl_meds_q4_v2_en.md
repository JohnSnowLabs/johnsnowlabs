---
layout: model
title: JSL_MedS_v2 (LLM - q4)
author: John Snow Labs
name: jsl_meds_q4_v2
date: 2024-10-05
tags: [en, licensed, clinical, medical, llm, ner, tensorflow]
task: [Summarization, Question Answering, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to perform Q&A, Summarization, RAG, and Chat.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v2_en_5.5.0_3.0_1728145616615.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v2_en_5.5.0_3.0_1728145616615.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_q4_v2", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)


pipeline = Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

prompt = """
### Question:
who you are, describe yourself
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medical_llm = MedicalLLM.pretrained("jsl_meds_q4_v2", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("completions")
    .setBatchSize(1)
    .setNPredict(100)
    .setUseChatTemplate(True)
    .setTemperature(0)


val pipeline = new Pipeline().setStages(Array(
    document_assembler,
    medical_llm
))

val  prompt = """
### Question:
who you are, describe yourself
"""

val data = Seq(prompt).toDF("text")

val results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
</div>

## Results

```bash

Hello! I am JSL Medical LLM, an artificial intelligence language model specialized in medical knowledge. I am here to assist you with any medical inquiries, provide information on health conditions, and help you understand medical terminology. Please feel free to ask me any questions related to health and medicine.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_q4_v2|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|
