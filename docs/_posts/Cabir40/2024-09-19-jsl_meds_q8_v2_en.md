---
layout: model
title: JSL_MedS_v2 (LLM - q8) 
author: John Snow Labs
name: jsl_meds_q8_v2
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q8_v2_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q8_v2_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_q8_v2", "en", "clinical/models")

prompt = """
Based on the following text, what age group is most susceptible to breast cancer?

## Text:
The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy
"""

response = llm_loader_pretrained.generate(prompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_meds_q8_v2", "en", "clinical/models")

val prompt = """
Based on the following text, what age group is most susceptible to breast cancer?

## Text:
The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
- A personal or family history of breast cancer
- A genetic mutation, such as BRCA1 or BRCA2
- Exposure to radiation
- Age (most commonly occurring in women over 50)
- Early onset of menstruation or late menopause
- Obesity
- Hormonal factors, such as taking hormone replacement therapy
"""

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
"""
Based on the provided text, the age group most susceptible to breast cancer is women over the age of 50. This is explicitly mentioned in the text, indicating that breast cancer is most commonly occurring in this age group. It is important to note that while age is a significant risk factor, other factors such as genetic mutations, family history, and hormonal factors also contribute to the likelihood of developing breast cancer. Regular screenings and awareness of risk factors are crucial for early detection and effective management of breast cancer.
"""
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_q8_v2|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.7 GB|



