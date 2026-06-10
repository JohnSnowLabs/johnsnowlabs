---
layout: model
title: Sentence Entity Resolver for UMLS CUI Codes (Major Concepts)
author: John Snow Labs
name: sbiobertresolve_umls_major_concepts
date: 2026-06-10
tags: [en, entity_resolution, licensed, clinical, umls, major_concepts]
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

This model maps clinical entities to 4 major categories of UMLS CUI codes. It is trained on the 2026AA release of the Unified Medical Language System (UMLS) dataset. The training data covers "Clinical Finding" (T033), "Medical Device" (T074), "Body Part, Organ, or Organ Component" (T023), and "Injury or Poisoning" (T037) semantic types, comprising approximately 1,270,000 name-CUI pairs. The model uses `sbiobert_base_cased_mli_onnx` embeddings.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781093193697.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781093193697.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["Patient received an influenza vaccine and later reported ankle pain. She has a history of gestational diabetes mellitus and type two diabetes mellitus."]]).toDF("text")
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
    .setOutputCol("embeddings")

ner_model = medical.NerModel.pretrained("ner_clinical","en","clinical/models")\
    .setInputCols(["sentence","token","embeddings"])\
    .setOutputCol("clinical_ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","clinical_ner"])\
    .setOutputCol("clinical_ner_chunk")\
    .setWhiteList(["PROBLEM"])

chunk2doc = medical.Chunk2Doc()\
    .setInputCols("clinical_ner_chunk")\
    .setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sbert_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_umls_major_concepts","en","clinical/models")\
    .setInputCols(["sbert_embeddings"])\
    .setOutputCol("resolution")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
])

data = spark.createDataFrame([["Patient received an influenza vaccine and later reported ankle pain. She has a history of gestational diabetes mellitus and type two diabetes mellitus."]]).toDF("text")
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
    .setOutputCol("embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("clinical_ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "clinical_ner"))
    .setOutputCol("clinical_ner_chunk")
    .setWhiteList(Array("PROBLEM"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("clinical_ner_chunk")
    .setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sbert_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_umls_major_concepts", "en", "clinical/models")
    .setInputCols(Array("sbert_embeddings"))
    .setOutputCol("resolution")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, sbert_embedder, resolver
))

