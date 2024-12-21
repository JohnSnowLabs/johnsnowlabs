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
Please see the more benchmark information [here](https://nlp.johnsnowlabs.com/docs/en/benchmark-llm).

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