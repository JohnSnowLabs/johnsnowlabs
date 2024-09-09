---
layout: model
title: ZIP Code Contextual Parser Model
author: John Snow Labs
name: zip_parser
date: 2024-09-09
tags: [en, clinical, licensed, contextualparser, zip]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.4.1
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model, extracts ZIP code entities from clinical texts.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/zip_parser_en_5.4.1_3.0_1725875840810.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/zip_parser_en_5.4.1_3.0_1725875840810.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

zip_contextual_parser = ContextualParserModel.pretrained("zip_parser", "en", "clinical/models") \
    .setInputCols(["sentence", "token"]) \
    .setOutputCol("chunk_zip") 

chunk_converter = ChunkConverter() \
    .setInputCols(["chunk_zip"]) \
    .setOutputCol("ner_chunk")

parserPipeline = Pipeline(stages=[
        document_assembler,
        sentence_detector,
        tokenizer,
        zip_contextual_parser,
        chunk_converter
        ])

model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))

sample_text = """John Doe lives at 1234 Maple Street, Springfield, IL 62704. He works at 5678 Oak Avenue, Austin, TX 73301. His previous address was 4321 Pine Street, Los Angeles, CA 90001. His cousin Jane lives at 7890 Elm Street, Chicago, IL 60614."""

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

val zip_cp.json_contextual_parser = ContextualParserModel.pretrained("zip_parser", "en", "clinical/models") 
    .setInputCols(Array("sentence", "token")) 
    .setOutputCol("chunk_zip") 

val chunk_converter = new ChunkConverter() 
    .setInputCols(Array("chunk_zip")) 
    .setOutputCol("ner_chunk")

val parserPipeline = new Pipeline().setStages(Array(
        document_assembler,
        sentence_detector,
        tokenizer,
        zip_contextual_parser,
        chunk_converter
        ))

val data = Seq(Array("""John Doe lives at 1234 Maple Street, Springfield, IL 62704. He works at 5678 Oak Avenue, Austin, TX 73301. His previous address was 4321 Pine Street, Los Angeles, CA 90001. His cousin Jane lives at 7890 Elm Street, Chicago, IL 60614.""")).toDS.toDF("text")

val result = parserPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----+-----+---+-----+
|chunk|begin|end|label|
+-----+-----+---+-----+
|62704|53   |57 |ZIP  |
|73301|100  |104|ZIP  |
|90001|166  |170|ZIP  |
|60614|227  |231|ZIP  |
+-----+-----+---+-----+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|zip_parser|
|Compatibility:|Healthcare NLP 5.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[entity_zip_code]|
|Language:|en|
|Size:|5.8 KB|
|Case sensitive:|false|
