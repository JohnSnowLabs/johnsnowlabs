---
layout: model
title: Sentence Embeddings - Bluebert uncased (MedNLI) OpenVINO
author: John Snow Labs
name: sbluebert_base_uncased_mli_openvino
date: 2025-07-14
tags: [openvino, english, embeddings, licensed, bert, en]
task: Embeddings
language: en
edition: Spark NLP 6.0.0
spark_version: 3.0
supported: true
engine: openvino
annotator: BertEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained to generate contextual sentence embeddings of input sentences. It has been fine-tuned on MedNLI dataset to provide sota performance on STS and SentEval Benchmarks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbluebert_base_uncased_mli_openvino_en_6.0.0_3.0_1752524808127.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbluebert_base_uncased_mli_openvino_en_6.0.0_3.0_1752524808127.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
from pyspark.ml import Pipeline
from sparknlp.annotator import Tokenizer
from sparknlp.base import DocumentAssembler

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

bert_loaded = BertEmbeddings.pretrained("sbluebert_base_uncased_mli_openvino", "en", "clinical/models")\
    .setInputCols(["document", "token"])\
    .setOutputCol("bert")\

pipeline = Pipeline(
    stages = [
        document_assembler,
        tokenizer,
        bert_loaded
  ])

data = spark.createDataFrame([
    ['William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, and philanthropist.']
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.selectExpr("explode(bert.embeddings) as embeddings").show()

```
```scala
import com.johnsnowlabs.nlp.base._
import com.johnsnowlabs.nlp.annotator._
import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.functions._

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val bertEmbeddings = BertEmbeddings.load("sbluebert_base_uncased_mli_openvino", "en", "clinical/models")
  .setInputCols("document", "token")
  .setOutputCol("bert")

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  bertEmbeddings
))

val data = Seq("William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, and philanthropist.")
  .toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.selectExpr("explode(bert.embeddings) as embeddings").show()

```
</div>

## Results

```bash

+--------------------+
|          embeddings|
+--------------------+
|[0.1681659, -0.48...|
|[0.036125436, -0....|
|[0.15888084, -0.4...|
|[0.16455273, -0.4...|
|[-0.3108327, -0.4...|
|[-0.43798715, -0....|
|[-0.19900186, -0....|
|[-0.002081308, -0...|
|[-0.55144304, -0....|
|[0.21119273, -0.7...|
|[-0.5376373, -0.5...|
|[-0.34766135, -0....|
|[-0.31874946, -0....|
|[0.1254674, -0.51...|
|[0.35613278, -0.4...|
|[0.05157185, -0.5...|
|[-0.18467347, -0....|
|[0.40078178, -0.3...|
|[-0.05733884, -0....|
|[-0.24340808, -0....|
+--------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbluebert_base_uncased_mli_openvino|
|Compatibility:|Spark NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[bert]|
|Language:|en|
|Size:|407.1 MB|
|Case sensitive:|true|
