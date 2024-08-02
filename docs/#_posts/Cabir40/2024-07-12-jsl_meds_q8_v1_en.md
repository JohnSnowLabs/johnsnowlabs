---
layout: model
title: JSL_MedS (LLM - q8)
author: John Snow Labs
name: jsl_meds_q8_v1
date: 2024-07-12
tags: [en, licensed, clinical, medical, llm, summarization, qa]
task: [Summarization, Question Answering]
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: LLMLoader
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to perform Summarization and Q&A based on a given context.


## Predicted Entities




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q8_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q8_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_q8_v1", "en", "clinical/models")

ptompt = """
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

response = llm_loader_pretrained.generate(ptompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_meds_q8_v1", "en", "clinical/models")

val prompt = """Based on the following text, what age group is most susceptible to breast cancer?
|## Text:
|The exact cause of breast cancer is unknown. However, several risk factors can increase your likelihood of developing breast cancer, such as:
|- A personal or family history of breast cancer
|- A genetic mutation, such as BRCA1 or BRCA2
|- Exposure to radiation
|- Age (most commonly occurring in women over 50)
|- Early onset of menstruation or late menopause
|- Obesity
|- Hormonal factors, such as taking hormone replacement therapy""".stripMargin

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
"The age group most susceptible to breast cancer, as mentioned in the text, is women over the age of 50."
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_q8_v1|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.7 GB|



