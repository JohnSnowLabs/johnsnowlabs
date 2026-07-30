---
layout: model
title: Sentence Entity Resolver for ATC (sbiobert_base_cased_mli_onnx embeddings)
author: John Snow Labs
name: sbiobertresolve_atc
date: 2026-07-30
tags: [en, entity_resolution, licensed, clinical, atc, sbiobert]
task: Entity Resolution
language: en
edition: Healthcare NLP 6.4.1
spark_version: 3.4
supported: true
annotator: SentenceEntityResolverModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

This model maps drugs entities to ATC (Anatomic Therapeutic Chemical) codes using `sbiobert_base_cased_mli_onnx` Sentence Bert Embeddings. Trained on the WHO ATC-DDD dataset (release 2026-04-25).

{:.btn-box}
[Live Demo](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange}
[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/3.Clinical_Entity_Resolvers.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_atc_en_6.4.1_3.4_1785443296843.zip){:.button.button-orange.button-orange-trans.arr.button-icon.hidden}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/clinical/models/sbiobertresolve_atc_en_6.4.1_3.4_1785443296843.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
  
```python

document_assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")

sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = Tokenizer().setInputCols(["sentence"]).setOutputCol("token")

word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

atc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_atc", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("atc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, sbert_embedder, atc_resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```

{:.jsl-block}
```python

document_assembler = nlp.DocumentAssembler().setInputCol("text").setOutputCol("document")

sentenceDetectorDL = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")\
    .setInputCols(["document"])\
    .setOutputCol("sentence")

tokenizer = nlp.Tokenizer().setInputCols(["sentence"]).setOutputCol("token")

word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")\
    .setInputCols(["sentence", "token"])\
    .setOutputCol("word_embeddings")

posology_ner = medical.NerModel.pretrained("ner_posology", "en", "clinical/models")\
    .setInputCols(["sentence", "token", "word_embeddings"])\
    .setOutputCol("ner")

ner_converter = medical.NerConverterInternal()\
    .setInputCols(["sentence", "token", "ner"])\
    .setOutputCol("ner_chunk")\
    .setWhiteList(["DRUG"])

c2doc = nlp.Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

sbert_embedder = nlp.BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en", "clinical/models")\
    .setInputCols(["ner_chunk_doc"])\
    .setOutputCol("sentence_embeddings")\
    .setCaseSensitive(False)

atc_resolver = medical.SentenceEntityResolverModel.pretrained("sbiobertresolve_atc", "en", "clinical/models")\
    .setInputCols(["sentence_embeddings"])\
    .setOutputCol("atc_code")\
    .setDistanceFunction("EUCLIDEAN")

resolver_pipeline = nlp.Pipeline(stages=[
    document_assembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, sbert_embedder, atc_resolver
])

data = spark.createDataFrame([["The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection."]]).toDF("text")
result = resolver_pipeline.fit(data).transform(data)

```
```scala

val documentAssembler = new DocumentAssembler().setInputCol("text").setOutputCol("document")

val sentenceDetectorDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en", "clinical/models")
    .setInputCols(Array("document"))
    .setOutputCol("sentence")

val tokenizer = new Tokenizer().setInputCols("sentence").setOutputCol("token")

val word_embeddings = WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models")
    .setInputCols(Array("sentence", "token"))
    .setOutputCol("word_embeddings")

val posology_ner = MedicalNerModel.pretrained("ner_posology", "en", "clinical/models")
    .setInputCols(Array("sentence", "token", "word_embeddings"))
    .setOutputCol("ner")

val ner_converter = new NerConverterInternal()
    .setInputCols(Array("sentence", "token", "ner"))
    .setOutputCol("ner_chunk")
    .setWhiteList(Array("DRUG"))

val c2doc = new Chunk2Doc().setInputCols("ner_chunk").setOutputCol("ner_chunk_doc")

val sbert_embedder = BertSentenceEmbeddings.pretrained("sbiobert_base_cased_mli_onnx", "en","clinical/models")
    .setInputCols(Array("ner_chunk_doc"))
    .setOutputCol("sentence_embeddings")
    .setCaseSensitive(false)

val atc_resolver = SentenceEntityResolverModel.pretrained("sbiobertresolve_atc", "en", "clinical/models")
    .setInputCols(Array("sentence_embeddings"))
    .setOutputCol("atc_code")
    .setDistanceFunction("EUCLIDEAN")

val resolver_pipeline = new Pipeline().setStages(Array(
    documentAssembler, sentenceDetectorDL, tokenizer, word_embeddings,
    posology_ner, ner_converter, c2doc, sbert_embedder, atc_resolver
))

val data = Seq("The patient was started on metformin 500 mg twice daily for type 2 diabetes and was also prescribed atorvastatin for hyperlipidemia. She was given amoxicillin for a sinus infection.").toDF("text")
val result = resolver_pipeline.fit(data).transform(data)

```
</div>

## Results

```bash
| ner_chunk    | entity   | atc_code   | resolution   | all_k_results                                                                       | all_k_distances                                                                     | all_k_cosine_distances                                                              | all_k_resolutions                                                                   | all_k_aux_labels                                                                    |
|:-------------|:---------|:-----------|:-------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| metformin    | DRUG     | A10BA02    | metformin    | A10BA02:::A10BA01:::A10BB01:::A10BD17:::A10BD02:::A10BH04:::A10BD13:::J05AA01:::... | 0.0000:::8.3109:::8.5307:::8.6477:::8.8556:::8.9024:::9.3279:::9.3832:::9.4126::... | 0.0000:::0.1134:::0.1192:::0.1236:::0.1274:::0.1309:::0.1439:::0.1445:::0.1451::... | metformin:::phenformin :::glyburide / metformin :::metformin and acarbose:::metf... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| atorvastatin | DRUG     | C10AA05    | atorvastatin | C10AA05:::C10AA07:::C10AA06:::C10BX08:::C10AA03:::C10AA04:::C10BX15:::C10AA02:::... | 0.0000:::6.1618:::6.2856:::7.4259:::7.4874:::7.5918:::7.6736:::7.7381:::8.0282::... | 0.0000:::0.0667:::0.0695:::0.1002:::0.0980:::0.1013:::0.1076:::0.1058:::0.1183::... | atorvastatin :::rosuvastatin :::cerivastatin :::atorvastatin and acetylsalicylic... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
| amoxicillin  | DRUG     | J01CA04    | amoxicillin  | J01CA04:::S01AA19:::J01CA01:::J01CF02:::J01CF01:::J01CF05:::J01CA19:::J01CA51:::... | 0.0000:::6.9141:::6.9141:::7.4772:::7.6220:::7.6735:::7.8381:::7.8753:::7.8847      | 0.0000:::0.0820:::0.0820:::0.0967:::0.1006:::0.1002:::0.1101:::0.1082:::0.1119      | amoxicillin:::ampicillin:::ampicillin :::cloxacillin :::dicloxacillin :::fluclox... | ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::ATC 5th:::... |
```

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sbiobertresolve_atc|
|Compatibility:|Healthcare NLP 6.4.1+|
|License:|Licensed|
|Edition:|Official|
|Input Labels:|[sentence_embeddings]|
|Output Labels:|[atc_code]|
|Language:|en|
|Size:|110.1 MB|
|Case sensitive:|false|
