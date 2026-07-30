---
layout: model
title: Mapping Entities with Corresponding CPT Codes
author: John Snow Labs
name: cpt_mapper
date: 2026-07-16
tags: [en, chunk_mapper, licensed, clinical, cpt]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities (procedures, tests, treatments) to their corresponding CPT codes without requiring embeddings for accurate procedural code mapping. 

Training data: current CPT data, further augmented by John Snow Labs for broader coverage. 

CPT mapper models are removed from the Models Hub due to license restrictions and can only be shared with users who already have a valid CPT license. Please contact support@johnsnowlabs.com for access.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("jsl_ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "jsl_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Procedure', 'Test', 'Treatment', 'Clinical_Dept'])

cpt_mapper = ChunkMapperModel.load("cpt_mapper")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["cpt_code"])\
    .setLowerCase(True)

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_jsl, ner_converter, cpt_mapper
])
data = spark.createDataFrame([["The patient underwent an episiotomy during delivery, pulse oximetry was monitored throughout, and later required a blood transfusion due to postpartum hemorrhage."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetector()\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("jsl_ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "jsl_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(['Procedure', 'Test', 'Treatment', 'Clinical_Dept'])

cpt_mapper = medical.ChunkMapperModel.load("cpt_mapper")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["cpt_code"])\
    .setLowerCase(True)

pipeline = nlp.Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_jsl, ner_converter, cpt_mapper
])
data = spark.createDataFrame([["The patient underwent an episiotomy during delivery, pulse oximetry was monitored throughout, and later required a blood transfusion due to postpartum hemorrhage."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("jsl_ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "jsl_ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test", "Treatment", "Clinical_Dept"))

val cptMapper = ChunkMapperModel.load("cpt_mapper")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("cpt_code"))
    .setLowerCase(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, wordEmbeddings,
    nerJsl, nerConverter, cptMapper
))

val data = Seq("The patient underwent an episiotomy during delivery, pulse oximetry was monitored throughout, and later required a blood transfusion due to postpartum hemorrhage.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk         |   cpt_code |
|:------------------|-----------:|
| episiotomy        |      59300 |
| pulse oximetry    |      94760 |
| blood transfusion |      36430 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|cpt_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|5.2 MB|
