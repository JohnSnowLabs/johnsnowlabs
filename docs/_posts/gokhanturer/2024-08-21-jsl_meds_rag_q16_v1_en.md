---
layout: model
title: JSL_MedS_Rag_v1 (LLM - q16) 
author: John Snow Labs
name: jsl_meds_rag_q16_v1
date: 2024-08-21
tags: [en, licensed, clinical, medical, llm, ner]
task: [Summarization, Question Answering, Named Entity Recognition]
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: LLMLoader
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to perform Q&A, Summarization, RAG, and Chat.


## Predicted Entities




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_rag_q16_v1_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_rag_q16_v1_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_rag_q16_v1", "en", "clinical/models")

prompt = """
### Template:
Use the following pieces of context to answer the user's question. If you return an answer, end with 'It's my pleasure'.
If you don't know the answer, just say that you don't know, don't try to make up an answer .


### Context:
'Background: Diabetes is referred to a group of diseases characterized by high glucose levels in blood. It is caused by a deficiency in the production or function of insulin or both, which can occur because of different reasons, resulting in protein and lipid metabolic disorders. The aim of this study was to systematically review the prevalence and incidence of type 1 diabetes in the world.',
'A higher prevalence of diabetes mellitus was observed in Addis Ababa public health institutions.\xa0Factors such as age, alcohol drinking, HDL, triglycerides, and vagarious physical activity were associated with diabetes mellitus. Concerned bodies need to work over the ever-increasing diabetes mellitus in Addis Ababa.',

### Questions:
relationship between diabetes and obesity?
"""

response = llm_loader_pretrained.generate(prompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_meds_rag_q16_v1", "en", "clinical/models")

val prompt = """
### Template:
Use the following pieces of context to answer the user's question. If you return an answer, end with 'It's my pleasure'.
If you don't know the answer, just say that you don't know, don't try to make up an answer .

### Context:
'Background: Diabetes is referred to a group of diseases characterized by high glucose levels in blood. It is caused by a deficiency in the production or function of insulin or both, which can occur because of different reasons, resulting in protein and lipid metabolic disorders. The aim of this study was to systematically review the prevalence and incidence of type 1 diabetes in the world.',
'A higher prevalence of diabetes mellitus was observed in Addis Ababa public health institutions.\xa0Factors such as age, alcohol drinking, HDL, triglycerides, and vagarious physical activity were associated with diabetes mellitus. Concerned bodies need to work over the ever-increasing diabetes mellitus in Addis Ababa.',

### Questions:
relationship between diabetes and obesity?
"""

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
"""
Diabetes and obesity are closely related conditions. Obesity is a significant risk factor for the development of type 2 diabetes.
Excess body fat, particularly in the abdominal area, can lead to insulin resistance, where the body's cells do not respond effectively to insulin.
This resistance can result in elevated blood glucose levels, leading to diabetes.
Additionally, obesity can also contribute to the development of type 1 diabetes by triggering an autoimmune response that destines the body's cells to be resistant to insulin
"""
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_rag_q16_v1|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|5.6 GB|



