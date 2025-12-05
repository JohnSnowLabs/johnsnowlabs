---
layout: model
title: Sentence Entity Resolver for CPT Codes (bge_base_en_v1_5_onnx)
author: John Snow Labs
name: bgeresolve_cpt
date: 2025-12-05
tags: [resolver, cpt, en, licensed, clinical, bge, sentence_embeddings]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.2.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities (Observation, Procedures, Tests, Treatments, Drug) to their corresponding CPT (Current Procedural Terminology) codes using `bge_base_en_v1_5_onnx` embeddings. It uses `bge_base_en_v1_5_onnx` embeddings and provides multiple resolution candidates with confidence scores, making it ideal for accurate procedural code assignment in clinical documentation.

## Predicted Entities

`CPT Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_cpt_en_6.2.0_3.4_1764900772092.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_cpt_en_6.2.0_3.4_1764900772092.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test", "Treatment", "Clinical_Dept"])

chunk2doc = Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

cpt_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_cpt", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("cpt_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    bge_embeddings,
    cpt_resolver
])

text = """A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence_detector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("embeddings")

ner_model = medical.MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "embeddings"])\
    .setOutputCol("ner")

ner_model_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["Procedure", "Test", "Treatment", "Clinical_Dept"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols(["ner_chunk"])\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

cpt_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_cpt", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("cpt_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_model,
    ner_model_converter,
    chunk2doc,
    bge_embeddings,
    cpt_resolver
])

text = """A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation."""

data = spark.createDataFrame([[text]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(Array("sentence"))
    .setOutputCol("token")

val wordEmbeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("embeddings")

val nerModel = MedicalNerModel.pretrained("ner_jsl", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "embeddings"))
    .setOutputCol("ner")

val nerModelConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("Procedure", "Test", "Treatment", "Clinical_Dept"))

val chunk2doc = new Chunk2Doc()
    .setInputCols(Array("ner_chunk"))
    .setOutputCol("ner_chunk_doc")

val bgeEmbeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")

val cptResolver = SentenceEntityResolverModel.pretrained("bgeresolve_cpt", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("cpt_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerModel,
    nerModelConverter,
    chunk2doc,
    bgeEmbeddings,
    cptResolver
))

val data = Seq("""A 28-year-old female underwent episiotomy during vaginal delivery. Pulse oximetry was monitored continuously throughout the procedure. Due to postpartum hemorrhage, blood transfusion was administered. The patient was transferred to the inpatient hospital for overnight observation.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|sent_id|ner_chunk         |entity       |cpt_code|resolutions       |all_codes                                              |all_resolutions                                                                                                              |
|-------|------------------|-------------|--------|------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
|0      |episiotomy        |Procedure    |59300   |episiotomy        |[59300, 59409, 59410, 59614, 59612, 59610, 100...]     |[episiotomy, vaginal delivery with episiotomy, ...]                                                                          |
|1      |Pulse oximetry    |Test         |94760   |pulse oximetry    |[94760, 99453, 94761, 82810, 94762, 1013256, 8...]     |[pulse oximetry, device pulse oximetry, noninvasive ear or pulse oximetry for oxygen saturation single determination, ...]   |
|2      |blood transfusion |Procedure    |36430   |blood transfusion |[36430, 86950, 38243, 36450, 0232T, 36460, 382...]     |[blood transfusion, white blood cell transfusion, ...]                                                                       |
|3      |inpatient hospital|Clinical_Dept|1021881 |inpatient hospital|[1021881, 94003, 1021895, 99236, 1013660, 1013...]     |[inpatient hospital, inpatient care, inpatient hospital care, ...]                                                           |

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_cpt|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[cpt_code]|
|Language:|en|
|Size:|388.0 MB|
|Case sensitive:|false|

## References

**CPT resolver models are removed from the Models Hub due to license restrictions and can only be shared with the users who already have a valid CPT license. If you possess one and wish to use this model, kindly contact us at support@johnsnowlabs.com.**
