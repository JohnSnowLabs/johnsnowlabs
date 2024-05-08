---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_rxnorm_augmented
date: 2024-04-18
tags: [rxnorm, en, clinical, licensed, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.3.1
spark_version: 3.2
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023_c` embeddings. It trained on the augmented version of the dataset used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

## Predicted Entities

`RxNorm Codes`, `Concept Classes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_en_5.3.1_3.2_1713400566709.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_en_5.3.1_3.2_1713400566709.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

rxnorm_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented", "en", "clinical/models")\
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

text= "The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. She was seen by the endocrinology service and was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"
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

val data = Seq("The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    | ner_chunk         | entity   |   rxnorm_code | resolution                                                      | all_k_results                                  | all_k_distances                              | all_k_cosine_distances                       | all_k_resolutions                                                                                          | all_k_aux_labels                                                                  |
|---:|:------------------|:---------|--------------:|:----------------------------------------------------------------|:--------------------------------------------...|:---------------------------------------------|:---------------------------------------------|:-----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
|  0 | aspirin           | DRUG     |          1191 | aspirin [aspirin]                                               | 1191:::1154070:::1537020:::1295740:::1299851...| 0.2747:::0.4428:::0.4512:::0.4900:::0.5305...| 0.0377:::0.0980:::0.1018:::0.1200:::0.1407...| aspirin [aspirin]:::aspirin pill [aspirin pill]:::aspirin effervescent oral tablet:::aspirin oral powder...| Ingredient:::Clinical Dose Group:::Clinical Drug Form:::Clinical Dose Group:::B...|
|  1 | Albuterol inhaler | DRUG     |        745678 | albuterol metered dose inhaler [albuterol metered dose inhaler] | 745678:::1649559:::745790:::307779:::745679:...| 0.4336:::0.4758:::0.5416:::0.5701:::0.5863...| 0.0940:::0.1132:::0.1466:::0.1625:::0.1719...| albuterol metered dose inhaler [albuterol metered dose inhaler]:::albuterol dry powder inhaler [albutero...| Clinical Drug Form:::Clinical Drug Form:::Clinical Drug Form:::Clinical Drug:::...|
|  2 | Coumadin 5 mg     | DRUG     |        855333 | warfarin sodium 5 mg [coumadin]                                 | 855333:::432467:::438740:::451604:::855345::...| 0.3421:::0.4407:::0.4601:::0.4798:::0.5002...| 0.0585:::0.0971:::0.1058:::0.1151:::0.1251...| warfarin sodium 5 mg [coumadin]:::coumarin 5 mg oral tablet:::coumarin 5 mg [coumarin 5 mg]:::coumarin 0...| Branded Drug Comp:::Clinical Drug:::Clinical Drug Comp:::Clinical Drug Comp:::B...|
|  3 | metformin 1000 mg | DRUG     |        316255 | metformin 1000 mg [metformin 1000 mg]                           | 316255:::860995:::860999:::861004:::316256::...| 0.3468:::0.4492:::0.4492:::0.5133:::0.5497...| 0.0601:::0.1009:::0.1009:::0.1317:::0.1511...| metformin 1000 mg [metformin 1000 mg]:::metformin hydrochloride 1000 mg [metformin hydrochloride 1000 mg...| Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Clinical Drug:::Clini...|
|  4 | Lisinopril 10 mg  | DRUG     |        314076 | lisinopril 10 mg oral tablet                                    | 314076:::316151:::197885:::567576:::316153::...| 0.4704:::0.4845:::0.6129:::0.6281:::0.6384...| 0.1106:::0.1174:::0.1878:::0.1973:::0.2038...| lisinopril 10 mg oral tablet:::lisinopril 10 mg [lisinopril 10 mg]:::hydrochlorothiazide 12.5 mg / lisin...| Clinical Drug:::Clinical Drug Comp:::Clinical Drug:::Branded Drug Comp:::Clinic...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.3.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|

## References

In this model, RxNorm version 5.0 was used for the training.
