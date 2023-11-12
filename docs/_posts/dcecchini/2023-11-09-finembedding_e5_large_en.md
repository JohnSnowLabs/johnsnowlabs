---
layout: model
title: Finance E5 Embedding Large
author: John Snow Labs
name: finembedding_e5_large
date: 2023-11-09
tags: [finance, en, licensed, e5, sentence_embedding, onnx]
task: Embeddings
language: en
edition: Finance NLP 1.0.0
spark_version: 3.0
supported: true
engine: onnx
annotator: E5Embeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a financial version of the E5 large model fine-tuned on in-house curated financial datasets. Reference: Wang, Liang, et al. “Text embeddings by weakly-supervised contrastive pre-training.” arXiv preprint arXiv:2212.03533 (2022).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finembedding_e5_large_en_1.0.0_3.0_1699530885080.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finembedding_e5_large_en_1.0.0_3.0_1699530885080.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = (
    nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")
)

E5_embedding = (
    nlp.E5Embeddings.pretrained(
        "finembedding_e5_large", "en", "finance/models"
    )
    .setInputCols(["document"])
    .setOutputCol("E5")
)
pipeline = nlp.Pipeline(stages=[document_assembler, E5_embedding])

data = spark.createDataFrame(
    [["What is the best way to invest in the stock market?"]]
).toDF("text")

result = pipeline.fit(data).transform(data)
result. Select("E5.result").show()
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+
|                                                                                          embeddings|
+----------------------------------------------------------------------------------------------------+
|[0.8358813, -1.30341, -0.576791, 0.25893408, 0.26888973, 0.028243342, 0.47971666, 0.47653574, 0.4...|
+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finembedding_e5_large|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[E5]|
|Language:|en|
|Size:|1.2 GB|

## References

In-house annotated financial datasets.