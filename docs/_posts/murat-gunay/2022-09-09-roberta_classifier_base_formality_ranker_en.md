---
layout: model
title: English RobertaForSequenceClassification Base Cased model (from SkolkovoInstitute)
author: John Snow Labs
name: roberta_classifier_base_formality_ranker
date: 2022-09-09
tags: [en, open_source, roberta, sequence_classification, classification]
task: Text Classification
language: en
nav_key: models
edition: Spark NLP 4.1.0
spark_version: 3.0
supported: true
annotator: RoBertaForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RobertaForSequenceClassification model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP. `roberta-base-formality-ranker` is a English model originally trained by `SkolkovoInstitute`.

## Predicted Entities

`formal`, `informal`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_classifier_base_formality_ranker_en_4.1.0_3.0_1662765912018.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_classifier_base_formality_ranker_en_4.1.0_3.0_1662765912018.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler() \
    .setInputCols(["text"]) \
    .setOutputCols("document")

tokenizer = Tokenizer() \
    .setInputCols("document") \
    .setOutputCol("token")

seq_classifier = RoBertaForSequenceClassification.pretrained("roberta_classifier_base_formality_ranker","en") \
    .setInputCols(["document", "token"]) \
    .setOutputCol("class")
    
pipeline = Pipeline(stages=[documentAssembler, tokenizer, seq_classifier])

data = spark.createDataFrame([["PUT YOUR STRING HERE"]]).toDF("text")

result = pipeline.fit(data).transform(data)
```
```scala
val documentAssembler = new DocumentAssembler() 
      .setInputCols(Array("text")) 
      .setOutputCols(Array("document"))
      
val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")
 
val seq_classifier = RoBertaForSequenceClassification.pretrained("roberta_classifier_base_formality_ranker","en") 
    .setInputCols(Array("document", "token"))
    .setOutputCol("class")
   
val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, seq_classifier))

val data = Seq("PUT YOUR STRING HERE").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_classifier_base_formality_ranker|
|Compatibility:|Spark NLP 4.1.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|454.9 MB|
|Case sensitive:|true|
|Max sentence length:|256|

## References

- [https://huggingface.co/SkolkovoInstitute/roberta-base-formality-ranker](https://huggingface.co/SkolkovoInstitute/roberta-base-formality-ranker)
- [https://github.com/raosudha89/GYAFC-corpus](https://github.com/raosudha89/GYAFC-corpus)
- [https://aclanthology.org/N18-1012](https://aclanthology.org/N18-1012)
- [https://www.seas.upenn.edu/~nlp/resources/formality-corpus.tgz](https://www.seas.upenn.edu/~nlp/resources/formality-corpus.tgz)
- [https://aclanthology.org/Q16-1005](https://aclanthology.org/Q16-1005)