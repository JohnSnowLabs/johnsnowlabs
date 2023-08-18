---
layout: model
title: Text-to-SQL Generation (MIMICSQL)
author: John Snow Labs
name: text2sql_mimicsql
date: 2023-08-14
tags: [licensed, text2sql, medicaltextgeneration, medicalquestionanswering, clinical, en, tensorflow]
task: Table Question Answering
language: en
edition: Healthcare NLP 5.0.1
spark_version: 3.0
supported: true
engine: tensorflow
annotator: Text2SQL
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can generate SQL queries from natural questions. It is based on a small-size LLM, which is finetuned by John Snow Labs on a dataset having a schema with the same schema that MIMIC-III has.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text2sql_mimicsql_en_5.0.1_3.0_1692034266037.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text2sql_mimicsql_en_5.0.1_3.0_1692034266037.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python
document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text2sql = Text2SQL.pretrained("text2sql_mimicsql", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sql")

pipeline = Pipeline(stages=[
    document_assembler,
    text2sql 
])

text = "Calulate the total number of patients who had icd9 code 5771"
data = spark.createDataFrame([[text]]).toDF("text")

pipeline = Pipeline(stages=[document_assembler, text2sql])
result= pipeline.fit(data).transform(data)

```
```scala
val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val text2sql = new Text2SQL.pretrained("text2sql_mimicsql", "en", "clinical/models")
    .setInputCols(["document"])
    .setOutputCol("sql")

val pipeline = new Pipeline().setStages(Array(document_assembler, text2sql ))

val text = """Calulate the total number of patients who had icd9 code 5771"""

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)




```
</div>

## Results

```bash
[
SELECT COUNT ( DISTINCT DEMOGRAPHIC."SUBJECT_ID" )
FROM DEMOGRAPHIC
INNER JOIN PROCEDURES on DEMOGRAPHIC.HADM_ID = PROCEDURES.HADM_ID
WHERE PROCEDURES."ICD9_CODE" = "5771"
]
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text2sql_mimicsql|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.0 GB|
