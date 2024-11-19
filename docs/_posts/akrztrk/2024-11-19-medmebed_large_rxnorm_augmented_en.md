---
layout: model
title: Sentence Entity Resolver for RxNorm (bge_medembed_large_v0_1 embeddings)
author: John Snow Labs
name: medmebed_large_rxnorm_augmented
date: 2024-11-19
tags: [licensed, en, medembed, rxnorm, entity_resolution, clinical]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.5.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `[bge_medembed_large_v0_1](https://sparknlp.org/2024/10/21/bge_medembed_large_v0_1_en.html)` embeddings.
Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

## Predicted Entities

`RxNorm Codes`, `Concept Classes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medmebed_large_rxnorm_augmented_en_5.5.0_3.4_1732046847333.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medmebed_large_rxnorm_augmented_en_5.5.0_3.4_1732046847333.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

bge_embedding = BGEEmbeddings.pretrained("bge_medembed_large_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("medmebed_large_rxnorm_augmented", "en", "clinical/models")\
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
                                       bge_embedding,
                                       rxnorm_resolver])

data = spark.createDataFrame([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"""]]).toDF("text")

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

val bge_embedding = BGEEmbeddings.pretrained("bge_medembed_large_v0_1","en")
    .setInputCols(["ner_chunk_doc"])
    .setOutputCol("embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("medmebed_large_rxnorm_augmented", "en", "clinical/models")
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



val data = Seq([["""The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"""]]).toDF("text")

val result = resolver_pipeline.fit(data).transform(data)
```
</div>

## Results

```bash

+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|        ner_chunk|entity|rxnorm_code|                                                               all_k_resolutions|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|                                                                all_k_aux_labels|
+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|          aspirin|  DRUG|       1191|aspirin[aspirin]:::Empirin[Empirin]:::aluminum aspirin[aluminum aspirin]:::as...|1191:::202547:::611:::329295:::335953:::218266:::317299:::1295740:::437699:::...|0.4045:::0.4813:::0.4893:::0.4898:::0.4922:::0.4936:::0.4995:::0.5047:::0.508...|0.0818:::0.1158:::0.1197:::0.1200:::0.1211:::0.1218:::0.1247:::0.1274:::0.129...|Ingredient:::Brand Name:::Ingredient:::Clinical Drug Comp:::Clinical Drug Com...|
|Albuterol inhaler|  DRUG|    1649559|albuterol Dry Powder Inhaler[albuterol Dry Powder Inhaler]:::albuterol[albute...|1649559:::435:::307779:::104514:::2108233:::1154602:::745678:::252298:::11546...|0.4190:::0.4468:::0.4481:::0.4511:::0.4546:::0.4591:::0.4687:::0.4738:::0.480...|0.0878:::0.0998:::0.1004:::0.1017:::0.1033:::0.1054:::0.1099:::0.1122:::0.115...|Clinical Drug Form:::Ingredient:::Clinical Drug:::Clinical Drug:::Clinical Dr...|
|    Coumadin 5 mg|  DRUG|     855333|warfarin sodium 5 MG [Coumadin]:::warfarin sodium 7.5 MG [Coumadin]:::Warfari...|855333:::855345:::330536:::855313:::855334:::855314:::438740:::855339:::85532...|0.2281:::0.3900:::0.4020:::0.4085:::0.4208:::0.4322:::0.4334:::0.4401:::0.455...|0.0260:::0.0760:::0.0808:::0.0834:::0.0885:::0.0934:::0.0939:::0.0968:::0.103...|Branded Drug Comp:::Branded Drug Comp:::Clinical Drug Comp:::Branded Drug Com...|
|metformin 1000 mg|  DRUG|     316255|metformin 1000 MG[metformin 1000 MG]:::metformin hydrochloride 1000 MG[metfor...|316255:::860995:::332809:::316256:::861004:::330861:::316257:::860999:::43850...|0.0933:::0.3953:::0.4180:::0.4216:::0.4262:::0.4406:::0.4515:::0.4518:::0.465...|0.0044:::0.0781:::0.0873:::0.0889:::0.0908:::0.0971:::0.1019:::0.1020:::0.108...|Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug ...|
| Lisinopril 10 mg|  DRUG|     316151|lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 MG Oral Tablet:::lisinopri...|316151:::314076:::563611:::567576:::316156:::197885:::316153:::104377:::31615...|0.1448:::0.2378:::0.3672:::0.3938:::0.4047:::0.4163:::0.4367:::0.4398:::0.441...|0.0105:::0.0283:::0.0674:::0.0775:::0.0819:::0.0867:::0.0954:::0.0967:::0.097...|Clinical Drug Comp:::Clinical Drug:::Branded Drug Comp:::Branded Drug Comp:::...|
+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medmebed_large_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[BGE]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.5 GB|
|Case sensitive:|false|
