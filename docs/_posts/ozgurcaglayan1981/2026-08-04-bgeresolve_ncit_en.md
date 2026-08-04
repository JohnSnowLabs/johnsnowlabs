---
layout: model
title: Sentence Entity Resolver for NCI-t (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_ncit
date: 2026-08-04
tags: [en, entity_resolution, licensed, clinical, ncit, bge]
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

This model maps clinical/oncology entities to NCIt (NCI Thesaurus) codes using `bge_base_en_v1_5_onnx` Sentence Embeddings. Trained on the NCI Thesaurus dataset (July 28, 2026 release).

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_ncit_en_6.4.1_3.4_1785880039155.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_ncit_en_6.4.1_3.4_1785880039155.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

ncit_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_ncit", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

sbert_embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

ncit_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_ncit", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val sbert_embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val ncit_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_ncit", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| ner_chunk        | entity         | ncit_code   | resolution_text                     | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:-----------------|:---------------|:------------|:------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| breast carcinoma | Cancer_Dx      | C4872       | breast carcinoma [breast carcinoma] | C4872:::C4017:::C118809:::C2910:::C2918:::C9335:::C5214:::C9245:::C2916:::C16264... | 0.0000:::0.3921:::0.4018:::0.4583:::0.4678:::0.5308:::0.5342:::0.5486:::0.5512::... | 0.0000:::0.0769:::0.0807:::0.1050:::0.1094:::0.1409:::0.1427:::0.1505:::0.1519::... | breast carcinoma [breast carcinoma]:::breast ductal carcinoma [breast ductal car... |
| biopsy           | Pathology_Test | C15189      | biopsy [biopsy]                     | C15189:::C15385:::C51692:::C51698:::C192621:::C51748:::C51699:::C51678:::C77677:... | 0.0000:::0.4025:::0.4440:::0.4530:::0.4538:::0.4771:::0.4821:::0.4857:::0.4929::... | 0.0000:::0.0810:::0.0986:::0.1026:::0.1030:::0.1138:::0.1162:::0.1180:::0.1215::... | biopsy [biopsy]:::surgical biopsy [surgical biopsy]:::skin biopsy [skin biopsy]:... |
| chemotherapy     | Chemotherapy   | C15632      | chemotherapy [chemotherapy]         | C15632:::C226697:::C191:::C174557:::C1594:::C158803:::C15807:::C51967:::C180666:... | 0.0000:::0.4523:::0.5313:::0.5667:::0.5671:::0.5676:::0.5717:::0.5764:::0.5779::... | 0.0000:::0.1023:::0.1411:::0.1606:::0.1608:::0.1611:::0.1634:::0.1661:::0.1670::... | chemotherapy [chemotherapy]:::chemotherapy answer [chemotherapy answer]:::chemot... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_ncit|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|