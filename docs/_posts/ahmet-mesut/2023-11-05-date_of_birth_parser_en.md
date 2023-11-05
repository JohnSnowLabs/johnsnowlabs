---
layout: model
title: Date of Brith Contextual Parser Model
author: John Snow Labs
name: date_of_birth_parser
date: 2023-11-05
tags: [licensed, en, clinical, contextual_parser, date_of_birth, dob]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.0.2
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a `ContextualParserModel` that can extract date-of-birth (DOB) entities in clinical texts

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/date_of_birth_parser_en_5.0.2_3.0_1699188001566.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/date_of_birth_parser_en_5.0.2_3.0_1699188001566.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

dob_contextual_parser = ContextualParserModel.pretrained("date_of_birth_parser", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_dob") 

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_dob"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        dob_contextual_parser,
    chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """
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

val dob_contextual_parser = ContextualParserModel.pretrained("date_of_birth_parser", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("chunk_dob")

val chunk_converter = new ChunkConverter() \
    .setInputCols(["chunk_dob"]) \
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        dob_contextual_parser,
        chunk_converter
        ))

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

val result = model.transform(spark.createDataFrame([["""
Record date : 2081-01-04 
DB : 11.04.1962
DT : 12-03-1978 
DOD : 10.25.23 

SOCIAL HISTORY:
She was born on Nov 04, 1962 in London and got married on 04/05/1979. When she got pregnant on 15 May 1079, the doctor wanted to verify her DOB was November 4, 1962. Her date of birth was confirmed to be 11-04-1962, the patient is 45 years old on 25 Sep 2007.

PROCEDURES:
Patient was evaluated on 1988-03-15 for allergies. She was seen by the endocrinology service and she was discharged on 9/23/1988. 

MEDICATIONS
1. Coumadin 1 mg daily. Last INR was on August 14, 2007, and her INR was 2.3."""]]).toDF("text"))
```
</div>

## Results

```bash
+-----------+----------------+-----+---+---------+
|sentence_id|chunk           |begin|end|ner_label|
+-----------+----------------+-----+---+---------+
|1          |11.04.1962      |31   |40 |DOB      |
|3          |Nov 04, 1962    |107  |118|DOB      |
|4          |November 4, 1962|239  |254|DOB      |
|5          |11-04-1962      |295  |304|DOB      |
+-----------+----------------+-----+---+---------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|date_of_birth_parser|
|Compatibility:|Healthcare NLP 5.0.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[chunk_dob]|
|Language:|en|
|Size:|4.9 KB|
|Case sensitive:|false|
