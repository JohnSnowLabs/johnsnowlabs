---
layout: model
title: Drug Strength Contextual Parser
author: John Snow Labs
name: drug_strength_parser
date: 2025-11-30
tags: [parser, drug_strength, en, licensed, clinical, contextual_parser]
task: Named Entity Recognition
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.2
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a ContextualParser model that identifies drug strength entities in clinical text. It recognizes dosage patterns including mg, mcg, g, ml, IU, units, and various numeric formats.

## Predicted Entities

`DRUG_STRENGTH`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_strength_parser_en_6.2.0_3.2_1764469403664.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_strength_parser_en_6.2.0_3.2_1764469403664.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

drug_strength_parser = ContextualParserModel.pretrained("drug_strength_parser", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("parsed_drug_strength")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_strength_parser
])

text = """Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

drug_strength_parser = medical.ContextualParserModel.pretrained("drug_strength_parser", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("parsed_drug_strength")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    drug_strength_parser
])

text = """Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val drugStrengthParser = ContextualParserModel.pretrained("drug_strength_parser", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("parsed_drug_strength")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    drugStrengthParser
))

val data = Seq("""Patient was prescribed Metformin 500mg twice daily and Lisinopril 10mg once daily. Ibuprofen 200mg PRN for pain. Vitamin D 1000 IU daily was also recommended.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-------+-----+---+-------------+
|chunk  |begin|end|label        |
+-------+-----+---+-------------+
|500mg  |33   |37 |DRUG_STRENGTH|
|10mg   |64   |67 |DRUG_STRENGTH|
|200mg  |95   |99 |DRUG_STRENGTH|
|1000 IU|126  |132|DRUG_STRENGTH|
+-------+-----+---+-------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_strength_parser|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[chunk_drug_strength]|
|Language:|en|
|Size:|16.2 KB|
|Case sensitive:|false|
