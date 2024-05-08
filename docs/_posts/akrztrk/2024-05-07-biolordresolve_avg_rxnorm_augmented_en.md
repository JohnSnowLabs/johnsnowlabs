---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023 embeddings)
author: John Snow Labs
name: biolordresolve_avg_rxnorm_augmented
date: 2024-05-07
tags: [licensed, en, biolord, rxnorm, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023` embeddings. It trained on the augmented version of the dataset used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_en_5.3.1_3.4_1715083589743.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_en_5.3.1_3.4_1715083589743.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented", "en", "clinical/models")\
    .setInputCols(["embeddings"])\
     .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       biolord_embedding,
                                       rxnorm_resolver])

data = spark.createDataFrame([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."""]]).toDF("text")

result = resolver_pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(["document"])
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols(["sentence"])
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner = MedicalNerModel.pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(["DRUG"])

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023", "en")
    .setInputCols(["ner_chunk_doc"])
    .setOutputCol("embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented", "en", "clinical/models")
    .setInputCols(["embeddings"])
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new PipelineModel().setStages(Array(
          document_assembler,
          sentenceDetectorDL,
          tokenizer,
          word_embeddings,
          ner,
          ner_converter,
          c2doc,
          biolord_embedding,
          rxnorm_resolver])


val data = Seq([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash

+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|        ner_chunk|entity|rxnorm_code|                                                                      resolution|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|                                                              all_k_resolutions |                                                                all_k_aux_labels|
+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|          aspirin|  DRUG|    1295740|                                                     aspirin oral powder product|1295740:::1191:::1154070:::1154068:::1299851:::368658:::830532:::368480:::830...|0.3227:::0.3484:::0.4167:::0.4580:::0.4739:::0.4848:::0.4890:::0.4946:::0.504...|0.0521:::0.0607:::0.0868:::0.1049:::0.1123:::0.1175:::0.1196:::0.1223:::0.127...|aspirin oral powder product:::aspirin [aspirin]:::aspirin pill [aspirin pill]...|Clinical Dose Group:::Ingredient:::Clinical Dose Group:::Clinical Dose Group:...|
|Albuterol inhaler|  DRUG|     745678|                 albuterol metered dose inhaler [albuterol metered dose inhaler]|745678:::2108246:::2108257:::1360201:::1649559:::1154604:::746762:::745790:::...|0.4481:::0.5102:::0.5241:::0.5246:::0.5343:::0.5437:::0.5609:::0.5619:::0.571...|0.1004:::0.1301:::0.1373:::0.1376:::0.1427:::0.1478:::0.1573:::0.1579:::0.163...|albuterol metered dose inhaler [albuterol metered dose inhaler]:::albuterol i...|Clinical Drug Form:::Branded Drug Form:::Branded Drug Form:::Clinical Drug:::...|
|    Coumadin 5 mg|  DRUG|     855345|                                               warfarin sodium 7.5 mg [coumadin]|855345:::855314:::451604:::432467:::855346:::855298:::855333:::855290:::85532...|0.4956:::0.5290:::0.5292:::0.5458:::0.5563:::0.5613:::0.5706:::0.5999:::0.609...|0.1228:::0.1399:::0.1400:::0.1489:::0.1548:::0.1575:::0.1628:::0.1799:::0.185...|warfarin sodium 7.5 mg [coumadin]:::coumadin 2.5 mg oral tablet [warfarin sod...|Branded Drug Comp:::Branded Drug:::Clinical Drug Comp:::Clinical Drug:::Brand...|
|metformin 1000 mg|  DRUG|     861005|metformin hydrochloride 1000 mg [glucophage] [metformin hydrochloride 1000 mg...|861005:::861014:::861004:::316255:::316256:::860999:::861006:::861016:::86101...|0.3233:::0.3393:::0.3679:::0.3830:::0.3914:::0.3955:::0.4197:::0.4369:::0.453...|0.0523:::0.0576:::0.0677:::0.0733:::0.0766:::0.0782:::0.0881:::0.0954:::0.102...|metformin hydrochloride 1000 mg [glucophage] [metformin hydrochloride 1000 mg...|Branded Drug Comp:::Branded Drug Comp:::Clinical Drug:::Clinical Drug Comp:::...|
| Lisinopril 10 mg|  DRUG|     314076|                     lisinopril 10 mg oral tablet [lisinopril 10 mg oral tablet]|314076:::104377:::567576:::197884:::206765:::104378:::1806881:::567581:::3161...|0.4719:::0.4766:::0.4793:::0.4888:::0.4978:::0.5117:::0.5175:::0.5283:::0.542...|0.1114:::0.1136:::0.1149:::0.1195:::0.1239:::0.1309:::0.1339:::0.1395:::0.147...|lisinopril 10 mg oral tablet [lisinopril 10 mg oral tablet]:::lisinopril 10 m...|Clinical Drug:::Branded Drug:::Branded Drug Comp:::Clinical Drug:::Branded Dr...|
+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_avg_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|

## Dependency
This model can be used with spark v3.4.0 and above versions.
