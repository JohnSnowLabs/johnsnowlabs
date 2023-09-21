---
layout: model
title: DO_NOT_MERGE
author: John Snow Labs
name: TEST_MODEL
date: 2023-09-21
tags: [es, licensed]
task: Named Entity Recognition
language: es
edition: Spark NLP 4.3.1
spark_version: 3.2
supported: true
annotator: MedicalNerModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

TEST MODEL

## Predicted Entities

`PROBLEM`, `TEST`, `TREATMENT`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/TEST_MODEL_es_4.3.1_3.2_1695277623329.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/TEST_MODEL_es_4.3.1_3.2_1695277623329.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
TEST DATA
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|TEST_MODEL|
|Compatibility:|Spark NLP 4.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token, embeddings]|
|Output Labels:|[ner]|
|Language:|es|
|Size:|2.6 MB|
|Dependencies:|embeddings_clinical|