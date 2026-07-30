---
layout: model
title: Sentence Entity Resolver for ICD11
author: John Snow Labs
name: sbiobertresolve_icd11
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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_en_6.4.1_3.4_1782797735696.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_icd11_en_6.4.1_3.4_1782797735696.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11", "en", "clinical/models") \
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


data = spark.createDataFrame([["""The 68-year-old male patient presents with a 5-year history of sporadic Parkinson disease complicated by chronic insomnia that has progressively worsened over the past twelve months.
Laboratory workup revealed chronic posthaemorrhagic anaemia attributed to long-term NSAID use, alongside combined diastolic and systolic hypertension requiring adjustment of his antihypertensive regimen.
Follow-up MRI confirmed glioblastoma of brain in the right temporal lobe, for which the multidisciplinary oncology team has recommended immediate neurosurgical consultation."""]]).toDF("text")

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

icd_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11", "en", "clinical/models") \
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


data = spark.createDataFrame([["""The 68-year-old male patient presents with a 5-year history of sporadic Parkinson disease complicated by chronic insomnia that has progressively worsened over the past twelve months.
Laboratory workup revealed chronic posthaemorrhagic anaemia attributed to long-term NSAID use, alongside combined diastolic and systolic hypertension requiring adjustment of his antihypertensive regimen.
Follow-up MRI confirmed glioblastoma of brain in the right temporal lobe, for which the multidisciplinary oncology team has recommended immediate neurosurgical consultation."""]]).toDF("text")

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

val icd_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_icd11", "en", "clinical/models")
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


