---
layout: model
title: Sentence Entity Resolver for RxNorm (sbiobert_base_cased_mli embeddings)
author: John Snow Labs
name: sbiobertresolve_rxnorm_augmented
date: 2024-01-17
tags: [rxnorm, licensed, en, clinical, entity_resolution]
task: Entity Resolution
language: en
edition: Healthcare NLP 5.2.1
spark_version: 3.0
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `sbiobert_base_cased_mli` Sentence Bert Embeddings. It trained on the augmented version of the dataset which is used in previous RxNorm resolver models. Additionally, this model returns concept classes of the drugs in `all_k_aux_labels` column.

## Predicted Entities

`RxNorm Codes`, `Concept Classes`

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_augmented_en_5.2.1_3.0_1705502473156.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_rxnorm_augmented_en_5.2.1_3.0_1705502473156.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

rxnorm_resolver = SentenceEntityResolverModel..pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")\ \
    .setInputCols(["sentence_embeddings"]) \
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages = [document_assembler,
                                       sentenceDetectorDL,
                                       tokenizer,
                                       word_embeddings,
                                       ner,
                                       ner_converter,
                                       c2doc,
                                       sbert_embedder,
                                       rxnorm_resolver])

text= "The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on avandia 4 mg at night , Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily"
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

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli","en","clinical/models")
    .setInputCols("ner_chunk_doc")
    .setOutputCol("sbert_embeddings")

val rxnorm_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_rxnorm_augmented", "en", "clinical/models")
    .setInputCols("sbert_embeddings")
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(document_assembler,
                               sentence_detector,
                               tokenizer,
                               word_embeddings,
                               ner,
                               ner_converter,
                               chunk2doc,
                               sbert_embedder,
                               rxnorm_resolver))

val data = Seq("The patient was prescribed aspirin and and Albuterol inhaler, two puffs every 4 hours as needed for asthma. He was seen by the endocrinology service and she was discharged on Coumadin 5 mg with meals , and metformin 1000 mg two times a day and Lisinopril 10 mg daily").toDS().toDF("text")

val result = pipeline.fit(data).transform(data)
```
</div>

## Results

```bash
|    | ner_chunk         | entity   | RxNormCode | resolution                                                      | all_k_results                                    | all_k_distances                               | all_k_cosine_distances                        | all_k_resolutions                                                                                | all_k_aux_labels                                                                |
|---:|-------------------|:---------|------------|-----------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|  0 | aspirin           | DRUG     | 1537020    | aspirin Effervescent Oral Tablet                                | 1537020:::1191:::1295740:::405403:::218266...    | 0.0000:::0.0000:::4.1826:::5.7007:::6.0877... | 0.0000:::0.0000:::0.0292:::0.0550:::0.0624... |aspirin Effervescent Oral Tablet:::aspirin [aspirin]:::aspirin Oral Powder Product...             | Clinical Drug Form:::Ingredient:::Clinical Dose Group:::Brand Name:::Brand Na...|
|  1 | Albuterol inhaler | DRUG     | 745678     | albuterol metered dose inhaler [albuterol metered dose inhaler] | 745678:::2108226:::1154602:::2108233:::2108228...| 4.9847:::5.1028:::5.4746:::5.7809:::6.28597...| 0.0414:::0.0439:::0.0505:::0.0562:::0.0676 ...|albuterol metered dose inhaler [albuterol metered dose inhaler]:::albuterol inhalation solution...| Clinical Drug Form:::Clinical Drug Form:::Clinical Dose Group:::Clinical Drug...|
|  2 | Coumadin 5 mg     | DRUG     | 855333     | warfarin sodium 5 MG [Coumadin]                                 | 855333:::432467:::438740:::153692:::352120...    | 0.0000:::4.0885:::4.0885:::5.3065:::5.51327...| 0.0000:::0.0287:::0.0287:::0.0479:::0.0518... |warfarin sodium 5 MG [Coumadin]:::coumarin 5 MG Oral Tablet:::coumarin 5 mg [coumarin 5 mg]:::o...| Branded Drug Comp:::Clinical Drug:::Clinical Drug Comp:::Branded Drug:::Brand...|
|  3 | metformin 1000 mg | DRUG     | 316255     | metformin 1000 mg [metformin 1000 mg]                           | 316255:::860995:::860999:::860997:::861014.      | 0.0000:::5.2988:::5.2988:::5.9071:::6.3066... | 0.0000:::0.0445:::0.0445:::0.0553:::0.0632... |metformin 1000 mg [metformin 1000 mg]:::metformin hydrochloride 1000 mg [metformin hydrochlore... | Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Branded Drug Comp::...|
|  4 | Lisinopril 10 mg  | DRUG     | 314076     | lisinopril 10 MG Oral Tablet                                    | 314076:::316151:::567576:::565846:::389184...    | 0.0000:::0.0000:::3.6543:::4.2782:::4.2805... | 0.0000:::0.0000:::0.0234:::0.0325:::0.0315... |lisinopril 10 MG Oral Tablet:::lisinopril 10 mg [lisinopril 10 mg]:::lisinopril 10 mg [prinivil...| Clinical Drug:::Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::...|
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_rxnorm_augmented|
|Compatibility:|Healthcare NLP 5.2.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.3 GB|
|Case sensitive:|false|

## References

In this model, RxNorm  version 5.0 was used for the training.
