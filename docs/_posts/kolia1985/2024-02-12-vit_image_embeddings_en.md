---
layout: model
title: VIT image embeddings
author: John Snow Labs
name: vit_image_embeddings
date: 2024-02-12
tags: [en, licensed]
task: Embeddings
language: en
edition: Visual NLP 5.0.0
spark_version: 3.0
supported: true
annotator: VitImageEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

The Vision Transformer (ViT) model was proposed in An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale by Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby. It’s the first paper that successfully trains a Transformer encoder on ImageNet, attaining very good results compared to familiar convolutional architectures.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/ocr/vit_image_embeddings_en_5.0.0_3.0_1707715428834.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/ocr/vit_image_embeddings_en_5.0.0_3.0_1707715428834.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use

val embeddings = VitImageEmbeddings.pretrained("vit_image_embeddings")
   .setInputCol("image")
   .setOutputCol("embeddings")

<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
embeddings = VitImageEmbeddings.pretrained("vit_image_embeddings") \
   .setInputCol("image") \
   .setOutputCol("embeddings")
```
```scala
val embeddings = VitImageEmbeddings.pretrained("vit_image_embeddings")
   .setInputCol("image")
   .setOutputCol("embeddings")
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|vit_image_embeddings|
|Type:|ocr|
|Compatibility:|Visual NLP 5.0.0+|
|License:|Licensed|
|Edition:|Official|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|318.3 MB|