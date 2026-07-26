---
layout: model
title: Mapping Entities with Corresponding NDC Codes
author: John Snow Labs
name: ndc_mapper
date: 2026-07-26
tags: [en, chunk_mapper, licensed, clinical, ndc]
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

This model maps drug entities extracted from clinical text to their corresponding National Drug Codes (NDC). It uses ner_posology_greedy for drug entity recognition and provides fast code mapping without requiring embeddings at inference time. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ndc_mapper_en_6.4.0_3.4_1785090677195.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ndc_mapper_en_6.4.0_3.4_1785090677195.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_posology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("posology_ner")

ner_posology_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "posology_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

ndc_mapper = ChunkMapperModel.pretrained("ndc_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ndc_code"])

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_posology_converter, ndc_mapper
])
data = spark.createDataFrame([["She was started on amoxicillin 500 mg three times daily for a bacterial sinus infection, continues aspirin 81 mg once daily for cardiovascular prophylaxis, takes acetaminophen 500 mg as needed for pain, and was also prescribed cetirizine hydrochloride 10 mg once daily for seasonal allergies."]]).toDF("text")
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

ner_posology = medical.NerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("posology_ner")

ner_posology_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "posology_ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

ndc_mapper = medical.ChunkMapperModel.pretrained("ndc_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ndc_code"])

pipeline = nlp.Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_posology_converter, ndc_mapper
])
data = spark.createDataFrame([["She was started on amoxicillin 500 mg three times daily for a bacterial sinus infection, continues aspirin 81 mg once daily for cardiovascular prophylaxis, takes acetaminophen 500 mg as needed for pain, and was also prescribed cetirizine hydrochloride 10 mg once daily for seasonal allergies."]]).toDF("text")
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

val nerPosology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("posology_ner")

val nerPosologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "posology_ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val ndcMapper = ChunkMapperModel.pretrained("ndc_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("ndc_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, wordEmbeddings,
    nerPosology, nerPosologyConverter, ndcMapper
))

val data = Seq("She was started on amoxicillin 500 mg three times daily for a bacterial sinus infection, continues aspirin 81 mg once daily for cardiovascular prophylaxis, takes acetaminophen 500 mg as needed for pain, and was also prescribed cetirizine hydrochloride 10 mg once daily for seasonal allergies.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                      | ndc_code   |
|:-------------------------------|:-----------|
| amoxicillin 500 mg             | 83112-0500 |
| aspirin 81 mg                  | 41250-0780 |
| acetaminophen 500 mg           | 69618-0011 |
| cetirizine hydrochloride 10 mg | 66424-0564 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ndc_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|8.3 MB|
