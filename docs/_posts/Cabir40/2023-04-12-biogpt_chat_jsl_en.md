---
layout: model
title: Clinical QA BioGPT (JSL)
author: John Snow Labs
name: biogpt_chat_jsl
date: 2023-04-12
tags: [licensed, en, clinical, text_generation, biogpt, tensorflow]
task: Text Generation
language: en
edition: Healthcare NLP 4.3.2
spark_version: 3.0
supported: true
engine: tensorflow
annotator: MedicalTextGenerator
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is based on BioGPT finetuned with medical conversations happening in a clinical settings and can answer clinical questions related to symptoms, drugs, tests, and diseases.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_en_4.3.2_3.0_1681319163583.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biogpt_chat_jsl_en_4.3.2_3.0_1681319163583.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")
    
gpt_qa = MedicalTextGenerator.pretrained("biogpt_chat_jsl", "en", "clinical/models")\
    .setInputCols("documents")\
    .setOutputCol("answer")
    
pipeline = Pipeline().setStages([document_assembler, gpt_qa])

data = spark.createDataFrame([["How to treat asthma ?"]]).toDF("text")

pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val summarizer  = MedicalTextGenerator.pretrained("biogpt_chat_jsl", "en", "clinical/models")
    .setInputCols("documents")
    .setOutputCol("answer")

val pipeline = new Pipeline().setStages(Array(document_assembler, summarizer))

val text = "How to treat asthma ?"

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

['Asthma is itself an allergic disease due to cold or dust or pollen or grass etc. irrespective of the triggering factor. You can go for pulmonary function tests if not done. Treatment is mainly symptomatic which might require inhalation steroids, beta agonists, anticholinergics as MDI or rota haler as a regular treatment. To decrease the inflammation of bronchi and bronchioles, you might be given oral antihistamines with mast cell stabilizers (montelukast) and steroids (prednisolone) with nebulization and frequently steam inhalation. To decrease the bronchoconstriction caused by allergens, you might be given oral antihistamines with mast cell stabilizers (montelukast) and steroids (prednisolone) with nebulization and frequently steam inhalation. The best way to cure any allergy is a complete avoidance of allergen or triggering factor. Consult your pulmonologist for further advise.']

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biogpt_chat_jsl|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|true|