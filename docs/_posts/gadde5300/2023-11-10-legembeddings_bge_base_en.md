---
layout: model
title: Legal Embeddings BGE Base
author: John Snow Labs
name: legembeddings_bge_base
date: 2023-11-10
tags: [en, licensed, onnx, embeddings]
task: Embeddings
language: en
edition: Legal NLP 1.0.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a legal version of the BGE base model fine-tuned on Edgar and legal question-answering datasets. Reference: Wang, Liang, et al. “Text embeddings by weakly-supervised contrastive pre-training.” arXiv preprint arXiv:2212.03533 (2022).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/legal/models/legembeddings_bge_base_en_1.0.0_3.0_1699632504201.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/legal/models/legembeddings_bge_base_en_1.0.0_3.0_1699632504201.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

BGE_loaded = nlp.BertEmbeddings.load("legembeddings_bge_base","en", "legal/models")\
    .setInputCols(["document","token"])\
    .setOutputCol("BGE")\

pipeline = nlp.Pipeline(
    stages = [
        documentAssembler,
        tokenizer,
        BGE_loaded
  ])

data = spark.createDataFrame([['''Receiving Party shall not use any Confidential Information for any purpose other than the purposes stated in Agreement.''']]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)
result.show(truncate=150)
```

</div>

## Results

```bash
+----------------------------------------------------------------------------------------------------+
|                                                                                          embeddings|
+----------------------------------------------------------------------------------------------------+
|[-0.060075462, -0.26741037, 0.32553613, 0.13449538, 0.22019976, -0.35624868, 1.1038424, 0.8212698...|
|[-0.10228735, -0.3738884, 0.27723783, 0.17312518, 0.26656383, -0.24942908, 1.1518378, 0.7217457, ...|
|[-0.38215938, -0.5851373, 0.35209915, -0.30132422, -0.9744857, 0.5976255, 0.86980593, 0.5825193, ...|
|[-0.8023102, -0.1705234, 0.4355616, -0.16370925, -0.99943596, -0.13651904, 1.0603938, 0.76027215,...|
|[0.17291568, -0.74328834, 0.43998405, -0.1694346, -0.7754292, -0.025751337, 1.1425712, 0.43741557...|
|[-0.27675575, -0.17631046, 0.09160468, -0.22860324, -0.6295841, -0.11335259, 1.0146872, 0.6610859...|
|[-0.11538671, -0.31234437, 0.21929267, 0.10618421, 0.2265009, -0.37587893, 1.1389759, 0.7971325, ...|
|[0.009457495, -0.33288023, 0.2432522, 0.12458266, 0.2707794, -0.36873063, 1.0906105, 0.70786965, ...|
|[-0.295701, -0.61499435, 0.07829141, -0.74933016, -0.531358, -0.18479005, 1.1679127, 0.5615579, 0...|
|[-0.67664135, 0.12311895, 0.08994642, -0.07882077, -0.6767479, -0.16962644, 1.0955209, 0.6912421,...|
|[-0.33884412, -0.26324403, -0.03943791, 0.12610006, -0.6458304, -0.3981361, 0.6717623, 0.5545144,...|
|[-0.84253764, -0.18777902, -0.0011436939, -0.29669517, -0.008230045, -0.19728595, 0.9491053, 0.67...|
|[-0.70816183, -0.22422114, -0.07173601, -0.18688664, -0.1930152, -0.30726036, 0.8886021, 0.789013...|
|[-0.18011564, 0.055544622, 0.061416026, -0.110076465, -0.028466597, -0.27377772, 0.98722064, 0.91...|
|[-0.4780874, -0.28484517, -0.105963364, 0.060177833, -0.75987476, -0.36107045, 0.6527582, 0.53413...|
|[-0.39539725, -0.6021485, -0.018175352, -0.12834826, -0.71462053, -0.17749298, 0.8468195, 0.59975...|
|[-0.095429584, -0.8838102, 0.5930538, -0.33268213, 0.010708451, 0.06336981, 1.2200518, 0.9934566,...|
|[0.06960945, -0.17862234, 0.36319345, 0.28421152, 0.22127056, -0.4145783, 1.0451053, 1.0578575, 0...|
|[-0.07706641, -0.09056446, 0.47557953, -0.14709732, 0.37253422, -0.39098266, 1.2081625, 1.2230319...|
+----------------------------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|legembeddings_bge_base|
|Compatibility:|Legal NLP 1.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[bert]|
|Language:|en|
|Size:|1.2 GB|
|Case sensitive:|true|

## References

For our Legal models, we will use publicly available datasets to fine-tune the model:

- [EDGAR](https://huggingface.co/datasets/pile-of-law/pile-of-law)
- In-house annotated Earning Calls Transcripts