val data = Seq("Patient received an influenza vaccine and later reported ankle pain. She has a history of gestational diabetes mellitus and type two diabetes mellitus.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                      | entity   | umls_code   | resolution                                 | all_k_results                                                                                                                                                                                                             | all_k_distances                                                                                                                                                                   | all_k_cosine_distances                                                                                                                                                            | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------------------------|:---------|:------------|:-------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hepatomegaly                   | PROBLEM  | C0019209    | hepatomegaly                               | C0019209:::C3277279:::C5436272:::C1835881:::C4746801:::C3275672:::C0744871:::C0744873:::C1399464:::C5775427:::C0086565:::C5563363:::C3551918:::C5883455:::C2054287:::C4764276:::C2227725:::C0857338:::C4021591            | 0.0072:::4.9152:::5.3459:::5.3965:::5.8476:::6.1865:::6.4947:::6.5779:::7.1451:::7.9376:::8.0301:::8.1377:::8.2148:::8.3183:::8.4253:::8.7290:::8.7448:::8.8419:::8.8901          | 0.0000:::0.0386:::0.0438:::0.0463:::0.0544:::0.0606:::0.0649:::0.0690:::0.0813:::0.0985:::0.1009:::0.1070:::0.1053:::0.1106:::0.1141:::0.1204:::0.1227:::0.1199:::0.1239          | hepatomegaly:::hepatomegaly (variable):::progressive hepatomegaly:::fluctuating hepatomegaly:::hepatomegaly, intermittent:::hepatomegaly, transient:::massive hepatomegaly:::hepatomegaly nodular:::splenomegaly; hepatomegaly:::fetal hepatomegaly:::hepatic function abnormal nos:::hepatomegaly, mild to moderate:::hepatomegaly associated with infection:::hepatomegaly (early-onset):::technetium scan of liver: hepatomegaly:::jaundice status:::abdominal x-ray, ap view: hepatomegaly:::deranged liver function tests:::hepatic ductopenia                                                                                                                                                                                                                                                                             |
| peripheral edema               | PROBLEM  | C1820687    | distal peripheral edema                    | C1820687:::C5970454:::C0521464:::C6053273:::C0544449:::C0577245:::C2825502:::C1822293:::C2038705:::C1328495:::C0745825:::C0474434:::C0456703:::C0239598:::C1851414:::C4551277:::C0476313:::C2219601                       | 4.9970:::7.1707:::7.3667:::7.9493:::7.9676:::8.2377:::8.3377:::8.3708:::8.4964:::8.5113:::8.5226:::8.5227:::8.5930:::8.6449:::8.7224:::8.7399:::8.7584:::8.8265                   | 0.0383:::0.0771:::0.0828:::0.1008:::0.0974:::0.1067:::0.1070:::0.1096:::0.1086:::0.1125:::0.1123:::0.1106:::0.1162:::0.1140:::0.1146:::0.1206:::0.1162:::0.1176                   | distal peripheral edema:::peripheral nerve swelling:::cutaneous edema:::peripheral edema, ctcae:::state of edema:::preputial edema:::vasogenic edema:::periwound edema:::forearm swelling:::wound edema:::lower extremity edema asymmetric:::swelling edema:::myedema:::finger swelling:::peripheral nerve compression:::edema of periwound skin (finding):::groin swelling:::scalp swelling                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| tibial fracture                | PROBLEM  | C0040185    | tibial fracture                            | C0040185:::C0262488:::C0272767:::C3687007:::C5691295:::C0749492:::C2862392:::C0159852:::C1397790:::C0435895                                                                                                               | 0.0072:::4.3259:::4.7913:::4.8150:::5.1589:::5.3061:::5.7201:::5.8100:::5.8214:::5.8488                                                                                           | 0.0000:::0.0294:::0.0356:::0.0372:::0.0424:::0.0455:::0.0513:::0.0536:::0.0543:::0.0557                                                                                           | tibial fracture:::distal tibia fracture:::fracture of tibial shaft:::tibiotarsal fracture:::tibial eminence fracture:::tibia fracture compound:::segmental fracture of tibial shaft:::tibia fibula fracture:::tibial tuberosity fractures:::tibial plafond fracture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ligament tear in the left knee | PROBLEM  | C5566795    | left knee lateral collateral ligament tear | C5566795:::C4721093:::C2116772:::C4749637:::C5768238:::C2864449:::C6063140:::C2119193:::C2138529:::C6063576:::C2156799:::C5924722:::C2142182:::C2864452:::C2142275:::C4047881:::C2142287:::C5224644:::C2864491:::C2186685 | 5.2423:::5.8925:::6.0362:::6.3427:::6.5390:::6.5475:::6.6266:::6.7484:::6.7661:::6.8356:::6.8481:::6.8510:::6.8834:::6.9195:::6.9649:::6.9973:::7.0036:::7.0084:::7.0258:::7.0419 | 0.0427:::0.0538:::0.0561:::0.0634:::0.0668:::0.0673:::0.0687:::0.0712:::0.0715:::0.0726:::0.0728:::0.0740:::0.0742:::0.0758:::0.0752:::0.0767:::0.0781:::0.0770:::0.0776:::0.0777 | left knee lateral collateral ligament tear:::injury of left knee:::tissue injury of left knee:::chondral injury of left knee:::traumatic tear of cruciate ligament of left knee:::peripheral tear of lateral meniscus, current injury, left knee:::fracture of left knee:::dislocation of left knee with tear of lateral cartilage:::crush injury of left knee:::injury of lateral collateral ligament of left knee:::dislocation of left knee:::tear of lateral meniscus of left knee joint:::laceration of left knee:::peripheral tear of lateral meniscus, current injury, left knee, sequela:::aseptic tissue injury of left knee:::acute lateral meniscal tear of left knee:::dehiscence of incision of left knee:::laceration of lateral left knee:::tear of articular cartilage of left knee, current:::left knee trauma |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_umls_major_concepts|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bert_embeddings]|
|Output Labels:|[umls_code]|
|Language:|en|
|Size:|3.7 GB|
|Case sensitive:|false|