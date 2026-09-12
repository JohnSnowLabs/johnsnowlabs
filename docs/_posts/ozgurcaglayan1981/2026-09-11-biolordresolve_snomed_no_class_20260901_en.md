---
layout: model
title: Sentence Entity Resolver for SNOMED CT (Miscellaneous (No Class) Concepts) (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_snomed_no_class_20260901
date: 2026-09-11
tags: [en, snomed, resolver, licensed, clinical, no_class, biolord]
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_no_class_20260901_en_6.4.1_3.4_1789155421491.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_snomed_no_class_20260901_en_6.4.1_3.4_1789155421491.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setWhiteList(["Drug", "Drug_Ingredient", "Drug_BrandName", "Disease_Syndrome_Disorder", "Kidney_Disease", "Heart_Disease", "Diabetes", "Oncological"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_snomed_no_class_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid."]]).toDF("text")
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
    .setWhiteList(["Drug", "Drug_Ingredient", "Drug_BrandName", "Disease_Syndrome_Disorder", "Kidney_Disease", "Heart_Disease", "Diabetes", "Oncological"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("resolver_embeddings")\
    .setCaseSensitive(False)\
    .setBatchSize(1)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_snomed_no_class_20260901","en","clinical/models")\
    .setInputCols(["resolver_embeddings"])\
    .setOutputCol("snomed_code")\
    .setDistanceFunction("EUCLIDEAN")\
    .setThreshold(1000)

pipeline = nlp.Pipeline(stages=[\
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver\
])

data = spark.createDataFrame([["The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid."]]).toDF("text")
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
    .setWhiteList(Array("Drug", "Drug_Ingredient", "Drug_BrandName", "Disease_Syndrome_Disorder", "Kidney_Disease", "Heart_Disease", "Diabetes", "Oncological"))

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
    .pretrained("biolordresolve_snomed_no_class_20260901", "en", "clinical/models")
    .setInputCols(Array("resolver_embeddings"))
    .setOutputCol("snomed_code")
    .setDistanceFunction("EUCLIDEAN")
    .setThreshold(1000)

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings, ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient developed postsurgical gastroparesis after her procedure. Pathology confirmed a malignant gastroblastoma. On eye exam she was also noted to have trichiasis of upper eyelid.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| chunk                      | label                     |     snomed_code | resolution                               | all_codes                                                                           | all_resolutions                                                                     |
|:---------------------------|:--------------------------|----------------:|:-----------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| gastroparesis              | Disease_Syndrome_Disorder |      1397402007 | postsurgical gastroparesis               | 1397402007:::1388584008:::1399540004:::1398959002:::1389148002:::440295211000119... | postsurgical gastroparesis:::gastric dilatation:::iem - ineffective esophageal m... |
| malignant gastroblastoma   | Oncological               |   2711000181102 | malignant gastroblastoma                 | 2711000181102:::112761000112106:::1382012000:::510204201000119100:::112751000112... | malignant gastroblastoma:::malignant neoplasm of stomach suspected:::inspection ... |
| trichiasis of upper eyelid | Disease_Syndrome_Disorder | 412041000087109 | entropion and trichiasis of upper eyelid | 412041000087109:::412031000087103:::412001000087106:::412021000087100:::41201100... | entropion and trichiasis of upper eyelid:::entropion and trichiasis of right upp... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_snomed_no_class_20260901|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[snomed_code]|
|Language:|en|
|Size:|34.2 MB|
|Case sensitive:|false|