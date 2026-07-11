---
layout: model
title: Sentence Entity Resolver for RxNorm (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_rxnorm_augmented_v2
date: 2026-07-11
tags: [en, entity_resolution, licensed, clinical, rxnorm, biolord]
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

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `mpnet_embeddings_biolord_2023_c` embeddings. Additionally, this model returns concept classes of the drugs in the `all_k_aux_labels` column.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_v2_en_6.4.0_3.4_1783800071176.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_rxnorm_augmented_v2_en_6.4.0_3.4_1783800071176.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented_v2","en","clinical/models")\
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

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_rxnorm_augmented_v2","en","clinical/models")\
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
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_rxnorm_augmented_v2", "en", "clinical/models")
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
| ner_chunk          | entity   |   rxnorm_code | resolution                                                      | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-------------------|:---------|--------------:|:----------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| metformin 500 mg   | DRUG     |        860974 | metformin hydrochloride 500 mg [metformin hydrochloride 500 mg] | 860974:::316256:::861007:::860978:::861001:::860995:::861009:::876009:::861017::... | 0.3055:::0.5156:::0.5611:::0.5796:::0.5928:::0.5930:::0.6026:::0.6063:::0.6076::... | 0.0467:::0.1329:::0.1574:::0.1680:::0.1757:::0.1758:::0.1816:::0.1838:::0.1846::... | metformin hydrochloride 500 mg [metformin hydrochloride 500 mg]:::metformin 500 ... | Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::Clinical Drug:::Brande... |
| Lipitor            | DRUG     |       1177401 | lipitor pill [lipitor pill]                                     | 1177401:::153165:::1177400:::1422091:::617320:::1177403:::1177399:::262095:::617... | 0.4722:::0.5060:::0.5297:::0.6885:::0.7587:::0.7656:::0.7809:::0.7834:::0.7837::... | 0.1115:::0.1280:::0.1403:::0.2370:::0.2878:::0.2931:::0.3049:::0.3069:::0.3071::... | lipitor pill [lipitor pill]:::lipitor [lipitor]:::lipitor oral product [lipitor ... | Branded Dose Group:::Brand Name:::Branded Dose Group:::Branded Dose Group:::Bran... |
| Tylenol PRN        | DRUG     |       1187313 | tylenol pm oral product [tylenol pm oral product]               | 1187313:::1187505:::1187503:::220586:::1187317:::209387:::2634560:::220581:::263... | 0.7145:::0.7300:::0.7331:::0.7363:::0.7419:::0.7500:::0.7551:::0.7552:::0.7583::... | 0.2552:::0.2664:::0.2687:::0.2711:::0.2752:::0.2813:::0.2851:::0.2851:::0.2875::... | tylenol pm oral product [tylenol pm oral product]:::tylenol with codeine oral pr... | Branded Dose Group:::Branded Dose Group:::Branded Dose Group:::Brand Name:::Bran... |
| amoxicillin 500 mg | DRUG     |        317616 | amoxicillin 500 mg [amoxicillin 500 mg]                         | 317616:::308191:::565641:::565639:::565638:::565640:::308192:::575262:::566613::... | 0.4134:::0.4812:::0.4942:::0.4989:::0.5015:::0.5111:::0.5143:::0.5190:::0.5504::... | 0.0855:::0.1158:::0.1221:::0.1245:::0.1258:::0.1306:::0.1323:::0.1347:::0.1514::... | amoxicillin 500 mg [amoxicillin 500 mg]:::amoxicillin 500 mg oral capsule [amoxi... | Clinical Drug Comp:::Clinical Drug:::Branded Drug Comp:::Branded Drug Comp:::Bra... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_rxnorm_augmented_v2|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|