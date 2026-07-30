---
layout: model
title: Sentence Entity Resolver for ICD11
author: John Snow Labs
name: sbiobertresolve_icd11_mental_health
date: 2026-06-30
tags: [en, entity_resolution, licensed, clinical, icd11]
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

This model maps clinical entities and concepts to ICD11 codes using `sbiobert_base_cased_mli_onnx` sentence bert embeddings. It also returns the official resolution text within the brackets inside the metadata.

## Predicted Entities

`ICD11 Code`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_mental_health_en_6.4.1_3.4_1782806275328.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_mental_health_en_6.4.1_3.4_1782806275328.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_mental_health", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       icd_resolver])


data = spark.createDataFrame([["""The patient was diagnosed with major depressive disorder, generalized anxiety disorder, post-traumatic stress disorder, and attention deficit hyperactivity disorder."""]]).toDF("text")

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

ner = medical.NerModel.pretrained("ner_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["PROBLEM"])

c2doc = medical.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

icd_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_mental_health", "en", "clinical/models") \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       icd_resolver])


data = spark.createDataFrame([["""The patient was diagnosed with major depressive disorder, generalized anxiety disorder, post-traumatic stress disorder, and attention deficit hyperactivity disorder."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11_mental_health", "en", "clinical/models")
    .setInputCols("sentence_embeddings")
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       icd_resolver))


val data = Seq("The patient was diagnosed with major depressive disorder, generalized anxiety disorder, post-traumatic stress disorder, and attention deficit hyperactivity disorder.").toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash


+----------------------------------------+-------+----------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|                               ner_chunk| entity|ICD11_code|                             resolutions|                                                                                                                                     all_k_resolutions|                                                                                                                                         all_k_results|                                                                                                                                       all_k_distances|                                                                                                                                all_k_cosine_distances|all_k_aux_labels|
+----------------------------------------+-------+----------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|               major depressive disorder|PROBLEM|      6A71|           recurrent depressive disorder|recurrent depressive disorder:::secondary mood syndrome, with depressive symptoms:::current depressive episode with melancholia:::other specified r...|6A71:::6E62.0:::6A80.3:::6A71.Y:::6A71.2:::6A80.2:::6A71.4:::6A73:::6A71.Z:::6A71.5:::6A25.2:::6C40.70:::6A61.3:::6A61.5:::6A60.7:::6A60.5:::6C43.7...|4.7217:::6.6189:::7.2678:::7.5443:::7.8206:::7.8908:::7.9318:::7.9466:::8.1707:::8.2523:::8.5598:::8.5884:::8.6755:::8.7597:::8.9602:::9.0284:::9.1...|0.0330:::0.0655:::0.0801:::0.0862:::0.0933:::0.0935:::0.0940:::0.0949:::0.1032:::0.1063:::0.1131:::0.1105:::0.1153:::0.1154:::0.1206:::0.1248:::0.1...|                |
|            generalized anxiety disorder|PROBLEM|      6B00|            generalised anxiety disorder|generalised anxiety disorder:::alcohol-induced anxiety disorder:::social anxiety disorder:::separation anxiety disorder:::secondary anxiety syndrom...|6B00:::6C40.71:::6B04:::6B05:::6E63:::6C43.71:::6A73:::6C48.40:::6C4B.71:::6C41.71:::6C4F.71:::6C49.61:::6B44:::6C44.71:::6B43:::6C20:::6C42.71:::6...|3.7698:::5.4005:::5.4946:::6.2958:::6.5870:::6.7308:::6.9875:::7.4471:::7.4568:::7.4935:::8.2124:::8.2393:::8.4184:::8.7823:::8.8752:::8.9603:::9.0...|0.0214:::0.0438:::0.0454:::0.0595:::0.0659:::0.0686:::0.0735:::0.0849:::0.0835:::0.0846:::0.1027:::0.1028:::0.1065:::0.1201:::0.1180:::0.1189:::0.1...|                |
|          post-traumatic stress disorder|PROBLEM|      6B40|          post traumatic stress disorder|post traumatic stress disorder:::complex post traumatic stress disorder:::bodily distress disorder:::severe bodily distress disorder:::moderate bod...|6B40:::6B41:::6C20:::6C20.2:::6C20.1:::6A71:::6B43:::6A73:::6E62.0:::6A23:::6B42:::6E65:::6B04:::6A23.1:::6C4B.70:::6C4B.71:::6C43.70:::6C4F.71:::6...|2.2115:::4.8253:::8.7386:::9.4150:::9.4348:::9.6083:::9.6641:::9.7994:::9.8663:::9.9743:::10.0094:::10.0257:::10.0687:::10.2637:::10.2790:::10.2860...|0.0074:::0.0353:::0.1134:::0.1306:::0.1333:::0.1373:::0.1402:::0.1448:::0.1460:::0.1506:::0.1520:::0.1523:::0.1526:::0.1604:::0.1590:::0.1592:::0.1...|                |
|attention deficit hyperactivity disorder|PROBLEM|      6A05|attention deficit hyperactivity disorder|attention deficit hyperactivity disorder:::attention deficit hyperactivity disorder, combined presentation:::attention deficit hyperactivity disord...|6A05:::6A05.2:::6A05.0:::6A05.Y:::6A05.1:::6B20:::6A05.Z:::6A21.2:::6C90:::6A21:::6B60:::6A02:::6B21:::6C91:::6A21.1:::6E64:::6D10.2:::6B60.1:::6B4...|0.0000:::5.2815:::6.3980:::7.0887:::7.5034:::9.0577:::9.4166:::10.5818:::10.5984:::10.6765:::10.7369:::10.9379:::10.9599:::11.0425:::11.0438:::11.1...|0.0000:::0.0419:::0.0612:::0.0767:::0.0842:::0.1212:::0.1375:::0.1698:::0.1651:::0.1722:::0.1698:::0.1768:::0.1773:::0.1791:::0.1860:::0.1879:::0.1...|                |
+----------------------------------------+-------+----------+----------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd11_mental_health|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd11_code]|
|Language:|en|
|Size:|2.5 MB|
|Case sensitive:|false|
