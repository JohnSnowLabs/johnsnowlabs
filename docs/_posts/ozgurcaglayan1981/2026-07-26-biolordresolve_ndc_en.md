---
layout: model
title: Sentence Entity Resolver for NDC (mpnet_embeddings_biolord_2023_c embeddings)
author: John Snow Labs
name: biolordresolve_ndc
date: 2026-07-26
tags: [en, entity_resolution, licensed, clinical, ndc, biolord]
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

This model maps clinical entities and concepts, particularly drugs and ingredients, to National Drug Codes. It leverages `mpnet_embeddings_biolord_2023_c` Sentence Embeddings and provides package options plus alternative drug suggestions through the `all_k_aux_label` column. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/biolordresolve_ndc_en_6.4.0_3.4_1785069570547.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/biolordresolve_ndc_en_6.4.0_3.4_1785069570547.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

documentAssembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner = MedicalNerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = SentenceEntityResolverModel.pretrained("biolordresolve_ndc","en","clinical/models")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("ndc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, embedder, ndc_resolver
])

data = spark.createDataFrame([["She was started on losartan potassium 50 mg and hydrochlorothiazide 25 mg once daily for blood pressure control, continues sertraline 50 mg for depression, was switched to metoprolol succinate 25 mg for rate control, and takes gabapentin 300 mg at bedtime for neuropathic pain."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

documentAssembler = nlp.DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare","en","clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer()\
    .setInputCols(["sentence"])\
    .setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical","en","clinical/models")\
    .setInputCols(["sentence","token"])\
    .setOutputCol("word_embeddings")

ner = medical.NerModel.pretrained("ner_posology_greedy","en","clinical/models")\
    .setInputCols(["sentence","token","word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence","token","ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = nlp.Chunk2Doc()\
    .setInputCols("ner_chunk")\
    .setOutputCol("ner_chunk_doc")

embedder = nlp.MPNetEmbeddings.pretrained("mpnet_embeddings_biolord_2023_c","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("mpnet_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = medical.SentenceEntityResolverModel.pretrained("biolordresolve_ndc","en","clinical/models")\
    .setInputCols(["mpnet_embeddings"])\
    .setOutputCol("ndc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, embedder, ndc_resolver
])

data = spark.createDataFrame([["She was started on losartan potassium 50 mg and hydrochlorothiazide 25 mg once daily for blood pressure control, continues sertraline 50 mg for depression, was switched to metoprolol succinate 25 mg for rate control, and takes gabapentin 300 mg at bedtime for neuropathic pain."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel
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

val ner = MedicalNerModel
    .pretrained("ner_posology_greedy", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val c2doc = new Chunk2Doc()
    .setInputCols("ner_chunk")
    .setOutputCol("ner_chunk_doc")

val embedder = MPNetEmbeddings
    .pretrained("mpnet_embeddings_biolord_2023_c", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("mpnet_embeddings")
    .setCaseSensitive(false)

val ndc_resolver = SentenceEntityResolverModel
    .pretrained("biolordresolve_ndc", "en", "clinical/models")
    .setInputCols(Array("mpnet_embeddings"))
    .setOutputCol("ndc_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, embedder, ndc_resolver
))

val data = Seq("She was started on losartan potassium 50 mg and hydrochlorothiazide 25 mg once daily for blood pressure control, continues sertraline 50 mg for depression, was switched to metoprolol succinate 25 mg for rate control, and takes gabapentin 300 mg at bedtime for neuropathic pain.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                  | entity   | ndc_code   | resolution                              | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:---------------------------|:---------|:-----------|:----------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| losartan potassium 50 mg   | DRUG     | 70010-0742 | losartan 50 mg/1 tablet                 | 70010-0742:::64380-0934:::68180-0377:::0904-7048:::59746-0334:::68180-0376:::090... | 0.3996:::0.4204:::0.4247:::0.4661:::0.4862:::0.5264:::0.5362:::0.5575:::0.5787::... | 0.0799:::0.0883:::0.0902:::0.1086:::0.1182:::0.1385:::0.1438:::0.1554:::0.1674::... | losartan 50 mg/1 tablet:::losartan potassium 50 mg:::losartan potassium 50 mg/1 ... | {'packages': "['30 TABLET in 1 BOTTLE (70010-742-03)', '90 TABLET in 1 BOTTLE (7... |
| hydrochlorothiazide 25 mg  | DRUG     | 68645-0510 | hydrochlorothiazide 25 mg/1 tablet      | 68645-0510:::65862-0631:::62135-0669:::69097-0831:::0591-0862:::0378-6325:::0591... | 0.5349:::0.6266:::0.6398:::0.6462:::0.6675:::0.6682:::0.6699:::0.6822:::0.6859::... | 0.1430:::0.1963:::0.2047:::0.2088:::0.2228:::0.2233:::0.2244:::0.2327:::0.2352::... | hydrochlorothiazide 25 mg/1 tablet:::irbesartan and hydrochlorothiazide 25 mg/1:... | {'packages': "['30 TABLET in 1 BOTTLE (68645-510-54)']", 'alternatives': ['0172-... |
| sertraline 50 mg           | DRUG     | 72189-0551 | sertraline hcl 50 mg/1                  | 72189-0551:::68645-0522:::76282-0213:::0904-6925:::76282-0212:::0904-6924:::6864... | 0.3778:::0.4472:::0.4638:::0.4835:::0.5591:::0.5764:::0.6186:::0.6410:::0.6586::... | 0.0714:::0.1000:::0.1075:::0.1169:::0.1563:::0.1661:::0.1913:::0.2055:::0.2169::... | sertraline hcl 50 mg/1:::sertraline hydrochloride 50 mg/1 tablet:::sertraline 50... | {'packages': "['30 TABLET, FILM COATED in 1 BOTTLE (72189-551-30)', '90 TABLET, ... |
| metoprolol succinate 25 mg | DRUG     | 63629-8863 | metoprolol succinate er tablets 25 mg/1 | 63629-8863:::0378-0018:::61919-0754:::46708-0290:::55154-6886:::71335-0158:::467... | 0.4207:::0.4494:::0.4840:::0.5089:::0.6069:::0.6287:::0.6621:::0.6785:::0.6847::... | 0.0885:::0.1010:::0.1171:::0.1295:::0.1842:::0.1976:::0.2192:::0.2302:::0.2344::... | metoprolol succinate er tablets 25 mg/1:::metoprolol tartrate 25 mg/1:::metoprol... | {'packages': "['100 TABLET, FILM COATED, EXTENDED RELEASE in 1 BOTTLE (63629-886... |
| gabapentin 300 mg          | DRUG     | 16714-0662 | gabapentin 300 mg/1 capsule             | 16714-0662:::65862-0199:::70771-1861:::53451-0103:::81279-0126:::68462-0126:::74... | 0.4204:::0.4424:::0.4664:::0.5558:::0.6058:::0.6689:::0.6735:::0.6870:::0.7024::... | 0.0884:::0.0978:::0.1088:::0.1544:::0.1835:::0.2237:::0.2268:::0.2360:::0.2467::... | gabapentin 300 mg/1 capsule:::gabapentin 300 mg/1:::gabapentin 300 mg/1 tablet::... | {'packages': "['100 CAPSULE in 1 BOTTLE (16714-662-01)', '500 CAPSULE in 1 BOTTL... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|biolordresolve_ndc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[mpnet_embeddings]|
|Output Labels:|[ndc_code]|
|Language:|en|
|Size:|768.3 MB|
|Case sensitive:|false|
