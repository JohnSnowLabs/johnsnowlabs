---
layout: model
title: Sentence Entity Resolver for NDC (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_ndc
date: 2026-07-26
tags: [en, entity_resolution, licensed, clinical, ndc, sbiobert]
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

This model maps clinical entities and concepts, particularly drugs and ingredients, to National Drug Codes. It leverages `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings and provides package options plus alternative drug suggestions through the `all_k_aux_label` column. Trained on the openFDA NDC Directory (release 2026-07-22).

{:.btn-box}
[Live Demo](https://demo.johnsnowlabs.com/healthcare/ER_NDC/){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/26.Chunk_Mapping.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ndc_en_6.4.0_3.4_1785025436584.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_ndc_en_6.4.0_3.4_1785025436584.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_ndc","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("ndc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, ndc_resolver
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

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx","en","clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

ndc_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_ndc","en","clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("ndc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, ndc_resolver
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

val sbert_embedder = BertSentenceEmbeddings
    .pretrained("sbiobert_base_cased_mli_onnx", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val ndc_resolver = SentenceEntityResolverModel
    .pretrained("sbiobertresolve_ndc", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("ndc_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    ner, ner_converter, c2doc, sbert_embedder, ndc_resolver
))

val data = Seq("She was started on losartan potassium 50 mg and hydrochlorothiazide 25 mg once daily for blood pressure control, continues sertraline 50 mg for depression, was switched to metoprolol succinate 25 mg for rate control, and takes gabapentin 300 mg at bedtime for neuropathic pain.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk                  | entity   | ndc_code   | resolution                   | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:---------------------------|:---------|:-----------|:-----------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| losartan potassium 50 mg   | DRUG     | 64380-0934 | losartan potassium 50 mg     | 64380-0934:::0904-7048:::59746-0334:::63187-0071:::70010-0742:::68180-0377:::059... | 0.0000:::3.4537:::4.1715:::4.3757:::5.5351:::6.5793:::7.1780:::7.4024:::7.5303::... | 0.0000:::0.0197:::0.0280:::0.0317:::0.0506:::0.0719:::0.0851:::0.0903:::0.0948::... | losartan potassium 50 mg:::losartan potassium 50 mg/1:::losartan potassium table... | {'packages': "['30 TABLET, FILM COATED in 1 BOTTLE (64380-934-04)', '90 TABLET, ... |
| hydrochlorothiazide 25 mg  | DRUG     | 68645-0510 | hydrochlorothiazide 25 mg/1  | 68645-0510:::46708-0211:::0591-0424:::0378-0614:::50111-0327:::0517-4201:::0378-... | 3.3059:::5.6094:::5.7282:::5.9631:::6.1827:::6.3636:::6.3982:::6.5080:::6.5657::... | 0.0198:::0.0578:::0.0607:::0.0643:::0.0681:::0.0708:::0.0757:::0.0786:::0.0794::... | hydrochlorothiazide 25 mg/1:::telmisartan and hydrochlorothiazide 25 mg/1:::tria... | {'packages': "['30 TABLET in 1 BOTTLE (68645-510-54)']", 'alternatives': ['0172-... |
| sertraline 50 mg           | DRUG     | 76282-0213 | sertraline 50 mg/1           | 76282-0213:::72189-0551:::0135-0550:::73352-0835:::21922-0107:::64896-0403:::090... | 4.2370:::4.6930:::5.9452:::6.0866:::6.1552:::6.2522:::6.3589:::6.4492:::6.5168::... | 0.0288:::0.0351:::0.0563:::0.0593:::0.0599:::0.0640:::0.0658:::0.0669:::0.0679::... | sertraline 50 mg/1:::sertraline hcl 50 mg/1:::sensodyne 50 mg/g:::tridacaine iii... | {'packages': "['100 TABLET, FILM COATED in 1 BOTTLE (76282-213-01)', '500 TABLET... |
| metoprolol succinate 25 mg | DRUG     | 55111-0466 | metoprolol succinate 25 mg/1 | 55111-0466:::61919-0754:::0378-0018:::46708-0290:::63629-8863:::54766-0726:::831... | 3.6995:::4.0826:::4.7247:::5.5334:::5.6337:::6.2463:::6.4721:::6.6422:::6.7591::... | 0.0252:::0.0307:::0.0404:::0.0559:::0.0572:::0.0707:::0.0744:::0.0767:::0.0808::... | metoprolol succinate 25 mg/1:::metoprolol succinate er 25 mg/1:::metoprolol tart... | {'packages': "['100 TABLET, FILM COATED, EXTENDED RELEASE in 1 BOTTLE (55111-466... |
| gabapentin 300 mg          | DRUG     | 65862-0199 | gabapentin 300 mg/1          | 65862-0199:::53451-0103:::16714-0662:::70771-1519:::70771-1861:::55111-0428:::54... | 3.4135:::4.9239:::5.4970:::6.7556:::6.9104:::7.1170:::7.2007:::7.2374:::7.2745::... | 0.0189:::0.0396:::0.0493:::0.0758:::0.0777:::0.0838:::0.0854:::0.0862:::0.0864::... | gabapentin 300 mg/1:::gabapentin enacarbil 300 mg/1:::gabapentin 300 mg/1 capsul... | {'packages': "['2000 CAPSULE in 1 BAG (65862-199-26)', '100 CAPSULE in 1 BOTTLE ... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_ndc|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[ndc_code]|
|Language:|en|
|Size:|766.5 MB|
|Case sensitive:|false|