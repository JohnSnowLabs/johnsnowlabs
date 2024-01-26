---
layout: model
title: Legal E5 Embedding Base
author: John Snow Labs
name: legembedding_e5_base
date: 2023-11-05
tags: [legal, en, e5, sentence_embeddings, onnx, licensed]
task: Embeddings
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: onnx
annotator: E5Embeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a legal version of the E5 base model fine-tuned on Edgar and legal question-answering datasets. Reference: Wang, Liang, et al. “Text embeddings by weakly-supervised contrastive pre-training.” arXiv preprint arXiv:2212.03533 (2022).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legembedding_e5_base_en_1.0.0_3.0_1699207424943.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legembedding_e5_base_en_1.0.0_3.0_1699207424943.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = (
    nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")
)

E5_embedding = (
    nlp.E5Embeddings.pretrained(
        "legembedding_e5_base", "en", "legal/models"
    )
    .setInputCols(["document"])
    .setOutputCol("E5")
)
pipeline = nlp.Pipeline(stages=[document_assembler, E5_embedding])

data = spark.createDataFrame([[' What is the rate of shipment for crude oil from the Lincoln Parish Plant to the Mount Olive Plant and from the Mount Olive Plant to the DCP Black Lake in Ada, LA?']]).toDF("text")


result = pipeline.fit(data).transform(data)
result. Select("E5.result").show()
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+
|                                                                                          embeddings|
+----------------------------------------------------------------------------------------------------+
|[-1.0422493, 0.008562431, -0.31533027, -0.39874774, 0.27517456, 0.6205345, -0.34923095, 0.2872358...|
+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legembedding_e5_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[E5]|
|Language:|en|
|Size:|393.9 MB|

## References

We used in-house annotated data.
