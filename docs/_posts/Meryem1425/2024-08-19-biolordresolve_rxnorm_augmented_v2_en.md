---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_rxnorm_augmented_v2
date: 2024-08-19
tags: [licensed, en, biolord, rxnorm, entity_resolution, clinical]
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

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using mpnet_embeddings_biolord_2023_c embeddings. It trained on the augmented version of the dataset used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in the all_k_aux_labels column.

## Predicted Entities



{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_v2_en_5.4.0_3.0_1724078508724.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_v2_en_5.4.0_3.0_1724078508724.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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
    .setOutputCol("ner")\

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented_v2", "en", "clinical/models")\
    .setInputCols(["embeddings"]) \
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

text= "The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily."

data = spark.createDataFrame([[text]]).toDF("text")

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

val biolord_embedding = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c", "en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented_v2", "en", "clinical/models")
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

val data = Seq("The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily.").toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
+-----------------+------+-----------+--------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|        ner_chunk|entity|rxnorm_code|                                                    resolution|                                                                   all_k_results|                                                                 all_k_distances|                                                          all_k_cosine_distances|                                                              all_k_resolutions |                                                                all_k_aux_labels|
+-----------------+------+-----------+--------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
|          aspirin|  DRUG|       1191|                                              aspirin[aspirin]|1191:::1154070:::1295740:::370611:::218266:::2269660:::370940:::1172167:::215...|0.3779:::0.4650:::0.4900:::0.5611:::0.6042:::0.6118:::0.6139:::0.6193:::0.622...|0.0714:::0.1081:::0.1200:::0.1574:::0.1826:::0.1871:::0.1884:::0.1917:::0.193...|aspirin[aspirin]:::aspirin Pill[aspirin Pill]:::aspirin Oral Powder Product::...|Ingredient:::Clinical Dose Group:::Clinical Dose Group:::Clinical Drug Form::...|
|Albuterol inhaler|  DRUG|     745678|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]|745678:::745790:::1163444:::1154602:::2108226:::247840:::1649560:::745679:::3...|0.5321:::0.5416:::0.5540:::0.5618:::0.6010:::0.6078:::0.6085:::0.6129:::0.620...|0.1416:::0.1466:::0.1535:::0.1578:::0.1806:::0.1847:::0.1851:::0.1878:::0.192...|albuterol Metered Dose Inhaler[albuterol Metered Dose Inhaler]:::levalbuterol...|Clinical Drug Form:::Clinical Drug Form:::Clinical Dose Group:::Clinical Dose...|
|    Coumadin 5 mg|  DRUG|     855313|                             warfarin sodium 2.5 MG [Coumadin]|855313:::855333:::855325:::855314:::855334:::855339:::855345:::451604:::43874...|0.4486:::0.4753:::0.5334:::0.5567:::0.5640:::0.5674:::0.5748:::0.5764:::0.578...|0.1006:::0.1130:::0.1423:::0.1549:::0.1590:::0.1610:::0.1652:::0.1661:::0.167...|warfarin sodium 2.5 MG [Coumadin]:::warfarin sodium 5 MG [Coumadin]:::warfari...|Branded Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Branded Drug:::Br...|
|metformin 1000 mg|  DRUG|     316255|                          metformin 1000 MG[metformin 1000 MG]|316255:::860995:::428759:::1807894:::861004:::316257:::861009:::860999:::1593...|0.2907:::0.4766:::0.5041:::0.5346:::0.5436:::0.5469:::0.5890:::0.5946:::0.609...|0.0423:::0.1136:::0.1270:::0.1429:::0.1478:::0.1495:::0.1735:::0.1768:::0.185...|metformin 1000 MG[metformin 1000 MG]:::metformin hydrochloride 1000 MG[metfor...|Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Clinical Drug:::Cli...|
| Lisinopril 10 mg|  DRUG|     314076|                                  lisinopril 10 MG Oral Tablet|314076:::316151:::316153:::197885:::316155:::563611:::565846:::898349:::56757...|0.3809:::0.4221:::0.5944:::0.6129:::0.6354:::0.6400:::0.6502:::0.6780:::0.682...|0.0725:::0.0891:::0.1767:::0.1878:::0.2019:::0.2048:::0.2114:::0.2299:::0.233...|lisinopril 10 MG Oral Tablet:::lisinopril 10 MG[lisinopril 10 MG]:::lisinopri...|Clinical Drug:::Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Cli...|
+-----------------+------+-----------+--------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_rxnorm_augmented_v2|
|Compatibility:|Healthcare NLP 5.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|
