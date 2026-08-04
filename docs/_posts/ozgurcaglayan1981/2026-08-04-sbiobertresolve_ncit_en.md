---
layout: model
title: Sentence Entity Resolver for NCI-t (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_ncit
date: 2026-08-04
tags: [en, entity_resolution, licensed, clinical, ncit, sbiobert]
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

This model maps clinical/oncology entities to NCIt (NCI Thesaurus) codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. Trained on the NCI Thesaurus dataset (July 28, 2026 release).

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ncit_en_6.4.1_3.4_1785878391478.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ncit_en_6.4.1_3.4_1785878391478.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

ncit_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ncit", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
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

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models") \
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

ncit_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_ncit", "en", "clinical/models")\
    .setInputCols(["sbert_embeddings"])\
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

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val ncit_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ncit", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
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
| breast carcinoma | Cancer_Dx      | C4872       | breast carcinoma [breast carcinoma] | C4872:::C4017:::C147915:::C217270:::C53554:::C118809:::C40364:::C5214:::C167189:... | 0.0000:::4.5876:::4.7017:::4.8119:::5.0894:::5.0900:::5.1965:::5.2565:::5.3467::... | 0.0000:::0.0320:::0.0341:::0.0360:::0.0400:::0.0399:::0.0416:::0.0425:::0.0441::... | breast carcinoma [breast carcinoma]:::breast ductal carcinoma [breast ductal car... |
| biopsy           | Pathology_Test | C15189      | biopsy [biopsy]                     | C15189:::C192621:::C18202:::C77677:::C164175:::C160869:::C49567:::C15190:::C1608... | 0.0000:::4.5896:::4.6661:::5.1726:::5.6365:::5.9746:::6.5265:::7.0238:::7.2550::... | 0.0000:::0.0336:::0.0353:::0.0433:::0.0513:::0.0583:::0.0682:::0.0803:::0.0854::... | biopsy [biopsy]:::biopsy finding [biopsy finding]:::biopsy specimen [biopsy spec... |
| chemotherapy     | Chemotherapy   | C15632      | chemotherapy [chemotherapy]         | C15632:::C160336:::C204795:::C168835:::C274:::C15681:::C191:::C158802:::C58008::... | 0.0000:::4.8505:::5.9540:::6.1603:::6.3463:::6.4772:::6.6041:::7.2356:::7.2422::... | 0.0000:::0.0374:::0.0595:::0.0640:::0.0664:::0.0694:::0.0735:::0.0844:::0.0858::... | chemotherapy [chemotherapy]:::chemotherapy received [chemotherapy received]:::ch... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_ncit|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sbert_embeddings]|
|Output Labels:|[resolution]|
|Language:|en|
|Size:|1.7 GB|
|Case sensitive:|false|
