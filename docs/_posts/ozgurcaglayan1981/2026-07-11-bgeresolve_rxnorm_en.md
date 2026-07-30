---
layout: model
title: Sentence Entity Resolver for RxNorm Codes (bge_base_en_v1_5_onnx embeddings)
author: John Snow Labs
name: bgeresolve_rxnorm
date: 2026-07-11
tags: [en, entity_resolution, licensed, clinical, rxnorm, bge]
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

This model maps drug entities and concepts to RxNorm codes using `bge_base_en_v1_5_onnx` embeddings. It also returns drug concept classes in the `all_k_aux_labels` column.

{:.btn-box}
[Live Demo](https://nlp.johnsnowlabs.com/resolve_entities_codes){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_en_6.4.0_3.4_1783801505970.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/bgeresolve_rxnorm_en_6.4.0_3.4_1783801505970.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

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

embedder = BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = SentenceEntityResolverModel.pretrained("bgeresolve_rxnorm","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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

embedder = nlp.BGEEmbeddings.pretrained("bge_base_en_v1_5_onnx","en")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("bge_embeddings")\
    .setCaseSensitive(False)

resolver = medical.SentenceEntityResolverModel.pretrained("bgeresolve_rxnorm","en","clinical/models")\
    .setInputCols(["bge_embeddings"])\
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
    .pretrained("bge_base_en_v1_5_onnx", "en")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("bge_embeddings")
    .setCaseSensitive(false)

val resolver = SentenceEntityResolverModel
    .pretrained("bgeresolve_rxnorm", "en", "clinical/models")
    .setInputCols(Array("bge_embeddings"))
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
| metformin 500 mg   | DRUG     |        316256 | metformin 500 mg [metformin 500 mg]     | 316256:::860974:::332809:::861007:::875864:::316255:::861001:::330861:::860976::... | 0.0000:::0.3536:::0.4056:::0.4113:::0.4221:::0.4441:::0.4536:::0.4557:::0.4646::... | 0.0000:::0.0625:::0.0823:::0.0846:::0.0891:::0.0986:::0.1029:::0.1038:::0.1079::... | metformin 500 mg [metformin 500 mg]:::metformin hydrochloride 500 mg [metformin ... | Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug Comp:::Clinical Drug:::B... |
| Lipitor            | DRUG     |        153165 | lipitor [lipitor]                       | 153165:::1177401:::1177400:::367665:::574676:::617313:::617317:::617319:::617314... | 0.0000:::0.5064:::0.5838:::0.6637:::0.6714:::0.6731:::0.6806:::0.6872:::0.6895::... | 0.0000:::0.1282:::0.1704:::0.2203:::0.2254:::0.2266:::0.2316:::0.2361:::0.2377::... | lipitor [lipitor]:::lipitor pill [lipitor pill]:::lipitor oral product [lipitor ... | Brand Name:::Branded Dose Group:::Branded Dose Group:::Branded Drug Form:::Brand... |
| Tylenol PRN        | DRUG     |        202433 | tylenol [tylenol]                       | 202433:::1187315:::220581:::1187314:::1187311:::1187313:::209387:::161:::570070:... | 0.5701:::0.6307:::0.6359:::0.6718:::0.6738:::0.6872:::0.7010:::0.7033:::0.7055::... | 0.1625:::0.1989:::0.2022:::0.2256:::0.2270:::0.2361:::0.2457:::0.2473:::0.2489::... | tylenol [tylenol]:::tylenol pill [tylenol pill]:::tylenol pm [tylenol pm]:::tyle... | Brand Name:::Branded Dose Group:::Brand Name:::Branded Dose Group:::Branded Dose... |
| amoxicillin 500 mg | DRUG     |        317616 | amoxicillin 500 mg [amoxicillin 500 mg] | 317616:::565639:::575262:::565638:::565641:::565314:::565640:::563098:::566614::... | 0.0000:::0.1997:::0.2010:::0.2225:::0.2792:::0.2819:::0.2988:::0.3043:::0.3081::... | 0.0000:::0.0199:::0.0202:::0.0248:::0.0390:::0.0397:::0.0446:::0.0463:::0.0475::... | amoxicillin 500 mg [amoxicillin 500 mg]:::amoxicillin 500 mg [amoxil] [amoxicill... | Clinical Drug Comp:::Branded Drug Comp:::Branded Drug Comp:::Branded Drug Comp::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bgeresolve_rxnorm|
|Compatibility:|Healthcare NLP 6.4.0+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[bge_embeddings]|
|Output Labels:|[rxnorm_code]|
|Language:|en|
|Size:|1.4 GB|
|Case sensitive:|false|