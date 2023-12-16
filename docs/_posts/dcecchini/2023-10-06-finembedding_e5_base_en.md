---
layout: model
title: Finance E5 Embedding Base
author: John Snow Labs
name: finembedding_e5_base
date: 2023-10-06
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

This model is a financial version of the E5 base model fine-tuned on in-house curated financial datasets. Reference: Wang, Liang, et al. "Text embeddings by weakly-supervised contrastive pre-training." arXiv preprint arXiv:2212.03533 (2022).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/finance/models/finembedding_e5_base_en_1.0.0_3.0_1696603847700.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/finance/models/finembedding_e5_base_en_1.0.0_3.0_1696603847700.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = (
    nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")
)

E5_embedding = (
    nlp.E5Embeddings.pretrained(
        "finembedding_e5_base", "en", "finance/models"
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
|[0.45521045, -0.16874692, -0.06179046, -0.37956607, 1.152633, 0.6849592, -0.9676384, 0.4624033, ...|
+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|finembedding_e5_base|
|Compatibility:|Finance NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[E5]|
|Language:|en|
|Size:|398.5 MB|

## References


In-house curated financial datasets.
