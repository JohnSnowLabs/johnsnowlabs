---
layout: model
title: Mapping Entities (General Concepts) with Corresponding UMLS CUI Codes
author: John Snow Labs
name: umls_general_concepts_mapper
date: 2026-06-12
tags: [en, chunk_mapper, licensed, clinical, umls, general]
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

This model maps general biomedical concept entities extracted by NER to UMLS CUI codes covering Disease, Symptom, Device, and Procedure semantic types (T047, T184, T074, T061), comprising approximately 1,170,000 name–CUI pairs. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/umls_general_concepts_mapper_en_6.4.0_3.4_1781273727496.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/umls_general_concepts_mapper_en_6.4.0_3.4_1781273727496.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_model = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "clinical_ner"])\
    .setOutputCol("ner_chunk")

chunkerMapper = ChunkMapperModel.pretrained("umls_general_concepts_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])\
    .setLowerCase(True)

mapper_pipeline = Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunkerMapper,
])
data = spark.createDataFrame([["The patient presents with dyspnea and fever due to pneumonia. Treatment includes bronchoscopy, catheter placement, and chemotherapy."]]).toDF("text")
result = mapper_pipeline.fit(data).transform(data)

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

ner_model = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("clinical_ner")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "clinical_ner"])\
    .setOutputCol("ner_chunk")

chunkerMapper = medical.ChunkMapperModel.pretrained("umls_general_concepts_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["umls_code"])\
    .setLowerCase(True)

mapper_pipeline = nlp.Pipeline(stages=[
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunkerMapper,
])
data = spark.createDataFrame([["The patient presents with dyspnea and fever due to pneumonia. Treatment includes bronchoscopy, catheter placement, and chemotherapy."]]).toDF("text")
result = mapper_pipeline.fit(data).transform(data)

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

val nerModel = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("clinical_ner")

val nerModelConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "clinical_ner"))
    .setOutputCol("ner_chunk")

val chunkerMapper = ChunkMapperModel.pretrained("umls_general_concepts_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("umls_code"))
    .setLowerCase(true)

val mapperPipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerModel,
    nerModelConverter,
    chunkerMapper,
))

val data = Seq("The patient presents with dyspnea and fever due to pneumonia. Treatment includes bronchoscopy, catheter placement, and chemotherapy.").toDF("text")
val result = mapperPipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk          | umls_code   |
|:-------------------|:------------|
| dyspnea            | C0013404    |
| fever              | C0015967    |
| pneumonia          | C0032285    |
| bronchoscopy       | C5979970    |
| catheter placement | C0883301    |
| chemotherapy       | C0013216    |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umls_general_concepts_mapper|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|46.5 MB|