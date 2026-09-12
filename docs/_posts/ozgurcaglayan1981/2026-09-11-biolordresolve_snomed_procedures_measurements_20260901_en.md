---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Procedures and Measurements) (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_snomed_procedures_measurements_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, procedure_measurements, biolord]
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

This model maps extracted clinical NER entities to SNOMED CT concepts using `mpnet_embeddings_biolord_2023_c` embeddings.

It is trained on SNOMED CT US Edition 20260901 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_procedures_measurements_20260901_en_6.4.1_3.4_1789143552010.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_procedures_measurements_20260901_en_6.4.1_3.4_1789143552010.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_tags")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner_tags"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_procedures_measurements_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```

{:.jsl-block}
```python
documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("ner_tags")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner_tags"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_procedures_measurements_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count."]]).toDF("text")
result = pipeline.fit(data).transform(data)
```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner_tags")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner_tags"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test"))

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("resolver_embeddings")
    .setCaseSensitive(false)
    .setBatchSize(1)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_snomed_procedures_measurements_20260901", "en", "clinical/models")
    .setInputCols(Array("resolver_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient underwent a laparoscopic cholecystectomy and appendectomy. Laboratory testing showed an elevated white blood cell count.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                        | label     |   snomed_code | resolution                   | all_codes                                                                           | all_resolutions                                                                     |
|:-----------------------------|:----------|--------------:|:-----------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| laparoscopic cholecystectomy | Procedure |      45595009 | laparoscopic cholecystectomy | 45595009:::450499007:::713872007:::1137453008:::1137372009:::67557008:::38102005... | laparoscopic cholecystectomy:::laparoscopic subtotal cholecystectomy:::single-po... |
| appendectomy                 | Procedure |      80146002 | appendectomy                 | 80146002:::174045003:::82730006:::6025007:::174036004:::1299000:::235313004:::49... | appendectomy:::interval appendicectomy:::incidental appendectomy:::laparoscopic ... |
| Laboratory testing           | Test      |      15220000 | laboratory test              | 15220000:::108252007:::127789004:::386521001:::386344002:::117044006:::401096005... | laboratory test:::laboratory procedures:::laboratory procedure categorized by me... |
| white blood cell count       | Test      |        767002 | white blood cell count       | 767002:::391558003:::42396003:::252305002:::165511009:::116708001:::30630007:::1... | white blood cell count:::total white blood cell count:::white blood cell estimat... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_procedures_measurements_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|324.4 MB|
|Case sensitive:|false|