---
layout: model
title: Sentence Entity Resolver for SNOMED CT (All Concepts) (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_snomed_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, general, biolord]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_20260901_en_6.4.1_3.4_1789156690433.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_20260901_en_6.4.1_3.4_1789156690433.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["Injury_or_Poisoning", "Hyperlipidemia", "Kidney_Disease", "Oncological", "Cerebrovascular_Disease", "Oxygen_Therapy", "Heart_Disease", "Obesity", "Disease_Syndrome_Disorder", "Symptom", "Treatment", "Diabetes", "Procedure", "Drug_Ingredient", "VS_Finding", "Communicable_Disease", "Drug_BrandName", "Hypertension", "Imaging_Technique"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
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
    .setWhiteList(["Injury_or_Poisoning", "Hyperlipidemia", "Kidney_Disease", "Oncological", "Cerebrovascular_Disease", "Oxygen_Therapy", "Heart_Disease", "Obesity", "Disease_Syndrome_Disorder", "Symptom", "Treatment", "Diabetes", "Procedure", "Drug_Ingredient", "VS_Finding", "Communicable_Disease", "Drug_BrandName", "Hypertension", "Imaging_Technique"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin."]]).toDF("text")
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
    .setWhiteList(Array("Injury_or_Poisoning", "Hyperlipidemia", "Kidney_Disease", "Oncological", "Cerebrovascular_Disease", "Oxygen_Therapy", "Heart_Disease", "Obesity", "Disease_Syndrome_Disorder", "Symptom", "Treatment", "Diabetes", "Procedure", "Drug_Ingredient", "VS_Finding", "Communicable_Disease", "Drug_BrandName", "Hypertension", "Imaging_Technique"))

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
    .pretrained("biolordresolve_snomed_20260901", "en", "clinical/models")
    .setInputCols(Array("resolver_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient with inflammatory bowel disease presented with dyspnea and abdominal pain. She underwent a laparoscopic appendectomy and was started on aspirin.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |   snomed_code | resolution                 | all_codes                                                                           | all_resolutions                                                                     |
|:---------------------------|:--------------------------|--------------:|:---------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| inflammatory bowel disease | Disease_Syndrome_Disorder |      24526004 | inflammatory bowel disease | 24526004:::1396343004:::64226004:::1187638005:::43752006:::50440006:::397173003:... | inflammatory bowel disease:::inflammatory bowel disease unclassified:::colitis::... |
| dyspnea                    | Symptom                   |     267036007 | dyspnea                    | 267036007:::297216006:::230145002:::248549001:::23141003:::60845006:::870535009:... | dyspnea:::increasing breathlessness:::difficulty breathing:::labored breathing::... |
| abdominal pain             | Symptom                   |      21522001 | abdominal pain             | 21522001:::9991008:::271681002:::102614006:::73063007:::438506002:::162042000:::... | abdominal pain:::abdominal colic:::belly ache:::generalised abdominal pain:::col... |
| laparoscopic appendectomy  | Procedure                 |       6025007 | laparoscopic appendectomy  | 6025007:::307581005:::708876004:::174041007:::80146002:::440588003:::235313004::... | laparoscopic appendectomy:::laparoscopic interval appendectomy:::robot assisted ... |
| aspirin                    | Drug_Ingredient           |     387458008 | aspirin                    | 387458008:::7947003:::426365001:::25796002:::10876551000119102:::60526005:::2920... | aspirin:::aspirin-containing product:::buffered aspirin:::aluminum aspirin:::asp... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|2.1 GB|
|Case sensitive:|false|