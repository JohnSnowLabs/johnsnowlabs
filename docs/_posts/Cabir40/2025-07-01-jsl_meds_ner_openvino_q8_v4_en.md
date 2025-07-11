---
layout: model
title: JSL_MedS_NER (LLM - q8 - v4)
author: John Snow Labs
name: jsl_meds_ner_openvino_q8_v4
date: 2025-07-01
tags: [licensed, clinical, en, llm, ner, meds, openvino]
task: [Named Entity Recognition, Question Answering, Summarization]
language: en
edition: Healthcare NLP 6.0.3
spark_version: 3.0
supported: true
engine: openvino
annotator: Phi3Transformer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to extract and link entities in a document. Users needs to define an input schema as explained in the example section. Drug is defined as a list which tells the model that there could be multiple drugs in the document and it has to extract all of them. Each drug has properties like name and reaction. Since “name” is only one, it is a string, but there could be multiple reactions, hence it is a list. Similarly, users can define any schema for any type of entity.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_openvino_q8_v4_en_6.0.3_3.0_1751358785691.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_openvino_q8_v4_en_6.0.3_3.0_1751358785691.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

phi3 = Phi3Transformer.pretrained(f"jsl_meds_ner_openvino_q8_v4", "en", "clinical/models")\
    .setInputCols(["documents"])\
    .setOutputCol("generation")\
    .setMaxOutputLength(500)

pipeline = Pipeline().setStages([
    document_assembler,
    phi3
])

text = """
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

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
from johnsnowlabs import nlp, medical

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("documents")

phi3 = nlp.Phi3Transformer.pretrained(f"jsl_meds_ner_openvino_q8_v4", "en", "clinical/models")\
    .setInputCols(["documents"])\
    .setOutputCol("generation")\
    .setMaxOutputLength(500)

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    phi3
])

text = """
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

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("documents")

val phi3 = Phi3Transformer.pretrained(f"jsl_meds_ner_openvino_q8_v4", "en", "clinical/models")
    .setInputCols(Array("documents"))
    .setOutputCol("generation")
    .setMaxOutputLength(500)

val pipeline = new Pipeline().setStages([
    document_assembler,
    phi3
])

val text = """
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

val data = Seq(text).toDF("text")

val result = pipeline.fit(data).transform(data)
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
|Model Name:|jsl_meds_ner_openvino_q8_v4|
|Compatibility:|Healthcare NLP 6.0.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[documents]|
|Output Labels:|[generation]|
|Language:|en|
|Size:|3.5 GB|