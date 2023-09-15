---
layout: model
title: Text-to-SQL Generation (Custom_DB_Schema_Single_Table_Augmented)
author: John Snow Labs
name: text2sql_with_schema_single_table_augmented
date: 2023-09-15
tags: [licensed, text2sql, onnx, custom_database_schema, single_table, augmented_dataset, en, tensorflow]
task: Table Question Answering
language: en
edition: Healthcare NLP 5.1.0
spark_version: 3.0
supported: true
engine: tensorflow
annotator: Text2SQL
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model can generate SQL queries from natural questions and custom database schemas with a single table. It is based on a large-size LLM, which is finetuned by John Snow Labs on an augmented dataset having schemas with single tables.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/text2sql_with_schema_single_table_augmented_en_5.1.0_3.0_1694798119772.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/text2sql_with_schema_single_table_augmented_en_5.1.0_3.0_1694798119772.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}

```python
question = "What is the average age of male patients with 'Diabetes'?"
query_schema = {
    "medical_treatment": ["patient_id","patient_name","age","gender","diagnosis","treatment","doctor_name","hospital_name","admission_date","discharge_date"]
}


document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

text2sql_with_schema_single_table_augmented = Text2SQL.pretrained("text2sql_with_schema_single_table_augmented", "en", "clinical/models")\
    .setMaxNewTokens(200)\
    .setSchema(query_schema)\
    .setInputCols(["document"])\
    .setOutputCol("sql")


pipeline = Pipeline(stages=[document_assembler, text2sql_with_schema_single_table_augmented ])

data = spark.createDataFrame([[question]]).toDF("text")

pipeline.fit(data)\
        .transform(data)\
        .select("sql.result")\
        .show(truncate=False)
```
```scala
val question = """What is the average age of male patients with 'Diabetes'? """
val query_schema : Map[String, List[String]] = Map(
    "medical_treatment" -> List("patient_id","patient_name","age","gender","diagnosis","treatment","doctor_name","hospital_name","admission_date","discharge_date")
  )

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val text2sql_with_schema_single_table_augmented = new Text2SQL.pretrained("text2sql_with_schema_single_table_augmented", "en", "clinical/models")
    .setMaxNewTokens(200)
    .setSchema(query_schema)
    .setInputCols(["document"])
    .setOutputCol("sql")

val pipeline = new Pipeline().setStages(Array(document_assembler, text2sql_with_schema_single_table_augmented ))

val data = Seq(Array(text)).toDS.toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
[SELECT AVG(age) FROM medical_treatment WHERE gender = 'male' AND diagnosis = 'diabetes']
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|text2sql_with_schema_single_table_augmented|
|Compatibility:|Healthcare NLP 5.1.0+|
|License:|Licensed|
|Edition:|Official|
|Language:|en|
|Size:|3.1 GB|
