---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Conditions) (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_snomed_conditions_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, conditions, bge]
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

This model maps extracted clinical NER entities to SNOMED CT concepts using `bge_base_en_v1_5_onnx` embeddings.

It is trained on SNOMED CT US Edition 20260901 release.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_conditions_20260901_en_6.4.1_3.4_1789141450108.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_snomed_conditions_20260901_en_6.4.1_3.4_1789141450108.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_snomed_conditions_20260901","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_snomed_conditions_20260901","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_snomed_conditions_20260901", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| type 2 diabetes mellitus | Diabetes       |      44054006 | type 2 diabetes mellitus | 44054006:::81531005:::73211009:::422014003:::359642000:::368051000119109:::19038... | type 2 diabetes mellitus:::type 2 diabetes mellitus in obese:::diabetes mellitus... |
| essential hypertension   | Hypertension   |      59621000 | essential hypertension   | 59621000:::429457004:::19769006:::46481004:::1201005:::78975002:::72022006:::371... | essential hypertension:::systolic essential hypertension:::high-renin essential ... |
| myocardial infarction    | Heart_Disease  |      22298006 | myocardial infarction    | 22298006:::57054005:::164865005:::414795007:::380001000004106:::42531007:::39471... | myocardial infarction:::acute myocardial infarction:::electrocardiographic myoca... |
| hyperlipidemia           | Hyperlipidemia |      55822004 | hyperlipidemia           | 55822004:::3744001:::13644009:::124322002:::238080004:::302870006:::370992007:::... | hyperlipidemia:::hyperlipoproteinaemia:::hypercholesterolaemia:::hyperglycerolem... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_snomed_conditions_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|598.9 MB|
|Case sensitive:|false|