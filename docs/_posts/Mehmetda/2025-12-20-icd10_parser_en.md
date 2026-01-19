---
layout: model
title: ICD10 Contextual Parser Model
author: John Snow Labs
name: icd10_parser
date: 2025-12-20
tags: [en, contextualparser, licensed, clinical, icd10]
task: Contextual Parser
language: en
edition: Healthcare NLP 6.2.2
spark_version: 3.4
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts icd10 entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/icd10_parser_en_6.2.2_3.0_1766261208910.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/icd10_parser_en_6.2.2_3.0_1766261208910.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ıcd10_contextualparser = ContextualParserModel.pretrained("icd10_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_ıcd_10") 

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_ıcd_10"])\
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        ıcd10_contextualparser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A. 
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""

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

ıcd10_contextualparser = medical.ContextualParserModel.pretrained("icd10_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_ıcd_10") 

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_ıcd_10"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        ıcd10_contextualparser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A. 
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""

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

val ıcd10_contextualparser = ContextualParserModel.pretrained("icd10_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_ssn") 

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_ıcd-10")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        ıcd10_contextualparser,
        chunk_converter
))

val sample_text = """A . Record date: 2093-01-13, date: 2093-01-13, DATE: 2093-01-13, David Hale, M.D. IP: 203.120.223.13. ID: 1231511863, Des Moines AL 50129-4444, The driver's license no: A334455B. the SSN:324598674 and e-mail: hale@gmail.com. Name : Hendrickson, Ora MR. # 719435 Date : 01/13/93. PCP : Oliveira, 25 years-old. Record date : 2079-11-09, Cocke County Baptist Hospital. 0295 Keats Street. Phone (302) 786-5227.
Mine is SSN#332255677, The other is ssN: 333-44-6666. the rest ssn:  212-33-4444. his is sSN : 345-33-5666, HER is ssn 332233445.
me again ssn 223344556, Their SSN: 234-44-3333. MY dln# D08954796. your DLN : AB773955A. 
Social Security no: 445-66-4432. Patient's VIN : 1HGBH41JXMN109286. Molina Cortes, Alvaro, MD. MRN: 1482926 from GE Healthcare. Primary diagnosis: E11.9 for type 2 diabetes mellitus.
His personal IP: 2001:db8:85a3:8d3:1319:8a2e:370:7348. the patient's ssns: 333224444. my account number is 123456789. your routing 44334456. Secondary diagnosis code I10 indicates essential hypertension.
account#3344556677. his bank no: 334455667788. Patient's Vehicle Identifiers: 1HGBH41JXMN109286. my VIN# 1dddd41JXMN109286. our vehicle id no: 1HGBH41JXMN109286. The patient also has chronic kidney disease coded as N18.3.
his aba is 3445-6543-2. sample bankrouting: 23443245. Final billing diagnosis was J45.909 for asthma without complications."""


val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)


```
</div>

## Results

```bash


| chunk    |   begin |   end | label   |
|:---------|--------:|------:|:--------|
| A334455B |     169 |   176 | ICD_10  |
| E11.9    |     774 |   778 | ICD_10  |
| I10      |     976 |   978 | ICD_10  |
| N18.3    |    1229 |  1233 | ICD_10  |
| J45.909  |    1318 |  1324 | ICD_10  |



```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icd10_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_icd10]|
|Language:|en|
|Size:|4.2 KB|
|Case sensitive:|true|
