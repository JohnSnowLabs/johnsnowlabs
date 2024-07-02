---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_rxnorm_augmented
date: 2024-07-02
tags: [licensed, en, biolord, rxnorm, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.3
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023_c` embeddings. It trained on the augmented version of the dataset used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_en_5.3.3_3.4_1719924324929.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_en_5.3.3_3.4_1719924324929.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()    .setInputCol("text")    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")    .setInputCols(["document"])    .setOutputCol("sentence")

tokenizer = Tokenizer()    .setInputCols(["sentence"])    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")    .setInputCols(["sentence", "token"])    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")    .setInputCols(["sentence", "token", "word_embeddings"])    .setOutputCol("ner")
ner_converter = NerConverterInternal()    .setInputCols(["sentence", "token", "ner"])    .setOutputCol("ner_chunk")    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()    .setInputCols("ner_chunk")    .setOutputCol("ner_chunk_doc")

biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")    .setInputCols(["ner_chunk_doc"])    .setOutputCol("embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented", "en", "clinical/models")\     .setInputCols(["embeddings"])     .setOutputCol("rxnorm_code")    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       biolord_embedding,
                                       rxnorm_resolver])

data = spark.createDataFrame([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 2.5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")
    .setInputCols("document")
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence","token"))
    .setOutputCol("embeddings")

val ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence","token","embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverter()
    .setInputCols(Array("sentence","token","ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList("DRUG")

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")    .setInputCols(["ner_chunk_doc"])    .setOutputCol("embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented", "en", "clinical/models")
    .setInputCols("embeddings")
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
                               document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner,
                               ner_converter,
                               chunk2doc,
                               biolord_embedding,
                               rxnorm_resolver))

val data = Seq([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 2.5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|        ner_chunk|rxnorm_code|entity|                                 all_k_resolutions|                                     all_k_results|                                   all_k_distances|                            all_k_cosine_distances|                                  all_k_aux_labels|
+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|          aspirin|    1537020|  DRUG|aspirin Effervescent Oral Tablet:::aspirin pill...|1537020:::1154070:::1295740:::1299851:::1154068...|0.3894:::0.4329:::0.5029:::0.5322:::0.5897:::0....|0.0758:::0.0937:::0.1265:::0.1416:::0.1739:::0....|Clinical Drug Form:::Clinical Dose Group:::Clin...|
|Albuterol inhaler|     745678|  DRUG|albuterol metered dose inhaler [albuterol meter...|745678:::2108226:::2108233:::745790:::745679:::...|0.3196:::0.4894:::0.5403:::0.5654:::0.5765:::0....|0.0511:::0.1197:::0.1460:::0.1598:::0.1662:::0....|Clinical Drug Form:::Clinical Drug Form:::Clini...|
|  Coumadin 2.5 mg|     855313|  DRUG|warfarin sodium 2.5 MG [Coumadin]:::warfarin so...|855313:::855303:::855314:::855333:::855304:::43...|0.3695:::0.5485:::0.5511:::0.5690:::0.6115:::0....|0.0683:::0.1504:::0.1518:::0.1619:::0.1869:::0....|Branded Drug Comp:::Branded Drug Comp:::Branded...|
|metformin 1000 mg|     316255|  DRUG|metformin 1000 mg [metformin 1000 mg]:::metform...|316255:::860999:::1807888:::860978:::861004:::4...|0.3005:::0.4992:::0.5267:::0.5375:::0.5537:::0....|0.0452:::0.1246:::0.1387:::0.1445:::0.1533:::0....|Clinical Drug Comp:::Clinical Drug:::Clinical D...|
| Lisinopril 10 mg|     314076|  DRUG|lisinopril 10 MG Oral Tablet:::hydrochlorothiaz...|314076:::197885:::567576:::563611:::565846:::89...|0.3625:::0.6018:::0.6307:::0.6404:::0.6622:::0....|0.0657:::0.1811:::0.1989:::0.2050:::0.2193:::0....|Clinical Drug:::Clinical Drug:::Branded Drug Co...|
+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.3.3+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|