---
layout: model
title: Lilt checkbox v1
author: John Snow Labs
name: lilt_checkbox_v1
date: 2024-04-17
tags: [en, licensed]
task: Named Entity Recognition
language: en
edition: Visual NLP 5.0.0
spark_version: 3.2
supported: true
annotator: VisualDocumentNerLilt
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Lilt fine-tuned for checkbox recognition

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/lilt_checkbox_v1_en_5.0.0_3.2_1713328336164.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/lilt_checkbox_v1_en_5.0.0_3.2_1713328336164.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
visual_ner = VisualDocumentNerLilt() \
      .pretrained("lilt_checkbox_v1", "en", "clinical/ocr") \
      .setInputCols(["tokens", "image"]) \
      .setOutputCol("entities") \
      .setWhiteList(['I-Key', 'I-Value', 'B-Key'])
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|lilt_checkbox_v1|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[tokens, image]|
|Output Labels:|[entities]|
|Language:|en|
|Size:|431.4 MB|