val data = Seq("The 68-year-old male patient presents with a 5-year history of sporadic Parkinson disease complicated by chronic insomnia that has progressively worsened over the past twelve months.
Laboratory workup revealed chronic posthaemorrhagic anaemia attributed to long-term NSAID use, alongside combined diastolic and systolic hypertension requiring adjustment of his antihypertensive regimen.
Follow-up MRI confirmed glioblastoma of brain in the right temporal lobe, for which the multidisciplinary oncology team has recommended immediate neurosurgical consultation.").toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash


+------------------------------------------------+-------+----------+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|                                       ner_chunk| entity|ICD11_code|                                 resolutions|                                                                                                                                     all_k_resolutions|                                                                                                                                         all_k_results|                                                                                                                                       all_k_distances|                                                                                                                                all_k_cosine_distances|all_k_aux_labels|
+------------------------------------------------+-------+----------+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+
|                      sporadic Parkinson disease|PROBLEM|   8A00.00|                  sporadic parkinson disease|sporadic parkinson disease:::parkinson disease, unspecified:::atypical parkinsonism, unspecified:::secondary parkinsonism, unspecified:::parkinsoni...|8A00.00:::8A00.0Z:::8A00.1Z:::8A00.2Z:::8A00.Z:::8A00.0:::8B44.0Z:::8A00.01:::8A03.2:::8E00:::8A03.2Z:::8A00.1:::8A00:::8A00.3:::XH50P7:::XH8GG7:::...|0.0000:::9.6161:::10.4703:::10.8449:::10.9659:::11.0528:::11.3415:::11.5735:::11.5828:::11.9273:::12.0736:::12.0737:::12.1910:::12.2703:::12.4275::...|0.0000:::0.1549:::0.1859:::0.2011:::0.2007:::0.1974:::0.2147:::0.2161:::0.2210:::0.2370:::0.2406:::0.2393:::0.2413:::0.2435:::0.2691:::0.2678:::0.2...|                |
|                                chronic insomnia|PROBLEM|      7A00|                            chronic insomnia|chronic insomnia:::insomnia disorder (tm2):::insomnia disorder (tm1):::short-term insomnia:::dyssomnia:::somnolence disorder (tm1):::idiopathic hyp...|7A00:::SQ24:::SD84:::7A01:::MB43:::SD85:::7A21:::7A0Z:::SQ40:::SA80:::7A25:::SM3B:::MG30.00:::MG30.0:::MG30.02:::FB56.2:::7B02.1:::7B00.1:::SP97:::...|0.0000:::6.5516:::7.0140:::7.2155:::8.9452:::9.2790:::9.3440:::9.3777:::9.5424:::9.7302:::9.8528:::10.0789:::10.1589:::10.1912:::10.3415:::10.3417:...|0.0000:::0.0649:::0.0745:::0.0783:::0.1196:::0.1325:::0.1313:::0.1375:::0.1385:::0.1441:::0.1475:::0.1549:::0.1527:::0.1537:::0.1578:::0.1617:::0.1...|                |
|                chronic posthaemorrhagic anaemia|PROBLEM|   3A00.01|            chronic posthaemorrhagic anaemia|chronic posthaemorrhagic anaemia:::acute posthaemorrhagic anaemia:::anaemia due to acute disease:::scorbutic anaemia:::refractory anaemia:::drug-in...|3A00.01:::3A94:::3A90:::3A03.2:::2A30:::3A70.10:::BE14.A:::3A01.30:::3B81.1:::DB91:::NA07.86:::8B24.0:::3A21.1:::3A71:::3A70:::3A71.1:::NE81.3:::ME...|0.0000:::5.8242:::9.7957:::9.8368:::9.8499:::10.1266:::10.5007:::10.6165:::10.7321:::10.7958:::10.8435:::10.9423:::10.9443:::10.9590:::10.9608:::10...|0.0000:::0.0529:::0.1477:::0.1553:::0.1498:::0.1605:::0.1776:::0.1722:::0.1886:::0.1844:::0.1808:::0.1875:::0.1890:::0.1846:::0.1870:::0.1918:::0.2...|                |
|             diastolic and systolic hypertension|PROBLEM|    BA00.0|combined diastolic and systolic hypertension|combined diastolic and systolic hypertension:::combined diastolic and systolic secondary hypertension:::hypertensive heart disease:::secondary hype...|BA00.0:::BA04.0:::BA01:::BA04:::BA00:::9C61.01:::BB01.0:::JA23:::DB99.3:::BB01:::BB01.4:::BA04.Y:::BA02:::BA04.Z:::BA04.2:::BA03:::BA00.Y:::KB45:::...|3.6370:::4.9906:::7.1918:::7.2196:::7.3080:::8.6505:::9.3156:::9.5562:::9.7624:::9.9468:::10.0080:::10.0890:::10.1195:::10.1859:::10.2332:::10.3164...|0.0201:::0.0385:::0.0780:::0.0806:::0.0814:::0.1139:::0.1296:::0.1376:::0.1452:::0.1486:::0.1529:::0.1605:::0.1549:::0.1677:::0.1651:::0.1610:::0.1...|                |
|glioblastoma of brain in the right temporal lobe|PROBLEM|   2A00.00|                       glioblastoma of brain|glioblastoma of brain:::epithelioid glioblastoma:::giant cell glioblastoma:::infant-type hemispheric glioma:::gliomas of brain:::glioblastoma of sp...|2A00.00:::XH2BA5:::XH8UC5:::XH4ZM8:::2A00.0:::2A02.00:::2A00.4:::XH1L48:::XH4101:::XH2SS9:::XH4FN3:::XH29Q5:::XH7M44:::2A00.10:::XH6C35:::XH12D2:::...|8.5497:::9.4256:::9.4310:::9.9133:::9.9814:::10.0810:::10.2381:::10.3549:::10.3699:::10.5140:::10.5983:::10.6097:::10.7732:::10.7932:::10.8193:::10...|0.1161:::0.1428:::0.1407:::0.1582:::0.1592:::0.1650:::0.1676:::0.1783:::0.1737:::0.1823:::0.1859:::0.1906:::0.1897:::0.1862:::0.1938:::0.1933:::0.1...|                |
+------------------------------------------------+-------+----------+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+


```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_icd11|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[icd11_code]|
|Language:|en|
|Size:|103.1 MB|
|Case sensitive:|false|
