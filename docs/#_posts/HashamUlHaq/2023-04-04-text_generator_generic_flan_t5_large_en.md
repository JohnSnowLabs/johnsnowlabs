---
layout: model
title: Generic Text Generation - Large
author: John Snow Labs
name: text_generator_generic_flan_t5_large
date: 2023-04-04
tags: [licensed, en, text_generation, tensorflow]
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

This model is based on google's Flan-T5 Large, and can generate conditional text. Sequence length is 512 tokens.

## Predicted Entities



{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/MEDICAL_TEXT_GENERATION/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/33.1.Medical_Text_Generation.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text_generator_generic_flan_t5_large_en_4.3.2_3.0_1680648636099.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text_generator_generic_flan_t5_large_en_4.3.2_3.0_1680648636099.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document_prompt")

med_text_generator  = MedicalTextGenerator.pretrained("text_generator_generic_flan_t5_large", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)

pipeline = Pipeline(stages=[document_assembler, med_text_generator])
data = spark.createDataFrame([["""Classify the following review as negative or positive:

Not a huge fan of her acting, but the movie was actually quite good!"""]]).toDF("prompt")
pipeline.fit(data).transform(data)
```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("document_prompt")

val med_text_generator  = MedicalTextGenerator.pretrained("text_generator_generic_flan_t5_large", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setOutputCol("answer")
    .setMaxNewTokens(256)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)

val pipeline = new Pipeline().setStages(Array(document_assembler, med_text_generator))
val data = Seq(Array("""Classify the following review as negative or positive:

Not a huge fan of her acting, but the movie was actually quite good!""")).toDS.toDF("prompt")
val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
positive
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_generator_generic_flan_t5_large|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|2.9 GB|