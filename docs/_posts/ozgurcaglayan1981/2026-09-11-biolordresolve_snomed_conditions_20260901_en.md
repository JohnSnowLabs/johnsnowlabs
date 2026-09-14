---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Conditions) (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_snomed_conditions_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, conditions, biolord]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_conditions_20260901_en_6.4.1_3.4_1789140316358.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_conditions_20260901_en_6.4.1_3.4_1789140316358.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease", "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding", "EKG_Findings", "Communicable_Disease", "Pregnancy", "Obesity", "Hypertension", "Overweight", "Hyperlipidemia", "Triglycerides", "Diabetes", "Oncological", "Psychological_Condition", "Injury_or_Poisoning"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_conditions_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia."]]).toDF("text")
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
    .setWhiteList(["Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease", "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding", "EKG_Findings", "Communicable_Disease", "Pregnancy", "Obesity", "Hypertension", "Overweight", "Hyperlipidemia", "Triglycerides", "Diabetes", "Oncological", "Psychological_Condition", "Injury_or_Poisoning"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_conditions_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia."]]).toDF("text")
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
    .setWhiteList(Array("Kidney_Disease", "Cerebrovascular_Disease", "Heart_Disease", "Disease_Syndrome_Disorder", "ImagingFindings", "Symptom", "VS_Finding", "EKG_Findings", "Communicable_Disease", "Pregnancy", "Obesity", "Hypertension", "Overweight", "Hyperlipidemia", "Triglycerides", "Diabetes", "Oncological", "Psychological_Condition", "Injury_or_Poisoning"))

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
    .pretrained("biolordresolve_snomed_conditions_20260901", "en", "clinical/models")
    .setInputCols(Array("resolver_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient has a history of type 2 diabetes mellitus and essential hypertension. She was admitted with an acute myocardial infarction and later diagnosed with hyperlipidemia.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                    | label          |   snomed_code | resolution               | all_codes                                                                           | all_resolutions                                                                     |
|:-------------------------|:---------------|--------------:|:-------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| type 2 diabetes mellitus | Diabetes       |      44054006 | type 2 diabetes mellitus | 44054006:::422014003:::359642000:::199230006:::445353002:::237599002:::443694000... | type 2 diabetes mellitus:::disorder due to type 2 diabetes mellitus:::type 2 dia... |
| essential hypertension   | Hypertension   |      59621000 | essential hypertension   | 59621000:::78975002:::38341003:::371125006:::1201005:::64715009:::697929007:::70... | essential hypertension:::accelerated essential hypertension:::systemic arterial ... |
| myocardial infarction    | Heart_Disease  |      22298006 | myocardial infarction    | 22298006:::57054005:::164865005:::251061000:::194856005:::1755008:::394710008:::... | myocardial infarction:::acute myocardial infarction:::electrocardiographic myoca... |
| hyperlipidemia           | Hyperlipidemia |      55822004 | hyperlipidemia           | 55822004:::3744001:::13644009:::302870006:::402727002:::238080004:::129589009:::... | hyperlipidemia:::hyperlipoproteinemia:::hypercholesterolemia:::hypertriglyceride... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_conditions_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|599.3 MB|
|Case sensitive:|false|