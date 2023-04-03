---
layout: model
title: Medical Text Generation (T5-based)
author: John Snow Labs
name: text_generator_generic_jsl_base
date: 2023-04-03
tags: [licensed, en, clinical, text_generation, tensorflow]
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

MedicalTextGenerator is a T5-based model for text generation. It can generate texts given a few tokens as an into and can generate up to 512 tokens.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text_generator_generic_jsl_base_en_4.3.2_3.0_1680519245746.zip){:.button.button-orange}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text_generator_generic_jsl_base_en_4.3.2_3.0_1680519245746.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
document_assembler = DocumentAssembler()\
    .setInputCol("prompt")\
    .setOutputCol("document_prompt")

med_text_generator  = MedicalTextGenerator.pretrained("text_generator_generic_jsl_base", "en", "clinical/models")\
    .setInputCols("document_prompt")\
    .setOutputCol("answer")\
    .setMaxNewTokens(256)\
    .setDoSample(True)\
    .setTopK(3)\
    .setRandomSeed(42)

pipeline = Pipeline(stages=[document_assembler, med_text_generator])

data = spark.createDataFrame([["the patient is admitted to the clinic with a severe back pain and "]]).toDF("document_prompt")

pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("prompt")
    .setOutputCol("document_prompt")

val med_text_generator  = MedicalTextGenerator.pretrained("text_generator_generic_jsl_base", "en", "clinical/models")
    .setInputCols("document_prompt")
    .setOutputCol("answer")
    .setMaxNewTokens(256)
    .setDoSample(true)
    .setTopK(3)
    .setRandomSeed(42)

val pipeline = new Pipeline().setStages(Array(document_assembler, med_text_generator))

val data = Seq(Array("the patient is admitted to the clinic with a severe back pain and ")).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

['the patient is admitted to the clinic with a severe back pain and a severe left - sided leg pain. The patient was diagnosed with a lumbar disc herniation and underwent a discectomy. The patient was discharged on the third postoperative day. The patient was followed up for a period of 6 months and was found to be asymptomatic. A rare case of a giant cell tumor of the sacrum. Giant cell tumors ( GCTs ) are benign, locally aggressive tumors that are most commonly found in the long bones of the extremities. They are rarely found in the spine. We report a case of a GCT of the sacrum in a young female patient. The patient presented with a history of progressive lower back pain and a palpable mass in the left buttock. The patient underwent a left hemilaminectomy and biopsy. The histopathological examination revealed a GCT. The patient was treated with a combination of surgery and radiation therapy. The patient was followed up for 2 years and no recurrence was observed. A rare case of a giant cell tumor of the sacrum. Giant cell tumors ( GCTs ) are benign, locally aggressive tumors that are most commonly found in the long bones of the extremities. They are rarely found in the spine. We report a case of a GCT']

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text_generator_generic_jsl_base|
|Compatibility:|Healthcare NLP 4.3.2+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|920.8 MB|
|Case sensitive:|true|
