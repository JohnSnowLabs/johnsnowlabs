---
layout: model
title: Sentence Entity Resolver for NCI-t (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_ncit
date: 2026-08-04
tags: [en, entity_resolution, licensed, clinical, ncit, biolord]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical/oncology entities to NCIt (NCI Thesaurus) codes using `mpnet_embeddings_biolord_2023_c` Sentence Embeddings. Trained on the NCI Thesaurus dataset (July 28, 2026 release).

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_ncit_en_6.4.1_3.4_1785879314968.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_ncit_en_6.4.1_3.4_1785879314968.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

oncology_ner = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setBlackList(["Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                    "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ncit_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_ncit", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    oncology_ner, ner_converter, c2doc, sbert_embedder, ncit_resolver
])

data = spark.createDataFrame([["The patient was diagnosed with breast carcinoma and underwent a biopsy followed by chemotherapy."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

oncology_ner = medical.NerModel.pretrained("ner_oncology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setBlackList(["Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                    "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

ncit_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_ncit", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    oncology_ner, ner_converter, c2doc, sbert_embedder, ncit_resolver
])

data = spark.createDataFrame([["The patient was diagnosed with breast carcinoma and underwent a biopsy followed by chemotherapy."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val oncology_ner = MedicalNerModel.pretrained("ner_oncology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setBlackList(Array("Age", "Date", "Death_Entity", "Gender", "Race_Ethnicity",
                         "Relative_Date", "Smoking_Status", "Dosage", "Tumor_Size"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val ncit_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_ncit", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    oncology_ner, ner_converter, c2doc, sbert_embedder, ncit_resolver
))

val data = Seq("The patient was diagnosed with breast carcinoma and underwent a biopsy followed by chemotherapy.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk        | entity         | ncit_code   | resolution_text                       | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:-----------------|:---------------|:------------|:--------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| breast carcinoma | Cancer_Dx      | C4872       | mammary carcinoma [mammary carcinoma] | C4872:::C5214:::C2918:::C9335:::C118809:::C5164:::C206118:::C9245:::C3862:::C403... | 0.3398:::0.3783:::0.3810:::0.4347:::0.4584:::0.4596:::0.4822:::0.4902:::0.4992::... | 0.0577:::0.0716:::0.0726:::0.0945:::0.1051:::0.1056:::0.1163:::0.1202:::0.1246::... | mammary carcinoma [mammary carcinoma]:::breast adenocarcinoma [breast adenocarci... |
| biopsy           | Pathology_Test | C15189      | biopsy [biopsy]                       | C15189:::C18202:::C15385:::C217124:::C164175:::C182265:::C137813:::C15680:::C153... | 0.3457:::0.4810:::0.4839:::0.5454:::0.5462:::0.5739:::0.5795:::0.5939:::0.6055::... | 0.0598:::0.1157:::0.1171:::0.1487:::0.1492:::0.1647:::0.1679:::0.1764:::0.1833::... | biopsy [biopsy]:::biopsy specimen [biopsy specimen]:::surgical biopsy [surgical ... |
| chemotherapy     | Chemotherapy   | C15632      | chemotherapy [chemotherapy]           | C15632:::C171212:::C174557:::C71593:::C182408:::C15681:::C168837:::C15756:::C642... | 0.3501:::0.5622:::0.5633:::0.5960:::0.6074:::0.6267:::0.6324:::0.6360:::0.6418::... | 0.0613:::0.1580:::0.1586:::0.1776:::0.1845:::0.1964:::0.2000:::0.2023:::0.2059::... | chemotherapy [chemotherapy]:::chemotherapy session for neoplasm [chemotherapy se... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_ncit|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|