---
layout: model
title: Pipeline to JSL_MedS_NER (LLM - q16 - v4)
author: John Snow Labs
name: jsl_meds_ner_q16_v4_pipeline
date: 2025-08-16
tags: [licensed, en, clinical, meds, llm, ner]
task: [Named Entity Recognition]
language: en
edition: Healthcare NLP 6.1.0
spark_version: 3.4
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This pretrained pipeline is built on the top of [jsl_meds_ner_q16_v4](https://nlp.johnsnowlabs.com/2025/07/01/jsl_meds_ner_q16_v4_en.html) model.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q16_v4_pipeline_en_6.1.0_3.4_1755313793866.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q16_v4_pipeline_en_6.1.0_3.4_1755313793866.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from sparknlp.pretrained import PretrainedPipeline

pipeline = PretrainedPipeline("jsl_meds_ner_q16_v4_pipeline", "en", "clinical/models")

text = """### Template:
{
    "drugs": [
        {
            "name": "",
            "reactions": []
        }
    ]
}
### Text:
I feel a bit drowsy & have a little blurred vision , and some gastric problems .
I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50."""

result = pipeline.fullAnnotate(text)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

pipeline = nlp.PretrainedPipeline("jsl_meds_ner_q16_v4_pipeline", "en", "clinical/models")

text = """### Template:
{
    "drugs": [
        {
            "name": "",
            "reactions": []
        }
    ]
}
### Text:
I feel a bit drowsy & have a little blurred vision , and some gastric problems .
I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50."""

result = pipeline.fullAnnotate(text)
```
```scala
import com.johnsnowlabs.nlp.pretrained.PretrainedPipeline

val pipeline = new PretrainedPipeline("jsl_meds_ner_q16_v4_pipeline", "en", "clinical/models")

val text = """### Template:
{
    "drugs": [
        {
            "name": "",
            "reactions": []
        }
    ]
}
### Text:
I feel a bit drowsy & have a little blurred vision , and some gastric problems .
I 've been on Arthrotec 50 for over 10 years on and off , only taking it when I needed it .
Due to my arthritis getting progressively worse , to the point where I am in tears with the agony.
Gp 's started me on 75 twice a day and I have to take it every day for the next month to see how I get on , here goes .
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50."""

val result = pipeline.fullAnnotate(text)
```
</div>

## Results

```bash
{
    "drugs": [
        {
            "name": "Arthrotec 50",
            "reactions": [
                "drowsy",
                "blurred vision",
                "gastric problems"
            ]
        },
        {
            "name": "75",
            "reactions": [
                "weird"
            ]
        }
    ]
}

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_q16_v4_pipeline|
|Type:|pipeline|
|Compatibility:|Healthcare NLP 6.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|6.0 GB|

## Included Models

- DocumentAssembler
- MedicalLLM
