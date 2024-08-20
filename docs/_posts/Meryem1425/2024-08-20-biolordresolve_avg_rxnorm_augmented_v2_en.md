---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023 embeddings)
author: John Snow Labs
name: biolordresolve_avg_rxnorm_augmented_v2
date: 2024-08-20
tags: [licensed, en, rxnorm, biolord, entity_resolution, cinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.4.0
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using mpnet_embeddings_biolord_2023 embeddings. It trained on the augmented version of the dataset used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in the all_k_aux_labels column.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_v2_en_5.4.0_3.0_1724127179603.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_v2_en_5.4.0_3.0_1724127179603.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented_v2", "en", "clinical/models")\
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

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented_v2", "en", "clinical/models")
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
          rxnorm_resolver))



val data = Seq([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|        ner_chunk|rxnorm_code|entity|                                 all_k_resolutions|                                     all_k_results|                                   all_k_distances|                            all_k_cosine_distances|                                  all_k_aux_labels|
+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
|          aspirin|    1154070|  DRUG|aspirin Pill[aspirin Pill]:::aspirin Oral Produ...|1154070:::1154069:::368473:::830532:::1299851::...|0.4035:::0.4122:::0.4906:::0.4908:::0.4995:::0....|0.0814:::0.0849:::0.1203:::0.1204:::0.1248:::0....|Clinical Dose Group:::Clinical Dose Group:::Bra...|
|Albuterol inhaler|     801094|  DRUG|albuterol Metered Dose Inhaler [Ventolin][albut...|801094:::2108228:::746762:::745682:::2108257:::...|0.4221:::0.4684:::0.4786:::0.5358:::0.5424:::0....|0.0891:::0.1097:::0.1145:::0.1435:::0.1471:::0....|Branded Drug Form:::Branded Drug Form:::Branded...|
|    Coumadin 5 mg|     855334|  DRUG|Coumadin 5 MG Oral Tablet [warfarin sodium 5 MG...|855334:::855297:::432467:::451604:::333664:::85...|0.5419:::0.5466:::0.5577:::0.5817:::0.6057:::0....|0.1468:::0.1494:::0.1555:::0.1692:::0.1835:::0....|Branded Drug:::Branded Drug Comp:::Clinical Dru...|
|metformin 1000 mg|     860997|  DRUG|metformin hydrochloride 1000 MG [Fortamet][metf...|860997:::861004:::861006:::316256:::583195:::86...|0.3527:::0.3679:::0.3897:::0.3914:::0.4724:::0....|0.0622:::0.0677:::0.0759:::0.0766:::0.1116:::0....|Branded Drug Comp:::Clinical Drug:::Branded Dru...|
| Lisinopril 10 mg|     311354|  DRUG|lisinopril 5 MG Oral Tablet:::lisinopril 2.5 MG...|311354:::316152:::197885:::201381:::567581:::57...|0.4696:::0.5070:::0.5200:::0.5214:::0.5283:::0....|0.1103:::0.1285:::0.1352:::0.1359:::0.1395:::0....|Clinical Drug:::Clinical Drug Comp:::Clinical D...|
+-----------------+-----------+------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+--------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_avg_rxnorm_augmented_v2|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|