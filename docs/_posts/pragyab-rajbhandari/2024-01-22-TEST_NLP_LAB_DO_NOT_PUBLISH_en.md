---
layout: model
title: TESTING PURPOSE DO NOT PUBLISH
author: John Snow Labs
name: TEST_NLP_LAB_DO_NOT_PUBLISH
date: 2024-01-22
tags: [en, licensed]
task: Relation Extraction
language: en
edition: Healthcare NLP 5.1.2
spark_version: 3.2
supported: true
annotator: RelationExtractionModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

TESTING PURPOSE DO NOT PUBLISH

## Predicted Entities

`is_location_of`, `is_size_of`, `is_date_of`, `is_finding_of`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/TEST_NLP_LAB_DO_NOT_PUBLISH_en_5.1.2_3.2_1705908261638.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/TEST_NLP_LAB_DO_NOT_PUBLISH_en_5.1.2_3.2_1705908261638.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
TESTING PURPOSE DO NOT PUBLISH
```

</div>

## Results

```bash
TESTING PURPOSE DO NOT PUBLISH
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|TEST_NLP_LAB_DO_NOT_PUBLISH|
|Type:|re|
|Compatibility:|Healthcare NLP 5.1.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings, pos_tags, train_ner_chunks, dependencies]|
|Output Labels:|[relations]|
|Language:|en|
|Size:|5.0 MB|
|Max Syntactic Distance:|0|
|Dependencies:|embeddings_clinical|