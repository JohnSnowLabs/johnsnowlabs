---
layout: model
title: Mapping Entities with Corresponding SNOMED Codes
author: John Snow Labs
name: snomed_mapper
date: 2025-12-05
tags: [mapper, snomed, en, licensed, clinical, chunk_mapper]
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

This model maps clinical entities to their corresponding SNOMED codes. It provides fast and accurate clinical code mapping without requiring embeddings.

## Predicted Entities

`SNOMED Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/snomed_mapper_en_6.2.0_3.4_1764895840867.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/snomed_mapper_en_6.2.0_3.4_1764895840867.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                   "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                   "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                   "Internal_organ_or_component", "External_body_part_or_region", "Modifier",
                   "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                   "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                   "Psychological_Condition", "LDL", "Diabetes"])

snomed_mapper = ChunkMapperModel.pretrained("snomed_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    snomed_mapper
])

text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

data = spark.createDataFrame([[text]]).toDF("text")

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
    .setOutputCol("embeddings")

ner_jsl = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_jsl_converter = medical.NerConverter()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                   "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                   "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                   "Internal_organ_or_component", "External_body_part_or_region", "Modifier",
                   "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                   "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                   "Psychological_Condition", "LDL", "Diabetes"])

snomed_mapper = medical.ChunkMapperModel.pretrained("snomed_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["snomed_code"])

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    snomed_mapper
])

text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

data = spark.createDataFrame([[text]]).toDF("text")

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
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl")

val nerJslConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                        "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                        "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                        "Internal_organ_or_component", "External_body_part_or_region", "Modifier",
                        "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                        "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                        "Psychological_Condition", "LDL", "Diabetes"))

val snomedMapper = ChunkMapperModel.pretrained("snomed_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("snomed_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerJsl,
    nerJslConverter,
    snomedMapper
))

val data = Seq("""John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|ner_chunk        |mapping_result|
|-----------------|--------------|
|ofloxacin        |387551000     |
|secondary        |2603003       |
|conjunctivitis   |9826008       |
|cefixime         |387536009     |
|cystic urethritis|1259233009    |
|ibuprofen        |387207008     |
|inflammation     |257552002     |
|cilnidipine      |1177123004    |
|hypertension     |38341003      |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|snomed_mapper|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|26.6 MB|
