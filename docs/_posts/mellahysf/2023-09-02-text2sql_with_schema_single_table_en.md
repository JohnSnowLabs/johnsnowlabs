---
layout: model
title: Text-to-SQL Generation (Custom_DB_Schema_Single_Table)
author: John Snow Labs
name: text2sql_with_schema_single_table
date: 2023-09-02
tags: [licensed, text2sql, onnx, custom_database_schema, single_table, en, tensorflow]
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

This model can generate SQL queries from natural questions and custom database schemas with a single table. It is based on a large-size LLM, which is finetuned by John Snow Labs on a dataset having schemas with single tables.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text2sql_with_schema_single_table_en_5.0.1_3.0_1693675589556.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text2sql_with_schema_single_table_en_5.0.1_3.0_1693675589556.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
question = "Calculate the average age of patients with blood type 'A-' "
query_schema = {  
    "patient": ["ID","Name","Age","Gender","BloodType","Weight","Height","Address","Email","Phone"]
}

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text2sql_with_schema_single_table = Text2SQL.pretrained("text2sql_with_schema_single_table", "en", "clinical/models")\
    .setMaxNewTokens(200)\
    .setSchema(query_schema)\
    .setInputCols(["document"])\
    .setOutputCol("sql")


pipeline = Pipeline(stages=[document_assembler, text2sql_with_schema_single_table])

data = spark.createDataFrame([[question]]).toDF("text")

pipeline.fit(data)\
        .transform(data)\
        .select("sql.result")\
        .show(truncate=False)
```
```scala
val question = """Calculate the average age of patients with blood type 'A-' """
val query_schema : Map[String, List[String]] = Map(
    "patient" -> List("ID", "Name", "Age", "Gender", "BloodType", "Weight", "Height", "Address", "Email", "Phone")
  )

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val text2sql_with_schema_single_table = new Text2SQL.pretrained("text2sql_with_schema_single_table", "en", "clinical/models")
    .setMaxNewTokens(200)
    .setSchema(query_schema)
    .setInputCols(["document"])
    .setOutputCol("sql")

val pipeline = new Pipeline().setStages(Array(document_assembler, text2sql_with_schema_single_table ))

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
[SELECT AVG(Age) FROM patient WHERE BloodType = "A-"]

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text2sql_with_schema_single_table|
|Compatibility:|Healthcare NLP 5.0.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document_question]|
|Output Labels:|[sql_query]|
|Language:|en|
|Size:|3.0 GB|