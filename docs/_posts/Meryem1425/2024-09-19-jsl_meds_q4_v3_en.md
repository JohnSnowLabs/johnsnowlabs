---
layout: model
title: JSL_MedS_v3 (LLM - q4) 
author: John Snow Labs
name: jsl_meds_q4_v3
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v3_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_q4_v3_en_5.4.1_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_meds_q4_v3", "en", "clinical/models")

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

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_meds_q4_v3", "en", "clinical/models")

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
Based on the provided text, the age group most susceptible to breast cancer is women over 50 years old. This is explicitly mentioned as the most common occurrence age for breast cancer. While other factors like genetic mutations, family history, and hormonal factors also contribute to the risk, the text specifically highlights age as a significant risk factor. It is important to note that while age is a risk factor, breast cancer can still occur in younger women, and awareness and preventive measures should be considered across all age groups.
"""
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_q4_v3|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.2 GB|



## Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate

```bash
## Overall
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.24         | 0.25                 | 0.38          |
| GPT4o      | 0.19         | 0.26                 | 0.27          |
| Neutral    | 0.43         | 0.36                 | 0.18          |
| None       | 0.14         | 0.13                 | 0.17          |
| Total      | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.47         | 0.48                 | 0.42          |
| GPT4o      | 0.25         | 0.25                 | 0.25          |
| Neutral    | 0.22         | 0.22                 | 0.25          |
| None       | 0.07         | 0.05                 | 0.08          |
| Total      | 1.00         | 1.00                 | 1.00          |

## QA
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.35         | 0.36                 | 0.42          |
| GPT4o      | 0.24         | 0.24                 | 0.29          |
| Neutral    | 0.33         | 0.33                 | 0.18          |
| None       | 0.09         | 0.07                 | 0.11          |
| Total      | 1.00         | 1.00                 | 1.00          |

## BioMedical
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.33         | 0.24                 | 0.57          |
| GPT4o      | 0.12         | 0.08                 | 0.16          |
| Neutral    | 0.45         | 0.57                 | 0.16          |
| None       | 0.10         | 0.10                 | 0.10          |
| Total      | 1.00         | 1.00                 | 1.00          |

## OpenEnded
| Model      | Factuality % | Clinical Relevancy % | Conciseness % |
|------------|--------------|----------------------|---------------|
| JSL-MedS   | 0.35         | 0.30                 | 0.39          |
| GPT4o      | 0.30         | 0.33                 | 0.41          |
| Neutral    | 0.19         | 0.20                 | 0.02          |
| None       | 0.17         | 0.17                 | 0.19          |
| Total      | 1.00         | 1.00                 | 1.00          |
```