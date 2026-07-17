---
layout: model
title: Sentence Entity Resolver for CPT Codes - Augmented (bge_base_en_v1_5_onnx)
author: John Snow Labs
name: bgeresolve_cpt_augmented
date: 2026-07-17
tags: [en, entity_resolution, licensed, clinical, cpt, bge]
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

This model maps clinical procedure and measurement entities to CPT codes using `bge_base_en_v1_5_onnx` embeddings.

Training data: this model is trained on current CPT data, further augmented by John Snow Labs for broader coverage.

CPT resolver models are removed from the Models Hub due to license restrictions and can only be shared with users who already have a valid CPT license. Contact support@johnsnowlabs.com for access.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/24.Improved_Entity_Resolvers_in_SparkNLP_with_sBert.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}


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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.load("bgeresolve_cpt_augmented")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.load("bgeresolve_cpt_augmented")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .load("bgeresolve_cpt_augmented")
    .setInputCols(Array("bge_embeddings"))
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
| ner_chunk            | entity        |   cpt_code | resolution              | all_k_results                                                                       | all_k_cosine_distances                                                              | all_k_resolutions                                                                   |
|:---------------------|:--------------|-----------:|:------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| hospital             | Clinical_Dept |    1021881 | Inpatient Hospital      | 1021881:::1021883:::59855:::1021882:::94003:::99235:::1021895:::1013659:::101358... | 0.1291:::0.1593:::0.1873:::0.2055:::0.2094:::0.2292:::0.2375:::0.2393:::0.2459::... | Inpatient Hospital:::Emergency Room-Hospital:::hospital admission:::On Campus-Ou... |
| CT scan of the chest | Test          |      71250 | ct scan of chest        | 71250:::71260:::71271:::76497:::71550:::71270:::71275:::0174T:::70490:::1031050:... | 0.0276:::0.1043:::0.1339:::0.1360:::0.1423:::0.1449:::0.1626:::0.1673:::0.1725::... | ct scan of chest:::ct scan of chest with contrast:::ct scan of chest lung cancer... |
| pathology            | Clinical_Dept |      88329 | pathology examination   | 88329:::1011136:::89240:::1012454:::1036755:::88380:::88399:::1013981:::1011219:... | 0.1399:::0.1528:::0.1546:::0.1663:::0.1753:::0.1761:::0.1781:::0.1790:::0.1806::... | pathology examination:::Pathology and Laboratory Procedures:::pathology tests:::... |
| pericardectomy       | Procedure     |      33030 | pericardectomy          | 33030:::33020:::1006058:::1006057:::41821:::33050:::33025:::1006065                 | 0.0000:::0.1230:::0.2003:::0.2240:::0.2333:::0.2361:::0.2396:::0.2491               | pericardectomy:::pericardotomy:::surgical procedures pericardium:::surgical proc... |
| chest tube placement | Procedure     |      39503 | insertion of chest tube | 39503:::31605:::96440:::32560:::36225:::36010:::33964:::93453:::93456:::33236:::... | 0.0857:::0.1697:::0.1877:::0.1978:::0.2100:::0.2257:::0.2257:::0.2270:::0.2279::... | insertion of chest tube:::insertion of breathing tube:::chest cavity insertion o... |
| thoracoscopy         | Procedure     |    1020900 | Thoracoscopy            | 1020900:::32668:::1006014:::32601:::32654:::32608:::32653:::00540:::32606:::3266... | 0.0000:::0.0388:::0.0712:::0.0881:::0.1057:::0.1324:::0.1341:::0.1359:::0.1390::... | Thoracoscopy:::thoracoscopy (procedure):::thoracoscopy surgical:::diagnostic tho... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_cpt_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[cpt_code]|
|Language:|en|
|Size:|365.2 MB|
|Case sensitive:|false|
