---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023 embeddings)
author: John Snow Labs
name: biolordresolve_avg_rxnorm_augmented_v2
date: 2026-07-11
tags: [en, entity_resolution, licensed, clinical, rxnorm, biolord_avg]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.0
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023` embeddings. It returns concept classes of drugs in the `all_k_aux_labels` column.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_v2_en_6.4.0_3.4_1783800936003.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_avg_rxnorm_augmented_v2_en_6.4.0_3.4_1783800936003.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented_v2","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and continued on Lipitor for hyperlipidemia. She takes Tylenol PRN for headaches and was prescribed amoxicillin 500 mg for a sinus infection."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner_model = medical.NerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

chunk2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_avg_rxnorm_augmented_v2","en","clinical/models")\
    .setInputCols(["embeddings"])\
    .setOutputCol("rxnorm_code")\
    .setDistanceFunction("EUCLIDEAN")

pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and continued on Lipitor for hyperlipidemia. She takes Tylenol PRN for headaches and was prescribed amoxicillin 500 mg for a sinus infection."]]).toDF("text")
result = pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetector = SentenceDetectorDLModel
    .pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer()
    .setInputCols("sentence")
    .setOutputCol("token")

val word_embeddings = WordEmbeddingsModel
    .pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val ner_model = MedicalNerModel
    .pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val chunk2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_avg_rxnorm_augmented_v2", "en", "clinical/models")
    .setInputCols(Array("embeddings"))
    .setOutputCol("rxnorm_code")
    .setDistanceFunction("EUCLIDEAN")

val pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetector, tokenizer, word_embeddings,
    ner_model, ner_converter, chunk2doc, embedder, resolver
))

val data = Seq("The patient was started on metformin 500 mg twice daily for type 2 diabetes and continued on Lipitor for hyperlipidemia. She takes Tylenol PRN for headaches and was prescribed amoxicillin 500 mg for a sinus infection.").toDF("text")
val res = pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk          | entity   |   rxnorm_code | resolution                                                                      | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-------------------|:---------|--------------:|:--------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| metformin 500 mg   | DRUG     |        860974 | metformin hydrochloride 500 mg [metformin hydrochloride 500 mg]                 | 860974:::860975:::861007:::861008:::105376:::1807915:::861017:::2703582:::860978... | 0.2955:::0.3880:::0.3950:::0.4350:::0.4399:::0.5010:::0.5017:::0.5114:::0.5117::... | 0.0437:::0.0753:::0.0780:::0.0946:::0.0968:::0.1255:::0.1259:::0.1308:::0.1309::... | metformin hydrochloride 500 mg [metformin hydrochloride 500 mg]:::metformin hydr... | Clinical Drug Comp:::Quant Clinical Drug:::Clinical Drug:::Branded Drug:::Brande... |
| Lipitor            | DRUG     |       1177400 | lipitor oral product [lipitor oral product]                                     | 1177400:::1177401:::1422091:::1177399:::153165:::1422090:::1177928:::1177398:::6... | 0.4478:::0.5435:::0.6191:::0.6378:::0.6415:::0.6463:::0.6569:::0.6575:::0.6632::... | 0.1002:::0.1477:::0.1916:::0.2034:::0.2058:::0.2088:::0.2157:::0.2161:::0.2199::... | lipitor oral product [lipitor oral product]:::lipitor pill [lipitor pill]:::lipt... | Branded Dose Group:::Branded Dose Group:::Branded Dose Group:::Branded Dose Grou... |
| Tylenol PRN        | DRUG     |        209459 | tylenol extra strength 500mg tablet [tylenol extra strength 500 mg oral tablet] | 209459:::1187321:::2634560:::220577:::1094538:::1243440:::209387:::2374361:::173... | 0.6750:::0.7113:::0.7166:::0.7219:::0.7222:::0.7287:::0.7338:::0.7377:::0.7399::... | 0.2278:::0.2530:::0.2568:::0.2605:::0.2608:::0.2655:::0.2692:::0.2721:::0.2737::... | tylenol extra strength 500mg tablet [tylenol extra strength 500 mg oral tablet]:... | Branded Drug:::Branded Dose Group:::Clinical Pack:::Brand Name:::Clinical Drug::... |
| amoxicillin 500 mg | DRUG     |        565048 | amoxicillin 500 mg [zoxycil] [amoxicillin 500 mg [zoxycil]]                     | 565048:::308191:::575263:::200998:::200999:::565643:::566614:::540472:::565644::... | 0.3630:::0.3688:::0.3842:::0.3895:::0.3943:::0.3994:::0.4099:::0.4150:::0.4362::... | 0.0659:::0.0680:::0.0738:::0.0758:::0.0777:::0.0798:::0.0840:::0.0861:::0.0952::... | amoxicillin 500 mg [zoxycil] [amoxicillin 500 mg [zoxycil]]:::amoxicillin 500 mg... | Branded Drug Comp:::Clinical Drug:::Branded Drug Comp:::Branded Drug:::Branded D... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_avg_rxnorm_augmented_v2|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|