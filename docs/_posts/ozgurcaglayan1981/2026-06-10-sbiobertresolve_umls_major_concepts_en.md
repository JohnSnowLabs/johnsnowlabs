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
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781091117092.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_umls_major_concepts_en_6.4.0_3.4_1781091117092.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
| ner_chunk                     | entity   | umls_code   | resolution                                 | all_k_results                                                                                                                                                                                                                        | all_k_distances                                                                                                                                                                            | all_k_cosine_distances                                                                                                                                                                     | all_k_resolutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:------------------------------|:---------|:------------|:-------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ankle pain                    | PROBLEM  | C4315239    | joint and leg pain                         | C4315239:::C2032293:::C2089776:::C0311395:::C4314128:::C1456822:::C0240726:::C0576209:::C2088499:::C1997427:::C1859884:::C2228033:::C4021587:::C0576208:::C3809984:::C2237509:::C2228039:::C0240386:::C2088049:::C0241238:::C0026858 | 6.7160:::6.9561:::7.1439:::7.2412:::7.2615:::7.3682:::7.3847:::7.4599:::7.4772:::7.5426:::7.6363:::7.6365:::7.6808:::7.7232:::7.7247:::7.7533:::7.7751:::7.7918:::7.7966:::7.8635:::7.9590 | 0.0665:::0.0703:::0.0751:::0.0766:::0.0764:::0.0786:::0.0798:::0.0803:::0.0828:::0.0824:::0.0852:::0.0862:::0.0880:::0.0877:::0.0868:::0.0881:::0.0893:::0.0881:::0.0904:::0.0900:::0.0924 | joint and leg pain:::bilateral calf pain:::ankle pain observed on ambulation:::walking leg pain:::distal limb pain:::lower extremity pain walking:::periosteal pain:::ankle joint - painful on movement:::pain of ankle elicited at extreme limits of range of motion:::painful gait:::chronic joint pain:::ankle pain elicited by motion:::costochondral pain:::tenderness of ankle joint:::exertional leg pain:::bilateral ankle pain elicited by motion:::ankle weakness:::movement pain:::pain of ankle elicited by inversion:::standing pain:::rheumatic pain                                      |
| gestational diabetes mellitus | PROBLEM  | C3532257    | uncontrolled gestational diabetes mellitus | C3532257:::C2183115:::C3161145:::C4303558:::C3840222:::C2114054:::C3874269:::C0455488:::C5769536:::C1313937:::C4511231:::C3648970:::C4304438                                                                                         | 4.9178:::5.2183:::6.7683:::7.1690:::7.2158:::7.2549:::7.2947:::7.6202:::8.0201:::8.0206:::8.2793:::8.3303:::8.3393                                                                         | 0.0358:::0.0401:::0.0666:::0.0750:::0.0774:::0.0778:::0.0776:::0.0852:::0.0953:::0.0947:::0.0999:::0.1037:::0.1033                                                                         | uncontrolled gestational diabetes mellitus:::diabetes mellitus during pregnancy:::personal history of gestational diabetes:::maternal history of gestational diabetes:::supervision of high risk pregnancy with history of gestational diabetes mellitus done:::pre-existing maternal diabetes:::maternal history of diabetes mellitus:::h/o: diabetes mellitus:::brachial plexus lesion due to diabetes mellitus:::fh: diabetes mellitus:::lesion of skin due to diabetes mellitus:::gestational diabetes mellitus in pregnancy, controlled:::maternal history of diabetes mellitus type 2 (situation) |
| type two diabetes mellitus    | PROBLEM  | C4016960    | type 2 diabetes mellitus, association with | C4016960:::C4014362:::C3532488:::C3532621:::C2733146:::C1320657:::C3837967:::C1313937:::C0455488:::C6053694:::C4511231:::C4017629:::C3841927:::C3532489                                                                              | 4.3769:::5.4045:::6.1712:::6.3214:::6.3826:::6.4436:::6.4940:::6.8569:::7.2701:::7.3663:::7.7139:::7.7342:::7.7485:::7.7893                                                                | 0.0285:::0.0438:::0.0568:::0.0589:::0.0616:::0.0618:::0.0639:::0.0697:::0.0781:::0.0831:::0.0871:::0.0910:::0.0906:::0.0884                                                                | type 2 diabetes mellitus, association with:::type 2 diabetes mellitus (t2d):::history of diabetes mellitus type 2 (situation):::diabetes mellitus suspected:::uncontrolled type 2 diabetes mellitus (disorder):::diabete type:::diabetes mellitus type 2 susceptibility:::fh: diabetes mellitus:::h/o: diabetes mellitus:::grade 2 diabetes mellitus, ctcae:::skin lesion due to diabetes mellitus:::diabetes mellitus, type ii, digenic:::diabetic problem:::history of diabetes mellitus type i                                                                                                       |
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