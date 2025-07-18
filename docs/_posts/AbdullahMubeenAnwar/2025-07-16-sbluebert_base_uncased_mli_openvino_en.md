---
layout: model
title: Sentence Embeddings - Bluebert uncased (MedNLI, OpenVINO)
author: John Snow Labs
name: sbluebert_base_uncased_mli_openvino
date: 2025-07-16
tags: [openvino, english, embeddings, licensed, bert, clinical, en]
task: Embeddings
language: en
edition: Spark NLP 6.0.0
spark_version: 3.0
supported: true
engine: openvino
annotator: BertSentenceEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is trained to generate contextual sentence embeddings of input sentences. It has been fine-tuned on MedNLI dataset to provide sota performance on STS and SentEval Benchmarks.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbluebert_base_uncased_mli_openvino_en_6.0.0_3.0_1752676829250.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbluebert_base_uncased_mli_openvino_en_6.0.0_3.0_1752676829250.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
from johnsnowlabs import nlp

documentAssembler = nlp.DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence = nlp.SentenceDetector() \
    .setInputCols(["document"]) \
    .setOutputCol("sentence")

embeddings = nlp.BertSentenceEmbeddings.pretrained("sbluebert_base_uncased_mli_openvino", "en", "clinical/models") \
    .setInputCols(["sentence"]) \
    .setOutputCol("sentence_bert_embeddings")

embeddingsFinisher = nlp.EmbeddingsFinisher() \
    .setInputCols(["sentence_bert_embeddings"]) \
    .setOutputCols("finished_embeddings") \
    .setOutputAsVector(True)

pipeline = nlp.Pipeline().setStages([
    documentAssembler,
    sentence,
    embeddings,
    embeddingsFinisher
])

data = spark.createDataFrame([
    ['William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, and philanthropist.']
]).toDF("text")

model = pipeline.fit(data)
result = model.transform(data)

result.selectExpr("explode(finished_embeddings) as result").show(5, 80)

```
```scala
import spark.implicits._
import com.johnsnowlabs.nlp.base.DocumentAssembler
import com.johnsnowlabs.nlp.annotator.SentenceDetector
import com.johnsnowlabs.nlp.embeddings.BertSentenceEmbeddings
import com.johnsnowlabs.nlp.EmbeddingsFinisher
import org.apache.spark.ml.Pipeline

val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")

val embeddings = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_openvino", "en", "clinical/models")
  .setInputCols("sentence")
  .setOutputCol("sentence_bert_embeddings")

val embeddingsFinisher = new EmbeddingsFinisher()
  .setInputCols("sentence_bert_embeddings")
  .setOutputCols("finished_embeddings")
  .setOutputAsVector(true)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  sentenceDetector,
  embeddings,
  embeddingsFinisher
))

val data = Seq(
  "William Henry Gates III (born October 28, 1955) is an American business magnate, software developer, investor, and philanthropist."
).toDF("text")

val model = pipeline.fit(data)
val result = model.transform(data)

result.selectExpr("explode(finished_embeddings) as result").show(5, 80)

```
</div>

## Results

```bash

+--------------------------------------------------------------------------------+
|                                                                          result|
+--------------------------------------------------------------------------------+
|[-0.4706500768661499,-0.605597734451294,0.6036401987075806,-0.590848147869110...|
+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbluebert_base_uncased_mli_openvino|
|Compatibility:|Spark NLP 6.0.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document]|
|Output Labels:|[bert]|
|Language:|en|
|Size:|407.1 MB|