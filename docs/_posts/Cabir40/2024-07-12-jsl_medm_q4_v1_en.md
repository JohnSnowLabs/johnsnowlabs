---
layout: model
title: JSL_MedM (LLM - q4)
author: John Snow Labs
name: jsl_medm_q4_v1
date: 2024-07-12
tags: [en, licensed, clinical, medical, llm, summarization, qa, ragi chat]
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

This LLM model is trained to perform Q&A, Summarization, RAG, and Chat.


## Predicted Entities




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_medm_q4_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_medm_q4_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_medm_q4_v1", "en", "clinical/models")

prompt = """
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

response = llm_loader_pretrained.generate(prompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_medm_q4_v1", "en", "clinical/models")

val prompt = """A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin""".stripMargin

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
"""The correct answer is E: Nitrofurantoin.

The patient is presenting with symptoms of urinary tract infection (UTI), which is common during pregnancy. Nitrofurantoin is a first-line antibiotic for uncomplicated UTI during pregnancy. It is safe and effective in treating UTI during pregnancy and has been used for many years without any adverse effects on the fetus.
"""
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_medm_q4_v1|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|4.5 GB|



## Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate

```bash
## Overall
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.29         | 0.25                 | 0.50          |
| ChatGPT  | 0.21         | 0.30                 | 0.26          |
| Neutral  | 0.43         | 0.38                 | 0.17          |
| None     | 0.07         | 0.07                 | 0.08          |
| total    | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL-MedM | 0.42         | 0.42                 | 0.50          |
| GPT4o    | 0.33         | 0.33                 | 0.28          |
| Neutral  | 0.17         | 0.17                 | 0.12          |
| None     | 0.08         | 0.08                 | 0.10          |
| Total    | 1.00         | 1.00                 | 1.00          |

...
```