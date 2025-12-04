---
layout: model
title: Mapping Entities with Corresponding RxNorm Codes
author: John Snow Labs
name: rxnorm_mapper
date: 2025-12-04
tags: [mapper, rxnorm, en, licensed, clinical, chunk_mapper]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps drug entities to their corresponding RxNorm codes. It provides fast and accurate drug code mapping without requiring embeddings.

## Predicted Entities

`RxNorm Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_en_6.2.0_3.4_1764808728293.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_en_6.2.0_3.4_1764808728293.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_posology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("posology_ner")

ner_posology_converter = NerConverterInternal()\
    .setInputCols("sentence", "token", "posology_ner")\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

rxnorm_mapper = ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["rxnorm_code"])

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_posology,
    ner_posology_converter,
    rxnorm_mapper
])

text = """The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief."""

data = spark.createDataFrame([[text]]).toDF("text")

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
    .setInputCols("sentence")\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_posology = medical.MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("posology_ner")

ner_posology_converter = medical.NerConverterInternal()\
    .setInputCols("sentence", "token", "posology_ner")\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

rxnorm_mapper = medical.ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["rxnorm_code"])

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_posology,
    ner_posology_converter,
    rxnorm_mapper
])

text = """The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = new SentenceDetector()
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerPosology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("posology_ner")

val nerPosologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "posology_ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val rxnormMapper = ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("rxnorm_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerPosology,
    nerPosologyConverter,
    rxnormMapper
))

val data = Seq("""The patient reported persistent musculoskeletal discomfort, for which ibuprofen topical cream was initiated. Due to concurrent scalp irritation, selenium sulfide 25 mg/ml was also prescribed, and salicylamide 250 mg was added for additional symptomatic relief.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|ner_chunk                |mapping_result|
|-------------------------|--------------|
|ibuprofen topical cream  |377732        |
|selenium sulfide 25 mg/ml|328880        |
|salicylamide 250 mg      |316651        |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_mapper|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|10.4 MB|
