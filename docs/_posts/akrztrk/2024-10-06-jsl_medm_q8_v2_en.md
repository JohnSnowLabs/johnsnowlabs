---
layout: model
title: JSL__v2 (LLM - q8)
author: John Snow Labs
name: jsl__q8_v2
date: 2024-10-06
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

This LLM model is trained to extract and link entities in a document. Users needs to define an input schema as explained in the example section. Drug is defined as a list which tells the model that there could be multiple drugs in the document and it has to extract all of them. Each drug has properties like name and reaction. Since “name” is only one, it is a string, but there could be multiple reactions, hence it is a list. Similarly, users can define any schema for any type of entity.

NOTE: "This model's size is 8B and is available to Healthcare NLP license owners for free. However, this is not the model most capable medical LLM that John Snow has to Labs offer. For the larger and better versions, please try out the models we have in [marketplaces](https://aws.amazon.com/marketplace/pp/prodview-z4jqmczvwgtby)."


{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl__q8_v2_en_5.5.0_3.0_1728224117678.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl__q8_v2_en_5.5.0_3.0_1728224117678.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl__q8_v2", "en", "clinical/models")\
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
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

data = spark.createDataFrame([[prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medical_llm = MedicalLLM.pretrained("jsl__q8_v2", "en", "clinical/models")
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
A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus.
Which of the following is the best treatment for this patient?
A: Ampicillin
B: Ceftriaxone
C: Ciprofloxacin
D: Doxycycline
E: Nitrofurantoin
"""

val data = Seq(prompt).toDF("text")

val results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)

```
</div>

## Results

```bash

The correct answer is E: Nitrofurantoin.

The patient is presenting with symptoms of urinary tract infection (UTI), which is common during pregnancy. Nitrofurantoin is a first-line antibiotic for uncomplicated UTI during pregnancy. It is safe and effective in treating UTI during pregnancy and has been used for many years without any adverse effects on the fetus.

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl__q8_v2|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|8.2 GB|


## Benchmarking

We have generated a total of 400 questions, 100 from each category. These questions were labeled and reviewed by 3 physician annotators. `%` indicates the preference rate.
Please see the more benchmark information [here](https://nlp.johnsnowlabs.com/docs/en/benchmark-llm).

```bash
## Overall
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL- | 0.29         | 0.25                 | 0.50          |
| ChatGPT  | 0.21         | 0.30                 | 0.26          |
| Neutral  | 0.43         | 0.38                 | 0.17          |
| None     | 0.07         | 0.07                 | 0.08          |
| total    | 1.00         | 1.00                 | 1.00          |

## Summary 
| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL- | 0.42         | 0.42                 | 0.50          |
| GPT4o    | 0.33         | 0.33                 | 0.28          |
| Neutral  | 0.17         | 0.17                 | 0.12          |
| None     | 0.08         | 0.08                 | 0.10          |
| Total    | 1.00         | 1.00                 | 1.00          |

## QA

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL- | 0.40         | 0.36                 | 0.60          |
| GPT4o    | 0.15         | 0.19                 | 0.19          |
| Neutral  | 0.38         | 0.38                 | 0.11          |
| None     | 0.08         | 0.08                 | 0.09          |
| Total    | 1.00         | 1.00                 | 1.00          |


## BioMedical

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL- | 0.22         | 0.14                 | 0.55          |
| GPT4o    | 0.21         | 0.36                 | 0.23          |
| Neutral  | 0.49         | 0.44                 | 0.14          |
| None     | 0.07         | 0.06                 | 0.07          |
| Total    | 1.00         | 1.00                 | 1.00          |

## OpenEnded

| Model    | Factuality % | Clinical Relevancy % | Conciseness % |
|----------|--------------|----------------------|---------------|
| JSL- | 0.21         | 0.19                 | 0.38          |
| GPT4o    | 0.18         | 0.30                 | 0.31          |
| Neutral  | 0.55         | 0.46                 | 0.26          |
| None     | 0.05         | 0.05                 | 0.06          |
| Total    | 1.00         | 1.00                 | 1.00          |

```
