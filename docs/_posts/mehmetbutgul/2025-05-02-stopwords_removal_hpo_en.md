---
layout: model
title: Stop Words Cleaner for HPO
author: John Snow Labs
name: stopwords_removal_hpo
date: 2025-05-02
tags: [en, licensed, clinical, hpo, stopwords]
task: Stop Words Removal
language: en
edition: Healthcare NLP 5.5.3
spark_version: 3.0
supported: true
annotator: StopWordsCleaner
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is designed to remove stop words from clinical phenotype descriptions, particularly in the context of Human Phenotype Ontology (HPO).

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/stopwords_removal_hpo_en_5.5.3_3.0_1746187715959.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/stopwords_removal_hpo_en_5.5.3_3.0_1746187715959.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = StopWordsCleaner.pretrained("stopwords_removal_hpo", "en", "clinical/models") \
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)
    
pipeline = Pipeline().setStages([
    document_assembler,
    tokenizer,
    stopwords_cleaner
])

text_df = spark.createDataFrame([["The patient shows no signs of muscle weakness or developmental delay"]]).toDF("text")
result_df = pipeline.fit(text_df).transform(text_df)
```

{:.jsl-block}
```python
document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = nlp.StopWordsCleaner.pretrained("stopwords_removal_hpo", "en", "clinical/models") \
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)
    
pipeline = nlp.Pipeline().setStages([
    document_assembler,
    tokenizer,
    stopwords_cleaner
])

text_df = spark.createDataFrame([["The patient shows no signs of muscle weakness or developmental delay"]]).toDF("text")
result_df = pipeline.fit(text_df).transform(text_df)
```
```scala
import spark.implicits._
val documentAssembler = new DocumentAssembler()
  .setInputCol("text")
  .setOutputCol("document")

val tokenizer = new Tokenizer()
  .setInputCols("document")
  .setOutputCol("token")

val stopWordsCleaner = StopWordsCleaner.pretrained("stopwords_removal_hpo", "en", "clinical/models")
  .setInputCols("token")
  .setOutputCol("cleanTokens")
  .setCaseSensitive(false)

val pipeline = new Pipeline().setStages(Array(
  documentAssembler,
  tokenizer,
  stopWordsCleaner
))

val textData = Seq(
  "The patient shows no signs of muscle weakness or developmental delay"
).toDF("text")

val model = pipeline.fit(textData)
val resultDF = model.transform(textData)
```
</div>

## Results

```bash
|   | token    | cleanTokens  |
|---|----------|--------------|
| 0 | The      | --           |
| 1 | patient  | patient      |
| 2 | shows    | shows        |
| 3 | no       | no           |
| 4 | signs    | signs        |
| 5 | of       | --           |
| 6 | muscle   | muscle       |
| 7 | weakness | weakness     |
| 8 | or       | --           |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|stopwords_removal_hpo|
|Compatibility:|Healthcare NLP 5.5.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[token]|
|Output Labels:|[cleanTokens]|
|Language:|en|
|Size:|1.4 KB|
|Case sensitive:|false|