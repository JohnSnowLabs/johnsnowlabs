---
layout: model
title: Mapping Entities with Corresponding ATC Codes
author: John Snow Labs
name: atc_mapper
date: 2026-07-30
tags: [en, chunk_mapper, licensed, clinical, atc]
task: Chunk Mapping
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: ChunkMapperModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps drug entities extracted from clinical text to their corresponding ATC (Anatomic Therapeutic Chemical) codes. It uses ner_posology for drug entity recognition and provides fast code mapping without requiring embeddings at inference time. Trained on the WHO ATC-DDD dataset (release 2026-04-25).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/atc_mapper_en_6.4.1_3.4_1785445723495.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/atc_mapper_en_6.4.1_3.4_1785445723495.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner_posology = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

atc_mapper = ChunkMapperModel.pretrained("atc_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["atc_code"])

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_converter, atc_mapper
])
data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

ner_posology = medical.NerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

atc_mapper = medical.ChunkMapperModel.pretrained("atc_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["atc_code"])

pipeline = nlp.Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_converter, atc_mapper
])
data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val nerPosology = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val atcMapper = ChunkMapperModel.pretrained("atc_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("atc_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, wordEmbeddings,
    nerPosology, nerConverter, atcMapper
))

val data = Seq("The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk    | atc_code   |
|:-------------|:-----------|
| metformin    | A10BA02    |
| atorvastatin | C10AA05    |
| amoxicillin  | J01CA04    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|atc_mapper|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|811.0 KB|