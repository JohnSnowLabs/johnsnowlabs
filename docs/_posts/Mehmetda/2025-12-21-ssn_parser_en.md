---
layout: model
title: SSN Number Contextual Parser Model
author: John Snow Labs
name: ssn_parser
date: 2025-12-21
tags: [en, contextualparser, licensed, clinical, ssn]
task: Entity Resolution
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

This model, extracts SSN number entities from clinical texts.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ssn_parser_en_6.2.2_3.0_1766302712247.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ssn_parser_en_6.2.2_3.0_1766302712247.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ssn_contextual_parser = ContextualParserModel.pretrained("ssn_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_ssn") 

chunk_converter = ChunkConverter()\
    .setInputCols(["chunk_ssn"])\
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        ssn_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))


sample_text = """San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

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

ssn_contextual_parser = medical.ContextualParserModel.pretrained("ssn_parser","en","clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("chunk_ssn") 

chunk_converter = medical.ChunkConverter()\
    .setInputCols(["chunk_ssn"])\
    .setOutputCol("ner_chunk")

parserPipeline = nlp.Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        ssn_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))


sample_text = """San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

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

val ssn_contextual_parser = ContextualParserModel.pretrained("ssn_parser","en","clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("chunk_ssn") 

val chunk_converter = new ChunkConverter()
    .setInputCols("chunk_ssn")
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        ssn_contextual_parser,
        chunk_converter
))


val sample_text = """San Diego, CA, USA
Email: medunites@firsthospital.com
Patient John Davies, 62 y.o. ssn: 023-92-7136 was discharged after 12 hours of monitoring without any signs of internal damage.
TSICU Admission 65332 on 24/06/2019 by ambulance VIN 4Y1SL65848Z411439
Patient Mary Smith, 45 y.o. ssn: 456-78-9012 was admitted for routine checkup on 25/06/2019.
Patient Robert Johnson, 38 y.o. ssn: 789-12-3456 underwent surgery on 26/06/2019.
Patient Sarah Williams, 55 y.o. ssn: 234-56-7890 was treated in emergency room on 27/06/2019.
Patient Michael Brown, 41 y.o. ssn: 567-89-0123 was released after observation on 28/06/2019."""

val data = Seq(sample_text).toDF("text")

val results = parserPipeline.fit(data).transform(data)


```
</div>

## Results

```bash


| chunk       |   begin |   end | label   |
|:------------|--------:|------:|:--------|
| 023-92-7136 |      88 |    98 | SSN     |
| 456-78-9012 |     286 |   296 | SSN     |
| 789-12-3456 |     383 |   393 | SSN     |
| 234-56-7890 |     465 |   475 | SSN     |
| 567-89-0123 |     558 |   568 | SSN     |




```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ssn_parser|
|Compatibility:|Healthcare NLP 6.2.2+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token_doc]|
|Output Labels:|[entity_ssn]|
|Language:|en|
|Size:|4.4 KB|
|Case sensitive:|false|