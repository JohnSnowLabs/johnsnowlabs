---
layout: model
title: Finance Embeddings BGE Base
author: John Snow Labs
name: finembeddings_bge_base
date: 2023-12-07
tags: [finance, en, licensed, bge, embeddings, onnx]
task: Embeddings
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a legal version of the BGE base model fine-tuned on in-house curated datasets. Reference: Xiao, S., Liu, Z., Zhang, P., & Muennighof, N. (2023). C-pack: Packaged resources to advance general chinese embedding. arXiv preprint arXiv:2309.07597.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finembeddings_bge_base_en_1.0.0_3.0_1701948521741.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finembeddings_bge_base_en_1.0.0_3.0_1701948521741.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

tokenizer = nlp.Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

bge = nlp.BertEmbeddings.pretrained("finembeddings_bge_base", "en", "finance/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("bge")

pipeline = nlp.Pipeline(
    stages = [
        documentAssembler,
        tokenizer,
        bge
  ])

data = spark.createDataFrame([['
    ''What is the best way to invest in the stock market?'''
]]).toDF("text")

result = pipeline.fit(data).transform(data)
.selectExpr("explode(bge.embeddings) as bge_embeddings").show(truncate=100)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+
|                                                                                      bge_embeddings|
+----------------------------------------------------------------------------------------------------+
|[0.70071065, 0.8154926, 0.3667199, 0.49541458, 0.5675478, 0.47981235, 0.09903594, 1.0118086, -0.3...|
|[0.5844246, 0.897823, 0.36319774, 0.33672202, 0.6926622, 0.62645215, 0.21583402, 0.99781555, -0.0...|
|[0.5678047, 0.9290247, 0.19549623, 0.29991657, 0.6558282, 0.60267514, 0.2365676, 0.87947553, -0.1...|
|[0.31799358, 0.60279167, 0.7648379, 0.2832115, 0.45711696, 0.12192034, -0.10309678, 1.1410849, -0...|
|[1.0170714, 1.1024956, 0.59346, 0.4784618, 0.81034416, 0.2503267, -0.02142908, 0.6190611, -0.1401...|
|[0.8248961, 1.1220868, 0.27929437, 0.20173876, 0.6809691, 0.6311508, 0.15206291, 0.8089775, 0.317...|
|[0.76785743, 0.9963818, 0.21050292, 0.2416854, 1.0152707, 0.18767616, 0.27576423, 0.85077125, 0.3...|
|[0.654324, 1.1681782, 0.17568657, 0.23243408, 0.76372075, 0.6539263, 0.2841307, 1.224574, 0.21359...|
|[0.5922923, 1.2471354, 0.090304464, 0.48645073, 0.59852546, 0.8716394, 0.34509993, 0.9442089, 0.1...|
|[0.72195786, 0.9363174, 0.06630206, 0.27642763, 0.7145356, 0.23325293, 0.12738094, 1.0298125, -0....|
|[0.45599157, 0.9871535, 0.15671916, 0.17181304, 0.93662477, 0.27518728, -0.18060194, 0.93082047, ...|
|[0.6865296, 1.052128, 0.2681757, 0.32934788, 0.47195143, 0.81678694, 0.012849957, 1.0271766, -0.0...|
+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finembeddings_bge_base|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[bge_embeddings]|
|Language:|en|
|Size:|397.2 MB|
|Case sensitive:|false|

## References

In-house curated financial datasets.