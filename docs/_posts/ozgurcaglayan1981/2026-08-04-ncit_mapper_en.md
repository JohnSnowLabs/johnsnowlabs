---
layout: model
title: Mapping Entities with Corresponding NCIt Codes
author: John Snow Labs
name: ncit_mapper
date: 2026-08-04
tags: [en, chunk_mapper, licensed, clinical, ncit]
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

This model maps oncology/clinical entities extracted from clinical text to their corresponding NCIt (NCI Thesaurus) codes. It uses ner_oncology for entity recognition and provides fast code mapping without requiring embeddings at inference time. Trained on the NCI Thesaurus dataset (July 28, 2026 release).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/healthcare-nlp/06.0.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ncit_mapper_en_6.4.1_3.4_1785880587364.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/ncit_mapper_en_6.4.1_3.4_1785880587364.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner_oncology = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setBlackList(["Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                    "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"])

ncit_mapper = ChunkMapperModel.pretrained("ncit_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ncit_code"])

pipeline = Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_oncology, ner_converter, ncit_mapper
])
data = spark.createDataFrame([["The patient underwent a biopsy that confirmed carcinoma. Imaging revealed lung cancer, and the patient was later diagnosed with breast carcinoma, prompting a mastectomy followed by chemotherapy and radiation therapy. A separate evaluation confirmed melanoma, while ongoing monitoring raised concern for leukemia. A follow-up colonoscopy was also scheduled."]]).toDF("text")
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

ner_oncology = medical.NerModel.pretrained("ner_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setBlackList(["Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                    "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"])

ncit_mapper = medical.ChunkMapperModel.pretrained("ncit_mapper", "en", "clinical/models")\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("mappings")\
    .setRels(["ncit_code"])

pipeline = nlp.Pipeline(stages=[
    document_assembler, sentence_detector, tokenizer, word_embeddings,
    ner_oncology, ner_converter, ncit_mapper
])
data = spark.createDataFrame([["The patient underwent a biopsy that confirmed carcinoma. Imaging revealed lung cancer, and the patient was later diagnosed with breast carcinoma, prompting a mastectomy followed by chemotherapy and radiation therapy. A separate evaluation confirmed melanoma, while ongoing monitoring raised concern for leukemia. A follow-up colonoscopy was also scheduled."]]).toDF("text")
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

val nerOncology = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setBlackList(Array("Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                         "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"))

val ncitMapper = ChunkMapperModel.pretrained("ncit_mapper", "en", "clinical/models")
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("mappings")
    .setRels(Array("ncit_code"))

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, wordEmbeddings,
    nerOncology, nerConverter, ncitMapper
))

val data = Seq("The patient underwent a biopsy that confirmed carcinoma. Imaging revealed lung cancer, and the patient was later diagnosed with breast carcinoma, prompting a mastectomy followed by chemotherapy and radiation therapy. A separate evaluation confirmed melanoma, while ongoing monitoring raised concern for leukemia. A follow-up colonoscopy was also scheduled.").toDF("text")
val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk         | ncit_code   |
|:------------------|:------------|
| biopsy            | C15189      |
| carcinoma         | C2916       |
| lung cancer       | C4878       |
| breast carcinoma  | C4872       |
| mastectomy        | C15277      |
| chemotherapy      | C15632      |
| radiation therapy | C15313      |
| melanoma          | C3224       |
| leukemia          | C3161       |
| colonoscopy       | C16450      |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|ncit_mapper|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[ner_chunk]|
|Output Labels:|[mappings]|
|Language:|en|
|Size:|14.9 MB|
