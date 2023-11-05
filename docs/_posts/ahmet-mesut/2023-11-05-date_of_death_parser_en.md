---
layout: model
title: Date of Death Contextual Parser Model
author: John Snow Labs
name: date_of_death_parser
date: 2023-11-05
tags: [en, clinical, date_of_death, contextual_parser, dod, licensed]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.1.2
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a `ContextualParserModel` that can extract date-of-death (DOD) entities in clinical texts.

## Predicted Entities

`DOD`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_of_death_parser_en_5.1.2_3.0_1699192712408.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_of_death_parser_en_5.1.2_3.0_1699192712408.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler() \
    .setInputCol("text") \
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer() \
    .setInputCols(["sentence"]) \
    .setOutputCol("token")

dod_contextual_parser = ContextualParserModel.pretrained("date_of_death_parser", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_dod") 

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_dod"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        dod_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """
Record date : 2081-01-04
DB : 11.04.1962
DT : 12-03-1978
DOD : 10.25.23

SOCIAL HISTORY:
Jane Doe was born on November 4, 1962, in London, and she got married on April 5, 1979.
When she got pregnant on May 15, 1979, the doctor wanted to verify her date of birth, which was confirmed to be November 4, 1962.
Jane was 45 years old when she sadly passed away on September 25, 2007.

PROCEDURES:
Patient Jane Doe was evaluated on March 15, 1988, for allergies. She was seen by the endocrinology service and was discharged on September 23, 1988.

MEDICATIONS:
1. Coumadin 1 mg daily. Jane's last INR was measured on August 14, 2007, and it was 2.3."""

result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))

```
```scala
val document_assembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer() 
    .setInputCols("sentence") 
    .setOutputCol("token")

val dod_contextual_parser = ContextualParserModel.pretrained("date_of_death_parser", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("chunk_dod") 

val chunk_converter = new ChunkConverter() 
    .setInputCols(Array("chunk_dod")) 
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        dod_contextual_parser,
        chunk_converter
        ))

val data = Seq(Array("""
Record date : 2081-01-04 
DB : 11.04.1962
DT : 12-03-1978 
DOD : 10.25.23 

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988. 

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""
)).toDS.toDF("text")

val result = parserPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------+------------------+-----+---+---------+
|sentence_id|chunk             |begin|end|ner_label|
+-----------+------------------+-----+---+---------+
|3          |10.25.23          |64   |71 |DOD      |
|5          |September 25, 2007|360  |377|DOD      |
+-----------+------------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_of_death_parser|
|Compatibility:|Healthcare NLP 5.1.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[chunk_dod]|
|Language:|en|
|Size:|5.0 KB|
|Case sensitive:|false|
