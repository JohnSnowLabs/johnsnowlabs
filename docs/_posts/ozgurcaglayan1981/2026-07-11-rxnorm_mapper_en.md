---
layout: model
title: Mapping Entities with Corresponding RxNorm Codes
author: John Snow Labs
name: rxnorm_mapper
date: 2026-07-11
tags: [en, chunk_mapper, licensed, clinical, rxnorm]
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

This model maps drug entities to their corresponding RxNorm codes. It provides fast and accurate drug code mapping without requiring embeddings at inference time.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_en_6.4.0_3.4_1783797770549.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/rxnorm_mapper_en_6.4.0_3.4_1783797770549.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

rxnorm_mapper = ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["rxnorm_code"])

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_posology_converter, rxnorm_mapper
])
data = spark.createDataFrame([["The patient's medication list was reviewed and updated to include Lisinopril 20 MG Oral Tablet for hypertension, Atorvastatin 20 MG Oral Tablet for hyperlipidemia, and Metoprolol Tartrate 25 MG Oral Tablet for rate control. She was also continued on Insulin Glargine 100 UNT/ML Injectable Solution for type 2 diabetes, started on Omeprazole 20 MG Delayed Release Oral Capsule for reflux symptoms, and given Amoxicillin 500 MG Oral Capsule for a bacterial sinus infection."]]).toDF("text")
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

rxnorm_mapper = medical.ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["rxnorm_code"])

pipeline = nlp.Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_posology, ner_posology_converter, rxnorm_mapper
])
data = spark.createDataFrame([["The patient's medication list was reviewed and updated to include Lisinopril 20 MG Oral Tablet for hypertension, Atorvastatin 20 MG Oral Tablet for hyperlipidemia, and Metoprolol Tartrate 25 MG Oral Tablet for rate control. She was also continued on Insulin Glargine 100 UNT/ML Injectable Solution for type 2 diabetes, started on Omeprazole 20 MG Delayed Release Oral Capsule for reflux symptoms, and given Amoxicillin 500 MG Oral Capsule for a bacterial sinus infection."]]).toDF("text")
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

val rxnormMapper = ChunkMapperModel.pretrained("rxnorm_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("rxnorm_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, wordEmbeddings,
    nerPosology, nerPosologyConverter, rxnormMapper
))

val data = Seq("The patient's medication list was reviewed and updated to include Lisinopril 20 MG Oral Tablet for hypertension, Atorvastatin 20 MG Oral Tablet for hyperlipidemia, and Metoprolol Tartrate 25 MG Oral Tablet for rate control. She was also continued on Insulin Glargine 100 UNT/ML Injectable Solution for type 2 diabetes, started on Omeprazole 20 MG Delayed Release Oral Capsule for reflux symptoms, and given Amoxicillin 500 MG Oral Capsule for a bacterial sinus infection.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                                       |   rxnorm_code |
|:------------------------------------------------|--------------:|
| Lisinopril 20 MG Oral Tablet                    |        314077 |
| Atorvastatin 20 MG Oral Tablet                  |        617310 |
| Metoprolol Tartrate 25 MG Oral Tablet           |        866924 |
| Insulin Glargine 100 UNT/ML Injectable Solution |        311041 |
| Omeprazole 20 MG Delayed Release Oral Capsule   |        198051 |
| Amoxicillin 500 MG Oral Capsule                 |        308191 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|rxnorm_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|20.6 MB|