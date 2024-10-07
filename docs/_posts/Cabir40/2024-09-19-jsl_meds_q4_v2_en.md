---
layout: model
title: JSL_MedS_v2 (LLM - q4) 
author: John Snow Labs
name: jsl_meds_q4_v2
date: 2024-09-19
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v2_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v2_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_q4_v2", "en", "clinical/models")

prompt = """
### Question:
who you are, describe yourself
"""

response = llm_loader_pretrained.generate(prompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_meds_q4_v2", "en", "clinical/models")

val prompt = """
### Question:
who you are, describe yourself
"""

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
"""
Hello! I am JSL Medical LLM, an artificial intelligence language model specialized in medical knowledge. I am here to assist you with any medical inquiries, provide information on health conditions, and help you understand medical terminology. Please feel free to ask me any questions related to health and medicine.
"""
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_q4_v2|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|



