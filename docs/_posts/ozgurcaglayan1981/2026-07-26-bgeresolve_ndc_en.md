---
layout: model
title: Sentence Entity Resolver for NDC (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_ndc
date: 2026-07-26
tags: [en, entity_resolution, licensed, clinical, ndc, bge]
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

This model maps clinical entities and concepts, particularly drugs and ingredients, to National Drug Codes. It leverages `bge_base_en_v1_5_onnx` Sentence Embeddings and provides package options plus alternative drug suggestions through the `all_k_aux_label` column. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_ndc_en_6.4.0_3.4_1785070165721.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_ndc_en_6.4.0_3.4_1785070165721.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = SentenceEntityResolverModel.pretrained("bgeresolve_ndc","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_ndc","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

val embedder = BGEEmbeddings
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val ndc_resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_ndc", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| ner_chunk                  | entity   | ndc_code   | resolution                   | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:---------------------------|:---------|:-----------|:-----------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| losartan potassium 50 mg   | DRUG     | 64380-0934 | losartan potassium 50 mg     | 64380-0934:::0904-7048:::59746-0334:::68180-0377:::70010-0742:::63187-0071:::643... | 0.0000:::0.1727:::0.2886:::0.3155:::0.3753:::0.3831:::0.4059:::0.4149:::0.4194::... | 0.0000:::0.0149:::0.0417:::0.0498:::0.0704:::0.0734:::0.0824:::0.0861:::0.0879::... | losartan potassium 50 mg:::losartan potassium 50 mg/1:::losartan potassium table... | {'packages': "['30 TABLET, FILM COATED in 1 BOTTLE (64380-934-04)', '90 TABLET, ... |
| hydrochlorothiazide 25 mg  | DRUG     | 68645-0510 | hydrochlorothiazide 25 mg/1  | 68645-0510:::65649-0311:::0172-2089:::0591-0347:::70954-0522:::63323-0658:::6586... | 0.2113:::0.3800:::0.4210:::0.4341:::0.4525:::0.4719:::0.4898:::0.4910:::0.4955::... | 0.0223:::0.0722:::0.0886:::0.0942:::0.1024:::0.1113:::0.1200:::0.1206:::0.1227::... | hydrochlorothiazide 25 mg/1:::chlorothiazide 250 mg/5ml:::hydrochlorothiazide 50... | {'packages': "['30 TABLET in 1 BOTTLE (68645-510-54)']", 'alternatives': ['0172-... |
| sertraline 50 mg           | DRUG     | 76282-0213 | sertraline 50 mg/1           | 76282-0213:::72189-0551:::0904-6925:::68645-0522:::58151-0575:::69238-2789:::762... | 0.2415:::0.3459:::0.3668:::0.4548:::0.4556:::0.4709:::0.4807:::0.4921:::0.5014::... | 0.0292:::0.0598:::0.0673:::0.1034:::0.1038:::0.1109:::0.1155:::0.1211:::0.1257::... | sertraline 50 mg/1:::sertraline hcl 50 mg/1:::sertraline hydrochloride 50 mg/1::... | {'packages': "['100 TABLET, FILM COATED in 1 BOTTLE (76282-213-01)', '500 TABLET... |
| metoprolol succinate 25 mg | DRUG     | 55111-0466 | metoprolol succinate 25 mg/1 | 55111-0466:::61919-0754:::55111-0469:::55154-6886:::0904-6324:::63629-8863:::633... | 0.1410:::0.3366:::0.3419:::0.3584:::0.3587:::0.3777:::0.3791:::0.3809:::0.3831::... | 0.0099:::0.0566:::0.0584:::0.0642:::0.0643:::0.0713:::0.0718:::0.0725:::0.0734::... | metoprolol succinate 25 mg/1:::metoprolol succinate er 25 mg/1:::metoprolol succ... | {'packages': "['100 TABLET, FILM COATED, EXTENDED RELEASE in 1 BOTTLE (55111-466... |
| gabapentin 300 mg          | DRUG     | 65862-0199 | gabapentin 300 mg/1          | 65862-0199:::70771-1861:::16714-0662:::53451-0103:::80425-0082:::81033-0124:::00... | 0.2162:::0.3360:::0.3471:::0.4207:::0.4656:::0.4932:::0.4976:::0.5001:::0.5056::... | 0.0234:::0.0564:::0.0603:::0.0885:::0.1084:::0.1216:::0.1238:::0.1251:::0.1278::... | gabapentin 300 mg/1:::gabapentin 300 mg/1 tablet:::gabapentin 300 mg/1 capsule::... | {'packages': "['2000 CAPSULE in 1 BAG (65862-199-26)', '100 CAPSULE in 1 BOTTLE ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_ndc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[ndc_code]|
|Language:|en|
|Size:|767.5 MB|
|Case sensitive:|false|