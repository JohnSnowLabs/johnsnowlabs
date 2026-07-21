---
layout: model
title: Mapping Phenotype Entities with Corresponding HPO Codes
author: John Snow Labs
name: hpo_mapper
date: 2026-07-20
tags: [en, chunk_mapper, licensed, clinical, hpo]
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

This model maps extracted phenotype entities from clinical or biomedical text to their corresponding Human Phenotype Ontology (HPO) codes, standardizing observed symptoms, signs, and clinical abnormalities using HPO terminology. It also returns all possible matching codes for ambiguous surface forms in the `all_k_resolutions` metadata field. Trained on the Human Phenotype Ontology (HPO) 2026-06-23 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_en_6.4.0_3.4_1784589687417.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/hpo_mapper_en_6.4.0_3.4_1784589687417.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = StopWordsCleaner()\
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)

token_assembler = TokenAssembler()\
    .setInputCols(["document", "cleanTokens"])\
    .setOutputCol("cleanTokens_newDoc")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["cleanTokens_newDoc"])\
    .setOutputCol("sentence")

tokenizer_2 = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("clean_tokens")

hpo_matcher = TextMatcherInternalModel().pretrained("hpo_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "clean_tokens"])\
    .setOutputCol("hpo_term")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

hpo_mapper = ChunkMapperModel().pretrained("hpo_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_term"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(True)

pipeline = Pipeline(stages=[
    document_assembler, tokenizer, stopwords_cleaner, token_assembler,
    sentence_detector, tokenizer_2, hpo_matcher, hpo_mapper
])
data = spark.createDataFrame([["The patient presents with memory impairment and seizures. Physical exam notable for microcephaly and low-set ears. Cardiac evaluation revealed a ventricular septal defect. The patient was diagnosed with ASD."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["document"])\
    .setOutputCol("token")

stopwords_cleaner = nlp.StopWordsCleaner()\
    .setInputCols("token")\
    .setOutputCol("cleanTokens")\
    .setCaseSensitive(False)

token_assembler = nlp.TokenAssembler()\
    .setInputCols(["document", "cleanTokens"])\
    .setOutputCol("cleanTokens_newDoc")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["cleanTokens_newDoc"])\
    .setOutputCol("sentence")

tokenizer_2 = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("clean_tokens")

hpo_matcher = medical.TextMatcherInternalModel().pretrained("hpo_matcher", "en", "clinical/models")\
    .setInputCols(["sentence", "clean_tokens"])\
    .setOutputCol("hpo_term")\
    .setCaseSensitive(False)\
    .setMergeOverlapping(False)

hpo_mapper = medical.ChunkMapperModel().pretrained("hpo_mapper", "en", "clinical/models")\
    .setInputCols(["hpo_term"])\
    .setOutputCol("hpo_code")\
    .setLowerCase(True)

pipeline = nlp.Pipeline(stages=[
    document_assembler, tokenizer, stopwords_cleaner, token_assembler,
    sentence_detector, tokenizer_2, hpo_matcher, hpo_mapper
])
data = spark.createDataFrame([["The patient presents with memory impairment and seizures. Physical exam notable for microcephaly and low-set ears. Cardiac evaluation revealed a ventricular septal defect. The patient was diagnosed with ASD."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document")
    .setOutputCol("token")

val stopwordsCleaner = new StopWordsCleaner()
    .setInputCols("token")
    .setOutputCol("cleanTokens")
    .setCaseSensitive(false)

val tokenAssembler = new TokenAssembler()
    .setInputCols(Array("document", "cleanTokens"))
    .setOutputCol("cleanTokens_newDoc")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("cleanTokens_newDoc"))
    .setOutputCol("sentence")

val tokenizer2 = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("clean_tokens")

val hpoMatcher = TextMatcherInternalModel
    .pretrained("hpo_matcher", "en", "clinical/models")
    .setInputCols(Array("sentence", "clean_tokens"))
    .setOutputCol("hpo_term")
    .setCaseSensitive(false)
    .setMergeOverlapping(false)

val hpoMapper = ChunkMapperModel
    .pretrained("hpo_mapper", "en", "clinical/models")
    .setInputCols("hpo_term")
    .setOutputCol("hpo_code")
    .setLowerCase(true)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, tokenizer, stopwordsCleaner, tokenAssembler,
    sentenceDetector, tokenizer2, hpoMatcher, hpoMapper
))

val data = Seq("The patient presents with memory impairment and seizures. Physical exam notable for microcephaly and low-set ears. Cardiac evaluation revealed a ventricular septal defect. The patient was diagnosed with ASD.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                     | hpo_code   | all_k_resolutions       |
|:--------------------------|:-----------|:------------------------|
| memory impairment         | HP:0002354 | HP:0002354:::           |
| seizures                  | HP:0001250 | HP:0001250:::           |
| microcephaly              | HP:0000252 | HP:0000252:::           |
| low-set ears              | HP:0000369 | HP:0000369:::           |
| ventricular septal defect | HP:0001629 | HP:0001629:::           |
| ASD                       | HP:0000729 | HP:0000729:::HP:0001631 |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|hpo_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|980.6 KB|
