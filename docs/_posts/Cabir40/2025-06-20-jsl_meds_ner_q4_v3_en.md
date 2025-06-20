---
layout: model
title: JSL_MedS_NER (LLM - q4 - v3)
author: John Snow Labs
name: jsl_meds_ner_q4_v3
date: 2025-06-20
tags: [en, licensed, clinical, medical, llm, ner, llamacpp]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.0.2
spark_version: 3.0
supported: true
engine: llamacpp
annotator: MedicalLLM
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This LLM model is trained to extract and link entities in a document. Users needs to define an input schema as explained in the example section. Drug is defined as a list which tells the model that there could be multiple drugs in the document and it has to extract all of them. Each drug has properties like name and reaction. Since “name” is only one, it is a string, but there could be multiple reactions, hence it is a list. Similarly, users can define any schema for any type of entity.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q4_v3_en_6.0.2_3.0_1750422521824.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/jsl_meds_ner_q4_v3_en_6.0.2_3.0_1750422521824.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = MedicalLLM.pretrained("jsl_meds_ner_q4_v3", "en", "clinical/models")\
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

med_ner_prompt = """

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

data = spark.createDataFrame([[med_ner_prompt]]).toDF("text")

results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)
```

{:.jsl-block}

```python
from johnsnowlabs import nlp, medical
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

medical_llm = medical.AutoGGUFModel.pretrained("jsl_meds_ner_q4_v3", "en", "clinical/models")\
    .setInputCols("document")\
    .setOutputCol("completions")\
    .setBatchSize(1)\
    .setNPredict(100)\
    .setUseChatTemplate(True)\
    .setTemperature(0)


pipeline = nlp.Pipeline(
    stages = [
        document_assembler,
        medical_llm
])

med_ner_prompt = """
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

```

```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val medical_llm = MedicalLLM.pretrained("jsl_meds_ner_q4_v3", "en", "clinical/models")
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

val  med_ner_prompt = """

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

val data = Seq(med_ner_prompt).toDF("text")

val results = pipeline.fit(data).transform(data)

results.select("completions").show(truncate=False)
```
</div>

## Results

```bash
{
    "drugs": [
        {
            "name": "Arthrotec",
            "reactions": [
                "drowsy",
                "blurred vision",
                "gastric problems",
                "weird"
            ]
        },
        {
            "name": "",
            "reactions": []
        }
    ]
}
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|jsl_meds_ner_q4_v3|
|Compatibility:|Healthcare NLP 6.0.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.4 GB|
