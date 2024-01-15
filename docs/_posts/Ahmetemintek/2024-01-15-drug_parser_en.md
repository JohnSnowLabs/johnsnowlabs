---
layout: model
title: Drug Contextual Parser Model
author: John Snow Labs
name: drug_parser
date: 2024-01-15
tags: [en, clinical, contextual_parser, drug, licensed]
task: Contextual Parser
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: ContextualParserModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model is a `ContextualParserModel` that can extract drug entities in clinical texts.

## Predicted Entities

`drug`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.2.Contextual_Parser_Rule_Based_NER.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/drug_parser_en_5.2.1_3.0_1705323093457.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/drug_parser_en_5.2.1_3.0_1705323093457.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
document_assembler = DocumentAssembler() \
     .setInputCol("text") \
     .setOutputCol("document")

 sentence_detector = SentenceDetector() \
     .setInputCols(["document"]) \
     .setOutputCol("sentence")

 tokenizer = Tokenizer() \
     .setInputCols(["sentence"]) \
     .setOutputCol("token")

 contextual_parser = ContextualParserModel.pretrained("drug_parser", "en", "clinical/models")\
     .setInputCols(["sentence", "token"]) \
     .setOutputCol("cp_output")\
     .setCaseSensitive(False)

 chunk_converter = ChunkConverter() \
    .setInputCols(["cp_output"]) \
    .setOutputCol("ner_chunk")

 parserPipeline = Pipeline(stages=[
     document_assembler,
     sentence_detector,
     tokenizer,
     contextual_parser,
     chunk_converter
     ])

 sample_text = """ Patient is prescribed Lescol 40 MG, Zydol 1.5 mg tablet and Furtulon. The other patient is given Acetafen and  Citalon"""

 model = parserPipeline.fit(spark.createDataFrame([[""]]).toDF("text"))
 result = model.transform(spark.createDataFrame([[sample_text]]).toDF("text"))
```
```scala
val document_assembler = new DocumentAssembler() 
     .setInputCol("text") 
     .setOutputCol("document")

 val sentence_detector = new SentenceDetector()
     .setInputCols("document")
     .setOutputCol("sentence")

 val tokenizer = new Tokenizer() 
     .setInputCols("sentence") 
     .setOutputCol("token")

 val contextual_parser = ContextualParserModel.pretrained("drug_parser", "en", "clinical/models") 
     .setInputCols(Array("sentence", "token")) 
     .setOutputCol("cp_output") 

 val chunk_converter = new ChunkConverter() 
     .setInputCols(Array("cp_output")) 
     .setOutputCol("ner_chunk")

 val parserPipeline = new Pipeline().setStages(Array(
         document_assembler,
         sentence_detector,
         tokenizer,
         contextual_parser,
         chunk_converter
         ))

 val data = Seq(Array("""Patient is prescribed Lescol 40 MG, Zydol 1.5 mg tablet and Furtulon. The other patient is given Acetafen and  Citalon""")).toDS.toDF("text")

 val result = parserPipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------+-----+---+----------+
 |sentence_id|begin|end|drug_chunk|
 +-----------+-----+---+----------+
 |0          |22   |27 |Lescol    |
 |0          |36   |40 |Zydol     |
 |0          |60   |67 |Furtulon  |
 |1          |97   |104|Acetafen  |
 |1          |110  |116|Citalon   |
 +-----------+-----+---+----------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|drug_parser|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence, token]|
|Output Labels:|[cp_output]|
|Language:|en|
|Size:|1.1 MB|
|Case sensitive:|false|

## References

This model was trained with the data from https://pillintrip.com