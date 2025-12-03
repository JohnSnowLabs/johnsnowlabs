---
layout: model
title: Sentence Entity Resolver for SNOMED CT (BGE Embeddings)
author: John Snow Labs
name: bgeresolve_snomed
date: 2025-12-03
tags: [resolver, snomed, en, licensed, clinical, bge, sentence_entity_resolver]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This is a Sentence Entity Resolver model that maps clinical entities to SNOMED codes using `bge_base_en_v1_5_onnx` embeddings. It leverages contextual embeddings to improve code resolution accuracy for medical concepts, including diseases, symptoms, procedures, and drugs.

## Predicted Entities

`SNOMED Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_en_6.2.0_3.4_1764794266602.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_en_6.2.0_3.4_1764794266602.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_jsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_jsl_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_jsl_chunk")\
    .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                   "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                   "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                   "Internal_organ_or_component","External_body_part_or_region","Modifier",
                   "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                   "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                   "Psychological_Condition","LDL","Diabetes"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

snomed_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_snomed", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    bge_embeddings,
    snomed_resolver
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

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_jsl = medical.MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner_jsl")

ner_jsl_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner_jsl"])\
    .setOutputCol("ner_jsl_chunk")\
    .setWhiteList(["Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                   "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                   "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                   "Internal_organ_or_component","External_body_part_or_region","Modifier",
                   "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                   "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                   "Psychological_Condition","LDL","Diabetes"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_jsl_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

snomed_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_snomed", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_jsl,
    ner_jsl_converter,
    chunk2doc,
    bge_embeddings,
    snomed_resolver
])

text = """John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerJsl = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_jsl")

val nerJslConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_jsl"))
    .setOutputCol("ner_jsl_chunk")
    .setWhiteList(Array("Procedure","Kidney_Disease","Cerebrovascular_Disease","Heart_Disease",
                        "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding",
                        "EKG_Findings", "Communicable_Disease","Substance","Drug_Ingredient",
                        "Internal_organ_or_component","External_body_part_or_region","Modifier",
                        "Triglycerides", "Alcohol", "Smoking", "Hypertension", "Obesity",
                        "Injury_or_Poisoning","Test","Hyperlipidemia","BMI","Oncological",
                        "Psychological_Condition","LDL","Diabetes"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_jsl_chunk")
    .setOutputCol("ner_chunk_doc")

val bgeEmbeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")

val snomedResolver = SentenceEntityResolverModel.pretrained("bgeresolve_snomed", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerJsl,
    nerJslConverter,
    chunk2doc,
    bgeEmbeddings,
    snomedResolver
))

val data = Seq("""John's doctor prescribed ofloxacin for his secondary conjunctivitis, cefixime for his cystic urethritis, ibuprofen for his inflammation, and cilnidipine for his hypertension on 2023-12-01.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|sent_id|ner_chunk        |entity                   |snomed_code|resolutions       |all_codes                                      |all_resolutions                                |
|-------|-----------------|-------------------------|-----------|------------------|-----------------------------------------------|-----------------------------------------------|
|0      |ofloxacin        |Drug_Ingredient          |387551000  |ofloxacin         |[387551000, 96086002, 392417006, 392415003, ...]|[ofloxacin, ofloxacin product, parenteral oflo...]|
|0      |secondary        |Modifier                 |2603003    |secondary         |[2603003, 262134003, 721071000000106, ...]     |[secondary, secondary procedure, secondary and...]|
|0      |conjunctivitis   |Disease_Syndrome_Disorder|9826008    |conjunctivitis    |[9826008, 473460002, 45261009, 128350005, ...] |[conjunctivitis, allergic conjunctivitis, vira...]|
|0      |cefixime         |Drug_Ingredient          |387536009  |cefixime          |[387536009, 96052006, 713750001, 294548002, ...]|[cefixime, cefixime product, oral form cefixim...]|
|0      |cystic urethritis|Disease_Syndrome_Disorder|1259233009 |cystic urethritis |[1259233009, 70795003, 31822004, 429728004, ...]|[cystic urethritis, urethral cyst, urethritis,...]|
|0      |ibuprofen        |Drug_Ingredient          |387207008  |ibuprofen         |[387207008, 350321003, 293619005, 38268001, ...]|[ibuprofen, oral ibuprofen, ibuprofen allergy,...]|
|0      |inflammation     |Symptom                  |257552002  |inflammation      |[257552002, 225540005, 274144001, 3723001, ...] |[inflammation, wound inflammation, inflammatio...]|
|0      |cilnidipine      |Drug_Ingredient          |1177123004 |cilnidipine       |[1177123004, 1179035008, 1179037000, ...]      |[cilnidipine, cilnidipine-containing product, ...]|
|0      |hypertension     |Hypertension             |38341003   |hypertension      |[38341003, 75367002, 73578008, 28119000, ...]  |[hypertension, blood pressure, hyperdistension...]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_snomed|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.7 GB|
|Case sensitive:|false|