---
layout: model
title: JSL_MedSNER (LLM - q8)
author: John Snow Labs
name: jsl_medsner_zs_q8_v1
date: 2024-07-12
tags: [en, licensed, clinical, medical, llm, ner]
task: [Summarization, Question Answering, Named Entity Recognition]
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

This LLM model is trained to extract and link entities in a document. Users needs to define an input schema as explained in the example section. Drug is defined as a list which tells the model that there could be multiple drugs in the document and it has to extract all of them. Each drug has properties like `name` and `reaction`. Since "name" is only one, it is a string, but there could be multiple reactions, hence it is a list. Similarly, users can define any schema for any type of entity.


## Predicted Entities




{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_medsner_zs_q8_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_medsner_zs_q8_v1_en_5.4.0_3.0_1720040078717.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from sparknlp_jsl.llm import LLMLoader

llm_loader_pretrained = LLMLoader(spark).pretrained("jsl_medsner_zs_q8_v1", "en", "clinical/models")

prompt = """
### Template:
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
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.
"""

response = llm_loader_pretrained.generate(prompt)

```
```scala
import com.johnsnowlabs.ml.gguf.LLMLoader
import com.johnsnowlabs.nlp.SparkAccessor.spark

val llmLoader = new LLMLoader().setSparkSession(spark).pretrained("jsl_medsner_zs_q8_v1", "en", "clinical/models")

val prompt = """
### Template:
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
So far its been very good , pains almost gone , but I feel a bit weird , did n't have that when on 50.
"""

val response = llmLoader.generate(prompt)

```
</div>

## Results

```bash
'''
{
    "drugs": [
        {
            "name": "Arthrotec",
            "reactions": [
                "drowsy",
                "blurred vision",
                "gastric problems"
            ]
        }
    ]
}
'''
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_medsner_zs_q8_v1|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.7 GB|



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