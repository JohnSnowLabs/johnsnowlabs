---
layout: model
title: Account Number Contextual Parser Model
author: John Snow Labs
name: account_parser
date: 2025-12-21
tags: [en, contextualparser, licensed, clinical, account]
task: Contextual Parser
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts account number entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/account_parser_en_6.2.2_3.0_1766305725986.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/account_parser_en_6.2.2_3.0_1766305725986.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python


document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

account_contextual_parser = ContextualParserModel.pretrained("account_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_account")

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_account"])\
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        account_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments."""

result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))




```

{:.jsl-block}
```python


document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

account_contextual_parser = medical.ContextualParserModel.pretrained("account_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_account")

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_account"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        account_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments."""

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

val account_contextual_parser = ContextualParserModel.pretrained("account_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_account")

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_account")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        account_contextual_parser,
        chunk_converter
))

sample_text = """Name : Hendrickson, Ora, Record date: 2093-01-13, # 719435.
Dr. John Green, ID: 1231511863, IP 203.120.223.13. account: 1234567890120 route number: 123567
He is a 60-year-old male was admitted to the Day Hospital for cystectomy on 01/13/93.
Patient's VIN : 1HGBH41JXMN109286, SSN #333-44-6666, Driver's license no:A334455B.
Phone (302) 786-5227, 0295 Keats Street, San Francisco, E-MAIL: smith@gmail.com.
Additional account: 9876543210987 for billing purposes.
Secondary account number: 4567890123456 linked to insurance.
Backup account: 7890123456789 for emergency payments."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)


```
</div>

## Results

```bash


|         chunk |   begin |   end | label   |
|--------------:|--------:|------:|:--------|
| 1234567890120 |     120 |   132 | ACCOUNT |
|        123567 |     148 |   153 | ACCOUNT |
| 9876543210987 |     425 |   437 | ACCOUNT |
| 4567890123456 |     487 |   499 | ACCOUNT |
| 7890123456789 |     538 |   550 | ACCOUNT |



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|account_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_account]|
|Language:|en|
|Size:|4.4 KB|
|Case sensitive:|false|
