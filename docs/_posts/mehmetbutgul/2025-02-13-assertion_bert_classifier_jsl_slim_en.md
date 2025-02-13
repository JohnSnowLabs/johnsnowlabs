---
layout: model
title: Detect Assertion Status (assertion_bert_classifier_jsl_slim)
author: John Snow Labs
name: assertion_bert_classifier_jsl_slim
date: 2025-02-13
tags: [licensed, clinical, en, assertion, tensorflow, classification]
task: Assertion Status
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.0
supported: true
engine: tensorflow
annotator: BertAssertionClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Assign assertion status to clinical entities.

## Predicted Entities

`present`, `absent`, `possible`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classifier_jsl_slim_en_5.5.3_3.0_1739484033697.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/assertion_bert_classifier_jsl_slim_en_5.5.3_3.0_1739484033697.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
     .setInputCol("text") \
     .setOutputCol("document")
sentence_detector = SentenceDetector() \
     .setInputCols(["document"]) \
     .setOutputCol("sentence")
tokenizer = Tokenizer() \
     .setInputCols(["sentence"]) \
     .setOutputCol("token")
word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
     .setInputCols(["sentence", "token"]) \
     .setOutputCol("embeddings")
clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models") \
     .setInputCols(["sentence", "token", "embeddings"]) \
     .setOutputCol("ner")
ner_converter = NerConverterInternal() \
     .setInputCols(["sentence", "token", "ner"]) \
     .setOutputCol("ner_chunk")
clinical_assertion = BertAssertionClassifier.pretrained("assertion_bert_classifier_jsl_slim", "en", "clinical/models") \
     .setInputCols(["sentence", "ner_chunk"]) \
     .setOutputCol("assertion")
pipeline = Pipeline().setStages([
     document_assembler,
     sentence_detector,
     tokenizer,
     word_embeddings,
     clinical_ner,
     ner_converter,
     clinical_assertion
 ])
text = """Patient with severe fever and sore throat. He shows no stomach pain and he maintained on an epidural.
and PCA for pain control. He also became short of breath with climbing a flight of stairs. After CT,
lung tumor located at the right lower lobe. Father with Alzheimer."""
data = spark.createDataFrame([[text]]).toDF("text")
result_df = pipeline.fit(data).transform(data)
result_df.selectExpr("explode(assertion) as result")\
    .select("result.metadata.ner_chunk", "result.begin", "result.end","result.metadata.ner_label", "result.result")\
    .show(100, False)
```
```scala
val document_assembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")
val sentence_detector = new SentenceDetector()
  .setInputCols("document")
  .setOutputCol("sentence")
val tokenizer = new Tokenizer()
  .setInputCols("sentence")
  .setOutputCol("token")
val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
  .setInputCols("sentence", "token")
  .setOutputCol("embeddings")
val clinical_ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
  .setInputCols("sentence", "token", "embeddings")
  .setOutputCol("ner")
val ner_converter = new NerConverterInternal()
  .setInputCols("sentence", "token", "ner")
  .setOutputCol("ner_chunk")
val clinical_assertion = BertAssertionClassifier.pretrained("assertion_bert_classifier_jsl_slim", "en", "clinical/models")
  .setInputCols("sentence", "ner_chunk")
  .setOutputCol("assertion")
val pipeline = new Pipeline().setStages(Array(
  document_assembler,
  sentence_detector,
  tokenizer,
  word_embeddings,
  clinical_ner,
  ner_converter,
  clinical_assertion
))
val text = """Patient with severe fever and sore throat. He shows no stomach pain and he maintained on an epidural.
           |and PCA for pain control. He also became short of breath with climbing a flight of stairs. After CT,
           |lung tumor located at the right lower lobe. Father with Alzheimer.""".stripMargin
val data = Seq(text).toDF("text")
val result_df = pipeline.fit(data).transform(data)
result_df.selectExpr("explode(assertion) as result")
  .select("result.metadata.ner_chunk", "result.begin", "result.end","result.metadata.ner_label", "result.result")
  .show(100, false)
```
</div>

## Results

```bash
+---------------+-----+---+---------+-------+
|ner_chunk      |begin|end|ner_label|result |
+---------------+-----+---+---------+-------+
|severe fever   |13   |24 |PROBLEM  |present|
|sore throat    |30   |40 |PROBLEM  |present|
|stomach pain   |55   |66 |PROBLEM  |absent |
|an epidural    |89   |99 |TREATMENT|present|
|PCA            |106  |108|TREATMENT|present|
|pain control   |114  |125|TREATMENT|present|
|short of breath|143  |157|PROBLEM  |present|
|CT             |199  |200|TEST     |present|
|lung tumor     |203  |212|PROBLEM  |present|
|Alzheimer      |259  |267|PROBLEM  |present|
+---------------+-----+---+---------+-------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|assertion_bert_classifier_jsl_slim|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, ner_chunk]|
|Output Labels:|[assertion]|
|Language:|en|
|Size:|406.3 MB|
|Case sensitive:|false|

## Benchmarking

```bash
               label         precision     recall       f1-score         support
            absent              0.988      0.931           0.959             2594
         possible              0.730      0.755           0.742               652
          present               0.964      0.979           0.971            8622
       accuracy                    -              -                0.956          11868
     macro avg              0.894       0.888          0.891           11868
weighted avg              0.957       0.956          0.956           11868
```