---
layout: model
title: Sentence Entity Resolver for RxNorm (bge_medembed_base_v0_1 embeddings)
author: John Snow Labs
name: medembed_base_rxnorm_augmented
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

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `(bge_medembed_base_v0_1)[https://sparknlp.org/2024/10/21/bge_medembed_base_v0_1_en.html]` embeddings.
Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

## Predicted Entities

`RxNorm Codes`, `Concept Classes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medembed_base_rxnorm_augmented_en_5.5.0_3.4_1732045925411.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medembed_base_rxnorm_augmented_en_5.5.0_3.4_1732045925411.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

bge_embedding = BGEEmbeddings.pretrained("bge_medembed_base_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")

rxnorm_resolver = SentenceEntityResolverModel.pretrained("medembed_base_rxnorm_augmented", "en", "clinical/models")\
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

val bge_embedding = BGEEmbeddings.pretrained("bge_medembed_base_v0_1","en")
    .setInputCols(["ner_chunk_doc"])
    .setOutputCol("embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("medembed_base_rxnorm_augmented", "en", "clinical/models")
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
|          aspirin|  DRUG|    1295740|aspirin Oral Powder Product:::aspirin Pill[aspirin Pill]:::Ecpirin[Ecpirin]::...|1295740:::1154070:::1001473:::215568:::1168631:::1172520:::315424:::218266:::...|0.3736:::0.4185:::0.4276:::0.4422:::0.4803:::0.4823:::0.4855:::0.4865:::0.488...|0.0698:::0.0876:::0.0914:::0.0978:::0.1153:::0.1163:::0.1179:::0.1183:::0.119...|Clinical Dose Group:::Clinical Dose Group:::Brand Name:::Brand Name:::Branded...|
|Albuterol inhaler|  DRUG|    1154602|albuterol Inhalant Product[albuterol Inhalant Product]:::albuterol 0.09 MG/AC...|1154602:::1360201:::1649559:::745679:::307779:::2108226:::745790:::1649563:::...|0.4852:::0.5081:::0.5166:::0.5166:::0.5198:::0.5220:::0.5243:::0.5301:::0.531...|0.1177:::0.1291:::0.1334:::0.1334:::0.1351:::0.1362:::0.1374:::0.1405:::0.141...|Clinical Dose Group:::Clinical Drug:::Clinical Drug Form:::Quant Clinical Dru...|
|    Coumadin 5 mg|  DRUG|     855333|warfarin sodium 5 MG [Coumadin]:::warfarin sodium 7.5 MG [Coumadin]:::warfari...|855333:::855345:::855313:::855334:::438740:::855314:::855346:::451601:::45160...|0.2797:::0.3486:::0.3645:::0.4034:::0.4114:::0.4356:::0.4384:::0.4496:::0.450...|0.0391:::0.0608:::0.0664:::0.0814:::0.0846:::0.0949:::0.0961:::0.1011:::0.101...|Branded Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Branded Drug:::Cl...|
|metformin 1000 mg|  DRUG|     316255|metformin 1000 MG[metformin 1000 MG]:::metformin hydrochloride 1000 MG[metfor...|316255:::860995:::429841:::860997:::861005:::861004:::1807888:::861760:::1796...|0.2313:::0.3947:::0.4225:::0.4485:::0.4564:::0.4719:::0.4793:::0.4836:::0.490...|0.0268:::0.0779:::0.0893:::0.1006:::0.1041:::0.1113:::0.1149:::0.1169:::0.120...|Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Branded Drug Comp::...|
| Lisinopril 10 mg|  DRUG|     316151|lisinopril 10 MG[lisinopril 10 MG]:::lisinopril 10 MG [Zestril][lisinopril 10...|316151:::563611:::314076:::567576:::197885:::206765:::104377:::316155:::31615...|0.2147:::0.3242:::0.3611:::0.3957:::0.4448:::0.4566:::0.4788:::0.4839:::0.495...|0.0231:::0.0525:::0.0652:::0.0783:::0.0989:::0.1042:::0.1146:::0.1171:::0.122...|Clinical Drug Comp:::Branded Drug Comp:::Clinical Drug:::Branded Drug Comp:::...|
+-----------------+------+-----------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medembed_base_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.5.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[BGE]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.1 GB|
|Case sensitive:|false|
