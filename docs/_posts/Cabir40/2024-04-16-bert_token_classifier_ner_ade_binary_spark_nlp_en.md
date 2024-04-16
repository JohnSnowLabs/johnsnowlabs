---
layout: model
title: BertForTokenClassification from dslim
author: John Snow Labs
name: bert_token_classifier_ner_ade_binary_spark_nlp
date: 2024-04-16
tags: [bert, berttoken, ner, en, licensed]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.0
supported: true
annotator: MedicalBertForTokenClassifier
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertForTokenClassification model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.bert_ner_bert_base_ner is a English model originally trained by dslim.

## Predicted Entities

`PER`, `LOC`, `MISC`, `ORG`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_ade_binary_spark_nlp_en_5.3.1_3.0_1713295856610.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bert_token_classifier_ner_ade_binary_spark_nlp_en_5.3.1_3.0_1713295856610.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("documents")
    
    
tokenClassifier = BertForTokenClassification.pretrained("bert_ner_bert_base_ner","en") \
            .setInputCols(["documents","token"]) \
            .setOutputCol("ner")

pipeline = Pipeline().setStages([documentAssembler, tokenClassifier])



# couple of simple examples
example = spark.createDataFrame([["My name is Sarah and I live in London"],
                                 ["My name is Clara and I live in Berkeley, California."]]).toDF("text")

result = pipeline.fit(example).transform(example)

# result is a DataFrame
result.select("text", "ner.result").show(truncate=False)
```
```scala
val documentAssembler = new DocumentAssembler()
    .setInputCol("text") 
    .setOutputCol("embeddings")
    
val tokenClassifier = BertForTokenClassification  
    .pretrained("bert_ner_bert_base_ner", "en")
    .setInputCols(Array("documents","token")) 
    .setOutputCol("ner") 

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenClassifier))

val pipelineModel = pipeline.fit(data)

val pipelineDF = pipelineModel.transform(data)
```
</div>

## Results

```bash
+----------------------------------------------------+------------------------------------------------+
|text                                                |result                                          |
+----------------------------------------------------+------------------------------------------------+
|My name is Sarah and I live in London               |[O, O, O, B-PER, O, O, O, O, B-LOC]             |
|My name is Clara and I live in Berkeley, California.|[O, O, O, B-PER, O, O, O, O, B-LOC, O, B-LOC, O]|
+----------------------------------------------------+------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_token_classifier_ner_ade_binary_spark_nlp|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[ner]|
|Language:|en|
|Size:|404.2 MB|
|Case sensitive:|true|
|Max sentence length:|128|