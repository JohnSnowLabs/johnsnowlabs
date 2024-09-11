---
layout: model
title: Bros Hocr Tokenizer
author: John Snow Labs
name: bros_hocr_tokenizer
date: 2024-09-11
tags: [en, licensed]
task: Relation Extraction
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: BrosHocrTokenizer
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Bros Hocr Tokenizer

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/bros_hocr_tokenizer_en_5.0.0_3.0_1726033091322.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/bros_hocr_tokenizer_en_5.0.0_3.0_1726033091322.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

tokenizer = BrosHocrTokenizer().pretrained("bros_hocr_tokenizer") \
            .setInputCol("hocr") \
            .setOutputCol("tokens")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
tokenizer = BrosHocrTokenizer().pretrained("bros_hocr_tokenizer") \
            .setInputCol("hocr") \
            .setOutputCol("tokens")
```

</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bros_hocr_tokenizer|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[token]|
|Language:|en|
|Size:|320.9 KB|