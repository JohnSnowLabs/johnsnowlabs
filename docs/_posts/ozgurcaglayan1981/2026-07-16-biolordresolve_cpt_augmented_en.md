---
layout: model
title: Sentence Entity Resolver for CPT Codes - Augmented (mpnet_embeddings_biolord_2023_c)
author: John Snow Labs
name: biolordresolve_cpt_augmented
date: 2026-07-16
tags: [en, entity_resolution, licensed, clinical, cpt, biolord]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical procedure and measurement entities to CPT codes using `mpnet_embeddings_biolord_2023_c` embeddings.

Training data: this model is trained on current CPT data, further augmented by John Snow Labs for broader coverage.

CPT resolver models are removed from the Models Hub due to license restrictions and can only be shared with users who already have a valid CPT license. Contact support@johnsnowlabs.com for access.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_cpt_augmented_en_6.4.0_3.4_1784239914342.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_cpt_augmented_en_6.4.0_3.4_1784239914342.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure","Test","Treatment","Clinical_Dept"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.load("biolordresolve_cpt_augmented")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("cpt_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner = medical.NerModel.pretrained("ner_jsl","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure","Test","Treatment","Clinical_Dept"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.load("biolordresolve_cpt_augmented")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("cpt_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner = MedicalNerModel
    .pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val nerConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test", "Treatment", "Clinical_Dept"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("mpnet_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .load("biolordresolve_cpt_augmented")
    .setInputCols(Array("mpnet_embeddings"))
    .setOutputCol("cpt_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner, nerConverter, chunk2doc, embedder, resolver
))

val data = Seq("She was admitted to the hospital with chest pain and found to have bilateral pleural effusion, the right greater than the left. CT scan of the chest also revealed a large mediastinal lymph node. We reviewed the pathology obtained from the pericardectomy in March 2006, which was diagnostic of mesothelioma. At this time, chest tube placement for drainage of the fluid occurred and thoracoscopy, which were performed.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk            | entity        |   cpt_code | resolution                                                  | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:---------------------|:--------------|-----------:|:------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| hospital             | Clinical_Dept |    1021881 | Inpatient Hospital                                          | 1021881:::59855:::1021883:::99026:::1013682:::1013659:::1021882:::1028888:::1013... | 0.2813:::0.3761:::0.4060:::0.4245:::0.4282:::0.4388:::0.4632:::0.4654:::0.4663::... | Inpatient Hospital:::hospital admission:::Emergency Room-Hospital:::hospital man... |
| CT scan of the chest | Test          |      71260 | diagnostic computed tomography (ct) of thorax with contrast | 71260:::71270:::1036223:::0878T:::71250:::78814:::71275                             | 0.1654:::0.2153:::0.2679:::0.3121:::0.3189:::0.3225:::0.3234                        | diagnostic computed tomography (ct) of thorax with contrast:::diagnostic compute... |
| pathology            | Clinical_Dept |      89240 | anatomic pathology procedure                                | 89240:::88329:::1012348:::88302:::88305:::88037:::88399:::1011136:::88331:::8802... | 0.2306:::0.2393:::0.2515:::0.3386:::0.3503:::0.3611:::0.3621:::0.3707:::0.3716::... | anatomic pathology procedure:::pathology examination:::Anatomic Pathology Proced... |
| pericardectomy       | Procedure     |      33030 | excision of pericardium                                     | 33030:::33025:::33050:::1006065:::32659:::32661:::33031:::33020                     | 0.1802:::0.2533:::0.2616:::0.2856:::0.2896:::0.2905:::0.3002:::0.3077               | excision of pericardium:::partial resection of pericardium drainage:::excision o... |
| chest tube placement | Procedure     |      96440 | chest cavity insertion of catheter                          | 96440:::39503:::32553:::32557:::33621:::1021149:::1002859:::32550:::32556:::3255... | 0.1921:::0.2293:::0.2884:::0.2931:::0.2966:::0.2971:::0.3032:::0.3036:::0.3040::... | chest cavity insertion of catheter:::insertion of chest drain:::percutaneous pla... |
| thoracoscopy         | Procedure     |      32654 | thoracoscopy with                                           | 32654:::1006014:::32601:::1020900:::1006007:::32609:::32668:::32651:::1006006:::... | 0.0941:::0.1344:::0.1517:::0.1540:::0.1893:::0.2020:::0.2164:::0.2243:::0.2298::... | thoracoscopy with:::thoracoscopy, surgical | [diagnostic procedure]:::diagnostic... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_cpt_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[cpt_code]|
|Language:|en|
|Size:|365.5 MB|
|Case sensitive:|false|