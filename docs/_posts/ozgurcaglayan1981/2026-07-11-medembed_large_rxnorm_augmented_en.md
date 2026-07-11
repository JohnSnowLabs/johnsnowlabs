---
layout: model
title: Sentence Entity Resolver for RxNorm (bge_medembed_large_v0_1 embeddings)
author: John Snow Labs
name: medembed_large_rxnorm_augmented
date: 2026-07-11
tags: [en, entity_resolution, licensed, clinical, rxnorm, medembed_large]
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

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `bge_medembed_large_v0_1` embeddings. Additionally, the model returns concept classes of drugs in the `all_k_aux_labels` column.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medembed_large_rxnorm_augmented_en_6.4.0_3.4_1783802752356.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medembed_large_rxnorm_augmented_en_6.4.0_3.4_1783802752356.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_medembed_large_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("medembed_large_rxnorm_augmented","en","clinical/models")\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_medembed_large_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("medembed_large_rxnorm_augmented","en","clinical/models")\
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

val embedder = BGEEmbeddings
    .pretrained("bge_medembed_large_v0_1", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("medembed_large_rxnorm_augmented", "en", "clinical/models")
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
| ner_chunk          | entity   |   rxnorm_code | resolution                              | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-------------------|:---------|--------------:|:----------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| metformin 500 mg   | DRUG     |        316256 | metformin 500 mg [metformin 500 mg]     | 316256:::861007:::860974:::438507:::861025:::332809:::330861:::334886:::316255::... | 0.0000:::0.3281:::0.3371:::0.3512:::0.3548:::0.3948:::0.4065:::0.4222:::0.4393::... | 0.0000:::0.0538:::0.0568:::0.0617:::0.0629:::0.0779:::0.0826:::0.0891:::0.0965::... | metformin 500 mg [metformin 500 mg]:::metformin 500 mg oral tablet [metformin hc... | Clinical Drug Comp:::Clinical Drug:::Clinical Drug Comp:::Clinical Drug Comp:::C... |
| Lipitor            | DRUG     |        153165 | lipitor [lipitor]                       | 153165:::1177401:::1177400:::617314:::617318:::617320:::262095:::617317:::617313... | 0.0000:::0.4917:::0.5204:::0.5313:::0.5411:::0.5756:::0.5757:::0.5786:::0.5803::... | 0.0000:::0.1209:::0.1354:::0.1412:::0.1464:::0.1656:::0.1657:::0.1674:::0.1684::... | lipitor [lipitor]:::lipitor pill [lipitor pill]:::lipitor oral product [lipitor ... | Brand Name:::Branded Dose Group:::Branded Dose Group:::Branded Drug:::Branded Dr... |
| Tylenol PRN        | DRUG     |        202433 | tylenol [tylenol]                       | 202433:::334048:::1187315:::220581:::161:::330892:::570061:::437174:::336435:::3... | 0.6106:::0.6507:::0.6516:::0.6523:::0.6549:::0.6557:::0.6623:::0.6650:::0.6662::... | 0.1864:::0.2117:::0.2123:::0.2127:::0.2144:::0.2150:::0.2193:::0.2211:::0.2219::... | tylenol [tylenol]:::acetaminophen 350 mg [acetaminophen 350 mg]:::tylenol pill [... | Brand Name:::Clinical Drug Comp:::Branded Dose Group:::Brand Name:::Ingredient::... |
| amoxicillin 500 mg | DRUG     |        317616 | amoxicillin 500 mg [amoxicillin 500 mg] | 317616:::575262:::565638:::565639:::791946:::308192:::331059:::565640:::802548::... | 0.0000:::0.2612:::0.2895:::0.2927:::0.2958:::0.2996:::0.3014:::0.3037:::0.3085::... | 0.0000:::0.0341:::0.0419:::0.0428:::0.0438:::0.0449:::0.0454:::0.0461:::0.0476::... | amoxicillin 500 mg [amoxicillin 500 mg]:::amoxicillin 500 mg [amoxicot] [amoxici... | Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Branded Drug Comp::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medembed_large_rxnorm_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.9 GB|
|Case sensitive:|false|