---
layout: model
title: Sentence Entity Resolver for CPT Codes - Augmented (sbiobert_base_cased_mli_onnx)
author: John Snow Labs
name: sbiobertresolve_cpt_augmented
date: 2026-07-16
tags: [en, entity_resolution, licensed, clinical, cpt, sbiobert]
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

This model maps clinical procedure and measurement entities to CPT codes using `sbiobert_base_cased_mli_onnx` embeddings.

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

embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.load("sbiobertresolve_cpt_augmented")\
    .setInputCols(["sentence_embeddings"])\
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

embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.load("sbiobertresolve_cpt_augmented")\
    .setInputCols(["sentence_embeddings"])\
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

val embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .load("sbiobertresolve_cpt_augmented")
    .setInputCols(Array("sentence_embeddings"))
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
| hospital             | Clinical_Dept |    1021881 | Inpatient Hospital      | 1021881:::94003:::59855:::1013648:::1021883:::1013668:::1021895:::99236:::102187... | 0.0865:::0.1012:::0.1025:::0.1168:::0.1686:::0.1837:::0.1799:::0.1863:::0.1869::... | Inpatient Hospital:::inpatient care:::hospital admission (procedure):::Hospital ... |
| CT scan of the chest | Test          |      71250 | ct scan of chest        | 71250:::70490:::76497:::71260:::74150:::70486:::73200:::70480:::77014:::73700:::... | 0.0080:::0.0772:::0.0809:::0.0957:::0.1037:::0.1028:::0.1056:::0.1088:::0.1178::... | ct scan of chest:::ct scan of neck:::ct scan:::ct scan of chest with contrast:::... |
| pathology            | Clinical_Dept |      88329 | pathology examination   | 88329:::89240:::77768:::1012348:::76098:::0551F:::1011136:::91120:::91299:::1012... | 0.0987:::0.1139:::0.1398:::0.1422:::0.1546:::0.1665:::0.1646:::0.1708:::0.1713::... | pathology examination:::pathology tests:::with lesions:::Anatomic Pathology Proc... |
| pericardectomy       | Procedure     |      33030 | pericardectomy          | 33030:::33020:::64746:::49250:::27350:::68520:::32310:::33025:::32215:::41821:::... | 0.0000:::0.0703:::0.1048:::0.1148:::0.1225:::0.1276:::0.1347:::0.1394:::0.1398::... | pericardectomy:::pericardotomy:::phrenicectomy:::omphalectomy:::patellectomy:::d... |
| chest tube placement | Procedure     |      39503 | insertion of chest tube | 39503:::96440:::32553:::35820:::32100:::36226:::21899:::29200:::0174T:::31502:::... | 0.0331:::0.0847:::0.1056:::0.1311:::0.1333:::0.1391:::0.1364:::0.1382:::0.1414::... | insertion of chest tube:::chest cavity insertion of catheter:::insertion of devi... |
| thoracoscopy         | Procedure     |    1020900 | Thoracoscopy            | 1020900:::32654:::32668:::1006014:::1005962:::35820:::32606:::32555:::31781:::31... | 0.0000:::0.0079:::0.0314:::0.0793:::0.0875:::0.0874:::0.0948:::0.1195:::0.1162::... | Thoracoscopy:::thoracoscopy with:::thoracoscopy (procedure):::thoracoscopy surgi... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_cpt_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[cpt_code]|
|Language:|en|
|Size:|364.8 MB|
|Case sensitive:|false|
