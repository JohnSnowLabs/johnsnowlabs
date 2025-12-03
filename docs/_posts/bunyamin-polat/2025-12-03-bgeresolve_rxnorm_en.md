---
layout: model
title: Sentence Entity Resolver for RxNorm Codes (bge_base_en_v1_5_onnx)
author: John Snow Labs
name: bgeresolve_rxnorm
date: 2025-12-03
tags: [resolver, rxnorm, en, licensed, clinical, bge, sentence_entity_resolver]
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

This model maps drug entities to RxNorm codes using `bge_base_en_v1_5_onnx` Sentence BGE Embeddings. It leverages contextual embeddings to improve code resolution accuracy for drug concepts.

## Predicted Entities

`RxNorm Codes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_en_6.2.0_3.4_1764801566299.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_en_6.2.0_3.4_1764801566299.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("word_embeddings")

ner_posology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_posology_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_rxnorm", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_posology,
    ner_posology_converter,
    chunk2doc,
    bge_embeddings,
    rxnorm_resolver
])

text = """The patient was prescribed aspirin and Albuterol inhaler for respiratory issues. She also takes apixaban 5 mg, metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure."""

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
    .setOutputCol("word_embeddings")

ner_posology = medical.MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_posology_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

bge_embeddings = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")

rxnorm_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_rxnorm", "en", "clinical/models")\
    .setInputCols(["bge_embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline().setStages([
    document_assembler,
    sentence_detector,
    tokenizer,
    word_embeddings,
    ner_posology,
    ner_posology_converter,
    chunk2doc,
    bge_embeddings,
    rxnorm_resolver
])

text = """The patient was prescribed aspirin and Albuterol inhaler for respiratory issues. She also takes apixaban 5 mg, metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure."""

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
    .setOutputCol("word_embeddings")

val nerPosology = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val nerPosologyConverter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val bgeEmbeddings = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")

val rxnormResolver = SentenceEntityResolverModel.pretrained("bgeresolve_rxnorm", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler,
    sentenceDetector,
    tokenizer,
    wordEmbeddings,
    nerPosology,
    nerPosologyConverter,
    chunk2doc,
    bgeEmbeddings,
    rxnormResolver
))

val data = Seq("""The patient was prescribed aspirin and Albuterol inhaler for respiratory issues. She also takes apixaban 5 mg, metformin 1000 mg for diabetes, and Lisinopril 10 mg for blood pressure.""").toDF("text")

val result = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

|sent_id|ner_chunk        |entity|rxnorm_code|resolutions              |all_codes                                      |all_resolutions                                |
|-------|-----------------|------|-----------|-------------------------|-----------------------------------------------|-----------------------------------------------|
|0      |aspirin          |DRUG  |1191       |aspirin                  |[1191, 1295740, 1154070, 1001473, 218266, ...] |[aspirin, aspirin product, aspirin pill, ecpi...]|
|0      |Albuterol inhaler|DRUG  |1154602    |albuterol inhalant product|[1154602, 745678, 435, 1154606, 1649559, ...]  |[albuterol inhalant product, albuterol metered...]|
|1      |apixaban 5 mg    |DRUG  |1364444    |apixaban 5 mg            |[1364444, 1364431, 1364446, 1364445, 1364447, ...]|[apixaban 5 mg, apixaban 2.5 mg, apixaban 5 mg...]|
|1      |metformin 1000 mg|DRUG  |316255     |metformin 1000 mg        |[316255, 860995, 330861, 860997, 429841, ...]  |[metformin 1000 mg, metformin hydrochloride 10...]|
|1      |Lisinopril 10 mg |DRUG  |316151     |lisinopril 10 mg         |[316151, 314076, 563611, 565846, 567576, ...]  |[lisinopril 10 mg, lisinopril 10mg 10 mg, lisi...]|

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_rxnorm|
|Compatibility:|Healthcare NLP 6.2.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|