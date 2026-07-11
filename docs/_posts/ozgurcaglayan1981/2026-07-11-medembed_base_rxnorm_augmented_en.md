---
layout: model
title: Sentence Entity Resolver for RxNorm (bge_medembed_base_v0_1 embeddings)
author: John Snow Labs
name: medembed_base_rxnorm_augmented
date: 2026-07-11
tags: [en, entity_resolution, licensed, clinical, rxnorm, medembed_base]
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

This model maps clinical entities and concepts (like drugs/ingredients) to RxNorm codes using `bge_medembed_base_v0_1` embeddings. It additionally returns drug concept classes in the `all_k_aux_labels` column.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/medembed_base_rxnorm_augmented_en_6.4.0_3.4_1783802162441.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/medembed_base_rxnorm_augmented_en_6.4.0_3.4_1783802162441.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_medembed_base_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("medembed_base_rxnorm_augmented","en","clinical/models")\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_medembed_base_v0_1","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("medembed_base_rxnorm_augmented","en","clinical/models")\
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
    .pretrained("bge_medembed_base_v0_1", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("medembed_base_rxnorm_augmented", "en", "clinical/models")
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
| metformin 500 mg   | DRUG     |        316256 | metformin 500 mg [metformin 500 mg]     | 316256:::860974:::332809:::316255:::861007:::330861:::875864:::438507:::861025::... | 0.0000:::0.3293:::0.3636:::0.3910:::0.4074:::0.4124:::0.4161:::0.4420:::0.4529::... | 0.0000:::0.0542:::0.0661:::0.0764:::0.0830:::0.0851:::0.0866:::0.0977:::0.1025::... | metformin 500 mg [metformin 500 mg]:::metformin hydrochloride 500 mg [metformin ... | Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Com... |
| Lipitor            | DRUG     |        153165 | lipitor [lipitor]                       | 153165:::1177401:::1177400:::617317:::574676:::617313:::617319:::617314:::617318... | 0.0000:::0.4566:::0.5634:::0.6239:::0.6264:::0.6288:::0.6332:::0.6373:::0.6438::... | 0.0000:::0.1042:::0.1587:::0.1946:::0.1962:::0.1977:::0.2005:::0.2031:::0.2073::... | lipitor [lipitor]:::lipitor pill [lipitor pill]:::lipitor oral product [lipitor ... | Brand Name:::Branded Dose Group:::Branded Dose Group:::Branded Drug Comp:::Brand... |
| Tylenol PRN        | DRUG     |        202433 | tylenol [tylenol]                       | 202433:::1187315:::220581:::1187311:::1187314:::1092374:::1092375:::209387:::569... | 0.5055:::0.5785:::0.5931:::0.6328:::0.6357:::0.6385:::0.6388:::0.6463:::0.6506::... | 0.1277:::0.1673:::0.1759:::0.2002:::0.2021:::0.2038:::0.2041:::0.2088:::0.2116::... | tylenol [tylenol]:::tylenol pill [tylenol pill]:::tylenol pm [tylenol pm]:::tyle... | Brand Name:::Branded Dose Group:::Brand Name:::Branded Dose Group:::Branded Dose... |
| amoxicillin 500 mg | DRUG     |        317616 | amoxicillin 500 mg [amoxicillin 500 mg] | 317616:::565639:::575262:::565638:::565314:::565641:::329103:::563098:::360876::... | 0.0000:::0.2213:::0.2243:::0.2329:::0.2830:::0.2879:::0.2943:::0.3016:::0.3118::... | 0.0000:::0.0245:::0.0252:::0.0271:::0.0401:::0.0414:::0.0433:::0.0455:::0.0486::... | amoxicillin 500 mg [amoxicillin 500 mg]:::amoxicillin 500 mg [amoxil] [amoxicill... | Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Branded Drug Comp::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|medembed_base_rxnorm_augmented|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|